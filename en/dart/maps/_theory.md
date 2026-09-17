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

---

An empty map literal `{}` has no pairs to infer the types from, so give it explicit types with `<K, V>{}` or with a type annotation:

```dart
var cart = <String, int>{};
Map<String, int> other = {};
```

The `.isEmpty` property is `true` when a map has no pairs, and `.isNotEmpty` is `true` when it has at least one:

```dart
print(cart.isEmpty); // true
cart['pen'] = 2;
print(cart.isNotEmpty); // true
```

---

The `.forEach()` method runs a function once for every pair. The function receives two parameters: the key and the value:

```dart
var ages = {'Ann': 30, 'Bob': 25};
ages.forEach((name, age) {
  print('$name is $age');
});
// Ann is 30
// Bob is 25
```

---

A map is not an `Iterable`, so you cannot loop over it directly with `for-in`. Instead, loop over `.entries`: each element is a `MapEntry` with a `.key` and a `.value`:

```dart
var ages = {'Ann': 30, 'Bob': 25};
for (var entry in ages.entries) {
  print('${entry.key}: ${entry.value}');
}
// Ann: 30
// Bob: 25
```

---

The `.putIfAbsent(key, ifAbsent)` method adds a pair **only if** the key is not in the map yet. The second argument is a function that produces the value. If the key already exists, the map is left untouched. In both cases the value now stored under the key is returned:

```dart
var ages = {'Ann': 30};
ages.putIfAbsent('Ann', () => 99); // Ann is already there, nothing changes
ages.putIfAbsent('Bob', () => 25); // Bob is added
print(ages); // {Ann: 30, Bob: 25}
```

---

The `.update(key, update)` method replaces the value of an existing key. The second argument is a function that receives the current value and returns the new one. If the key is missing, `.update()` throws an error, unless you pass an `ifAbsent` function that produces the initial value:

```dart
var stock = {'apple': 3};
stock.update('apple', (n) => n + 1); // apple becomes 4
stock.update('kiwi', (n) => n + 1, ifAbsent: () => 1); // kiwi is added with 1
print(stock); // {apple: 4, kiwi: 1}
```
