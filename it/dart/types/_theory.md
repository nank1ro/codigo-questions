I tipi ti permettono di categorizzare tutti i differenti tipi di dati che usi nel tuo codice.
In Dart, un __type__ (tipo) è un modo per dire al compilatore come userai un determinato dato.
Ecco un esempio di tipi che Dart supporta:
- int
- String
- double
- dynamic
- num

Dart supporta molti altri tipi. Questi elencati sono i principali che userai.

---

Va bene se definisci esplicitamente il tipo di una variabile, per esempio:
```dart
int numeroIntero = 2;
double numeroDecimale = 3.14;
```

---

Anche le variabili con il tipo esplicito possono essere costanti, basta aggiungere la parola chiave `const` o `final` prima del tipo:
```dart
const int numeroIntero = 2;
final double numeroDecimale = 3.14;
```

> Nota: Un dato mutabile ti permette di cambiarlo quando vuoi in modo semplice. Tuttavia, molti programmatori esperti apprezzano i benefici del dato immutabile. Quando un valore è immutabile, puoi fidarti che nessuno potrà cambiarne il valore dopo che lo hai creato. Limitare il tuo dato in questo modo previeni molti bug difficili da individuare e rende il programma più semplice da ragionare e testare.

---

Per quanto sia possibile annotare il tipo di una variabile, ciò è ridondante. Sai bene che `10` è di tipo `int` e che `3.14` è di tipo `double`.
Lo stesso è in grado di inferirlo il compilatore Dart grazie alla __type inference__.
Non tutti i linguaggi di programmazione hanno la _type inference_, e questo rende Dart un linguaggio di programmazione davvero potente.

Puoi semplicemente rimuovere il tipo dalle variabili, per esempio:
```dart
const numeroIntero = 2;
final numeroDecimale = 3.14;
```

Quando il tipo di una variabile non è annotato esplicitamente, Dart proverà ad inferirne il tipo.

---

Esiste un modo programmatico per controllare il tipo di una variabile, ovvero con la parola chiave `is`:
```dart
final numero = 3.14;
print(numero is int); // false
print(numero is double); // true
```

Come puoi vedere Dart ha assegnato il tipo `double` alla variable `numero`.

---

La parola chiave `is` ti permette di verificare se una variabile è del tipo che definisci.
Ma puoi anche verificare se una variabile non è del tipo definito con la parola chiave `is!`
```dart
final numero = 3.14;
print(numero is! int); // true
```

---

Un'altra opzione che hai per vedere il tipo di una variabile _runtime_ è quella di usare la proprietà `runtimeType` che è disponibile a tutti i tipi.
```dart
final numero = 3.14;
print(numero.runtimeType); // double
```

---

A volte ti troverai nella situazione di avere un tipo, ma doverlo convertire in un altro.
Potresti essere tentato dal fare:

```dart
var intero = 5;
var decimale = 3.14;
intero = decimale;
```

Ma Dart si lamenterà e ti restituirá l'errore:
> Error: A value of type 'double' can't be assigned to a variable of type 'int'.

Alcuni linguaggi di programmazione non sono cosí restrittivi e silentemente effettueranno la conversione. L'esperienza dimostra che questo tipo di conversione implicita silente è una fonte frequente di bug e problemi di performance. Dart ha disabilitato questa funzionalità per evitare questi problemi.

Ricorda, i computer fanno affidamento sui programmatori per capire cosa fare. In Dart questo include l'essere espliciti sul tipo di conversione.

Invece di aspettarti una conversione implicita da Dart, devi dire in modo esplicito che vuoi che Dart ti converta il tipo. Ecco come convertire un numero `double` in uno `int`:
```dart
var intero = decimale.toInt();
```

L'assegnazione dice a Dart, in modo inequivocabile, che vuoi convertire dal tipo originale `double` al nuovo tipo `double`.

> NOTA: In questo caso, assegnare un valore decimale ad un intero fa perdere la precisione. La variabile `intero` si ritrova il valore __3__ invece di __3.14__. Questo è il motivo per cui è importante essere espliciti. Dart vuole essere sicuro di quello che stai facendo e ti mette al corrente che perderai delle informazioni effettuando la conversione.

---

Fino ad adesso abbiamo visto gli operatori usati indipendentemente su numeri interi o decimali.
Cosa succede se hai un numero intero e lo devi moltiplicare con un numero decimale?
Vediamo un esempio:
```dart
const raggio = 5;
const pi = 3.14;
const circonferenza = 2 * pi * raggio;
```

`raggio` è di tipo `int` mentre `pi` è di tipo `double`. Quale sarà il tipo di `circonferenza`?
Dart assegnerà il tipo `double` alla variabile `circonferenza`. Questa è la scelta più sicura in quanto se l'avesso reso di tipo `int` avrebbe potuto causare una perdita di precisione.

Se vuoi un `int` come risultato, devi effettuare la conversione in modo esplicito:
```dart
const circonferenza = (2 * pi * raggio).toInt();
```

Le parentesi tonde indicano a Dart di moltiplicare prima, e poi di predendere il risultato e convertirlo in un valore intero. Purtroppo all'analyzer questo codice non piacerà:
> Const variables must be initialized with a constant value.

Il problema è che il metodo `toInt` è un metodo eseguibili solo a runtime. Questo significa che la variabile `circonferenza` non può essere determinata a tempo di compilazione, quindi non è possibile che la variabile sia costante. Per risolvere sostituisci `const` con `final`:

```dart
final circonferenza = (2 * pi * raggio).toInt();
```

Ora `circonferenza` è una variabile __runtime constant__ di tipo `int`.

---

A volte potresti avere una variabile con un tipo generico, ma ti serve una funzionalità presente solo in un sottotipo. Se sei sicuro che il tipo della variabile è il sottotipo che ti serve, allora puoi usare la parola chiave `as` per modificarne il tipo. Questa prodecura è anche conosciuta come __type casting__, ecco un esempio:

```dart
num numero = 3;
```

Ipotizziamo di voler controllare se il numero è pari, e la funzionalità in questione è presente solo sul sotto tipo `int`.
```dart
print(numero.isEven);
```

Il codice qui sopra ti dovrebbe restituire un errore del tipo:
> The getter `isEven` isn't defined for the type 'num'.

Il tipo `num` è un tipo troppo generico per sapere se un numero è pari o dispari. Solo i numeri interi possono essere pari o dispari.
Il problema si presenta se `num` contiene un valore `double`, in quanto `num` include entrambi i tipi `double` e `int`. In questo caso, siamo sicuri che __3__ è un numero intero, quindi possiamo fare il casting a `int`

```dart
final intero = numero as int;
print(intero.isEven); // false
```

La parola chiave `as` fa si che il compilatore riconosce la variabile `intero` con il tipo `int`. Questo permette di usare la proprietà `isEven` che è presente sui numeri interi. Dato che il numero __3__ non è intero, il risultato è false.

Devi stare attendo quando fai casting. Se casti erroneamente il tipo otterrai un errore runtime:
```dart
num numero = 3;
final decimale = numero as double;
```

Questo farà crashare il programma con il seguente errore:
> CastError (type 'int' is not a subtype of type 'double' in type cast)

Il tipo runtime di `numero` è `int` e non `double`. In Dart non puoi effettuare il casting con tipi allo stesso livello, come `int` e `double`. Puoi effettuare il casting solo per sotto tipi.
