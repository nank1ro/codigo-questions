Un **metodo di ordine superiore** è un metodo che prende una funzione come argomento. Le collezioni di Dart ne offrono molti, e la funzione che passi è di solito una funzione anonima scritta con la sintassi freccia `(x) => ...`.

`map` è il più comune: chiama la funzione su ogni elemento e produce i risultati, uno per ogni elemento, lasciando intatta la collezione originale:

```dart
final numbers = [1, 2, 3];
print(numbers.map((n) => n * 2)); // (2, 4, 6)
print(numbers);                   // [1, 2, 3]
```

Nota le **parentesi tonde** nell'output. `map` non restituisce una `List`: restituisce un `Iterable`, una sequenza che puoi percorrere. Per ottenere una vera lista, chiama **`toList()`** su di essa:

```dart
final doubled = numbers.map((n) => n * 2).toList();
print(doubled); // [2, 4, 6]
```

Le parentesi quadre nell'output indicano che stai guardando una `List`, quelle tonde che stai guardando un semplice `Iterable`.

---

`where` prende una funzione che restituisce un `bool`, chiamata **predicato**, e mantiene solo gli elementi per cui risponde `true`. L'ordine degli elementi superati non cambia mai:

```dart
final numbers = [4, -2, 7, 0];
print(numbers.where((n) => n > 0).toList()); // [4, 7]
```

Come `map`, `where` restituisce un `Iterable` e non modifica mai la collezione originale, quindi anche in questo caso è `toList()` a trasformare il risultato in una `List`.

In altri linguaggi questo metodo si chiama `filter`; in Dart si chiama `where`.

---

La funzione data a `map` non deve restituire necessariamente lo stesso tipo degli elementi che riceve. Mappare una lista di stringhe alle loro lunghezze trasforma una `List<String>` in un `Iterable<int>`, che `toList()` rende poi una `List<int>`:

```dart
final words = ['fig', 'kiwi'];
print(words.map((w) => w.length).toList()); // [3, 4]
```

Il risultato ha sempre **esattamente lo stesso numero di elementi dell'originale**, nello stesso ordine: `map` trasforma gli elementi, non ne aggiunge né ne rimuove mai.

---

Alcuni metodi di ordine superiore rispondono a una domanda sulla collezione invece di costruirne una nuova. Prendono un predicato e restituiscono un `bool`:

- `any` è `true` quando **almeno un** elemento soddisfa il predicato
- `every` è `true` quando **tutti** gli elementi lo soddisfano

```dart
final numbers = [1, 2, 3];
print(numbers.any((n) => n > 2));   // true
print(numbers.every((n) => n > 2)); // false
```

Entrambi si fermano appena la risposta è certa: `any` al primo elemento che corrisponde, `every` al primo che non corrisponde.

Su una collezione vuota `any` è `false` e `every` è `true`: non c'è alcun elemento che dimostri il primo, e nessuno che rompa il secondo.

---

`map` e `where` sono **lazy** (pigri): chiamarli non esegue nulla. Restituiscono un `Iterable` che ricorda la sorgente e la funzione, e la funzione viene chiamata solo mentre qualcosa percorre il risultato, un elemento alla volta.

```dart
final numbers = [1, 2, 3];
final doubled = numbers.map((n) => n * 2); // nothing computed yet
print(doubled.first);                      // computes only 2
```

`toList()` è ciò che **materializza** la sequenza: la percorre dall'inizio alla fine e memorizza ogni risultato in una vera `List`.

La pigrizia ha due conseguenze che vale la pena ricordare. Un `Iterable` lazy viene ricalcolato ogni volta che lo iteri, quindi materializzarlo una volta con `toList()` è più conveniente quando ti servono i valori più di una volta. E continua a guardare la collezione originale, quindi modificare quella collezione cambia ciò che l'`Iterable` produce:

```dart
final numbers = [1, 2, 3];
final lazy = numbers.map((n) => n * 2);
final eager = numbers.map((n) => n * 2).toList();
numbers.add(4);
print(lazy.toList()); // [2, 4, 6, 8]
print(eager);         // [2, 4, 6]
```

---

`fold` combina un'intera collezione in un **singolo valore**. Prende due argomenti: il valore iniziale dell'**accumulatore**, e una funzione che riceve l'accumulatore costruito finora e l'elemento successivo, e restituisce il nuovo accumulatore:

```dart
final numbers = [1, 2, 3, 4];
final total = numbers.fold(0, (acc, n) => acc + n);
print(total); // 10
```

Qui `acc` parte da `0`, poi diventa `1`, `3`, `6` e infine `10`.

L'accumulatore non deve essere per forza un numero, né dello stesso tipo degli elementi: partendo da `''` e aggiungendo testo si costruisce una `String` a partire da una lista di qualsiasi cosa.

Un dettaglio da tenere a mente: Dart deduce il tipo dell'accumulatore dal valore iniziale **e** dal punto in cui il risultato viene usato. Dentro `print(...)` il tipo atteso è sconosciuto, quindi salva prima il risultato in una variabile (oppure scrivi `fold<int>(...)`), altrimenti il compilatore si lamenta che non può usare `+` sull'accumulatore.

---

`reduce` è il parente più snello di `fold`. Non prende alcun valore iniziale: il **primo elemento** è l'accumulatore di partenza, e la funzione viene eseguita per ogni elemento rimanente:

```dart
final numbers = [1, 2, 3, 4];
print(numbers.reduce((a, b) => a + b)); // 10
```

Poiché non c'è un valore iniziale, il risultato ha sempre lo **stesso tipo degli elementi**, e chiamare `reduce` su una collezione vuota lancia una `StateError`: non c'è un primo elemento da cui partire. `fold` non ha questo problema, ed è per questo che è la scelta predefinita più sicura.

`reduce` dà il meglio di sé quando cerchi un elemento tra molti, come il più grande:

```dart
print(numbers.reduce((a, b) => a > b ? a : b)); // 4
```

---

`firstWhere` restituisce il **primo** elemento che corrisponde a un predicato, invece di tutti:

```dart
final words = ['fig', 'kiwi', 'banana'];
print(words.firstWhere((w) => w.length > 3)); // kiwi
```

Quando nessun elemento corrisponde non c'è nulla da restituire, quindi `firstWhere` lancia una `StateError`. Per dare una risposta invece di un errore, passa l'argomento nominato **`orElse`**: una funzione senza parametri che produce il valore di riserva.

```dart
print(words.firstWhere((w) => w.length > 10, orElse: () => 'none')); // none
```

`orElse` è una funzione, non un valore semplice, quindi viene chiamata solo quando la ricerca fallisce. Scrivere `orElse: 'none'` non compila.

---

Quando la funzione che dai a `map` restituisce una collezione per ogni elemento, ottieni una sequenza di collezioni. **`expand`** fa lo stesso lavoro ma poi unisce tutte le collezioni in un'unica sequenza piatta:

```dart
final numbers = [1, 2];
print(numbers.map((n) => [n, -n]).toList());    // [[1, -1], [2, -2]]
print(numbers.expand((n) => [n, -n]).toList()); // [1, -1, 2, -2]
```

L'ordine è preservato: tutto ciò che è prodotto dal primo elemento viene prima, poi tutto ciò che è prodotto dal secondo, e così via.

Poiché la collezione restituita può avere qualsiasi dimensione, `expand` è anche il modo per produrre **più o meno** elementi di quanti ne avessi all'inizio: restituire una lista vuota per un elemento lo scarta semplicemente.

```dart
print(['a b', 'c'].expand((s) => s.split(' ')).toList()); // [a, b, c]
```

---

`take(n)` mantiene i **primi** `n` elementi e `skip(n)` li scarta. Nessuna delle due prende una funzione, ma entrambe restituiscono un `Iterable` lazy, quindi si collocano naturalmente tra gli altri metodi di ordine superiore:

```dart
final scores = [10, 20, 30, 40, 50];
print(scores.take(2).toList()); // [10, 20]
print(scores.skip(3).toList()); // [40, 50]
```

Chiedere più elementi di quanti ce ne siano non è un errore: ottieni semplicemente ciò che esiste, oppure un risultato vuoto.

`takeWhile` e `skipWhile` sono le versioni con un predicato. Prendono o scartano elementi dall'inizio **fintanto che** il predicato resta vero, e si fermano al primo elemento che lo fallisce, anche se quelli successivi potrebbero corrispondere di nuovo:

```dart
print(scores.takeWhile((s) => s < 35).toList()); // [10, 20, 30]
```

---

Dart non ha un metodo `sorted`. `sort` appartiene a `List`, riordina la lista **sul posto** e non restituisce nulla:

```dart
final numbers = [3, 1, 2];
numbers.sort();
print(numbers); // [1, 2, 3]
```

Poiché restituisce `void`, non puoi usare il risultato in alcun modo: `final sorted = numbers.sort();` produce un valore che il compilatore non ti permette di leggere. L'idioma per una **copia** ordinata è `toList()` seguito dalla cascade `..sort()`: `toList()` crea la copia, e `..` esegue `sort` su di essa restituendo comunque la copia stessa.

```dart
final numbers = [3, 1, 2];
final sorted = numbers.toList()..sort();
print(sorted);  // [1, 2, 3]
print(numbers); // [3, 1, 2], untouched
```

`sort` accetta anche un **comparatore**: una funzione di due elementi che restituisce un numero negativo quando il primo viene prima del secondo, `0` quando sono uguali, e un numero positivo negli altri casi. `compareTo` produce esattamente questo, quindi ordinare per qualsiasi chiave è una riga di codice:

```dart
final words = ['kiwi', 'fig', 'banana'];
print(words.toList()..sort((a, b) => a.length.compareTo(b.length)));
// [fig, kiwi, banana]
```

---

`fold` e `reduce` si somigliano, e scegliere tra loro si riduce a due domande: la collezione può essere vuota? E il risultato ha lo stesso tipo degli elementi?

```dart
final words = ['fig', 'kiwi'];
final joined = words.reduce((a, b) => '$a, $b'); // String from Strings
final letters = words.fold(0, (acc, w) => acc + w.length); // int from Strings
print(joined);  // fig, kiwi
print(letters); // 7
```

`reduce` può restituire solo un tipo elemento, perché parte da un elemento. `fold` parte da un valore che scegli tu, quindi l'accumulatore può essere un `int` che conta, una `String` che cresce, o perfino una `List` che si costruisce. E poiché quel valore iniziale esiste già, una collezione vuota è semplicemente la risposta che `fold` restituisce invariata, mentre `reduce` non ha nulla da restituire e lancia un'eccezione.

---

Ognuno di questi metodi restituisce un `Iterable`, e ogni `Iterable` ha di nuovo gli stessi metodi. È questo che permette di **incatenarli**: un'intera computazione si legge come una pipeline da sinistra a destra, con ogni passo che lavora su ciò che il precedente ha prodotto.

```dart
final words = ['kiwi', 'fig', 'banana', 'date'];
print(words.where((w) => w.length == 4).map((w) => w.toUpperCase()).toList());
// [KIWI, DATE]
```

Solo l'ultimo passo ha bisogno di `toList()`: chiamarla a metà costruirebbe una lista che nessuno conserva.

Il tipo cambia lungo la catena, e cambia anche ciò che la funzione successiva riceve: dopo `where` su una `List<String>` hai ancora stringhe, ma dopo `map((w) => w.length)` il passo successivo vede numeri.

Poiché ogni passo è lazy, l'ordine conta per il lavoro svolto, non solo per il risultato: filtrare prima con `where` significa che `map` viene chiamata su meno elementi.

---

Nulla in questi metodi è speciale: hanno semplicemente **una funzione come parametro**, e le tue funzioni possono fare lo stesso. Il tipo di un parametro funzione si scrive con il tipo di ritorno, poi `Function`, poi i tipi dei parametri tra parentesi:

```dart
List<int> applyAll(List<int> numbers, int Function(int) operation) {
  return numbers.map(operation).toList();
}
```

Chi chiama decide **cosa** succede, la funzione decide **su cosa**. Nota come `operation` viene passata direttamente a `map`: un valore funzione può essere passato avanti come qualsiasi altro valore.

L'argomento può essere una funzione anonima, oppure il **nome** di una funzione esistente, scritto senza parentesi. Aggiungere le parentesi la chiamerebbe invece di passarla:

```dart
int square(int n) => n * n;

print(applyAll([1, 2, 3], square));       // [1, 4, 9]
print(applyAll([1, 2, 3], (n) => n + 1)); // [2, 3, 4]
```

---

Una funzione può anche **restituire** una funzione. Il tipo di ritorno si scrive esattamente come il tipo di un parametro funzione, e il valore restituito è di solito una funzione anonima:

```dart
int Function(int) multiplier(int factor) {
  return (n) => n * factor;
}
```

`multiplier(3)` non moltiplica nulla: costruisce e restituisce una nuova funzione che moltiplica per `3`. Quella funzione viene poi memorizzata, chiamata, o passata a `map` come qualsiasi altra:

```dart
final triple = multiplier(3);
print(triple(5));                       // 15
print([1, 2, 3].map(triple).toList());  // [3, 6, 9]
```

La funzione restituita ricorda ancora `factor` dopo che `multiplier` è terminata. Una funzione che conserva le variabili dello scope in cui è stata creata si chiama **closure**, ed è ciò che rende possibili le fabbriche di funzioni come questa.

---

Messi insieme, questi metodi sostituiscono la maggior parte dei cicli scritti a mano. Una pipeline di solito si legge in tre fasi: **seleziona** gli elementi con `where`, **trasformali** con `map`, poi **combinali** con `fold`:

```dart
final prices = [12, 40, 7];
final cheapTotal = prices.where((p) => p < 20).fold(0, (acc, p) => acc + p);
print(cheapTotal); // 19
```

Poiché `fold` sceglie il proprio valore iniziale, può anche concludere una catena con un tipo che non c'entra nulla con gli elementi, come una `String` cresciuta un pezzo alla volta:

```dart
final words = ['fig', 'kiwi'];
final firstLetters = words.fold('', (acc, w) => acc + w[0]);
print(firstLetters); // fk
```

Ogni fase resta breve e dice cosa fa, ed è questa la vera ragione per preferirli a un ciclo che fa tutte e tre le cose insieme.
