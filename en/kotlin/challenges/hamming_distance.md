---
language: kotlin
exerciseType: 1
difficulty: 1
title: Hamming distance
---

# --description--

DNA is written as a strand of nucleotides, each one a single letter: `A`, `C`, `G` or `T`. When two strands of the same length are lined up side by side, some positions hold the same nucleotide and some hold different ones.

The number of positions where the two strands differ is called the Hamming distance, and biologists use it to measure how far two strands have drifted apart. Lining up `GAGCCTACTAACGGGAT` with `CATCGTAATGACGGCCT` gives 7 positions that differ, so their Hamming distance is 7.

# --instructions--

Write a function `hammingDistance` that takes two DNA strands of the same length and returns the number of positions where they differ.

Examples:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- The two strands always have the same length, so you never have to handle strands of different lengths.
- Two empty strands differ nowhere, so their distance is 0.

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

Two empty strands differ nowhere

```kotlin
    tryCatch(hammingDistance("", "") == 0)
```

Two identical single nucleotide strands have no difference

```kotlin
    tryCatch(hammingDistance("A", "A") == 0)
```

Two different single nucleotide strands differ in one position

```kotlin
    tryCatch(hammingDistance("A", "G") == 1)
```

Two short strands that differ in every position

```kotlin
    tryCatch(hammingDistance("AG", "CT") == 2)
```

Two short strands that differ in the first position only

```kotlin
    tryCatch(hammingDistance("AT", "CT") == 1)
```

A single differing nucleotide in the middle of the strands

```kotlin
    tryCatch(hammingDistance("GGACG", "GGTCG") == 1)
```

The same nucleotides in different positions still count as differences

```kotlin
    tryCatch(hammingDistance("TAG", "GAT") == 2)
```

A longer pair of strands with four differences

```kotlin
    tryCatch(hammingDistance("GATACA", "GCATAA") == 4)
```

Shifting a strand by one position makes almost every position differ

```kotlin
    tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9)
```

The two strands from the description have a distance of seven

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
