Una **enumeración** (o *enum*) define un tipo común para un grupo de valores relacionados, para que puedas trabajar con esos valores de forma segura en cuanto a tipos. En Dart se declara con la palabra clave `enum`, listando sus **valores** separados por comas:

```dart
enum Direction { north, south, east, west }
```

Por convención, los nombres de los valores se escriben en `lowerCamelCase`, como las variables. Se accede a cada valor a través del nombre del enum, y al imprimirlo se muestra tanto el enum como el valor:

```dart
var heading = Direction.north;
print(heading); // Direction.north
```

Un enum debe declararse en el nivel superior de un archivo, nunca dentro de una función como `main`.

---

Cada valor de un enum tiene dos propiedades integradas:

- `name` es el nombre del valor como `String`
- `index` es su posición en la declaración, empezando desde `0`

```dart
enum Direction { north, south, east, west }

print(Direction.east.name);  // east
print(Direction.east.index); // 2
```

---

Cada enum también tiene una lista constante llamada `values` que contiene todos sus valores en el orden de declaración. Puedes indexarla como cualquier lista, leer su `length` o recorrerla con `for-in`:

```dart
enum Direction { north, south, east, west }

print(Direction.values.length); // 4
print(Direction.values[1]);     // Direction.south

for (var direction in Direction.values) {
  print(direction.name);
}
```

---

Como `values` es una lista, puedes combinarla con los métodos de lista que ya conoces. Por ejemplo, `.map()` junto con `.name` convierte los valores en una lista de strings:

```dart
enum Direction { north, south, east, west }

List<String> names = Direction.values.map((d) => d.name).toList();
print(names); // [north, south, east, west]
```

---

Recorrer `values` es la forma habitual de procesar todos los valores de un enum. Dentro del bucle, el valor actual se comporta como cualquier otro objeto, así que puedes leer su `index` y su `name` y usarlos directamente en una interpolación de cadena:

```dart
enum Direction { north, south, east, west }

for (var direction in Direction.values) {
  print('${direction.index}: ${direction.name}');
}
```

---

Cada valor de un enum existe exactamente una vez, por lo que dos referencias al mismo valor son siempre iguales. Compáralas con `==` y `!=`:

```dart
enum Direction { north, south, east, west }

var heading = Direction.north;
print(heading == Direction.north); // true
print(heading != Direction.south); // true
print(Direction.values[0] == heading); // true
```

---

Una sentencia `switch` es la forma natural de ramificar sobre un enum, con un `case` por valor:

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

Cuando los casos cubren todos los valores, el switch es *exhaustivo* y no necesita `default`. Si olvidas un valor, el compilador reporta un error en lugar de dejar que el fallo llegue a tiempo de ejecución.

---

Desde Dart 3, un `switch` también puede usarse como una **expresión** que produce un valor. Cada caso se escribe como `pattern => value` y los casos se separan por comas, sin la palabra clave `case` y sin `break`:

```dart
enum Direction { north, south, east, west }

String arrow(Direction direction) => switch (direction) {
      Direction.north => '^',
      Direction.south => 'v',
      Direction.east => '>',
      Direction.west => '<',
    };
```

Al igual que la forma de sentencia, una expresión switch sobre un enum debe ser exhaustiva.

---

Desde Dart 2.17, un enum puede declarar **campos** y un **constructor**, igual que una clase. Esto se llama un *enum mejorado*. Cada valor pasa entonces sus propios argumentos al constructor:

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

Fíjate en las tres reglas: la lista de valores termina con un **punto y coma** `;`, los campos deben ser `final`, y el constructor debe ser `const`.

---

Un enum mejorado también puede declarar **métodos** y **getters**. Dentro de ellos, `this` es el valor actual, así que puedes usar directamente su `name`, `index` y sus campos:

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

Un enum sin campos puede seguir declarando métodos: la lista de valores termina entonces con `;` y los miembros van a continuación.

---

Para pasar de un `String` de vuelta a un valor de enum, llama a `byName` sobre la lista `values`. Devuelve el valor cuyo `name` coincide exactamente:

```dart
enum Direction { north, south, east, west }

var direction = Direction.values.byName('east');
print(direction == Direction.east); // true
```

Si ningún valor tiene ese nombre, `byName` lanza un `ArgumentError`. Cuando el string proviene de la entrada del usuario, `asNameMap()` es una opción más segura: devuelve un `Map<String, Direction>` de nombres a valores, de modo que una búsqueda de un nombre desconocido da `null` en lugar de un error:

```dart
print(Direction.values.asNameMap()['up']); // null
```

---

Los valores de un enum son excelentes **claves de mapa**: son únicos, fáciles de comparar, y el compilador comprueba que solo uses valores reales. Declara el mapa con el enum como tipo de clave y busca los valores con `[]`:

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

Como con cualquier mapa, una búsqueda devuelve `null` cuando falta la clave, así que usa `??` para proporcionar un valor alternativo.

---

Un enum puede **implementar una interfaz** con la palabra clave `implements`. El enum promete entonces proporcionar cada miembro que declara la interfaz, y sus valores pueden usarse en cualquier lugar donde se espere ese tipo de interfaz:

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

Un getter declarado en la interfaz puede implementarse tanto con un getter como con un campo `final` del mismo nombre.
