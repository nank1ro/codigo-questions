有些操作不会立即完成：下载文件、读取数据库、等待计时器。JavaScript 在它们运行时并不会卡住，而是交给你一个 **`Promise`**：一个代表某个**稍后**才可用的值的对象。

标记为 **`async`** 的函数总是返回一个 promise。函数返回什么，什么就成为该 promise 内部的值：
```javascript
async function fetchNumber() {
  return 42;
}
```
要把值从 promise 中取出来，你要使用 **`await`**。它会暂停这个函数，直到 promise 拿到了自己的值，然后给你这个普通的值。`await` 只允许在 `async` 函数内部使用：
```javascript
async function main() {
  const n = await fetchNumber();
  console.log(n);
  // prints 42
}

main();
```
如果没有 `await`，`n` 就会是 promise 本身，`console.log(n)` 打印的将是 `Promise { 42 }` 而不是这个数字。

---

在函数前面加上 `async` 会改变它交回的东西：函数体仍然计算出一个普通的值，但调用者收到的是包裹着它的一个 promise。
```javascript
function shout(text) {
  return text.toUpperCase();
}
async function shoutLater(text) {
  return text.toUpperCase();
}

console.log(shout("hi"));
// prints HI
console.log(shoutLater("hi"));
// prints Promise { 'HI' }
```
这两个函数包含相同的代码；不同的只是读取结果的方式。`shoutLater("hi")` 必须在另一个 `async` 函数中被 await，才能得到 `"HI"`。

在没有等待要做时，把函数标记为 `async` 没有任何代价，而且正是它让你以后能在函数内部使用 `await`。

---

当值真的稍后才到达时，你要用 **`new Promise`** 自己构建 promise。它接收一个函数，该函数会得到一个 **`resolve`** 回调：在值就绪时调用 `resolve(value)`，promise 就会以这个值兑现。
```javascript
const soon = new Promise((resolve) => {
  setTimeout(() => resolve("done"), 1000);
});
```
`setTimeout(callback, ms)` 安排 `callback` 在 `ms` 毫秒后运行并立即返回，所以在此期间什么都不会被阻塞。

传给 `new Promise` 的函数会立刻运行，但在 `resolve` 被调用之前，promise 会一直保持**待定**状态。await 它就能得到值：
```javascript
async function main() {
  console.log(await soon);
  // prints done, about one second later
}

main();
```

---

promise 总是处于三种状态之一：

- **待定**（pending）：工作仍在进行；
- **已兑现**（fulfilled）：工作成功，promise 中持有一个值；
- **已拒绝**（rejected）：工作失败，promise 中持有一个错误。

promise 从待定开始，并且最多改变一次状态。一旦兑现或拒绝，它就是**已定型**（settled）的，再也不会改变。

调用 `async` 函数从不等待：它会启动工作并立即交给你一个待定的 promise，所以调用之后的下一行会在工作完成之前运行。那个 promise 是一个普通的对象，而不是它内部的值，这就是为什么忘记 `await` 是一个如此常见的错误。

---

`await` 不是读取 promise 的唯一方式。每个 promise 都有一个 **`.then(callback)`** 方法：一旦 promise 兑现，回调就会收到这个值。
```javascript
Promise.resolve(21).then((n) => {
  console.log(n);
  // prints 21
});
```
**`Promise.resolve(value)`** 构建一个已经以 `value` 兑现的 promise，当你手头就有这个值但必须返回一个 promise 时，它非常方便。

.then 返回一个以回调返回的任何内容兑现的**新** promise，因此调用可以**链式**进行，每一步都处理上一步的结果：
```javascript
Promise.resolve(21)
  .then((n) => n * 2)
  .then((n) => console.log(n));
// prints 42
```

---

`async` 函数和其他函数一样自上而下阅读：`await` 只是把它暂停，直到被 await 的 promise 兑现，然后执行继续到下一行。
```javascript
async function main() {
  console.log("start");
  const value = await Promise.resolve("data");
  console.log(value);
  console.log("done");
}

main();
// prints start, then data, then done
```
注意最后一行：`async` 函数仍然必须被**调用**。写 `main` 而不带括号只是定义了工作但从不启动它，什么都不会打印。

---

异步工作也可能失败。传给 `new Promise` 的函数会收到第二个回调 **`reject`**：调用 `reject(error)`，promise 就会变成已拒绝而不是已兑现。
```javascript
function readAge(age) {
  return new Promise((resolve, reject) => {
    if (age >= 0) {
      resolve(age);
    } else {
      reject(new Error("negative age"));
    }
  });
}
```
总是用 `Error` 对象来拒绝：它带有 `message` 和堆栈跟踪，而裸字符串没有这些。

拒绝通过 **`.catch(callback)`** 读取，它是 `.then` 的镜像。**`Promise.reject(error)`** 构建一个已经被拒绝的 promise，就像 `Promise.resolve` 构建一个已兑现的 promise 一样：
```javascript
readAge(-1).catch((error) => {
  console.log(error.message);
  // prints negative age
});
```
既调用 `resolve` 又调用 `reject`，或者调用两次，都不会有任何改变：只有第一次调用有效。

---

`.then`、`.catch` 和 `.finally` 是同一条链上的环节。拒绝会跳过每一个 `.then`，直到遇到一个 `.catch`；一旦 `.catch` 回调返回了一个值，链就重新兑现并继续正常运行。

**`.finally(callback)`** 在链定型时运行，无论它是兑现还是被拒绝。它的回调不接收参数，其返回值会被忽略，因此值会继续流向下一个 `.then`。它是进行清理工作的位置，比如隐藏加载指示器：
```javascript
Promise.reject(new Error("no network"))
  .then((value) => `ok: ${value}`)
  .catch((error) => `error: ${error.message}`)
  .finally(() => console.log("cleanup"))
  .then((message) => console.log(message));
// prints cleanup, then error: no network
```

---

在 `async` 函数内部，你不需要 `.catch`。await 一个被拒绝的 promise 会**抛出**这个错误，因此普通的 `try` / `catch` / `finally` 语句就能处理它：
```javascript
async function main() {
  try {
    const data = await load();
    console.log(data);
  } catch (error) {
    console.log(`failed: ${error.message}`);
  } finally {
    console.log("end");
  }
}
```
反方向也成立：`async` 函数内部的 `throw` 不会让调用者崩溃，而是拒绝该函数返回的 promise。
```javascript
async function risky() {
  throw new Error("boom");
}
// risky() returns a promise rejected with Error("boom")
```
与任何 `try` 块一样，失败的 `await` 之后的行会被跳过，`catch` 块会运行，而 `finally` 块在两种情况下都会运行。

---

在 `await` 周围使用 `try` / `catch` 的一个常见用途，是用一个合理的默认值替换失败，这样调用者永远不必处理这个错误：
```javascript
async function sizeOf(path) {
  try {
    return await measure(path);
  } catch (error) {
    return 0;
  }
}
```
即使在值被立即返回时，也要保留 `measure(path)` 前面的 `await`。没有它，promise 会直接离开函数而从不经过 `try` 块，拒绝就会逃过 `catch`。

---

当需要多个结果时，一个接一个地 await 它们会浪费时间：每一个只有在前一个完成后才会开始。**`Promise.all(promises)`** 接收一个已经在运行的 promise 组成的数组，并返回一个以包含它们所有值的数组兑现的单一 promise：
```javascript
const results = await Promise.all([fetchUser(), fetchOrders()]);
```
有两条规则值得记住：

- 值**按数组的顺序**返回，而不是按它们完成的顺序；
- 如果任何一个 promise 被拒绝，`Promise.all` 返回的 promise 会立即以那个第一个错误拒绝，其他值都会丢失。

---

`Promise.all` 可以处理任意长度的数组，包括空数组：await `Promise.all([])` 会立即返回一个空数组。这使得传递一个在运行时构建的列表也很安全，不需要为"没有要等待的东西"写特殊情况。
```javascript
const values = await Promise.all(items);
console.log(values.length === items.length);
// prints true
```
它返回的数组总是恰好拥有与它接收到的数组一样多的条目，并且位于相同的位置上，因此可以像任何其他数组一样对它进行循环。

---

**顺序**等待与**并行**等待的区别取决于你把 `await` 放在*哪里*：
```javascript
// sequential: about 300 + 300 = 600 ms
const a = await load("a");
const b = await load("b");

// parallel: about 300 ms
const [a, b] = await Promise.all([load("a"), load("b")]);
```
在第一种版本中，第二次下载只有等第一次完成后才会开始，因为 `await` 在那一行暂停了函数。在第二种版本中，两个调用都在任何 await 之前发出，所以当 `Promise.all` 等待时，两个下载都已经在运行。

只有当第二个任务确实需要第一个任务的结果时，才使用顺序的 await。否则先启动所有任务，再一起 await。

---

`Promise.all` 会在一个 promise 被拒绝时立刻放弃。当你无论如何都想要每一个结果时，使用 **`Promise.allSettled(promises)`**：它永远不会被拒绝，并且以每个 promise 一个小对象兑现，顺序相同：

- 成功的那些是 `{ status: "fulfilled", value: ... }`；
- 失败的那些是 `{ status: "rejected", reason: ... }`。

```javascript
const results = await Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("nope")),
]);
console.log(results[0].status);
// prints fulfilled
console.log(results[1].reason.message);
// prints nope
```
只有当 `status` 是 `"fulfilled"` 时才读取 `value`，只有当它是 `"rejected"` 时才读取 `reason`：另一个属性根本不存在。

---

**`Promise.race(promises)`** 会在**第一个** promise 定型时立刻定型，并复制它的结果：以第一个值兑现，或以第一个错误拒绝。其余的不会被取消，它们继续运行，但无论产生什么都会被忽略。
```javascript
const winner = await Promise.race([slowServer(), fastServer()]);
```
典型的用途是截止时间：让真正的工作与一个过一会儿就失败的 promise 竞争，你要么得到结果，要么得到一个超时错误。

要小心空数组：`Promise.race([])` 会永远保持待定，因为没有任何东西能使它定型。

---

把最后几块拼在一起，就得到一个几乎每个真实应用都会用到的小工具：截止时间。构建一个在 `ms` 毫秒后被拒绝的 promise，让它与真正的工作竞争，先定型的那个决定结果：
```javascript
const timer = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("timeout")), ms);
});
return Promise.race([work, timer]);
```
从 `async` 函数返回一个 promise 是没有问题的：函数交回的 promise 会跟随它，所以调用者 await 到的是最终的值，而不是 promise 的 promise。
