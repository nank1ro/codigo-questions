你已经知道如何给自己编写的类添加方法。但 `String`、`int` 或 `List` 呢？它们的代码位于 Dart SDK 中。你无法修改它们，却常常希望它们能多一个方法。

**扩展**解决了这个问题：它为一个**现有**类型添加新的成员，无需改动其源代码，也无需创建子类。语法如下：

```dart
extension ExtensionName on Type {
  // new methods and getters
}
```

在扩展内部，`this` 指代调用该成员的值。扩展一旦声明，其成员的调用方式与类型自身的成员完全相同：

```dart
extension Greeting on String {
  String greet() => 'Hello, $this!';
}

void main() {
  var name = 'Ada';
  print(name.greet()); // Hello, Ada!
}
```

扩展声明在文件的**顶层**，与类和函数并列，绝不在 `main` 内部。

---

扩展适用于任何类型，包括数字。下面这个扩展为每个 `int` 提供了一个让它翻倍的方法：

```dart
extension Doubling on int {
  int doubled() => this * 2;
}
```

由于扩展作用于**类型**，你既可以在变量上调用该方法，也可以直接在**字面量**上调用。负数字面量需要加括号，否则点号会先于负号被解析：

```dart
var n = 21;
print(n.doubled());    // 42
print(4.doubled());    // 8
print((-3).doubled()); // -6
```

---

扩展还可以声明 **getter**，它们像属性一样被读取，无需括号。在扩展内部，你可以直接调用类型自身的成员：`this.` 是可选的，与在类内部完全一样。

```dart
extension Sizes on String {
  bool get isLong => length > 10;      // same as this.length
  String get firstChar => this[0];
}

void main() {
  print('Dart'.isLong);           // false
  print('extension'.firstChar);   // e
}
```

当成员只是**读取**一个值且不接受参数时，请选择 getter；当它需要执行操作或需要参数时，请选择方法。

---

`on` 后面的类型可以是**参数化**类型，例如 `List<int>`。这时扩展只适用于该元素类型的列表：`[1, 2].total()` 可以运行，`['a', 'b'].total()` 则无法编译。

```dart
extension Totals on List<int> {
  int total() {
    var sum = 0;
    for (final n in this) {
      sum += n;
    }
    return sum;
  }
}
```

在扩展内部，`this` 就是这个列表，因此你可以像往常一样遍历它、按索引访问它，或调用 `length`。

---

作用于 `List<int>` 的扩展不能用在 `List<String>` 上。要编写一个对**任意**元素类型都有效的扩展，可以给扩展一个**类型参数**，写在它名字后面的尖括号中，并在 `on` 的类型里使用它：

```dart
extension Firsts<T> on List<T> {
  T get firstOrLast => length > 1 ? this[0] : this[length - 1];
}
```

`T` 是“元素类型是什么”的占位符：在 `List<int>` 上它就是 `int`，在 `List<String>` 上它就是 `String`，因此上面的 getter 会相应地返回 `int` 或 `String`。编译器会在每次调用时替你填入 `T`。

```dart
print([7, 8, 9].firstOrLast); // 7
print(['a', 'b'].firstOrLast); // a
```

---

作用于 `String` 的扩展不能在 `String?` 上调用：值可能是 `null`，编译器会拒绝这次调用。如果把扩展声明在**可空**类型上，方法就可以直接在 `String?` 上调用，此时内部的 `this` 类型是 `String?`，因此你必须自己处理 `null` 的情况，例如用 `??`：

```dart
extension Defaults on int? {
  int orZero() => this ?? 0;
}

void main() {
  int? count = null;
  print(count.orZero()); // 0
  print(5.orZero());     // 5
}
```

在需要 `int?` 的地方可以传入非空的 `int`，所以这个扩展对两者都有效。

---

扩展可以添加方法、getter、setter 和运算符，但**不能添加实例字段**。一个 `int` 值在内存中的布局是固定的，而扩展只是编译器允许你用点语法调用的一组函数：没有地方可以为每个值存储额外的数据。

```dart
extension Counter on int {
  int count = 0; // error: extensions can't declare instance fields
}
```

扩展中的 getter 和 setter 只能从 `this` 计算值，或转发给已有的成员：它们无法在两次调用之间记住任何东西。

---

扩展可以声明 **static** 成员。与类中一样，它们属于扩展本身而不是任何值，并且要通过**扩展的名字**来访问，而不是通过它所扩展的类型：

```dart
extension Temperatures on double {
  static const double boiling = 100.0;

  static bool isBoiling(double celsius) => celsius >= boiling;
}

void main() {
  print(Temperatures.boiling);         // 100.0
  print(Temperatures.isBoiling(37.5)); // false
  print(double.boiling);               // error: 'boiling' isn't defined for 'double'
}
```

静态成员是存放与被扩展类型相关的常量和辅助函数的好地方。

---

扩展不仅适用于 SDK 类型：你也可以扩展**自己的类**。当类来自一个你无法控制的包，或者你想让类保持精简、把可选的辅助功能放在需要它们的代码旁边时，这会很有用。

```dart
class Circle {
  final double radius;
  Circle(this.radius);
}

extension CircleMath on Circle {
  double get diameter => radius * 2;
}

void main() {
  print(Circle(3).diameter); // 6.0
}
```

扩展可以看到类的公共字段和方法，与写在类外面的代码完全一样。

---

Dart 允许一个类型定义 `+`、`*` 或 `==` 这类运算符对它的值意味着什么，做法是使用一个名字为关键字 `operator` 加上符号的方法。运算符的右侧就是方法的参数：

```dart
extension Scaling on List<int> {
  List<int> operator *(int factor) => map((n) => n * factor).toList();
}

void main() {
  print([1, 2, 3] * 10); // [10, 20, 30]
}
```

由于扩展可以声明运算符，你可以给现有类型添加一个它还没有的新运算符。`String` 有 `+` 和 `*`，但没有 `-`，所以扩展可以定义 `'hello world' - 'o'` 的含义。

---

如果扩展声明的成员是类型**已经拥有**的成员会怎样？类型自己的成员总是胜出：只有当类型本身没有同名成员时，才会考虑扩展的成员。扩展的成员会被静默忽略，既不会报错，也不存在重写。

```dart
extension Shorter on String {
  int get length => 0;
}

void main() {
  print('four'.length); // 4, String's own length is used
}
```

所以扩展可以添加成员、填补空缺，但永远无法**改变**现有成员的行为。

---

扩展的名字是可选的。**未命名**的扩展工作方式相同，但只在声明它的文件中可见：

```dart
extension on int {
  bool get isTriple => this % 3 == 0;
}
```

一旦两个扩展在同一类型上提供相同的成员，**名字**就变得重要了：调用会变得**有歧义**，无法编译。名字让你可以用两种方式解决冲突。当扩展来自不同文件时，可以在 import 中 `show` 或 `hide` 其中一个：

```dart
import 'package:loud/loud.dart';
import 'package:quiet/quiet.dart' hide Quiet;
```

或者，在任何地方，你都可以**显式**应用扩展，把值用扩展名包裹起来，就像调用构造函数一样：

```dart
print(Loud('hi').describe());
```

未命名的扩展无法被隐藏或显式应用，所以在会被他人 import 的代码中请优先使用命名的扩展。

---

泛型扩展可以接受**函数**作为参数，与 `where` 和 `map` 的做法完全一样。函数类型用元素类型 `T` 来书写，因此回调收到的元素具有正确的类型：

```dart
extension Checks<T> on List<T> {
  bool all(bool Function(T) test) {
    for (final item in this) {
      if (!test(item)) return false;
    }
    return true;
  }
}

void main() {
  print([2, 4, 6].all((n) => n.isEven)); // true
}
```
