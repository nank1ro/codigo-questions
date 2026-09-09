Eine **Funktion höherer Ordnung** ist eine Funktion, die eine andere Funktion als Argument entgegennimmt, eine zurückgibt oder beides. Du hast bereits `map`, `filter`, `reduce` und `sorted(by:)` kennengelernt: Sie nehmen eine Closure entgegen und wenden sie auf die Elemente einer Sammlung an. Swift hat noch viele mehr davon, und sie zu kennen ermöglicht es dir, lange Schleifen durch eine einzige lesbare Zeile zu ersetzen.
`compactMap` funktioniert wie `map`, aber die Closure gibt ein Optional zurück und die `nil`-Ergebnisse werden verworfen:
```swift
let words = ["3", "seven", "12"]
let numbers = words.compactMap { Int($0) }
print(numbers) // [3, 12]
```
`Int("seven")` ist `nil`, deshalb verschwindet dieses Element und das Ergebnis ist ein `[Int]`, nicht ein `[Int?]`.

---

`flatMap` ist für Closures, die ein **Array** zurückgeben: Statt ein Array von Arrays zu erzeugen, fügt es alle zurückgegebenen Arrays zu einem einzigen flachen Ergebnis zusammen:
```swift
let teams = [["Ann", "Bob"], ["Cid"]]
print(teams.map { $0 })     // [["Ann", "Bob"], ["Cid"]]
print(teams.flatMap { $0 }) // ["Ann", "Bob", "Cid"]
```
Die Closure kann jedes innere Array auch verändern, bevor es zusammengefügt wird, zum Beispiel gibt `teams.flatMap { $0.reversed() }` `["Bob", "Ann", "Cid"]` zurück.

---

Die drei `map`-Varianten unterscheiden sich nur darin, was die Closure zurückgibt:
- `map`: ein beliebiger Wert, ein Ergebnis pro Element
- `compactMap`: ein Optional, die `nil`-Ergebnisse werden verworfen
- `flatMap`: ein Array, alle Ergebnisse werden zu einem Array zusammengefügt

Die an `flatMap` übergebene Closure kann selbst `map` auf dem inneren Array aufrufen und so eine Transformation in die andere verschachteln:
```swift
let matrix = [[1, 2], [3]]
print(matrix.flatMap { row in row.map { $0 + 1 } }) // [2, 3, 4]
```

---

`reduce` baut bei jedem Schritt einen neuen Akkumulationswert auf, was verschwenderisch ist, wenn das Ergebnis ein Array oder ein Wörterbuch ist. `reduce(into:)` übergibt der Closure den Akkumulator als `inout`-Parameter, sodass er direkt vor Ort verändert werden kann, ohne `return`:
```swift
let words = ["a", "b", "a"]
let counts = words.reduce(into: [String: Int]()) { result, word in
    result[word, default: 0] += 1
}
print(counts["a"]!) // 2
```
`[String: Int]()` erzeugt ein leeres Wörterbuch, und `result[word, default: 0]` liest die aktuelle Anzahl oder `0`, wenn der Schlüssel fehlt.

---

Einige Funktionen höherer Ordnung beantworten eine Frage über die Sammlung, statt sie zu transformieren. Sie nehmen alle eine Closure entgegen, die einen `Bool` zurückgibt:
- `first(where:)` gibt das erste Element zurück, das die Closure erfüllt, oder `nil`, wenn es keines gibt
- `contains(where:)` gibt `true` zurück, wenn mindestens ein Element sie erfüllt
- `allSatisfy` gibt `true` zurück, wenn jedes Element sie erfüllt

```swift
let nums = [4, 9, 16]
print(nums.first(where: { $0 > 5 }))  // Optional(9)
print(nums.contains(where: { $0 > 5 })) // true
print(nums.allSatisfy { $0 > 5 })       // false
```
Anders als `filter` stoppt `first(where:)` bei der ersten Übereinstimmung und baut kein neues Array auf.

---

`contains(where:)` und `allSatisfy` ersetzen das verbreitete Muster einer Schleife mit einer Flag-Variablen. Beide stoppen, sobald die Antwort bekannt ist: `contains(where:)` bei der ersten Übereinstimmung, `allSatisfy` beim ersten Element, das die Prüfung nicht erfüllt.
```swift
let ages = [15, 22, 40]
let anyMinor = ages.contains { $0 < 18 }  // true
let allAdults = ages.allSatisfy { $0 >= 18 } // false
```
`contains { ... }` ist die Trailing-Closure-Form von `contains(where:)`, nicht zu verwechseln mit `contains(_:)`, das nach einem bestimmten Wert sucht.

---

Funktionen höherer Ordnung funktionieren mit jedem Array, auch mit Arrays aus eigenen Structs. `filter` und danach `map` zu verketten ist die übliche Methode, um einige Elemente auszuwählen und aus jedem einen Wert zu extrahieren:
```swift
struct Book {
    var title: String
    var pages: Int
}
let books = [Book(title: "Dune", pages: 412), Book(title: "Haiku", pages: 40)]
let long = books.filter { $0.pages > 100 }.map { $0.title }
print(long) // ["Dune"]
```
In umgekehrter Reihenfolge, erst `map` dann `filter`, würde die `pages`-Eigenschaft verloren gehen, bevor die Prüfung sie verwenden könnte.

---

Wenn eine Closure nur eine Eigenschaft liest, kannst du stattdessen einen **Key Path** übergeben: `\.name` bedeutet „die `name`-Eigenschaft des Elements“, und `map(\.name)` ist dasselbe wie `map { $0.name }`.
Das Sortieren nach einer Eigenschaft verwendet die übliche Closure mit zwei Argumenten, die diese Eigenschaft auf beiden Elementen vergleicht:
```swift
struct City {
    var name: String
    var population: Int
}
let cities = [City(name: "Oslo", population: 700), City(name: "Rome", population: 2800)]
let byPopulation = cities.sorted { $0.population > $1.population }
print(byPopulation.map(\.name)) // ["Rome", "Oslo"]
```

---

Um nach **mehr als einem Kriterium** zu sortieren, vergleiche die erste Eigenschaft und greife nur dann auf die zweite zurück, wenn die ersten Werte gleich sind:
```swift
let sorted = people.sorted {
    if $0.age != $1.age {
        return $0.age < $1.age
    }
    return $0.name < $1.name
}
```
Hier werden die Personen nach Alter geordnet, und Personen mit demselben Alter werden nach Name geordnet. Die Closure muss nur dann `true` zurückgeben, wenn das erste Element vor dem zweiten stehen soll, damit der Fall gleicher Werte an den nächsten Vergleich durchgereicht wird.

---

`enumerated()` verwandelt ein Array in eine Sequenz von `(offset, element)`-Paaren, sodass eine Closure die Position jedes Elements zusammen mit seinem Wert verwenden kann:
```swift
let steps = ["mix", "bake"]
let numbered = steps.enumerated().map { pair in
    "\(pair.offset + 1). \(pair.element)"
}
print(numbered) // ["1. mix", "2. bake"]
```
Da jedes Paar ein Tupel ist, kann die Closure es auch destrukturieren: `.map { (i, step) in "\(i + 1). \(step)" }`.

---

`zip` ordnet die Elemente zweier Sequenzen Position für Position paarweise an und erzeugt dabei eine Sequenz von Tupeln. Es stoppt am Ende der kürzeren:
```swift
let names = ["Ann", "Bob"]
let ages = [31, 27, 99]
let pairs = zip(names, ages).map { "\($0) is \($1)" }
print(pairs) // ["Ann is 31", "Bob is 27"]
```
Innerhalb der Closure ist `$0` das Element aus der ersten Sequenz und `$1` das aus der zweiten. `zip` ist eine freie Funktion, keine Methode: Du schreibst `zip(a, b)`, nicht `a.zip(b)`.

---

`forEach` ist das Gegenstück zur `for-in`-Schleife im Stil der Funktionen höherer Ordnung: Sie ruft die Closure einmal pro Element auf, der Reihe nach. Der Unterschied liegt darin, wie du die Schleife verlässt. In einer `for-in`-Schleife kannst du mit `break` abbrechen oder `continue` verwenden; innerhalb einer `forEach`-Closure sind `break` und `continue` nicht erlaubt, und `return` beendet nur den **aktuellen Aufruf** der Closure, danach wird das nächste Element wie gewohnt verarbeitet:
```swift
[1, 2, 3].forEach { n in
    if n == 2 { return }
    print(n)
}
// prints 1 and 3
```
Verwende `forEach` für einen kurzen Seiteneffekt auf jedem Element und `for-in`, wenn du vorzeitig stoppen musst.

---

`Dictionary(grouping:by:)` teilt eine Sammlung in ein Wörterbuch aus Arrays auf. Die Closure berechnet den **Schlüssel** jedes Elements, und alle Elemente mit demselben Schlüssel landen im selben Array:
```swift
let words = ["apple", "bee", "avocado"]
let byInitial = Dictionary(grouping: words, by: { $0.first! })
print(byInitial["a"]!) // ["apple", "avocado"]
```
`mapValues` transformiert jeden Wert eines Wörterbuchs und behält dabei die Schlüssel, daher ist es der naheliegende nächste Schritt nach dem Gruppieren:
```swift
let sizes = byInitial.mapValues { $0.count }
print(sizes["a"]!) // 2
```

---

`prefix(while:)` übernimmt Elemente vom Anfang, **solange** die Closure `true` zurückgibt, und stoppt beim ersten Element, das die Prüfung nicht erfüllt, selbst wenn spätere Elemente sie wieder erfüllen würden. `drop(while:)` ist sein Gegenstück: Es überspringt genau diesen Anfangsabschnitt und gibt alles andere zurück:
```swift
let temps = [12, 15, 21, 14]
print(temps.prefix { $0 < 20 }) // [12, 15]
print(temps.drop { $0 < 20 })   // [21, 14]
```
Beide geben ein `ArraySlice` zurück, eine Ansicht auf das ursprüngliche Array, das wie ein Array ausgegeben wird und sich mit `Array(...)` in eines umwandeln lässt.

---

Du kannst eigene Funktionen höherer Ordnung schreiben. Eine Funktion, die eine Closure entgegennimmt und eine aus ihr aufgebaute **neue Closure zurückgibt**, ist ein verbreitetes Muster: Die zurückgegebene Closure erfasst die ursprüngliche, daher muss der Parameter `@escaping` sein.
Zum Beispiel verwandelt `negate` ein Prädikat in sein Gegenteil, bereit, um an `filter` übergeben zu werden:
```swift
func negate(_ predicate: @escaping (Int) -> Bool) -> (Int) -> Bool {
    return { !predicate($0) }
}
let isEven: (Int) -> Bool = { $0 % 2 == 0 }
print([1, 2, 3, 4].filter(negate(isEven))) // [1, 3]
```
Beachte, dass `filter(negate(isEven))` die Closure als normales Argument übergibt, ohne Trailing-Closure-Syntax.

---

`map` und `filter` auf einem Array sind **gierig**: Jedes verarbeitet das gesamte Array und baut ein neues auf, bevor der nächste Schritt läuft. Bei einer großen Sammlung, oder wenn du nur das erste Ergebnis brauchst, ist das verschwendete Arbeit.
Die `lazy`-Eigenschaft gibt eine Ansicht zurück, deren Operationen nur ausgeführt werden, wenn ein Element tatsächlich angefordert wird, und zwar jeweils ein Element auf einmal durch die gesamte Kette:
```swift
let firstBig = (1...1000).lazy.map { $0 * $0 }.first { $0 > 50 }
print(firstBig!) // 64
```
Hier werden nur `1, 2, ..., 8` quadriert: `first(where:)` fordert Elemente an, bis eines die Bedingung erfüllt, und die Kette stoppt dort. Ohne `lazy` würde `map` zuerst alle 1000 Zahlen quadrieren.
