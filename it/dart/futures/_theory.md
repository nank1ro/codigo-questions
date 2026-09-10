Alcune operazioni richiedono tempo: leggere un file, chiamare un server, aspettare un timer. Dart non blocca il programma mentre vengono eseguite. Al loro posto, una funzione del genere restituisce un **`Future<T>`**: la promessa che un valore di tipo `T` sarà disponibile **più tardi**.

Il future più semplice è quello che ha già il suo valore, costruito con `Future.value`:

```dart
Future<int> fetchNumber() {
  return Future.value(42);
}
```

Per tirare fuori il valore da un future usi **`await`**. `await` mette in pausa la funzione corrente finché il future non si completa, poi ti dà il valore semplice. È consentito solo dentro una funzione marcata **`async`**, quindi `main` diventa `Future<void> main() async`:

```dart
Future<void> main() async {
  final n = await fetchNumber();
  print(n); // 42
}
```

Senza `await`, `n` sarebbe il `Future` stesso, e `print(n)` mostrerebbe `Instance of 'Future<int>'` invece del numero.

---

Marcare una funzione come `async` fa due cose: permette `await` nel corpo e fa **restituire un `Future`** alla funzione. Qualunque cosa restituisci con `return` diventa il valore con cui il future si completa, quindi il tipo di ritorno dichiarato è `Future<T>` anche se il corpo restituisce un `T` semplice:

```dart
Future<String> label(int n) async {
  return 'item $n';
}

Future<void> main() async {
  print(await label(3)); // item 3
}
```

Qui non serve `Future.value`: la parola chiave `async` avvolge il valore restituito al posto tuo.

---

`Future.value` si completa subito. Per simulare un lavoro che richiede tempo, usa **`Future.delayed`**: prende una `Duration` e una funzione, aspetta la durata, poi si completa con ciò che la funzione restituisce:

```dart
Future<String> slowHello() {
  return Future.delayed(const Duration(milliseconds: 10), () => 'hello');
}
```

`Duration` si costruisce con parametri con nome come `seconds`, `milliseconds` o `minutes`. Dentro una funzione `async` puoi anche attendere un ritardo da solo, senza valore, giusto per fare una pausa:

```dart
Future<int> slowDouble(int n) async {
  await Future.delayed(const Duration(milliseconds: 10));
  return n * 2;
}
```

Entrambi gli stili sono comuni; il secondo si legge come normale codice sequenziale.

---

Tieni ben distinte le due facce di un future:

- una funzione `async` **dichiara** `Future<T>` e **restituisce** un `T` semplice: l'incapsulamento è automatico
- chi fa `await` su un `Future<T>` **riceve** un `T` semplice: l'estrazione è automatica

```dart
Future<int> count() async {
  return 3;                 // int, wrapped into Future<int>
}

Future<void> main() async {
  int n = await count();    // Future<int>, unwrapped to int
  Future<int> f = count();  // no await: still a Future<int>
}
```

Scrivere `int count() async` è un errore: una funzione `async` deve dichiarare un tipo di ritorno `Future` (o `void`).

---

`await` non è l'unico modo di usare un future. Puoi anche registrare una **callback** con **`then`**: la funzione che passi viene chiamata con il valore appena il future si completa. A differenza di `await`, `then` **non** mette in pausa la funzione corrente, quindi il codice che viene dopo viene eseguito per primo:

```dart
Future<int> fetchNumber() => Future.value(42);

void main() {
  fetchNumber().then((n) => print('got $n'));
  print('waiting');
}
// waiting
// got 42
```

Anche un future costruito con `Future.value` consegna il suo valore solo dopo che il codice corrente è finito, ed è per questo che `waiting` viene stampato per primo. `then` funziona in qualsiasi funzione, `async` o no.

---

Dentro una funzione `async`, `await` ti permette di scrivere passi asincroni come se fossero normale codice sequenziale. Ogni `await` aspetta il suo future, e la riga successiva viene eseguita solo quando il valore è disponibile:

```dart
Future<int> width() => Future.delayed(const Duration(milliseconds: 5), () => 4);
Future<int> height() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<int> area() async {
  final w = await width();
  final h = await height();
  return w * h; // 12
}
```

`await` può essere usato anche direttamente dentro un'espressione: `return await width() * await height();` dà lo stesso risultato.

---

Quando una funzione incontra un `await`, si **mette in pausa** su quella riga e il resto del programma continua. Le righe dopo l'`await` vengono eseguite solo quando il future si completa. Leggere una funzione `async` dall'alto verso il basso ti dice quindi l'ordine esatto dei suoi effetti:

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

Un future può anche completarsi con un **errore**. Quando una funzione `async` lancia, l'eccezione non sfugge subito: diventa l'errore del future restituito. Chi fa `await` su quel future vede l'errore lanciato all'`await`, quindi può gestirlo con un normale `try`/`catch`:

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

L'`await` dentro il `try` è essenziale: `return parseLater(s);` consegnerebbe il future al chiamante **senza aspettare**, quindi l'errore arriverebbe quando il blocco `try` è già finito e il `catch` non verrebbe mai eseguito.

---

Gli errori viaggiano con il future, non attraverso lo stack delle chiamate. Chiamare una funzione `async` che lancia non fa mai crollare il chiamante di per sé: l'errore viene conservato nel future restituito e salta fuori più tardi, nel punto in cui il future viene atteso. Un `try`/`catch` deve quindi avvolgere l'**`await`**, non la chiamata che ha creato il future.

Se nessuno attende o gestisce mai il future fallito, Dart segnala una *unhandled exception* e, in un programma da riga di comando, esce con un errore.

---

Con le callback, gli errori si gestiscono con **`catchError`**, la controparte di `then`. Entrambi restituiscono un nuovo future, quindi di solito si concatenano: `then` riceve il valore se il future ha successo, `catchError` riceve l'errore se fallisce, e viene eseguita solo una delle due callback:

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

Un `catchError` messo dopo `then` cattura anche gli errori lanciati dentro la callback di `then`. Come con `then`, il codice dopo la catena viene eseguito per primo, perché le callback vengono invocate solo quando il codice corrente è finito.

---

Quando più future non dipendono l'uno dall'altro, passali tutti a **`Future.wait`**: prende una `List<Future<T>>`, li lascia girare insieme e restituisce un unico `Future<List<T>>` che si completa quando **tutti** hanno finito. I risultati mantengono l'ordine della lista in ingresso, indipendentemente da quale future ha finito per primo:

```dart
Future<String> slow() => Future.delayed(const Duration(milliseconds: 20), () => 'slow');
Future<String> fast() => Future.delayed(const Duration(milliseconds: 5), () => 'fast');

final results = await Future.wait([slow(), fast()]);
print(results); // [slow, fast]
```

`await slow(); await fast();` impiega `25` millisecondi, perché `fast()` viene chiamata solo dopo che `slow()` si è completata; `await Future.wait([slow(), fast()])` impiega circa `20`, la durata del più lungo.

---

`Future.wait` è lo strumento per "carica più cose, poi continua". La forma tipica è: costruire la lista dei future, farci `await Future.wait` sopra, poi usare la lista risultante:

```dart
Future<int> stock() => Future.delayed(const Duration(milliseconds: 10), () => 8);
Future<int> orders() => Future.delayed(const Duration(milliseconds: 5), () => 3);

Future<void> main() async {
  final counts = await Future.wait([stock(), orders()]);
  print(counts); // [8, 3]
}
```

`orders()` si completa per prima, ma la lista segue comunque l'ordine delle chiamate: `stock()` per prima, `orders()` per seconda.

---

Non serve `Future.wait` per far girare due future insieme. Una funzione `async` inizia a essere eseguita appena viene **chiamata**, fino al suo primo `await`; il future che ricevi è il lavoro già in corso. Il trucco quindi è: **prima chiama, poi attendi**:

```dart
Future<int> pages() => Future.delayed(const Duration(milliseconds: 20), () => 300);
Future<int> words() => Future.delayed(const Duration(milliseconds: 20), () => 90000);

Future<double> average() async {
  final p = pages();          // both timers start now
  final w = words();
  return await w / await p;   // waits once, about 20 ms in total
}
```

Confronta con `return await words() / await pages();`, dove `pages()` viene chiamata solo dopo che `words()` si è completata: stesso risultato, il doppio del tempo. Preferisci la forma concorrente ogni volta che la seconda chiamata non ha bisogno del risultato della prima.

---

Un errore si **propaga** attraverso ogni `await` che non lo cattura. Se `load()` fallisce, `await load()` dentro `loadTwice()` lancia; poiché `loadTwice` non ha un `try`/`catch`, anche il suo future fallisce con lo stesso errore; e così via lungo la catena, finché qualche `await` non è avvolto in un `try`/`catch`:

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

Questo rispecchia il modo in cui le eccezioni si propagano attraverso le chiamate sincrone: le gestisci una volta sola, al livello che sa cosa fare.

---

`Future.wait` segue la stessa regola: se **uno qualsiasi** dei future fallisce, il future combinato si completa con quell'errore e `await Future.wait(...)` lancia. Non ottieni mai una lista parziale dei valori riusciti. Per tenere gli altri, gestisci l'errore dentro ogni singolo future, per esempio con `catchError`, prima di passarlo a `Future.wait`.

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

Poiché `await` trasforma gli errori di un future in normali eccezioni, al codice asincrono si applicano tutti i soliti schemi `try`/`catch`, inclusi i cicli che ritentano. Dentro un blocco `catch`, **`rethrow`** rilancia lo stesso errore, ed è così che ti arrendi dopo l'ultimo tentativo:

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

Un parametro di tipo funzione come `Future<String> Function() task` riceve la **funzione** stessa, non un future: ogni chiamata a `task()` avvia un nuovo tentativo.
