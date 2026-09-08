JavaScript 有两种不同的方式来表示"这里没有值"。
`undefined` 表示一个值**从未被提供**。声明时没有赋值的变量持有 `undefined`，对象中不存在的属性也是如此：
```javascript
let city;
console.log(city);
// prints undefined
const user = { name: "Ana" };
console.log(user.age);
// prints undefined
```
`null` 是**你**有意赋的一个值，用来表示"它是空的，而且我知道"：
```javascript
let owner = null;
console.log(owner);
// prints null
```
所以 `undefined` 通常是语言在告诉你缺少了什么，而 `null` 是程序员在声明某处是有意为空的。

---

还有两种情况会让函数产生 `undefined`。
当你调用函数时传入的**实参数量少于**它声明的形参数量，缺失的参数会持有 `undefined`：
```javascript
function greet(name) {
  console.log(name);
}
greet();
// prints undefined
```
当函数**没有 `return`** 就结束（或者只有单独的 `return;`）时，调用它会得到 `undefined`：
```javascript
function log(message) {
  console.log(message);
}
const result = log("hi");
console.log(result);
// prints hi, then undefined
```
注意，显式传入 `null` 与省略实参并不相同：`greet(null)` 打印 `null`，因为 `null` 是一个真正传递给函数的值。

---

`typeof` 运算符以字符串形式返回值的类型。对于 `undefined`，它如你所愿地回答 `"undefined"`：
```javascript
let city;
console.log(typeof city);
// prints undefined
```
然而对于 `null`，它回答的是 `"object"`。这是 JavaScript 第一个版本就存在且从未被修复的 bug，因为有太多代码依赖它：
```javascript
console.log(typeof null);
// prints object
```
所以 `typeof` 是检测 `undefined` 的可靠方式，但不适用于 `null`。要检查 `null`，直接与它比较即可：`value === null`。

---

`null` 和 `undefined` 相互比较时结果如何？这取决于运算符。
**宽松**相等 `==` 把它们视为同一种东西，并认为它们与任何其他值都不同，包括 `0`、`""` 和 `false`：
```javascript
console.log(null == undefined);
// prints true
console.log(null == 0, undefined == "");
// prints false false
```
**严格**相等 `===` 还会比较类型，而 `null` 和 `undefined` 的类型不同：
```javascript
console.log(null === undefined);
// prints false
console.log(null === null);
// prints true
```

---

大多数时候你并不关心得到的是两个"无值"标记中的*哪一个*：你只想知道值是否存在。
由于 `null == undefined` 是 `true`，且没有其他值与 `null` 宽松相等，比较 `value == null` 就是一次捕获**两者**的标准惯用法：
```javascript
function show(value) {
  if (value == null) {
    return "missing";
  }
  return "present";
}
console.log(show(null), show(undefined));
// prints missing missing
console.log(show(0), show(""));
// prints present present
```
这是唯一一个 `==` 比 `===` 更受青睐的场景：写 `value === null || value === undefined` 做的事完全一样，只是更长。
`0`、`""` 和 `false` 这样的值*不是* `null`：它们是恰好为假值的真实值。

---

读取 `null` 或 `undefined` 的属性是一个会中止程序的错误：
```javascript
const user = { name: "Ana" };
console.log(user.address.city);
// TypeError: Cannot read properties of undefined (reading 'city')
```
`user.address` 是 `undefined`，而 `undefined` 没有任何属性。**可选链**运算符 `?.` 解决了这个问题：如果它左边的值是 `null` 或 `undefined`，整个表达式会停止求值并得到 `undefined`，而不是抛出错误：
```javascript
console.log(user.address?.city);
// prints undefined
console.log(user.name?.length);
// prints 3
```
当左边确实有值时，`?.` 的行为与普通的 `.` 完全一样。你可以链接多个：只要任何一环缺失，`user.address?.street?.name` 就会返回 `undefined`。

---

可选链并不限于点属性。它还有另外两种形式。
`?.[]` 只在左边有值时才读取一个元素或一个计算出来的键：
```javascript
const post = { tags: ["js", "node"] };
console.log(post.tags?.[0]);
// prints js
const empty = {};
console.log(empty.tags?.[0]);
// prints undefined
```
`?.()` 只在函数存在时才调用它，这对可选的回调非常方便：
```javascript
const task = { name: "build" };
task.onDone?.();
// nothing happens, no error
```
在每种形式中，检查都作用于 `?.` **紧前面**的值：即使 `post` 本身是 `null` 或 `undefined`，`post?.tags?.[0]` 也是安全的。

---

一旦知道一个值可能缺失，你通常希望在它的位置放一个**默认值**。有两个运算符可以做到这一点，它们对什么算"缺失"的判断不同。
只要 `a` 是**假值**，`a || b` 就返回 `b`：不仅是 `null` 和 `undefined`，还有 `0`、`""`、`false` 和 `NaN`。
**空值合并**运算符 `a ?? b` 只在 `a` 是 `null` 或 `undefined` 时才返回 `b`，并保留所有其他值：
```javascript
const count = 0;
console.log(count || 10);
// prints 10
console.log(count ?? 10);
// prints 0
let name;
console.log(name ?? "Guest");
// prints Guest
```
当 `0`、`""` 或 `false` 是必须保留的合法值时使用 `??`，当你确实想替换每一个假值时使用 `||`。

---

一个非常常见的模式是"仅当此属性尚未设置时才填入它"。用 `??` 书写会重复属性名：
```javascript
options.timeout = options.timeout ?? 1000;
```
**空值赋值**运算符 `??=` 一步完成同样的事：只有当左边当前是 `null` 或 `undefined` 时才赋上右边的值，并保持任何其他值不变：
```javascript
const options = { retries: 0 };
options.retries ??= 3;
options.timeout ??= 1000;
console.log(options);
// prints { retries: 0, timeout: 1000 }
```
`retries` 保持为 `0`，因为 `0` 不是空值；`timeout` 原本不存在，所以它获得 `1000`。同样的想法对 `||` 也存在，即 `||=`，它会覆盖每一个假值。

---

**默认参数**在调用者不提供值时给参数一个值。规则很精确：只有当实参是 `undefined` 时才使用默认值，这也包括省略实参。传入 `null` **不会**触发默认值，因为 `null` 是一个值：
```javascript
function repeat(text, times = 2) {
  return text.repeat(times);
}
console.log(repeat("ab"));
// prints abab
console.log(repeat("ab", undefined));
// prints abab
console.log(repeat("ab", null));
// prints an empty string, because null is converted to 0
```
默认参数遵循 `undefined` 规则，而 `??` 同时覆盖 `null` 和 `undefined`：选择与你的函数被调用方式相匹配的那一个。

---

可选链和 `== null` 守卫配合得很好：链在不抛出错误的情况下读取嵌套值，而守卫决定结果缺失时该做什么：
```javascript
function cityOf(user) {
  if (user?.address?.city == null) {
    return "unknown";
  }
  return user.address.city;
}
```
在最后一个 `return` 中，普通的 `.` 是安全的，因为守卫已经证明了每一环都存在。

---

许多内置方法通过返回 `undefined` 来报告"没有找到"。数组方法 `find(callback)` 是典型的例子：它返回第一个使回调为 `true` 的元素，当没有元素匹配时返回 `undefined`：
```javascript
const products = [{ name: "pen", price: 2 }];
const found = products.find((p) => p.name === "ink");
console.log(found);
// prints undefined
```
在这里读取 `found.price` 会抛出错误，所以 `?.` 和 `??` 是 `find` 的天然伙伴：
```javascript
console.log(products.find((p) => p.name === "ink")?.price ?? "no price");
// prints no price
```

---

当对象用 `JSON.stringify()` 转换为 JSON 时，`null` 和 `undefined` 的表现不同。
JSON 有 `null` 值但没有 `undefined`，所以值为 `undefined` 的属性会被直接**省略**，而 `null` 属性会被保留：
```javascript
const user = { name: "Ana", nickname: undefined, email: null };
console.log(JSON.stringify(user));
// prints {"name":"Ana","email":null}
```
在数组内部位置不能消失，所以 `undefined` 在那里会变成 `null`：
```javascript
console.log(JSON.stringify([1, undefined, 3]));
// prints [1,null,3]
```

---

检查 `obj.key === undefined` 无法区分两种情况：属性不存在，或者属性存在但持有值 `undefined`。
`Object.hasOwn(obj, key)` 只回答第一个问题：当对象拥有名为 `key` 的**自有**属性时返回 `true`，无论其值是什么：
```javascript
const config = { debug: undefined };
console.log(config.debug === undefined, config.level === undefined);
// prints true true
console.log(Object.hasOwn(config, "debug"), Object.hasOwn(config, "level"));
// prints true false
```
"自有"意味着声明在对象本身上：像 `toString` 这样的继承成员在每个对象上都可用，但 `Object.hasOwn(config, "toString")` 是 `false`。
