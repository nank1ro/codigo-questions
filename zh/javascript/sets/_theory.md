**Set** 是**唯一**值的集合：每个值最多只能出现一次，并且没有可以按位置访问值的索引。
当你只关心*哪些*值存在，而不关心出现次数或顺序时，Set 非常合适。
你可以用 `new Set()` 创建一个空的 set，用 `add(value)` 添加一个值，用 `has(value)` 检查某个值是否存在：
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// 打印 true
console.log(colors.has("green"));
// 打印 false
```

---

添加一个已经在 set 中的值不会做**任何事**：重复值会被直接忽略。
还有两个重要的方法/属性：
- `delete(value)` 从 set 中移除该值
- `size` 是存储的值的数量（这是一个属性，所以没有括号）

```javascript
let tags = new Set();
tags.add("js");
tags.add("css");
tags.add("js");
console.log(tags.size);
// 打印 2
tags.delete("css");
console.log(tags.size);
// 打印 1
```

---

`add()` 返回 set 本身，因此可以链式调用多次：
```javascript
let letters = new Set();
letters.add("a").add("b");
```
无论是否链式调用，已经存在的值都不会被再次添加，因此 `size` 只统计每个不同的值一次。

---

你可以通过把一个数组传给 `new Set()` 一次性构建一个 set。数组中的重复值会被丢弃，因此这是找到数组中不同值的最快方式：
```javascript
let nums = [1, 2, 2, 3, 3, 3];
let distinct = new Set(nums);
console.log(distinct.size);
// 打印 3
```
**展开**运算符 `...` 反过来使用，可以把 set 再转换回数组：
```javascript
let unique = [...distinct];
console.log(unique);
// 打印 [ 1, 2, 3 ]
```
`Array.from(distinct)` 的效果是一样的。

---

set 会记住值被添加的顺序，你可以用 `for...of` 遍历它：
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// 打印 3
// 打印 1
// 打印 2
```
set 也有一个 `forEach()` 方法，会为每个值调用一次函数：
```javascript
nums.forEach((n) => console.log(n * 10));
// 打印 30
// 打印 10
// 打印 20
```

---

当值被移除时，`delete(value)` 返回 `true`；当该值不在 set 中时，返回 `false`。
要一次性移除**所有**值，调用 `clear()`：
```javascript
let cart = new Set(["pen", "ink"]);
console.log(cart.delete("pen"));
// 打印 true
console.log(cart.delete("pen"));
// 打印 false
cart.clear();
console.log(cart.size);
// 打印 0
```

---

set 判断两个值是否"相同"的规则与 `===` 几乎一样（区别是 `NaN` 被视为与自身相等）。对于字符串和数字，这比较的是内容，但**对象是按引用比较的**：两个字段完全相同的对象字面量是两个不同的值。
```javascript
let alice = { name: "Alice" };
let people = new Set();
people.add(alice);
people.add(alice);
console.log(people.size);
// 打印 1
people.add({ name: "Alice" });
console.log(people.size);
// 打印 2
```
只有再次添加完全相同的那个对象才会被忽略。

---

把展开运算符和 `filter()` 结合起来，就能得到集合论中的经典操作。每一种都会构建一个**新的**集合，不会改变原来的集合：
- **并集**，出现在 `a`、`b` 或两者中的每一个值：`new Set([...a, ...b])`
- **交集**，只有同时出现在**两者**中的值：`[...a].filter((x) => b.has(x))`
- **差集**，`a` 中**不**在 `b` 里的值：`[...a].filter((x) => !b.has(x))`

```javascript
let a = new Set([1, 2, 3]);
let b = new Set([3, 4]);
console.log([...new Set([...a, ...b])]);
// 打印 [ 1, 2, 3, 4 ]
console.log([...a].filter((x) => b.has(x)));
// 打印 [ 3 ]
console.log([...a].filter((x) => !b.has(x)));
// 打印 [ 1, 2 ]
```
较新的 JavaScript 引擎也直接在 set 上提供了 `a.union(b)`、`a.intersection(b)` 和 `a.difference(b)`，但展开加 filter 的写法在任何地方都能用。

---

为了保持和 `Map` 相同的接口，set 提供了迭代器方法 `values()`、`keys()` 和 `entries()`。
由于 set 没有键，`keys()` 只是 `values()` 的另一个名字，而 `entries()` 会把每个值产出**两次**，作为一个 `[value, value]` 对：
```javascript
let letters = new Set(["a", "b"]);
console.log([...letters.values()]);
// 打印 [ 'a', 'b' ]
console.log([...letters.entries()]);
// 打印 [ [ 'a', 'a' ], [ 'b', 'b' ] ]
```
实际上你很少需要它们：`for...of` 和展开运算符已经可以直接遍历值。

---

`new Set()` 接受任何**可迭代对象**，而不仅仅是数组。字符串是可以逐字符迭代的，因此可以用它得到一段文本中不同的字符：
```javascript
let letters = new Set("hello");
console.log([...letters]);
// 打印 [ 'h', 'e', 'l', 'o' ]
```
