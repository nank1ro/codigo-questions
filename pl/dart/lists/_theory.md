W Dart **lista** to uporządkowana kolekcja elementów. Najprostszym sposobem tworzenia listy jest użycie składni literału `[]`:

```dart
List<int> numbers = [1, 2, 3];
```

Możesz również użyć wnioskowania o typie za pomocą `var`:

```dart
var fruits = ['apple', 'banana', 'cherry'];
```

Adnotacja typu `List<String>` informuje Dart, że każdy element listy musi być typu `String`.

---

Listy w Dart są **indeksowane od zera**, co oznacza, że pierwszy element jest pod indeksem `0`, drugi pod indeksem `1` i tak dalej.

```dart
var colors = ['red', 'green', 'blue'];
print(colors[0]); // red
print(colors[2]); // blue
```

Dostęp do elementu po indeksie odbywa się za pomocą składni `list[index]`.

---

Metoda `.add()` dołącza pojedynczy element na **końcu** listy:

```dart
var nums = [1, 2, 3];
nums.add(4);
print(nums); // [1, 2, 3, 4]
```

Należy pamiętać, że `.add()` modyfikuje listę **w miejscu** i zwraca `void`.

---

Właściwość `.length` zwraca liczbę elementów na liście:

```dart
var scores = [95, 87, 72, 100];
print(scores.length); // 4
```

Pusta lista ma długość `0`:

```dart
var empty = [];
print(empty.length); // 0
```

---

Metoda `.contains()` sprawdza, czy lista zawiera daną wartość. Zwraca `true`, jeśli zostanie znaleziona, lub `false` w przeciwnym razie:

```dart
var fruits = ['apple', 'mango', 'grape'];
print(fruits.contains('mango'));  // true
print(fruits.contains('orange')); // false
```

Jest to przydatne do sprawdzania przynależności bez potrzeby używania pętli.
