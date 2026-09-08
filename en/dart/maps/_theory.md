A **Map** is a collection of **key-value pairs**: every value is stored under a unique key, and you use the key to find the value again. A map is created with the `{}` literal syntax, writing each pair as `key: value`:

```dart
Map<String, int> ages = {'Ann': 30, 'Bob': 25};
print(ages); // {Ann: 30, Bob: 25}
```

The type annotation `Map<String, int>` tells Dart that every key is a `String` and every value is an `int`. As with lists, `var` infers the type from the literal:

```dart
var capitals = {'Italy': 'Rome', 'France': 'Paris'};
```

---

To read a value you use the key inside square brackets, just like an index in a list:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages['Ann']); // 30
```

If the key is not in the map, the lookup does **not** throw an error: it returns `null`. For this reason the type of `ages['Ann']` is `int?` (a nullable `int`), not `int`:

```dart
print(ages['Zed']); // null
```

---

Assigning with `map[key] = value` either **adds** a new pair, when the key is not in the map yet, or **updates** the value stored under an existing key:

```dart
var ages = {'Ann': 30};
ages['Bob'] = 25; // adds Bob
ages['Ann'] = 31; // updates Ann
print(ages); // {Ann: 31, Bob: 25}
```

New keys are appended after the existing ones, so a map remembers the insertion order.

---

The `.remove(key)` method deletes a key and its value from the map. It returns the removed value, or `null` if the key was not there:

```dart
var ages = {'Ann': 30, 'Bob': 25};
int? removed = ages.remove('Ann');
print(removed); // 30
print(ages); // {Bob: 25}
```

The `.length` property returns the number of key-value pairs:

```dart
print(ages.length); // 1
```

---

To check whether a map has a given key, use `.containsKey(key)`. To check whether any pair stores a given value, use `.containsValue(value)`. Both return a `bool`:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages.containsKey('Ann')); // true
print(ages.containsKey('Zed')); // false
print(ages.containsValue(25)); // true
```

---

Reading a missing key never throws, so always consider that a lookup can give you `null`. A safe pattern is to provide a fallback with the `??` operator:

```dart
var ages = {'Ann': 30};
int age = ages['Zed'] ?? 0;
print(age); // 0
```

---

The `.keys` property gives all the keys of a map and `.values` gives all the values, in insertion order. They are lazy `Iterable`s, so call `.toList()` when you need a real `List`:

```dart
var ages = {'Ann': 30, 'Bob': 25};
List<String> names = ages.keys.toList();
List<int> years = ages.values.toList();
print(names); // [Ann, Bob]
print(years); // [30, 25]
```
