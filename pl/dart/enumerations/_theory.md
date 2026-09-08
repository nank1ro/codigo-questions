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
