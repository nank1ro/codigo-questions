---
language: javascript
exerciseType: 1
difficulty: 3
title: Pasujące nawiasy
---

# --description--

Tekst zawierający kod, zapis matematyczny czy znaczniki jest pełen nawiasów, a każdy nawias otwierający potrzebuje nawiasu zamykającego tego samego rodzaju. Ciąg znaków jest zrównoważony, gdy jego nawiasy tworzą pary i zagnieżdżają się jak warstwy cebuli: `{[()]}` jest zrównoważony, natomiast `{[(])}` już nie, ponieważ para okrągła zostaje zamknięta przed parą kwadratową, wewnątrz której się znajduje.

Liczą się tutaj trzy pary: okrągła `()`, kwadratowa `[]` i klamrowa `{}`. Każdy inny znak w ciągu jest ignorowany. Nawias zamykający musi zamykać ostatnio otwarty nawias, który wciąż jest otwarty, a gdy ciąg się kończy, żaden nawias nie może pozostać otwarty.

# --instructions--

Napisz funkcję `isBalanced`, która przyjmuje ciąg znaków i zwraca `true`, gdy wszystkie zawarte w niej nawiasy są sparowane i poprawnie zagnieżdżone, a w przeciwnym razie zwraca `false`.

Przykłady:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- Pusty ciąg znaków jest zrównoważony.
- Znaki, które nie są nawiasami, są ignorowane.
- Nawias zamykający musi pasować do ostatnio otwartego nawiasu, który wciąż jest otwarty.
- Żaden nawias nie może pozostać otwarty, gdy ciąg znaków się kończy.

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
function isBalanced(text) {
  
}
```

# --asserts--

Pusty ciąg znaków jest zrównoważony

```javascript
tryCatch(isBalanced("") === true);
```

Pojedyncza para nawiasów okrągłych jest zrównoważona

```javascript
tryCatch(isBalanced("()") === true);
```

Trzy rodzaje par zagnieżdżone jeden w drugim są zrównoważone

```javascript
tryCatch(isBalanced("{[()]}") === true);
```

Nawiasy przeplatane innym tekstem nadal są zrównoważone

```javascript
tryCatch(isBalanced("{what is (42)}[?]") === true);
```

Pary ustawione obok siebie są zrównoważone

```javascript
tryCatch(isBalanced("()[]{}") === true);
```

Ciąg znaków bez żadnych nawiasów jest zrównoważony

```javascript
tryCatch(isBalanced("no brackets in here at all") === true);
```

Skrzyżowana para nawiasów nie jest zrównoważona

```javascript
tryCatch(isBalanced("{[(])}") === false);
```

Nawias otwierający, który nigdy nie zostaje zamknięty, nie jest zrównoważony

```javascript
tryCatch(isBalanced("(") === false);
```

Nawias zamykający pojawiający się przed jakimkolwiek nawiasem otwierającym nie jest zrównoważony

```javascript
tryCatch(isBalanced(")(") === false);
```

Skrzyżowane pary głębiej w ciągu znaków nie są zrównoważone

```javascript
tryCatch(isBalanced("(([]{[}]))") === false);
```

Nawias zamykający pozostawiony na końcu nie jest zrównoważony

```javascript
tryCatch(isBalanced("())") === false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isBalanced(text) {
  const pairs = { ")": "(", "]": "[", "}": "{" };
  const stack = [];

  for (const char of text) {
    if (char === "(" || char === "[" || char === "{") {
      stack.push(char);
    } else if (char in pairs) {
      if (stack.pop() !== pairs[char]) {
        return false;
      }
    }
  }

  return stack.length === 0;
}
```
