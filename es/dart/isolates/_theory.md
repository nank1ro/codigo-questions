Cada línea de Dart que has escrito hasta ahora se ejecuta dentro de un **isolate**: un hilo con su propia memoria y su propio bucle de eventos. Un programa arranca con un isolate, el isolate *principal*, y puede iniciar más.

Lo que hace especiales a los isolates es que no comparten **nada**. Dos isolates nunca ven el mismo objeto, así que no hay bloqueos, ni carreras de datos, ni valores actualizados a medias. Se comunican entre sí únicamente pasando **copias** de mensajes.

La forma más corta de usar un segundo isolate es **`Isolate.run`**: recibe una función, la ejecuta en un isolate completamente nuevo y te devuelve un `Future` con su resultado:

```dart
import 'dart:isolate';

Future<void> main() async {
  final total = await Isolate.run(() => 21 * 2);
  print(total); // 42
}
```

`Isolate` vive en la librería `dart:isolate`, así que el archivo debe empezar con `import 'dart:isolate';`. Mientras el nuevo isolate calcula, el isolate principal queda libre: esto es **paralelismo** real, el trabajo ocurre en otro núcleo del procesador.

---

La función que le pasas a `Isolate.run` puede **capturar** variables de su entorno. Esos valores se copian al nuevo isolate junto con la función, así que el cálculo puede depender de quien la llama:

```dart
Future<int> triple(int n) {
  return Isolate.run(() => n * 3);
}
```

`Isolate.run` devuelve un `Future` de lo que devuelva la función, así que `triple` puede simplemente devolverlo: no hace falta `async` ni `await` cuando solo reenvías el future.

El propósito de mover trabajo a otro isolate es que los cálculos largos ya no congelen al principal. Un bucle que se ejecuta durante un segundo bloquea todo cuando corre en el isolate principal; dentro de `Isolate.run` se ejecuta en otro lado y el isolate principal sigue manejando sus propios eventos.

---

Entre isolates solo se copian los **datos**; el **código** no. Cada isolate de un programa ya puede ver todas las funciones de nivel superior y las clases de ese programa, así que el cálculo que se le da a `Isolate.run` puede llamarlas sin problema:

```dart
int slowLength(String text) => text.length;

Future<int> lengthInIsolate(String text) {
  return Isolate.run(() => slowLength(text));
}
```

Lo que viaja es el `text` capturado a la ida y el `int` resultante a la vuelta, cada uno una copia. El patrón es siempre el mismo: deja la función pesada donde está y envuelve la **llamada** en `Isolate.run`.

---

`await` y `Isolate.run` resuelven dos problemas distintos, y vale la pena no confundirlos.

`await` te da **concurrencia** en un único isolate: mientras una función espera un temporizador o un servidor, el isolate ejecuta otro código pendiente. Nada se ejecuta en el mismo instante; el isolate simplemente deja de estar ocioso. Esta es la herramienta adecuada para esperar.

`Isolate.run` te da **paralelismo**: un segundo isolate en un segundo núcleo del procesador, ejecutando su propio código en el mismo instante que el primero. Esta es la herramienta adecuada para calcular.

```dart
await Future.delayed(const Duration(seconds: 1)); // esperando: ningún núcleo está ocupado
await Isolate.run(() => hugeCalculation());       // calculando: otro núcleo está ocupado
```

Esperar un cálculo lento con `await` no ayuda en absoluto: `await bigSum()` sigue ejecutando `bigSum` en el isolate actual y lo bloquea hasta la última línea. Solo un segundo isolate saca ese trabajo de allí.

---

`Isolate.run` es el atajo para un único resultado. Cuando quieres un isolate que siga ejecutándose y reporte más de una vez, inícialo tú mismo con **`Isolate.spawn`** y dale una forma de responder.

Esa forma es un par de puertos. Un **`ReceivePort`** es un buzón: lo creas de tu lado y lees los mensajes que llegan. Su **`sendPort`** es la dirección de ese buzón, y es lo único que el otro isolate necesita para responder.

```dart
import 'dart:isolate';

void sayHello(SendPort port) {
  port.send('hi');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(sayHello, receivePort.sendPort);
  final message = await receivePort.first;
  print(message); // hi
}
```

`Isolate.spawn` recibe la función a ejecutar y el único mensaje que se le pasa, aquí el `SendPort`. Del otro lado, `send` deja un valor en el buzón, y `await receivePort.first` espera el primer mensaje y cierra el puerto.

---

La función que se le da a `Isolate.spawn` se llama el **punto de entrada**. Debe ser una función de nivel superior (o estática) que reciba exactamente un parámetro: el mensaje que `Isolate.spawn` le pasa.

```dart
void reportAnswer(SendPort port) {
  port.send(42);
}
```

Los mensajes que llegan a un `ReceivePort` tienen el tipo estático `dynamic`, porque cualquier valor pudo haber sido enviado. Cuando sabes qué envía el otro isolate, hazle un cast:

```dart
final receivePort = ReceivePort();
await Isolate.spawn(reportAnswer, receivePort.sendPort);
final answer = await receivePort.first as int;
```

---

Un isolate iniciado siempre sigue los mismos cuatro pasos: abrir el buzón, iniciar el worker con su dirección, esperar la respuesta y usarla.

```dart
import 'dart:isolate';

void worker(SendPort port) {
  port.send('done');
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(worker, receivePort.sendPort);
  print(await receivePort.first);
}
```

El `await` delante de `Isolate.spawn` espera a que el isolate *arranque*, no a que termine su trabajo: el resultado llega más tarde, a través del puerto.

---

`Isolate.spawn` pasa exactamente **un** mensaje al punto de entrada, y el worker normalmente necesita tanto un `SendPort` para responder como algunos datos con los que trabajar. El truco habitual es agrupar todo en una `List` y desempaquetarlo del otro lado:

```dart
void multiply(List<Object> message) {
  final port = message[0] as SendPort;
  final value = message[1] as int;
  port.send(value * 2);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(multiply, <Object>[receivePort.sendPort, 21]);
  print(await receivePort.first); // 42
}
```

La lista se copia a la ida, así que el worker lee sus propios valores. Un `SendPort` es una de las pocas cosas que no se copian sino que se comparten: sigue apuntando al buzón del isolate que lo creó, que es justamente por eso que puede usarse como dirección de respuesta.

---

`first` lee un mensaje y cierra el buzón. Un `ReceivePort` también es un **`Stream`**, así que para leer muchos mensajes lo recorres con `await for`.

El bucle nunca termina por sí solo: el puerto queda abierto esperando un mensaje que quizás nunca llegue. Por eso el worker envía un último valor como señal, a menudo `null`, y quien escucha reacciona llamando a **`close()`**, que termina el stream y el bucle:

```dart
import 'dart:isolate';

void countdown(SendPort port) {
  port.send(3);
  port.send(2);
  port.send(1);
  port.send(null);
}

Future<void> main() async {
  final receivePort = ReceivePort();
  await Isolate.spawn(countdown, receivePort.sendPort);
  await for (final message in receivePort) {
    if (message == null) {
      receivePort.close();
    } else {
      print(message);
    }
  }
  print('done');
}
```

---

Recolectar toda una serie de mensajes sigue una sola receta: una lista vacía antes del bucle, un `add` por cada mensaje real, y `close()` con la señal que termina el stream. Una vez que el puerto se cierra, el `await for` termina y la función puede devolver:

```dart
Future<List<int>> collect(ReceivePort port) async {
  final values = <int>[];
  await for (final message in port) {
    if (message == null) {
      port.close();
    } else {
      values.add(message as int);
    }
  }
  return values;
}
```

Los mensajes conservan el orden en el que fueron enviados, así que la lista que construyes refleja el trabajo del otro isolate paso a paso.

---

Un `ReceivePort` abierto cuenta como trabajo pendiente: mientras exista uno, el isolate que lo posee tiene una razón para seguir vivo y su bucle de eventos sigue esperando un mensaje. En un programa de línea de comandos, un isolate principal con un puerto abierto simplemente **nunca sale**, y tienes que detenerlo a mano.

Cerrar el puerto es por tanto parte del trabajo, no una optimización:

- `await port.first` lo cierra por ti después de un mensaje
- `port.close()` lo cierra explícitamente, que es lo que necesitas después de un bucle `await for`

`Isolate.run` no tiene nada de esta gestión: crea los puertos, los cierra y apaga el isolate por ti. Prefiérelo siempre que un resultado sea todo lo que necesitas.

---

Una excepción lanzada dentro de un isolate no puede saltar a otro: ambos tienen stacks separados. `Isolate.run` salva esa distancia por ti capturando el error, copiándolo de vuelta y haciendo que el future devuelto falle con él. De tu lado es por tanto un error asincrónico ordinario, capturado con `try`/`catch` alrededor del `await`:

```dart
Future<int> parseInIsolate(String text) async {
  try {
    return await Isolate.run(() => int.parse(text));
  } catch (e) {
    return -1;
  }
}
```

El `await` dentro del `try` importa, exactamente igual que con cualquier otro future: sin él, el future dejaría el bloque `try` sin terminar y el `catch` nunca se ejecutaría.

Con `Isolate.spawn` no existe ese puente. Un error no capturado mata el isolate iniciado en silencio y el padre sigue esperando un mensaje que nunca llegará, que es una razón más para recurrir primero a `Isolate.run`.

---

El error que vuelve de `Isolate.run` es una **copia** del que se lanzó del otro lado, así que las comprobaciones habituales siguen funcionando: `catch (e)` te da el objeto, y `e is FormatException` te dice qué tipo de fallo fue.

```dart
try {
  await Isolate.run(() => int.parse('abc'));
} on FormatException {
  print('not a number');
}
```

En lo que no puedes confiar es en que el stack trace apunte a tu propio isolate: el error viajó, el stack no.

---

En conjunto, un programa con `Isolate.run` se lee como código secuencial ordinario: la línea anterior a la llamada se ejecuta en el isolate principal, el cálculo se ejecuta en otro lado, y la línea posterior al `await` vuelve a ejecutarse en el isolate principal con el resultado en la mano.

```dart
import 'dart:isolate';

int twice(int n) => n * 2;

Future<void> main() async {
  print('start');
  final result = await Isolate.run(() => twice(4));
  print(result);
}
// start
// 8
```

---

Como los isolates no comparten memoria, cada mensaje se **copia** al cruzar. Los números, los booleanos, las cadenas, `null`, las listas, los maps y la mayoría de los objetos simples pueden hacer el viaje; unas pocas cosas no se pueden copiar en absoluto, como un socket abierto, e intentar enviar una lanza un `ArgumentError`.

La consecuencia es la regla que hace seguros a los isolates: después de enviar, los dos lados tienen **dos objetos independientes**. Lo que un isolate haga con su copia es invisible para el otro.

```dart
final numbers = [1, 2, 3];
await Isolate.run(() => numbers..add(4)); // la copia crece
print(numbers);                           // [1, 2, 3]
```

`SendPort` es la excepción que confirma la regla: se comparte en lugar de copiarse, precisamente para que pueda seguir apuntando al buzón original.

---

Cada `Isolate.run` inicia su propio isolate, así que varios de ellos realmente se ejecutan en el mismo instante, en tantos núcleos como tenga la máquina. El patrón es el que ya conoces de los futures: inicia primero cada cálculo y luego espera todos con `Future.wait`, que conserva los resultados en el orden de la entrada.

```dart
Future<List<int>> doubleAll(List<int> numbers) {
  return Future.wait(numbers.map((n) => Isolate.run(() => n * 2)));
}
```

Iniciar un isolate no es gratis: cuesta memoria y unos pocos milisegundos. Dividir un cálculo largo entre un puñado de isolates vale la pena; enviar mil sumas triviales a mil isolates no.
