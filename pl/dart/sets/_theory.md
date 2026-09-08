**Zbiór** (`Set`) to kolekcja **unikalnych** wartości: ta sama wartość może wystąpić co najwyżej raz. Podobnie jak mapa, zbiór tworzy się za pomocą składni literału `{}`, ale zawiera on zwykłe wartości zamiast par `klucz: wartość`:

```dart
Set<int> numbers = {1, 2, 3};
print(numbers); // {1, 2, 3}
```

Adnotacja typu `Set<int>` informuje Dart, że każdy element jest typu `int`. Podobnie jak w przypadku list i map, `var` wnioskuje typ z literału:

```dart
var colors = {'red', 'green'}; // Set<String>
```

---

Zbiór nigdy nie przechowuje tej samej wartości dwa razy. Jeśli literał zawiera duplikaty, zachowywane jest tylko pierwsze wystąpienie, a pozostałe są odrzucane w czasie działania programu bez żadnego błędu (analizator ostrzeże o literale, który powtarza wartość):

```dart
var letters = {'a', 'b', 'a', 'b', 'c'};
print(letters); // {a, b, c}
```

Właściwość `.length` zwraca liczbę **unikalnych** elementów w zbiorze:

```dart
print(letters.length); // 3
```

---

Metoda `.add(value)` wstawia pojedynczą wartość. Zwraca `true`, jeśli wartość została dodana, i `false`, jeśli była już w zbiorze — w takim przypadku nic się nie zmienia. Metoda `.addAll(iterable)` wstawia wszystkie elementy z listy lub innego zbioru, również pomijając te, które już są obecne:

```dart
var tags = {'dart'};
tags.add('web');    // true
tags.add('dart');   // false, already there
tags.addAll(['web', 'mobile']);
print(tags); // {dart, web, mobile}
```

Pusty literał `{}` jest **mapą**, a nie zbiorem. Aby utworzyć pusty zbiór, nadaj mu typ:

```dart
var empty = <String>{};
Set<int> other = {};
```

---

Metoda `.remove(value)` usuwa wartość ze zbioru. Zwraca `true`, jeśli wartość tam była, i `false` w przeciwnym razie:

```dart
var numbers = {1, 2, 3};
print(numbers.remove(2)); // true
print(numbers.remove(9)); // false
print(numbers); // {1, 3}
```

Aby usunąć wszystkie elementy naraz, użyj `.clear()`.

---

Aby sprawdzić, czy wartość znajduje się w zbiorze, użyj `.contains(value)`, która zwraca `bool`. Właściwość `.isEmpty` ma wartość `true`, gdy zbiór nie ma elementów, a `.isNotEmpty` — gdy ma co najmniej jeden:

```dart
var seen = {'x', 'y'};
print(seen.contains('x')); // true
print(seen.contains('z')); // false
print(seen.isEmpty);       // false
print(seen.isNotEmpty);    // true
```

---

Domyślny zbiór w Dart zapamiętuje **kolejność wstawiania**: gdy go wypisujesz lub po nim iterujesz, elementy pojawiają się w kolejności, w jakiej zostały dodane po raz pierwszy. Dodanie wartości, która już jest obecna, nie zmienia jej pozycji:

```dart
var numbers = {3, 1, 3, 2};
print(numbers); // {3, 1, 2}
```

---

Zbiór jest typem `Iterable`, więc możesz iterować po jego elementach bezpośrednio za pomocą `for-in`, tak jak w przypadku listy. Nie ma indeksów: elementy są odwiedzane w kolejności wstawiania:

```dart
var numbers = {3, 1, 4};
for (var n in numbers) {
  print(n);
}
// 3
// 1
// 4
```
