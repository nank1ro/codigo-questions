Algunas operaciones llevan tiempo: leer un archivo, llamar a un servidor, esperar un temporizador. Dart no bloquea el programa mientras se ejecutan. En su lugar, una función así devuelve un **`Future<T>`**: la promesa de que un valor de tipo `T` estará disponible **más tarde**.

El future más simple es el que ya tiene su valor, construido con `Future.value`:

```dart
Future<int> fetchNumber() {
  return Future.value(42);
}
```

Para sacar el valor de un future usas **`await`**. `await` pausa la función actual hasta que el future se completa y entonces te da el valor sin envolver. Solo está permitido dentro de una función marcada con **`async`**, así que `main` pasa a ser `Future<void> main() async`:

```dart
Future<void> main() async {
  final n = await fetchNumber();
  print(n); // 42
}
```

Sin `await`, `n` sería el propio `Future` y `print(n)` mostraría `Instance of 'Future<int>'` en lugar del número.

---

Marcar una función como `async` hace dos cosas: permite usar `await` en el cuerpo y hace que la función **devuelva un `Future`**. Lo que devuelvas con `return` pasa a ser el valor con el que se completa el future, por eso el tipo de retorno declarado es `Future<T>` aunque el cuerpo devuelva un `T` sin envolver:

```dart
Future<String> label(int n) async {
  return 'item $n';
}

Future<void> main() async {
  print(await label(3)); // item 3
}
```

Aquí no necesitas `Future.value`: la palabra clave `async` envuelve el valor devuelto por ti.

---

`Future.value` se completa de inmediato. Para simular un trabajo que lleva tiempo, usa **`Future.delayed`**: recibe una `Duration` y una función, espera esa duración y luego se completa con lo que devuelve la función:

```dart
Future<String> slowHello() {
  return Future.delayed(const Duration(milliseconds: 10), () => 'hello');
}
```

`Duration` se construye con parámetros con nombre como `seconds`, `milliseconds` o `minutes`. Dentro de una función `async` también puedes esperar un retardo por sí solo, sin valor, solo para pausar:

```dart
Future<int> slowDouble(int n) async {
  await Future.delayed(const Duration(milliseconds: 10));
  return n * 2;
}
```

Ambos estilos son habituales; el segundo se lee como código secuencial normal.

---

Ten claras las dos caras de un future:

- una función `async` **declara** `Future<T>` y **devuelve** un `T` sin envolver: el envoltorio es automático
- quien hace `await` sobre un `Future<T>` **recibe** un `T` sin envolver: el desenvoltorio es automático

```dart
Future<int> count() async {
  return 3;                 // int, wrapped into Future<int>
}

Future<void> main() async {
  int n = await count();    // Future<int>, unwrapped to int
  Future<int> f = count();  // no await: still a Future<int>
}
```

Escribir `int count() async` es un error: una función `async` debe declarar un tipo de retorno `Future` (o `void`).

---

`await` no es la única forma de usar un future. También puedes registrar un **callback** con **`then`**: la función que le pasas se llama con el valor una vez que el future se completa. A diferencia de `await`, `then` **no** pausa la función actual, así que el código que viene después se ejecuta primero:

```dart
Future<int> fetchNumber() => Future.value(42);

void main() {
  fetchNumber().then((n) => print('got $n'));
  print('waiting');
}
// waiting
// got 42
```

Incluso un future construido con `Future.value` entrega su valor solo después de que el código actual haya terminado, por eso `waiting` se imprime primero. `then` funciona en cualquier función, sea `async` o no.

---

Dentro de una función `async`, `await` te permite escribir pasos asíncronos como si fueran código secuencial normal. Cada `await` espera su future, y la línea siguiente solo se ejecuta cuando el valor ya está ahí:

```dart
Future<int> width() => Future.delayed(const Duration(milliseconds: 5), () => 4);
Future<int> height() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<int> area() async {
  final w = await width();
  final h = await height();
  return w * h; // 12
}
```

`await` también puede usarse directamente dentro de una expresión: `return await width() * await height();` da el mismo resultado.

---

Cuando una función llega a un `await`, se **pausa** en esa línea y el resto del programa continúa. Las líneas posteriores al `await` se ejecutan solo cuando el future se completa. Por eso leer una función `async` de arriba abajo te dice el orden exacto de sus efectos:

```dart
Future<int> load() async {
  await Future.delayed(const Duration(milliseconds: 5));
  return 7;
}

Future<void> main() async {
  print('loading');
  final n = await load();
  print('value: $n');
  print('done');
}
// loading
// value: 7
// done
```

---

Un future también puede completarse con un **error**. Cuando una función `async` lanza, la excepción no escapa de inmediato: se convierte en el error del future devuelto. Quien haga `await` sobre ese future ve el error lanzado en el `await`, así que puede manejarse con un `try`/`catch` normal:

```dart
Future<int> parseLater(String s) async {
  await Future.delayed(const Duration(milliseconds: 5));
  return int.parse(s); // throws FormatException for 'abc'
}

Future<int> orZero(String s) async {
  try {
    return await parseLater(s);
  } catch (e) {
    return 0;
  }
}
```

El `await` dentro del `try` es esencial: `return parseLater(s);` entregaría el future al llamador **sin esperar**, así que el error llegaría cuando el bloque `try` ya hubiera terminado y el `catch` nunca se ejecutaría.

---

Los errores viajan con el future, no por la pila de llamadas. Llamar a una función `async` que lanza nunca hace fallar al llamador por sí solo: el error se guarda en el future devuelto y aparece más tarde, en el punto donde se espera el future. Por eso un `try`/`catch` tiene que envolver el **`await`**, no la llamada que creó el future.

Si nadie llega a esperar ni manejar el future fallido, Dart informa de una *unhandled exception* y, en un programa de línea de comandos, termina con error.

---

Con callbacks, los errores se manejan con **`catchError`**, la contraparte de `then`. Ambos devuelven un future nuevo, así que suelen encadenarse: `then` recibe el valor si el future tiene éxito, `catchError` recibe el error si falla, y solo se ejecuta uno de los dos callbacks:

```dart
Future<String> download() async {
  throw StateError('no network');
}

void main() {
  download()
      .then((data) => print('data: $data'))
      .catchError((e) => print('error: $e'));
  print('requested');
}
// requested
// error: Bad state: no network
```

Un `catchError` colocado después de `then` también captura los errores lanzados dentro del callback de `then`. Igual que con `then`, el código posterior a la cadena se ejecuta primero, porque los callbacks solo se invocan cuando el código actual ha terminado.

---

Cuando varios futures no dependen entre sí, pásalos todos a **`Future.wait`**: recibe una `List<Future<T>>`, los deja ejecutarse a la vez y devuelve un único `Future<List<T>>` que se completa cuando **todos** han terminado. Los resultados mantienen el orden de la lista de entrada, sin importar cuál terminó antes:

```dart
Future<String> slow() => Future.delayed(const Duration(milliseconds: 20), () => 'slow');
Future<String> fast() => Future.delayed(const Duration(milliseconds: 5), () => 'fast');

final results = await Future.wait([slow(), fast()]);
print(results); // [slow, fast]
```

`await slow(); await fast();` tarda `25` milisegundos, porque `fast()` solo se llama cuando `slow()` se ha completado; `await Future.wait([slow(), fast()])` tarda unos `20`, la duración del más largo.

---

`Future.wait` es la herramienta para "cargar varias cosas y luego continuar". La forma típica es: construir la lista de futures, hacer `await Future.wait` sobre ella y luego usar la lista resultante:

```dart
Future<int> stock() => Future.delayed(const Duration(milliseconds: 10), () => 8);
Future<int> orders() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<void> main() async {
  final counts = await Future.wait([stock(), orders()]);
  print(counts); // [8, 3]
}
```

`orders()` se completa antes, pero la lista sigue el orden de las llamadas: `stock()` primero, `orders()` segundo.

---

No necesitas `Future.wait` para ejecutar dos futures a la vez. Una función `async` empieza a ejecutarse en cuanto se la **llama**, hasta su primer `await`; el future que recibes es el trabajo ya en marcha. El truco es, por tanto: **llamar primero, esperar después**:

```dart
Future<int> pages() => Future.delayed(const Duration(milliseconds: 20), () => 300);
Future<int> words() => Future.delayed(const Duration(milliseconds: 20), () => 90000);

Future<double> average() async {
  final p = pages();          // both timers start now
  final w = words();
  return await w / await p;   // waits once, about 20 ms in total
}
```

Compáralo con `return await words() / await pages();`, donde `pages()` solo se llama después de que `words()` se haya completado: mismo resultado, el doble de tiempo. Prefiere la forma concurrente siempre que la segunda llamada no necesite el resultado de la primera.

---

Un error se **propaga** por cada `await` que no lo captura. Si `load()` falla, `await load()` dentro de `loadTwice()` lanza; como `loadTwice` no tiene `try`/`catch`, su propio future falla con el mismo error; y así hacia arriba en la cadena, hasta que algún `await` esté envuelto en un `try`/`catch`:

```dart
Future<int> load() async {
  throw StateError('offline');
}

Future<int> loadTwice() async {
  final n = await load();   // throws here, loadTwice fails too
  return n * 2;             // never runs
}

Future<void> main() async {
  try {
    print(await loadTwice());
  } catch (e) {
    print('failed: $e');    // failed: Bad state: offline
  }
}
```

Esto refleja cómo se propagan las excepciones en las llamadas síncronas: las manejas una vez, en el nivel que sabe qué hacer.

---

`Future.wait` sigue la misma regla: si **alguno** de los futures falla, el future combinado se completa con ese error y `await Future.wait(...)` lanza. Nunca obtienes una lista parcial con los valores que sí tuvieron éxito. Para conservar los demás, maneja el error dentro de cada future individual, por ejemplo con `catchError`, antes de pasarlo a `Future.wait`.

```dart
Future<int> ok() => Future.value(1);
Future<int> bad() async => throw StateError('nope');

Future<void> main() async {
  try {
    await Future.wait([ok(), bad()]);
  } catch (e) {
    print('failed: $e'); // failed: Bad state: nope
  }
}
```

---

Como `await` convierte los errores de un future en excepciones normales, al código asíncrono se le aplican todos los patrones habituales de `try`/`catch`, incluidos los bucles que reintentan. Dentro de un bloque `catch`, **`rethrow`** vuelve a lanzar el mismo error, que es la forma de rendirse tras el último intento:

```dart
Future<String> onceThenGiveUp(Future<String> Function() task) async {
  try {
    return await task();
  } catch (e) {
    print('first attempt failed');
    rethrow; // the caller sees the original error
  }
}
```

Un parámetro de tipo función como `Future<String> Function() task` recibe la **función** en sí, no un future: cada llamada a `task()` inicia un intento nuevo.
