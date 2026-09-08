Ya sabes cómo declarar una función con un nombre, como `void sayHello() { ... }`. Dart también te permite escribir una función **sin nombre**: una **función anónima**. Tiene las mismas partes que una función con nombre (parámetros entre paréntesis y un cuerpo entre llaves) pero sin tipo de retorno y sin nombre:

```dart
(String name) {
  print('Hello, $name!');
}
```

Como no tiene nombre, la forma habitual de usarla es guardarla en una variable y luego llamar a la variable como si fuera una función:

```dart
var sayHello = (String name) {
  print('Hello, $name!');
};

sayHello('Dart'); // Hello, Dart!
```

Fíjate en el `;` después de la llave de cierre: la asignación es una sentencia normal.

---

Una función anónima puede tomar parámetros y `return` un valor, exactamente igual que una con nombre. El tipo de retorno no se escribe: Dart lo **infiere** de las sentencias `return` del cuerpo.

```dart
var add = (int a, int b) {
  return a + b;
};

print(add(2, 3)); // 5
```

---

Cuando el cuerpo es una sola expresión, una función anónima puede usar la **sintaxis flecha** `=>`, igual que una función con nombre. La flecha reemplaza las llaves y la palabra clave `return`:

```dart
var add = (int a, int b) => a + b;

print(add(2, 3)); // 5
```

Esta forma corta es con diferencia la manera más común de escribir funciones anónimas en Dart.

---

Las funciones son valores, por lo que tienen un tipo. El tipo de una función se escribe como el **tipo de retorno**, luego la palabra clave `Function`, y luego los **tipos de los parámetros** entre paréntesis:

```dart
int Function(int, int) add = (int a, int b) => a + b;
bool Function(String) isEmpty = (String s) => s.isEmpty;
void Function() hello = () => print('Hello');
```

Cuando la variable tiene este tipo, los tipos de los parámetros pueden omitirse en la función anónima, porque Dart los infiere del tipo declarado:

```dart
int Function(int, int) add = (a, b) => a + b;
```

El tipo `Function` por sí solo acepta cualquier función, sea cual sea sus parámetros y tipo de retorno, pero no le dice a Dart nada sobre cómo llamarla.

---

Como un tipo de función es un tipo normal, una función puede tomar **otra función como parámetro**. Dentro del cuerpo, el parámetro se llama como cualquier función:

```dart
int apply(int n, int Function(int) operation) {
  return operation(n);
}

print(apply(5, (n) => n * 2)); // 10
print(apply(5, (n) => n - 1)); // 4
```

Aquí quien llama decide qué hace `apply` pasando una función anónima como segundo argumento.

---

Muchos métodos de las colecciones de Dart toman una función como argumento, y las funciones anónimas son la forma natural de pasar una. El más sencillo es `forEach`, que llama a la función dada una vez por cada elemento de una lista:

```dart
var fruits = ['apple', 'kiwi'];

fruits.forEach((fruit) {
  print('I like $fruit');
});
// I like apple
// I like kiwi
```

El tipo del parámetro se infiere de la lista, así que `fruit` es un `String` sin necesidad de escribirlo.

---

Otros dos métodos muy comunes que toman una función anónima son `map` y `where`:

- `map` transforma cada elemento con la función y devuelve los nuevos valores
- `where` conserva solo los elementos para los que la función devuelve `true`

Ambos devuelven un `Iterable` perezoso; llama a `toList()` para convertir el resultado en una `List`:

```dart
var numbers = [1, 2, 3];

var squares = numbers.map((n) => n * n).toList();
print(squares); // [1, 4, 9]

var big = numbers.where((n) => n > 1).toList();
print(big); // [2, 3]
```

---

Como `map` y `where` devuelven ambos un `Iterable`, sus llamadas pueden **encadenarse** una tras otra. Cada paso recibe el resultado del anterior, y `toList()` se llama una vez al final:

```dart
var numbers = [1, 2, 3, 4, 5, 6];

var result = numbers.where((n) => n > 3).map((n) => n * 10).toList();
print(result); // [40, 50, 60]
```

---

`sort` reordena una lista en el sitio. Por defecto usa el orden natural de los elementos, pero puedes pasar una función anónima que **compara dos elementos** y devuelve un número negativo, cero o un número positivo. `compareTo` da exactamente ese número, por lo que es el bloque de construcción habitual:

```dart
var words = ['pear', 'fig', 'banana'];

words.sort((a, b) => a.length.compareTo(b.length));
print(words); // [fig, pear, banana]
```

Intercambiar `a` y `b` en la comparación invierte el orden.

---

`reduce` combina todos los elementos de una lista en un solo valor. Su función anónima toma dos parámetros: el valor **acumulado hasta ahora** y el **siguiente elemento**, y devuelve el nuevo valor acumulado. El primer elemento se usa como punto de partida:

```dart
var numbers = [2, 3, 4];

var product = numbers.reduce((total, n) => total * n);
print(product); // 24
```

`reduce` lanza un error en una lista vacía, ya que no hay un primer elemento desde el que empezar.

---

Una función también puede **devolver una función**. El tipo de retorno es entonces un tipo de función, y el cuerpo devuelve una función anónima:

```dart
int Function(int) makeAdder(int amount) {
  return (int n) => n + amount;
}

var addTen = makeAdder(10);
print(addTen(5)); // 15
```

Observa que la función devuelta sigue usando `amount`, un parámetro de `makeAdder`, incluso después de que `makeAdder` haya terminado. Una función que recuerda las variables a su alrededor de esta manera se llama **closure**.

---

Un closure no solo lee las variables que captura: también puede **modificarlas**, y los cambios se conservan entre llamadas. Esto permite mantener un estado privado sin una clase:

```dart
int Function() makeTimer() {
  var seconds = 0;
  return () {
    seconds += 10;
    return seconds;
  };
}

var timer = makeTimer();
print(timer()); // 10
print(timer()); // 20
```

Cada llamada a `makeTimer()` crea una variable `seconds` completamente nueva, así que dos temporizadores nunca comparten su contador.
