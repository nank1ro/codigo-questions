---
language: javascript
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Twoim zadaniem jest przekształcenie liczby w ciąg znaków zawierający dźwięki kropelek deszczu odpowiadające określonym potencjalnym dzielelnikom.
Dzielnik to liczba, która dzieli inną liczbę bez reszty.
Najprostszym sposobem sprawdzenia, czy liczba jest dzielnikiem innej, jest użycie operacji modulo.
Zasady gry w krople deszczu są następujące:

- jeśli 3 jest dzielnikiem, dodaj 'Pling' do wyniku.
- jeśli 5 jest dzielnikiem, dodaj 'Plang' do wyniku.
- jeśli 7 jest dzielnikiem, dodaj 'Plong' do wyniku.
- jeśli żaden z 3, 5 ani 7 nie jest dzielnikiem, wynikiem powinny być cyfry danej liczby.

# --instructions--

Napisz funkcję, która zwraca poprawny ciąg znaków. Przykłady:

- 28 ma 7 jako dzielnik, ale nie 3 ani 5, więc wynikiem będzie `"Plong"`.
- 30 ma zarówno 3, jak i 5 jako dzielniki, ale nie 7, więc wynikiem będzie `"PlingPlang"`.
- 34 nie jest podzielne przez 3, 5 ani 7, więc wynikiem będzie `"34"`.

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
function convert(number) {
  
}
```

# --asserts--

Dźwięk dla 1 to "1"

```javascript
tryCatch(convert(1) === "1");
```

Dźwięk dla 3 to "Pling"

```javascript
tryCatch(convert(3) === "Pling");
```

Dźwięk dla 5 to "Plang"

```javascript
tryCatch(convert(5) === "Plang");
```

Dźwięk dla 7 to "Plong"

```javascript
tryCatch(convert(7) === "Plong");
```

Dźwięk dla 6 to "Pling"

```javascript
tryCatch(convert(6) === "Pling");
```

Dźwięk dla 8 to "8"

```javascript
tryCatch(convert(8) === "8");
```

Dźwięk dla 9 to "Pling"

```javascript
tryCatch(convert(9) === "Pling");
```

Dźwięk dla 10 to "Plang"

```javascript
tryCatch(convert(10) === "Plang");
```

Dźwięk dla 14 to "Plong"

```javascript
tryCatch(convert(14) === "Plong");
```

Dźwięk dla 15 to "PlingPlang"

```javascript
tryCatch(convert(15) === "PlingPlang");
```

Dźwięk dla 21 to "PlingPlong"

```javascript
tryCatch(convert(21) === "PlingPlong");
```

Dźwięk dla 25 to "Plang"

```javascript
tryCatch(convert(25) === "Plang");
```

Dźwięk dla 27 to "Pling"

```javascript
tryCatch(convert(27) === "Pling");
```

Dźwięk dla 35 to "PlangPlong"

```javascript
tryCatch(convert(35) === "PlangPlong");
```

Dźwięk dla 49 to "Plong"

```javascript
tryCatch(convert(49) === "Plong");
```

Dźwięk dla 52 to "52"

```javascript
tryCatch(convert(52) === "52");
```

Dźwięk dla 105 to "PlingPlangPlong"

```javascript
tryCatch(convert(105) === "PlingPlangPlong");
```

Dźwięk dla 3125 to "Plang"

```javascript
tryCatch(convert(3125) === "Plang");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function convert(number) {
  var result = ""
  if (number % 3 == 0) {
    result += "Pling"
  }
  if (number % 5 == 0) {
    result += "Plang"
  }
  if (number % 7 == 0) {
    result += "Plong"
  }
  if (!result) {
    result = number.toString()
  }
  return result
}
```
