---
language: kotlin
exerciseType: 1
difficulty: 1
title: Zwei für eins
---

# --description--

Geben Sie eine Zeichenkette mit der Nachricht zurück:
`Einer für X, einer für mich.`
Wobei `X` der angegebene Name ist.
Wenn der Name jedoch nicht angegeben ist, geben Sie die Zeichenkette zurück:
`Einer für dich, einer für mich.`

# --instructions--

Schreiben Sie eine Funktion, die die korrekte Zeichenkette zurückgibt. Beispiele:

**Eingabe**: `Walter`
**Ausgabe**: `Einer für Walter, einer für mich.`

**Eingabe**: `James`
**Ausgabe**: `Einer für James, einer für mich.`

**Eingabe**: `Martha`
**Ausgabe**: `Einer für Martha, einer für mich.`

# --seed--

```kotlin
fun twoForOne(): String {
    
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
```

# --asserts--

Kein Name angegeben

```kotlin
    tryCatch(twoForOne() == "One for you, one for me.")
```

Geben Sie "James" als Name ein.

```kotlin
    tryCatch(twoForOne(name = "James") == "One for James, one for me.")
```

Geben Sie "Martha" als Name ein.

```kotlin
    tryCatch(twoForOne(name = "Martha") == "One for Martha, one for me.")
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun twoForOne(name: String? = null): String {
    name?.let {
        return "One for $it, one for me."
    }
    return "One for you, one for me."
}
```


