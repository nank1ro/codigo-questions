A class can only `extend` one superclass, but very often the same behaviour is needed by classes that have nothing else in common. A **mixin** is a reusable slice of behaviour that any number of classes can pick up.

You declare one with the **`mixin`** keyword, and a class picks it up with the **`with`** keyword:

```dart
mixin Swimmer {
  String swim() => 'swimming';
}

class Fish with Swimmer {}

void main() {
  print(Fish().swim()); // swimming
}
```

`Fish` declares no members of its own, yet every `Fish` has `swim`, because the mixin's members become members of the class. A mixin can be used by as many classes as you like, related or not.

---

The body of a mixin looks like the body of a class: methods, getters and fields, written exactly the same way. The difference is what you can do with the declaration itself.

```dart
mixin Timestamped {
  String get stamp => '[log]';

  String format(String text) => '$stamp $text';
}

class Server with Timestamped {}
class Printer with Timestamped {}
```

The name of a mixin is also a **type**, so `Server() is Timestamped` is `true` and a variable can be declared as `Timestamped t = Server();`. Two unrelated classes now share one implementation without either of them inheriting from the other.

---

A mixin is not limited to methods: it can declare **fields** too, and every object of every class using the mixin gets its own copy of them.

```dart
mixin Counter {
  int count = 0;

  void increment() {
    count++;
  }
}

class Clicker with Counter {}

void main() {
  final a = Clicker();
  final b = Clicker();
  a.increment();
  a.increment();
  print(a.count); // 2
  print(b.count); // 0, b has its own count
}
```

This is what makes a mixin more than an interface: it brings both the data and the code that works on it.

---

A `mixin` declaration is **not** a class. It exists only to be mixed into other classes, so it has no constructor of its own and cannot be instantiated or extended:

```dart
mixin Scored {
  int score = 0;
}

final s = Scored();            // error: mixins cannot be instantiated
class Team extends Scored {}   // error: mixins cannot be extended
class Team with Scored {}      // this is the only way to use it
```

The name still works as a type, so `Team() is Scored` and `Scored s = Team();` are both fine. A mixin has no constructor, so a non-nullable field must be initialised where it is declared (or marked `late`), like `int score = 0;` above.

---

A mixin can declare a member **without a body**. Such a member is abstract: the mixin uses it, and the class that picks up the mixin has to supply it.

```dart
mixin Greeting {
  String get name;                       // no body: the class provides it

  String greet() => 'Hello, $name!';
}

class Person with Greeting {
  @override
  final String name;

  Person(this.name);
}

void main() {
  print(Person('Ada').greet()); // Hello, Ada!
}
```

The mixin brings the behaviour, the class brings the data. A field in the class, like `final String name;`, is enough to satisfy an abstract getter of the same name.

---

Putting the pieces together, a program that uses a mixin has three parts: the `mixin` declaration, one or more classes that pick it up `with`, and the code that calls the shared member.

```dart
mixin Barker {
  String bark() => 'Woof!';
}

class Dog with Barker {}

void main() {
  print(Dog().bark()); // Woof!
}
```

Top-level declarations can be written in any order in Dart, but reading a file top to bottom is easier when the mixin comes before the classes that use it.

---

A class can use **several mixins at once**, listed after `with` and separated by commas. Dart applies them **left to right**, stacking each one on top of the previous, so when two mixins declare the same member the **last** one in the list wins:

```dart
mixin A {
  String who() => 'A';
}

mixin B {
  String who() => 'B';
}

class First with A, B {}
class Second with B, A {}

void main() {
  print(First().who());  // B, the last mixin in the list
  print(Second().who()); // A, the last mixin in the list
}
```

This stacking is called **linearization**: `with A, B` builds the chain `Object` → `A` → `B` → the class itself.

---

Because the last mixin wins, the order of the `with` list is part of the meaning of the class, not a detail of style. Reordering it changes which implementation the object ends up with:

```dart
mixin Plain {
  String format(String text) => text;
}

mixin Starred {
  String format(String text) => '*$text*';
}

class Fancy with Plain, Starred {}  // format comes from Starred
class Simple with Starred, Plain {} // format comes from Plain
```

Members that only one mixin declares are never in competition: they are available whatever the order. Read `with X, Y` as "start from `X`, then let `Y` override it".

---

Mixins and `extends` work together. A class can have a superclass **and** a list of mixins, and the mixins are always applied **on top of** the superclass:

```dart
class Document {
  String header() => 'Document';
}

mixin Timestamped {
  String header() => 'Timestamped';
}

class Report extends Document with Timestamped {}
```

The chain here is `Object` → `Document` → `Timestamped` → `Report`. A member is looked up starting from the end of the chain, so `Report().header()` finds `Timestamped`'s version first. Declaring the same member in the superclass and in a mixin is perfectly legal: it is how a mixin replaces or wraps inherited behaviour.

---

The class body sits at the very end of the chain, so a member declared in the class **overrides** the same member coming from any of its mixins. Inside the override, **`super`** reaches the version the mixin provided:

```dart
mixin Polite {
  String greet() => 'Hello';
}

class Host with Polite {
  @override
  String greet() => '${super.greet()}, welcome!';
}

class Guest with Polite {}

void main() {
  print(Host().greet());  // Hello, welcome!
  print(Guest().greet()); // Hello
}
```

The mixin itself is untouched: `Guest` still gets the original `greet`. `super.greet()` is what lets `Host` build on the shared behaviour instead of copying it.

---

Some behaviour only makes sense on top of a particular class, and needs that class's members to do its job. The **`on`** clause states the requirement:

```dart
class Animal {
  String get name => 'animal';
}

mixin Noisy on Animal {
  String shout() => '${name.toUpperCase()}!';
}

class Dog extends Animal with Noisy {
  @override
  String get name => 'dog';
}

void main() {
  print(Dog().shout()); // DOG!
}
```

`on Animal` does two things: it lets the mixin use `Animal`'s members, like `name` above, and it restricts who may use the mixin. `class Rock with Noisy {}` is a compile-time error, because `Rock` is not an `Animal`.

---

A mixin with an `on` clause reads its superclass's members as if they were its own, which is what makes it a good place for behaviour that decorates an existing type:

```dart
class Shape {
  String get kind => 'shape';
}

mixin Printable on Shape {
  void show() {
    print('a $kind');
  }
}

class Square extends Shape with Printable {
  @override
  String get kind => 'square';
}
```

`Square` overrides `kind`, and `show` picks up the override automatically: the mixin always calls the member on the real object.

---

Once a mixin has an `on` clause, it may **override** a member of that type and call **`super`** to reach the version underneath it in the chain:

```dart
class Logger {
  String log(String message) => message;
}

mixin Timestamped on Logger {
  @override
  String log(String message) => '[12:00] ${super.log(message)}';
}

class AppLogger extends Logger with Timestamped {}

void main() {
  print(AppLogger().log('started')); // [12:00] started
}
```

`super.log` is not the mixin's own `log`, it is the one below it, so there is no infinite recursion. Stack several such mixins with `with A, B` and each one wraps the previous: the call enters the **last** mixin first and travels down to the superclass.

---

A `mixin` declaration cannot be instantiated or extended, and a plain `class` cannot be used after `with`. When you need one declaration that works **both** ways, write **`mixin class`**:

```dart
mixin class Serializable {
  String toText() => 'data';
}

final s = Serializable();            // works: it is a class
class Record extends Serializable {} // works: it is a class
class Row with Serializable {}       // works: it is a mixin
```

A `mixin class` pays for that flexibility with two restrictions: it must extend `Object`, so it cannot have its own `extends` clause, and it must not declare a constructor, because a mixin never runs one.

---

Mixins, inheritance and interfaces solve three different problems:

- **`extends`** gives a class one superclass, for an "is a kind of" relationship. There is only one slot, so it should go to the strongest relationship.
- **`with`** adds behaviour that many unrelated classes need. There is no limit, and the implementation is shared, not copied.
- **`implements`** promises a set of members but brings **no** implementation: every class has to write the body itself.

A tell-tale sign that you want a mixin is a method you would otherwise copy into classes that have no natural common parent, such as `Duck`, `Plane` and `Kite` all needing the same `fly`.

---

Stacked mixins are how small, independent rules are combined into one class. Each mixin overrides the same member, does its own part, and calls `super` to hand the work on. Because the call enters the **last** mixin first, the order of the `with` list decides which rule runs before which:

```dart
class Account {
  int balance = 0;

  void deposit(int amount) {
    balance += amount;
  }
}

mixin Doubled on Account {
  @override
  void deposit(int amount) {
    super.deposit(amount * 2);
  }
}
```

`class A extends Account with Doubled {}` doubles every deposit. Add a second mixin after `Doubled` and it gets the deposit first, before `Doubled` ever sees it.
