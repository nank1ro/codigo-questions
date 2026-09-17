Una **struct** (abbreviazione di *structure*, cioè struttura) è un tipo che progetti tu stesso per tenere insieme valori correlati. Invece di destreggiarti tra una `title` separata e una `pages` separata, descrivi un `Book` una volta sola e lo usi ovunque.

Se ne dichiara una con la parola chiave `struct`, e le variabili scritte al suo interno sono le sue **proprietà memorizzate** (stored properties):
```swift
struct Book {
    var title: String
    var pages: Int
}
```
`Book` è ora un tipo, esattamente come `Int` o `String`. Si accede a una proprietà di un'istanza con un punto:
```swift
let book = Book(title: "Swift", pages: 120)
print(book.title) // Swift
```

---

Non hai mai scritto il codice che costruisce una `Book`, eppure `Book(title: "Swift", pages: 120)` ha funzionato. Swift lo scrive per te: ogni struct riceve gratis un **inizializzatore membro per membro** (memberwise initializer), un inizializzatore i cui parametri sono le sue proprietà memorizzate, nell'ordine in cui sono dichiarate, ognuno dei quali usa il nome della proprietà come etichetta dell'argomento:
```swift
struct Point {
    var x: Int
    var y: Int
}

let p = Point(x: 3, y: 4)
print(p.x) // 3
```
Le classi non lo ricevono gratis, ed è uno dei motivi per cui le struct sono il modo più rapido di modellare un valore.

---

Una proprietà memorizzata può ricevere un **valore predefinito** proprio dove viene dichiarata. Swift ne deduce il tipo da quel valore, quindi puoi omettere l'annotazione del tipo:
```swift
struct Counter {
    var label: String
    var value = 0
}
```
L'inizializzatore membro per membro trasforma ogni proprietà con valore predefinito in un argomento facoltativo: passalo per sostituire il valore predefinito, omettilo per conservarlo.
```swift
let a = Counter(label: "clicks")
print(a.value) // 0

let b = Counter(label: "clicks", value: 7)
print(b.value) // 7
```

---

Una struct può anche contenere **metodi**: funzioni scritte tra le graffe che operano sull'istanza su cui vengono richiamate. All'interno di un metodo usi i nomi delle proprietà direttamente, senza alcun prefisso:
```swift
struct Rectangle {
    var width: Int
    var height: Int

    func area() -> Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area()) // 12
```
Se un parametro del metodo nasconde il nome di una proprietà, scrivi `self.width` per indicare la proprietà dell'istanza.

---

Una **proprietà calcolata** (computed property) sembra una proprietà ma si comporta come un metodo: non memorizza nulla, calcola il suo valore ogni volta che la leggi. Scrivi il tipo, poi un blocco di codice che restituisce il valore:
```swift
struct Rectangle {
    var width: Int
    var height: Int

    var area: Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area) // 12, senza parentesi
```
Le proprietà calcolate non fanno parte dell'inizializzatore membro per membro, poiché non c'è nulla da memorizzare. Usane una quando il valore deriva dagli altri, e un metodo quando il lavoro richiede parametri.

---

Una struct è un **tipo a valore** (value type): assegnarla a un'altra variabile, o passarla a una funzione, consegna una *copia*. Modificare la copia lascia intatto l'originale.
```swift
struct Point {
    var x: Int
}

var a = Point(x: 1)
var b = a
b.x = 99
print(a.x) // 1
```
Una classe è un **tipo a riferimento** (reference type): `b = a` farebbe puntare entrambi i nomi alla stessa istanza, quindi `b.x = 99` cambierebbe anche `a.x` in `99`.

Questa è la vera differenza tra i due, e il motivo per cui Swift modella la maggior parte dei dati come struct: un valore che possiedi non può essere modificato alle tue spalle dal codice che lo ha ricevuto.

---

Poiché una struct è un valore, a un metodo non è consentito modificare le sue proprietà a meno che tu non lo dichiari con la parola chiave `mutating`:
```swift
struct Counter {
    var value = 0

    mutating func increase(by amount: Int) {
        value += amount
    }
}

var c = Counter()
c.increase(by: 5)
print(c.value) // 5
```
Un metodo mutating può essere richiamato solo su un'istanza memorizzata in una `var`. Su un'istanza `let` il valore è congelato, quindi `c.increase(by: 5)` non compirebbe.

---

Quando l'inizializzatore membro per membro non è il modo in cui vuoi che il tuo tipo venga costruito, scrivi un tuo **inizializzatore**. Si dichiara con `init`, prende i parametri che scegli e deve dare a ogni proprietà memorizzata un valore prima di terminare. Al suo interno, `self` è l'istanza che viene creata:
```swift
struct Square {
    var side: Int

    init(_ side: Int) {
        self.side = side
    }
}

let s = Square(5)
print(s.side) // 5
```
Scrivere un `init` tra le graffe della struct sostituisce quello membro per membro, quindi da quel momento `Square(side: 5)` non esiste più.

---

Alcuni valori appartengono al tipo stesso piuttosto che a una singola istanza: un codice valuta, un valore predefinito condiviso, una factory che costruisce un caso comune. Contrassegnali `static` e leggili tramite il nome del tipo:
```swift
struct Money {
    static let currency = "EUR"
    var amount: Int

    static func zero() -> Money {
        return Money(amount: 0)
    }
}

print(Money.currency)     // EUR
print(Money.zero().amount) // 0
```
Qui `currency` è dichiarata con `let` perché non cambia mai, quindi è una costante condivisa dall'intero programma. `Money.currency` funziona senza creare nemmeno una `Money`, mentre `amount` richiede un'istanza.

---

Due struct non possono essere confrontate con `==` finché il tipo non dichiara di supportarlo. Lo fai conformandoti al **protocollo** `Equatable`, scritto dopo i due punti nella dichiarazione:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

let a = Point(x: 1, y: 2)
let b = Point(x: 1, y: 2)
print(a == b) // true
```
Non devi scrivere tu `==`: quando ogni proprietà memorizzata è già `Equatable`, Swift lo sintetizza per te, confrontando le proprietà una per una. Due istanze sono uguali quando tutte le loro proprietà sono uguali, che è esattamente ciò che ci si aspetta da un valore.

---

Una struct è un tipo come gli altri, quindi può essere memorizzata in un array, un dizionario o un set, e ogni strumento che già conosci continua a funzionare su di essa:
```swift
struct Item {
    var name: String
    var price: Int
}

let items = [Item(name: "Tea", price: 3), Item(name: "Cake", price: 7)]

for item in items {
    print(item.name)
}

let names = items.map { $0.name }
let total = items.reduce(0) { $0 + $1.price }
print(total) // 10
```
Ricorda che l'array contiene *copie*: leggere `items[0]` in una variabile e modificarla non tocca l'array.
