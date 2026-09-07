Una **classe** è un modello per creare oggetti. In Dart, si definisce una classe con la parola chiave `class` seguita dal nome della classe e da una coppia di parentesi graffe:

```dart
class Animal {
  // fields and methods go here
}
```

Per convenzione, i nomi delle classi usano il **PascalCase** (ogni parola inizia con una lettera maiuscola).

---

Una classe può avere **variabili di istanza** (chiamate anche campi) che contengono dati per ogni oggetto. Si dichiarano all'interno del corpo della classe, assegnando a ciascuna un valore iniziale:

```dart
class Animal {
  String name = '';
  int age = 0;
}
```

Ogni oggetto creato da questa classe avrà i propri valori di `name` e `age`.

---

Un **costruttore** è un metodo speciale eseguito quando crei (istanzi) un oggetto da una classe. Il costruttore ha lo stesso nome della classe:

```dart
class Animal {
  String name;

  Animal(this.name);
}
```

Un parametro scritto come `this.name` memorizza il valore passato al costruttore direttamente nel campo `name` del nuovo oggetto. Un campo impostato in questo modo non richiede un valore iniziale.

Si crea un oggetto usando la parola chiave `new` (opzionale in Dart) oppure semplicemente il nome della classe:

```dart
var dog = Animal('Rex');
```

---

Il parametro `this.x` visto nell'esercizio precedente è una forma abbreviata. La forma estesa assegna ogni parametro al proprio campo all'interno del corpo del costruttore (`this.x` è il campo, `x` è il parametro):

```dart
class Point {
  int x = 0;
  int y = 0;

  Point(int x, int y) {
    this.x = x;
    this.y = y;
  }
}
```

La stessa classe può essere scritta come:

```dart
class Point {
  int x;
  int y;

  Point(this.x, this.y);
}
```

Questa forma più breve si chiama **parametri formali di inizializzazione**.

---

Un **metodo** è una funzione definita all'interno di una classe. I metodi descrivono il comportamento di un oggetto:

```dart
class Animal {
  String name;

  Animal(this.name);

  void speak() {
    print('$name makes a sound.');
  }
}
```

Si chiama un metodo su un oggetto usando la notazione col punto: `dog.speak()`.

---

`this` si riferisce all'**istanza corrente** della classe, cioè l'oggetto su cui è stato chiamato un metodo. All'interno di un metodo puoi usarlo per accedere ai campi dell'oggetto stesso:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double diameter() {
    return this.radius * 2;
  }
}
```

Qui `this.radius` legge il campo `radius` del cerchio su cui è stato chiamato `diameter()`. Quando non c'è un'altra variabile con lo stesso nome, `this.` può essere omesso: `radius * 2` funziona allo stesso modo.

---

Dart supporta i **costruttori con nome**, che permettono di definire modi aggiuntivi per creare un oggetto. I costruttori con nome si scrivono come `ClassName.constructorName`:

```dart
class Point {
  double x;
  double y;

  Point(this.x, this.y);

  Point.origin()
      : x = 0,
        y = 0;
}
```

La parte dopo i due punti è la **lista di inizializzazione**: assegna i campi prima che venga eseguito il corpo del costruttore. Puoi quindi creare un oggetto all'origine con: `var p = Point.origin();`

---

Un **getter** è un metodo speciale che legge un valore calcolato o privato e appare come un accesso a una proprietà. Si definisce con la parola chiave `get`:

```dart
class Circle {
  double radius;

  Circle(this.radius);

  double get area => 3.14159 * radius * radius;
}
```

Si accede a un getter come a un campo: `circle.area` (senza parentesi).

La freccia `=> expr` è una forma abbreviata per un corpo che restituisce solo un valore: `{ return expr; }`. Funziona sia per i getter sia per qualsiasi funzione o metodo:

```dart
double half(double n) => n / 2;
```

---

Un **setter** è un metodo speciale che permette di assegnare un valore eseguendo al contempo una logica di validazione. Si definisce con la parola chiave `set`:

```dart
class Temperature {
  double _celsius = 0;

  double get celsius => _celsius;

  set celsius(double value) {
    if (value < -273.15) throw ArgumentError('Too cold!');
    _celsius = value;
  }
}
```

Il nome del campo è spesso preceduto da `_` per contrassegnarlo come privato.

---

L'**ereditarietà** permette a una classe (la **sottoclasse**) di estendere un'altra classe (la **superclasse**) e riutilizzarne campi e metodi. Usa la parola chiave `extends`:

```dart
class Animal {
  String name = 'animal';

  void speak() {
    print('$name makes a sound.');
  }
}

class Dog extends Animal {
  void fetch() {
    print('$name fetches the ball.');
  }
}
```

`Dog` eredita `name` e `speak()` da `Animal` e aggiunge il proprio metodo `fetch()`. Una classe che non dichiara alcun costruttore ne riceve uno predefinito senza parametri, quindi puoi scrivere `var dog = Dog();` e poi chiamare sia `dog.speak()` sia `dog.fetch()`.

---

Quando il costruttore di una sottoclasse deve chiamare il costruttore della superclasse, usa la parola chiave `super` nella **lista di inizializzazione**:

```dart
class Vehicle {
  String brand;
  Vehicle(this.brand);
}

class Car extends Vehicle {
  int doors;
  Car(String brand, this.doors) : super(brand);
}
```

`super(brand)` inoltra l'argomento `brand` al costruttore di `Vehicle`.

---

L'**override dei metodi** permette a una sottoclasse di fornire una propria implementazione di un metodo già presente nella superclasse. Usa l'annotazione `@override`:

```dart
class Shape {
  double area() => 0;
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

L'annotazione `@override` comunica a Dart (e agli altri sviluppatori) che stai sostituendo intenzionalmente il metodo della superclasse.

---

Una **classe astratta** è una classe che non può essere istanziata direttamente. Viene usata come base che definisce un contratto — metodi che devono essere implementati dalle sottoclassi. Si contrassegnano i metodi astratti omettendone il corpo:

```dart
abstract class Shape {
  double area(); // abstract method — no body
}

class Circle extends Shape {
  double radius;
  Circle(this.radius);

  @override
  double area() => 3.14159 * radius * radius;
}
```

Provare a istanziare `Shape()` direttamente genera un errore.

---

I **membri statici** appartengono alla classe stessa piuttosto che a una particolare istanza. Si dichiarano con la parola chiave `static` e vi si accede direttamente dalla classe:

```dart
class MathHelper {
  static const double pi = 3.14159;

  static double circleArea(double r) => pi * r * r;
}

void main() {
  // access without creating an object:
  print(MathHelper.pi);
  print(MathHelper.circleArea(5));
}
```

I campi e i metodi statici sono condivisi da tutte le istanze.

---

Un **costruttore factory** usa la parola chiave `factory` e permette di controllare la creazione degli oggetti — ad esempio restituendo un'istanza memorizzata nella cache o un sottotipo:

```dart
class Logger {
  static final Logger _instance = Logger._internal();

  factory Logger() => _instance;

  Logger._internal();
}
```

Ogni chiamata a `Logger()` restituisce la stessa istanza (pattern singleton).
