你已经知道如何声明一个带类型的变量，例如 `String name = 'Ada';`。但有时某个值就是**缺失**的：没有昵称的用户、什么都没找到的搜索、无法转换成数字的文本。Dart 用 `null` 表示缺失的值。

从 Dart 2.12 起，这门语言拥有**健全的空安全（sound null safety）**：像 `String` 这样的普通类型**永远**不能存放 `null`。尝试赋值会导致编译错误，程序根本无法运行：

```dart
String name = null; // error: a value of type 'Null' can't be assigned to 'String'
```

要允许缺失的值，你需要在类型后面加上问号 `?`。`String?` 存放的要么是 `String`，要么是 `null`，而打印 `null` 会显示单词 `null`：

```dart
String? nickname = null;
print(nickname); // null

nickname = 'Ada';
print(nickname); // Ada
```

不带 `?` 的类型称为**非空（non-nullable）**类型，带 `?` 的类型是**可空（nullable）**类型。

---

声明时**没有赋值**的可空变量初始为 `null`，所以 `= null` 可以省略：

```dart
int? age;
print(age); // null
```

非空变量没有这样的默认值：在赋值之前读取它的代码，Dart 会拒绝编译。

```dart
int count;
print(count); // error: 'count' must be assigned before it can be used
```

---

在 `null` 上调用方法或读取属性会导致崩溃，所以 Dart 不允许你用普通的点号在可空值上这样做：

```dart
String? text;
print(text.length); // error: the property 'length' can't be unconditionally accessed
```

**空安全访问**运算符 `?.` 解决了这个问题：如果值是 `null`，整个表达式就是 `null`，其余部分不会被求值；否则它就像普通的 `.` 一样工作：

```dart
String? text = 'Dart';
print(text?.length); // 4

text = null;
print(text?.length); // null
```

由于结果可能是 `null`，它的类型是可空的：`text?.length` 是 `int?`，而不是 `int`。

---

缺失的值常常应该用一个**默认值**来代替。**if-null** 运算符 `??` 在左操作数不是 `null` 时返回左操作数，否则返回右操作数：

```dart
String? nickname;
print(nickname ?? 'anonymous'); // anonymous

nickname = 'Ada';
print(nickname ?? 'anonymous'); // Ada
```

`??` 只对 `null` 起作用：空字符串 `''` 或数字 `0` 都是真实的值，因此会被保留。

`??` 与 `?.` 配合得很好，因为 `?.` 产生的是可空结果：

```dart
String? text;
print(text?.length ?? 0); // 0
```

---

空安全最大的好处是：大多数 `null` 错误由**编译器**发现，而不是由你的用户发现。目前学到的规则：

- 非空类型（`String`、`int`、`List<int>`...）永远不能是 `null`
- 可空类型（`String?`、`int?`、`List<int>?`...）可以，并且在声明时不赋值就以 `null` 开始
- 在可空值上使用 `.` 无法编译：请使用 `?.`，或用 `??` 提供默认值

---

**if-null 赋值**运算符 `??=` **仅当**变量当前为 `null` 时才给它赋值；否则保持原样：

```dart
int? retries;
retries ??= 3;
print(retries); // 3

retries ??= 10;
print(retries); // 3, it already had a value
```

它也适用于 map 的条目，因为键可能不存在，所以这些条目是可空的：

```dart
var stock = {'apple': 4};
stock['pear'] ??= 1;  // added
stock['apple'] ??= 9; // ignored
print(stock); // {apple: 4, pear: 1}
```

---

有时**你**知道某个可空值在某处不是 `null`，即使编译器无法判断。**空断言**运算符 `!` 通过承诺值一定存在，把 `String?` 转换成 `String`：

```dart
String? text = 'Dart';
String sure = text!;
print(sure.length); // 4
```

要小心：`!` 把检查从编译期挪到了运行期。如果值**确实**是 `null`，程序会抛出错误并停止：

```dart
String? text;
print(text!.length); // Null check operator used on a null value
```

请谨慎使用 `!`，只在那里出现 `null` 本来就是 bug 的情况下使用。

---

记住你已经见过的三个用于可空值的运算符之间的区别：

- `?.` 在值为 `null` 时返回 `null`，绝不抛出错误
- `??` 用默认值替换 `null`
- `!` 假定值一定存在，当它不存在时**在运行期抛出错误**

它们都不是编译错误：编译器信任你的 `!`，只有运行中的程序才能发现这个承诺被打破了。

---

用 `if` 检查可空值比用 `!` 更安全，Dart 也会为此奖励你。在像 `if (x != null)` 这样的检查之后，编译器知道在这个代码块内 `x` 不可能是 `null`，因此在那里把 `x` 当作非空类型处理。这称为**类型提升**：

```dart
int twice(int? n) {
  if (n != null) {
    return n * 2; // here n is an int, no ! needed
  }
  return 0;
}
```

提前返回之后同样会发生类型提升：

```dart
int twice(int? n) {
  if (n == null) return 0;
  return n * 2; // n is an int from here on
}
```

类型提升适用于**局部变量和参数**，它们的值不会在检查和使用之间被别处偷偷改掉。

---

类型提升**不**适用于可以从外部修改的类**字段**，因为在检查和使用之间，另一段代码（子类中被重写的 getter、另一个方法）可能又把它设回 `null`：

```dart
class Box {
  int? value;

  int doubled() {
    if (value != null) {
      return value * 2; // error: 'value' can't be unconditionally accessed
    }
    return 0;
  }
}
```

标准做法是把字段复制到一个**局部变量**中，局部变量是可以被提升的：

```dart
int doubled() {
  final v = value;
  if (v != null) {
    return v * 2;
  }
  return 0;
}
```

---

非空字段通常必须在构造函数中获得值。当这个值只有**稍后**才能知道时（读取文件之后、打开连接之后……），你可以把字段标记为 `late`：编译器接受缺少初始化器，并相信你会在读取之前给字段赋值。

```dart
class Connection {
  late String host;

  void open() {
    host = 'example.com';
  }
}
```

读取尚未赋值的 `late` 字段会在运行期抛出 `LateInitializationError`。和 `!` 一样，`late` 用编译期的保证换取运行期的检查，所以这是一个你必须遵守的承诺。

`late` 也可以和初始化器一起使用，此时初始化器会**惰性**执行，在变量第一次被读取时才运行：

```dart
late String report = buildReport(); // buildReport() runs only when report is used
```

---

可空性决定了你如何声明**命名参数**。类型可空的命名参数是可选的：调用方省略它时，它就是 `null`。

```dart
String label({String? title}) => title ?? 'untitled';

print(label());               // untitled
print(label(title: 'Notes')); // Notes
```

类型非空且没有默认值的命名参数在被省略时将没有值，所以 Dart 要求你把它标记为 `required`；这样调用方就必须始终传入它：

```dart
String label({required String name, String? title}) { ... }

label(name: 'Ada');               // ok
label(name: 'Ada', title: 'Dr.'); // ok
label(title: 'Dr.');              // error: the named parameter 'name' is required
```

---

可空性同样适用于集合的**元素**。`List<int>` 永远不包含 `null`，而 `List<int?>` 可以：

```dart
List<int?> scores = [7, null, 9];
```

注意它与 `List<int>?` 的区别：后者是列表本身可能缺失，但只要存在，里面就只有真正的数字。

要去掉 `null` 元素，`nonNulls` 会返回一个只包含存在值的 `Iterable`，其类型不带 `?`：

```dart
var present = scores.nonNulls.toList(); // List<int>
print(present); // [7, 9]
```

`whereType<int>()` 也能做到同样的事，并且在列表混合了多种类型时同样有效。

---

许多库函数用 `null` 来表示某件事**无法完成**。把字符串转换成数字是经典例子：当文本不是数字时，`int.parse` 会抛出 `FormatException`，而 `int.tryParse` 则返回 `null`，让你决定如何处理：

```dart
print(int.tryParse('42'));  // 42
print(int.tryParse('4x2')); // null
print(int.tryParse(''));    // null
```

`int.tryParse` 的返回类型是 `int?`，所以你学到的一切都适用：用 `??` 提供默认值，用 `?.` 链式调用，用 `if` 检查来实现类型提升。`double.tryParse` 的工作方式相同。

---

还有两个运算符拥有空安全变体。

**空安全级联** `?..` 只在对象不是 `null` 时才执行整条级联操作链，否则全部跳过：

```dart
List<int>? numbers;
numbers?..add(1)..add(2); // nothing happens, numbers is still null
```

**空安全展开** `...?` 把可空集合的元素插入到字面量中；当集合为 `null` 时则什么也不添加：

```dart
List<int>? extra;
print([0, ...?extra]); // [0]

extra = [1, 2];
print([0, ...?extra]); // [0, 1, 2]
```

如果没有 `?`，在 `List<int>?` 上写 `...extra` 会是编译错误。

---

真实数据中到处是缺口：留空的表单字段、文件中缺失的一列、算不上数字的字符串。本章的工具可以自然地组合起来处理它们：用 `nonNulls` 丢弃缺失的元素，用 `int.tryParse` 安全地转换，用 `??` 或 `if` 检查来处理无法转换的内容。
