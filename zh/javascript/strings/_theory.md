**字符串**是用引号括起来的字符序列，例如 `"hello"` 或 `'hello'`。
每个字符串都有一个 `length` 属性，用来说明它包含多少个字符：
```javascript
let greeting = "hello";
console.log(greeting.length);
// 打印 5
```
空格和标点符号也算作字符。

---

字符串中的每个字符都有一个**索引**，从 `0` 开始。
你可以使用方括号或 `charAt()` 方法读取单个字符：
```javascript
let word = "hello";
console.log(word[0]);
// 打印 h
console.log(word.charAt(1));
// 打印 e
```
最后一个字符的索引是 `length - 1`：
```javascript
console.log(word[word.length - 1]);
// 打印 o
```

---

字符串自带许多内置**方法**。其中两个最简单的方法可以改变每个字母的大小写：
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// 打印 HELLO
console.log(word.toLowerCase());
// 打印 hello
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
// 打印 true
console.log(file.startsWith("ph"));
// 打印 true
console.log(file.endsWith(".jpg"));
// 打印 false
```
比较是区分大小写的：`"Hello".includes("h")` 为 `false`。

---

`indexOf()` 方法返回一段文本在字符串中**第一次**出现的索引。
如果没有找到该文本，则返回 `-1`：
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// 打印 2
console.log(word.indexOf("z"));
// 打印 -1
```

---

`slice(start, end)` 方法从索引 `start` 到索引 `end`（不包含）提取字符串的一部分：
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// 打印 Java
console.log(word.slice(4));
// 打印 Script
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
// 打印 45
```

---

`split(separator)` 方法将字符串拆分为一个**数组**片段，在每个 `separator` 处切分：
```javascript
let sentence = "I like JavaScript";
let words = sentence.split(" ");
console.log(words);
// 打印 [ 'I', 'like', 'JavaScript' ]
```
与之相反的是数组方法 `join(separator)`，它把这些片段重新粘合成一个字符串：
```javascript
console.log(words.join("-"));
// 打印 I-like-JavaScript
```

---

用户输入常常带有多余的空格。`trim()` 方法返回一个去除**两端**空白字符的字符串副本：
```javascript
let input = "   hello   ";
console.log(input.trim());
// 打印 hello
```
`trimStart()` 只去除开头的空白，`trimEnd()` 只去除结尾的空白。
字符串中间的空格永远不会被处理。

---

`replace(search, replacement)` 方法返回一个新字符串，其中 `search` 的**第一次**出现被替换为 `replacement`：
```javascript
let text = "red red";
console.log(text.replace("red", "blue"));
// 打印 blue red
```
要替换**所有**出现的位置，使用 `replaceAll()`：
```javascript
console.log(text.replaceAll("red", "blue"));
// 打印 blue blue
```

---

`repeat(count)` 方法返回重复 `count` 次的字符串：
```javascript
console.log("ab".repeat(3));
// 打印 ababab
console.log("ab".repeat(0));
// 打印空字符串
```

---

`padStart(targetLength, padString)` 方法会在字符串的**开头**添加 `padString`，直到达到 `targetLength` 个字符。`padEnd()` 在结尾做同样的事：
```javascript
console.log("7".padStart(3, "0"));
// 打印 007
console.log("Tea".padEnd(6, "."));
// 打印 Tea...
```
如果字符串已经足够长，则原样返回。
数字没有字符串方法，所以要先用 `String(number)` 转换它们。

---

两个字符串只有在字符完全相同、大小写也相同的情况下，用 `===` 比较才相等：
```javascript
console.log("hello" === "hello");
// 打印 true
console.log("hello" === "Hello");
// 打印 false
```
`<` 和 `>` 运算符按字母顺序逐个字符比较字符串。
大写字母排在小写字母之前，所以 `"Zoo" < "apple"` 为 `true`。

---

字符串是**不可变的**：一旦创建，字符串就永远不能被更改。
对索引赋值不会产生任何效果，每个字符串方法都会返回一个**新**字符串，而不是修改原字符串：
```javascript
let word = "hello";
word[0] = "j";
console.log(word);
// 打印 hello
word.toUpperCase();
console.log(word);
// 打印 hello
```
要保留结果，需要把它重新赋值给变量：
```javascript
word = word.toUpperCase();
```

---

使用空分隔符调用 `split("")` 会把字符串转换为由单个字符组成的数组。
数组有一个 `reverse()` 方法，因此你可以通过拆分、反转再拼接来反转字符串：
```javascript
let word = "abc";
console.log(word.split("").reverse().join(""));
// 打印 cba
```
