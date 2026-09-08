**字符串**是用引号括起来的字符序列，例如 `"hello"` 或 `'hello'`。
每个字符串都有一个 `length` 属性，用来说明它包含多少个字符：
```javascript
let greeting = "hello";
console.log(greeting.length);
// prints 5
```
空格和标点符号也算作字符。

---

字符串中的每个字符都有一个**索引**，从 `0` 开始。
你可以使用方括号或 `charAt()` 方法读取单个字符：
```javascript
let word = "hello";
console.log(word[0]);
// prints h
console.log(word.charAt(1));
// prints e
```
最后一个字符的索引是 `length - 1`：
```javascript
console.log(word[word.length - 1]);
// prints o
```

---

字符串自带许多内置**方法**。其中两个最简单的方法可以改变每个字母的大小写：
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// prints HELLO
console.log(word.toLowerCase());
// prints hello
```
这两个方法都不需要参数，但别忘了括号。

---

要检查一个字符串是否包含另一个字符串，可以使用以下方法，它们都返回一个布尔值：
- 如果 `text` 出现在任意位置，`includes(text)` 为 `true`
- 如果字符串以 `text` 开头，`startsWith(text)` 为 `true`
- 如果字符串以 `text` 结尾，`endsWith(text)` 为 `true`

```javascript
let file = "photo.png";
console.log(file.includes("."));
// prints true
console.log(file.startsWith("ph"));
// prints true
console.log(file.endsWith(".jpg"));
// prints false
```
比较是区分大小写的：`"Hello".includes("h")` 为 `false`。

---

`indexOf()` 方法返回一段文本在字符串中**第一次**出现的索引。
如果没有找到该文本，则返回 `-1`：
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// prints 2
console.log(word.indexOf("z"));
// prints -1
```

---

`slice(start, end)` 方法从索引 `start` 到索引 `end`（不包含）提取字符串的一部分：
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// prints Java
console.log(word.slice(4));
// prints Script
```
如果省略 `end`，截取会一直到字符串末尾。
负数索引从末尾开始计数：`word.slice(-3)` 为 `"ipt"`。
`substring(start, end)` 方法的用法相同，但不接受负数索引。

---

`indexOf()` 和 `slice()` 搭配得很好：先找到某个内容的位置，然后在那里截取字符串。
```javascript
let time = "10:45";
let colon = time.indexOf(":");
console.log(time.slice(colon + 1));
// prints 45
```
