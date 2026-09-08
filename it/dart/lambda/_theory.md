Sai già come dichiarare una funzione con un nome, come `void sayHello() { ... }`. Dart ti permette anche di scrivere una funzione **senza nome**: una **funzione anonima**. Ha le stesse parti di una funzione con nome (parametri tra parentesi tonde e corpo tra parentesi graffe) ma niente tipo di ritorno e niente nome:

```dart
(String name) {
  print('Hello, $name!');
}
```

Poiché non ha nome, il modo usuale per usarla è memorizzarla in una variabile e poi chiamare la variabile come una funzione:

```dart
var sayHello = (String name) {
  print('Hello, $name!');
};

sayHello('Dart'); // Hello, Dart!
```

Nota il `;` dopo la parentesi graffa di chiusura: l'assegnazione è una normale istruzione.

---

Una funzione anonima può prendere parametri e restituire un valore con `return`, esattamente come una con nome. Il tipo di ritorno non viene scritto: Dart lo **deduce** dalle istruzioni `return` nel corpo.

```dart
var add = (int a, int b) {
  return a + b;
};

print(add(2, 3)); // 5
```

---

Quando il corpo è una singola espressione, una funzione anonima può usare la **sintassi freccia** `=>`, proprio come una funzione con nome. La freccia sostituisce le parentesi graffe e la parola chiave `return`:

```dart
var add = (int a, int b) => a + b;

print(add(2, 3)); // 5
```

Questa forma breve è di gran lunga il modo più comune per scrivere funzioni anonime in Dart.

---

Le funzioni sono valori, quindi hanno un tipo. Il tipo di una funzione si scrive come **tipo di ritorno**, poi la parola chiave `Function`, poi i **tipi dei parametri** tra parentesi tonde:

```dart
int Function(int, int) add = (int a, int b) => a + b;
bool Function(String) isEmpty = (String s) => s.isEmpty;
void Function() hello = () => print('Hello');
```

Quando la variabile è tipizzata in questo modo, i tipi dei parametri possono essere omessi dalla funzione anonima, perché Dart li deduce dal tipo dichiarato:

```dart
int Function(int, int) add = (a, b) => a + b;
```

Il tipo `Function` da solo accetta qualsiasi funzione, qualunque siano i suoi parametri e il suo tipo di ritorno, ma non dice a Dart nulla su come chiamarla.

---

Poiché un tipo funzione è un tipo normale, una funzione può prendere **un'altra funzione come parametro**. Nel corpo, il parametro viene chiamato come qualsiasi funzione:

```dart
int apply(int n, int Function(int) operation) {
  return operation(n);
}

print(apply(5, (n) => n * 2)); // 10
print(apply(5, (n) => n - 1)); // 4
```

Qui chi chiama decide cosa fa `apply` passando una funzione anonima come secondo argomento.

---

Molti metodi delle collezioni di Dart prendono una funzione come argomento, e le funzioni anonime sono il modo naturale per passargliela. Il più semplice è `forEach`, che chiama la funzione data una volta per ogni elemento di una lista:

```dart
var fruits = ['apple', 'kiwi'];

fruits.forEach((fruit) {
  print('I like $fruit');
});
// I like apple
// I like kiwi
```

Il tipo del parametro è dedotto dalla lista, quindi `fruit` è una `String` senza doverlo scrivere.

---

Altri due metodi molto comuni che prendono una funzione anonima sono `map` e `where`:

- `map` trasforma ogni elemento con la funzione e restituisce i nuovi valori
- `where` mantiene solo gli elementi per cui la funzione restituisce `true`

Entrambi restituiscono un `Iterable` pigro; chiama `toList()` per trasformare il risultato in una `List`:

```dart
var numbers = [1, 2, 3];

var squares = numbers.map((n) => n * n).toList();
print(squares); // [1, 4, 9]

var big = numbers.where((n) => n > 1).toList();
print(big); // [2, 3]
```

---

Poiché `map` e `where` restituiscono entrambi un `Iterable`, le loro chiamate possono essere **concatenate** una dopo l'altra. Ogni passo riceve il risultato del precedente, e `toList()` viene chiamata una sola volta alla fine:

```dart
var numbers = [1, 2, 3, 4, 5, 6];

var result = numbers.where((n) => n > 3).map((n) => n * 10).toList();
print(result); // [40, 50, 60]
```

---

`sort` riordina una lista sul posto. Per impostazione predefinita usa l'ordine naturale degli elementi, ma puoi passare una funzione anonima che **confronta due elementi** e restituisce un numero negativo, zero o un numero positivo. `compareTo` restituisce esattamente un numero del genere, quindi è il solito mattone di partenza:

```dart
var words = ['pear', 'fig', 'banana'];

words.sort((a, b) => a.length.compareTo(b.length));
print(words); // [fig, pear, banana]
```

Scambiare `a` e `b` nel confronto inverte l'ordine.

---

`reduce` combina tutti gli elementi di una lista in un unico valore. La sua funzione anonima prende due parametri: il valore **accumulato finora** e l'**elemento successivo**, e restituisce il nuovo valore accumulato. Il primo elemento viene usato come punto di partenza:

```dart
var numbers = [2, 3, 4];

var product = numbers.reduce((total, n) => total * n);
print(product); // 24
```

`reduce` genera un errore su una lista vuota, poiché non c'è un primo elemento da cui partire.

---

Una funzione può anche **restituire una funzione**. Il tipo di ritorno è allora un tipo funzione, e il corpo restituisce una funzione anonima:

```dart
int Function(int) makeAdder(int amount) {
  return (int n) => n + amount;
}

var addTen = makeAdder(10);
print(addTen(5)); // 15
```

Nota che la funzione restituita usa ancora `amount`, un parametro di `makeAdder`, anche dopo che `makeAdder` è terminata. Una funzione che ricorda le variabili attorno a sé in questo modo si chiama **closure**.

---

Una closure non si limita a leggere le variabili che cattura: può anche **modificarle**, e le modifiche vengono conservate tra le chiamate. Questo rende possibile mantenere uno stato privato senza una classe:

```dart
int Function() makeTimer() {
  var seconds = 0;
  return () {
    seconds += 10;
    return seconds;
  };
}

var timer = makeTimer();
print(timer()); // 10
print(timer()); // 20
```

Ogni chiamata a `makeTimer()` crea una variabile `seconds` completamente nuova, quindi due timer non condividono mai il loro contatore.
