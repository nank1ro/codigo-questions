A `List` does not just hold values, it holds values **of one type**. The type is written between angle brackets right after the name of the collection:

```dart
List<String> names = ['Ada', 'Grace'];
List<int> scores = [10, 20];
```

`String` and `int` here are **type arguments**, and a type that takes one is called **generic**. The list class is written once, and `List<String>` and `List<int>` are two different types produced from it.

The payoff is that the compiler knows what is inside:

```dart
names.add(42);          // error: 42 is not a String
print(names.first.toUpperCase()); // fine: first is a String
```

---

`List` is not the only generic collection. A `Set` takes one type argument, and a `Map` takes **two**: one for the keys and one for the values, in that order.

```dart
Set<String> tags = {'new', 'sale'};
Map<String, int> ages = {'Ada': 36, 'Grace': 45};
```

An empty collection literal cannot be read from its contents, so you write the type arguments on the literal itself:

```dart
final counts = <String, int>{};
final seen = <String>{};
counts['fig'] = 3;
```

Once the types are known, everything you take out of the collection already has the right type: `ages['Ada']` is an `int?`, never a mystery value.

---

Dart also has the type `dynamic`, which means "anything goes". A `List<dynamic>` accepts every value, so it looks more convenient than a `List<String>`:

```dart
List<dynamic> things = ['Ada', 'Grace'];
things.add(42);                    // accepted
print(things.first.toUpperCase()); // accepted
```

The catch is that nothing is checked while you write the code. Every call on a `dynamic` value is resolved while the program runs, so a typo like `things.first.toUpperCse()` compiles happily and blows up in front of a user.

Generics are the alternative: one piece of code that works with **any** type, while each use of it is still checked for **one** type. That is the whole point of this topic.

---

You are not limited to the generic classes Dart ships with: you can declare your own. A **type parameter** goes between angle brackets after the class name, and from there on it is a normal type inside the body:

```dart
class Box<T> {
  final T value;

  Box(this.value);

  T unwrap() => value;
}
```

`T` is only a placeholder. It is filled in when a `Box` is created, either explicitly or by inference:

```dart
final a = Box<int>(7);   // Box<int>
final b = Box('fig');    // Box<String>, inferred from the argument
print(a.value + 1);      // 8, the compiler knows value is an int
```

The letter does not matter: `T` is a convention for "type", nothing more.

---

A function can be generic on its own, without living in a generic class. The type parameter goes between the name and the parameter list:

```dart
T firstOf<T>(List<T> items) => items.first;

print(firstOf(['fig', 'kiwi'])); // fig, T is String here
print(firstOf([10, 20]));        // 10, T is int here
```

One function body, checked once, reused for every type. The type argument is usually inferred from the arguments, but it can be written explicitly when inference has nothing to work with:

```dart
final empty = firstOf<String>(<String>[]); // throws, but the type is clear
```

Methods inside a class follow exactly the same rule.

---

Inside a generic class the type parameter is visible everywhere: in fields, in constructor parameters, in method signatures and in method bodies. It is declared once, next to the class name, and every member can use it.

```dart
class Holder<T> {
  final T item;

  Holder(this.item);

  String describe() => 'holding $item';
}
```

Creating the object is what decides the type: `Holder<String>('fig')` makes `item` a `String`, `Holder<int>(3)` makes it an `int`.

---

A class can declare more than one type parameter, separated by commas. `Map<K, V>` is the built-in example: one type for the keys, one for the values.

```dart
class Entry<K, V> {
  final K key;
  final V value;

  Entry(this.key, this.value);
}

final e = Entry<String, int>('age', 30);
```

The **order** is part of the type: `Entry<String, int>` and `Entry<int, String>` are unrelated types, and a value of one cannot be assigned to the other. Type parameters can also be reordered in a return type, which is how a method can hand back a flipped version of the object:

```dart
Entry<V, K> get flipped => Entry(value, key);
```

---

With sound null safety the question mark can land in two different places, and they mean two different things:

```dart
Box<int?> a = Box(null); // a box that exists and holds a nullable int
Box<int>? b = null;      // no box at all, but if there is one it holds an int
```

In `Box<int?>` the **type argument** is nullable, so `a.value` has type `int?` and may be `null`, while `a` itself is always there. In `Box<int>?` the **variable** is nullable, so `b` may be `null` and you need `b?.value` or `b!.value` to reach inside it.

A plain `T` means `T extends Object?`, so a nullable type argument such as `Box<int?>` is perfectly legal.

---

The difference matters as soon as you use the value. On a `Box<int?>` you reach the field normally and then deal with the `null` inside it, while on a `Box<int>?` you have to get past the missing box first:

```dart
Box<int?> a = Box(null);
print(a.value ?? 0); // 0, the box is there, its content is null

Box<int>? b = null;
print(b?.value ?? 0); // 0, the box itself is missing
```

Writing `b.value` on a `Box<int>?` does not compile at all: Dart refuses to read a field of something that may not exist.

---

An unbounded `T` could be anything, so inside the body you may only use what every object has. This does not compile:

```dart
T twice<T>(T value) => value + value; // error: + is not defined for T
```

A **bound** fixes that. Writing `T extends num` says "`T` may only be a number", and in exchange the body may use everything a `num` offers:

```dart
T twice<T extends num>(T value) => (value + value) as T;

num half<T extends num>(T value) => value / 2;
```

The bound is checked at the call site: `half(4)` and `half(2.5)` are fine, `half('fig')` is a compile-time error. A bound is a promise in both directions, narrower arguments for more power inside.

---

The keyword for a bound is always `extends`, even when the bound is an interface rather than a superclass. There is no `implements` in a type parameter list.

```dart
num biggerOf<T extends num>(T a, T b) => a > b ? a : b;
```

Without the bound, `a > b` would not compile: the comparison operator belongs to `num`, not to every object.

---

A bound can mention the type parameter itself. `Comparable<T>` is the interface of everything that knows how to compare itself with its own kind, through `compareTo`:

```dart
print('fig'.compareTo('kiwi')); // negative: fig comes first
print('kiwi'.compareTo('fig')); // positive
print('fig'.compareTo('fig'));  // zero
```

So `T extends Comparable<T>` reads as "any type that can be compared with itself", which is exactly what a sorting or maximum function needs:

```dart
T maxOf<T extends Comparable<T>>(T a, T b) => a.compareTo(b) >= 0 ? a : b;

print(maxOf('fig', 'kiwi')); // kiwi
```

`String` and `DateTime` both satisfy it directly. `int` and `double` implement `Comparable<num>`, so a list of numbers simply gets compared as `num`.

---

The same bound works just as well for the smallest element: only the sign of the comparison changes. `compareTo` returns a negative number when the receiver comes first, so `item.compareTo(best) < 0` means "this one is smaller".

---

A generic class can have named and **factory** constructors like any other class, and the type parameter is available inside them. A factory constructor does not create the object itself: it runs a body and returns one, which lets it choose, reuse or build the instance in any way it likes.

```dart
class Box<T> {
  final T value;

  Box(this.value);

  factory Box.first(List<T> items) => Box(items.first);
}

final b = Box<int>.first([5, 6]);
print(b.value); // 5
```

The type argument goes on the class, not on the constructor name: `Box<int>.first(...)`. Inside the factory, `<T>[]` is a real empty `List<T>`, so a factory is the natural place to build a default value for a type you do not know yet.

---

A type parameter written without a bound is not unbounded at all: `class Box<T>` is short for `class Box<T extends Object?>`. That is why `Box<int?>` is accepted, and why inside the class you may never assume `value` is non-null.

To forbid nullable type arguments, bound the parameter with `Object`:

```dart
class Strict<T extends Object> {
  final T value;
  Strict(this.value);
}

final ok = Strict<int>(7);
final bad = Strict<int?>(null);
// error: Type argument 'int?' doesn't conform to the bound 'Object'
```

`Object` is the type of everything except `null`, so `T extends Object` reads as "anything, as long as it is really there".

---

A `typedef` gives a name to a type, and it can take type parameters of its own. The usual reason is to name a family of function types once instead of spelling it out at every use:

```dart
typedef Transform<I, O> = O Function(I input);

final Transform<String, int> length = (word) => word.length;
print(length('kiwi')); // 4
```

`Transform<String, int>` is just another way of writing `int Function(String)`, so the two are interchangeable. The gain is readability: a parameter declared as `Transform<I, O> transform` says what the function is for, while `O Function(I)` only says what it looks like.

A generic typedef and a generic function combine naturally, with the function's own type parameters filling the typedef's.
