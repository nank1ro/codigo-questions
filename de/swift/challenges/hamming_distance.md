---
language: swift
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

> HINWEIS: Lassen Sie die Argumentbezeichnungen mit dem `_` (Unterstrich) weg

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func hammingDistance(_ left: String, _ right: String) -> Int {
    
}
```

# --asserts--

Zwei leere Stränge unterscheiden sich nirgends

```swift
tryCatch(hammingDistance("", "") == 0)
```

Zwei identische Stränge aus einem einzelnen Nukleotid haben keinen Unterschied

```swift
tryCatch(hammingDistance("A", "A") == 0)
```

Zwei unterschiedliche Stränge aus einem einzelnen Nukleotid unterscheiden sich an einer Position

```swift
tryCatch(hammingDistance("A", "G") == 1)
```

Zwei kurze Stränge, die sich an jeder Position unterscheiden

```swift
tryCatch(hammingDistance("AG", "CT") == 2)
```

Zwei kurze Stränge, die sich nur an der ersten Position unterscheiden

```swift
tryCatch(hammingDistance("AT", "CT") == 1)
```

Ein einzelnes abweichendes Nukleotid in der Mitte der Stränge

```swift
tryCatch(hammingDistance("GGACG", "GGTCG") == 1)
```

Dieselben Nukleotide an anderen Positionen zählen weiterhin als Unterschiede

```swift
tryCatch(hammingDistance("TAG", "GAT") == 2)
```

Ein längeres Paar von Strängen mit vier Unterschieden

```swift
tryCatch(hammingDistance("GATACA", "GCATAA") == 4)
```

Das Verschieben eines Strangs um eine Position bewirkt, dass sich fast jede Position unterscheidet

```swift
tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9)
```

Die beiden Stränge aus der Beschreibung haben einen Abstand von sieben

```swift
tryCatch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func hammingDistance(_ left: String, _ right: String) -> Int {
    var distance = 0

    for (leftNucleotide, rightNucleotide) in zip(left, right) {
        if leftNucleotide != rightNucleotide {
            distance += 1
        }
    }

    return distance
}
```