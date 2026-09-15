Ogni riga di Dart che hai scritto finora viene eseguita dentro un **isolate**: un thread con la sua memoria e il suo event loop. Un programma parte con un isolate, l'isolate *main*, e può avviarne altri.

Ciò che rende gli isolate speciali è che non condividono **nulla**. Due isolate non vedono mai lo stesso oggetto, quindi non ci sono lock, né data race, né valori aggiornati a metà. Comunicano tra loro solo scambiandosi **copie** di messaggi.

Il modo più breve per usare un secondo isolate è **`Isolate.run`**: prende una funzione, la esegue su un isolate completamente nuovo e ti restituisce un `Future` con il suo risultato:

```dart
import 'dart:isolate';

Future<void> main() async {
  final total = await Isolate.run(() => 21 * 2);
  print(total); // 42
}
```

`Isolate` vive nella libreria `dart:isolate`, quindi il file deve iniziare con `import 'dart:isolate';`. Mentre il nuovo isolate calcola, l'isolate main resta libero: questo è vero **parallelismo**, il lavoro avviene su un altro core del processore.

---

La funzione che passi a `Isolate.run` può **catturare** le variabili che le stanno intorno. Quei valori vengono copiati nel nuovo isolate insieme alla funzione, così il calcolo può dipendere da chi lo ha invocato:

```dart
Future<int> triple(int n) {
  return Isolate.run(() => n * 3);
}
```

`Isolate.run` restituisce un `Future` di qualunque cosa restituisca la funzione, quindi `triple` può semplicemente restituirlo: non servono `async` né `await` quando ti limiti a passare il future avanti.

Il senso di spostare il lavoro su un altro isolate è che i calcoli lunghi non bloccano più quello principale. Un ciclo che gira per un secondo blocca tutto quando gira sull'isolate main; dentro `Isolate.run` gira altrove e l'isolate main continua a gestire i propri eventi.

---

Tra gli isolate vengono copiati solo i **dati**, non il **codice**. Ogni isolate di un programma può già vedere tutte le funzioni e le classi top-level di quel programma, quindi il calcolo affidato a `Isolate.run` è libero di chiamarle:

```dart
int slowLength(String text) => text.length;

Future<int> lengthInIsolate(String text) {
  return Isolate.run(() => slowLength(text));
}
```

Ciò che viaggia è il `text` catturato all'andata e l'`int` risultante al ritorno, ognuno una copia. Lo schema è sempre lo stesso: lascia la funzione pesante dov'è e avvolgi la **chiamata** in `Isolate.run`.

---

`await` e `Isolate.run` risolvono due problemi diversi, e vale la pena tenerli distinti.

`await` ti dà **concorrenza** su un singolo isolate: mentre una funzione aspetta un timer o un server, l'isolate esegue altro codice in sospeso. Nulla viene eseguito nello stesso istante, l'isolate smette semplicemente di stare fermo. Questo è lo strumento giusto per aspettare.

`Isolate.run` ti dà **parallelismo**: un secondo isolate su un secondo core del processore, che esegue il proprio codice nello stesso istante del primo. Questo è lo strumento giusto per calcolare.

```dart
await Future.delayed(const Duration(seconds: 1)); // in attesa: nessun core è occupato
await Isolate.run(() => hugeCalculation());       // in elaborazione: un altro core è occupato
```

Fare `await` su un calcolo lento non aiuta affatto: `await bigSum()` esegue comunque `bigSum` sull'isolate corrente e lo blocca fino all'ultima riga. Solo un secondo isolate sposta quel lavoro altrove.

---

`Isolate.run` è la scorciatoia per un risultato singolo. Quando vuoi un isolate che resta in esecuzione e fa sapere qualcosa più di una volta, lo avvii tu con **`Isolate.spawn`** e gli dai un modo per rispondere.

Quel modo è una coppia di porte. Una **`ReceivePort`** è una casella postale: la crei dalla tua parte e leggi i messaggi che arrivano. Il suo **`sendPort`** è l'indirizzo di quella casella, ed è l'unica cosa di cui l'altro isolate ha bisogno per rispondere.

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

`Isolate.spawn` prende la funzione da eseguire e l'unico messaggio da passarle, qui la `SendPort`. Dall'altra parte, `send` lascia cadere un valore nella casella, e `await receivePort.first` aspetta il primo messaggio e chiude la porta.

---

La funzione passata a `Isolate.spawn` si chiama **punto di ingresso**. Deve essere una funzione top-level (o statica) che prende esattamente un parametro: il messaggio che `Isolate.spawn` le passa.

```dart
void reportAnswer(SendPort port) {
  port.send(42);
}
```

I messaggi che arrivano in una `ReceivePort` hanno tipo statico `dynamic`, perché poteva essere inviato qualsiasi valore. Quando sai cosa invia l'altro isolate, fai un cast:

```dart
final receivePort = ReceivePort();
await Isolate.spawn(reportAnswer, receivePort.sendPort);
final answer = await receivePort.first as int;
```

---

Un isolate avviato segue sempre gli stessi quattro passi: apri la casella postale, avvia il worker con il suo indirizzo, aspetta la risposta, usala.

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

L'`await` davanti a `Isolate.spawn` aspetta che l'isolate *parta*, non che finisca il suo lavoro: il risultato arriva più tardi, attraverso la porta.

---

`Isolate.spawn` passa esattamente **un** messaggio al punto di ingresso, e il worker di solito ha bisogno sia di una `SendPort` su cui rispondere sia di qualche dato su cui lavorare. Il trucco abituale è impacchettare tutto in una `List` e spacchettarla dall'altra parte:

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

La lista viene copiata all'andata, quindi il worker legge i propri valori. Una `SendPort` è una delle poche cose che non viene copiata ma condivisa: continua a puntare alla casella postale dell'isolate che l'ha creata, ed è esattamente per questo che può essere usata come indirizzo di risposta.

---

`first` legge un messaggio e chiude la casella postale. Una `ReceivePort` è anche uno **`Stream`**, quindi per leggere molti messaggi la scorri con `await for`.

Il ciclo non finisce mai da solo: la porta resta aperta ad aspettare un messaggio che potrebbe non arrivare mai. Il worker invia quindi un ultimo valore come segnale, spesso `null`, e chi lo ascolta reagisce chiamando **`close()`**, che termina lo stream e il ciclo:

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

Raccogliere un'intera serie di messaggi segue una sola ricetta: una lista vuota prima del ciclo, una `add` per ogni messaggio vero, e `close()` sul segnale che termina lo stream. Una volta chiusa la porta, l'`await for` finisce e la funzione può restituire:

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

I messaggi mantengono l'ordine in cui sono stati inviati, quindi la lista che costruisci rispecchia passo dopo passo il lavoro dell'altro isolate.

---

Una `ReceivePort` aperta conta come lavoro in sospeso: finché ne esiste una, l'isolate che la possiede ha un motivo per restare vivo e il suo event loop continua ad aspettare un messaggio. In un programma da riga di comando, un isolate main con una porta aperta semplicemente **non esce mai**, e devi fermarlo a mano.

Chiudere la porta fa quindi parte del lavoro, non è un'ottimizzazione:

- `await port.first` la chiude per te dopo un messaggio
- `port.close()` la chiude esplicitamente, che è ciò che ti serve dopo un ciclo `await for`

`Isolate.run` non ha nessuna di queste faccende: crea le porte, le chiude e spegne l'isolate per te. Preferiscilo ogni volta che un solo risultato è tutto ciò di cui hai bisogno.

---

Un'eccezione lanciata dentro un isolate non può saltare verso un altro: i due hanno stack separati. `Isolate.run` colma questo divario per te, catturando l'errore, copiandolo indietro e facendo fallire con esso il future restituito. Dalla tua parte è quindi un normale errore asincrono, catturato con `try`/`catch` attorno all'`await`:

```dart
Future<int> parseInIsolate(String text) async {
  try {
    return await Isolate.run(() => int.parse(text));
  } catch (e) {
    return -1;
  }
}
```

L'`await` dentro il `try` conta, esattamente come per qualsiasi altro future: senza di esso il future uscirebbe dal blocco `try` incompleto e il `catch` non verrebbe mai eseguito.

Con `Isolate.spawn` non esiste un simile ponte. Un errore non catturato uccide in silenzio l'isolate avviato e il genitore continua ad aspettare un messaggio che non arriverà mai, che è un motivo in più per puntare prima a `Isolate.run`.

---

L'errore che torna da `Isolate.run` è una **copia** di quello lanciato dall'altra parte, quindi i controlli abituali funzionano ancora: `catch (e)` ti dà l'oggetto, e `e is FormatException` ti dice che tipo di fallimento era.

```dart
try {
  await Isolate.run(() => int.parse('abc'));
} on FormatException {
  print('not a number');
}
```

Su cui non puoi contare è lo stack trace che punta dentro il tuo isolate: l'errore ha viaggiato, lo stack no.

---

Messo insieme, un programma con `Isolate.run` si legge come normale codice sequenziale: la riga prima della chiamata gira sull'isolate main, il calcolo gira altrove, e la riga dopo l'`await` torna a girare sull'isolate main con il risultato in mano.

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

Poiché gli isolate non condividono memoria, ogni messaggio viene **copiato** quando attraversa il confine. Numeri, booleani, stringhe, `null`, liste, mappe e la maggior parte dei semplici oggetti possono fare il viaggio; alcune cose non si possono copiare affatto, come un socket aperto, e provare a inviarne una lancia un `ArgumentError`.

La conseguenza è la regola che rende gli isolate sicuri: dopo l'invio, le due parti tengono **due oggetti indipendenti**. Qualunque cosa un isolate faccia alla propria copia è invisibile all'altro.

```dart
final numbers = [1, 2, 3];
await Isolate.run(() => numbers..add(4)); // la copia cresce
print(numbers);                           // [1, 2, 3]
```

`SendPort` è l'eccezione che conferma la regola: viene condiviso anziché copiato, proprio così che possa continuare a puntare alla casella postale originale.

---

Ogni `Isolate.run` avvia il suo isolate, quindi parecchi di loro girano davvero nello stesso istante, su tutti i core di cui la macchina dispone. Lo schema è quello che conosci già dai future: avvia prima ogni calcolo, poi aspettali tutti con `Future.wait`, che mantiene i risultati nell'ordine dell'input.

```dart
Future<List<int>> doubleAll(List<int> numbers) {
  return Future.wait(numbers.map((n) => Isolate.run(() => n * 2)));
}
```

Avviare un isolate non è gratuito: costa memoria e qualche millisecondo. Spezzare un calcolo lungo su una manciata di isolate ripaga, mandare mille addizioni banali a mille isolate no.
