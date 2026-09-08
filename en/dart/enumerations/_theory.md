An **enumeration** (or *enum*) defines a common type for a group of related values, so you can work with those values in a type-safe way. In Dart you declare one with the `enum` keyword, listing its **values** separated by commas:

```dart
enum Direction { north, south, east, west }
```

By convention value names are written in `lowerCamelCase`, like variables. Each value is accessed through the enum name, and printing it shows both the enum and the value:

```dart
var heading = Direction.north;
print(heading); // Direction.north
```

An enum must be declared at the **top level** of a file, never inside a function such as `main`.

---

Every enum value has two built-in properties:

- `name` is the value's name as a `String`
- `index` is its position in the declaration, starting from `0`

```dart
enum Direction { north, south, east, west }

print(Direction.east.name);  // east
print(Direction.east.index); // 2
```

---

Every enum also has a constant list called `values` that holds all of its values in declaration order. You can index it like any list, read its `length`, or loop over it with `for-in`:

```dart
enum Direction { north, south, east, west }

print(Direction.values.length); // 4
print(Direction.values[1]);     // Direction.south

for (var direction in Direction.values) {
  print(direction.name);
}
```

---

Because `values` is a list, you can combine it with the list methods you already know. For example `.map()` with `.name` turns the values into a list of strings:

```dart
enum Direction { north, south, east, west }

List<String> names = Direction.values.map((d) => d.name).toList();
print(names); // [north, south, east, west]
```

---

Looping over `values` is the usual way to process every value of an enum. Inside the loop the current value behaves like any other object, so you can read its `index` and its `name` and use them directly in a string interpolation:

```dart
enum Direction { north, south, east, west }

for (var direction in Direction.values) {
  print('${direction.index}: ${direction.name}');
}
```

---

Each enum value exists exactly once, so two references to the same value are always equal. Compare them with `==` and `!=`:

```dart
enum Direction { north, south, east, west }

var heading = Direction.north;
print(heading == Direction.north); // true
print(heading != Direction.south); // true
print(Direction.values[0] == heading); // true
```

---

A `switch` statement is the natural way to branch over an enum, with one `case` per value:

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

When the cases cover **every** value the switch is *exhaustive* and needs no `default`. If you forget a value, the compiler reports an error instead of letting the bug reach runtime.

---

Since Dart 3 a `switch` can also be used as an **expression** that produces a value. Each case is written as `pattern => value` and the cases are separated by commas, with no `case` keyword and no `break`:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) => switch (direction) {
      Direction.north => '^',
      Direction.south => 'v',
      Direction.east => '>',
      Direction.west => '<',
    };
```

Like the statement form, a switch expression over an enum must be exhaustive.
