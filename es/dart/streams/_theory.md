Un `Future` representa un **único** valor que llega más tarde. Un **Stream** representa una **secuencia** de valores que llegan a lo largo del tiempo: pulsaciones de teclas, fragmentos de un archivo, mensajes de un servidor. Cada valor se llama **evento** y, después del último evento, el stream está **terminado**.

La forma más sencilla de construir un stream es `Stream.fromIterable`, que emite cada elemento de una lista, uno tras otro:

```dart
final numbers = Stream.fromIterable([1, 2, 3]);
```

Para consumir los eventos uno a uno usas un bucle **`await for`**. Como `await`, solo se permite dentro de una función marcada con `async`, así que `main` pasa a ser `Future<void> main() async`. El cuerpo del bucle se ejecuta una vez por evento y el bucle termina cuando el stream está terminado:

```dart
Future<void> main() async {
  final names = Stream.fromIterable(['Ada', 'Linus']);
  await for (final name in names) {
    print(name);
  }
  // Ada
  // Linus
}
```

Un bucle `for` normal no funciona aquí: un `Stream` no es un `Iterable`, sus valores no están disponibles todos a la vez.

---

`Stream.fromIterable` necesita todos los valores por adelantado. Para **producir** valores de uno en uno, escribe un **generador asíncrono**: una función cuyo cuerpo está marcado con `async*` y cuyo tipo de retorno es `Stream<T>`. Dentro de ella, `yield` envía un evento al stream:

```dart
Stream<int> countTo(int n) async* {
  for (var i = 1; i <= n; i++) {
    yield i;
  }
}
```

El cuerpo no se ejecuta cuando llamas a `countTo(3)`: se ejecuta de forma perezosa, a medida que el oyente pide valores, y el stream está terminado cuando el cuerpo acaba.

Para recoger todos los eventos en una `List`, llama a `toList()`. Devuelve un `Future<List<T>>`, así que lo esperas con `await`:

```dart
final values = await countTo(3).toList();
print(values); // [1, 2, 3]
```

---

Un bucle `await for` puede hacer más que imprimir: puede actualizar una variable declarada antes del bucle. Una función que consume un stream y calcula un resultado debe estar marcada con `async`, y devuelve un `Future` de ese resultado:

```dart
Future<int> count(Stream<String> words) async {
  var total = 0;
  await for (final word in words) {
    total += word.length;
  }
  return total;
}
```

La función solo llega al `return` después de que el stream esté terminado, así que quien la llama obtiene el valor final cuando espera el future:

```dart
print(await count(Stream.fromIterable(['hi', 'dart']))); // 6
```

---

Todo stream acaba terminando. En un generador `async*`, el stream está **terminado** en cuanto acaba el cuerpo de la función, tanto si llegó al final como si encontró un `return`. Un bucle `await for` sobre un stream terminado sale, y cualquier future de `toList()` se completa.

Un stream no se reinicia ni repite sus valores: una vez terminado, sigue terminado.

---

`await for` pausa la función actual hasta que el stream está terminado. Cuando quieres reaccionar a los eventos **sin esperar**, llama a `listen` y pasa una callback: se invoca una vez por evento, y el código que sigue a `listen` se ejecuta enseguida.

```dart
final ticks = Stream.fromIterable([1, 2]);
ticks.listen((tick) => print('tick $tick'));
print('not waiting');
// not waiting
// tick 1
// tick 2
```

`listen` también acepta un parámetro con nombre `onDone`, una función sin argumentos que se llama cuando el stream acaba:

```dart
final ticks2 = Stream.fromIterable([1, 2]);
ticks2.listen((tick) => print(tick), onDone: () => print('no more ticks'));
```

---

Un generador `async*` puede reenviar **todos los eventos de otro stream** con `yield*` (yield-star). Es como un bucle `await for` que emite cada valor, en una sola línea:

```dart
Stream<int> ones() async* {
  yield 1;
  yield 1;
}

Stream<int> sequence() async* {
  yield 0;
  yield* ones();
  yield 2;
}
// sequence() emits 0, 1, 1, 2
```

El stream exterior continúa con sus propios `yield` una vez que el stream interior está terminado.

---

Como `Iterable`, un `Stream` tiene métodos que construyen un **nuevo stream** a partir de uno existente:

- `map` transforma cada evento
- `where` conserva solo los eventos que cumplen una condición
- `take` se detiene después de un número dado de eventos

```dart
final numbers = Stream.fromIterable([1, 2, 3, 4, 5, 6]);
final firstOdds = numbers.where((n) => n.isOdd).take(2);
print(await firstOdds.toList()); // [1, 3]
```

Estos métodos son **perezosos**: no se ejecuta nada hasta que alguien escucha el stream resultante. Se pueden encadenar, y el stream de origen nunca se modifica.

---

Como `where`, `map` y `take` devuelven cada uno un stream, puedes encadenarlos y terminar con `toList()` para obtener el resultado como una lista. Solo el `toList()` final necesita un `await`, porque es la única llamada que devuelve un `Future`:

```dart
final numbers = Stream.fromIterable([5, 12, 8, 20, 3]);
final big = await numbers.where((n) => n > 6).take(2).toList();
print(big); // [12, 8]
```

---

Además de `toList()`, un stream ofrece otros métodos que **consumen** todos sus eventos y devuelven un único `Future`:

- `first` y `last` se completan con el primer o el último evento
- `length` se completa con el número de eventos
- `join(separator)` se completa con todos los eventos unidos en un solo `String`
- `reduce(combine)` combina los eventos de dos en dos en un único valor

```dart
final numbers = Stream.fromIterable([3, 9, 2]);
print(await numbers.reduce((a, b) => a + b)); // 14
```

`reduce` llama a `combine` con el resultado acumulado y el siguiente evento. Lanza una excepción si el stream está vacío, así que úsalo solo cuando se garantice al menos un evento.

---

Los métodos de `Stream` se dividen en dos grupos:

- los métodos de **transformación** como `map`, `where`, `take` y `skip` devuelven un **nuevo `Stream`** y son perezosos: no se procesa ningún evento hasta que se escucha el nuevo stream
- los métodos de **consumo** como `toList`, `reduce`, `join`, `first`, `last` y `length` escuchan el stream y devuelven un **`Future`** con el resultado final

Por eso una cadena está formada por cero o más llamadas de transformación seguidas de como mucho una llamada de consumo.

---

Los generadores producen eventos desde dentro de una función. Cuando los eventos vienen de **otro sitio** (un botón, una callback de red, otro objeto) necesitas un **`StreamController`**. Vive en la biblioteca `dart:async`, así que el archivo debe empezar con `import 'dart:async';`.

Un controlador es dueño de un stream y te deja empujar eventos dentro de él:

```dart
import 'dart:async';

Stream<int> dice() {
  final controller = StreamController<int>();
  controller.add(4);
  controller.add(2);
  controller.close();
  return controller.stream;
}
```

- `add(value)` envía un evento
- `close()` termina el stream; olvidarlo significa que los oyentes esperan para siempre
- `stream` es el `Stream` que consumen los oyentes

Los eventos añadidos antes de que alguien escuche se guardan en un búfer, así que el código de arriba es seguro: un oyente que llega más tarde recibe igualmente `4` y `2`.

---

Un `StreamController` se suele crear y consumir en el mismo sitio: te suscribes a `controller.stream` con `listen`, luego añades eventos con `add` y cierras el controlador con `close`. Como `listen` no espera, los eventos se entregan después de que acabe el código actual, pero siempre en el orden en que se añadieron:

```dart
import 'dart:async';

void main() {
  final controller = StreamController<int>();
  controller.stream.listen((n) => print('got $n'));
  controller.add(1);
  controller.add(2);
  controller.close();
}
// got 1
// got 2
```

---

Los streams vistos hasta ahora son de **suscripción única**: permiten exactamente un oyente. Llamar a `listen`, `await for` o a cualquier método de consumo por segunda vez lanza un `StateError` ("Stream has already been listened to").

Para compartir un stream entre varios oyentes, conviértelo en un stream **broadcast** con `asBroadcastStream()`:

```dart
final shared = Stream.fromIterable([1, 2, 3]).asBroadcastStream();
final total = shared.reduce((a, b) => a + b);
final count = shared.length;
print(await total); // 6
print(await count); // 3
```

Un stream broadcast no usa búfer: un oyente solo recibe los eventos emitidos **después** de suscribirse. En el ejemplo, ambos oyentes se suscriben antes del primer `await`, así que ambos reciben todos los eventos.

---

Un controlador puede crear un stream broadcast directamente con el constructor con nombre `StreamController<T>.broadcast()`. Su `stream` acepta cualquier número de oyentes, y cada evento se entrega a todos ellos, en el orden en que se suscribieron:

```dart
import 'dart:async';

void main() {
  final controller = StreamController<String>.broadcast();
  controller.stream.listen((msg) => print('first: $msg'));
  controller.stream.listen((msg) => print('second: $msg'));
  controller.add('hi');
  controller.close();
}
// first: hi
// second: hi
```

Como todo stream broadcast, no usa búfer: los eventos añadidos antes de que un oyente se suscriba se pierden para ese oyente.

---

Un stream puede llevar **errores** además de valores. Dentro de un generador `async*`, un `throw` envía un evento de error y termina el stream; un `StreamController` puede enviar uno con `addError`.

Del lado del consumo, un bucle `await for` relanza el error donde está el bucle, así que lo manejas con un `try`/`catch` normal alrededor del bucle:

```dart
Stream<int> risky() async* {
  yield 1;
  throw StateError('sensor offline');
}

Future<void> main() async {
  try {
    await for (final n in risky()) {
      print(n);
    }
  } catch (e) {
    print('caught: $e');
  }
}
// 1
// caught: Bad state: sensor offline
```

Con `listen`, pasa en su lugar una callback `onError`: `stream.listen(print, onError: (e) => print('caught: $e'));`
