你已经知道如何声明一个有名字的函数，例如 `void sayHello() { ... }`。Dart 还允许你编写**没有名字**的函数：**匿名函数**。它与命名函数的组成部分相同（括号中的参数和花括号中的函数体），但没有返回类型也没有名字：

```dart
(String name) {
  print('Hello, $name!');
}
```

由于它没有名字，通常的用法是把它存储在一个变量中，然后像调用函数一样调用这个变量：

```dart
var sayHello = (String name) {
  print('Hello, $name!');
};

sayHello('Dart'); // Hello, Dart!
```

注意闭括号后面的 `;`：这个赋值是一条普通的语句。

---

匿名函数可以接收参数并 `return` 一个值，与命名函数完全一样。返回类型不需要写出：Dart 会根据函数体中的 `return` 语句**推断**它。

```dart
var add = (int a, int b) {
  return a + b;
};

print(add(2, 3)); // 5
```

---

当函数体是单个表达式时，匿名函数可以使用**箭头语法** `=>`，与命名函数一样。箭头取代了花括号和 `return` 关键字：

```dart
var add = (int a, int b) => a + b;

print(add(2, 3)); // 5
```

这种简写形式是 Dart 中编写匿名函数最常见的方式。

---

函数是值，因此它们也有类型。函数的类型写作**返回类型**，然后是关键字 `Function`，再然后是括号中的**参数类型**：

```dart
int Function(int, int) add = (int a, int b) => a + b;
bool Function(String) isEmpty = (String s) => s.isEmpty;
void Function() hello = () => print('Hello');
```

当变量以这种方式声明类型时，匿名函数中的参数类型可以省略，因为 Dart 会从声明的类型中推断它们：

```dart
int Function(int, int) add = (a, b) => a + b;
```

单独的 `Function` 类型可以接受任何函数，无论它的参数和返回类型是什么，但它不会告诉 Dart 如何调用它。

---

由于函数类型是一种普通类型，函数可以把**另一个函数作为参数**。在函数体中，该参数可以像任何函数一样被调用：

```dart
int apply(int n, int Function(int) operation) {
  return operation(n);
}

print(apply(5, (n) => n * 2)); // 10
print(apply(5, (n) => n - 1)); // 4
```

这里调用者通过传递一个匿名函数作为第二个参数，来决定 `apply` 做什么。

---

Dart 集合的许多方法都把函数作为参数，而匿名函数是传递函数的自然方式。最简单的是 `forEach`，它会为列表中的每个元素调用一次给定的函数：

```dart
var fruits = ['apple', 'kiwi'];

fruits.forEach((fruit) {
  print('I like $fruit');
});
// I like apple
// I like kiwi
```

参数类型是从列表中推断出来的，所以无需写出，`fruit` 就是一个 `String`。

---

另外两个接收匿名函数的非常常见的方法是 `map` 和 `where`：

- `map` 用该函数转换每个元素并返回新的值
- `where` 只保留函数对其返回 `true` 的元素

两者都返回一个惰性的 `Iterable`；调用 `toList()` 可以把结果转换成 `List`：

```dart
var numbers = [1, 2, 3];

var squares = numbers.map((n) => n * n).toList();
print(squares); // [1, 4, 9]

var big = numbers.where((n) => n > 1).toList();
print(big); // [2, 3]
```

---

由于 `map` 和 `where` 都返回 `Iterable`，它们的调用可以一个接一个地**链式**连接。每一步都接收上一步的结果，最后调用一次 `toList()`：

```dart
var numbers = [1, 2, 3, 4, 5, 6];

var result = numbers.where((n) => n > 3).map((n) => n * 10).toList();
print(result); // [40, 50, 60]
```

---

`sort` 会对列表就地重新排序。默认情况下它使用元素的自然顺序，但你也可以传递一个**比较两个元素**的匿名函数，它返回一个负数、零或正数。`compareTo` 正好给出这样的数字，因此它是常用的构建块：

```dart
var words = ['pear', 'fig', 'banana'];

words.sort((a, b) => a.length.compareTo(b.length));
print(words); // [fig, pear, banana]
```

在比较中交换 `a` 和 `b` 会反转顺序。

---

`reduce` 把列表中的所有元素组合成单个值。它的匿名函数接收两个参数：到目前为止**已累积的值**和**下一个元素**，并返回新的累积值。第一个元素被用作起始值：

```dart
var numbers = [2, 3, 4];

var product = numbers.reduce((total, n) => total * n);
print(product); // 24
```

`reduce` 在空列表上会抛出错误，因为没有第一个元素可以作为起点。

---

函数还可以**返回一个函数**。此时返回类型是一个函数类型，函数体返回一个匿名函数：

```dart
int Function(int) makeAdder(int amount) {
  return (int n) => n + amount;
}

var addTen = makeAdder(10);
print(addTen(5)); // 15
```

注意，返回的函数即使在 `makeAdder` 结束之后，仍然使用着 `makeAdder` 的参数 `amount`。像这样记住周围变量的函数被称为**闭包**。

---

闭包不只是读取它捕获的变量：它还可以**修改**它们，并且这些修改会在多次调用之间保留。这使得不使用类也能保存私有的状态：

```dart
int Function() makeTimer() {
  var seconds = 0;
  return () {
    seconds += 10;
    return seconds;
  };
}

var timer = makeTimer();
print(timer()); // 10
print(timer()); // 20
```

每次调用 `makeTimer()` 都会创建一个全新的 `seconds` 变量，所以两个计时器永远不会共享它们的计数。
