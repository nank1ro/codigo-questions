Sai già che `extends` rende una classe figlia di un'altra. Ciò che quella parola chiave ti dà davvero è l'**ereditarietà**: la figlia riceve gratuitamente ogni proprietà e metodo del genitore, e può aggiungerne di propri sopra.

Il pezzo che rende utile l'ereditarietà è **`super`**. Dentro il costruttore di una classe figlia, `super(...)` chiama il costruttore del genitore, così il genitore può impostare la parte dell'oggetto che gli appartiene:
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
Qui `super(name)` passa `name` ad `Animal`, che lo memorizza, e `Dog` deve preoccuparsi solo di `breed`.

---

Una classe figlia non deve ridefinire tutto ciò che il genitore fornisce già. Anche i metodi sono ereditati, quindi un'istanza della figlia può chiamarli come se fossero suoi:
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
// prints Max makes a sound
```
Quando una figlia dichiara un proprio costruttore, chiamare `super(...)` al suo interno è **obbligatorio**: senza di esso l'oggetto non viene mai inizializzato e JavaScript lancia un `ReferenceError`. Una figlia senza alcun costruttore va bene, perché JavaScript ne scrive uno che inoltra ogni argomento al genitore.

---

La regola su `super()` è più severa di "chiamalo da qualche parte". Nel costruttore di una classe figlia la parola `this` non esiste finché `super()` non è stato eseguito, perché è il costruttore del genitore a creare l'oggetto. Toccare `this` prima di quella riga lancia un errore:
```javascript
class Child extends Base {
    constructor() {
        this.x = 1; // ReferenceError
        super();
    }
}
```
Quindi `super(...)` dovrebbe essere la **prima istruzione** di ogni costruttore figlio che usa `this`.

---

Quando una classe figlia definisce un metodo che il genitore ha già, vince la versione della figlia. Questo si chiama **override** (sovrascrittura):
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
// prints Woof
```
L'override non elimina la versione del genitore, la nasconde soltanto. Dentro il metodo della figlia, `super.methodName(...)` raggiunge comunque quella del genitore, il che ti permette di estendere il comportamento del genitore invece di sostituirlo:
```javascript
class Puppy extends Dog {
    speak() {
        return super.speak() + "!";
    }
}
console.log(new Puppy().speak());
// prints Woof!
```
Nota la differenza: `super(...)` chiama il **costruttore** del genitore, `super.name(...)` chiama un **metodo** del genitore.

---

Finora ogni proprietà veniva creata dentro il costruttore. Un **campo di classe** ti permette di dichiararla direttamente nel corpo della classe, con un valore iniziale facoltativo:
```javascript
class Counter {
    count = 0;
    step = 1;
}
console.log(new Counter().count);
// prints 0
```
I campi vengono assegnati a ogni nuova istanza prima che il corpo del costruttore venga eseguito, quindi il costruttore può già contare su di essi. Un campo senza valore è comunque dichiarato, semplicemente parte come `undefined`:
```javascript
class Task {
    done = false;
    title;
}
```
Nota la sintassi: niente `let`, niente `const`, niente `this` nella dichiarazione, e la riga termina con un punto e virgola.

---

L'ordine conta quando le classi ereditano l'una dall'altra. Una dichiarazione `class` **non** viene sollevata (hoisted) come avviene per una `function`: il nome esiste solo dalla riga in cui la classe è scritta in poi. Quindi una classe figlia deve comparire *dopo* il genitore che estende, altrimenti la clausola `extends` fallisce con un `ReferenceError`.

---

Alcuni comportamenti appartengono alla classe stessa piuttosto che a una singola istanza. Una conversione tra due unità, per esempio, non ha bisogno di un oggetto su cui lavorare. Contrassegnare un metodo con **`static`** lo mette sulla classe:
```javascript
class MathUtils {
    static double(n) {
        return n * 2;
    }
}
console.log(MathUtils.double(4));
// prints 8
```
Un metodo statico viene chiamato sul nome della classe, mai su un'istanza: `new MathUtils().double(4)` lancia un `TypeError`, perché le istanze non ricevono i membri statici. Dentro un metodo statico `this` si riferisce alla classe, quindi un metodo statico può chiamarne un altro con `this.otherStatic(...)`.

---

`static` funziona anche con i campi. Una **proprietà statica** viene memorizzata una sola volta sulla classe, non una volta per istanza, il che la rende il posto naturale per un contatore condiviso o una costante:
```javascript
class Circle {
    static PI = 3.14;
}
console.log(Circle.PI);
// prints 3.14
```
Dato che esiste una sola copia, ogni istanza che la aggiorna aggiorna lo stesso valore. Dentro un costruttore vi accedi tramite il nome della classe, `Circle.PI`, e non tramite `this`: `this.PI` cercherebbe una proprietà sull'istanza, non troverebbe nulla e ti darebbe `undefined`.

---

Un uso molto comune di un metodo statico è la **factory** (fabbrica): un metodo che costruisce un'istanza a partire da un'altra forma di dati e la restituisce. Mantiene `new` in un unico posto e dà alla costruzione un nome che dice cosa fa:
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
// prints 120
```
Una factory può essere chiamata prima che esista qualsiasi istanza, cosa che un metodo normale non potrebbe fare.

---

Un **getter** è un metodo che viene letto come se fosse una proprietà. Scrivi `get` davanti ad esso e ometti le parentesi al momento della chiamata:
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
// prints 12
```
`r.area` esegue il metodo e restituisce il suo risultato, quindi è un numero. Aggiungere le parentesi proverebbe quindi a chiamare quel numero, cosa che fallisce.

L'immagine speculare è un **setter**, dichiarato con `set`, che viene eseguito quando alla proprietà viene assegnato un valore. Prende esattamente un parametro:
```javascript
set area(value) {
    this.width = value / this.height;
}
```

---

Il vero valore di un setter è che può rifiutare. Tra l'assegnazione e il valore memorizzato hai la possibilità di controllare, limitare o respingere ciò che arriva:
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
// prints 3, the setter rejected 50
```
Un getter e un setter con lo stesso nome formano un'unica proprietà, quindi non possono essere anche un campo normale: il valore memorizzato vive sotto un nome diverso, per convenzione lo stesso nome con un underscore iniziale.

---

L'underscore iniziale di `_temperature` è solo una convenzione: nulla impedisce al mondo esterno di scrivere `v._level = 999` e passare dritto oltre il tuo setter. Un **campo privato** è invece imposto dal linguaggio. Il suo nome inizia con `#`, deve essere dichiarato nel corpo della classe e può essere letto o scritto solo dall'interno di quella classe:
```javascript
class Secret {
    #code = 1234;
    reveal() {
        return this.#code;
    }
}
const s = new Secret();
console.log(s.reveal());
// prints 1234
console.log(s.#code);
// SyntaxError: the field is not accessible here
```
Due dettagli su cui è facile inciampare. Il `#` fa parte del nome, quindi scrivi sempre `this.#code`, mai `this.code`. E un campo privato non compare in `Object.keys` né nel `console.log` dell'istanza.

---

Anche i metodi possono essere privati. Prefissa il nome con `#` e il metodo sparisce dalla superficie pubblica della classe, pur restando chiamabile da qualsiasi altro metodo con `this.#name(...)`:
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
// prints $7
```
È così che tieni fuori dall'API i passaggi di supporto: chi chiama vede `print`, non il dettaglio di formattazione dietro di essa. Campi privati e metodi privati insieme danno a una classe un dentro e un fuori ben chiari.

---

Stampare un oggetto di solito dà qualcosa di poco utile. Ogni volta che JavaScript ha bisogno di una stringa e riceve invece un oggetto, chiama il metodo **`toString`** dell'oggetto, e quello predefinito restituisce `[object Object]`. Definirne uno tuo sostituisce quel comportamento:
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
// prints $7
```
Lo stesso metodo è usato dalla concatenazione di stringhe e da `String(value)`. Se vuoi anche un **numero** sensato, definisci `[Symbol.toPrimitive](hint)`, che riceve `"string"`, `"number"` o `"default"` e decide cosa restituire; quando esiste ha la precedenza su `toString`.

---

L'operatore **`instanceof`** chiede se un oggetto è stato costruito a partire da una classe, o da qualsiasi classe che erediti da essa:
```javascript
class Animal {}
class Dog extends Animal {}
const max = new Dog();
console.log(max instanceof Dog);    // true
console.log(max instanceof Animal); // true, Dog extends Animal
```
JavaScript non ha una parola chiave `abstract`, ma la stessa idea si scrive a mano: una classe base definisce la forma ed ogni metodo che una figlia *deve* fornire semplicemente lancia un errore:
```javascript
class Shape {
    area() {
        throw new Error("area() must be implemented");
    }
}
```
Una figlia che dimentica di fare l'override di `area` fallisce rumorosamente la prima volta che viene usata, invece di restituire silenziosamente `undefined`.

---

`for...of` e l'operatore spread `...` non funzionano su qualsiasi oggetto: funzionano sugli **iterabili**, oggetti che forniscono un metodo memorizzato sotto la chiave speciale `Symbol.iterator`. Dai alla tua classe quel metodo ed entra nel club:
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
// prints [ 'a', 'b' ]
```
Il `*` davanti al nome lo rende un **generatore**: una funzione che consegna i valori uno alla volta con `yield` e si mette in pausa tra uno e l'altro. È il modo più breve per soddisfare il protocollo di iterazione, e funziona anche per valori che vengono calcolati anziché memorizzati.
