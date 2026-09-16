---
language: kotlin
exerciseType: 1
difficulty: 1
title: Distanza di Hamming
---

# --description--

Il DNA è scritto come un filamento di nucleotidi, ognuno dei quali è una singola lettera: `A`, `C`, `G` o `T`. Quando due filamenti della stessa lunghezza vengono affiancati, alcune posizioni contengono lo stesso nucleotide e altre ne contengono di diversi.

Il numero di posizioni in cui i due filamenti differiscono è chiamato distanza di Hamming, e i biologi lo usano per misurare quanto due filamenti si sono allontanati l'uno dall'altro. Affiancando `GAGCCTACTAACGGGAT` con `CATCGTAATGACGGCCT` si ottengono 7 posizioni che differiscono, quindi la loro distanza di Hamming è 7.

# --instructions--

Scrivi una funzione `hammingDistance` che riceve due filamenti di DNA della stessa lunghezza e restituisce il numero di posizioni in cui differiscono.

Esempi:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- I due filamenti hanno sempre la stessa lunghezza, quindi non devi mai gestire filamenti di lunghezza diversa.
- Due filamenti vuoti non differiscono in nessuna posizione, quindi la loro distanza è 0.

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

Due filamenti vuoti non differiscono in nessuna posizione

```kotlin
    tryCatch(hammingDistance("", "") == 0)
```

Due filamenti identici di un solo nucleotide non hanno differenze

```kotlin
    tryCatch(hammingDistance("A", "A") == 0)
```

Due filamenti di un solo nucleotide diversi differiscono in una posizione

```kotlin
    tryCatch(hammingDistance("A", "G") == 1)
```

Due filamenti brevi che differiscono in ogni posizione

```kotlin
    tryCatch(hammingDistance("AG", "CT") == 2)
```

Due filamenti brevi che differiscono solo nella prima posizione

```kotlin
    tryCatch(hammingDistance("AT", "CT") == 1)
```

Un singolo nucleotide diverso nel mezzo dei filamenti

```kotlin
    tryCatch(hammingDistance("GGACG", "GGTCG") == 1)
```

Gli stessi nucleotidi in posizioni diverse contano comunque come differenze

```kotlin
    tryCatch(hammingDistance("TAG", "GAT") == 2)
```

Una coppia di filamenti più lunga con quattro differenze

```kotlin
    tryCatch(hammingDistance("GATACA", "GCATAA") == 4)
```

Spostare un filamento di una posizione fa differire quasi ogni posizione

```kotlin
    tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9)
```

I due filamenti della descrizione hanno una distanza di sette

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
