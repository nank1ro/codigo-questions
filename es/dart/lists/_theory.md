En Dart, una **lista** es una colección ordenada de elementos. La forma más sencilla de crear una lista es con la sintaxis literal `[]`:

```dart
List<int> numbers = [1, 2, 3];
```

También puedes usar la inferencia de tipos con `var`:

```dart
var fruits = ['apple', 'banana', 'cherry'];
```

La anotación de tipo `List<String>` le indica a Dart que cada elemento de la lista debe ser un `String`.

---

Las listas en Dart están **indexadas desde cero**, lo que significa que el primer elemento está en el índice `0`, el segundo en el índice `1`, y así sucesivamente.

```dart
var colors = ['red', 'green', 'blue'];
print(colors[0]); // red
print(colors[2]); // blue
```

El acceso a un elemento por índice se realiza con la sintaxis `list[index]`.

---

El método `.add()` agrega un único elemento al **final** de una lista:

```dart
var nums = [1, 2, 3];
nums.add(4);
print(nums); // [1, 2, 3, 4]
```

Ten en cuenta que `.add()` modifica la lista **en el lugar** y devuelve `void`.

---

La propiedad `.length` devuelve el número de elementos de una lista:

```dart
var scores = [95, 87, 72, 100];
print(scores.length); // 4
```

Una lista vacía tiene longitud `0`:

```dart
var empty = [];
print(empty.length); // 0
```

---

El método `.contains()` comprueba si una lista incluye un valor determinado. Devuelve `true` si se encuentra, `false` en caso contrario:

```dart
var fruits = ['apple', 'mango', 'grape'];
print(fruits.contains('mango'));  // true
print(fruits.contains('orange')); // false
```

Esto es útil para comprobar la pertenencia sin necesidad de un bucle.

---

El método `.remove(value)` elimina el **primer** elemento igual a `value` de una lista. Devuelve `true` si se eliminó un elemento, o `false` si no se encontró el valor.

```dart
var colors = ['red', 'green', 'blue'];
bool removed = colors.remove('green');
print(removed); // true
print(colors); // [red, blue]
```

---

Las propiedades `.first` y `.last` te dan el primer y el último elemento de una lista sin usar un índice.

```dart
var colors = ['red', 'green', 'blue'];
print(colors.first); // red
print(colors.last); // blue
```

Ambas lanzan un error si la lista está vacía.

---

La propiedad `.isEmpty` es `true` cuando una lista no tiene elementos, y `.isNotEmpty` es `true` cuando tiene al menos uno.

```dart
var colors = <String>[];
print(colors.isEmpty); // true
colors.add('red');
print(colors.isNotEmpty); // true
```

---

El método `.indexOf(value)` devuelve el índice del primer elemento igual a `value`. Si el valor no está en la lista, devuelve `-1`.

```dart
var colors = ['red', 'green', 'blue'];
print(colors.indexOf('green')); // 1
print(colors.indexOf('pink')); // -1
```

---

El método `.where()` conserva solo los elementos para los que una función devuelve `true`. No devuelve una nueva lista sino un `Iterable` perezoso (lazy), por lo que debes llamar a `.toList()` para convertir el resultado de nuevo en una `List`.

```dart
var numbers = [1, 2, 3, 4];
List<int> big = numbers.where((n) => n > 2).toList();
print(big); // [3, 4]
```
