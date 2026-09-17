Hay sentencias que no se pueden llevar a cabo: leer un texto que no es un número, tomar un elemento más allá del final de una lista, pedir el primer elemento de una vacía. Cuando eso ocurre, Dart **lanza** un objeto que describe el fallo.

Puedes lanzar uno tú mismo con la palabra clave `throw`. `Exception('message')` construye un objeto listo para usar que lleva una breve explicación:

```dart
throw Exception('no fuel');
```

Un throw no es un `return`. Abandona la sentencia, la función y todos los que la llamaron por encima, buscando algo que lo gestione. Cuando nada lo hace, el programa se detiene e imprime el fallo:

```
Unhandled exception:
Exception: no fuel
```

Todo lo que va después del throw se omite, así que las líneas que habrían llegado a ejecutarse nunca lo hacen. De eso trata este tema: decidir dónde se gestiona un fallo en lugar de dejar que termine el programa.

---

Para mantener el programa con vida, envuelve la sentencia arriesgada en un bloque `try` y describe la recuperación en un bloque `catch`:

```dart
try {
  print(int.parse('twelve'));
} catch (e) {
  print('that is not a number');
}
```

`int.parse` lanza una excepción cuando el texto no describe un número entero. Dart abandona el bloque `try` en la primera sentencia que lanza, omite el resto, ejecuta el bloque `catch` y después continúa con el código que sigue. La variable entre paréntesis, `e` aquí, es el propio objeto lanzado.

Nada de lo que hay dentro del bloque `try` se deshace, así que mantenlo tan corto como el fallo que esperas.

---

Un `catch` sin tipo lo acepta todo, lo que también oculta los fallos que no habías previsto. Para gestionar exactamente un tipo, indica su tipo en una cláusula `on`:

```dart
try {
  return int.parse(text);
} on FormatException catch (e) {
  return -1;
}
```

`int.parse` lanza una **`FormatException`** cuando el texto no es un número entero, así que ese es el tipo que debes indicar al leer datos de entrada. Una cláusula `on` coincide con ese tipo y sus subtipos, y con nada más: cualquier otro fallo sigue viajando hacia fuera y sigue apareciendo, en lugar de ser absorbido por una recuperación que nunca iba dirigida a él.

---

Un bloque `try` puede ir seguido de **varias** cláusulas, cada una recuperándose de un fallo distinto. Dart compara el objeto lanzado con ellas de arriba abajo y ejecuta la **primera** que coincide:

```dart
try {
  return names[int.parse(text)];
} on FormatException {
  return 'not a number';
} on RangeError {
  return 'out of range';
} catch (e) {
  return 'unknown problem';
}
```

Leer una lista con un índice que no existe lanza un **`RangeError`**, así que los dos fallos de esa misma línea obtienen respuestas distintas.

Como gana la primera coincidencia, el orden importa: una cláusula de un tipo general colocada encima de una más específica ganaría siempre, dejando la cláusula específica inalcanzable. Escribe primero las cláusulas específicas y, si quieres una red de seguridad, un `catch` a secas al final.

La cláusula `on RangeError` de arriba está aquí solo para mostrar cómo se ordenan varias cláusulas. `RangeError` señala un error en el código en lugar de una condición que el programa no pudo controlar, y un ejercicio posterior explica por qué semejante fallo debe prevenirse en lugar de capturarse.

---

A menudo la recuperación no necesita en absoluto el objeto lanzado: el tipo ya lo dice todo. En ese caso quita la parte `catch` y conserva solo la cláusula `on`:

```dart
try {
  return int.parse(text);
} on FormatException {
  return 0;
}
```

Las dos formas se diferencian solo en si recibes una variable:

- `on FormatException catch (e)` — coincide con ese tipo y te da el objeto como `e`
- `on FormatException` — coincide con ese tipo, sin variable
- `catch (e)` — coincide con todo y te da el objeto

Omitir una variable que no se usa deja claro lo que el gestor realmente usa.

---

Un tercer bloque puede ir después de los gestores. `finally` se ejecuta **en todos los casos**: después de que el bloque `try` termine con normalidad, después de que un gestor se recupere, y también cuando nada coincide y el fallo sigue viajando hacia fuera.

```dart
try {
  return 'parsed ${int.parse(text)}';
} on FormatException {
  return 'failed';
} finally {
  print('done');
}
```

Se ejecuta incluso antes de que un `return` entregue su valor, por eso el mensaje de arriba se imprime antes de que el llamador vea el resultado. Eso hace de `finally` el lugar para el trabajo que debe ocurrir de cualquier forma, como cerrar lo que abriste.

---

Tu propio código lanza igual que lo hace la biblioteca. `Exception('message')` construye una excepción sencilla que lleva una breve explicación, y `throw` la pone en camino:

```dart
if (amount > balance) {
  throw Exception('insufficient funds');
}
```

El mensaje no se pierde: `toString()` junta la palabra `Exception`, dos puntos y el mensaje, que es exactamente lo que imprime el informe de excepción no controlada.

```dart
print(Exception('insufficient funds')); // Exception: insufficient funds
```

Lanzar es mejor que devolver un valor inventado como `-1`: el llamador no puede olvidarse de mirarlo, y el motivo viaja con él.

---

A veces un gestor no es el lugar adecuado para recuperarse: solo quieres *notar* el fallo y dejar que continúe hacia el llamador que de verdad puede ocuparse de él. La palabra clave `rethrow` hace eso, dentro de un bloque `catch` o `on ... catch`:

```dart
try {
  return int.parse(text);
} on FormatException {
  log.add('bad input: $text');
  rethrow;
}
```

`rethrow` envía hacia fuera el **mismo** objeto, así que el llamador ve el fallo original. Escribir `throw e` en su lugar también funcionaría, pero reinicia el viaje y pierde dónde ocurrió el fallo por primera vez.

Un bloque `finally` en la misma sentencia sigue ejecutándose, incluso en el camino hacia fuera.

---

Una cláusula `catch` acepta un **segundo** parámetro:

```dart
try {
  return int.parse(text);
} on FormatException catch (e, s) {
  log.add('$e');
  log.add('$s');
  rethrow;
}
```

El primero es el objeto lanzado, el segundo es un `StackTrace`: la cadena de llamadas que se estaban ejecutando en el momento del throw. Responde a *dónde* se originó el fallo, algo que el mensaje por sí solo rara vez hace.

Un stack trace enumera nombres de archivo, números de línea y marcos, y cambia con la compilación y la ruta de llamadas. Imprímelo, adjúntalo a un informe, pásalo — pero nunca lo compares con un texto fijo, y nunca construyas el comportamiento del programa sobre su contenido. Pídelo solo cuando vayas a registrarlo.

---

`Exception` es una interfaz, así que tu propia clase puede serlo. Una excepción personalizada le da al fallo un nombre que una cláusula `on` puede seleccionar, y campos que un gestor puede leer:

```dart
class EmptyCartException implements Exception {
  final String message;

  EmptyCartException(this.message);

  @override
  String toString() => 'EmptyCartException: $message';
}

throw EmptyCartException('nothing to pay for');
```

Tres partes merecen conservarse: `implements Exception` para que la clase pertenezca al grupo de los demás fallos, un campo `final` que lleve el detalle y un `toString()` sobreescrito para que el informe de excepción no controlada sea legible. Sin esa sobreescritura, Dart imprime el nombre de la clase a secas y el detalle se pierde.

---

Dart lanza dos familias de objetos, y significan cosas opuestas.

Una **`Exception`** describe una condición que el programa no pudo controlar: un texto que no era un número, un archivo que no estaba, una red que no respondió con nada. `FormatException` es una de ellas. Son esperadas, y capturarlas es la respuesta normal.

Un **`Error`** describe una equivocación en el propio código:

- `ArgumentError` — una función fue llamada con un valor que documenta como inválido
- `StateError` — un objeto fue usado en un momento en que no puede hacer lo que se le pide
- `RangeError` — un índice o un valor estaba fuera del rango permitido

Capturar un `Error` oculta el fallo del código en lugar de arreglarlo. La respuesta correcta es cambiar el código para que deje de lanzarse: comprueba el argumento antes de llamar, o usa una API que no lance. Por eso una cláusula `on FormatException` es una buena práctica, mientras que una cláusula `on ArgumentError` casi nunca lo es.

---

Algunas bibliotecas ofrecen una versión que no lanza nada en absoluto. Junto a `int.parse`, Dart tiene **`int.tryParse`**: la misma conversión, pero devuelve `null` en lugar de lanzar cuando el texto no es un número.

```dart
print(int.parse('42'));     // 42
print(int.tryParse('42'));  // 42
print(int.tryParse('42x')); // null
```

El resultado es un `int?`, así que el operador `??` lo convierte directamente en un valor por defecto:

```dart
final port = int.tryParse(text) ?? 8080;
```

Cuando el fallo es ordinario y solo quieres un valor alternativo, esto es más corto y claro que un bloque `try`. Reserva `int.parse` para los casos en que un texto defectuoso es de verdad un fallo del que alguien más arriba debe enterarse.

---

`firstWhere` devuelve el primer elemento que cumple una condición. Cuando nada la cumple no hay elemento que devolver, así que lanza un `StateError`:

```dart
final words = ['a', 'fg'];
print(words.firstWhere((w) => w.length > 3)); // Bad state: No element
```

Como `int.tryParse`, la biblioteca ofrece una salida. El parámetro con nombre `orElse` recibe una función que produce el valor a usar cuando nada coincidió:

```dart
print(words.firstWhere((w) => w.length > 3, orElse: () => 'none')); // none
```

La elección es la misma que antes: `orElse` cuando "nada coincidió" es un desenlace ordinario, la llamada a secas cuando significaría que los datos están rotos y alguien debe enterarse.

---

El `throw` y el `try` no tienen que vivir en la misma función. Una función que no puede hacer su trabajo lanza, y el llamador que sabe qué hacer al respecto captura:

```dart
int ageFromText(String text) {
  final age = int.tryParse(text);
  if (age == null) throw FormatException('not a number');
  return age;
}
```

`ageFromText` no opina sobre si una edad defectuosa debe terminar el programa, mostrar un mensaje o saltarse — esa es la decisión del llamador, y el llamador es donde pertenece el bloque `try`. Esta separación es la razón por la que lanzar vale más que devolver `-1`: el fallo llega al único lugar que puede responderle.

Recuerda que el bloque `try` se detiene en el primer fallo, así que las sentencias posteriores a la llamada que falla también se omiten.

---

Dónde se coloca el bloque `try` decide cuánto trabajo destruye un solo fallo. Alrededor de un bucle, el primer elemento defectuoso termina el lote entero; **dentro** del bucle, solo ese elemento se pierde y el resto sigue procesándose:

```dart
for (final text in texts) {
  try {
    total += int.parse(text);
  } on FormatException {
    continue;
  }
}
```

Esta es la forma cotidiana de importar un archivo, leer una lista de ajustes o gestionar una cola de mensajes: una fila dañada no debería desechar las buenas. La regla sigue siendo la misma de antes — mantén el bloque `try` alrededor de la sentencia que puede fallar, y no más grande.

---

La última pieza es lanzar un `Error` a propósito. Una función que documenta qué acepta debe rechazar cualquier otra cosa de forma sonora, y `ArgumentError` es el objeto para ello:

```dart
int setVolume(int level) {
  if (level < 0 || level > 100) {
    throw ArgumentError('level must be between 0 and 100');
  }
  return level;
}
```

El mensaje es accesible como `e.message`, y `toString()` imprime `Invalid argument(s): ` seguido de él.

Esto no contradice la regla de antes. Lanzar un `ArgumentError` es correcto, capturarlo no lo es: le dice al autor del *llamador* que la llamada en sí está mal, y la solución es una comprobación antes de la llamada, no un gestor alrededor de ella.
