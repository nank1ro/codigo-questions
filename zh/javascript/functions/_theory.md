你可能遇到过这样的情况：想要重复使用一段代码，只是需要改变一些值。
与其重写整段代码，不如定义一个函数，这样可以反复使用，代码也更简洁。
在 JavaScript 中，我们使用 `function` 关键字后跟函数名来定义函数：
```javascript
function sayHi() {
    console.log("Hello!");
}
sayHi();
// prints "Hello!"
```

---

如果我们想指定参数，__函数定义__中的括号不必为空

---

有时我们希望函数能__返回__一个值。
这就需要用到 `return` 关键字。

---

函数可以有多个输入参数，这些参数写在函数的括号内，用逗号分隔。
```javascript
function sayHello(name, newUser) {
  var greet = `Hello ${name}!`;
  if (newUser) {
    greet += " Welcome on board :)";
  }
  return greet;
}
// prints "Hello Smith! Welcome on board :)"
console.log(sayHello("Smith", true));
```

---

你可以通过在参数后面赋值来为函数的任何参数定义_默认_值。
如果定义了默认值，调用函数时可以省略该参数
```javascript
function someFunction(parameterWithoutDefault, parameterWithDefault = 12) {
    // do stuff here
}
```

---

__剩余参数__语法允许我们将不定数量的参数表示为一个数组。
通过在参数名前插入三个句点字符 `...` 来编写剩余参数。
传递给剩余参数的值在函数体内以数组的形式提供。
例如，名为 `numbers` 的剩余参数在函数体内以名为 numbers 的常量数组形式提供

---

在函数中，我们可以添加一个_可选注释_来解释函数的作用：
```javascript
// Prints 'Hello World' to the console.
function helloWorld() {
    console.log("Hello, World!");
}
```
我们可以使用 `//` 来写单行注释，使用 `/** */` 来写多行注释
