Eine Funktion ist ein Codeblock, der eine bestimmte Aufgabe ausführt und im gesamten Programm wiederverwendet werden kann.
In Kotlin definiert man eine Funktion mit dem Schlüsselwort `fun`, gefolgt vom Funktionsnamen und Klammern:
```kotlin
fun greet() {
    println("Hello!")
}
```
Um eine Funktion aufzurufen (auszuführen), verwendet man ihren Namen gefolgt von Klammern:
```kotlin
greet() // prints Hello!
```
Eine Funktion, die keinen Wert zurückgibt, gibt implizit `Unit` zurück.

---

Funktionen können einen Wert zurückgeben. Den Rückgabetyp gibt man nach den Klammern mit einem Doppelpunkt an:
```kotlin
fun getNumber(): Int {
    return 42
}
```
Das Schlüsselwort `return` sendet einen Wert zurück an den Aufrufer:
```kotlin
var result = getNumber()
println(result) // prints 42
```
Der Rückgabetyp muss mit dem Typ des zurückgegebenen Wertes übereinstimmen.

---

Funktionen können Parameter akzeptieren, also Eingaben, die beim Aufruf der Funktion übergeben werden.
Parameter werden innerhalb der Klammern mit einem Namen und einem Typ deklariert:
```kotlin
fun greet(name: String) {
    println("Hello, $name!")
}
```
Beim Aufruf der Funktion übergibt man Argumente:
```kotlin
greet("Alice") // prints Hello, Alice!
```
Parameter ermöglichen wiederverwendbaren Code, der mit verschiedenen Werten arbeitet.

---

Kotlin unterstützt Standardparameterwerte. Wenn ein Aufrufer kein Argument angibt, wird der Standardwert verwendet:
```kotlin
fun greet(name: String = "World") {
    println("Hello, $name!")
}
greet()         // prints Hello, World!
greet("Alice")  // prints Hello, Alice!
```
Standardwerte machen Parameter optional und reduzieren die Notwendigkeit von überladenen Funktionen.

---

Wenn ein Funktionskörper aus einem einzigen Ausdruck besteht, kann man die Einzelausdrucks-Syntax mit `=` verwenden:
```kotlin
fun square(n: Int): Int = n * n
```
Dies ist kompakter als die Blockkörper-Form. Kotlin kann den Rückgabetyp oft ableiten, sodass man auch schreiben kann:
```kotlin
fun square(n: Int) = n * n
```
Einzelausdrucks-Funktionen sind ein gängiges Kotlin-Idiom für einfache Berechnungen.

---

Funktionen können `Boolean`-Werte zurückgeben, was nützlich ist, um Bedingungen zu prüfen:
```kotlin
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
println(isEven(4)) // prints true
println(isEven(7)) // prints false
```
Eine `Boolean`-Funktion gibt entweder `true` oder `false` zurück.

---

Funktionen können mehrere Parameter verschiedener Typen haben:
```kotlin
fun introduce(name: String, age: Int): String {
    return "My name is $name and I am $age years old."
}
println(introduce("Bob", 30))
// prints My name is Bob and I am 30 years old.
```
Benannte Argumente ermöglichen es, Werte in beliebiger Reihenfolge mit dem Parameternamen zu übergeben:
```kotlin
println(introduce(age = 30, name = "Bob"))
```

---

Eine einfache Funktion in Kotlin verwendet das Schlüsselwort `fun`, gefolgt von einem Namen und Klammern:
```kotlin
fun sayBye() {
    println("Bye!")
}
```

---

Um einen Rückgabetyp für eine Funktion zu deklarieren, fügt man nach den Klammern einen Doppelpunkt und den Typ hinzu:
```kotlin
fun getName(): String {
    return "Alice"
}
```

---

Ein Funktionsparameter wird mit einem Namen, einem Doppelpunkt und einem Typ deklariert:
```kotlin
fun greet(name: String) {
    println("Hi, $name!")
}
```

---

Eine Einzelausdrucks-Funktion verwendet `=` anstatt eines Blockkörpers:
```kotlin
fun triple(n: Int) = n * 3
```
Dies ist eine Kurzform für:
```kotlin
fun triple(n: Int): Int {
    return n * 3
}
```
