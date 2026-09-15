Un **método de orden superior** es un método que toma una función como argumento. Las colecciones de Dart ofrecen muchos de ellos, y la función que pasas suele ser una función anónima escrita con la sintaxis de flecha `(x) => ...`.

`map` es el más común: llama a la función sobre cada elemento y produce los resultados, uno por cada elemento, dejando la colección original intacta:

```dart
final numbers = [1, 2, 3];
print(numbers.map((n) => n * 2)); // (2, 4, 6)
print(numbers);                   // [1, 2, 3]
```

Fíjate en los **paréntesis** de la salida. `map` no devuelve una `List`: devuelve un `Iterable`, una secuencia que puedes recorrer. Para obtener una lista real, llama a **`toList()`** sobre él:

```dart
final doubled = numbers.map((n) => n * 2).toList();
print(doubled); // [2, 4, 6]
```

Los corchetes en la salida indican que estás viendo una `List`, y los paréntesis que estás viendo un `Iterable` simple.

---

`where` toma una función que devuelve un `bool`, llamada **predicado**, y conserva solo los elementos para los que responde `true`. El orden de los elementos que sobreviven nunca cambia:

```dart
final numbers = [4, -2, 7, 0];
print(numbers.where((n) => n > 0).toList()); // [4, 7]
```

Como `map`, `where` devuelve un `Iterable` y nunca modifica la colección original, así que de nuevo es `toList()` lo que convierte el resultado en una `List`.

En otros lenguajes este método se llama `filter`; en Dart es `where`.

---

La función que se le da a `map` no tiene que devolver el mismo tipo que los elementos que recibe. Mapear una lista de cadenas a sus longitudes convierte una `List<String>` en un `Iterable<int>`, que `toList()` luego convierte en una `List<int>`:

```dart
final words = ['fig', 'kiwi'];
print(words.map((w) => w.length).toList()); // [3, 4]
```

El resultado siempre tiene **exactamente tantos elementos como el original**, en el mismo orden: `map` transforma elementos, nunca añade ni quita ninguno.

---

Algunos métodos de orden superior responden una pregunta sobre la colección en lugar de construir una nueva. Toman un predicado y devuelven un `bool`:

- `any` es `true` cuando **al menos un** elemento satisface el predicado
- `every` es `true` cuando **todos** los elementos lo satisfacen

```dart
final numbers = [1, 2, 3];
print(numbers.any((n) => n > 2));   // true
print(numbers.every((n) => n > 2)); // false
```

Ambos se detienen en cuanto la respuesta es segura: `any` en el primer elemento que coincide, `every` en el primero que no.

Sobre una colección vacía `any` es `false` y `every` es `true`: no hay ningún elemento que pruebe la primera, y ninguno que rompa la segunda.

---

`map` y `where` son **perezosos**: llamarlos no ejecuta nada. Devuelven un `Iterable` que recuerda la fuente y la función, y la función solo se llama mientras algo recorre el resultado, un elemento a la vez.

```dart
final numbers = [1, 2, 3];
final doubled = numbers.map((n) => n * 2); // todavía no se ha calculado nada
print(doubled.first);                      // calcula solo 2
```

`toList()` es lo que **materializa** la secuencia: la recorre de principio a fin y guarda cada resultado en una `List` real.

La pereza tiene dos consecuencias que vale la pena recordar. Un `Iterable` perezoso se recalcula cada vez que lo iteras, así que materializarlo una vez con `toList()` es más barato cuando necesitas los valores más de una vez. Y sigue mirando la colección original, así que cambiar esa colección cambia lo que el `Iterable` produce:

```dart
final numbers = [1, 2, 3];
final lazy = numbers.map((n) => n * 2);
final eager = numbers.map((n) => n * 2).toList();
numbers.add(4);
print(lazy.toList()); // [2, 4, 6, 8]
print(eager);         // [2, 4, 6]
```

---

`fold` combina una colección entera en un **único valor**. Toma dos argumentos: el valor inicial del **acumulador**, y una función que recibe el acumulador hasta el momento y el siguiente elemento, y devuelve el nuevo acumulador:

```dart
final numbers = [1, 2, 3, 4];
final total = numbers.fold(0, (acc, n) => acc + n);
print(total); // 10
```

Aquí `acc` empieza en `0`, luego se convierte en `1`, `3`, `6` y finalmente `10`.

El acumulador no tiene que ser un número, ni del mismo tipo que los elementos: empezar desde `''` y añadir texto construye una `String` a partir de una lista de cualquier cosa.

Un detalle a tener en cuenta: Dart deduce el tipo del acumulador a partir del valor inicial **y** de dónde se usa el resultado. Dentro de `print(...)` el tipo esperado es desconocido, así que guarda primero el resultado en una variable (o escribe `fold<int>(...)`), de lo contrario el compilador se queja de que no puede usar `+` sobre el acumulador.

---

`reduce` es el pariente más corto de `fold`. No toma valor inicial: el **primer elemento** es el acumulador inicial, y la función se ejecuta para cada elemento restante:

```dart
final numbers = [1, 2, 3, 4];
print(numbers.reduce((a, b) => a + b)); // 10
```

Como no hay valor inicial, el resultado siempre tiene el **mismo tipo que los elementos**, y llamar a `reduce` sobre una colección vacía lanza un `StateError`: no hay primer elemento desde el que empezar. `fold` no tiene ese problema, por eso es la opción por defecto más segura.

`reduce` da lo mejor de sí cuando buscas un elemento entre muchos, como el mayor:

```dart
print(numbers.reduce((a, b) => a > b ? a : b)); // 4
```

---

`firstWhere` devuelve el **primer** elemento que coincide con un predicado, en lugar de todos:

```dart
final words = ['fig', 'kiwi', 'banana'];
print(words.firstWhere((w) => w.length > 3)); // kiwi
```

Cuando nada coincide no hay ningún elemento que devolver, así que `firstWhere` lanza un `StateError`. Para dar una respuesta en lugar de un error, pasa el argumento con nombre **`orElse`**: una función sin parámetros que produce el valor de respaldo.

```dart
print(words.firstWhere((w) => w.length > 10, orElse: () => 'none')); // none
```

`orElse` es una función, no un valor simple, así que solo se llama cuando la búsqueda falla. Escribir `orElse: 'none'` no compila.

---

Cuando la función que le das a `map` devuelve una colección para cada elemento, acabas con una secuencia de colecciones. **`expand`** hace el mismo trabajo pero luego une todas en una única secuencia plana:

```dart
final numbers = [1, 2];
print(numbers.map((n) => [n, -n]).toList());    // [[1, -1], [2, -2]]
print(numbers.expand((n) => [n, -n]).toList()); // [1, -1, 2, -2]
```

El orden se conserva: todo lo producido por el primer elemento va primero, luego todo lo producido por el segundo, y así sucesivamente.

Como la colección devuelta puede tener cualquier tamaño, `expand` también es la forma de producir **más o menos** elementos de los que tenías al principio: devolver una lista vacía para un elemento simplemente lo descarta.

```dart
print(['a b', 'c'].expand((s) => s.split(' ')).toList()); // [a, b, c]
```

---

`take(n)` conserva los **primeros** `n` elementos y `skip(n)` los descarta. Ninguno toma una función, pero ambos devuelven un `Iterable` perezoso, así que encajan de forma natural entre los demás métodos de orden superior:

```dart
final scores = [10, 20, 30, 40, 50];
print(scores.take(2).toList()); // [10, 20]
print(scores.skip(3).toList()); // [40, 50]
```

Pedir más elementos de los que hay no es un error: simplemente obtienes lo que existe, o un resultado vacío.

`takeWhile` y `skipWhile` son las versiones con un predicado. Toman o descartan elementos desde el principio **mientras** el predicado se cumpla, y se detienen en el primer elemento que no lo cumple, aunque los posteriores volverían a coincidir:

```dart
print(scores.takeWhile((s) => s < 35).toList()); // [10, 20, 30]
```

---

Dart no tiene un método `sorted`. `sort` pertenece a `List`, reordena la lista **en su lugar** y no devuelve nada:

```dart
final numbers = [3, 1, 2];
numbers.sort();
print(numbers); // [1, 2, 3]
```

Como devuelve `void`, no puedes usar el resultado en absoluto: `final sorted = numbers.sort();` da un valor que el compilador no te deja leer. El modismo para una **copia** ordenada es `toList()` seguido de la cascada `..sort()`: `toList()` hace la copia, y `..` ejecuta `sort` sobre ella mientras sigue devolviendo la propia copia.

```dart
final numbers = [3, 1, 2];
final sorted = numbers.toList()..sort();
print(sorted);  // [1, 2, 3]
print(numbers); // [3, 1, 2], sin modificar
```

`sort` también acepta un **comparador**: una función de dos elementos que devuelve un número negativo cuando el primero va antes que el segundo, `0` cuando son iguales, y un número positivo en caso contrario. `compareTo` produce exactamente eso, así que ordenar por cualquier clave cabe en una sola línea:

```dart
final words = ['kiwi', 'fig', 'banana'];
print(words.toList()..sort((a, b) => a.length.compareTo(b.length)));
// [fig, kiwi, banana]
```

---

`fold` y `reduce` se parecen, y elegir entre ellos se reduce a dos preguntas: ¿puede la colección estar vacía, y el resultado tiene el mismo tipo que los elementos?

```dart
final words = ['fig', 'kiwi'];
final joined = words.reduce((a, b) => '$a, $b'); // String a partir de Strings
final letters = words.fold(0, (acc, w) => acc + w.length); // int a partir de Strings
print(joined);  // fig, kiwi
print(letters); // 7
```

`reduce` solo puede devolver un tipo de elemento, porque empieza desde un elemento. `fold` empieza desde un valor que eliges, así que el acumulador puede ser un `int` que cuenta, una `String` que crece, o incluso una `List` que se va construyendo. Y como ese valor inicial ya existe, una colección vacía es simplemente la respuesta que `fold` devuelve sin cambios, mientras que `reduce` no tiene nada que devolver y lanza un error.

---

Cada uno de estos métodos devuelve un `Iterable`, y cada `Iterable` tiene otra vez los mismos métodos. Eso es lo que permite **encadenarlos**: un cálculo completo se lee como un pipeline de izquierda a derecha, cada paso trabajando sobre lo que produjo el anterior.

```dart
final words = ['kiwi', 'fig', 'banana', 'date'];
print(words.where((w) => w.length == 4).map((w) => w.toUpperCase()).toList());
// [KIWI, DATE]
```

Solo el último paso necesita `toList()`: llamarlo en medio construiría una lista que nadie guarda.

El tipo cambia a lo largo de la cadena, y también lo que recibe la siguiente función: después de `where` sobre una `List<String>` todavía tienes cadenas, pero después de `map((w) => w.length)` el siguiente paso ve números.

Como cada paso es perezoso, el orden importa para el trabajo realizado, no solo para el resultado: filtrar primero con `where` significa que `map` se llama sobre menos elementos.

---

Nada en estos métodos es especial: simplemente tienen una **función como parámetro**, y tus propias funciones pueden hacer lo mismo. El tipo de un parámetro de función se escribe como el tipo de retorno, luego `Function`, y luego los tipos de los parámetros entre paréntesis:

```dart
List<int> applyAll(List<int> numbers, int Function(int) operation) {
  return numbers.map(operation).toList();
}
```

Quien llama decide **qué** ocurre, y la función decide **sobre qué**. Fíjate en cómo `operation` se entrega directamente a `map`: un valor de función se puede pasar como cualquier otro valor.

El argumento puede ser una función anónima, o el **nombre** de una existente, escrito sin paréntesis. Añadir los paréntesis la llamaría en lugar de pasarla:

```dart
int square(int n) => n * n;

print(applyAll([1, 2, 3], square));       // [1, 4, 9]
print(applyAll([1, 2, 3], (n) => n + 1)); // [2, 3, 4]
```

---

Una función también puede **devolver** una función. El tipo de retorno se escribe exactamente igual que un tipo de parámetro de función, y el valor devuelto suele ser una función anónima:

```dart
int Function(int) multiplier(int factor) {
  return (n) => n * factor;
}
```

`multiplier(3)` no multiplica nada: construye y devuelve una nueva función que multiplica por `3`. Esa función luego se guarda, se llama, o se pasa a `map` como cualquier otra:

```dart
final triple = multiplier(3);
print(triple(5));                       // 15
print([1, 2, 3].map(triple).toList());  // [3, 6, 9]
```

La función devuelta todavía recuerda `factor` después de que `multiplier` haya terminado. Una función que conserva las variables del ámbito donde fue creada se llama **closure**, y es lo que hace posibles fábricas de funciones como esta.

---

En conjunto, estos métodos reemplazan la mayoría de los bucles escritos a mano. Un pipeline suele leerse en tres etapas: **selecciona** los elementos con `where`, **transfórmalos** con `map`, y luego **combínalos** con `fold`:

```dart
final prices = [12, 40, 7];
final cheapTotal = prices.where((p) => p < 20).fold(0, (acc, p) => acc + p);
print(cheapTotal); // 19
```

Como `fold` elige su propio valor inicial, también puede terminar una cadena con un tipo que no tiene nada que ver con los elementos, como una `String` que crece una pieza a la vez:

```dart
final words = ['fig', 'kiwi'];
final firstLetters = words.fold('', (acc, w) => acc + w[0]);
print(firstLetters); // fk
```

Cada etapa se mantiene corta y dice lo que hace, que es la razón real para preferirlos sobre un bucle que hace las tres cosas a la vez.
