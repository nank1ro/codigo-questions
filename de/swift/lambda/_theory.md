Eine **Closure** ist ein Codeblock, den du herumreichen und später aufrufen kannst, wie eine Funktion ohne Namen.
Die vollständige Closure-Ausdruckssyntax schreibt die Parameter und den Rückgabetyp in geschweifte Klammern, gefolgt vom Schlüsselwort `in` und dem Rumpf:
```swift
{ (parameters) -> ReturnType in
    body
}
```
Wie jeder andere Wert kann eine Closure in einer Konstante gespeichert und dann über den Namen der Konstante aufgerufen werden:
```swift
let greet = { (name: String) -> String in
    return "Hello, \(name)!"
}
print(greet("Ada")) // Hello, Ada!
```

---

Jeden Typ innerhalb der Closure auszuschreiben ist oft unnötig. Wenn die Konstante einen expliziten **Funktionstyp** hat, leitet Swift die Parameter- und Rückgabetypen ab, sodass du nur die Parameternamen vor `in` angeben musst:
```swift
let triple: (Int) -> Int = { n in
    return n * 3
}
```
Der Typ `(Int) -> Int` liest sich als „eine Funktion, die einen `Int` entgegennimmt und einen `Int` zurückgibt".
Wenn der Rumpf ein einzelner Ausdruck ist, kann das Schlüsselwort `return` ebenfalls weggelassen werden, das nennt man eine **implizite Rückgabe**:
```swift
let triple: (Int) -> Int = { n in n * 3 }
print(triple(4)) // 12
```

---

Swift geht noch einen Schritt weiter: Innerhalb einer Closure kannst du dich mit den **abgekürzten Argumentnamen** `$0`, `$1`, `$2` und so weiter auf die Argumente beziehen, ohne einen Parameter oder das Schlüsselwort `in` zu deklarieren.
`$0` ist das erste Argument, `$1` das zweite:
```swift
let add: (Int, Int) -> Int = { $0 + $1 }
print(add(2, 3)) // 5
```
Die Typen kommen weiterhin aus der Annotation `(Int, Int) -> Int`.

---

Da Closures Werte sind, kann eine Funktion eine als Parameter entgegennehmen. Der Parametertyp ist einfach der Funktionstyp:
```swift
func apply(_ n: Int, _ operation: (Int) -> Int) -> Int {
    return operation(n)
}
print(apply(5, { $0 + 1 })) // 6
```
Die Funktion `apply` weiß nicht, was `operation` tut, sie weiß nur, dass sie einen `Int` entgegennimmt und einen `Int` zurückgibt, und ruft sie wie jede andere Funktion auf.

---

Wenn eine Closure das **letzte** Argument einer Funktion ist, kannst du sie nach der schließenden Klammer des Aufrufs schreiben. Das ist die **Trailing-Closure**-Syntax:
```swift
print(apply(5) { $0 + 1 }) // 6
```
Wenn die Closure das einzige Argument ist, können die Klammern vollständig weggelassen werden:
```swift
func run(_ task: () -> Int) -> Int {
    return task()
}
print(run { 42 }) // 42
```
Beide Formen rufen genau dieselbe Funktion auf, die Trailing-Syntax ist nur leichter zu lesen, wenn die Closure lang ist.

---

Closures glänzen bei den Array-Methoden, die eine als Argument entgegennehmen. `map` ruft die Closure auf jedem Element auf und gibt ein neues Array mit den Ergebnissen zurück:
```swift
let nums = [1, 2, 3]
let doubled = nums.map { $0 * 2 }
print(doubled) // [2, 4, 6]
```
Das ursprüngliche Array wird nicht verändert. Da `map` ein einzelnes Closure-Argument entgegennimmt, ist die Trailing-Closure-Syntax die übliche Art, es aufzurufen.

---

`filter` behält nur die Elemente, für die die Closure `true` zurückgibt. Die Closure erhält ein Element und muss einen `Bool` zurückgeben:
```swift
let nums = [5, 12, 8, 20]
let big = nums.filter { $0 > 10 }
print(big) // [12, 20]
```
Die Elemente behalten ihre ursprüngliche Reihenfolge, und das Ergebnis ist ein neues Array desselben Elementtyps.

---

`reduce` kombiniert alle Elemente zu einem einzigen Wert. Es nimmt einen Anfangswert und eine Closure mit zwei Argumenten entgegen: den bisher akkumulierten Wert und das aktuelle Element. Die Closure gibt den neuen akkumulierten Wert zurück:
```swift
let nums = [1, 2, 3, 4]
let product = nums.reduce(1) { $0 * $1 }
print(product) // 24
```
Hier beginnt `$0` als `1`, wird dann zu `1 * 1`, `1 * 2`, `2 * 3` und schließlich `6 * 4`.
Da `map`, `filter` und `reduce` alle Werte zurückgeben, können sie verkettet werden: `nums.filter { $0 > 1 }.map { $0 * 10 }`.

---

`sorted(by:)` gibt ein neues sortiertes Array zurück. Die Closure erhält zwei Elemente und gibt `true` zurück, wenn das erste **vor** dem zweiten stehen soll:
```swift
let nums = [3, 1, 2]
print(nums.sorted { $0 < $1 }) // [1, 2, 3]
print(nums.sorted { $0 > $1 }) // [3, 2, 1]
```
Die Closure kann alles Mögliche vergleichen, zum Beispiel ordnet `words.sorted { $0.count < $1.count }` Strings von der kürzesten zur längsten.
