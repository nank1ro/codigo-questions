Un **Set** es una colección de valores **únicos**: el mismo valor puede aparecer como máximo una vez. Al igual que un mapa, un Set se crea con la sintaxis literal `{}`, pero contiene valores simples en lugar de pares `key: value`:

```dart
Set<int> numbers = {1, 2, 3};
print(numbers); // {1, 2, 3}
```

La anotación de tipo `Set<int>` le indica a Dart que cada elemento es un `int`. Al igual que con las listas y los mapas, `var` infiere el tipo a partir del literal:

```dart
var colors = {'red', 'green'}; // Set<String>
```

---

Un Set nunca almacena el mismo valor dos veces. Si un literal contiene duplicados, solo se conserva la primera aparición y las demás se descartan en tiempo de ejecución sin ningún error (el analizador te advertirá sobre un literal que repite un valor):

```dart
var letters = {'a', 'b', 'a', 'b', 'c'};
print(letters); // {a, b, c}
```

La propiedad `.length` devuelve cuántos elementos **únicos** contiene el Set:

```dart
print(letters.length); // 3
```

---

El método `.add(value)` inserta un único valor. Devuelve `true` si el valor fue añadido y `false` si ya estaba en el Set, en cuyo caso no cambia nada. El método `.addAll(iterable)` inserta todos los elementos de una lista o de otro Set, saltando también los que ya están presentes:

```dart
var tags = {'dart'};
tags.add('web');    // true
tags.add('dart');   // false, already there
tags.addAll(['web', 'mobile']);
print(tags); // {dart, web, mobile}
```

Un literal `{}` vacío es un **mapa**, no un Set. Para crear un Set vacío, dale un tipo:

```dart
var empty = <String>{};
Set<int> other = {};
```

---

El método `.remove(value)` elimina un valor del Set. Devuelve `true` si el valor estaba presente y `false` en caso contrario:

```dart
var numbers = {1, 2, 3};
print(numbers.remove(2)); // true
print(numbers.remove(9)); // false
print(numbers); // {1, 3}
```

Para eliminar todos los elementos a la vez, usa `.clear()`.

---

Para comprobar si un valor está en un Set usa `.contains(value)`, que devuelve un `bool`. La propiedad `.isEmpty` es `true` cuando el Set no tiene elementos, y `.isNotEmpty` cuando tiene al menos uno:

```dart
var seen = {'x', 'y'};
print(seen.contains('x')); // true
print(seen.contains('z')); // false
print(seen.isEmpty);       // false
print(seen.isNotEmpty);    // true
```

---

El Set predeterminado en Dart recuerda el **orden de inserción**: cuando lo imprimes o lo recorres, los elementos aparecen en el orden en que se añadieron por primera vez. Añadir un valor que ya está presente no lo mueve de posición:

```dart
var numbers = {3, 1, 3, 2};
print(numbers); // {3, 1, 2}
```

---

Un Set es un `Iterable`, por lo que puedes recorrer sus elementos directamente con `for-in`, igual que con una lista. No hay índices: los elementos se visitan en el orden de inserción:

```dart
var numbers = {3, 1, 4};
for (var n in numbers) {
  print(n);
}
// 3
// 1
// 4
```
