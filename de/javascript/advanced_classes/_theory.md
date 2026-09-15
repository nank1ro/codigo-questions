Du weißt bereits, dass `extends` eine Klasse zur Kindklasse einer anderen macht. Was dieses Schlüsselwort dir wirklich gibt, ist **Vererbung**: Die Kindklasse bekommt jede Eigenschaft und Methode der Elternklasse gratis dazu und kann eigene darüberhinaus hinzufügen.

Das Stück, das Vererbung nützlich macht, ist **`super`**. Innerhalb des Konstruktors einer Kindklasse ruft `super(...)` den Eltern-Konstruktor auf, damit die Elternklasse den Teil des Objekts einrichten kann, der ihr gehört:
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
}
class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
}
```
Hier übergibt `super(name)` den `name` an `Animal`, das ihn speichert, und `Dog` muss sich nur noch um `breed` kümmern.

---

Eine Kindklasse muss nichts neu definieren, was die Elternklasse bereits bereitstellt. Auch Methoden werden vererbt, sodass eine Instanz der Kindklasse sie aufrufen kann, als wären es ihre eigenen:
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        return `${this.name} makes a sound`;
    }
}
class Dog extends Animal {}
console.log(new Dog("Max").speak());
// gibt Max makes a sound aus
```
Wenn eine Kindklasse ihren eigenen Konstruktor deklariert, ist der Aufruf von `super(...)` darin **verpflichtend**: Ohne ihn wird das Objekt nie initialisiert und JavaScript wirft einen `ReferenceError`. Eine Kindklasse ohne eigenen Konstruktor ist kein Problem, denn JavaScript schreibt einen, der jedes Argument an die Elternklasse weiterleitet.

---

Die Regel zu `super()` ist strenger als „Rufe es irgendwo auf". Im Konstruktor einer Kindklasse existiert das Wort `this` nicht, bevor `super()` gelaufen ist, denn der Eltern-Konstruktor ist es, der das Objekt erzeugt. `this` vor dieser Zeile zu benutzen, wirft einen Fehler:
```javascript
class Child extends Base {
    constructor() {
        this.x = 1; // ReferenceError
        super();
    }
}
```
`super(...)` sollte daher die **erste Anweisung** jedes Kind-Konstruktors sein, der `this` benutzt.

---

Wenn eine Kindklasse eine Methode definiert, die die Elternklasse bereits hat, gewinnt die Version der Kindklasse. Das nennt sich **Überschreiben**:
```javascript
class Animal {
    speak() {
        return "some sound";
    }
}
class Dog extends Animal {
    speak() {
        return "Woof";
    }
}
console.log(new Dog().speak());
// gibt Woof aus
```
Beim Überschreiben wird die Version der Elternklasse nicht gelöscht, sie wird nur verdeckt. Innerhalb der Methode der Kindklasse erreichst du sie weiterhin über `super.methodName(...)`, sodass du das Verhalten der Elternklasse erweitern kannst, statt es zu ersetzen:
```javascript
class Puppy extends Dog {
    speak() {
        return super.speak() + "!";
    }
}
console.log(new Puppy().speak());
// gibt Woof! aus
```
Beachte den Unterschied: `super(...)` ruft den **Konstruktor** der Elternklasse auf, `super.name(...)` ruft eine **Methode** der Elternklasse auf.

---

Bisher wurde jede Eigenschaft innerhalb des Konstruktors angelegt. Ein **Klassenfeld** erlaubt es dir, sie direkt im Klassenkörper zu deklarieren, mit einem optionalen Startwert:
```javascript
class Counter {
    count = 0;
    step = 1;
}
console.log(new Counter().count);
// gibt 0 aus
```
Felder werden jeder neuen Instanz zugewiesen, bevor der Konstruktor-Körper läuft, sodass sich der Konstruktor bereits auf sie verlassen kann. Ein Feld ohne Wert ist trotzdem deklariert, es startet nur als `undefined`:
```javascript
class Task {
    done = false;
    title;
}
```
Beachte die Syntax: kein `let`, kein `const`, kein `this` in der Deklaration, und die Zeile endet mit einem Semikolon.

---

Die Reihenfolge spielt eine Rolle, wenn Klassen voneinander erben. Eine `class`-Deklaration wird **nicht** so gehoistet wie eine `function`: Der Name existiert erst ab der Zeile, in der die Klasse geschrieben wird. Eine Kindklasse muss daher *nach* der Elternklasse erscheinen, die sie erweitert, sonst schlägt die `extends`-Klausel mit einem `ReferenceError` fehl.

---

Manches Verhalten gehört zur Klasse selbst und nicht zu einer einzelnen Instanz. Eine Umrechnung zwischen zwei Einheiten braucht zum Beispiel kein Objekt, auf dem sie arbeitet. Markiert man eine Methode als **`static`**, liegt sie auf der Klasse:
```javascript
class MathUtils {
    static double(n) {
        return n * 2;
    }
}
console.log(MathUtils.double(4));
// gibt 8 aus
```
Eine statische Methode wird über den Klassennamen aufgerufen, nie über eine Instanz: `new MathUtils().double(4)` wirft einen `TypeError`, weil Instanzen keine statischen Mitglieder erhalten. Innerhalb einer statischen Methode verweist `this` auf die Klasse, sodass eine statische Methode eine andere mit `this.otherStatic(...)` aufrufen kann.

---

`static` funktioniert auch bei Feldern. Eine **statische Eigenschaft** wird einmal auf der Klasse gespeichert, nicht einmal pro Instanz, was sie zum natürlichen Ort für einen gemeinsamen Zähler oder eine Konstante macht:
```javascript
class Circle {
    static PI = 3.14;
}
console.log(Circle.PI);
// gibt 3.14 aus
```
Weil es nur eine Kopie gibt, ändert jede Instanz, die sie aktualisiert, denselben Wert. Innerhalb eines Konstruktors greifst du über den Klassennamen darauf zu, `Circle.PI`, und nicht über `this`: `this.PI` würde auf der Instanz nach einer Eigenschaft suchen, nichts finden und dir `undefined` geben.

---

Eine sehr häufige Verwendung einer statischen Methode ist eine **Fabrik**: eine Methode, die eine Instanz aus einer anderen Form von Daten erzeugt und zurückgibt. Sie hält `new` an einem Ort und gibt der Konstruktion einen Namen, der sagt, was sie tut:
```javascript
class Duration {
    constructor(seconds) {
        this.seconds = seconds;
    }
    static fromMinutes(minutes) {
        return new Duration(minutes * 60);
    }
}
console.log(Duration.fromMinutes(2).seconds);
// gibt 120 aus
```
Eine Fabrik kann aufgerufen werden, bevor irgendeine Instanz existiert, was einer normalen Methode nicht möglich wäre.

---

Ein **Getter** ist eine Methode, die wie eine Eigenschaft gelesen wird. Schreibe `get` davor und lass die Klammern an der Aufrufstelle weg:
```javascript
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    get area() {
        return this.width * this.height;
    }
}
const r = new Rectangle(3, 4);
console.log(r.area);
// gibt 12 aus
```
`r.area` führt die Methode aus und liefert ihr Ergebnis zurück, es ist also eine Zahl. Zusätzliche Klammern würden dann versuchen, diese Zahl aufzurufen, was fehlschlägt.

Das Spiegelbild dazu ist ein **Setter**, deklariert mit `set`, der ausgeführt wird, wenn der Eigenschaft ein Wert zugewiesen wird. Er nimmt genau einen Parameter entgegen:
```javascript
set area(value) {
    this.width = value / this.height;
}
```

---

Der eigentliche Wert eines Setters liegt darin, dass er ablehnen kann. Zwischen der Zuweisung und dem gespeicherten Wert hast du die Gelegenheit zu prüfen, zu begrenzen oder abzulehnen, was ankommt:
```javascript
class Volume {
    constructor(level) {
        this._level = level;
    }
    get level() {
        return this._level;
    }
    set level(value) {
        if (value <= 10) {
            this._level = value;
        }
    }
}
const v = new Volume(3);
v.level = 50;
console.log(v.level);
// gibt 3 aus, der Setter hat 50 abgelehnt
```
Ein Getter und ein Setter mit demselben Namen bilden zusammen eine Eigenschaft, daher können sie nicht zusätzlich ein normales Feld sein: Der gespeicherte Wert lebt unter einem anderen Namen, üblicherweise derselbe Name mit einem vorangestellten Unterstrich.

---

Der führende Unterstrich von `_temperature` ist nur eine Konvention: Nichts hindert die Außenwelt daran, `v._level = 999` zu schreiben und deinen Setter komplett zu umgehen. Ein **privates Feld** wird von der Sprache erzwungen. Sein Name beginnt mit `#`, es muss im Klassenkörper deklariert werden und kann nur innerhalb dieser Klasse gelesen oder geschrieben werden:
```javascript
class Secret {
    #code = 1234;
    reveal() {
        return this.#code;
    }
}
const s = new Secret();
console.log(s.reveal());
// gibt 1234 aus
console.log(s.#code);
// SyntaxError: the field is not accessible here
```
Zwei Details, an denen man leicht stolpert. Das `#` ist Teil des Namens, daher schreibst du immer `this.#code`, nie `this.code`. Und ein privates Feld taucht weder in `Object.keys` noch in `console.log` der Instanz auf.

---

Auch Methoden können privat sein. Stelle dem Namen ein `#` voran und die Methode verschwindet von der öffentlichen Oberfläche der Klasse, während sie aus jeder anderen Methode heraus weiterhin mit `this.#name(...)` aufrufbar bleibt:
```javascript
class Receipt {
    #format(n) {
        return `$${n}`;
    }
    print(n) {
        return this.#format(n);
    }
}
console.log(new Receipt().print(7));
// gibt $7 aus
```
So hältst du Hilfsschritte aus der API heraus: Der Aufrufer sieht `print`, nicht das Formatierungsdetail dahinter. Private Felder und private Methoden geben einer Klasse zusammen ein klares Innen und Außen.

---

Das Ausgeben eines Objekts liefert meist etwas Unnützes. Immer wenn JavaScript einen String braucht und stattdessen ein Objekt bekommt, ruft es die **`toString`**-Methode des Objekts auf, und die Standardvariante gibt `[object Object]` zurück. Eine eigene Definition ersetzt das:
```javascript
class Money {
    constructor(amount) {
        this.amount = amount;
    }
    toString() {
        return `$${this.amount}`;
    }
}
console.log(`${new Money(7)}`);
// gibt $7 aus
```
Dieselbe Methode wird von der String-Verkettung und von `String(value)` benutzt. Wenn du auch eine sinnvolle **Zahl** willst, definiere `[Symbol.toPrimitive](hint)`, das `"string"`, `"number"` oder `"default"` erhält und entscheidet, was zurückgegeben wird; wenn es existiert, hat es Vorrang vor `toString`.

---

Der Operator **`instanceof`** fragt, ob ein Objekt aus einer Klasse erzeugt wurde, oder aus einer beliebigen Klasse, die von ihr erbt:
```javascript
class Animal {}
class Dog extends Animal {}
const max = new Dog();
console.log(max instanceof Dog);    // true
console.log(max instanceof Animal); // true, Dog extends Animal
```
JavaScript hat kein `abstract`-Schlüsselwort, aber dieselbe Idee schreibt man von Hand: Eine Basisklasse definiert die Form, und jede Methode, die eine Kindklasse *bereitstellen muss*, wirft einfach einen Fehler:
```javascript
class Shape {
    area() {
        throw new Error("area() must be implemented");
    }
}
```
Eine Kindklasse, die vergisst, `area` zu überschreiben, scheitert laut beim ersten Einsatz, statt stillschweigend `undefined` zurückzugeben.

---

`for...of` und der Spread-Operator `...` funktionieren nicht mit einem beliebigen Objekt: Sie funktionieren mit **Iterables**, Objekten, die eine Methode unter dem besonderen Schlüssel `Symbol.iterator` bereitstellen. Gib deiner Klasse diese Methode und sie gehört zum Club:
```javascript
class Playlist {
    constructor(songs) {
        this.songs = songs;
    }
    *[Symbol.iterator]() {
        for (const song of this.songs) {
            yield song;
        }
    }
}
const list = new Playlist(["a", "b"]);
console.log([...list]);
// gibt [ 'a', 'b' ] aus
```
Das `*` vor dem Namen macht daraus einen **Generator**: eine Funktion, die Werte einzeln mit `yield` herausgibt und dazwischen pausiert. Das ist der kürzeste Weg, das Iterationsprotokoll zu erfüllen, und er funktioniert auch für Werte, die berechnet statt gespeichert werden.
