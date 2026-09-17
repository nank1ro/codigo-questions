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

---

从 Dart 2.17 开始，枚举可以像类一样声明**字段**和**构造函数**。这被称为*增强枚举*。每个值会向构造函数传入自己的参数：

```dart
enum Planet {
  mercury(0),
  earth(1),
  mars(2);

  final int moons;

  const Planet(this.moons);
}

print(Planet.mars.moons); // 2
```

注意这三条规则：值列表以**分号** `;` 结尾，字段必须是 `final`，构造函数必须是 `const`。

---

增强枚举还可以声明**方法**和 **getter**。在它们内部，`this` 就是当前值，因此你可以直接使用它的 `name`、`index` 和字段：

```dart
enum Planet {
  mercury(0),
  earth(1),
  mars(2);

  final int moons;

  const Planet(this.moons);

  bool get hasMoons => moons > 0;

  String describe() => '$name has $moons moon(s)';
}

print(Planet.earth.hasMoons);   // true
print(Planet.mars.describe()); // mars has 2 moon(s)
```

没有字段的枚举仍然可以声明方法：这时值列表以 `;` 结尾，后面跟着成员。

---

要从 `String` 转换回枚举值，可以在 `values` 列表上调用 `byName`。它会返回 `name` 完全匹配的那个值：

```dart
enum Direction { north, south, east, west }

var direction = Direction.values.byName('east');
print(direction == Direction.east); // true
```

如果没有值具有该名称，`byName` 会抛出 `ArgumentError`。当字符串来自用户输入时，`asNameMap()` 是更安全的选择：它返回一个从名称到值的 `Map<String, Direction>`，因此查找一个未知名称会得到 `null` 而不是错误：

```dart
print(Direction.values.asNameMap()['up']); // null
```

---

枚举值是极好的 **map 键**：它们是唯一的、易于比较，并且编译器会检查你只使用真实存在的值。将枚举声明为键类型来创建 map，并使用 `[]` 查找值：

```dart
enum Direction { north, south, east, west }

Map<Direction, String> arrows = {
  Direction.north: '^',
  Direction.south: 'v',
  Direction.east: '>',
  Direction.west: '<',
};

print(arrows[Direction.east]); // >
```

和任何 map 一样，当键不存在时查找会返回 `null`，因此使用 `??` 提供一个回退值。

---

枚举可以使用 `implements` 关键字**实现一个接口**。这样枚举就承诺提供接口声明的每一个成员，并且它的值可以用在任何期望该接口类型的地方：

```dart
abstract class Describable {
  String describe();
}

enum Animal implements Describable {
  dog,
  cat;

  @override
  String describe() => 'I am a $name';
}

Describable pet = Animal.cat;
print(pet.describe()); // I am a cat
```

接口中声明的 getter 既可以用 getter 实现，也可以用同名的 `final` 字段实现。
