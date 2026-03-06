类型允许你对代码中使用的所有不同数据类型进行分类。
在 Dart 中，__类型__是一种告诉编译器你将如何使用给定数据的方式。
以下是 Dart 支持的一些类型示例：
- int
- String
- double
- dynamic
- num

Dart 支持许多其他类型。上面列出的是你将使用的主要类型。

---

你可以显式定义变量的类型，例如：
```dart
int integerNumber = 2;
double decimalNumber = 3.14;
```

---

具有显式类型的变量也可以是常量，只需在类型前添加 `const` 或 `final` 关键字：
```dart
const int integerNumber = 2;
final double decimalNumber = 3.14;
```

> 注意：可变数据允许你随时轻松更改它。然而，许多有经验的程序员更欣赏不可变数据的好处。当一个值是不可变的，你可以确信在创建它之后没有人能够更改该值。以这种方式限制你的数据可以防止许多难以发现的错误，并使程序更容易理解和测试。

---

虽然可以标注变量的类型，但这是多余的。你知道 `10` 是 `int` 类型，`3.14` 是 `double` 类型。Dart 编译器能够通过__类型推断__来推断它。并非所有编程语言都有_类型推断_，这使得 Dart 成为一种非常强大的编程语言。

你可以简单地从变量中移除类型，例如：
```dart
const integerNumber = 2;
final decimalNumber = 3.14;
```

当变量的类型没有被显式标注时，Dart 会尝试推断其类型。

---

有一种编程方式可以检查变量的类型，即使用 `is` 关键字：
```dart
final number = 3.14;
print(number is int); // false
print(number is double); // true
```

如你所见，Dart 已将 `double` 类型分配给变量 `number`。

---

`is` 关键字允许你检查变量是否为你定义的类型。但你也可以使用 `is!` 关键字检查变量是否不是定义的类型：
```dart
final number = 3.14;
print(number is! int); // true
```

---

查看_运行时_变量类型的另一种方法是使用 `runtimeType` 属性，该属性对所有类型都可用。
```dart
final number = 3.14;
print(number.runtimeType); // double
```

---

有时你会遇到这样的情况：拥有一种类型，但需要将其转换为另一种类型。你可能会想这样做：

```dart
var integer = 5;
var decimal = 3.14;
integer = decimal;
```

但 Dart 会报错：
> Error: A value of type 'double' can't be assigned to a variable of type 'int'.

一些编程语言没有这么严格，会默默地进行转换。经验表明，这种隐式转换是错误和性能问题的常见来源。Dart 禁用了此功能以避免这些问题。

记住，计算机依赖程序员来决定该做什么。在 Dart 中，这包括明确指定类型转换。

与其期望 Dart 进行隐式转换，你需要明确告诉 Dart 你想要进行类型转换。以下是将 `double` 数字转换为 `int` 的方法：
```dart
var integer = decimal.toInt();
```

该赋值明确告诉 Dart，你想从原始类型 `double` 转换为新类型 `int`。

> 注意：在这种情况下，将小数值赋给整数会损失精度。变量 `integer` 的值为 __3__ 而不是 __3.14__。这就是为什么明确指定很重要。Dart 想要确认你知道自己在做什么，并告知你转换时会丢失信息。

---

到目前为止，我们已经看到运算符分别独立用于整数或小数。如果你有一个整数需要与一个小数相乘呢？让我们看一个示例：
```dart
const radius = 5;
const pi = 3.14;
const circumference = 2 * pi * radius;
```

`radius` 是 `int` 类型，而 `pi` 是 `double` 类型。`circumference` 的类型是什么？Dart 会将 `double` 类型分配给变量 `circumference`。这是更安全的选择，因为如果将其设为 `int` 类型，可能会导致精度损失。

如果你想要一个 `int` 类型的结果，你需要显式进行转换：
```dart
const circumference = (2 * pi * radius).toInt();
```

括号告诉 Dart 先进行乘法运算，然后获取结果并将其转换为整数值。不幸的是，分析器不会喜欢这段代码：
 > Const variables must be initialized with a constant value.

问题在于 `toInt` 方法是仅在运行时使用的方法。这意味着 `circumference` 变量无法在编译时确定，因此变量不能是常量。要修复这个问题，将 `const` 替换为 `final`：

```dart
final circumference = (2 * pi * radius).toInt();
```

现在 `circumference` 是一个 `int` 类型的__运行时常量__变量。

---

有时你可能有一个通用类型的变量，但需要仅存在于子类型中的功能。如果你确定变量的类型是你需要的子类型，那么可以使用 `as` 关键字来更改其类型。这个过程也被称为__类型转换__，以下是一个示例：

```dart
num number = 3;
```

假设我们想检查这个数字是否为偶数，而相关功能仅存在于 `int` 子类型中。
```dart
print(number.isEven);
```

上面的代码会返回一个类型错误：
> The getter `isEven` isn't defined for the type 'num'.

`num` 类型过于通用，无法知道一个数字是偶数还是奇数。只有整数才能是偶数或奇数。
如果 `num` 包含 `double` 值就会出现问题，因为 `num` 同时包含 `double` 和 `int` 类型。在这种情况下，我们确定 __3__ 是一个整数，所以可以转换为 `int`：

```dart
final integer = number as int;
print(integer.isEven); // false
```

`as` 关键字使编译器将变量 `integer` 识别为 `int` 类型。这允许你使用整数上存在的 `isEven` 属性。由于数字 __3__ 不是偶数，结果为 false。

进行类型转换时必须小心。如果你错误地转换了类型，会得到一个运行时错误：
```dart
num numero = 3;
final decimale = numero as double;
```

这将导致程序崩溃，错误如下：
> CastError (type 'int' is not a subtype of type 'double' in type cast)

`number` 的运行时类型是 `int` 而不是 `double`。在 Dart 中，你不能在同级类型之间进行转换，如 `int` 和 `double`。你只能转换子类型。
