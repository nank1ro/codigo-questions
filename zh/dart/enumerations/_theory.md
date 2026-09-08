**枚举**（或 *enum*）为一组相关的值定义了一个共同的类型，让你可以以类型安全的方式使用这些值。在 Dart 中，你使用 `enum` 关键字来声明枚举，用逗号分隔列出它的**值**：

```dart
enum Direction { north, south, east, west }
```

按照惯例，值的名称使用 `lowerCamelCase` 书写，就像变量一样。每个值都通过枚举名访问，打印它会同时显示枚举和值：

```dart
var heading = Direction.north;
print(heading); // Direction.north
```

枚举必须声明在文件的**顶层**，绝不能在像 `main` 这样的函数内部声明。

---

每个枚举值都有两个内置属性：

- `name` 是该值的名称，类型为 `String`
- `index` 是它在声明中的位置，从 `0` 开始

```dart
enum Direction { north, south, east, west }

print(Direction.east.name);  // east
print(Direction.east.index); // 2
```

---

每个枚举还有一个名为 `values` 的常量列表，按声明顺序保存它的所有值。你可以像操作任何列表一样对它进行索引、读取它的 `length`，或者用 `for-in` 遍历它：

```dart
enum Direction { north, south, east, west }

print(Direction.values.length); // 4
print(Direction.values[1]);     // Direction.south

for (var direction in Direction.values) {
  print(direction.name);
}
```

---

因为 `values` 是一个列表，你可以将它与你已经了解的列表方法结合使用。例如，`.map()` 配合 `.name` 可以把值转换成字符串列表：

```dart
enum Direction { north, south, east, west }

List<String> names = Direction.values.map((d) => d.name).toList();
print(names); // [north, south, east, west]
```

---

遍历 `values` 是处理枚举全部值的常用方式。在循环中，当前值和其他对象一样，因此你可以读取它的 `index` 和 `name`，并直接用在字符串插值中:

```dart
enum Direction { north, south, east, west }

for (var direction in Direction.values) {
  print('${direction.index}: ${direction.name}');
}
```

---

每个枚举值都只存在一份，因此两个指向同一个值的引用总是相等的。使用 `==` 和 `!=` 比较它们：

```dart
enum Direction { north, south, east, west }

var heading = Direction.north;
print(heading == Direction.north); // true
print(heading != Direction.south); // true
print(Direction.values[0] == heading); // true
```

---

`switch` 语句是对枚举进行分支处理的自然方式，每个值对应一个 `case`：

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) {
  switch (direction) {
    case Direction.north:
      return '^';
    case Direction.south:
      return 'v';
    case Direction.east:
      return '>';
    case Direction.west:
      return '<';
  }
}
```

当所有 `case` 覆盖了**所有**值时，这个 switch 就是*穷举的*，不需要 `default`。如果你遗漏了某个值，编译器会报错，而不是让这个 bug 一直存在到运行时。

---

从 Dart 3 开始，`switch` 也可以用作能产生值的**表达式**。每个 case 写成 `模式 => 值` 的形式，各个 case 之间用逗号分隔，不需要 `case` 关键字，也不需要 `break`：

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) => switch (direction) {
      Direction.north => '^',
      Direction.south => 'v',
      Direction.east => '>',
      Direction.west => '<',
    };
```

和语句形式一样，作用于枚举的 switch 表达式也必须是穷举的。
