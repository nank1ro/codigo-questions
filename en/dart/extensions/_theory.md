You know how to add methods to a class you wrote yourself. But what about `String`, `int` or `List`, whose code lives in the Dart SDK? You cannot edit them, yet you often wish they had one more method.

An **extension** solves this: it adds new members to an **existing** type, without touching its source code and without creating a subclass. The syntax is:

```dart
extension ExtensionName on Type {
  // new methods and getters
}
```

Inside the extension, `this` refers to the value the member is called on. Once the extension is declared, its members are called exactly like the type's own members:

```dart
extension Greeting on String {
  String greet() => 'Hello, $this!';
}

void main() {
  var name = 'Ada';
  print(name.greet()); // Hello, Ada!
}
```

Extensions are declared at the **top level** of a file, next to classes and functions, never inside `main`.

---

Extensions work on any type, including numbers. This extension gives every `int` a method that doubles it:

```dart
extension Doubling on int {
  int doubled() => this * 2;
}
```

Because the extension applies to the **type**, you can call the method on a variable or directly on a **literal**. Negative literals need parentheses, otherwise the dot is read before the minus sign:

```dart
var n = 21;
print(n.doubled());    // 42
print(4.doubled());    // 8
print((-3).doubled()); // -6
```

---

An extension can also declare **getters**, which are read like properties, without parentheses. Inside an extension you can call the type's own members directly: `this.` is optional, exactly as inside a class.

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

Choose a getter when the member only **reads** a value and takes no parameters; choose a method when it does work or needs arguments.

---

The type after `on` can be a **parameterized** type such as `List<int>`. The extension then applies only to lists of that element type: `[1, 2].total()` works, `['a', 'b'].total()` does not compile.

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

Inside the extension, `this` is the list, so you can loop over it, index it, or call `length` as usual.

---

An extension on `List<int>` cannot be used on a `List<String>`. To write one extension that works for **every** element type, give the extension a **type parameter**, written between angle brackets after its name, and use it in the `on` type:

```dart
extension Firsts<T> on List<T> {
  T get firstOrLast => length > 1 ? this[0] : this[length - 1];
}
```

`T` is a placeholder for "whatever the element type is": on a `List<int>` it becomes `int`, on a `List<String>` it becomes `String`, so the getter above returns an `int` or a `String` accordingly. The compiler fills in `T` for you at each call.

```dart
print([7, 8, 9].firstOrLast); // 7
print(['a', 'b'].firstOrLast); // a
```

---

An extension on `String` cannot be called on a `String?`: the value might be `null`, and the compiler refuses the call. If you declare the extension on the **nullable** type instead, the method can be called on a `String?` directly, and inside it `this` has type `String?`, so you must handle the `null` case yourself, for example with `??`:

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

A non-nullable `int` can be passed where an `int?` is expected, so the extension works on both.

---

An extension can add methods, getters, setters and operators, but it **cannot add instance fields**. An `int` value has a fixed layout in memory, and an extension is only a set of functions the compiler lets you call with the dot syntax: there is no place to store extra data per value.

```dart
extension Counter on int {
  int count = 0; // error: extensions can't declare instance fields
}
```

Getters and setters in an extension can only compute values from `this` or forward to existing members: they cannot remember anything between calls.

---

An extension can declare **static** members. As in a class, they belong to the extension itself, not to any value, and they are accessed through the **extension's name**, not through the type it extends:

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

Static members are a handy place for constants and helper functions related to the extended type.

---

Extensions are not only for SDK types: you can extend **your own classes** too. This is useful when the class comes from a package you do not control, or when you want to keep the class small and add optional helpers next to the code that needs them.

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

The extension sees the class's public fields and methods, exactly like code written outside the class.

---

Dart lets a type define what operators like `+`, `*` or `==` mean for its values, using a method whose name is the keyword `operator` followed by the symbol. The right-hand side of the operator is the method's parameter:

```dart
extension Scaling on List<int> {
  List<int> operator *(int factor) => map((n) => n * factor).toList();
}

void main() {
  print([1, 2, 3] * 10); // [10, 20, 30]
}
```

Since extensions can declare operators, you can give an existing type a new operator it does not already have. `String` has `+` and `*`, but no `-`, so an extension can define what `'hello world' - 'o'` means.

---

What if an extension declares a member that the type **already has**? The type's own member always wins: extension members are only considered when the type itself has no member with that name. The extension member is silently ignored, there is no error and no override.

```dart
extension Shorter on String {
  int get length => 0;
}

void main() {
  print('four'.length); // 4, String's own length is used
}
```

So an extension can add members and fill gaps, but it can never **change** how existing members behave.

---

The name of an extension is optional. An **unnamed** extension works the same way, but it is only visible in the file that declares it:

```dart
extension on int {
  bool get isTriple => this % 3 == 0;
}
```

A **name** matters as soon as two extensions offer the same member on the same type: the call becomes **ambiguous** and does not compile. The name lets you resolve the conflict in two ways. When the extensions come from different files, you can `show` or `hide` one of them in the import:

```dart
import 'package:loud/loud.dart';
import 'package:quiet/quiet.dart' hide Quiet;
```

Or, anywhere, you can apply the extension **explicitly**, by wrapping the value in the extension name as if it were a constructor:

```dart
print(Loud('hi').describe());
```

Unnamed extensions cannot be hidden or applied explicitly, so prefer named extensions in code that others will import.

---

A generic extension can take **functions** as parameters, exactly like `where` and `map` do. The function type is written with the element type `T`, so the callback receives elements of the right type:

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
