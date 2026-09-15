---
language: kotlin
exerciseType: 1
difficulty: 2
title: Bubblesort
---

# --description--

Bubblesort ist einer der einfachsten Sortieralgorithmen. Er durchläuft eine Liste und vergleicht jedes Paar benachbarter Elemente, wobei er sie vertauscht, sobald sie in der falschen Reihenfolge stehen. Nach jedem vollständigen Durchlauf ist der größte verbleibende Wert an seine endgültige Position „aufgestiegen“, und die Liste ist sortiert, sobald ein Durchlauf ohne einen einzigen Tausch endet.

# --instructions--

Schreiben Sie eine Funktion namens `bubbleSort`, die eine `List<Int>` entgegennimmt und eine **neue** Liste mit denselben Werten in aufsteigender Reihenfolge zurückgibt. Die übergebene Liste darf nicht verändert werden.

Sie müssen den Bubblesort-Algorithmus selbst implementieren, indem Sie benachbarte Elemente vergleichen und vertauschen. Verwenden Sie keine Sortierfunktion aus der Standardbibliothek.

Ihre Funktion muss auch mit einem leeren Array, einem Array mit einem einzigen Element, einem bereits sortierten Array, wiederholten Werten und negativen Zahlen funktionieren.

Beispiel eines Funktionsaufrufs:
```kotlin
println(bubbleSort(listOf(3, 1, 2)))
// gibt [1, 2, 3] aus
```

# --seed--

```kotlin
fun bubbleSort(arr: List<Int>): List<Int> {
    
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

Ein leeres Array muss ein leeres Array zurückgeben

```kotlin
    tryCatch(bubbleSort(listOf<Int>()) == listOf<Int>())
```

Ein Array mit einem einzigen Element muss gleich bleiben

```kotlin
    tryCatch(bubbleSort(listOf<Int>(42)) == listOf<Int>(42))
```

Ein bereits sortiertes Array muss in derselben Reihenfolge bleiben

```kotlin
    tryCatch(bubbleSort(listOf<Int>(1, 2, 3, 4, 5)) == listOf<Int>(1, 2, 3, 4, 5))
```

Ein absteigend sortiertes Array muss in aufsteigende Reihenfolge gebracht werden

```kotlin
    tryCatch(bubbleSort(listOf<Int>(5, 4, 3, 2, 1)) == listOf<Int>(1, 2, 3, 4, 5))
```

Wiederholte Werte müssen alle erhalten bleiben

```kotlin
    tryCatch(bubbleSort(listOf<Int>(3, 1, 3, 2, 1)) == listOf<Int>(1, 1, 2, 3, 3))
```

Negative Zahlen müssen vor den positiven sortiert werden

```kotlin
    tryCatch(bubbleSort(listOf<Int>(-5, 3, -1, 0, -9)) == listOf<Int>(-9, -5, -1, 0, 3))
```

Ein längeres gemischtes Array muss in aufsteigender Reihenfolge sortiert werden

```kotlin
    tryCatch(bubbleSort(listOf<Int>(9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6)) == listOf<Int>(-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14))
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
fun bubbleSort(arr: List<Int>): List<Int> {
    val result = arr.toMutableList()
    var end = result.size
    var swapped = true
    while (swapped) {
        swapped = false
        for (i in 1 until end) {
            if (result[i - 1] > result[i]) {
                val temp = result[i - 1]
                result[i - 1] = result[i]
                result[i] = temp
                swapped = true
            }
        }
        end--
    }
    return result
}
```
