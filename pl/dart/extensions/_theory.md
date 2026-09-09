Wiesz już, jak dodawać metody do klasy, którą sam napisałeś. Ale co z `String`, `int` czy `List`, których kod znajduje się w Dart SDK? Nie możesz ich edytować, a jednak często chciałbyś, aby miały jeszcze jedną metodę.

**Rozszerzenie** rozwiązuje ten problem: dodaje nowe składowe do **istniejącego** typu, bez dotykania jego kodu źródłowego i bez tworzenia podklasy. Składnia to:

```dart
extension ExtensionName on Type {
  // new methods and getters
}
```

Wewnątrz rozszerzenia `this` odnosi się do wartości, na której wywoływana jest składowa. Po zadeklarowaniu rozszerzenia jego składowe wywołuje się dokładnie tak samo jak własne składowe typu:

```dart
extension Greeting on String {
  String greet() => 'Hello, $this!';
}

void main() {
  var name = 'Ada';
  print(name.greet()); // Hello, Ada!
}
```

Rozszerzenia deklaruje się na **poziomie najwyższym** pliku, obok klas i funkcji, nigdy wewnątrz `main`.

---

Rozszerzenia działają na dowolnym typie, w tym na liczbach. To rozszerzenie daje każdemu `int` metodę, która podwaja jego wartość:

```dart
extension Doubling on int {
  int doubled() => this * 2;
}
```

Ponieważ rozszerzenie dotyczy **typu**, możesz wywołać metodę na zmiennej lub bezpośrednio na **literale**. Ujemne literały wymagają nawiasów, w przeciwnym razie kropka zostanie odczytana przed znakiem minus:

```dart
var n = 21;
print(n.doubled());    // 42
print(4.doubled());    // 8
print((-3).doubled()); // -6
```

---

Rozszerzenie może też deklarować **gettery**, które odczytuje się jak właściwości, bez nawiasów. Wewnątrz rozszerzenia możesz wywoływać bezpośrednio własne składowe typu: `this.` jest opcjonalne, dokładnie tak jak wewnątrz klasy.

```dart
extension Sizes on String {
  bool get isLong => length > 10;      // same as this.length
  String get firstChar => this[0];
}

void main() {
  print('Dart'.isLong);           // false
  print('extension'.firstChar);   // e
}
```

Wybierz getter, gdy składowa tylko **odczytuje** wartość i nie przyjmuje parametrów; wybierz metodę, gdy wykonuje pracę lub potrzebuje argumentów.

---

Typ po `on` może być typem **parametryzowanym**, takim jak `List<int>`. Rozszerzenie dotyczy wtedy tylko list o tym typie elementów: `[1, 2].total()` działa, `['a', 'b'].total()` się nie kompiluje.

```dart
extension Totals on List<int> {
  int total() {
    var sum = 0;
    for (final n in this) {
      sum += n;
    }
    return sum;
  }
}
```

Wewnątrz rozszerzenia `this` to lista, więc możesz po niej iterować, indeksować ją lub wywołać `length` jak zwykle.

---

Rozszerzenia na `List<int>` nie można użyć na `List<String>`. Aby napisać jedno rozszerzenie działające dla **każdego** typu elementów, nadaj rozszerzeniu **parametr typu**, zapisany w nawiasach kątowych po jego nazwie, i użyj go w typie po `on`:

```dart
extension Firsts<T> on List<T> {
  T get firstOrLast => length > 1 ? this[0] : this[length - 1];
}
```

`T` to symbol zastępczy dla „cokolwiek to jest za typ elementów”: na `List<int>` staje się `int`, na `List<String>` staje się `String`, więc getter powyżej zwraca odpowiednio `int` albo `String`. Kompilator wstawia `T` za ciebie przy każdym wywołaniu.

```dart
print([7, 8, 9].firstOrLast); // 7
print(['a', 'b'].firstOrLast); // a
```

---

Rozszerzenia na `String` nie można wywołać na `String?`: wartość może być `null`, a kompilator odrzuca takie wywołanie. Jeśli zadeklarujesz rozszerzenie na typie **nullable**, metodę można wywołać bezpośrednio na `String?`, a wewnątrz niej `this` ma typ `String?`, więc musisz sam obsłużyć przypadek `null`, na przykład za pomocą `??`:

```dart
extension Defaults on int? {
  int orZero() => this ?? 0;
}

void main() {
  int? count = null;
  print(count.orZero()); // 0
  print(5.orZero());     // 5
}
```

Wartość `int` non-nullable można przekazać tam, gdzie oczekiwane jest `int?`, więc rozszerzenie działa na obu.

---

Rozszerzenie może dodawać metody, gettery, setter i operatory, ale **nie może dodawać pól instancji**. Wartość `int` ma stały układ w pamięci, a rozszerzenie to tylko zestaw funkcji, które kompilator pozwala wywoływać składnią z kropką: nie ma miejsca na przechowywanie dodatkowych danych dla każdej wartości.

```dart
extension Counter on int {
  int count = 0; // error: extensions can't declare instance fields
}
```

Gettery i setter w rozszerzeniu mogą tylko obliczać wartości na podstawie `this` lub przekazywać wywołania do istniejących składowych: nie mogą niczego zapamiętywać między wywołaniami.

---

Rozszerzenie może deklarować składowe **statyczne**. Jak w klasie, należą one do samego rozszerzenia, a nie do żadnej wartości, i dostęp do nich uzyskuje się przez **nazwę rozszerzenia**, a nie przez rozszerzany typ:

```dart
extension Temperatures on double {
  static const double boiling = 100.0;

  static bool isBoiling(double celsius) => celsius >= boiling;
}

void main() {
  print(Temperatures.boiling);         // 100.0
  print(Temperatures.isBoiling(37.5)); // false
  print(double.boiling);               // error: 'boiling' isn't defined for 'double'
}
```

Składowe statyczne to wygodne miejsce na stałe i funkcje pomocnicze związane z rozszerzanym typem.

---

Rozszerzenia nie służą tylko do typów z SDK: możesz rozszerzać też **własne klasy**. Jest to przydatne, gdy klasa pochodzi z pakietu, którym nie zarządzasz, albo gdy chcesz utrzymać klasę małą i dodać opcjonalne funkcje pomocnicze obok kodu, który ich potrzebuje.

```dart
class Circle {
  final double radius;
  Circle(this.radius);
}

extension CircleMath on Circle {
  double get diameter => radius * 2;
}

void main() {
  print(Circle(3).diameter); // 6.0
}
```

Rozszerzenie widzi publiczne pola i metody klasy, dokładnie tak jak kod napisany poza klasą.

---

Dart pozwala typowi zdefiniować, co operatory takie jak `+`, `*` czy `==` oznaczają dla jego wartości, za pomocą metody, której nazwą jest słowo kluczowe `operator`, a po nim symbol. Prawa strona operatora to parametr metody:

```dart
extension Scaling on List<int> {
  List<int> operator *(int factor) => map((n) => n * factor).toList();
}

void main() {
  print([1, 2, 3] * 10); // [10, 20, 30]
}
```

Ponieważ rozszerzenia mogą deklarować operatory, możesz nadać istniejącemu typowi nowy operator, którego jeszcze nie ma. `String` ma `+` i `*`, ale nie ma `-`, więc rozszerzenie może zdefiniować, co oznacza `'hello world' - 'o'`.

---

Co jeśli rozszerzenie deklaruje składową, którą typ **już ma**? Zawsze wygrywa własna składowa typu: składowe rozszerzenia są brane pod uwagę tylko wtedy, gdy sam typ nie ma składowej o tej nazwie. Składowa rozszerzenia jest po cichu ignorowana, nie ma błędu ani nadpisania.

```dart
extension Shorter on String {
  int get length => 0;
}

void main() {
  print('four'.length); // 4, String's own length is used
}
```

Rozszerzenie może więc dodawać składowe i wypełniać luki, ale nigdy nie może **zmienić** zachowania istniejących składowych.

---

Nazwa rozszerzenia jest opcjonalna. Rozszerzenie **nienazwane** działa tak samo, ale jest widoczne tylko w pliku, który je deklaruje:

```dart
extension on int {
  bool get isTriple => this % 3 == 0;
}
```

**Nazwa** ma znaczenie, gdy tylko dwa rozszerzenia oferują tę samą składową na tym samym typie: wywołanie staje się **niejednoznaczne** i się nie kompiluje. Nazwa pozwala rozwiązać konflikt na dwa sposoby. Gdy rozszerzenia pochodzą z różnych plików, możesz użyć `show` lub `hide` dla jednego z nich w instrukcji importu:

```dart
import 'package:loud/loud.dart';
import 'package:quiet/quiet.dart' hide Quiet;
```

Albo, w dowolnym miejscu, możesz zastosować rozszerzenie **jawnie**, opakowując wartość w nazwę rozszerzenia, jak gdyby była konstruktorem:

```dart
print(Loud('hi').describe());
```

Rozszerzeń nienazwanych nie można ukryć ani zastosować jawnie, więc preferuj rozszerzenia nazwane w kodzie, który inni będą importować.

---

Rozszerzenie generyczne może przyjmować **funkcje** jako parametry, dokładnie tak jak robią to `where` i `map`. Typ funkcji zapisuje się z typem elementów `T`, więc callback otrzymuje elementy właściwego typu:

```dart
extension Checks<T> on List<T> {
  bool all(bool Function(T) test) {
    for (final item in this) {
      if (!test(item)) return false;
    }
    return true;
  }
}

void main() {
  print([2, 4, 6].all((n) => n.isEven)); // true
}
```
