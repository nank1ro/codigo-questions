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
ages['Bob'] = 25; // dodaje Bob
ages['Ann'] = 31; // aktualizuje Ann
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

---

Pusty literał mapy `{}` nie ma par, z których można wywnioskować typy, więc nadaj mu jawne typy za pomocą `<K, V>{}` lub adnotacji typu:

```dart
var cart = <String, int>{};
Map<String, int> other = {};
```

Właściwość `.isEmpty` jest `true`, gdy mapa nie ma par, a `.isNotEmpty` jest `true`, gdy ma co najmniej jedną:

```dart
print(cart.isEmpty); // true
cart['pen'] = 2;
print(cart.isNotEmpty); // true
```

---

Metoda `.forEach()` uruchamia funkcję raz dla każdej pary. Funkcja przyjmuje dwa parametry: klucz i wartość:

```dart
var ages = {'Ann': 30, 'Bob': 25};
ages.forEach((name, age) {
  print('$name is $age');
});
// Ann is 30
// Bob is 25
```

---

Mapa nie jest `Iterable`, więc nie można jej przechodzić bezpośrednio za pomocą `for-in`. Zamiast tego przechodź po `.entries`: każdy element to `MapEntry` z `.key` i `.value`:

```dart
var ages = {'Ann': 30, 'Bob': 25};
for (var entry in ages.entries) {
  print('${entry.key}: ${entry.value}');
}
// Ann: 30
// Bob: 25
```

---

Metoda `.putIfAbsent(key, ifAbsent)` dodaje parę **tylko wtedy, gdy** klucza jeszcze nie ma w mapie. Drugi argument to funkcja, która tworzy wartość. Jeśli klucz już istnieje, mapa pozostaje niezmieniona. W obu przypadkach zwracana jest wartość aktualnie przechowywana pod tym kluczem:

```dart
var ages = {'Ann': 30};
ages.putIfAbsent('Ann', () => 99); // Ann już tam jest, nic się nie zmienia
ages.putIfAbsent('Bob', () => 25); // Bob zostaje dodany
print(ages); // {Ann: 30, Bob: 25}
```

---

Metoda `.update(key, update)` zastępuje wartość istniejącego klucza. Drugi argument to funkcja, która otrzymuje bieżącą wartość i zwraca nową. Jeśli klucza brakuje, `.update()` rzuca błąd, chyba że przekażesz funkcję `ifAbsent`, która utworzy wartość początkową:

```dart
var stock = {'apple': 3};
stock.update('apple', (n) => n + 1); // apple staje się 4
stock.update('kiwi', (n) => n + 1, ifAbsent: () => 1); // kiwi zostaje dodane z wartością 1
print(stock); // {apple: 4, kiwi: 1}
```
