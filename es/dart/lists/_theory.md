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
