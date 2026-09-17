**枚举**（或 *enum*）是一种用于表示一小组相关的固定值的通用类型：一周的天数、一副牌的花色、订单的可能状态。
与许多语言不同，JavaScript **没有** `enum` 关键字。惯用的替代方案是一个普通对象，它的属性即为成员，并传入 `Object.freeze()`，这样就没有人能在之后修改它：
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// 打印 red
```
按照惯例，该对象使用 `const` 声明，其名称以大写字母开头，成员名称使用 `UPPER_CASE` 书写，与其他常量完全一致。

---

每个成员中存储的值由你决定。**字符串**是最常见的选择，因为它们在打印、记录日志或保存到文件时都是可读的：
```javascript
const Status = Object.freeze({
  ACTIVE: "active",
  DONE: "done",
});
console.log(Status.DONE);
// 打印 done
```
一旦被冻结，该对象也无法再获得新的属性，`Object.isFrozen(obj)` 可以告诉你一个对象是否已被冻结：
```javascript
console.log(Object.isFrozen(Status));
// 打印 true
```

---

为什么要冻结对象呢？被冻结的对象会拒绝任何更改：对现有成员赋值、添加新成员或删除成员都不会产生任何效果。
拒绝的表现方式取决于代码运行的模式：
- 在**非严格模式**（sloppy mode，普通脚本的默认模式）下，赋值会被**静默忽略**
- 在**严格模式**（strict mode，以 `"use strict"` 开头的文件、ES 模块以及类的内部）下，它会**抛出** `TypeError`

```javascript
const Size = Object.freeze({ SMALL: "s", LARGE: "l" });
Size.SMALL = "xs";
Size.MEDIUM = "m";
console.log(Size.SMALL);
// 打印 s
console.log(Size.MEDIUM);
// 打印 undefined
```
无论哪种情况，枚举都会保留你定义的值，这正是一组常量所需要的。

---

成员也可以保存**数字**。当成员具有自然顺序时，数值就很方便，因为可以用常规运算符对它们进行比较：
```javascript
const Priority = Object.freeze({
  LOW: 1,
  MEDIUM: 2,
  HIGH: 3,
});
console.log(Priority.HIGH > Priority.LOW);
// 打印 true
```
代价是可读性：打印 `Priority.HIGH` 只会显示 `3`，比字符串 `"high"` 所传达的信息要少得多。

---

因为枚举只是一个对象，常见的对象工具方法可以用来检查它：
- `Object.keys(Enum)` 返回一个包含成员**名称**的数组
- `Object.values(Enum)` 返回一个包含成员**值**的数组
- `Object.entries(Enum)` 返回一个 `[名称, 值]` 对的数组

```javascript
const Color = Object.freeze({ RED: "red", BLUE: "blue" });
console.log(Object.keys(Color));
// 打印 [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// 打印 [ 'red', 'blue' ]
```
将 `Object.values()` 与数组方法 `includes()` 结合使用，是检查任意值（例如从用户输入中读取的值）是否为有效成员的标准方式：
```javascript
console.log(Object.values(Color).includes("red"));
// 打印 true
console.log(Object.values(Color).includes("pink"));
// 打印 false
```

---

枚举天然地与 `switch` 语句搭配使用，`switch` 会将一个值与一系列 `case` 标签进行比较，并执行第一个匹配项的代码。
每个分支以 `return` 或 `break` 结尾，可选的 `default` 分支会在没有任何匹配时执行：
```javascript
const Light = Object.freeze({ RED: "red", GREEN: "green" });

function action(light) {
  switch (light) {
    case Light.RED:
      return "stop";
    case Light.GREEN:
      return "go";
    default:
      return "unknown";
  }
}
console.log(action(Light.GREEN));
// 打印 go
```
始终与成员（`Light.RED`）进行比较，而不是与原始值（`"red"`）比较：这样即使值发生变化，`switch` 仍能正常工作。

---

从值反过来找到其成员名称，称为**反向查找**。用 `Object.keys()` 遍历名称，并使用数组方法 `find()` 选出第一个值匹配的名称，`find()` 返回第一个使回调函数结果为 `true` 的元素（如果没有则返回 `undefined`）：
```javascript
const Priority = Object.freeze({ LOW: 1, HIGH: 3 });
let name = Object.keys(Priority).find((key) => Priority[key] === 3);
console.log(name);
// 打印 HIGH
```
`Priority[key]` 读取名称存储在变量 `key` 中的那个成员，这与你对任何对象使用的方括号表示法相同。

---

字符串成员有一个弱点：任何具有相同文本的字符串都会被当作该成员接受。
```javascript
const Color = Object.freeze({ RED: "red" });
console.log(Color.RED === "red");
// 打印 true
```
当你想要成员**只**与自身相等时，使用 `Symbol`。`Symbol(description)` 会创建一个全新的值，它与任何其他 symbol 都不同，即使是用相同描述创建的：
```javascript
const Suit = Object.freeze({
  HEARTS: Symbol("hearts"),
  SPADES: Symbol("spades"),
});
console.log(Suit.HEARTS === Suit.HEARTS);
// 打印 true
console.log(Suit.HEARTS === Symbol("hearts"));
// 打印 false
console.log(typeof Suit.HEARTS);
// 打印 symbol
```
你传入的文本只是一个用于调试的标签；你可以通过 `description` 属性读取它（`Suit.HEARTS.description` 是 `"hearts"`）。

---

枚举的值经常被用作另一个对象的**键**，例如将每个成员映射到一个标签或价格。在对象字面量中，把一个键用方括号 `[ ]` 包裹起来会对表达式求值，并将其结果用作键（**计算属性名**）。这对字符串成员和 symbol 成员都适用：
```javascript
const Status = Object.freeze({ ACTIVE: "active", DONE: "done" });
const labels = {
  [Status.ACTIVE]: "In progress",
  [Status.DONE]: "Completed",
};
console.log(labels[Status.DONE]);
// 打印 Completed
```
如果不加方括号，`Status.DONE: "Completed"` 会是语法错误，而 `"Status.DONE"` 只会是一个普通的字符串键。

---

当每个成员都需要多项数据或自己的方法时，**类**可以扮演枚举的角色。每个成员都是该类的一个实例，存储在一个 `static` 属性中，也就是属于类本身而不是属于每个实例的属性：
```javascript
class Planet {
  static MERCURY = new Planet("Mercury", 0.4);
  static EARTH = new Planet("Earth", 1);

  constructor(name, gravity) {
    this.name = name;
    this.gravity = gravity;
  }
}
console.log(Planet.EARTH.name);
// 打印 Earth
```
在类之后调用 `Object.freeze(Planet)`，防止任何人添加或替换成员，并在构造函数中用 `Object.freeze(this)` 冻结每个实例，使成员本身保持只读。
