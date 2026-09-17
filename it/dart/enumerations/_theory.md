Un'**enumerazione** (o *enum*) definisce un tipo comune per un gruppo di valori correlati, così puoi lavorare con quei valori in modo type-safe. In Dart la dichiari con la parola chiave `enum`, elencando i suoi **valori** separati da virgole:

```dart
enum Direction { north, south, east, west }
```

Per convenzione i nomi dei valori sono scritti in `lowerCamelCase`, come le variabili. Si accede a ogni valore tramite il nome dell'enum, e stamparlo mostra sia l'enum sia il valore:

```dart
var heading = Direction.north;
print(heading); // Direction.north
```

Un enum deve essere dichiarato al livello superiore di un file, mai all'interno di una funzione come `main`.

---

Ogni valore di un enum ha due proprietà integrate:

- `name` è il nome del valore come `String`
- `index` è la sua posizione nella dichiarazione, a partire da `0`

```dart
enum Direction { north, south, east, west }

print(Direction.east.name);  // east
print(Direction.east.index); // 2
```

---

Ogni enum ha anche una lista costante chiamata `values` che contiene tutti i suoi valori nell'ordine di dichiarazione. Puoi indicizzarla come qualsiasi lista, leggere la sua `length` o scorrerla con `for-in`:

```dart
enum Direction { north, south, east, west }

print(Direction.values.length); // 4
print(Direction.values[1]);     // Direction.south

for (var direction in Direction.values) {
  print(direction.name);
}
```

---

Poiché `values` è una lista, puoi combinarla con i metodi delle liste che già conosci. Per esempio `.map()` con `.name` trasforma i valori in una lista di stringhe:

```dart
enum Direction { north, south, east, west }

List<String> names = Direction.values.map((d) => d.name).toList();
print(names); // [north, south, east, west]
```

---

Ciclare su `values` è il modo abituale per elaborare ogni valore di un enum. Dentro al ciclo il valore corrente si comporta come qualsiasi altro oggetto, quindi puoi leggere il suo `index` e il suo `name` e usarli direttamente in un'interpolazione di stringa:

```dart
enum Direction { north, south, east, west }

for (var direction in Direction.values) {
  print('${direction.index}: ${direction.name}');
}
```

---

Ogni valore di un enum esiste esattamente una volta, quindi due riferimenti allo stesso valore sono sempre uguali. Confrontali con `==` e `!=`:

```dart
enum Direction { north, south, east, west }

var heading = Direction.north;
print(heading == Direction.north); // true
print(heading != Direction.south); // true
print(Direction.values[0] == heading); // true
```

---

Un'istruzione `switch` è il modo naturale per diramarsi su un enum, con un `case` per ogni valore:

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

Quando i case coprono ogni valore, lo switch è *esaustivo* e non necessita di `default`. Se dimentichi un valore, il compilatore segnala un errore invece di lasciare che il bug arrivi a runtime.

---

A partire da Dart 3, uno `switch` può essere usato anche come **espressione** che produce un valore. Ogni case è scritto come `pattern => value` e i case sono separati da virgole, senza la parola chiave `case` e senza `break`:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) => switch (direction) {
      Direction.north => '^',
      Direction.south => 'v',
      Direction.east => '>',
      Direction.west => '<',
    };
```

Come nella forma istruzione, un'espressione switch su un enum deve essere esaustiva.

---

A partire da Dart 2.17, un enum può dichiarare **campi** e un **costruttore**, proprio come una classe. Questo si chiama *enum avanzato*. Ogni valore passa quindi i propri argomenti al costruttore:

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

Nota le tre regole: la lista dei valori termina con un **punto e virgola** `;`, i campi devono essere `final`, e il costruttore deve essere `const`.

---

Un enum avanzato può anche dichiarare **metodi** e **getter**. Al loro interno, `this` è il valore corrente, quindi puoi usare direttamente il suo `name`, `index` e i suoi campi:

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

Un enum senza campi può comunque dichiarare metodi: la lista dei valori termina allora con `;` seguita dai membri.

---

Per passare da una `String` a un valore dell'enum, chiama `byName` sulla lista `values`. Restituisce il valore il cui `name` corrisponde esattamente:

```dart
enum Direction { north, south, east, west }

var direction = Direction.values.byName('east');
print(direction == Direction.east); // true
```

Se nessun valore ha quel nome, `byName` lancia un `ArgumentError`. Quando la stringa proviene dall'input dell'utente, `asNameMap()` è una scelta più sicura: restituisce una `Map<String, Direction>` dai nomi ai valori, così una ricerca per un nome sconosciuto restituisce `null` invece di un errore:

```dart
print(Direction.values.asNameMap()['up']); // null
```

---

I valori di un enum sono ottime **chiavi di mappa**: sono unici, facili da confrontare, e il compilatore verifica che tu usi solo valori reali. Dichiara la mappa con l'enum come tipo di chiave e cerca i valori con `[]`:

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

Come con qualsiasi mappa, una ricerca restituisce `null` quando la chiave manca, quindi usa `??` per fornire un valore di riserva.

---

Un enum può **implementare un'interfaccia** con la parola chiave `implements`. L'enum promette quindi di fornire ogni membro dichiarato dall'interfaccia, e i suoi valori possono essere usati ovunque sia previsto quel tipo di interfaccia:

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

Un getter dichiarato nell'interfaccia può essere implementato sia con un getter sia con un campo `final` dello stesso nome.
