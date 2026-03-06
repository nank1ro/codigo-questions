数组是一种数据类型，可以用来将多条不同的信息作为序列存储在一个变量名下。
数组可以存储一种或多种类型的多个值，并使用**索引**来区分这些值。
你可以使用以下表达式将元素赋值给数组：
```swift
var arrayName: [itemsType] = [item1, item2]
```
`itemsType` 表示数组中元素的类型，例如可以是 `Int`、`String`、`Any` 等...

---

你可以通过索引访问数组中的单个元素。
索引就像一个地址，标识了元素在数组中的位置。
索引直接写在数组名称后面的方括号中，像这样：
```swift
arrayName[index]
```

数组索引从 `0` 开始，**不是** `1`！你可以这样访问数组的第一个元素：`arrayName[0]`。
数组中的第二个元素位于索引 1：`arrayName[1]`。

---

数组索引的行为与其他变量名相同。
它既可以用于访问值，也可以用于赋值。
你已经了解了如何这样访问数组索引：
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
print(names[0])
```
下面是赋值的方式：
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
print(names[0])
```

---

与字符串一样，数组也有**长度** `count`。
数组的长度是它包含的元素数量

---

数组不必有固定的长度。
你可以随时向数组末尾添加元素！
要向数组添加元素，我们使用 `append` 函数：
```swift
var letters = ["a", "b"]
letters.append("c")
print(letters)
// Prints ["a", "b", "c"]
```

---

有时你只想访问数组的一部分。
考虑以下代码：
```swift
let numbers = [1, 2, 3, 4]
let slice = numbers[1...2]
print(slice)
// prints [2, 3]
```
首先，我们创建一个名为 `numbers` 的数组。
然后，我们取数组的一个子部分并存储在 slice 数组中。
我们通过在数组名称后定义要包含的索引来实现：`numbers[1...2]`。
在 Swift 中，我们可以使用 `...` 来包含最后一个索引，也可以使用 `..<` 来排除最后一个索引

---

在 Swift 中，我们可以随意切片数组！
```swift
// Grabs the first two items
listName[..<2]
// Grabs the fourth through last items
listName[3...]
```
如果你的数组切片包含数组中的第一个或最后一个元素，则不必包含该元素的索引

---

如果我们指定 `Any` 类型，数组元素可以是任何类型：
```swift
var arrayName: [Any] = ["one", 2, true]
```
事实上，上面我们依次有一个字符串、一个整数和一个布尔值。
但我们也可以在数组中嵌套数组！

---

有时你需要在数组中搜索某个元素。
在 Swift 中，我们可以使用 `firstIndex()` 方法：
```swift
var names: [String] = ["Trevor", "Zac", "Glenn"]
if let index = names.firstIndex(of: "Zac") {
  print(index)
}
// prints 1
```
上面的代码打印包含字符串 `"Zac"` 的第一个索引，在本例中为 `1`。
我们还可以使用 `insert()` 方法在特定索引处插入元素：
```swift
names.insert("Ali", at: 1)
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
上面的代码在索引 `1` 处插入 `"Ali"`，这会将该索引之后的所有元素向后移动 1 位

---

在 Swift 中，我们可以使用 `for..in` 关键字以非常简单的方式遍历数组：
```swift
var numbers = [1, 2, 3]
for num in numbers {
    print(num)
}
// prints 1, 2, 3
```
`for` 关键字后面跟一个变量名，它将依次被赋值为每个数组元素的值。

---

**元组**类似于数组，但你可以为元素命名并使用这些名称来引用它们
创建元组时使用圆括号 `()`
```swift
var person = (firstName: "John", lastName: "Smith")
var firstName = person.firstName // John
var lastName = person.lastName // Smith
```
