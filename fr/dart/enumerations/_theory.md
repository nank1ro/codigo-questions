Une **énumération** (ou *enum*) définit un type commun pour un groupe de valeurs liées, afin de pouvoir travailler avec ces valeurs de manière sûre du point de vue des types. En Dart, on en déclare une avec le mot-clé `enum`, en listant ses **valeurs** séparées par des virgules :

```dart
enum Direction { north, south, east, west }
```

Par convention, les noms des valeurs sont écrits en `lowerCamelCase`, comme les variables. On accède à chaque valeur via le nom de l'enum, et l'afficher montre à la fois l'enum et la valeur :

```dart
var heading = Direction.north;
print(heading); // Direction.north
```

Un enum doit être déclaré au niveau supérieur d'un fichier, jamais à l'intérieur d'une fonction comme `main`.

---

Chaque valeur d'un enum possède deux propriétés intégrées :

- `name` est le nom de la valeur sous forme de `String`
- `index` est sa position dans la déclaration, en commençant à `0`

```dart
enum Direction { north, south, east, west }

print(Direction.east.name);  // east
print(Direction.east.index); // 2
```

---

Chaque enum possède aussi une liste constante appelée `values` qui contient toutes ses valeurs dans l'ordre de déclaration. Vous pouvez l'indexer comme n'importe quelle liste, lire sa `length` ou la parcourir avec `for-in` :

```dart
enum Direction { north, south, east, west }

print(Direction.values.length); // 4
print(Direction.values[1]);     // Direction.south

for (var direction in Direction.values) {
  print(direction.name);
}
```

---

Comme `values` est une liste, vous pouvez la combiner avec les méthodes de liste que vous connaissez déjà. Par exemple, `.map()` avec `.name` transforme les valeurs en une liste de chaînes :

```dart
enum Direction { north, south, east, west }

List<String> names = Direction.values.map((d) => d.name).toList();
print(names); // [north, south, east, west]
```

---

Parcourir `values` est la manière habituelle de traiter chaque valeur d'un enum. Dans la boucle, la valeur courante se comporte comme n'importe quel autre objet : tu peux donc lire son `index` et son `name` et les utiliser directement dans une interpolation de chaîne :

```dart
enum Direction { north, south, east, west }

for (var direction in Direction.values) {
  print('${direction.index}: ${direction.name}');
}
```

---

Chaque valeur d'un enum existe exactement une fois, donc deux références à la même valeur sont toujours égales. Comparez-les avec `==` et `!=` :

```dart
enum Direction { north, south, east, west }

var heading = Direction.north;
print(heading == Direction.north); // true
print(heading != Direction.south); // true
print(Direction.values[0] == heading); // true
```

---

Une instruction `switch` est la manière naturelle de brancher sur un enum, avec un `case` par valeur :

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

Lorsque les cas couvrent toutes les valeurs, le switch est *exhaustif* et n'a pas besoin de `default`. Si vous oubliez une valeur, le compilateur signale une erreur au lieu de laisser le bug atteindre l'exécution.

---

Depuis Dart 3, un `switch` peut aussi être utilisé comme une **expression** qui produit une valeur. Chaque cas s'écrit comme `pattern => value` et les cas sont séparés par des virgules, sans le mot-clé `case` et sans `break` :

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) => switch (direction) {
      Direction.north => '^',
      Direction.south => 'v',
      Direction.east => '>',
      Direction.west => '<',
    };
```

Comme la forme instruction, une expression switch sur un enum doit être exhaustive.
