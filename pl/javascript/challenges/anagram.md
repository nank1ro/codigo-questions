---
language: javascript
exerciseType: 1
difficulty: 2
title: Anagram
---

# --description--

Dwa słowa są anagramami, gdy jedno jest przestawieniem drugiego: używają dokładnie tych samych liter, a każda z nich występuje tę samą liczbę razy, tylko w innej kolejności. `listen` i `silent` są anagramami, podobnie jak `stone` i `tones`.

Słowo nigdy nie jest anagramem samego siebie. Jeśli oba słowa są dokładnie takie same, nic nie zostało przestawione, więc odpowiedź to `false`. Oba słowa są podane małymi literami i zawierają wyłącznie litery od `a` do `z`.

# --instructions--

Napisz funkcję `isAnagram`, która przyjmuje dwa słowa, `first` i `second`, i zwraca `true`, gdy jedno z nich jest anagramem drugiego, oraz `false` w przeciwnym razie.

Przykłady:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Dwa identyczne słowa nie są anagramami.
- Słowa o różnych długościach nigdy nie są anagramami.
- Każda litera musi występować tyle samo razy w obu słowach.

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
function isAnagram(first, second) {
  
}
```

# --asserts--

Słowa "listen" i "silent" są anagramami

```javascript
tryCatch(isAnagram("listen", "silent") === true);
```

Słowa "stone" i "tones" są anagramami

```javascript
tryCatch(isAnagram("stone", "tones") === true);
```

Słowo nie jest anagramem samego siebie

```javascript
tryCatch(isAnagram("stone", "stone") === false);
```

Słowa o różnych długościach nie są anagramami

```javascript
tryCatch(isAnagram("abc", "abcd") === false);
```

Te same litery w różnych ilościach nie tworzą anagramu

```javascript
tryCatch(isAnagram("aab", "abb") === false);
```

Słowa "anagram" i "nagaram" są anagramami

```javascript
tryCatch(isAnagram("anagram", "nagaram") === true);
```

Dwa słowa tej samej długości z różnymi literami nie są anagramami

```javascript
tryCatch(isAnagram("rat", "car") === false);
```

Dwa puste słowa są identyczne, więc nie są anagramami

```javascript
tryCatch(isAnagram("", "") === false);
```

Dwie różne pojedyncze litery nie są anagramami

```javascript
tryCatch(isAnagram("a", "b") === false);
```

Słowa "evil" i "vile" są anagramami

```javascript
tryCatch(isAnagram("evil", "vile") === true);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isAnagram(first, second) {
  if (first === second) {
    return false;
  }

  const sortLetters = (word) => word.split("").sort().join("");

  return sortLetters(first) === sortLetters(second);
}
```
