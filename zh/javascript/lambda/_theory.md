函数不一定需要名字。**函数表达式**会把函数创建为一个值，你可以把它存储在变量中，并通过该变量来调用：
```javascript
const add = function (a, b) {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
**箭头函数**是写同样内容的更简短方式：去掉 `function` 关键字，在参数列表和函数体之间放上一个胖箭头 `=>`：
```javascript
const add = (a, b) => {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
箭头函数通常存储在 `const` 中，这样名字就不会被误重新赋值，而且它的调用方式与其他任何函数完全相同。

---

在两种常见情况下，箭头函数可以写得更短。
当函数体是一个**单一表达式**时，你可以省略花括号和 `return` 关键字：表达式的值会被自动返回（即**隐式返回**）：
```javascript
const add = (a, b) => a + b;
console.log(add(2, 3));
// prints 5
```
当**恰好只有一个参数**时，你还可以省略它两侧的圆括号：
```javascript
const double = n => n * 2;
console.log(double(4));
// prints 8
```
当没有参数或有两个及以上参数时，圆括号则是必需的：`() => 42` 和 `(a, b) => a + b`。

---

隐式返回有一个陷阱。当箭头函数的函数体以 `{` 开头时，它会被解读为**块级函数体**，而绝不会是对象字面量：
```javascript
const make = (name) => { name: name };
console.log(make("Ana"));
// prints undefined
```
这里 `{ name: name }` 是一个块，其中包含标签 `name:`，后面跟着表达式 `name`。没有返回任何东西，所以调用结果是 `undefined`。
要在同一行返回对象字面量，请用**圆括号**把它包裹起来，让 JavaScript 将其视为表达式：
```javascript
const make = (name) => ({ name: name });
console.log(make("Ana"));
// prints { name: 'Ana' }
```

---

用圆括号包裹对象字面量是使用单行箭头函数构建对象的标准方式，例如当你把几个值变成一条记录时：
```javascript
const user = (name, age) => ({ name: name, age: age });
console.log(user("Ana", 30).age);
// prints 30
```
没有参数的箭头函数以一对空圆括号 `()` 开头：
```javascript
const empty = () => ({});
console.log(empty());
// prints {}
```

---

箭头函数作为**回调**时真正大放异彩：回调是作为实参传递给其他函数的函数。数组方法就是最常见的例子。
`map(callback)` 返回一个新数组，其中包含回调对每个元素的处理结果，而 `filter(callback)` 返回一个新数组，只包含回调对其返回 `true` 的那些元素：
```javascript
const numbers = [1, 2, 3, 4];
console.log(numbers.map((n) => n * 10));
// prints [ 10, 20, 30, 40 ]
console.log(numbers.filter((n) => n > 2));
// prints [ 3, 4 ]
```
两者都返回新数组且不修改原数组，因此你可以将它们链式调用：`numbers.filter(...).map(...)`。

---

还有两个数组方法需要传入回调。
`forEach(callback)` 对每个元素调用一次回调且不返回任何东西；可以用它来执行打印这类副作用操作。
`reduce(callback, initialValue)` 把数组折叠成单个值：回调接收到目前为止的累积值和当前元素，并返回新的累积值：
```javascript
const numbers = [1, 2, 3];
numbers.forEach((n) => console.log(n));
// prints 1, 2 and 3 on three lines
const total = numbers.reduce((sum, n) => sum + n, 0);
console.log(total);
// prints 6
```

---

`sort(compare)` 使用一个回调对数组进行就地排序：回调接收两个元素，当第一个元素应排在前面时返回负数，当第二个元素应排在前面时返回正数，两者相等时返回 `0`。对于数字，`(a, b) => a - b` 按升序排序，`(a, b) => b - a` 按降序排序。
`find(callback)` 返回第一个使回调返回 `true` 的元素，如果没有这样的元素则返回 `undefined`：
```javascript
const scores = [50, 90, 70];
scores.sort((a, b) => a - b);
console.log(scores);
// prints [ 50, 70, 90 ]
console.log(scores.find((s) => s > 60));
// prints 70
```

---

箭头函数的参数支持与普通函数参数相同的特性。
当实参被省略或为 `undefined` 时，会使用**默认值**：
```javascript
const greet = (name = "World") => `Hello, ${name}!`;
console.log(greet());
// prints Hello, World!
console.log(greet("Ana"));
// prints Hello, Ana!
```
注意，带默认值的参数总是需要圆括号，即使它是唯一的参数：`name = "World" => ...` 是一个语法错误。

---

**剩余参数** `...name` 会把任意数量的实参收集到一个数组中，它在箭头函数中同样可用：
```javascript
const count = (...items) => items.length;
console.log(count("a", "b", "c"));
// prints 3
```
普通函数还有一个隐藏的类数组 `arguments` 对象，保存着它们接收到的每个实参。箭头函数则**没有**：在箭头函数内部，`arguments` 指向外围函数的 `arguments`，或者根本不存在。每当你在箭头函数中需要所有实参时，请使用剩余参数。

---

函数会记住它被**创建**时所处作用域中的变量，即使那个作用域已经运行结束。这被称为**闭包**。
经典的例子是计数器工厂：每次调用 `makeCounter` 都会创建一个全新的 `count`，并返回一个持续使用同一个 `count` 的箭头函数：
```javascript
const makeCounter = () => {
  let count = 0;
  return () => {
    count += 1;
    return count;
  };
};
const next = makeCounter();
console.log(next());
// prints 1
console.log(next());
// prints 2
```
其他任何人都无法读取或重置 `count`：它只存在于返回的函数内部。再次调用 `makeCounter()` 会创建一个独立的计数器，它拥有自己的 `count`。

---

因为函数是一个值，箭头函数可以**返回另一个箭头函数**。把两个箭头链在一起是编写构建函数的函数的一种紧凑方式：
```javascript
const makeAdder = (amount) => (n) => n + amount;
const addTen = makeAdder(10);
console.log(addTen(5));
// prints 15
console.log(makeAdder(1)(5));
// prints 6
```
从左往右阅读：`makeAdder` 接收 `amount` 并返回 `(n) => n + amount`，这是一个通过闭包捕获 `amount` 的箭头函数。`makeAdder(1)(5)` 会立即调用返回的函数。
