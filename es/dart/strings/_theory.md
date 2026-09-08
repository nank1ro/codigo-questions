Un **String** es un fragmento de texto: una secuencia de caracteres entre comillas. En Dart puedes usar comillas simples `'...'` o comillas dobles `"..."`, funcionan exactamente igual:

```dart
String name = 'Dart';
String other = "Dart";
print(name == other); // true
```

Elegir un tipo de comillas te permite usar el otro tipo dentro del texto sin necesidad de escaparlo:

```dart
print("It's sunny");   // It's sunny
print('Say "hi"');     // Say "hi"
```

Si necesitas la misma comilla dentro, escápala con una barra invertida: `'It\'s sunny'`.

---

Dos cadenas se pueden unir en una nueva con el operador `+`, llamado **concatenación**:

```dart
var greeting = 'Hello' + ', ' + 'Dart';
print(greeting); // Hello, Dart
```

Dart también une dos **literales** de cadena que están escritos uno junto al otro, sin ningún operador. Esto es útil para dividir un texto largo en varias líneas:

```dart
var text = 'Hello, '
    'Dart';
print(text); // Hello, Dart
```

Solo las cadenas se pueden concatenar con `+`: `'Age: ' + 30` es un error de compilación, porque `30` es un `int`.

---

En lugar de concatenar, puedes insertar valores directamente en una cadena con **interpolación**. Escribe `$name` para insertar el valor de una variable, y `${expression}` para insertar el resultado de cualquier expresión:

```dart
var name = 'Ana';
var age = 20;
print('$name is $age');             // Ana is 20
print('Next year: ${age + 1}');     // Next year: 21
```

La interpolación funciona con cualquier tipo: los números, booleanos y listas se convierten a texto automáticamente, así que `'Age: $age'` funciona bien aunque `age` sea un `int`.

---

Toda cadena conoce cuántos caracteres tiene a través de su propiedad `.length`. Los espacios y la puntuación también cuentan como caracteres:

```dart
var word = 'hello';
print(word.length);      // 5
print('a b'.length);     // 3
```

Puedes leer un único carácter con corchetes y su **índice**, empezando desde `0`. El resultado es un `String` de un solo carácter:

```dart
print(word[0]);                // h
print(word[word.length - 1]);  // o
```

Leer un índice fuera de la cadena (como `word[5]`) lanza un error.

---

Las cadenas en Dart son **inmutables**: una vez creada, una cadena nunca cambia. Métodos como `.toUpperCase()` y `.toLowerCase()` no modifican la cadena original, **devuelven una nueva**:

```dart
var word = 'Dart';
var loud = word.toUpperCase();
print(loud);  // DART
print(word);  // Dart
```

Si quieres que la variable contenga el nuevo valor, asigna de nuevo el resultado: `word = word.toUpperCase();`.

---

El texto escrito por un usuario suele tener espacios extra alrededor. El método `.trim()` devuelve una copia de la cadena sin los espacios en blanco iniciales y finales (espacios, tabulaciones y saltos de línea). `.trimLeft()` y `.trimRight()` los eliminan solo de un lado:

```dart
var input = '   hello  ';
print('[${input.trim()}]');      // [hello]
print('[${input.trimLeft()}]');  // [hello  ]
```

---

El método `.substring(start, end)` devuelve la parte de una cadena desde el índice `start` hasta, **sin incluirlo**, el índice `end`. Si omites `end`, toma todo hasta el final de la cadena:

```dart
var text = 'Hello Dart';
print(text.substring(0, 5));  // Hello
print(text.substring(6));     // Dart
```

---

Varios métodos te permiten buscar dentro de una cadena:

- `.contains(other)` devuelve `true` si `other` aparece en cualquier parte de la cadena
- `.startsWith(other)` y `.endsWith(other)` comprueban el inicio y el final
- `.indexOf(other)` devuelve el índice de la primera aparición, o `-1` si no se encuentra

```dart
var file = 'report.pdf';
print(file.contains('port'));    // true
print(file.startsWith('rep'));   // true
print(file.endsWith('.txt'));    // false
print(file.indexOf('.'));        // 6
print(file.indexOf('x'));        // -1
```

Todos son sensibles a mayúsculas y minúsculas: `'Dart'.contains('dart')` es `false`.

---

El método `.replaceAll(from, to)` devuelve una nueva cadena donde **cada** aparición de `from` se reemplaza por `to`. `.replaceFirst(from, to)` reemplaza solo la primera:

```dart
var text = 'a-b-c';
print(text.replaceAll('-', '+'));    // a+b+c
print(text.replaceFirst('-', '+'));  // a+b-c
```

---

El método `.split(separator)` corta una cadena en una `List<String>` en cada aparición del separador. Lo opuesto es `.join(separator)`, un método de las listas que une los elementos en una sola cadena:

```dart
var csv = 'a,b,c';
List<String> parts = csv.split(',');
print(parts);            // [a, b, c]
print(parts.join(' - ')); // a - b - c
```

Llamar a `.split('')` con un separador vacío te da una lista con cada carácter individual.
