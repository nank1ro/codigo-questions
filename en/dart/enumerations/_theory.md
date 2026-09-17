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

---

Since Dart 2.17 an enum can declare **fields** and a **constructor**, just like a class. This is called an *enhanced enum*. Each value then passes its own arguments to the constructor:

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

Notice the three rules: the list of values ends with a **semicolon** `;`, the fields must be `final`, and the constructor must be `const`.

---

An enhanced enum can also declare **methods** and **getters**. Inside them, `this` is the current value, so you can use its `name`, `index` and fields directly:

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

An enum with no fields can still declare methods: the value list then ends with `;` and the members follow.

---

To go from a `String` back to an enum value, call `byName` on the `values` list. It returns the value whose `name` matches exactly:

```dart
enum Direction { north, south, east, west }

var direction = Direction.values.byName('east');
print(direction == Direction.east); // true
```

If no value has that name, `byName` throws an `ArgumentError`. When the string comes from user input, `asNameMap()` is a safer choice: it returns a `Map<String, Direction>` from names to values, so a lookup for an unknown name gives `null` instead of an error:

```dart
print(Direction.values.asNameMap()['up']); // null
```

---

Enum values make excellent **map keys**: they are unique, easy to compare and the compiler checks that you only use real values. Declare the map with the enum as the key type and look values up with `[]`:

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

As with any map, a lookup returns `null` when the key is missing, so use `??` to provide a fallback.

---

An enum can **implement an interface** with the `implements` keyword. The enum then promises to provide every member the interface declares, and its values can be used wherever that interface type is expected:

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

A getter declared in the interface can be implemented either with a getter or with a `final` field of the same name.
