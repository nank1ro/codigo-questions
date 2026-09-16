---
language: javascript
exerciseType: 1
difficulty: 1
title: Odległość Hamminga
---

# --description--

DNA zapisuje się jako nić nukleotydów, z których każdy jest pojedynczą literą: `A`, `C`, `G` lub `T`. Gdy dwie nici o tej samej długości ustawimy obok siebie, niektóre pozycje mają ten sam nukleotyd, a niektóre różne.

Liczba pozycji, w których dwie nici różnią się między sobą, nazywana jest odległością Hamminga, a biolodzy używają jej do mierzenia, jak bardzo dwie nici się od siebie oddaliły. Ustawienie `GAGCCTACTAACGGGAT` obok `CATCGTAATGACGGCCT` daje 7 różniących się pozycji, więc ich odległość Hamminga wynosi 7.

# --instructions--

Napisz funkcję `hammingDistance`, która przyjmuje dwie nici DNA o tej samej długości i zwraca liczbę pozycji, w których się różnią.

Przykłady:
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- Obie nici zawsze mają tę samą długość, więc nigdy nie musisz obsługiwać nici o różnych długościach.
- Dwie puste nici nie różnią się nigdzie, więc ich odległość wynosi 0.

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

Dwie puste nici nie różnią się nigdzie

```javascript
tryCatch(hammingDistance("", "") === 0);
```

Dwie identyczne nici z pojedynczym nukleotydem nie mają żadnej różnicy

```javascript
tryCatch(hammingDistance("A", "A") === 0);
```

Dwie różne nici z pojedynczym nukleotydem różnią się w jednej pozycji

```javascript
tryCatch(hammingDistance("A", "G") === 1);
```

Dwie krótkie nici różniące się w każdej pozycji

```javascript
tryCatch(hammingDistance("AG", "CT") === 2);
```

Dwie krótkie nici różniące się tylko w pierwszej pozycji

```javascript
tryCatch(hammingDistance("AT", "CT") === 1);
```

Pojedynczy różniący się nukleotyd w środku nici

```javascript
tryCatch(hammingDistance("GGACG", "GGTCG") === 1);
```

Te same nukleotydy w różnych pozycjach nadal liczą się jako różnice

```javascript
tryCatch(hammingDistance("TAG", "GAT") === 2);
```

Dłuższa para nici z czterema różnicami

```javascript
tryCatch(hammingDistance("GATACA", "GCATAA") === 4);
```

Przesunięcie nici o jedną pozycję powoduje, że prawie każda pozycja się różni

```javascript
tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") === 9);
```

Dwie nici z opisu mają odległość równą siedem

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
