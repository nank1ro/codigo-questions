我们知道如何使用 `while` 循环来重复执行代码。
就像这个程序重复输出 `hello` 一样
```javascript
var counter = 0;

while (counter < 5) {
    console.log("hello");
    counter++;
}
```
但我们也可以使用 `for` 循环来实现同样的效果：
```javascript
for (let i = 0; i < 5; i++) {
    console.log("hello");
}
```

---

在 `for` 循环中，我们可以指定希望循环运行的次数

---

我们可以使用 `<` 来循环到下一个数字（不包含该数字），或者使用 `<=` 来循环到下一个数字（包含该数字）

---

名为 `i` 的变量是计数器变量。
我们可以给它取任何名字。
它记录当前循环执行到了第几次

---

在 JavaScript 中，我们还有 `forEach` 循环。
实际上，`forEach` 按照与 `for` 循环相同的顺序对序列中的每个元素调用给定的闭包：
```javascript
// this is an array, we'll see about that soon
let numbers = [1, 3, 5, 7, 9];
numbers.forEach((num) => console.log(num));}
```
使用 `forEach` 方法与 `for` 循环有两个重要区别：
1. 不能使用 `break` 或 `continue` 语句来退出当前闭包调用或跳过后续调用。
2. 在闭包体中使用 `return` 语句只会退出闭包而不会退出外部作用域，也不会跳过后续调用。
注意：`=>` 这被称为 _箭头函数_，它是 ES6 中更简短的函数语法，可以替代花括号 {} 并返回值（如果需要的话）
