Alcune istruzioni non possono essere portate a termine: leggere un testo che non è un numero, prendere un elemento oltre la fine di una lista, chiedere il primo elemento di una lista vuota. Quando succede, Dart **lancia** un oggetto che descrive l'errore.

Puoi lanciarne uno tu stesso con la parola chiave `throw`. `Exception('message')` costruisce un oggetto già pronto che porta con sé una breve spiegazione:

```dart
throw Exception('no fuel');
```

Un lancio non è un `return`. Abbandona l'istruzione, la funzione e ogni chiamante sopra di essa, cercando qualcosa che la gestisca. Quando non c'è nulla, il programma si ferma e stampa l'errore:

```
Unhandled exception:
Exception: no fuel
```

Tutto ciò che segue il lancio viene saltato, quindi le righe che sarebbero state eseguite non lo vengono mai. È questo il tema dell'argomento: decidere dove un errore viene gestito invece di lasciare che termini il programma.

---

Per tenere in vita il programma, avvolgi l'istruzione rischiosa in un blocco `try` e descrivi il recupero in un blocco `catch`:

```dart
try {
  print(int.parse('twelve'));
} catch (e) {
  print('that is not a number');
}
```

`int.parse` lancia quando il testo non descrive un numero intero. Dart esce dal blocco `try` alla prima istruzione che lancia, salta il resto del blocco, esegue il blocco `catch` e poi prosegue con il codice che segue. La variabile tra parentesi, qui `e`, è l'oggetto lanciato stesso.

Nulla di ciò che sta dentro il blocco `try` viene annullato, quindi mantienilo corto quanto l'errore che ti aspetti.

---

Un `catch` senza tipo cattura tutto, e nasconde anche gli errori che non avevi previsto. Per gestire esattamente un solo tipo, indica il suo tipo in una clausola `on`:

```dart
try {
  return int.parse(text);
} on FormatException catch (e) {
  return -1;
}
```

`int.parse` lancia una **`FormatException`** quando il testo non è un numero intero, quindi è quel tipo da indicare quando leggi un input. Una clausola `on` corrisponde a quel tipo e ai suoi sottotipi, e a nient'altro: qualunque altro errore continua a viaggiare verso l'esterno e continua a presentarsi, invece di essere ingoiato da un recupero che non era pensato per lui.

---

Un blocco `try` può essere seguito da **più** clausole, ognuna delle quali si riprende da un errore diverso. Dart confronta l'oggetto lanciato con esse dall'alto verso il basso ed esegue la **prima** che corrisponde:

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

Leggere una lista con un indice che non esiste lancia un **`RangeError`**, quindi i due errori di quella sola riga ricevono risposte diverse.

Poiché vince la prima corrispondenza, l'ordine conta: una clausola per un tipo generale messa sopra una più specifica vincerebbe sempre, lasciando la clausola specifica irraggiungibile. Scrivi prima le clausole specifiche, e un `catch` senza tipo per ultimo se vuoi una rete di sicurezza.

La clausola `on RangeError` qui sopra è presente solo per mostrare come si ordinano più clausole. Un `RangeError` segnala un errore nel codice più che una condizione che il programma non poteva controllare, e un esercizio successivo spiega perché un simile errore dovrebbe essere prevenuto invece che catturato.

---

Spesso il recupero non ha bisogno dell'oggetto lanciato: il tipo dice già tutto. In quel caso elimina la parte `catch` e tieni solo la clausola `on`:

```dart
try {
  return int.parse(text);
} on FormatException {
  return 0;
}
```

Le due forme differiscono solo per il fatto di ricevere o meno una variabile:

- `on FormatException catch (e)` — corrisponde a quel tipo e ti dà l'oggetto come `e`
- `on FormatException` — corrisponde a quel tipo, nessuna variabile
- `catch (e)` — corrisponde a tutto e ti dà l'oggetto

Omettere una variabile inutilizzata mantiene il gestore onesto riguardo a ciò che usa davvero.

---

Un terzo blocco può seguire i gestori. `finally` viene eseguito **in ogni caso**: dopo che il blocco `try` è terminato normalmente, dopo che un gestore si è ripreso, e anche quando nulla corrisponde e l'errore sta ancora viaggiando verso l'esterno.

```dart
try {
  return 'parsed ${int.parse(text)}';
} on FormatException {
  return 'failed';
} finally {
  print('done');
}
```

Viene eseguito persino prima che un `return` riconsegni il suo valore, ed è per questo che il messaggio qui sopra viene stampato prima che il chiamante veda il risultato. Questo fa di `finally` il posto per il lavoro che deve avvenire in ogni caso, come chiudere ciò che hai aperto.

---

Il tuo codice lancia allo stesso modo in cui lancia la libreria. `Exception('message')` costruisce un'eccezione semplice che porta con sé una breve spiegazione, e `throw` la mette in viaggio:

```dart
if (amount > balance) {
  throw Exception('insufficient funds');
}
```

Il messaggio non va perso: `toString()` mette insieme la parola `Exception`, due punti e il messaggio, che è esattamente ciò che stampa il resoconto dell'eccezione non gestita.

```dart
print(Exception('insufficient funds')); // Exception: insufficient funds
```

Lanciare è meglio che restituire un valore inventato come `-1`: il chiamante non può dimenticarsi di guardarlo, e il motivo viaggia con esso.

---

A volte un gestore non è il posto giusto per riprendersi: vuoi solo *accorgerti* dell'errore e lasciarlo proseguire verso il chiamante che può davvero occuparsene. La parola chiave `rethrow` fa proprio questo, dentro un blocco `catch` o `on ... catch`:

```dart
try {
  return int.parse(text);
} on FormatException {
  log.add('bad input: $text');
  rethrow;
}
```

`rethrow` rimanda oltre lo **stesso** oggetto, quindi il chiamante vede l'errore originale. Scrivere `throw e` al suo posto funzionerebbe ugualmente, ma fa ripartire il viaggio e perde il punto in cui l'errore si è verificato la prima volta.

Un blocco `finally` nella stessa istruzione viene comunque eseguito, anche mentre si esce.

---

Una clausola `catch` accetta un **secondo** parametro:

```dart
try {
  return int.parse(text);
} on FormatException catch (e, s) {
  log.add('$e');
  log.add('$s');
  rethrow;
}
```

Il primo è l'oggetto lanciato, il secondo è uno `StackTrace`: la catena di chiamate in esecuzione al momento del lancio. Risponde alla domanda *da dove* è nato l'errore, cosa che il messaggio da solo fa raramente.

Uno stack trace elenca nomi di file, numeri di riga e frame, e cambia con la build e con il percorso delle chiamate. Stampalo, allegalo a un resoconto, passalo avanti — ma non confrontarlo mai con un testo fisso, e non costruire mai il comportamento del programma sul suo contenuto. Richiedilo solo quando intendi registrarlo.

---

`Exception` è un'interfaccia, quindi anche la tua classe può esserlo. Un'eccezione personalizzata dà all'errore un nome che una clausola `on` può selezionare, e campi che un gestore può leggere:

```dart
class EmptyCartException implements Exception {
  final String message;

  EmptyCartException(this.message);

  @override
  String toString() => 'EmptyCartException: $message';
}

throw EmptyCartException('nothing to pay for');
```

Tre parti meritano di essere tenute: `implements Exception` così la classe sta insieme agli altri errori, un campo `final` che porta con sé il dettaglio, e un `toString()` sovrascritto così il resoconto dell'eccezione non gestita è leggibile. Senza quella sovrascrittura, Dart stampa il solo nome della classe e il dettaglio va perso.

---

Dart lancia due famiglie di oggetti, e significano cose opposte.

Un'**`Exception`** descrive una condizione che il programma non poteva controllare: un testo che non era un numero, un file che non c'era, una rete che non ha risposto. `FormatException` è una di queste. Sono previste, e catturarle è la risposta normale.

Un **`Error`** descrive un errore nel codice stesso:

- `ArgumentError` — una funzione è stata chiamata con un valore che essa stessa documenta come non valido
- `StateError` — un oggetto è stato usato in un momento in cui non può fare ciò che gli è stato chiesto
- `RangeError` — un indice o un valore era fuori dall'intervallo consentito

Catturare un `Error` nasconde il bug invece di correggerlo. La risposta giusta è cambiare il codice così che smetta di essere lanciato: controlla l'argomento prima di chiamare, oppure usa un'API che non lancia. Per questo una clausola `on FormatException` è una buona pratica, mentre una clausola `on ArgumentError` quasi sempre non lo è.

---

Alcune librerie offrono una versione che non lancia affatto. Accanto a `int.parse`, Dart ha **`int.tryParse`**: la stessa conversione, ma restituisce `null` invece di lanciare quando il testo non è un numero.

```dart
print(int.parse('42'));     // 42
print(int.tryParse('42'));  // 42
print(int.tryParse('42x')); // null
```

Il risultato è un `int?`, quindi l'operatore `??` lo trasforma direttamente in un valore predefinito:

```dart
final port = int.tryParse(text) ?? 8080;
```

Quando l'errore è ordinario e ti serve solo un ripiego, questo è più corto e più chiaro di un blocco `try`. Tieni `int.parse` per i casi in cui un testo sbagliato è davvero un errore di cui qualcuno più in alto deve sentire parlare.

---

`firstWhere` restituisce il primo elemento che soddisfa un test. Quando nulla corrisponde non c'è nessun elemento da restituire, quindi lancia un `StateError`:

```dart
final words = ['a', 'fg'];
print(words.firstWhere((w) => w.length > 3)); // Bad state: No element
```

Come `int.tryParse`, anche la libreria offre una via d'uscita. Il parametro con nome `orElse` prende una funzione che produce il valore da usare quando nulla ha corrisposto:

```dart
print(words.firstWhere((w) => w.length > 3, orElse: () => 'none')); // none
```

La scelta è la stessa di prima: `orElse` quando «niente corrisponde» è un esito ordinario, la chiamata senza `orElse` quando significherebbe che i dati sono corrotti e qualcuno deve sentirlo dire.

---

Il `throw` e il `try` non devono per forza vivere nella stessa funzione. Una funzione che non può fare il suo lavoro lancia, e il chiamante che sa cosa farne cattura:

```dart
int ageFromText(String text) {
  final age = int.tryParse(text);
  if (age == null) throw FormatException('not a number');
  return age;
}
```

`ageFromText` non ha nulla da dire sul fatto che un'età sbagliata debba terminare il programma, mostrare un messaggio o essere saltata — è una decisione del chiamante, e il chiamante è dove appartiene il blocco `try`. Questa divisione è il motivo per cui lanciare vale più che restituire `-1`: l'errore arriva all'unico posto che può dargli una risposta.

Ricorda che il blocco `try` si ferma al primo errore, quindi anche le istruzioni dopo la chiamata che fallisce vengono saltate.

---

Dove sta il blocco `try` decide quanto lavoro un singolo errore distrugge. Attorno a un ciclo, il primo elemento sbagliato termina l'intero lotto; **dentro** il ciclo, solo quell'elemento va perso e il resto viene comunque elaborato:

```dart
for (final text in texts) {
  try {
    total += int.parse(text);
  } on FormatException {
    continue;
  }
}
```

Questa è la forma di ogni giorno per importare un file, leggere una lista di impostazioni o gestire una coda di messaggi: una riga danneggiata non deve buttare via quelle buone. La regola resta la stessa di prima — tieni il blocco `try` attorno all'istruzione che può fallire, e non più grande.

---

L'ultimo pezzo è lanciare un `Error` di proposito. Una funzione che documenta cosa accetta dovrebbe rifiutare tutto il resto con forza, e `ArgumentError` è l'oggetto fatto per questo:

```dart
int setVolume(int level) {
  if (level < 0 || level > 100) {
    throw ArgumentError('level must be between 0 and 100');
  }
  return level;
}
```

Il messaggio è raggiungibile come `e.message`, e `toString()` stampa `Invalid argument(s): ` seguito dal messaggio.

Questo non contraddice la regola di prima. Lanciare un `ArgumentError` è giusto, catturarne uno no: dice all'autore *del chiamante* che la chiamata stessa è sbagliata, e la correzione è un controllo prima della chiamata, non un gestore attorno ad essa.
