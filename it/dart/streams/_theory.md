Un `Future` rappresenta un **singolo** valore che arriva più tardi. Uno **Stream** rappresenta una **sequenza** di valori che arrivano nel tempo: pressioni di tasti, pezzi di un file, messaggi da un server. Ogni valore è chiamato **evento** e, dopo l'ultimo evento, lo stream è **concluso**.

Il modo più semplice per costruire uno stream è `Stream.fromIterable`, che emette ogni elemento di una lista, uno dopo l'altro:

```dart
final numbers = Stream.fromIterable([1, 2, 3]);
```

Per consumare gli eventi uno alla volta si usa un ciclo **`await for`**. Come `await`, è consentito solo dentro una funzione marcata `async`, quindi `main` diventa `Future<void> main() async`. Il corpo del ciclo viene eseguito una volta per evento e il ciclo termina quando lo stream è concluso:

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

Un normale ciclo `for` qui non funziona: uno `Stream` non è un `Iterable`, i suoi valori non sono disponibili tutti insieme.

---

`Stream.fromIterable` ha bisogno di tutti i valori in anticipo. Per **produrre** i valori uno alla volta, scrivi un **generatore asincrono**: una funzione il cui corpo è marcato `async*` e il cui tipo di ritorno è `Stream<T>`. Al suo interno, `yield` invia un evento allo stream:

```dart
Stream<int> countTo(int n) async* {
  for (var i = 1; i <= n; i++) {
    yield i;
  }
}
```

Il corpo non viene eseguito quando chiami `countTo(3)`: viene eseguito pigramente, man mano che l'ascoltatore chiede valori, e lo stream è concluso quando il corpo termina.

Per raccogliere ogni evento in una `List`, chiama `toList()`. Restituisce un `Future<List<T>>`, quindi lo devi attendere con `await`:

```dart
final values = await countTo(3).toList();
print(values); // [1, 2, 3]
```

---

Un ciclo `await for` può fare più che stampare: può aggiornare una variabile dichiarata prima del ciclo. Una funzione che consuma uno stream e calcola un risultato deve essere marcata `async`, e restituisce un `Future` di quel risultato:

```dart
Future<int> count(Stream<String> words) async {
  var total = 0;
  await for (final word in words) {
    total += word.length;
  }
  return total;
}
```

La funzione raggiunge il `return` solo dopo che lo stream è concluso, quindi il chiamante ottiene il valore finale quando attende il future:

```dart
print(await count(Stream.fromIterable(['hi', 'dart']))); // 6
```

---

Ogni stream prima o poi finisce. Per un generatore `async*`, lo stream è **concluso** non appena il corpo della funzione termina, sia che sia arrivato alla fine sia che abbia incontrato un `return`. Un ciclo `await for` su uno stream concluso esce, e ogni future di `toList()` si completa.

Uno stream non riparte e non ripete i suoi valori: una volta concluso, resta concluso.

---

`await for` mette in pausa la funzione corrente finché lo stream non è concluso. Quando vuoi reagire agli eventi **senza aspettare**, chiama `listen` e passa una callback: viene invocata una volta per evento, e il codice dopo `listen` viene eseguito subito.

```dart
final ticks = Stream.fromIterable([1, 2]);
ticks.listen((tick) => print('tick $tick'));
print('not waiting');
// not waiting
// tick 1
// tick 2
```

`listen` accetta anche un parametro con nome `onDone`, una funzione senza argomenti chiamata quando lo stream finisce:

```dart
final ticks2 = Stream.fromIterable([1, 2]);
ticks2.listen((tick) => print(tick), onDone: () => print('no more ticks'));
```

---

Un generatore `async*` può inoltrare **ogni evento di un altro stream** con `yield*` (yield-star). È come un ciclo `await for` che emette ogni valore, in una sola riga:

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

Lo stream esterno prosegue con i propri `yield` una volta che lo stream interno è concluso.

---

Come `Iterable`, uno `Stream` ha metodi che costruiscono un **nuovo stream** a partire da uno esistente:

- `map` trasforma ogni evento
- `where` mantiene solo gli eventi che soddisfano una condizione
- `take` si ferma dopo un dato numero di eventi

```dart
final numbers = Stream.fromIterable([1, 2, 3, 4, 5, 6]);
final firstOdds = numbers.where((n) => n.isOdd).take(2);
print(await firstOdds.toList()); // [1, 3]
```

Questi metodi sono **pigri**: non viene eseguito nulla finché qualcuno non ascolta lo stream risultante. Possono essere concatenati, e lo stream di partenza non viene mai modificato.

---

Poiché `where`, `map` e `take` restituiscono ognuno uno stream, puoi concatenarli e concludere con `toList()` per ottenere il risultato come lista. Solo il `toList()` finale ha bisogno di un `await`, perché è l'unica chiamata che restituisce un `Future`:

```dart
final numbers = Stream.fromIterable([5, 12, 8, 20, 3]);
final big = await numbers.where((n) => n > 6).take(2).toList();
print(big); // [12, 8]
```

---

Oltre a `toList()`, uno stream offre altri metodi che **consumano** tutti i suoi eventi e restituiscono un singolo `Future`:

- `first` e `last` si completano con il primo o l'ultimo evento
- `length` si completa con il numero di eventi
- `join(separator)` si completa con tutti gli eventi uniti in una sola `String`
- `reduce(combine)` combina gli eventi due alla volta in un unico valore

```dart
final numbers = Stream.fromIterable([3, 9, 2]);
print(await numbers.reduce((a, b) => a + b)); // 14
```

`reduce` chiama `combine` con il risultato ottenuto finora e l'evento successivo. Lancia un'eccezione se lo stream è vuoto, quindi usalo solo quando è garantito almeno un evento.

---

I metodi di `Stream` si dividono in due gruppi:

- i metodi di **trasformazione** come `map`, `where`, `take` e `skip` restituiscono un **nuovo `Stream`** e sono pigri: nessun evento viene elaborato finché il nuovo stream non viene ascoltato
- i metodi di **consumo** come `toList`, `reduce`, `join`, `first`, `last` e `length` ascoltano lo stream e restituiscono un **`Future`** con il risultato finale

Una catena quindi è fatta da zero o più chiamate di trasformazione seguite al massimo da una chiamata di consumo.

---

I generatori producono eventi dall'interno di una funzione. Quando gli eventi arrivano da **altrove** (un pulsante, una callback di rete, un altro oggetto) ti serve uno **`StreamController`**. Vive nella libreria `dart:async`, quindi il file deve iniziare con `import 'dart:async';`.

Un controller possiede uno stream e ti permette di inviarci eventi:

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

- `add(value)` invia un evento
- `close()` conclude lo stream; dimenticarlo significa che gli ascoltatori aspettano per sempre
- `stream` è lo `Stream` che gli ascoltatori consumano

Gli eventi aggiunti prima che qualcuno ascolti vengono tenuti in un buffer, quindi il codice sopra è sicuro: un ascoltatore che arriva dopo riceve comunque `4` e `2`.

---

Uno `StreamController` viene spesso creato e consumato nello stesso posto: ti iscrivi a `controller.stream` con `listen`, poi aggiungi eventi con `add` e chiudi il controller con `close`. Poiché `listen` non aspetta, gli eventi vengono consegnati dopo che il codice corrente è terminato, ma sempre nell'ordine in cui sono stati aggiunti:

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

Gli stream visti finora sono a **sottoscrizione singola**: permettono esattamente un ascoltatore. Chiamare `listen`, `await for` o un qualsiasi metodo di consumo una seconda volta lancia uno `StateError` ("Stream has already been listened to").

Per condividere uno stream tra più ascoltatori, convertilo in uno stream **broadcast** con `asBroadcastStream()`:

```dart
final shared = Stream.fromIterable([1, 2, 3]).asBroadcastStream();
final total = shared.reduce((a, b) => a + b);
final count = shared.length;
print(await total); // 6
print(await count); // 3
```

Uno stream broadcast non usa buffer: un ascoltatore riceve solo gli eventi emessi **dopo** la sua iscrizione. Nell'esempio entrambi gli ascoltatori si iscrivono prima del primo `await`, quindi entrambi ricevono ogni evento.

---

Un controller può creare direttamente uno stream broadcast con il costruttore con nome `StreamController<T>.broadcast()`. Il suo `stream` accetta un numero qualsiasi di ascoltatori, e ogni evento viene consegnato a tutti loro, nell'ordine in cui si sono iscritti:

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

Come ogni stream broadcast, non usa buffer: gli eventi aggiunti prima che un ascoltatore si iscriva sono persi per quell'ascoltatore.

---

Uno stream può trasportare **errori** oltre ai valori. Dentro un generatore `async*`, un `throw` invia un evento di errore e conclude lo stream; uno `StreamController` può inviarne uno con `addError`.

Dal lato di chi consuma, un ciclo `await for` rilancia l'errore nel punto in cui si trova il ciclo, quindi lo gestisci con un normale `try`/`catch` attorno al ciclo:

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

Con `listen`, passa invece una callback `onError`: `stream.listen(print, onError: (e) => print('caught: $e'));`
