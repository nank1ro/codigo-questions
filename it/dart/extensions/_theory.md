Sai già come aggiungere metodi a una classe scritta da te. Ma che dire di `String`, `int` o `List`, il cui codice vive nel Dart SDK? Non puoi modificarle, eppure spesso desideri che abbiano un metodo in più.

Un'**estensione** risolve il problema: aggiunge nuovi membri a un tipo **esistente**, senza toccarne il codice sorgente e senza creare una sottoclasse. La sintassi è:

```dart
extension ExtensionName on Type {
  // new methods and getters
}
```

All'interno dell'estensione, `this` si riferisce al valore su cui il membro viene chiamato. Una volta dichiarata l'estensione, i suoi membri vengono chiamati esattamente come i membri del tipo stesso:

```dart
extension Greeting on String {
  String greet() => 'Hello, $this!';
}

void main() {
  var name = 'Ada';
  print(name.greet()); // Hello, Ada!
}
```

Le estensioni vengono dichiarate al **livello principale** di un file, accanto a classi e funzioni, mai dentro `main`.

---

Le estensioni funzionano con qualsiasi tipo, numeri inclusi. Questa estensione aggiunge a ogni `int` un metodo che lo raddoppia:

```dart
extension Doubling on int {
  int doubled() => this * 2;
}
```

Poiché l'estensione si applica al **tipo**, puoi chiamare il metodo su una variabile o direttamente su un **letterale**. I letterali negativi richiedono le parentesi, altrimenti il punto viene letto prima del segno meno:

```dart
var n = 21;
print(n.doubled());    // 42
print(4.doubled());    // 8
print((-3).doubled()); // -6
```

---

Un'estensione può anche dichiarare **getter**, che si leggono come proprietà, senza parentesi. All'interno di un'estensione puoi chiamare direttamente i membri del tipo: `this.` è facoltativo, esattamente come all'interno di una classe.

```dart
extension Sizes on String {
  bool get isLong => length > 10;      // same as this.length
  String get firstChar => this[0];
}

void main() {
  print('Dart'.isLong);           // false
  print('extension'.firstChar);   // e
}
```

Scegli un getter quando il membro si limita a **leggere** un valore e non accetta parametri; scegli un metodo quando esegue un lavoro o ha bisogno di argomenti.

---

Il tipo dopo `on` può essere un tipo **parametrizzato** come `List<int>`. L'estensione si applica allora solo alle liste di quel tipo di elemento: `[1, 2].total()` funziona, `['a', 'b'].total()` non compila.

```dart
extension Totals on List<int> {
  int total() {
    var sum = 0;
    for (final n in this) {
      sum += n;
    }
    return sum;
  }
}
```

All'interno dell'estensione, `this` è la lista, quindi puoi scorrerla con un ciclo, indicizzarla o chiamare `length` come al solito.

---

Un'estensione su `List<int>` non può essere usata su una `List<String>`. Per scrivere un'estensione che funziona con **qualsiasi** tipo di elemento, dai all'estensione un **parametro di tipo**, scritto tra parentesi angolari dopo il nome, e usalo nel tipo dopo `on`:

```dart
extension Firsts<T> on List<T> {
  T get firstOrLast => length > 1 ? this[0] : this[length - 1];
}
```

`T` è un segnaposto per "qualunque sia il tipo dell'elemento": su una `List<int>` diventa `int`, su una `List<String>` diventa `String`, così il getter qui sopra restituisce un `int` oppure una `String` di conseguenza. Il compilatore riempie `T` per te a ogni chiamata.

```dart
print([7, 8, 9].firstOrLast); // 7
print(['a', 'b'].firstOrLast); // a
```

---

Un'estensione su `String` non può essere chiamata su una `String?`: il valore potrebbe essere `null`, e il compilatore rifiuta la chiamata. Se dichiari invece l'estensione sul tipo **nullable**, il metodo può essere chiamato direttamente su una `String?`, e al suo interno `this` ha tipo `String?`, quindi devi gestire tu il caso `null`, per esempio con `??`:

```dart
extension Defaults on int? {
  int orZero() => this ?? 0;
}

void main() {
  int? count = null;
  print(count.orZero()); // 0
  print(5.orZero());     // 5
}
```

Un `int` non nullable può essere passato dove è atteso un `int?`, quindi l'estensione funziona su entrambi.

---

Un'estensione può aggiungere metodi, getter, setter e operatori, ma **non può aggiungere campi di istanza**. Un valore `int` ha un layout fisso in memoria, e un'estensione è solo un insieme di funzioni che il compilatore ti lascia chiamare con la sintassi del punto: non c'è posto dove memorizzare dati extra per ogni valore.

```dart
extension Counter on int {
  int count = 0; // error: extensions can't declare instance fields
}
```

Getter e setter in un'estensione possono solo calcolare valori da `this` o inoltrare a membri esistenti: non possono ricordare nulla tra una chiamata e l'altra.

---

Un'estensione può dichiarare membri **static**. Come in una classe, appartengono all'estensione stessa, non a un valore, e vi si accede attraverso il **nome dell'estensione**, non attraverso il tipo che estende:

```dart
extension Temperatures on double {
  static const double boiling = 100.0;

  static bool isBoiling(double celsius) => celsius >= boiling;
}

void main() {
  print(Temperatures.boiling);         // 100.0
  print(Temperatures.isBoiling(37.5)); // false
  print(double.boiling);               // error: 'boiling' isn't defined for 'double'
}
```

I membri statici sono un posto comodo per costanti e funzioni di supporto legate al tipo esteso.

---

Le estensioni non servono solo per i tipi dell'SDK: puoi estendere anche le **tue classi**. È utile quando la classe proviene da un pacchetto che non controlli, o quando vuoi tenere la classe piccola e aggiungere helper opzionali accanto al codice che li usa.

```dart
class Circle {
  final double radius;
  Circle(this.radius);
}

extension CircleMath on Circle {
  double get diameter => radius * 2;
}

void main() {
  print(Circle(3).diameter); // 6.0
}
```

L'estensione vede i campi e i metodi pubblici della classe, esattamente come codice scritto fuori dalla classe.

---

Dart consente a un tipo di definire cosa significano operatori come `+`, `*` o `==` per i suoi valori, usando un metodo il cui nome è la parola chiave `operator` seguita dal simbolo. Il lato destro dell'operatore è il parametro del metodo:

```dart
extension Scaling on List<int> {
  List<int> operator *(int factor) => map((n) => n * factor).toList();
}

void main() {
  print([1, 2, 3] * 10); // [10, 20, 30]
}
```

Poiché le estensioni possono dichiarare operatori, puoi dare a un tipo esistente un operatore che non ha già. `String` ha `+` e `*`, ma non `-`, quindi un'estensione può definire cosa significa `'hello world' - 'o'`.

---

Cosa succede se un'estensione dichiara un membro che il tipo ha **già**? Vince sempre il membro del tipo: i membri dell'estensione vengono considerati solo quando il tipo stesso non ha un membro con quel nome. Il membro dell'estensione viene ignorato in silenzio, non c'è nessun errore e nessun override.

```dart
extension Shorter on String {
  int get length => 0;
}

void main() {
  print('four'.length); // 4, String's own length is used
}
```

Quindi un'estensione può aggiungere membri e colmare le lacune, ma non può mai **cambiare** il comportamento dei membri esistenti.

---

Il nome di un'estensione è facoltativo. Un'estensione **senza nome** funziona allo stesso modo, ma è visibile solo nel file che la dichiara:

```dart
extension on int {
  bool get isTriple => this % 3 == 0;
}
```

Un **nome** conta appena due estensioni offrono lo stesso membro sullo stesso tipo: la chiamata diventa **ambigua** e non compila. Il nome ti permette di risolvere il conflitto in due modi. Quando le estensioni provengono da file diversi, puoi fare `show` o `hide` di una di esse nell'import:

```dart
import 'package:loud/loud.dart';
import 'package:quiet/quiet.dart' hide Quiet;
```

Oppure, ovunque, puoi applicare l'estensione **esplicitamente**, avvolgendo il valore nel nome dell'estensione come se fosse un costruttore:

```dart
print(Loud('hi').describe());
```

Le estensioni senza nome non possono essere nascoste né applicate esplicitamente, quindi preferisci le estensioni con nome nel codice che altri importeranno.

---

Un'estensione generica può accettare **funzioni** come parametri, esattamente come fanno `where` e `map`. Il tipo della funzione è scritto con il tipo dell'elemento `T`, così la callback riceve elementi del tipo giusto:

```dart
extension Checks<T> on List<T> {
  bool all(bool Function(T) test) {
    for (final item in this) {
      if (!test(item)) return false;
    }
    return true;
  }
}

void main() {
  print([2, 4, 6].all((n) => n.isEven)); // true
}
```
