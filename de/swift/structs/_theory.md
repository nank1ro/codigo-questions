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
print(r.area) // 12, no parentheses
```
Berechnete Eigenschaften sind nicht Teil des memberwise initializers, da es nichts zu speichern gibt. Verwende eine, wenn der Wert aus den anderen abgeleitet ist, und eine Methode, wenn die Arbeit Parameter benötigt.
