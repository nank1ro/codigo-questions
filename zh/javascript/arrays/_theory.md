数组是一种数据类型，可用于在单个变量名下按顺序存储不同信息的集合。
数组存储一种或多种类型的多个值，并使用**索引**来区分这些值。
你可以使用以下形式的表达式将项目分配给数组：
```javascript
var arrayName = [item1, item2];
```

---

你可以通过索引访问数组中的单个项目。
索引就像一个地址，标识了项目在数组中的位置。
索引直接出现在数组名称之后的方括号中，如下所示：
```javascript
arrayName[index];
```
数组索引从 `0` 开始，**不是** `1`！你可以这样访问数组的第一个项目：`arrayName[0]`。
数组中的第二个项目的索引为 1：`arrayName[1]`。

---

数组索引的行为与任何其他变量名相同。
它既可以用于访问值，也可以用于赋值。
你已经看到了如何像这样访问数组索引：
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Prints the value "Jeremiah"
console.log(names[0]);
```
以下是赋值的方式：
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Assign the new value "Jordan"
names[0] = "Jordan";
// Prints the value "Jordan"
console.log(names[0]);
```

---

与字符串一样，数组也有**长度**。
数组的长度是它包含的项目数量

---

数组不必具有固定长度。
你可以随时将项目添加到数组的末尾！
要向数组添加项目，我们使用 `push` 函数：
```javascript
var letters = ["a", "b"];
letters.push("c");
console.log(letters);
// Prints ["a", "b", "c"]
```

---

有时，你只想访问数组的一部分。
请看以下代码：
```javascript
let numbers = [1, 2, 3, 4];
let slice = numbers.slice(1, 3);
console.log(slice);
// prints [2, 3]
```
首先，我们创建一个名为 `numbers` 的数组。
然后，我们取数组的一个子部分并将其存储在 slice 数组中。
我们通过在数组名称后定义要包含的索引来做到这一点：`numbers.slice(1, 3)`。
请记住，右边的索引是不包含在内的

---

在 JavaScript 中，我们可以随意切片数组！
```javascript
// Grabs the first two items
listName.slice(0, 2);
// Grabs the fourth through last items
listName.slice(3);
```
如果你的数组切片包含数组中的第一个或最后一个项目，则不必包含该项目的索引

---

数组元素可以是任何类型。
```javascript
var arrayName = ["one", 2, true];
```
实际上，上面我们依次有一个字符串、一个整数和一个布尔值。
但我们也可以在数组中嵌套数组！

---

有时你需要在数组中搜索一个项目。
在 JavaScript 中，我们可以使用 `indexOf()` 方法：
```javascript
var names = ["Trevor", "Zac", "Glenn"];
console.log(names.indexOf('Zac'));
// prints 1
```
上面的代码打印了包含字符串 `"Zac"` 的第一个索引，在本例中为 `1`。
我们还可以使用 `splice()` 方法在特定索引处插入项目：
```javascript
names.splice(1, 0, "Ali");
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
上面的代码在索引 `1` 处插入了 `"Ali"`，这会将此索引之后的所有内容向后移动 1 位。
第二个值 `0` 表示 _deleteCount_（删除数量），在本例中，我们不删除数组中的任何项目；但如果我们指定 `1`，则值 `Zac` 将从数组中被删除

---

在 JavaScript 中，我们可以使用 `for..of` 关键字以非常简单的方式遍历数组：
```javascript
var numbers = [1, 2, 3];
for (num of numbers) {
    console.log(num);
}
// prints 1, 2, 3
```
`for` 关键字后面跟着一个变量名，它将依次被赋予每个数组项目的值。
