在 JavaScript 中，函数是一个**值**：你可以把它存入变量、放进数组，也可以把它作为参数传给另一个函数。接收函数作为参数、或者返回一个函数的函数，称为**高阶函数**。被传入的函数称为**回调**，因为接收方在需要时会*回过头来调用它*：
```javascript
function shout(text) {
  return text.toUpperCase() + "!";
}
function twice(fn, value) {
  return fn(fn(value));
}
console.log(twice(shout, "hi"));
// prints HI!!
```
注意 `shout` 是**不带括号**传入的：`twice(shout, "hi")` 交出的是函数本身，而 `twice(shout("hi"), "hi")` 会先调用 `shout` 并传入它的结果，即字符串 `"HI!"`，而字符串是不能被调用的。

---

高阶函数让你把*对每个元素做什么*与*如何遍历这些元素*分开。遍历的部分只写一次，其余的由回调决定：
```javascript
function each(items, action) {
  for (let i = 0; i < items.length; i++) {
    action(items[i]);
  }
}
each(["a", "b"], (letter) => console.log(letter));
// prints a and b on two lines
```
回调每次接收一个元素。它可以像上面那样内联写成箭头函数，也可以是存在变量里的任何函数。接下来你会遇到的内置数组方法，内部正是这样工作的。

---

内置的 `map` 做的正是 `transform` 做的事：它为每个元素调用回调，并把结果收集到一个**新数组**中。`forEach` 也会为每个元素调用回调，但它什么都不收集，并且总是返回 `undefined`；只在需要副作用时使用它，比如打印：
```javascript
const prices = [5, 10];
const doubled = prices.map((p) => p * 2);
prices.forEach((p) => console.log(p));
// prints 5 and 10 on two lines
console.log(doubled);
// prints [ 10, 20 ]
```
一个常见错误是保存 `forEach` 的结果，或者在它后面继续链式调用其他方法：没有东西可以链式调用，因为它返回 `undefined`。经验法则：需要新值时用 `map`，只需要*做*某件事时用 `forEach`。

---

另外两个高阶方法覆盖了大部分日常需求。
`filter(callback)` 返回一个新数组，只包含回调返回 `true` 的元素；这种回答是或否的回调称为**谓词**。
`reduce(callback, initialValue)` 把所有元素合并成一个值：回调接收**累加器**（到目前为止的结果）和当前元素，并返回新的累加器。`reduce` 的第二个参数是累加器的初始值：
```javascript
const numbers = [3, 8, 5];
console.log(numbers.filter((n) => n > 4));
// prints [ 8, 5 ]
console.log(numbers.reduce((sum, n) => sum + n, 0));
// prints 16
```
因为 `filter` 和 `map` 都返回数组，你可以把它们链起来，并以 `reduce` 收尾：`numbers.filter(...).map(...).reduce(...)`。

---

有三个方法用谓词来回答关于数组的问题：
- `find(predicate)` 返回谓词为 `true` 的**第一个**元素，如果没有则返回 `undefined`
- `some(predicate)` 在**至少有一个**元素满足谓词时返回 `true`
- `every(predicate)` 在**所有**元素都满足时返回 `true`（空数组也返回 `true`）
```javascript
const scores = [72, 45, 90];
console.log(scores.find((s) => s < 60));
// prints 45
console.log(scores.some((s) => s === 90), scores.every((s) => s >= 60));
// prints true false
```
三者一旦得出答案就会停止，因此绝不会检查多于必要数量的元素。

---

`sort(compare)` 使用一个回调**就地**排序数组，该回调接收两个元素：当第一个应排在前面时返回负数，当第二个应排在前面时返回正数，相等时返回 `0`。对数字来说，`(a, b) => a - b` 升序排序，`(a, b) => b - a` 降序排序。
没有比较函数时，`sort()` 会把每个元素转换成**字符串**并逐字符比较，所以 `10` 排在 `9` 前面，因为 `"1"` 小于 `"9"`：
```javascript
console.log([10, 9, 1].sort());
// prints [ 1, 10, 9 ]
console.log([10, 9, 1].sort((a, b) => a - b));
// prints [ 1, 9, 10 ]
```
因为 `sort` 会修改数组，当你还需要原始顺序时请排序一个副本：`[...numbers].sort(...)`。对字符串使用 `(a, b) => a.localeCompare(b)` 作为比较函数，它会按字母顺序排列文本。

---

比较函数可以查看元素的任何部分，因此只要比较某个属性，就能按该属性排序一个对象数组：
```javascript
const items = [{ name: "b", size: 3 }, { name: "a", size: 1 }];
const bySize = [...items].sort((x, y) => x.size - y.size);
console.log(bySize.map((item) => item.name));
// prints [ 'a', 'b' ]
```
排序副本使 `items` 保持其原始顺序。

---

高阶函数也可以**返回**一个函数。返回的函数会记住它被创建之处的变量，即使外层函数已经结束：这称为**闭包**。
```javascript
function makeMultiplier(factor) {
  return function (n) {
    return n * factor;
  };
}
const triple = makeMultiplier(3);
console.log(triple(5));
// prints 15
console.log(makeMultiplier(10)(5));
// prints 50
```
每次调用 `makeMultiplier` 都会创建一个拥有自己 `factor` 的新函数。这就是从一个模板构建一族相似函数的方法。同样的写法也可以用箭头函数：`const makeMultiplier = (factor) => (n) => n * factor;`。

---

闭包保留的是与变量的**实时**关联，而不是它的值的副本。当在同一次调用中创建多个函数时，它们共享同一个变量，通过其中一个所做的任何修改，其他函数都能看到：
```javascript
function makeCounter() {
  let count = 0;
  return {
    increment: () => { count += 1; },
    value: () => count,
  };
}
const counter = makeCounter();
counter.increment();
counter.increment();
console.log(counter.value());
// prints 2
```
除了通过这两个函数，外部没有人能读取或重置 `count`：这个变量是**私有的**。再次调用 `makeCounter()` 会创建一个完全独立的 `count`。

---

因为函数是值，你可以写一个高阶函数把两个函数**组合**成一个新函数。`compose(f, g)` 返回一个函数，它先应用 `g`，再把 `f` 应用到结果上，对应数学记号 *f(g(x))*：
```javascript
const compose = (f, g) => (x) => f(g(x));
const trim = (s) => s.trim();
const shout = (s) => s.toUpperCase();
const clean = compose(shout, trim);
console.log(clean("  hi  "));
// prints HI
```
顺序很重要：`compose(f, g)` 先运行 `g`，再运行 `f`。用这种方式把小函数粘合起来构建程序，称为**函数组合**。

---

返回函数的函数也是**适配**回调的自然方式。假设你有一个谓词，而 `filter` 需要它的相反版本：不必重写它，把它包装起来就行：
```javascript
const isLong = (word) => word.length > 4;
const isShort = (word) => !isLong(word);
console.log(["tree", "forest"].filter(isShort));
// prints [ 'tree' ]
```
通用的 `not(predicate)` 可以对任何谓词做这件事：它返回一个新函数，用同样的参数调用 `predicate`，并用 `!` 取反结果。`filter`、`find`、`some` 和 `every` 的谓词都把元素作为第一个参数，所以包装器只需要转发这一个值。

---

`reduce` 的累加器不一定是数字：它可以是字符串、数组或对象。从空对象 `{}` 开始，你可以一次遍历就完成计数或分组。记得从回调中**返回累加器**，否则下一步会收到 `undefined`：
```javascript
const votes = ["yes", "no", "yes"];
const tally = votes.reduce((acc, vote) => {
  acc[vote] = (acc[vote] ?? 0) + 1;
  return acc;
}, {});
console.log(tally);
// prints { yes: 2, no: 1 }
```
`acc[vote] ?? 0` 读取当前计数，当该键还不存在时读取到 `0`。

---

每个函数都有一个 `bind` 方法，它返回一个预先固定了某些内容的**新**函数。它的第一个参数会成为新函数的 `this`；其余参数会被放在调用新函数时所传参数的前面（一种**部分应用**）：
```javascript
function multiply(a, b) {
  return a * b;
}
const double = multiply.bind(null, 2);
console.log(double(21));
// prints 42
```
固定 `this` 对方法很重要。当一个方法被从它的对象中取出并单独调用时，`this` 不再指向该对象，于是 `this.name` 变成 `undefined`。`bind` 会把它锁定到该对象上：
```javascript
const user = {
  name: "Ana",
  hello() { return `Hi ${this.name}`; },
};
const loose = user.hello;
console.log(loose());
// prints Hi undefined
const bound = user.hello.bind(user);
console.log(bound());
// prints Hi Ana
```
原函数永远不会被改变：`bind` 总是构建一个新函数，它的 `name` 是原名称加上前缀 `bound `。

---

真实的程序会把这些方法组合成**管道**：筛选出你关心的元素，把它们映射成你需要的值，再把它们归约成一个结果。把中间数组存入常量能让每一步保持清晰，也便于复用：
```javascript
const adults = people.filter((p) => p.age >= 18);
const names = adults.map((p) => p.name);
const totalAge = adults.reduce((sum, p) => sum + p.age, 0);
```
`names.join(", ")` 把字符串数组变成一个字符串，元素之间用逗号加空格分隔。

---

闭包让返回的函数能在多次调用之间保持**私有状态**。用这种方式构建的经典助手是 `once(fn)`：它返回一个函数，只在第一次被调用时运行 `fn`，记住结果，并在之后每次调用时返回同一个结果而不再运行 `fn`：
```javascript
let calls = 0;
const init = once(() => {
  calls += 1;
  return "ready";
});
console.log(init(), init(), calls);
// prints ready ready 1
```
包装器需要两个私有变量：`fn` 是否已经运行过，以及保存下来的结果。两者都存在于闭包中，对外部不可见。要把包装器的所有参数转发给 `fn`，用剩余参数 `(...args)` 声明包装器，并调用 `fn(...args)`。

---

一切都汇集到 `groupBy(items, keyFn)`：这是一个高阶函数，它接收一个决定每个元素**分组键**的回调，并返回一个把每个键映射到具有该键的元素数组的对象。用对象作累加器的 `reduce` 就能完成全部工作：
```javascript
const byInitial = groupBy(["hi", "yo", "hey"], (w) => w[0]);
console.log(byInitial);
// prints { h: [ 'hi', 'hey' ], y: [ 'yo' ] }
```
对每个元素，先计算键，如果该键的数组还不存在就创建它（`acc[key] ?? []`），把元素放进去，然后返回累加器。因为 `keyFn` 由调用方选择，同一个函数既能按首字母给单词分组，也能按城市给人分组，或按奇偶给数字分组。
