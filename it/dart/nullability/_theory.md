Sai già come dichiarare una variabile con un tipo, come `String name = 'Ada';`. A volte, però, un valore è semplicemente **assente**: un utente senza soprannome, una ricerca che non trova nulla, un testo che non può essere convertito in numero. Dart rappresenta un valore assente con `null`.

Dalla versione 2.12 il linguaggio ha una **null safety** solida: un tipo normale come `String` non può **mai** contenere `null`. Tentare di assegnarlo è un errore di compilazione, così il programma non viene nemmeno eseguito:

```dart
String name = null; // error: a value of type 'Null' can't be assigned to 'String'
```

Per consentire un valore assente aggiungi un punto interrogativo `?` dopo il tipo. Una `String?` contiene una `String` oppure `null`, e stampare `null` mostra la parola `null`:

```dart
String? nickname = null;
print(nickname); // null

nickname = 'Ada';
print(nickname); // Ada
```

I tipi senza `?` sono detti **non nullable**, i tipi con `?` sono **nullable**.

---

Una variabile nullable dichiarata **senza un valore** inizia come `null`, quindi `= null` può essere omesso:

```dart
int? age;
print(age); // null
```

Una variabile non nullable non ha tale valore predefinito: Dart rifiuta di compilare qualunque codice che la legga prima che le sia stato assegnato un valore.

```dart
int count;
print(count); // error: 'count' must be assigned before it can be used
```

---

Chiamare un metodo o leggere una proprietà su `null` provocherebbe un arresto anomalo, quindi Dart non ti lascia farlo su un valore nullable con il consueto punto:

```dart
String? text;
print(text.length); // error: the property 'length' can't be unconditionally accessed
```

L'operatore di **accesso null-aware** `?.` risolve il problema: se il valore è `null` l'intera espressione è `null` e nient'altro viene valutato, altrimenti funziona come un normale `.`:

```dart
String? text = 'Dart';
print(text?.length); // 4

text = null;
print(text?.length); // null
```

Poiché il risultato può essere `null`, il suo tipo è nullable: `text?.length` è un `int?`, non un `int`.

---

Spesso un valore assente dovrebbe essere sostituito da un valore **predefinito**. L'operatore **if-null** `??` restituisce l'operando di sinistra quando non è `null`, e quello di destra altrimenti:

```dart
String? nickname;
print(nickname ?? 'anonymous'); // anonymous

nickname = 'Ada';
print(nickname ?? 'anonymous'); // Ada
```

`??` reagisce solo a `null`: una stringa vuota `''` o il numero `0` sono valori reali, quindi vengono mantenuti.

`??` si combina bene con `?.`, perché `?.` produce un risultato nullable:

```dart
String? text;
print(text?.length ?? 0); // 0
```

---

Il grande vantaggio della null safety è che la maggior parte degli errori legati a `null` viene trovata dal **compilatore**, non dai tuoi utenti. Le regole viste finora:

- un tipo non nullable (`String`, `int`, `List<int>`...) non può mai essere `null`
- un tipo nullable (`String?`, `int?`, `List<int>?`...) può esserlo, e inizia come `null` quando è dichiarato senza un valore
- `.` su un valore nullable non compila: usa `?.` oppure fornisci un valore predefinito con `??`

---

L'operatore di **assegnazione if-null** `??=` assegna un valore a una variabile **solo se** quella variabile è attualmente `null`; altrimenti la lascia invariata:

```dart
int? retries;
retries ??= 3;
print(retries); // 3

retries ??= 10;
print(retries); // 3, it already had a value
```

Funziona anche sulle voci di una mappa, che sono nullable perché una chiave potrebbe mancare:

```dart
var stock = {'apple': 4};
stock['pear'] ??= 1;  // added
stock['apple'] ??= 9; // ignored
print(stock); // {apple: 4, pear: 1}
```

---

A volte sei **tu** a sapere che un valore nullable non è `null` in un certo punto, anche se il compilatore non può saperlo. L'operatore di **asserzione non null** `!` trasforma una `String?` in una `String` promettendo che il valore è presente:

```dart
String? text = 'Dart';
String sure = text!;
print(sure.length); // 4
```

Fai attenzione: `!` sposta il controllo dal tempo di compilazione al tempo di esecuzione. Se il valore **è** `null`, il programma genera un errore e si ferma:

```dart
String? text;
print(text!.length); // Null check operator used on a null value
```

Usa `!` con parsimonia, e solo quando un `null` lì sarebbe comunque un bug.

---

Ricorda la differenza tra i tre operatori che hai visto usati su un valore nullable:

- `?.` restituisce `null` quando il valore è `null`, e non lancia mai un errore
- `??` sostituisce `null` con un valore predefinito
- `!` presuppone che il valore sia presente e **lancia un errore a tempo di esecuzione** quando non lo è

Nessuno di essi è un errore di compilazione: il compilatore si fida del tuo `!`, e solo il programma in esecuzione può scoprire che la promessa è stata tradita.

---

Controllare un valore nullable con `if` è più sicuro di `!`, e Dart ti ricompensa per questo. Dopo un controllo come `if (x != null)`, il compilatore sa che `x` non può essere `null` all'interno del blocco, quindi tratta `x` come non nullable lì. Questo si chiama **promozione di tipo**:

```dart
int twice(int? n) {
  if (n != null) {
    return n * 2; // here n is an int, no ! needed
  }
  return 0;
}
```

La promozione funziona anche dopo un ritorno anticipato:

```dart
int twice(int? n) {
  if (n == null) return 0;
  return n * 2; // n is an int from here on
}
```

La promozione si applica alle **variabili locali e ai parametri**, il cui valore non può cambiare alle tue spalle tra il controllo e l'uso.

---

La promozione di tipo **non** funziona su un **campo** di una classe che può essere modificato dall'esterno, perché tra il controllo e l'uso un altro pezzo di codice (un getter ridefinito in una sottoclasse, un altro metodo) potrebbe reimpostarlo a `null`:

```dart
class Box {
  int? value;

  int doubled() {
    if (value != null) {
      return value * 2; // error: 'value' can't be unconditionally accessed
    }
    return 0;
  }
}
```

La soluzione standard è copiare il campo in una **variabile locale**, che invece viene promossa:

```dart
int doubled() {
  final v = value;
  if (v != null) {
    return v * 2;
  }
  return 0;
}
```

---

Un campo non nullable deve di norma ricevere un valore nel costruttore. Quando il valore è noto solo **più tardi** (dopo aver letto un file, aperto una connessione...), puoi marcare il campo `late`: il compilatore accetta l'inizializzatore mancante e si fida che tu assegnerai il campo prima di leggerlo.

```dart
class Connection {
  late String host;

  void open() {
    host = 'example.com';
  }
}
```

Leggere un campo `late` a cui non è ancora stato assegnato un valore lancia un `LateInitializationError` a tempo di esecuzione. Come `!`, `late` scambia una garanzia a tempo di compilazione con un controllo a tempo di esecuzione, quindi è una promessa che devi mantenere.

`late` può anche essere combinato con un inizializzatore, che viene eseguito **lazily**, la prima volta che la variabile viene letta:

```dart
late String report = buildReport(); // buildReport() runs only when report is used
```

---

La nullability condiziona il modo in cui dichiari i **parametri con nome**. Un parametro con nome con un tipo nullable è opzionale: quando chi lo chiama lo omette, è semplicemente `null`.

```dart
String label({String? title}) => title ?? 'untitled';

print(label());               // untitled
print(label(title: 'Notes')); // Notes
```

Un parametro con nome con un tipo non nullable e senza valore predefinito non avrebbe alcun valore quando viene omesso, quindi Dart richiede di marcarlo `required`; chi chiama deve quindi passarlo sempre:

```dart
String label({required String name, String? title}) { ... }

label(name: 'Ada');               // ok
label(name: 'Ada', title: 'Dr.'); // ok
label(title: 'Dr.');              // error: the named parameter 'name' is required
```

---

La nullability si applica anche agli **elementi** di una collezione. Una `List<int>` non contiene mai `null`, mentre una `List<int?>` può farlo:

```dart
List<int?> scores = [7, null, 9];
```

Nota la differenza con `List<int>?`, che è una lista che può essere essa stessa assente ma, quando è presente, contiene solo numeri reali.

Per liberarti degli elementi `null`, `nonNulls` restituisce un `Iterable` con soli i valori presenti, tipizzato senza `?`:

```dart
var present = scores.nonNulls.toList(); // List<int>
print(present); // [7, 9]
```

`whereType<int>()` fa la stessa cosa e funziona anche quando la lista mescola più tipi.

---

Molte funzioni delle librerie usano `null` per segnalare che qualcosa **non ha potuto essere fatto**. Convertire una stringa in un numero è l'esempio classico: `int.parse` lancia una `FormatException` quando il testo non è un numero, mentre `int.tryParse` restituisce `null` e ti lascia decidere cosa fare:

```dart
print(int.tryParse('42'));  // 42
print(int.tryParse('4x2')); // null
print(int.tryParse(''));    // null
```

Il tipo di ritorno di `int.tryParse` è `int?`, quindi tutto ciò che hai imparato si applica: `??` per un valore predefinito, `?.` per concatenare, e un controllo `if` per promuovere. `double.tryParse` funziona allo stesso modo.

---

Altri due operatori hanno una variante null-aware.

La **cascata null-aware** `?..` esegue una catena di operazioni a cascata solo quando l'oggetto non è `null`, e le salta tutte altrimenti:

```dart
List<int>? numbers;
numbers?..add(1)..add(2); // nothing happens, numbers is still null
```

Lo **spread null-aware** `...?` inserisce gli elementi di una collezione nullable in un letterale, senza aggiungere nulla quando la collezione è `null`:

```dart
List<int>? extra;
print([0, ...?extra]); // [0]

extra = [1, 2];
print([0, ...?extra]); // [0, 1, 2]
```

Senza il `?`, `...extra` su una `List<int>?` sarebbe un errore di compilazione.

---

I dati reali sono pieni di lacune: un campo di un modulo lasciato vuoto, una colonna mancante in un file, una stringa che non è proprio un numero. Gli strumenti di questo capitolo si combinano naturalmente per gestirli: `nonNulls` per scartare gli elementi mancanti, `int.tryParse` per convertire in sicurezza, `??` o un controllo `if` per gestire ciò che non ha potuto essere convertito.
