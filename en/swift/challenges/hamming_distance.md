---
language: swift
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

> HINT: omit the argument labels with the `_` (underscore)

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

Two empty strands differ nowhere

```swift
tryCatch(hammingDistance("", "") == 0)
```

Two identical single nucleotide strands have no difference

```swift
tryCatch(hammingDistance("A", "A") == 0)
```

Two different single nucleotide strands differ in one position

```swift
tryCatch(hammingDistance("A", "G") == 1)
```

Two short strands that differ in every position

```swift
tryCatch(hammingDistance("AG", "CT") == 2)
```

Two short strands that differ in the first position only

```swift
tryCatch(hammingDistance("AT", "CT") == 1)
```

A single differing nucleotide in the middle of the strands

```swift
tryCatch(hammingDistance("GGACG", "GGTCG") == 1)
```

The same nucleotides in different positions still count as differences

```swift
tryCatch(hammingDistance("TAG", "GAT") == 2)
```

A longer pair of strands with four differences

```swift
tryCatch(hammingDistance("GATACA", "GCATAA") == 4)
```

Shifting a strand by one position makes almost every position differ

```swift
tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9)
```

The two strands from the description have a distance of seven

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
