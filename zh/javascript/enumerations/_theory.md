**枚举**（或 *enum*）是一种用于表示一小组相关的固定值的通用类型：一周的天数、一副牌的花色、订单的可能状态。
与许多语言不同，JavaScript **没有** `enum` 关键字。惯用的替代方案是一个普通对象，它的属性即为成员，并传入 `Object.freeze()`，这样就没有人能在之后修改它：
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// prints red
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
// prints done
```
一旦被冻结，该对象也无法再获得新的属性，`Object.isFrozen(obj)` 可以告诉你一个对象是否已被冻结：
```javascript
console.log(Object.isFrozen(Status));
// prints true
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
// prints s
console.log(Size.MEDIUM);
// prints undefined
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
// prints true
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
// prints [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// prints [ 'red', 'blue' ]
```
将 `Object.values()` 与数组方法 `includes()` 结合使用，是检查任意值（例如从用户输入中读取的值）是否为有效成员的标准方式：
```javascript
console.log(Object.values(Color).includes("red"));
// prints true
console.log(Object.values(Color).includes("pink"));
// prints false
```
