In Dart, a **list** is an ordered collection of items. The simplest way to create a list is with the `[]` literal syntax:

```dart
List<int> numbers = [1, 2, 3];
```

You can also use type inference with `var`:

```dart
var fruits = ['apple', 'banana', 'cherry'];
```

The type annotation `List<String>` tells Dart that every element in the list must be a `String`.

---

Lists in Dart are **zero-indexed**, meaning the first element is at index `0`, the second at index `1`, and so on.

```dart
var colors = ['red', 'green', 'blue'];
print(colors[0]); // red
print(colors[2]); // blue
```

Accessing an element by index is done with the `list[index]` syntax.

---

The `.add()` method appends a single element to the **end** of a list:

```dart
var nums = [1, 2, 3];
nums.add(4);
print(nums); // [1, 2, 3, 4]
```

Note that `.add()` modifies the list **in place** and returns `void`.

---

The `.length` property returns the number of elements in a list:

```dart
var scores = [95, 87, 72, 100];
print(scores.length); // 4
```

An empty list has a length of `0`:

```dart
var empty = [];
print(empty.length); // 0
```

---

The `.contains()` method checks whether a list includes a given value. It returns `true` if found, `false` otherwise:

```dart
var fruits = ['apple', 'mango', 'grape'];
print(fruits.contains('mango'));  // true
print(fruits.contains('orange')); // false
```

This is useful for membership checks without needing a loop.

---

The `.remove(value)` method removes the **first** element equal to `value` from a list. It returns `true` if an element was removed, or `false` if the value was not found.

```dart
var colors = ['red', 'green', 'blue'];
bool removed = colors.remove('green');
print(removed); // true
print(colors); // [red, blue]
```

---

The `.first` and `.last` properties give you the first and last element of a list without using an index.

```dart
var colors = ['red', 'green', 'blue'];
print(colors.first); // red
print(colors.last); // blue
```

Both throw an error if the list is empty.

---

The `.isEmpty` property is `true` when a list has no elements, and `.isNotEmpty` is `true` when it has at least one.

```dart
var colors = <String>[];
print(colors.isEmpty); // true
colors.add('red');
print(colors.isNotEmpty); // true
```

---

The `.indexOf(value)` method returns the index of the first element equal to `value`. If the value is not in the list, it returns `-1`.

```dart
var colors = ['red', 'green', 'blue'];
print(colors.indexOf('green')); // 1
print(colors.indexOf('pink')); // -1
```

---

The `.where()` method keeps only the elements for which a function returns `true`. It does not return a new list but a lazy `Iterable`, so call `.toList()` to turn the result back into a `List`.

```dart
var numbers = [1, 2, 3, 4];
List<int> big = numbers.where((n) => n > 2).toList();
print(big); // [3, 4]
```
