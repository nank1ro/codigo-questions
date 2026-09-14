`List` 并不只是存放值，它存放的是**同一种类型**的值。类型写在尖括号里，紧跟在集合名称的后面：

```dart
List<String> names = ['Ada', 'Grace'];
List<int> scores = [10, 20];
```

这里的 `String` 和 `int` 是**类型实参**，而接受类型实参的类型称为**泛型**。列表类只编写一次，`List<String>` 和 `List<int>` 则是由它产生的两个不同的类型。

这样做的好处是编译器知道里面装的是什么：

```dart
names.add(42);          // error: 42 is not a String
print(names.first.toUpperCase()); // fine: first is a String
```

---

`List` 并不是唯一的泛型集合。`Set` 接受一个类型实参，而 `Map` 接受**两个**：一个对应键，一个对应值，按此顺序。

```dart
Set<String> tags = {'new', 'sale'};
Map<String, int> ages = {'Ada': 36, 'Grace': 45};
```

空的集合字面量无法从其内容推断出类型，所以要把类型实参写在字面量本身上：

```dart
final counts = <String, int>{};
final seen = <String>{};
counts['fig'] = 3;
```

一旦类型确定，从集合中取出的每个值都已经具有正确的类型：`ages['Ada']` 是一个 `int?`，绝不是来历不明的值。

---

Dart 还有 `dynamic` 类型，它的意思是“什么都可以”。`List<dynamic>` 接受任何值，所以看起来比 `List<String>` 更方便：

```dart
List<dynamic> things = ['Ada', 'Grace'];
things.add(42);                    // accepted
print(things.first.toUpperCase()); // accepted
```

代价是编写代码时什么都不会被检查。对 `dynamic` 值的每次调用都是在程序运行时才解析的，所以像 `things.first.toUpperCse()` 这样的拼写错误也能顺利编译，然后在用户面前崩溃。

泛型是另一种选择：一份代码可以处理**任意**类型，同时每次使用时仍会针对**某一种**类型进行检查。这正是本主题的全部意义所在。

---

你并不局限于 Dart 自带的泛型类：你也可以声明自己的泛型类。**类型参数**放在类名后面的尖括号中，从此它在类体内就是一个普通的类型：

```dart
class Box<T> {
  final T value;

  Box(this.value);

  T unwrap() => value;
}
```

`T` 只是一个占位符。它在创建 `Box` 时被填充，可以是显式指定，也可以通过推断得出：

```dart
final a = Box<int>(7);   // Box<int>
final b = Box('fig');    // Box<String>, inferred from the argument
print(a.value + 1);      // 8, the compiler knows value is an int
```

字母本身并不重要：`T` 只是“类型”的一种约定，仅此而已。

---

函数本身也可以是泛型的，而不必位于泛型类中。类型参数写在名称与参数列表之间：

```dart
T firstOf<T>(List<T> items) => items.first;

print(firstOf(['fig', 'kiwi'])); // fig, T is String here
print(firstOf([10, 20]));        // 10, T is int here
```

一份函数体，只检查一次，即可为每种类型复用。类型实参通常从参数推断得出，但当推断无据可依时，也可以显式写出：

```dart
final empty = firstOf<String>(<String>[]); // throws, but the type is clear
```

类中的方法遵循完全相同的规则。

---

在泛型类内部，类型参数处处可见：在字段中、在构造函数参数中、在方法签名中以及在方法体中。它只声明一次，就在类名旁边，之后每个成员都可以使用它。

```dart
class Holder<T> {
  final T item;

  Holder(this.item);

  String describe() => 'holding $item';
}
```

创建对象时才决定类型：`Holder<String>('fig')` 使 `item` 成为 `String`，`Holder<int>(3)` 使它成为 `int`。

---

一个类可以声明多个类型参数，用逗号分隔。`Map<K, V>` 是内置的例子：一个类型对应键，一个类型对应值。

```dart
class Entry<K, V> {
  final K key;
  final V value;

  Entry(this.key, this.value);
}

final e = Entry<String, int>('age', 30);
```

**顺序**是类型的一部分：`Entry<String, int>` 和 `Entry<int, String>` 是互不相关的类型，一个类型的值不能赋给另一个。类型参数还可以在返回类型中重新排列，方法正是借此返回一个调换了顺序的对象版本：

```dart
Entry<V, K> get flipped => Entry(value, key);
```

---

在健全的空安全下，问号可以出现在两个不同的位置，而它们表示两种不同的含义：

```dart
Box<int?> a = Box(null); // a box that exists and holds a nullable int
Box<int>? b = null;      // no box at all, but if there is one it holds an int
```

在 `Box<int?>` 中，**类型实参**是可空的，所以 `a.value` 的类型是 `int?`，可能是 `null`，而 `a` 本身始终存在。在 `Box<int>?` 中，**变量**是可空的，所以 `b` 可能是 `null`，你需要 `b?.value` 或 `b!.value` 才能访问它的内部。

不带边界的 `T` 意味着 `T extends Object?`，所以像 `Box<int?>` 这样可空的类型实参是完全合法的。

---

一旦使用这个值，区别就会显现。在 `Box<int?>` 上你可以正常访问字段，然后再处理其中的 `null`；而在 `Box<int>?` 上，你必须先越过“盒子缺失”这一关：

```dart
Box<int?> a = Box(null);
print(a.value ?? 0); // 0, the box is there, its content is null

Box<int>? b = null;
print(b?.value ?? 0); // 0, the box itself is missing
```

在 `Box<int>?` 上写 `b.value` 根本无法编译：Dart 拒绝读取可能不存在的东西的字段。

---

没有边界的 `T` 可以是任何东西，所以在函数体内你只能使用每个对象都有的东西。下面的代码无法编译：

```dart
T twice<T>(T value) => value + value; // error: + is not defined for T
```

**边界**可以解决这个问题。写 `T extends num` 就是说“`T` 只能是数字”，作为交换，函数体可以使用 `num` 提供的一切：

```dart
T twice<T extends num>(T value) => (value + value) as T;

num half<T extends num>(T value) => value / 2;
```

边界在调用处检查：`half(4)` 和 `half(2.5)` 没问题，`half('fig')` 则是编译期错误。边界是一个双向的承诺：调用方接受更窄的实参范围，换取函数体内更强的能力。

---

表示边界的关键字始终是 `extends`，即使边界是接口而不是父类。类型参数列表中没有 `implements`。

```dart
num biggerOf<T extends num>(T a, T b) => a > b ? a : b;
```

没有边界的话，`a > b` 将无法编译：比较运算符属于 `num`，而不是每个对象都有。

---

边界还可以提到类型参数本身。`Comparable<T>` 是所有懂得如何通过 `compareTo` 与自己同种类型进行比较的东西的接口：

```dart
print('fig'.compareTo('kiwi')); // negative: fig comes first
print('kiwi'.compareTo('fig')); // positive
print('fig'.compareTo('fig'));  // zero
```

所以 `T extends Comparable<T>` 应读作“任何可以与自身比较的类型”，这正是排序或求最大值的函数所需要的：

```dart
T maxOf<T extends Comparable<T>>(T a, T b) => a.compareTo(b) >= 0 ? a : b;

print(maxOf('fig', 'kiwi')); // kiwi
```

`String` 和 `DateTime` 都直接满足它。`int` 和 `double` 实现的是 `Comparable<num>`，所以数字列表直接作为 `num` 来比较。

---

同样的边界也完全适用于求最小的元素：只是比较结果的符号变了。当接收者排在前面时，`compareTo` 返回负数，所以 `item.compareTo(best) < 0` 表示“这个更小”。

---

泛型类可以像其他类一样拥有命名构造函数和**工厂构造函数**，而且类型参数在它们内部同样可用。工厂构造函数并不亲自创建对象：它运行一个函数体并返回一个实例，因此可以随意选择、复用或以任何方式构建实例。

```dart
class Box<T> {
  final T value;

  Box(this.value);

  factory Box.first(List<T> items) => Box(items.first);
}

final b = Box<int>.first([5, 6]);
print(b.value); // 5
```

类型实参写在类上，而不是构造函数名上：`Box<int>.first(...)`。在工厂内部，`<T>[]` 是一个真正的空 `List<T>`，所以工厂是为尚未知道的类型构建默认值的理想场所。

---

不带边界写的类型参数根本不是没有边界：`class Box<T>` 是 `class Box<T extends Object?>` 的简写。这正是 `Box<int?>` 被接受的原因，也是在类内部你绝不能假设 `value` 非空的原因。

要禁止可空的类型实参，就用 `Object` 为参数设置边界：

```dart
class Strict<T extends Object> {
  final T value;
  Strict(this.value);
}

final ok = Strict<int>(7);
final bad = Strict<int?>(null);
// error: Type argument 'int?' doesn't conform to the bound 'Object'
```

`Object` 是除 `null` 之外一切东西的类型，所以 `T extends Object` 应读作“任何东西，只要它确实存在”。

---

`typedef` 为一个类型起一个名字，而且它可以拥有自己的类型参数。通常的理由是给一族函数类型只命名一次，而不必在每次使用时都把它完整写出来：

```dart
typedef Transform<I, O> = O Function(I input);

final Transform<String, int> length = (word) => word.length;
print(length('kiwi')); // 4
```

`Transform<String, int>` 只是 `int Function(String)` 的另一种写法，两者可以互换。收益在于可读性：声明为 `Transform<I, O> transform` 的参数说明了这个函数是做什么用的，而 `O Function(I)` 只说明了它长什么样。

泛型 typedef 和泛型函数可以自然地组合，由函数自己的类型参数填入 typedef 的类型参数。
