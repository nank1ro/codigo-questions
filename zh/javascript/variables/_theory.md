变量是用于存储数据值的容器。
JavaScript 中的每个变量都是一个对象。
要创建一个变量，我们需要给它一个**名称**，并且要记住名称中不能包含空格。
变量在你第一次给它赋值时就被创建了。
在 JavaScript 中，你可以使用 `let` 或 `const` 关键字声明常量，使用 `var` 关键字声明变量。
常量的值一旦设定就不能更改，而变量的值可以在之后被修改。
下面是创建一个名为 `x` 的变量的示例：
```javascript
var x = 1;
```
这样我们就将值 `1` 赋给了名为 `x` 的变量。
如果我们打印变量 `x`，我们会得到数字 `1`：
```javascript
console.log(x);
// prints 1
```

---

变量之所以被称为变量，是因为它们存储的值是可以改变的。
我们可以使用 `=` 来更新 `x` 并给它一个新的值。
```javascript
var x = 1;
console.log(x); // prints 1
x = 2;
console.log(x); // prints 2
```

---

我们也可以将其他变量的值赋给变量。
在这里，我们可以将 `x` 的值赋给变量 `y`
```javascript
var x = 5;
var y = x;
console.log(y); // prints 5
```

---

当我们更新一个变量时，它会忘记之前的值。
在这里，我们可以打印两次变量 `x`，看看它的值是如何更新的。
```javascript
var x = 5;
console.log(x); // prints 5
x = 10;
console.log(x); // prints 10
```

---

在 JavaScript 中，字符串变量可以使用双引号和单引号来声明：
```javascript
let x = "May";
// both are the same string
let y = 'May';
console.log(x === y);
// prints true
```

---

如果我们想要一个包含多个单词的变量名，我们使用**驼峰命名法（camelCase）**。
它是一种书写方式，短语中间的每个单词的首字母大写
