**正则表达式**（regular expression，简称 **regex**）是一个描述文本形状的小模式。你可以用它来回答诸如"这个字符串里包含数字吗？"或者"单词 `cat` 出现在哪里？"这样的问题。

在 JavaScript 中，书写正则表达式最简短的方式是**正则表达式字面量**：写在两条斜杠之间的模式。
```javascript
const pattern = /cat/;
```
模式中的普通字符匹配它们自身，所以 `/cat/` 会匹配字符串中任意位置的三个字母 `c`、`a`、`t`。

对于一个模式，最简单的用法是询问它是否出现在某个字符串中。**`test`** 方法接收文本并返回 `true` 或 `false`：
```javascript
console.log(/cat/.test("the cat sleeps"));
// 打印 true
console.log(/cat/.test("the dog sleeps"));
// 打印 false
```
注意 `test` 只是在字符串中的*某个位置*查找模式；并不要求整个字符串都匹配。

---

当模式描述的是某一*类*字符而不是某个确切的字符时，它才真正变得有用。几个**转义序列**就能覆盖大多数需求：
- `\d` 任意数字，从 `0` 到 `9`
- `\w` 任意单词字符：字母、数字或 `_`
- `\s` 任意空白字符：空格、制表符、换行符

```javascript
console.log(/\d/.test("room 12"));
// 打印 true
console.log(/\d/.test("lobby"));
// 打印 false
```
**量词**表示前一个部分可以重复多少次。最常见的是 `+`，意思是"一个或多个"：
```javascript
console.log(/\d+/.test("42"));
// 打印 true
```
所以 `/\d/` 匹配单个数字，而 `/\d+/` 匹配一段连续数字。对于普通的 `test` 来说，两者行为相同，因为它们都只需要存在一个数字。

---

像 `/\d+/` 这样的字面量一经写出就固定不变了。当模式需要**在运行时构建**时，可以使用 **`RegExp` 构造函数**，它把模式作为字符串接收：
```javascript
const word = "cat";
const pattern = new RegExp(word);
console.log(pattern.test("the cat sleeps"));
// 打印 true
```
这里有一个陷阱。在字符串内部，反斜杠开启的是*字符串*的转义序列，所以它在正则表达式看到之前就消失了。要在模式中放入一个真正的反斜杠，必须把它写成两个：
```javascript
const digits = new RegExp("\\d+");
// 和 /\d+/ 相同的模式
```
如果写成 `new RegExp("\d+")`，得到的模式是 `/d+/`，它匹配字母 `d`，而不是数字。

在编写代码时就知道模式的情况下，优先使用字面量；它更简短，也不需要双写的反斜杠。

---

再有两个构件，你就能描述几乎任何形状的文本。

**字符类**是写在方括号之间的一组字符；它恰好匹配其中的一个。连字符表示一个范围，开头的 `^` 表示对集合取反：
```javascript
/[aeiou]/   // 一个元音字母
/[a-z]/     // 一个小写字母
/[A-Z0-9]/  // 一个大写字母或一个数字
/[^0-9]/    // 一个不是数字的字符
```
**量词**表示前一个部分重复多少次：`+` 一个或多个，`*` 零个或多个，`?` 零个或一个，`{n}` 恰好 `n` 次。

最后，**锚点**把模式固定到文本的两端：`^` 表示"从这里开始"，`$` 表示"到这里结束"。没有它们时，模式可以匹配字符串内部的任意位置，所以 `/\d{2}/.test("abc12def")` 是 `true`。两个锚点都用上时，整个字符串必须匹配：
```javascript
console.log(/^\d{2}$/.test("abc12def"));
// 打印 false
console.log(/^\d{2}$/.test("12"));
// 打印 true
```

---

`test` 只能回答是或否。要拿到匹配到的文本本身，可以在字符串上调用 **`match`**：
```javascript
const match = "order 42 shipped".match(/\d+/);
```
当没有任何匹配时，`match` 返回 `null`。当有匹配时，它返回一个类似数组的结果：
- `match[0]` 是被匹配到的文本
- `match.index` 是匹配开始的位置
- `match.input` 是被搜索的整个字符串

```javascript
console.log(match[0]);
// 打印 42
console.log(match.index);
// 打印 6
```
由于结果可能是 `null`，在读取 `match[0]` 之前要先检查它。

---

由于模式不存在时 `match` 会返回 `null`，直接读取 `match[0]` 会抛出 `TypeError: Cannot read properties of null`。要对它进行防护：
```javascript
function firstWord(text) {
  const match = text.match(/[a-z]+/);
  if (match === null) {
    return "";
  }
  return match[0];
}
```
空值合并运算符把同样的防护写在一行里，因为当 `match` 为 `null` 时 `match?.[0]` 是 `undefined`：
```javascript
return text.match(/[a-z]+/)?.[0] ?? "";
```

---

模式某一部分周围的圆括号会创建一个**捕获组**：该部分匹配到的文本会被单独保存起来，供你读取。

这些组出现在 `match[0]` 之后，按其左括号从左到右编号：
```javascript
const match = "2026-09-12".match(/(\d{4})-(\d{2})-(\d{2})/);
console.log(match[0]);
// 打印 2026-09-12
console.log(match[1]);
// 打印 2026
console.log(match[3]);
// 打印 12
```
所以 `match[0]` 始终是整个匹配，而 `match[1]`、`match[2]`、……是各个组。如果模式中的某个组完全没有匹配，那么整个 `match` 会返回 `null`。

---

只捕获你需要的东西。组不仅是一种读回某段文本的方式；它还告诉读者模式中哪一部分是重要的。在一个只想要分钟数的时间模式中，只给分钟加上组，其余部分不加组：
```javascript
const minutes = "at 14:35:02".match(/\d{2}:(\d{2}):\d{2}/)?.[1];
console.log(minutes);
// 打印 35
```
整个模式仍然必须匹配，所以小时和秒仍然是必需的；它们只是没有被捕获。组越少，读取 `match[1]`、`match[2]` 等时需要记住的编号就越少。

---

数括号很快就会让人疲惫，而且在模式中间添加一个组会让它之后的所有组重新编号。**命名捕获组**可以同时避免这两个问题：在左括号后面紧接着写 `?<name>`，然后从 `match.groups` 中读回这段文本：
```javascript
const match = "2026-09-12".match(/(?<year>\d{4})-(?<month>\d{2})-\d{2}/);
console.log(match.groups.year);
// 打印 2026
console.log(match.groups.month);
// 打印 09
```
命名捕获组仍然有编号，所以 `match[1]` 依然有效，但 `match.groups.year` 说明了这个值的含义。当模式中完全没有命名捕获组时，`match.groups` 是 `undefined`。

---

到目前为止的一切都在第一个匹配处停止。**标志**写在字面量的闭合斜杠之后，可以改变这一点以及搜索的其他细节：
- `g` 全局：找到每一个匹配，而不只是第一个
- `i` 忽略大小写，所以 `/cat/i` 也能匹配 `Cat` 和 `CAT`

带有 `g` 标志时，`match` 的行为有所不同：它返回一个由匹配到的**字符串**组成的普通数组，没有 `index`，也没有组；没有匹配时返回 `null`：
```javascript
const numbers = "a1 b22 c333".match(/\d+/g);
console.log(numbers);
// 打印 [ '1', '22', '333' ]
console.log(numbers.length);
// 打印 3
```
标志可以按任意顺序组合，例如 `/cat/gi`。使用 `RegExp` 构造函数时，它们放在第二个参数中：`new RegExp("\\d+", "g")`。

---

`g` 标志会给你每一个匹配到的字符串，但它把组丢掉了。当你需要*每一个*匹配的组时，使用 **`matchAll`**。它返回一个迭代器，其中是完整的匹配对象，每个都和普通 `match` 的结果完全一样：
```javascript
const text = "a=1;b=2";
for (const match of text.matchAll(/(?<key>\w+)=(?<value>\w+)/g)) {
  console.log(`${match.groups.key} -> ${match.groups.value}`);
}
// 打印 a -> 1
// 打印 b -> 2
```
`matchAll` 要求带有 `g` 标志；没有它会抛出 `TypeError`。由于它返回的是迭代器，当你想要真正的数组时，可以用 `[...text.matchAll(pattern)]` 展开它；还要注意，当模式从不匹配时，它不会产出任何东西。

---

**`replace`** 返回一个新字符串，其中匹配被换成别的内容。原字符串永远不会被改变。
```javascript
console.log("the cat sleeps".replace(/cat/, "dog"));
// 打印 the dog sleeps
```
在替换字符串内部，有几个序列具有特殊含义：
- `$1`、`$2`、…… 第 1 组、第 2 组、……捕获的文本
- `$<name>` 命名捕获组捕获的文本
- `$&` 整个匹配

这正是让 `replace` 成为改写工具而不只是交换工具的原因：
```javascript
console.log("2026-09-12".replace(/(\d{4})-(\d{2})-(\d{2})/, "$3/$2/$1"));
// 打印 12/09/2026
```
没有 `g` 标志时，只有**第一个**匹配会被替换。

---

要改写**每一个**匹配而不是第一个，你有两种选择：
```javascript
console.log("a1 b2".replace(/\d/g, "#"));
// 打印 a# b#
console.log("a1 b2".replaceAll(/\d/g, "#"));
// 打印 a# b#
```
**`replaceAll`** 是两者中更清晰的一个，而且它还接受普通字符串作为模式。当你给它一个正则表达式时，该正则表达式**必须**带有 `g` 标志，否则会抛出 `TypeError`；这恰好杜绝了"写了 `replace` 却只修正第一个匹配"这种无声的 bug。

---

替换的内容不必是字符串。当你传入一个**函数**时，每个匹配会调用它一次，它返回什么就把什么插入到该匹配的位置。

函数先接收整个匹配，然后接收各个捕获组：
```javascript
console.log("hello world".replace(/\w+/g, (word) => word.length));
// 打印 5 5

console.log("ann lee".replace(/(\w)(\w*)/g, (whole, first, rest) => first.toUpperCase() + rest));
// 打印 Ann Lee
```
这是根据匹配到的文本计算替换内容的唯一方式，仅靠 `$1` 做不到这一点。

---

**`split`** 把字符串切分成数组。给它普通字符串时，它按这段确切的文本切分；给它正则表达式时，它按模式的每一次匹配切分，这让一次调用就能处理各不相同的分隔符：
```javascript
console.log("a, b;c".split(", "));
// 打印 [ 'a', 'b;c' ]
console.log("a, b;c".split(/[,;]\s*/));
// 打印 [ 'a', 'b', 'c' ]
```
分隔符本身不会出现在结果中。要小心位于字符串开头或结尾的分隔符：它会在数组中产生一个空字符串，因为那一侧存在一个空字段。

---

最后一个标志补齐了整套标志。默认情况下，`^` 和 `$` 表示**整个字符串**的开头和结尾，所以用 `^` 锚定的模式只能匹配最开头，即使文本有多行。

**`m`**（多行）标志改变了这一点：`^` 和 `$` 还会匹配每个换行符之后和之前的位置，这样每一行都各自被锚定：
```javascript
const text = "note a\nb\nnote c";
console.log(text.match(/^note.*/g));
// 打印 [ 'note a' ]
console.log(text.match(/^note.*/gm));
// 打印 [ 'note a', 'note c' ]
```
这里有两个细节。默认情况下 `.` 不匹配换行符（只有 `s` 标志会改变这一点），所以 `.*` 自己就会停在行尾。另外，带 `g` 标志的 `match` 在没有匹配时返回 `null` 而不是空数组，所以当你承诺返回数组时，要把它与 `?? []` 搭配。
