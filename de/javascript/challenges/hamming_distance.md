---
language: javascript
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

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
var assert = require('assert')
const tryCatch = (...args) => {
  _testCount++
  try { assert(...args) }
  catch (e) {
    _testFailedCount++
    console.log(`Test Case '--err-t${_testCount}--' failed`);
  }
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function hammingDistance(left, right) {
  
}
```

# --asserts--

Zwei leere Stränge unterscheiden sich nirgends

```javascript
tryCatch(hammingDistance("", "") === 0);
```

Zwei identische Stränge aus einem einzelnen Nukleotid haben keinen Unterschied

```javascript
tryCatch(hammingDistance("A", "A") === 0);
```

Zwei unterschiedliche Stränge aus einem einzelnen Nukleotid unterscheiden sich an einer Position

```javascript
tryCatch(hammingDistance("A", "G") === 1);
```

Zwei kurze Stränge, die sich an jeder Position unterscheiden

```javascript
tryCatch(hammingDistance("AG", "CT") === 2);
```

Zwei kurze Stränge, die sich nur an der ersten Position unterscheiden

```javascript
tryCatch(hammingDistance("AT", "CT") === 1);
```

Ein einzelnes abweichendes Nukleotid in der Mitte der Stränge

```javascript
tryCatch(hammingDistance("GGACG", "GGTCG") === 1);
```

Dieselben Nukleotide an anderen Positionen zählen weiterhin als Unterschiede

```javascript
tryCatch(hammingDistance("TAG", "GAT") === 2);
```

Ein längeres Paar von Strängen mit vier Unterschieden

```javascript
tryCatch(hammingDistance("GATACA", "GCATAA") === 4);
```

Das Verschieben eines Strangs um eine Position bewirkt, dass sich fast jede Position unterscheidet

```javascript
tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") === 9);
```

Die beiden Stränge aus der Beschreibung haben einen Abstand von sieben

```javascript
tryCatch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") === 7);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function hammingDistance(left, right) {
  let distance = 0;

  for (let i = 0; i < left.length; i++) {
    if (left[i] !== right[i]) {
      distance++;
    }
  }

  return distance;
}
```