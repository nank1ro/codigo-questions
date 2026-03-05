---
language: kotlin
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Ihre Aufgabe ist es, eine Zahl in eine Zeichenkette umzuwandeln, die Regentropfengeräusche für bestimmte mögliche Faktoren enthält.
Ein Faktor ist eine Zahl, die eine andere Zahl ohne Rest teilt.
Die einfachste Möglichkeit, zu testen, ob eine Zahl ein Faktor ist, ist die Verwendung der Modulo-Operation.
Die Regeln für Regentropfen besagen, dass wenn eine Zahl:

- 3 als Faktor hat, 'Pling' zum Ergebnis hinzufügen.
- 5 als Faktor hat, 'Plang' zum Ergebnis hinzufügen.
- 7 als Faktor hat, 'Plong' zum Ergebnis hinzufügen.
- keinen der Faktoren 3, 5 oder 7 hat, sollte das Ergebnis die Ziffern der Zahl sein.

# --instructions--

Schreiben Sie eine Funktion, die die korrekte Zeichenkette zurückgibt. Beispiele:

- 28 hat 7 als Faktor, aber nicht 3 oder 5, daher wäre das Ergebnis `"Plong"`.
- 30 hat 3 und 5 als Faktoren, aber nicht 7, daher wäre das Ergebnis `"PlingPlang"`.
- 34 hat keinen der Faktoren 3, 5 oder 7, daher wäre das Ergebnis `"34"`.

Beispiel für einen Funktionsaufruf:
```kotlin
println(raindrops(28))
// gibt "Plong" aus
```

# --seed--

```kotlin
fun raindrops(): String {
    
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

Der Ton für 1 ist "1".

```kotlin
    tryCatch(raindrops(1) == "1")
```

Der Ton für 3 ist "Pling".

```kotlin
    tryCatch(raindrops(3) == "Pling")
```

Der Ton für 5 ist "Plang".

```kotlin
    tryCatch(raindrops(5) == "Plang")
```

Der Ton für 7 ist "Plong".

```kotlin
    tryCatch(raindrops(7) == "Plong")
```

Der Ton für 6 ist "Pling".

```kotlin
    tryCatch(raindrops(6) == "Pling")
```

Der Ton für 8 ist "8".

```kotlin
    tryCatch(raindrops(8) == "8")
```

Der Ton für 9 ist "Pling".

```kotlin
    tryCatch(raindrops(9) == "Pling")
```

Der Ton für 10 ist "Plang".

```kotlin
    tryCatch(raindrops(10) == "Plang")
```

Der Ton für 14 ist "Plong".

```kotlin
    tryCatch(raindrops(14) == "Plong")
```

Der Ton für 15 ist "PlingPlang".

```kotlin
    tryCatch(raindrops(15) == "PlingPlang")
```

Der Ton für 21 ist "PlingPlong".

```kotlin
    tryCatch(raindrops(21) == "PlingPlong")
```

Der Ton für 25 ist "Plang".

```kotlin
    tryCatch(raindrops(25) == "Plang")
```

Der Ton für 27 ist "Pling".

```kotlin
    tryCatch(raindrops(27) == "Pling")
```

Der Ton für 35 ist "PlangPlong".

```kotlin
    tryCatch(raindrops(35) == "PlangPlong")
```

Der Ton für 49 ist "Plong".

```kotlin
    tryCatch(raindrops(49) == "Plong")
```

Der Ton für 52 ist "52".

```kotlin
    tryCatch(raindrops(52) == "52")
```

Der Ton für 105 ist "PlingPlangPlong".

```kotlin
    tryCatch(raindrops(105) == "PlingPlangPlong")
```

Der Ton für 3125 ist "Plang".

```kotlin
    tryCatch(raindrops(3125) == "Plang")
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
fun raindrops(num: Int): String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty()) {
        result = num.toString()     
    }
    return result
}
```
