你可能遇到过这样的情况：想要重复使用一段代码，只是需要改变一些值。
与其重写整段代码，不如定义一个函数，这样可以反复调用，代码更加简洁。
在 Swift 中，我们使用 `func` 关键字后跟函数名来定义函数：
```swift
func say_hi() {
    print("Hello!")
}
say_hi() // prints "Hello!"
```

---

如果我们想要指定参数，__函数定义__中的圆括号就不必为空

---

有时我们希望函数__返回__一个值。
这时就需要用到 `return` 关键字。

---

函数可以有多个输入参数，这些参数写在函数的圆括号内，用逗号分隔。
```swift
func sayHello(name: String, newUser: Bool) -> String {
  var greet: String = "Hello \(name)!"
  if (newUser) {
    greet += " Welcome on board :)"
  }
  return greet
}
// prints "Hello Smith! Welcome on board :)"
print(sayHello(name: "Smith", newUser: true))
```

---

你可以使用元组类型作为函数的返回类型，将多个值作为一个复合返回值的一部分返回。

---

如果你不想为参数添加参数标签，可以在参数前使用下划线 `_` 代替显式的参数标签

---

你可以通过在参数类型后赋值来为函数中的任何参数定义_默认_值。
如果定义了默认值，调用函数时可以省略该参数
```swift
func someFunction(parameterWithoutDefault: Int, parameterWithDefault: Int = 12) {
    // do stuff here
}
```

---

_可变参数_接受零个或多个指定类型的值。
你可以使用可变参数来指定在调用函数时可以传入数量不定的输入值。
在参数类型名后面插入三个点 `...` 来编写可变参数。
传递给可变参数的值在函数体内以适当类型的数组形式提供。
例如，一个名为 `numbers`、类型为 `Double...` 的可变参数在函数体内以 `[Double]` 类型的常量数组形式提供

---

在函数中，我们可以添加一个_可选的注释_来解释函数的功能：
```swift
/// Prints 'Hello World' to the console.
func helloWorld() {
    print("Hello, World!")
}
```
我们可以使用 `///` 进行单行注释，使用 `/** */` 进行多行注释
