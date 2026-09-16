---
language: kotlin
exerciseType: 1
difficulty: 1
title: Hamming-Abstand
---

# --description--

DNA wird als Strang von Nukleotiden geschrieben, jedes davon ein einzelner Buchstabe: `A`, `C`, `G` oder `T`. Werden zwei Stränge gleicher Länge Seite an Seite ausgerichtet, enthalten einige Positionen dasselbe Nukleotid und andere unterschiedliche.

Die Anzahl der Positionen, an denen sich die beiden Stränge unterscheiden, wird Hamming-Abstand genannt, und Biologen nutzen sie, um zu messen, wie weit zwei Stränge auseinandergegangen sind. Richtet man `GAGCCTACTAACGGGAT` mit `CATCGTAATGACGGCCT` aus, ergeben sich 7 Positionen mit Unterschieden, ihr Hamming-Abstand ist also 7.

# --instructions--

Schreiben Sie eine Funktion `hammingDistance`, die zwei DNA-Stränge gleicher Länge entgegennimmt und die Anzahl der Positionen zurückgibt, an denen sie sich unterscheiden.

Beispiele:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- Die beiden Stränge haben immer die gleiche Länge, Sie müssen also niemals Stränge unterschiedlicher Länge behandeln.
- Zwei leere Stränge unterscheiden sich nirgends, ihr Abstand ist also 0.

# --seed--

```kotlin
fun hammingDistance(left: String, right: String): Int {
    
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

Zwei leere Stränge unterscheiden sich nirgends

```kotlin
    tryCatch(hammingDistance("", "") == 0)
```

Zwei identische Stränge aus einem einzelnen Nukleotid haben keinen Unterschied

```kotlin
    tryCatch(hammingDistance("A", "A") == 0)
```

Zwei unterschiedliche Stränge aus einem einzelnen Nukleotid unterscheiden sich an einer Position

```kotlin
    tryCatch(hammingDistance("A", "G") == 1)
```

Zwei kurze Stränge, die sich an jeder Position unterscheiden

```kotlin
    tryCatch(hammingDistance("AG", "CT") == 2)
```

Zwei kurze Stränge, die sich nur an der ersten Position unterscheiden

```kotlin
    tryCatch(hammingDistance("AT", "CT") == 1)
```

Ein einzelnes abweichendes Nukleotid in der Mitte der Stränge

```kotlin
    tryCatch(hammingDistance("GGACG", "GGTCG") == 1)
```

Dieselben Nukleotide an anderen Positionen zählen weiterhin als Unterschiede

```kotlin
    tryCatch(hammingDistance("TAG", "GAT") == 2)
```

Ein längeres Paar von Strängen mit vier Unterschieden

```kotlin
    tryCatch(hammingDistance("GATACA", "GCATAA") == 4)
```

Das Verschieben eines Strangs um eine Position bewirkt, dass sich fast jede Position unterscheidet

```kotlin
    tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9)
```

Die beiden Stränge aus der Beschreibung haben einen Abstand von sieben

```kotlin
    tryCatch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7)
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
fun hammingDistance(left: String, right: String): Int {
    var distance = 0

    for (i in left.indices) {
        if (left[i] != right[i]) {
            distance++
        }
    }

    return distance
}
```