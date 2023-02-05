Le variabili sono contenitori per salvare valori.
Ogni variable in Dart è un oggetto (`Object`).
Per creare una variabile, dobbiamo darle un __nome__ tenendo in considerazione il fatto che non deve contenere spazi.
Dai un'occhiata a quanto segue:

```dart
int numero = 1;
```

Questa dichiarazione dichiara una variable chiamata `numero` di tipo `int`.
Poi imposta il valore della variabile al numero `1`.
La parte della dichiarazione `int` è conosciuta come __type annotation__ (tipo di annotazione), ed indica a Dart in modo esplicito il tipo della variabile.

---

Nell'esempio precedente abbiamo visto la creazione di una variabile:

```dart
int numero = 1;
```

Non farti ingannare dal simbolo `=`.
Non è il simbolo di uguaglianza come in matematica, bensì è conosciuto come __operatore di assegnazione__ in quanto assegna un valore alla variabile.
Il segno di uguaglianza invece è il seguente `==`.

---

Se vuoi cambiare il valore di una variable, è sufficiente assegnarle un valore diverso dello stesso tipo:

```dart
int numero = 1;
numero = 2;
```

---

Il tipo `int` permettere di salvare numeri interi.
Per salvarare numeri decimali invece possiamo usare il tipo `double`:

```dart
double pi = 3.14159;
```

Questo esempio è simile al precendente. Questa volta però la variable è di tipo `double`, un tipo che permette di salvare numeri decimali con un'alta precisione.

---

Dart è un linguaggio __type-safe__ (sicurezza rispetto ai tipi).
Questo significa che quando assegni ad una variabile un tipo, non lo potrai piú modificare dopo. Ecco un esempio:

```dart
int numeroIntero = 1;
numeroIntero = 3.14159; // Errore
```

`3.14159` è di tipo `double`, ma hai già definito `numeroIntero` col tipo `int`.

Ovviamente, ogni tanto potrebbe essere utile assegnare tipo correlati alla stessa variabile. Per esempio potresti volere una variabile `numero` che accetta sia numeri `int`eri che `double`, come qui:
```dart
num numero;
numero = 1; // OK
numero = 3.14159; // OK
numero = '10'; // Errore
```

Sia `int` che `double` estendono `num`, quindi entrambi i tipi sono accettati.
Invece se proviamo ad assegnare una `String`a il compilatore ci restituisce un errore.

---

Volendo, se ti piace vivere rischiando, possiamo ignorare completamente la __type-safety__ del linguaggio usando il tipo `dynamic`.
Questo ti permette di assegnare qualsiasi tipo di valore alla variabile.

```dart
dynamic numero;
numero = 1; // OK
numero = 3.14159; // OK
numero = '10'; // OK
```

Questo approccio è fortemente sconsigliato in quanto gli errori non vengono piú intercettati dall'_analyzer_ del codice, ma solo _runtime_ (quando il programma è in esecuzione).

---

Dart supporta la __type inference__ (inferenza del tipo).
Non è necessario indicare il tipo di una variabile in quanto Dart riesce ad inferirne il tipo.
La parola chiave `var` indica a Dart di usare il tipo piú appropriato.

```dart
var numero = 5;
```

Non è necessario dire a Dart che il numero `5` è di tipo `int`.
Dart inferisce il tipo e rende `numero` di tipo `int`.

---

Dart supporta due tipi diversi di "_variabili_" il cui valore non cambia mai. Vengono dichiarate con le parole chiave `const` e `final`.
Iniziamo vedendo che cosa si intende per `const`.

## const (costanti)

Le variabili il cui valore valore puoi modificare sono conosciute come __dato mutabile__. I dati mutabili vengono spesso usati smisuratamente e possono presentare dei problemi. È facile perdere traccia di tutti i punti nel codice che possono modificare il valore di una variabile.

Per questa ragione, dovresti usare le constanti invece delle variabili quando possibile. Questi variabili che non possono cambiare valore vengono anche chiamate __dato immutabile__.

Per creare una constante in Dart usiamo la parola chiave `const`:

```dart
const numero = 5;
```

Esattamente come `var`, Dart con la __type inference__ determina che `numero` è di tipo `int`.

---

Quando hai dichiarato una variabile costante, non puoi modificarne più il valore. Per esempio:

```dart
const numero = 2;
numero = 3; // Errore
```

Questo codice produce l'errore:
> Constant variables can't be assigned a value.

Ovvero non è possibile modificare il valore di una variabile costante.

---

Spesso ti troverai nella situazione di voler usare una costante ma non conosci il valore a tempo di compilazione. Conoscerai il valore solo dopo che il programma ha iniziato la sua esecuzione.
Questo tipo di costante è conosciuta come __runtime constant__ (costante a tempo di esecuzione).

In Dart `const` viene usato solo per __compile-time constants__ (costanti a tempo di compilazione) per valori che possono essere determinati dal compilatore prima dell'esecuzione del programma.

Se non puoi creare una variabile costante in quanto non ne conosci il valore a tempo di compilazione, allora devi usare la parole chiave `final` per rendere la variabile una __runtime constant__.

Ci sono molte ragioni per cui non puoi conoscere il valore di una variabile prima di eseguire il programma. Per esempio, dovresti dover ottenere il valore dal server, oppure chiederlo all'utente.

---

Ecco un esempio di un valore ottenibile solo in tempo di esecuzione:

```dart
final ora = DateTime.now().hour;
```

`DateTime.now()` è una funziona che permette di ottenere la data e l'ora corrente di quando il codice viene eseguito.
Con il campo `hour` accediamo al numero di ore che sono passate dall'inizio della giornata.

Dato che il valore di `ora` è differente in base al momento in cui il codice viene eseguito, questo può essere definito come valore _runtime_.

Se provi a modificare il valore di una variabile `final` ottieni un errore.
