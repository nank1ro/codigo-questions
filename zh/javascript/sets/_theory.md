**Set** 是**唯一**值的集合：每个值最多只能出现一次，并且没有可以按位置访问值的索引。
当你只关心*哪些*值存在，而不关心出现次数或顺序时，Set 非常合适。
你可以用 `new Set()` 创建一个空的 set，用 `add(value)` 添加一个值，用 `has(value)` 检查某个值是否存在：
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// prints true
console.log(colors.has("green"));
// prints false
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
// prints 2
tags.delete("css");
console.log(tags.size);
// prints 1
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
// prints 3
```
**展开**运算符 `...` 反过来使用，可以把 set 再转换回数组：
```javascript
let unique = [...distinct];
console.log(unique);
// prints [ 1, 2, 3 ]
```
`Array.from(distinct)` 的效果是一样的。

---

set 会记住值被添加的顺序，你可以用 `for...of` 遍历它：
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// prints 3
// prints 1
// prints 2
```
set 也有一个 `forEach()` 方法，会为每个值调用一次函数：
```javascript
nums.forEach((n) => console.log(n * 10));
// prints 30
// prints 10
// prints 20
```
