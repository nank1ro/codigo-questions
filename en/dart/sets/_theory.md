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

---

Sets support the classic set operations. Each one returns a **new** set and leaves the originals untouched:

- `a.union(b)` contains the elements that are in `a` **or** in `b`
- `a.intersection(b)` contains the elements that are in **both** `a` and `b`
- `a.difference(b)` contains the elements of `a` that are **not** in `b`

```dart
var a = {1, 2, 3};
var b = {2, 3, 4};
print(a.union(b));        // {1, 2, 3, 4}
print(a.intersection(b)); // {2, 3}
print(a.difference(b));   // {1}
```

---

Converting a list to a set is the easiest way to **remove duplicates**: every list has a `.toSet()` method that returns a set with its unique elements, in order of first appearance. A set has a `.toList()` method that goes the other way, so chaining the two gives you a list without duplicates:

```dart
var votes = ['a', 'b', 'a', 'c', 'b'];
Set<String> unique = votes.toSet();
print(unique); // {a, b, c}
List<String> cleaned = votes.toSet().toList();
print(cleaned); // [a, b, c]
```

---

Both lists and sets have a `.contains()` method, but they work very differently. A list checks its elements one by one from the start, so a lookup in a long list gets slower as the list grows. A set stores its elements by their hash, so `.contains()` finds a value in roughly constant time no matter how many elements there are.

If you need to check membership many times and the order or duplicates do not matter, a set is the right tool:

```dart
var banned = {'spam', 'scam'};
print(banned.contains('spam')); // fast, even with millions of elements
```
