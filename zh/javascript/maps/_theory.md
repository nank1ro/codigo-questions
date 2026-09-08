**Map** 存储**键值对**：每个值都保存在一个键下，你可以使用该键再次找到该值。
你可以用 `new Map()` 创建一个空的 Map，用 `set(key, value)` 添加一对键值，用 `get(key)` 读取一个值：
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// prints 30
```
使用一个已经存在的键调用 `set()` 会替换它的值。

---

Map 还有一些其他重要的方法和属性：
- `has(key)` 如果键存在则返回 `true`
- `delete(key)` 删除该键对应的键值对
- `size` 是存储的键值对数量

```javascript
let stock = new Map();
stock.set("apple", 3);
stock.set("pear", 5);
console.log(stock.has("apple"));
// prints true
stock.delete("pear");
console.log(stock.size);
// prints 1
```
注意 `size` 是一个属性，而不是方法，所以它没有括号。

---

向 Map 请求一个它不包含的键并不是错误：`get()` 只会返回 `undefined`。
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// prints undefined
```
这就是为什么存在 `has()`：它可以让你区分缺失的键和值恰好为 `undefined` 的键。
`set()` 返回 Map 本身，所以可以链式调用：
```javascript
ages.set("Bob", 25).set("Cy", 41);
```

---

在普通对象中，每个键都会被转换为字符串：`user[1]` 和 `user["1"]` 是同一个键。
Map 会保留键的**类型**，所以一个数字、一个字符串、一个布尔值，甚至一个对象都可以各自作为不同的键：
```javascript
let lookup = new Map();
lookup.set(1, "number one");
lookup.set("1", "string one");
console.log(lookup.size);
// prints 2
let alice = { name: "Alice" };
lookup.set(alice, "an object key");
console.log(lookup.get(alice));
// prints an object key
```
对象键是按身份比较的：只有完全相同的那个对象才能取回对应的值。

---

Map 会记住键值对添加的顺序，你可以用 `for...of` 遍历它。
`entries()` 方法将每一对以 `[key, value]` 数组的形式给出，你可以在循环中直接解构：
```javascript
let stock = new Map();
stock.set("apple", 3);
stock.set("pear", 5);
for (const [name, qty] of stock.entries()) {
  console.log(`${name}: ${qty}`);
}
// prints apple: 3
// prints pear: 5
```
直接遍历 Map 本身，`for (const [name, qty] of stock)`，效果完全相同。

---

当你只需要键值对的一侧时，在循环中使用 `keys()` 或 `values()` 来代替 `entries()`：
```javascript
let prices = new Map();
prices.set("tea", 2);
prices.set("cake", 4);
for (const name of prices.keys()) {
  console.log(name);
}
// prints tea
// prints cake
for (const price of prices.values()) {
  console.log(price);
}
// prints 2
// prints 4
```

---

你可以不必多次调用 `set()`，而是通过向 `new Map()` 传入一个**键值对数组**来一次性构建一个 Map：
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// prints 2
```
因为 `Object.entries(obj)` 返回的正是这样一个键值对数组，所以它是把对象转换成 Map 最快的方法：
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// prints 30
```
