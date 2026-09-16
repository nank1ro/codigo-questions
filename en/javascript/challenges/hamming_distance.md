---
language: javascript
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

Two empty strands differ nowhere

```javascript
tryCatch(hammingDistance("", "") === 0);
```

Two identical single nucleotide strands have no difference

```javascript
tryCatch(hammingDistance("A", "A") === 0);
```

Two different single nucleotide strands differ in one position

```javascript
tryCatch(hammingDistance("A", "G") === 1);
```

Two short strands that differ in every position

```javascript
tryCatch(hammingDistance("AG", "CT") === 2);
```

Two short strands that differ in the first position only

```javascript
tryCatch(hammingDistance("AT", "CT") === 1);
```

A single differing nucleotide in the middle of the strands

```javascript
tryCatch(hammingDistance("GGACG", "GGTCG") === 1);
```

The same nucleotides in different positions still count as differences

```javascript
tryCatch(hammingDistance("TAG", "GAT") === 2);
```

A longer pair of strands with four differences

```javascript
tryCatch(hammingDistance("GATACA", "GCATAA") === 4);
```

Shifting a strand by one position makes almost every position differ

```javascript
tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") === 9);
```

The two strands from the description have a distance of seven

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
