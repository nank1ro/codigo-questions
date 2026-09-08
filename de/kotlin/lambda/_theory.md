Ein **Lambda** ist eine kleine Funktion ohne Namen, die direkt als Ausdruck zwischen geschweiften Klammern geschrieben wird.
Zuerst kommen die Parameter, dann ein Pfeil `->`, dann der Rumpf:
```kotlin
val add = { a: Int, b: Int -> a + b }
```
Ein Lambda ist ein Wert wie jeder andere: Sie können es in einer Variable speichern und später mit Klammern aufrufen, genau wie eine Funktion:
```kotlin
println(add(2, 3)) // 5
```
Ein Lambda ohne Parameter hat überhaupt keinen Pfeil: `val hello = { println("Hello!") }`.

---

Jedes Lambda hat einen **Funktionstyp**, geschrieben als die Parametertypen in Klammern, ein Pfeil und der Rückgabetyp.
Das Lambda `{ a: Int, b: Int -> a + b }` hat den Typ `(Int, Int) -> Int`: Es nimmt zwei `Int`-Werte entgegen und gibt ein `Int` zurück.
Wenn Sie den Funktionstyp bei der Variable deklarieren, können die Parametertypen innerhalb des Lambdas weggelassen werden, weil der Compiler sie bereits kennt:
```kotlin
val add: (Int, Int) -> Int = { a, b -> a + b }
val greet: (String) -> Unit = { name -> println("Hi, $name") }
```
Ein Lambda, das nichts zurückgibt, hat den Rückgabetyp `Unit`.

---

Der Rumpf eines Lambdas kann sich über mehrere Zeilen erstrecken. Es gibt kein `return`-Schlüsselwort: Der Wert des **letzten Ausdrucks** ist das, was das Lambda zurückgibt.
```kotlin
val describe: (Int) -> String = { n ->
    val half = n / 2
    "half of $n is $half" // returned
}
println(describe(10)) // half of 10 is 5
```
Da `if` in Kotlin ein Ausdruck ist, kann es die letzte Zeile sein und das Ergebnis bestimmen:
```kotlin
val parity: (Int) -> String = { n -> if (n % 2 == 0) "even" else "odd" }
```

---

Wenn ein Lambda genau **einen** Parameter hat, können Sie auf dessen Deklaration verzichten: Kotlin nennt ihn für Sie `it`.
```kotlin
// val double: (Int) -> Int = { n -> n * 2 }
val double: (Int) -> Int = { it * 2 } // same thing
```
`it` existiert nur, wenn der Parameter nicht explizit deklariert ist, und nur für Lambdas mit einem einzigen Parameter.
Es hält kurze Lambdas kompakt, aber bei längeren Rümpfen ist ein echter Name klarer.

---

Lambdas werden meistens als Argumente anderer Funktionen verwendet. Sammlungen bieten viele Funktionen, die ein Lambda entgegennehmen:
- `forEach` führt das Lambda einmal für jedes Element aus
- `map` baut eine neue Liste mit dem Ergebnis des Lambdas für jedes Element
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map({ it * 2 }) // [2, 4, 6]
```
Wenn das Lambda das **letzte** Argument ist, können Sie es außerhalb der Klammern verschieben; ist es das einzige Argument, können die Klammern ganz entfallen. Das nennt sich **Trailing-Lambda**-Syntax und ist die übliche Schreibweise:
```kotlin
val doubled = numbers.map { it * 2 }
doubled.forEach { println(it) }
```

---

Ein Lambda, das ein `Boolean` zurückgibt, wird **Prädikat** genannt. Mehrere Sammlungsfunktionen nehmen eines entgegen:
- `filter` behält nur die Elemente, für die das Prädikat `true` ist
- `count` gibt zurück, wie viele Elemente es erfüllen
- `any` und `all` sagen, ob einige oder alle Elemente es erfüllen
```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6)
println(numbers.filter { it % 2 == 0 }) // [2, 4, 6]
println(numbers.count { it > 4 })        // 2
println(numbers.any { it > 5 })          // true
```
Aufrufe können **verkettet** werden: Jede Funktion gibt eine neue Liste zurück, mit der die nächste arbeitet.
```kotlin
println(numbers.filter { it % 2 == 0 }.map { it * 10 }) // [20, 40, 60]
```

---

Lambdas treiben auch Sortierung und Aggregation an:
- `sortedBy` gibt eine neue Liste zurück, geordnet nach dem Wert, den das Lambda für jedes Element berechnet; `sortedByDescending` macht das Gegenteil
- `reduce` kombiniert alle Elemente zu einem einzigen Wert: Das Lambda erhält das bisher angesammelte Ergebnis und das nächste Element
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })          // [fig, kiwi, banana]
println(words.sortedByDescending { it.length }) // [banana, kiwi, fig]

val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n })   // 10
```
`reduce` beginnt mit dem ersten Element als `acc` und führt dann das Lambda für jedes verbleibende Element aus.

---

Mit `reduce` ist die Form des Ergebnisses dem Lambda überlassen. Jede Operation, die zwei Werte kombiniert, funktioniert: eine Summe, ein Produkt oder das Beibehalten des größeren der beiden.
```kotlin
val numbers = listOf(3, 9, 4)
println(numbers.reduce { acc, n -> if (n > acc) n else acc }) // 9
```
Beachten Sie, dass `reduce` bei einer leeren Liste eine Ausnahme auslöst, weil es kein erstes Element als Startpunkt gibt.

---

Ein Lambda kann die Variablen verwenden, die in seiner Umgebung deklariert wurden, sogar nachdem der umgebende Code bereits abgelaufen ist. Das nennt sich eine **Closure**: Das Lambda erfasst die Variablen, die es benötigt.
Anders als in vielen anderen Sprachen erlaubt Kotlin einem Lambda, eine erfasste `var` zu **ändern**:
```kotlin
var clicks = 0
val onClick = { clicks++ }
onClick()
onClick()
println(clicks) // 2
```
Jeder Aufruf von `onClick` aktualisiert dieselbe Variable `clicks`, die auch der äußere Code sieht.

---

Da ein Lambda ein Wert ist, kann eine Funktion auch eines **zurückgeben**. Der Rückgabetyp ist ein Funktionstyp:
```kotlin
fun multiplier(factor: Int): (Int) -> Int {
    return { it * factor }
}
val triple = multiplier(3)
println(triple(5)) // 15
```
Das zurückgegebene Lambda erfasst `factor`, daher baut jeder Aufruf von `multiplier` eine andere Funktion.
Funktionen, die andere Funktionen entgegennehmen oder zurückgeben, werden **Funktionen höherer Ordnung** genannt.

---

Ein zurückgegebenes Lambda kann eine `var` erfassen, die innerhalb der Funktion deklariert wurde. Diese Variable lebt weiter, nachdem die Funktion zurückgekehrt ist, und nur das Lambda kann auf sie zugreifen: Sie ist privater Zustand.
```kotlin
fun makeGreeter(): () -> String {
    var calls = 0
    return { calls++; "hello #$calls" }
}
val greeter = makeGreeter()
println(greeter()) // hello #1
println(greeter()) // hello #2
```
Jeder Aufruf von `makeGreeter()` deklariert ein neues `calls`, daher zählen zwei Greeter unabhängig voneinander.

---

Sie können Ihre eigenen Funktionen höherer Ordnung schreiben: Ein Parameter mit einem Funktionstyp akzeptiert jedes Lambda dieser Form, und innerhalb der Funktion rufen Sie es wie eine gewöhnliche Funktion auf.
```kotlin
fun repeatTwice(text: String, transform: (String) -> String): String {
    return transform(transform(text))
}
println(repeatTwice("a", { it + "!" })) // a!!
println(repeatTwice("a") { it + "!" })  // same, with a trailing lambda
```
Dass der Funktionsparameter **zuletzt** steht, ist genau das, was den Aufrufern die Trailing-Lambda-Syntax ermöglicht.

---

Wenn die Funktion, die Sie benötigen, bereits existiert, müssen Sie sie nicht in ein Lambda verpacken: Eine **Funktionsreferenz** `::name` macht aus einer benannten Funktion einen Wert mit dem passenden Funktionstyp.
```kotlin
fun isEven(n: Int) = n % 2 == 0
val numbers = listOf(1, 2, 3, 4)
println(numbers.filter { isEven(it) }) // [2, 4]
println(numbers.filter(::isEven))      // [2, 4], same thing
```
Member-Funktionen werden über ihren Typ referenziert, wie `String::uppercase`:
```kotlin
println(listOf("a", "b").map(String::uppercase)) // [A, B]
```

---

Eine **anonyme Funktion** ist eine Funktion, die mit `fun` deklariert wird, aber ohne Namen. Sie ist eine weitere Möglichkeit, einen Funktionswert zu erstellen:
```kotlin
val square = fun(x: Int): Int {
    return x * x
}
println(square(4)) // 16
```
Anders als ein Lambda kann sie ihren Rückgabetyp explizit deklarieren, und sie verwendet `return`, um den Wert zu erzeugen.
Anonyme Funktionen und Lambdas sind austauschbar: Beide können an `map`, `filter` oder jede Funktion übergeben werden, die einen Funktionstyp entgegennimmt.

---

Funktionen höherer Ordnung können Funktionen sowohl entgegennehmen als auch zurückgeben. Ein klassisches Beispiel ist **Komposition**: der Aufbau einer neuen Funktion, die eine Funktion ausführt und ihr Ergebnis in eine weitere einspeist.
```kotlin
fun andThen(first: (Int) -> Int, second: (Int) -> Int): (Int) -> Int {
    return { n -> second(first(n)) }
}
val addOneThenDouble = andThen({ it + 1 }, { it * 2 })
println(addOneThenDouble(3)) // 8
```
Das zurückgegebene Lambda erfasst sowohl `first` als auch `second`, daher arbeitet es noch lange weiter, nachdem `andThen` zurückgekehrt ist.

---

Einige Funktionen nehmen ein **Lambda mit Receiver** entgegen: Innerhalb des Lambdas ist `this` ein bestimmtes Objekt, sodass Sie dessen Member direkt aufrufen können, ohne es zu benennen.
`buildString` ist ein häufiges Beispiel: Innerhalb seines Lambdas ist `this` ein `StringBuilder`, sodass `append` aufgerufen werden kann, als wäre es eine lokale Funktion:
```kotlin
val text = buildString {
    append("Hello")
    append(", ")
    append("world")
}
println(text) // Hello, world
```
`buildString` gibt den fertigen String zurück. Es ist eine bequeme Alternative zum Verketten mit `+` in einer Schleife.
