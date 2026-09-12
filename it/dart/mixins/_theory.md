Una classe può fare `extend` di una sola superclasse, ma molto spesso lo stesso comportamento serve a classi che non hanno nulla altro in comune. Un **mixin** è una fetta riutilizzabile di comportamento che un numero qualsiasi di classi può adottare.

Lo dichiari con la parola chiave **`mixin`**, e una classe lo adotta con la parola chiave **`with`**:

```dart
mixin Swimmer {
  String swim() => 'swimming';
}

class Fish with Swimmer {}

void main() {
  print(Fish().swim()); // swimming
}
```

`Fish` non dichiara membri propri, eppure ogni `Fish` ha `swim`, perché i membri del mixin diventano membri della classe. Un mixin può essere usato da quante classi vuoi, correlate o meno.

---

Il corpo di un mixin assomiglia al corpo di una classe: metodi, getter e campi, scritti esattamente allo stesso modo. La differenza sta in ciò che puoi fare con la dichiarazione stessa.

```dart
mixin Timestamped {
  String get stamp => '[log]';

  String format(String text) => '$stamp $text';
}

class Server with Timestamped {}
class Printer with Timestamped {}
```

Il nome di un mixin è anche un **tipo**, quindi `Server() is Timestamped` è `true` e una variabile può essere dichiarata come `Timestamped t = Server();`. Due classi non correlate condividono ora un'unica implementazione senza che alcuna delle due eredi dall'altra.

---

Un mixin non è limitato ai metodi: può dichiarare anche **campi**, e ogni oggetto di ogni classe che utilizza il mixin ne ottiene una copia propria.

```dart
mixin Counter {
  int count = 0;

  void increment() {
    count++;
  }
}

class Clicker with Counter {}

void main() {
  final a = Clicker();
  final b = Clicker();
  a.increment();
  a.increment();
  print(a.count); // 2
  print(b.count); // 0, b has its own count
}
```

Questo è ciò che rende un mixin più di un'interfaccia: porta con sé sia i dati sia il codice che li elabora.

---

Una dichiarazione `mixin` **non** è una classe. Esiste solo per essere mescolata in altre classi, quindi non ha un costruttore proprio e non può essere istanziata né estesa:

```dart
mixin Scored {
  int score = 0;
}

final s = Scored();            // error: mixins cannot be instantiated
class Team extends Scored {}   // error: mixins cannot be extended
class Team with Scored {}      // this is the only way to use it
```

Il nome funziona comunque come un tipo, quindi `Team() is Scored` e `Scored s = Team();` vanno entrambe bene. Un mixin non ha costruttore, quindi un campo non nullable deve essere inizializzato dove viene dichiarato (o marcato `late`), come `int score = 0;` qui sopra.

---

Un mixin può dichiarare un membro **senza corpo**. Tale membro è astratto: il mixin lo utilizza, e la classe che adotta il mixin deve fornirlo.

```dart
mixin Greeting {
  String get name;                       // no body: the class provides it

  String greet() => 'Hello, $name!';
}

class Person with Greeting {
  @override
  final String name;

  Person(this.name);
}

void main() {
  print(Person('Ada').greet()); // Hello, Ada!
}
```

Il mixin porta il comportamento, la classe porta i dati. Un campo nella classe, come `final String name;`, è sufficiente a soddisfare un getter astratto con lo stesso nome.

---

Mettendo insieme i pezzi, un programma che utilizza un mixin ha tre parti: la dichiarazione `mixin`, una o più classi che lo adottano `with`, e il codice che chiama il membro condiviso.

```dart
mixin Barker {
  String bark() => 'Woof!';
}

class Dog with Barker {}

void main() {
  print(Dog().bark()); // Woof!
}
```

Le dichiarazioni al livello principale possono essere scritte in qualsiasi ordine in Dart, ma leggere un file dall'alto in basso è più facile quando il mixin viene prima delle classi che lo utilizzano.

---

Una classe può utilizzare **più mixin contemporaneamente**, elencati dopo `with` e separati da virgole. Dart li applica **da sinistra a destra**, impilandone ciascuno sopra il precedente, quindi quando due mixin dichiarano lo stesso membro vince l'**ultimo** della lista:

```dart
mixin A {
  String who() => 'A';
}

mixin B {
  String who() => 'B';
}

class First with A, B {}
class Second with B, A {}

void main() {
  print(First().who());  // B, the last mixin in the list
  print(Second().who()); // A, the last mixin in the list
}
```

Questo impilamento si chiama **linearizzazione**: `with A, B` costruisce la catena `Object` → `A` → `B` → la classe stessa.

---

Poiché vince l'ultimo mixin, l'ordine della lista `with` fa parte del significato della classe, non un dettaglio di stile. Riordinarla cambia l'implementazione con cui l'oggetto finisce:

```dart
mixin Plain {
  String format(String text) => text;
}

mixin Starred {
  String format(String text) => '*$text*';
}

class Fancy with Plain, Starred {}  // format comes from Starred
class Simple with Starred, Plain {} // format comes from Plain
```

I membri che solo un mixin dichiara non sono mai in competizione: sono disponibili qualunque sia l'ordine. Leggi `with X, Y` come "parti da `X`, poi lascia che `Y` ne faccia l'override".

---

I mixin e `extends` lavorano insieme. Una classe può avere una superclasse **e** una lista di mixin, e i mixin vengono sempre applicati **sopra** la superclasse:

```dart
class Document {
  String header() => 'Document';
}

mixin Timestamped {
  String header() => 'Timestamped';
}

class Report extends Document with Timestamped {}
```

La catena qui è `Object` → `Document` → `Timestamped` → `Report`. Un membro viene cercato partendo dalla fine della catena, quindi `Report().header()` trova prima la versione di `Timestamped`. Dichiarare lo stesso membro nella superclasse e in un mixin è perfettamente legale: è così che un mixin sostituisce o avvolge il comportamento ereditato.

---

Il corpo della classe si trova proprio alla fine della catena, quindi un membro dichiarato nella classe fa **override** dello stesso membro proveniente da qualunque suo mixin. All'interno dell'override, **`super`** raggiunge la versione fornita dal mixin:

```dart
mixin Polite {
  String greet() => 'Hello';
}

class Host with Polite {
  @override
  String greet() => '${super.greet()}, welcome!';
}

class Guest with Polite {}

void main() {
  print(Host().greet());  // Hello, welcome!
  print(Guest().greet()); // Hello
}
```

Il mixin stesso rimane intatto: `Guest` ottiene comunque il `greet` originale. `super.greet()` è ciò che permette a `Host` di costruire sul comportamento condiviso invece di copiarlo.

---

Alcuni comportamenti hanno senso solo sopra una classe particolare, e hanno bisogno dei membri di quella classe per fare il loro lavoro. La clausola **`on`** dichiara il requisito:

```dart
class Animal {
  String get name => 'animal';
}

mixin Noisy on Animal {
  String shout() => '${name.toUpperCase()}!';
}

class Dog extends Animal with Noisy {
  @override
  String get name => 'dog';
}

void main() {
  print(Dog().shout()); // DOG!
}
```

`on Animal` fa due cose: permette al mixin di usare i membri di `Animal`, come `name` qui sopra, e limita chi può usare il mixin. `class Rock with Noisy {}` è un errore di compilazione, perché `Rock` non è un `Animal`.

---

Un mixin con una clausola `on` legge i membri della sua superclasse come se fossero suoi, ed è questo che lo rende un buon posto per un comportamento che decora un tipo esistente:

```dart
class Shape {
  String get kind => 'shape';
}

mixin Printable on Shape {
  void show() {
    print('a $kind');
  }
}

class Square extends Shape with Printable {
  @override
  String get kind => 'square';
}
```

`Square` fa override di `kind`, e `show` raccoglie l'override automaticamente: il mixin chiama sempre il membro sull'oggetto reale.

---

Una volta che un mixin ha una clausola `on`, può fare **override** di un membro di quel tipo e chiamare **`super`** per raggiungere la versione sottostante nella catena:

```dart
class Logger {
  String log(String message) => message;
}

mixin Timestamped on Logger {
  @override
  String log(String message) => '[12:00] ${super.log(message)}';
}

class AppLogger extends Logger with Timestamped {}

void main() {
  print(AppLogger().log('started')); // [12:00] started
}
```

`super.log` non è il `log` del mixin stesso, è quello che sta sotto di esso, quindi non c'è ricorsione infinita. Impila più mixin di questo tipo con `with A, B` e ciascuno avvolge il precedente: la chiamata entra prima nell'**ultimo** mixin e scende fino alla superclasse.

---

Una dichiarazione `mixin` non può essere istanziata né estesa, e una semplice `class` non può essere usata dopo `with`. Quando ti serve una dichiarazione che funzioni in **entrambi** i modi, scrivi **`mixin class`**:

```dart
mixin class Serializable {
  String toText() => 'data';
}

final s = Serializable();            // works: it is a class
class Record extends Serializable {} // works: it is a class
class Row with Serializable {}       // works: it is a mixin
```

Una `mixin class` paga quella flessibilità con due restrizioni: deve estendere `Object`, quindi non può avere una clausola `extends` propria, e non deve dichiarare un costruttore, perché un mixin non ne esegue mai uno.

---

I mixin, l'ereditarietà e le interfacce risolvono tre problemi diversi:

- **`extends`** dà a una classe una superclasse, per una relazione "è una specie di". C'è un solo posto, quindi dovrebbe andare alla relazione più forte.
- **`with`** aggiunge un comportamento di cui molte classi non correlate hanno bisogno. Non c'è limite, e l'implementazione è condivisa, non copiata.
- **`implements`** promette un insieme di membri ma non porta **nessuna** implementazione: ogni classe deve scrivere il corpo da sé.

Un segnale che ti serve un mixin è un metodo che altrimenti copieresti in classi che non hanno un genitore comune naturale, come `Duck`, `Plane` e `Kite` che hanno tutti bisogno dello stesso `fly`.

---

I mixin impilati sono il modo in cui piccole regole indipendenti vengono combinate in una sola classe. Ogni mixin fa override dello stesso membro, fa la sua parte e chiama `super` per passare il lavoro avanti. Poiché la chiamata entra prima nell'**ultimo** mixin, l'ordine della lista `with` decide quale regola viene eseguita prima di quale:

```dart
class Account {
  int balance = 0;

  void deposit(int amount) {
    balance += amount;
  }
}

mixin Doubled on Account {
  @override
  void deposit(int amount) {
    super.deposit(amount * 2);
  }
}
```

`class A extends Account with Doubled {}` raddoppia ogni deposito. Aggiungi un secondo mixin dopo `Doubled` ed esso riceve il deposito per primo, prima che `Doubled` lo veda.
