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
print(r.area) // 12, no parentheses
```
Le proprietà calcolate non fanno parte dell'inizializzatore membro per membro, poiché non c'è nulla da memorizzare. Usane una quando il valore deriva dagli altri, e un metodo quando il lavoro richiede parametri.
