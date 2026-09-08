A **Set** is a collection of **unique** values: the same value can appear at most once. Like a map, a set is created with the `{}` literal syntax, but it contains plain values instead of `key: value` pairs:

```dart
Set<int> numbers = {1, 2, 3};
print(numbers); // {1, 2, 3}
```

The type annotation `Set<int>` tells Dart that every element is an `int`. As with lists and maps, `var` infers the type from the literal:

```dart
var colors = {'red', 'green'}; // Set<String>
```

---

A set never stores the same value twice. If a literal contains duplicates, only the first occurrence is kept and the others are discarded at runtime without any error (the analyzer will warn you about a literal that repeats a value):

```dart
var letters = {'a', 'b', 'a', 'b', 'c'};
print(letters); // {a, b, c}
```

The `.length` property returns how many **unique** elements the set holds:

```dart
print(letters.length); // 3
```

---

The `.add(value)` method inserts a single value. It returns `true` if the value was added and `false` if it was already in the set, in which case nothing changes. The `.addAll(iterable)` method inserts every element of a list or another set, again skipping the ones already present:

```dart
var tags = {'dart'};
tags.add('web');    // true
tags.add('dart');   // false, already there
tags.addAll(['web', 'mobile']);
print(tags); // {dart, web, mobile}
```

An empty `{}` literal is a **map**, not a set. To create an empty set give it a type:

```dart
var empty = <String>{};
Set<int> other = {};
```

---

The `.remove(value)` method deletes a value from the set. It returns `true` if the value was there and `false` otherwise:

```dart
var numbers = {1, 2, 3};
print(numbers.remove(2)); // true
print(numbers.remove(9)); // false
print(numbers); // {1, 3}
```

To delete every element at once, use `.clear()`.

---

To check whether a value is in a set use `.contains(value)`, which returns a `bool`. The `.isEmpty` property is `true` when the set has no elements, and `.isNotEmpty` when it has at least one:

```dart
var seen = {'x', 'y'};
print(seen.contains('x')); // true
print(seen.contains('z')); // false
print(seen.isEmpty);       // false
print(seen.isNotEmpty);    // true
```

---

The default set in Dart remembers the **insertion order**: when you print it or loop over it, the elements come out in the order they were first added. Adding a value that is already present does not move it:

```dart
var numbers = {3, 1, 3, 2};
print(numbers); // {3, 1, 2}
```

---

A set is an `Iterable`, so you can loop over its elements directly with `for-in`, just like a list. There are no indexes: the elements are visited in insertion order:

```dart
var numbers = {3, 1, 4};
for (var n in numbers) {
  print(n);
}
// 3
// 1
// 4
```
