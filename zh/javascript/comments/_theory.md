**注释**是写在源代码里、给阅读代码的人看的说明。JavaScript 会完全忽略注释，因此注释绝不会改变程序的行为。

最简单的注释是**单行注释**：它以 `//` 开头，一直延续到该行结尾。
```javascript
// Greets the user
console.log("Hello");
```
用注释说明一段代码的用途，或者当初为什么这样写。注意，与某些其他语言不同，在 JavaScript 中 `#` **不会**开始一条注释。

---

注释不必独占一行：它可以跟在同一行的代码后面。这就是**行内注释**（也叫行尾注释），很适合对某条语句写一句简短的说明：
```javascript
const retries = 3; // give up after three attempts
```
从 `//` 到行尾的所有内容都会被忽略，而它前面的代码照常执行。

---

由于注释会被忽略，添加或删除注释绝不会改变程序的行为。只有**没有**被注释掉的代码才会运行。

这让 `//` 成为一种不删除代码就能关掉某一行的快捷方式，这叫做**注释掉**代码：
```javascript
let total = 10;
// total = total + 5;
console.log(total); // prints 10
```
第二行现在是注释，所以 `total` 仍然是 `10`。去掉 `//` 就能让这一行重新生效。

注释掉代码在你做实验时很方便，但记得清理：长期留着被注释掉的代码只会让下一个阅读者困惑。

---

当一条注释需要不止一行时，JavaScript 提供了**多行注释**（也叫块注释）：它以 `/*` 开始、以 `*/` 结束，中间的一切都会被忽略，包括换行。
```javascript
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
console.log("Welcome!");
```
块注释也可以很短，写在一行里：`/* like this */`。

---

无论你用哪种注释，规则都一样：注释里的文字**不是代码**。注释中的 `console.log` 永远不会输出任何内容，同一行里写在 `//` 之后的代码也永远不会运行，即便这一行以真正的代码开头：
```javascript
console.log("a"); // console.log("b");
/* console.log("c"); */
// prints only a
```
当你不确定一个程序会输出什么时，先在心里删掉所有注释，再读剩下的内容。

---

与在行尾结束的 `//` 不同，`/*` 注释只有遇到 `*/` 才会结束。如果你忘了关闭它，JavaScript 会把后面的所有代码都当作注释的一部分，并报出语法错误：
```javascript
const width = 10; /* in centimetres
console.log(width); // still inside the comment: SyntaxError, the comment is never closed
```
`//` 和 `/* */` 都可以用作行内注释，但用 `/*` 时一定要确认 `*/` 存在。

---

JavaScript 中的块注释**不能嵌套**：注释在遇到的**第一个** `*/` 处结束，不管前面有多少个 `/*`。
```javascript
/* outer /* inner */ still a comment */
console.log("done");
```
这里注释在 `inner` 之后就结束了，所以 `still a comment */` 被当作代码读取并导致语法错误。当你要注释掉一段已经包含 `/* */` 注释的代码时请记住这一点：改用每行加 `//`，或者先删掉里面的注释。

---

要一次注释掉多行，就用一条块注释把它们包起来，而不是给每一行都加 `//`：
```javascript
let total = 100;
/*
total = total - 30;
total = total - 20;
*/
console.log(total); // prints 100
```
由于块内的这些行被忽略，`total` 始终不变。记住，只有当这些行中都不含 `*/` 时这样做才有效。

---

JavaScript 还有第三种注释，即**文档注释**，采用 **JSDoc** 格式：一条以 `/**`（两个星号）开头的块注释，直接放在函数上方。注释内部的各行通常以 ` * ` 开头，以 `@` 开头的特殊**标签**用来描述这个函数：
- `@param {type} name description` 对应每个参数
- `@returns {type} description` 对应返回值

```javascript
/**
 * Returns the greeting for a person.
 * @param {string} name the name of the person
 * @returns {string} the greeting, ending with an exclamation mark
 */
function greet(name) {
  return `Hi, ${name}!`;
}
```
对 JavaScript 来说它只是一条注释，但编辑器会读取它，并把它作为 `greet` 的提示文本显示出来，同时显示写在花括号里的类型（`{number}`、`{string}`、`{boolean}`、`{number[]}`……）。

---

JSDoc 注释的第一行是**概述**：用一句简短的话说明函数做什么。用第三人称来写，就像在描述这个函数："Returns..."、"Adds..."、"Checks..."。然后逐行列出标签：
```javascript
/**
 * Returns true when n is divisible by two.
 * @param {number} n the number to check
 * @returns {boolean} true for even numbers, false otherwise
 */
function isEven(n) {
  return n % 2 === 0;
}
```
注释必须紧挨在声明的上方，中间不能有空行，否则编辑器不会把它关联到这个函数。

---

JSDoc 注释也是一份**契约**：早在函数体写好之前，它就告诉调用者该传什么、能得到什么。读懂注释往往就足以实现这个函数：
```javascript
/**
 * Returns the larger of two numbers.
 * @param {number} a the first number
 * @param {number} b the second number
 * @returns {number} a if it is greater than b, otherwise b
 */
function larger(a, b) {
  return a > b ? a : b;
}
```
每个 `@param` 按相同顺序对应一个参数，而 `@returns` 描述所有可能的结果。

---

JSDoc 注释内部的顺序始终一致：先是概述，然后按参数声明顺序每个参数一行 `@param`，最后是 `@returns`。开头的 `/**` 和结尾的 ` */` 把这一切包起来，而注释就位于它所描述的函数正上方：
```javascript
/**
 * Returns the number of seconds in the given minutes.
 * @param {number} minutes a whole number of minutes
 * @returns {number} minutes multiplied by sixty
 */
function toSeconds(minutes) {
  return minutes * 60;
}
```

---

JavaScript 文件可以以一行特殊的内容开头，叫做 **shebang**（或 hashbang）：`#!` 后面跟着应当运行该文件的程序路径。在类 Unix 系统上，它让你可以直接从终端运行脚本，比如 `./hello.js`，而不必先输入 `node`：
```javascript
#!/usr/bin/env node
console.log("Hello from Node");
```
JavaScript 会像对待注释一样忽略这一行，但仅限它是文件的**第一行**：写在其他任何位置，`#!` 都是语法错误。`/usr/bin/env node` 的意思是"在这个系统上找到 `node` 并使用它"。

---

好的注释说明代码**为什么**这样做，而不是它**做了什么**。代码本身已经展示了发生的事情；用文字重复一遍只会增加噪音，而且代码一改动它就过时了：
```javascript
// set timeout to 30
const timeout = 30;
```
这个数字背后的原因才是读者猜不到的：
```javascript
// the server drops idle connections after 35 seconds, so stop earlier
const timeout = 30;
```
如果一条注释只是复述它下面那一行，就删掉它，或者换成写明原因。

---

有些注释遵循编辑器能够识别的约定。最常见的**标记**有：
- `// TODO: ...` 标出还需要编写的内容
- `// FIXME: ...` 标出已知有错、必须修正的代码

```javascript
const limit = 10;
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
对 JavaScript 来说它们只是普通注释；编辑器会把它们列出来，方便找到待办工作。`TODO` 通常紧挨着一个占位实现，在真正的实现写好之前先让代码能跑起来。当你完成这项工作时，要在同一次改动中替换掉占位实现并删除标记：过时的 `TODO` 会误导人。

---

`FIXME` 和 `TODO` 不同：代码已经存在，但已知它是错的。好的 `FIXME` 会说明 bug 是什么，并尽可能给出一个能体现它的例子，好让下一个人快速修复。和 `TODO` 一样，bug 修好后就删除这个标记，但要保留 JSDoc 注释，因为它依然成立。
