**Enumeracja** (lub *enum*) definiuje wspólny typ dla grupy powiązanych wartości, dzięki czemu możesz operować na tych wartościach w sposób bezpieczny pod względem typów. W Dart deklarujesz ją za pomocą słowa kluczowego `enum`, wypisując jej **wartości** oddzielone przecinkami:

```dart
enum Direction { north, south, east, west }
```

Zgodnie z konwencją nazwy wartości zapisuje się w stylu `lowerCamelCase`, tak jak zmienne. Do każdej wartości uzyskuje się dostęp przez nazwę enuma, a jej wypisanie pokazuje zarówno enum, jak i wartość:

```dart
var heading = Direction.north;
print(heading); // Direction.north
```

Enum musi być zadeklarowany na **najwyższym poziomie** pliku, nigdy wewnątrz funkcji takiej jak `main`.

---

Każda wartość enum ma dwie wbudowane właściwości:

- `name` to nazwa wartości jako `String`
- `index` to jej pozycja w deklaracji, licząc od `0`

```dart
enum Direction { north, south, east, west }

print(Direction.east.name);  // east
print(Direction.east.index); // 2
```

---

Każdy enum ma też stałą listę o nazwie `values`, która zawiera wszystkie jego wartości w kolejności deklaracji. Możesz ją indeksować jak każdą listę, odczytać jej `length` lub przejść przez nią pętlą `for-in`:

```dart
enum Direction { north, south, east, west }

print(Direction.values.length); // 4
print(Direction.values[1]);     // Direction.south

for (var direction in Direction.values) {
  print(direction.name);
}
```

---

Ponieważ `values` jest listą, możesz łączyć ją z metodami list, które już znasz. Na przykład `.map()` z `.name` zamienia wartości na listę ciągów znaków:

```dart
enum Direction { north, south, east, west }

List<String> names = Direction.values.map((d) => d.name).toList();
print(names); // [north, south, east, west]
```

---

Iterowanie po `values` to zwykły sposób na przetworzenie każdej wartości enuma. Wewnątrz pętli bieżąca wartość zachowuje się jak każdy inny obiekt, więc możesz odczytać jej `index` i `name` i użyć ich bezpośrednio w interpolacji łańcucha:

```dart
enum Direction { north, south, east, west }

for (var direction in Direction.values) {
  print('${direction.index}: ${direction.name}');
}
```

---

Każda wartość enum istnieje dokładnie raz, więc dwa odwołania do tej samej wartości są zawsze sobie równe. Porównuj je za pomocą `==` i `!=`:

```dart
enum Direction { north, south, east, west }

var heading = Direction.north;
print(heading == Direction.north); // true
print(heading != Direction.south); // true
print(Direction.values[0] == heading); // true
```

---

Instrukcja `switch` to naturalny sposób rozgałęziania po enumie, z jednym `case` na wartość:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) {
  switch (direction) {
    case Direction.north:
      return '^';
    case Direction.south:
      return 'v';
    case Direction.east:
      return '>';
    case Direction.west:
      return '<';
  }
}
```

Gdy case'y obejmują **wszystkie** wartości, switch jest *wyczerpujący* i nie potrzebuje `default`. Jeśli zapomnisz o jakiejś wartości, kompilator zgłosi błąd, zamiast pozwolić, by błąd dotarł do środowiska uruchomieniowego.

---

Od Dart 3 `switch` może być również używany jako **wyrażenie**, które zwraca wartość. Każdy case zapisuje się jako `wzorzec => wartość`, a case'y oddziela się przecinkami, bez słowa kluczowego `case` i bez `break`:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) => switch (direction) {
      Direction.north => '^',
      Direction.south => 'v',
      Direction.east => '>',
      Direction.west => '<',
    };
```

Podobnie jak w formie instrukcji, wyrażenie switch nad enumem musi być wyczerpujące.

---

Od Dart 2.17 enum może deklarować **pola** i **konstruktor**, tak jak klasa. Nazywa się to *rozszerzonym enumem*. Każda wartość przekazuje wtedy swoje własne argumenty do konstruktora:

```dart
enum Planet {
  mercury(0),
  earth(1),
  mars(2);

  final int moons;

  const Planet(this.moons);
}

print(Planet.mars.moons); // 2
```

Zwróć uwagę na trzy zasady: lista wartości kończy się **średnikiem** `;`, pola muszą być `final`, a konstruktor musi być `const`.

---

Rozszerzony enum może również deklarować **metody** i **gettery**. Wewnątrz nich `this` to bieżąca wartość, więc możesz bezpośrednio korzystać z jej `name`, `index` i pól:

```dart
enum Planet {
  mercury(0),
  earth(1),
  mars(2);

  final int moons;

  const Planet(this.moons);

  bool get hasMoons => moons > 0;

  String describe() => '$name has $moons moon(s)';
}

print(Planet.earth.hasMoons);   // true
print(Planet.mars.describe()); // mars has 2 moon(s)
```

Enum bez pól nadal może deklarować metody: lista wartości kończy się wtedy `;`, a po niej następują składowe.

---

Aby przejść z `String` z powrotem do wartości enum, wywołaj `byName` na liście `values`. Zwraca ona wartość, której `name` dokładnie pasuje:

```dart
enum Direction { north, south, east, west }

var direction = Direction.values.byName('east');
print(direction == Direction.east); // true
```

Jeśli żadna wartość nie ma takiej nazwy, `byName` rzuca `ArgumentError`. Gdy ciąg znaków pochodzi z danych wejściowych użytkownika, bezpieczniejszym wyborem jest `asNameMap()`: zwraca on `Map<String, Direction>` z nazw na wartości, więc wyszukanie nieznanej nazwy daje `null` zamiast błędu:

```dart
print(Direction.values.asNameMap()['up']); // null
```

---

Wartości enum świetnie sprawdzają się jako **klucze mapy**: są unikalne, łatwe do porównania, a kompilator sprawdza, że używasz tylko rzeczywistych wartości. Zadeklaruj mapę z enumem jako typem klucza i wyszukuj wartości za pomocą `[]`:

```dart
enum Direction { north, south, east, west }

Map<Direction, String> arrows = {
  Direction.north: '^',
  Direction.south: 'v',
  Direction.east: '>',
  Direction.west: '<',
};

print(arrows[Direction.east]); // >
```

Podobnie jak w każdej mapie, wyszukanie zwraca `null`, gdy brakuje klucza, więc użyj `??`, aby podać wartość zastępczą.

---

Enum może **implementować interfejs** za pomocą słowa kluczowego `implements`. Enum wtedy zobowiązuje się dostarczyć każdą składową zadeklarowaną przez interfejs, a jego wartości mogą być używane wszędzie tam, gdzie oczekiwany jest ten typ interfejsu:

```dart
abstract class Describable {
  String describe();
}

enum Animal implements Describable {
  dog,
  cat;

  @override
  String describe() => 'I am a $name';
}

Describable pet = Animal.cat;
print(pet.describe()); // I am a cat
```

Getter zadeklarowany w interfejsie może być zaimplementowany zarówno za pomocą gettera, jak i pola `final` o tej samej nazwie.
