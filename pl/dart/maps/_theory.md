**Map** to kolekcja **par klucz-wartość**: każda wartość jest przechowywana pod unikalnym kluczem, a klucza używa się, aby ponownie odnaleźć wartość. Mapę tworzy się za pomocą składni literału `{}`, zapisując każdą parę jako `klucz: wartość`:

```dart
Map<String, int> ages = {'Ann': 30, 'Bob': 25};
print(ages); // {Ann: 30, Bob: 25}
```

Adnotacja typu `Map<String, int>` informuje Dart, że każdy klucz jest typu `String`, a każda wartość jest typu `int`. Podobnie jak w przypadku list, `var` wnioskuje typ z literału:

```dart
var capitals = {'Italy': 'Rome', 'France': 'Paris'};
```

---

Aby odczytać wartość, używasz klucza w nawiasach kwadratowych, tak jak indeksu na liście:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages['Ann']); // 30
```

Jeśli klucza nie ma w mapie, wyszukanie **nie** rzuca błędu: zwraca `null`. Dlatego typ `ages['Ann']` to `int?` (nullowalny `int`), a nie `int`:

```dart
print(ages['Zed']); // null
```

---

Przypisanie za pomocą `map[key] = value` **dodaje** nową parę, gdy klucza jeszcze nie ma w mapie, albo **aktualizuje** wartość przechowywaną pod istniejącym kluczem:

```dart
var ages = {'Ann': 30};
ages['Bob'] = 25; // adds Bob
ages['Ann'] = 31; // updates Ann
print(ages); // {Ann: 31, Bob: 25}
```

Nowe klucze są dodawane po istniejących, więc mapa pamięta kolejność wstawiania.

---

Metoda `.remove(key)` usuwa klucz i jego wartość z mapy. Zwraca usuniętą wartość albo `null`, jeśli klucza nie było:

```dart
var ages = {'Ann': 30, 'Bob': 25};
int? removed = ages.remove('Ann');
print(removed); // 30
print(ages); // {Bob: 25}
```

Właściwość `.length` zwraca liczbę par klucz-wartość:

```dart
print(ages.length); // 1
```

---

Aby sprawdzić, czy mapa zawiera dany klucz, użyj `.containsKey(key)`. Aby sprawdzić, czy jakaś para przechowuje daną wartość, użyj `.containsValue(value)`. Obie zwracają `bool`:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages.containsKey('Ann')); // true
print(ages.containsKey('Zed')); // false
print(ages.containsValue(25)); // true
```

---

Odczytanie brakującego klucza nigdy nie rzuca błędu, więc zawsze zakładaj, że wyszukanie może zwrócić `null`. Bezpiecznym wzorcem jest podanie wartości zastępczej za pomocą operatora `??`:

```dart
var ages = {'Ann': 30};
int age = ages['Zed'] ?? 0;
print(age); // 0
```

---

Właściwość `.keys` zwraca wszystkie klucze mapy, a `.values` zwraca wszystkie wartości, w kolejności wstawiania. Są to leniwe (`lazy`) `Iterable`, więc wywołaj `.toList()`, gdy potrzebujesz prawdziwej `List`:

```dart
var ages = {'Ann': 30, 'Bob': 25};
List<String> names = ages.keys.toList();
List<int> years = ages.values.toList();
print(names); // [Ann, Bob]
print(years); // [30, 25]
```
