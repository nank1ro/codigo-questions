Ein **Struct** (kurz für *Struktur*) ist ein Typ, den du selbst entwirfst, um zusammengehörige Werte zusammenzuhalten. Statt eine separate `title`-Variable und eine separate `pages`-Variable zu verwalten, beschreibst du ein `Book` einmal und verwendest es überall.

Mit dem Schlüsselwort `struct` deklarierst du eines, und die Variablen, die darin stehen, sind seine **gespeicherten Eigenschaften**:
```swift
struct Book {
    var title: String
    var pages: Int
}
```
`Book` ist jetzt ein Typ, genau wie `Int` oder `String`. Auf eine Eigenschaft einer Instanz greifst du mit einem Punkt zu:
```swift
let book = Book(title: "Swift", pages: 120)
print(book.title) // Swift
```

---

Du hast nie den Code geschrieben, der ein `Book` erzeugt, und trotzdem funktionierte `Book(title: "Swift", pages: 120)`. Swift schreibt ihn für dich: Jedes Struct erhält kostenlos einen **memberwise initializer**, einen Initialisierer, dessen Parameter seine gespeicherten Eigenschaften sind, in der Reihenfolge, in der sie deklariert sind, wobei jeder den Eigenschaftsnamen als Argument-Label verwendet:
```swift
struct Point {
    var x: Int
    var y: Int
}

let p = Point(x: 3, y: 4)
print(p.x) // 3
```
Klassen bekommen das nicht kostenlos, was ein Grund ist, warum Structs der schnellste Weg sind, einen Wert zu modellieren.

---

Einer gespeicherten Eigenschaft kann direkt dort, wo sie deklariert wird, ein **Standardwert** gegeben werden. Swift leitet ihren Typ aus diesem Wert ab, sodass du die Typannotation weglassen kannst:
```swift
struct Counter {
    var label: String
    var value = 0
}
```
Der memberwise initializer macht aus jeder Eigenschaft mit Standardwert ein optionales Argument: übergib es, um den Standardwert zu überschreiben, und lasse es weg, um ihn zu behalten.
```swift
let a = Counter(label: "clicks")
print(a.value) // 0

let b = Counter(label: "clicks", value: 7)
print(b.value) // 7
```

---

Ein Struct kann auch **Methoden** enthalten: Funktionen, die innerhalb der geschweiften Klammern geschrieben sind und auf der Instanz arbeiten, auf der sie aufgerufen werden. Innerhalb einer Methode verwendest du die Eigenschaftsnamen direkt, ohne Präfix:
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
Wenn ein Parameter der Methode einen Eigenschaftsnamen verschattet, schreibe `self.width`, um die Eigenschaft der Instanz zu meinen.

---

Eine **berechnete Eigenschaft** sieht aus wie eine Eigenschaft, verhält sich aber wie eine Methode: Sie speichert nichts, sondern berechnet ihren Wert bei jedem Lesen neu. Du schreibst den Typ, dann einen Codeblock, der den Wert zurückgibt:
```swift
struct Rectangle {
    var width: Int
    var height: Int

    var area: Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area) // 12, ohne Klammern
```
Berechnete Eigenschaften sind nicht Teil des memberwise initializers, da es nichts zu speichern gibt. Verwende eine, wenn der Wert aus den anderen abgeleitet ist, und eine Methode, wenn die Arbeit Parameter benötigt.

---

Ein Struct ist ein **Werttyp**: Weist man es einer anderen Variable zu oder übergibt es an eine Funktion, wird eine *Kopie* übergeben. Die Kopie zu ändern lässt das Original unberührt.
```swift
struct Point {
    var x: Int
}

var a = Point(x: 1)
var b = a
b.x = 99
print(a.x) // 1
```
Eine Klasse ist ein **Referenztyp**: `b = a` würde beide Namen auf dieselbe Instanz zeigen lassen, deshalb würde `b.x = 99` auch `a.x` auf `99` ändern.

Das ist der echte Unterschied zwischen beiden und der Grund, warum Swift die meisten Daten als Structs modelliert: Ein Wert, den du hältst, kann von Code, der ihn erhalten hat, nicht heimlich geändert werden.

---

Da ein Struct ein Wert ist, darf eine Methode seine Eigenschaften nicht ändern, außer du sagst es mit dem Schlüsselwort `mutating`:
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
Eine mutating-Methode kann nur auf einer Instanz aufgerufen werden, die in einem `var` gespeichert ist. Bei einer `let`-Instanz ist der Wert eingefroren, deshalb würde `c.increase(by: 5)` nicht kompilieren.

---

Wenn der memberwise initializer nicht die Art ist, wie dein Typ erstellt werden soll, schreibe deinen eigenen **Initializer**. Er wird mit `init` deklariert, nimmt die Parameter, die du wählst, und muss jeder gespeicherten Eigenschaft einen Wert geben, bevor er endet. In ihm ist `self` die Instanz, die erstellt wird:
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
Das Schreiben eines `init` innerhalb der geschweiften Klammern des Structs ersetzt den memberwise initializer, daher existiert `Square(side: 5)` von nun an nicht mehr.

---

Manche Werte gehören zum Typ selbst und nicht zu einer einzelnen Instanz: ein Währungscode, ein geteilter Standardwert, eine Fabrik, die einen häufigen Fall erstellt. Markiere sie als `static` und lies sie über den Typnamen:
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
Hier ist `currency` mit `let` deklariert, weil es sich nie ändert, es ist also eine Konstante, die vom ganzen Programm geteilt wird. `Money.currency` funktioniert, ohne ein einziges `Money` zu erstellen, während `amount` eine Instanz benötigt.

---

Zwei Structs können nicht mit `==` verglichen werden, bis der Typ sagt, dass er es unterstützt. Das machst du, indem du dich an das `Equatable`-**Protokoll** hältst, das in der Deklaration nach einem Doppelpunkt geschrieben wird:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

let a = Point(x: 1, y: 2)
let b = Point(x: 1, y: 2)
print(a == b) // true
```
`==` musst du nicht selbst schreiben: Wenn jede gespeicherte Eigenschaft bereits `Equatable` ist, generiert Swift ihn für dich und vergleicht die Eigenschaften einzeln. Zwei Instanzen sind gleich, wenn alle ihre Eigenschaften gleich sind, was genau das ist, was du von einem Wert erwartest.

---

Ein Struct ist ein Typ wie jeder andere, also kann es in einem Array, einem Wörterbuch oder einem Set gespeichert werden, und jedes Werkzeug, das du bereits kennst, funktioniert damit weiter:
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
Denke daran, dass das Array *Kopien* enthält: `items[0]` in eine Variable zu lesen und sie zu ändern, berührt das Array nicht.
