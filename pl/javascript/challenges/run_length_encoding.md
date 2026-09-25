---
language: javascript
exerciseType: 1
difficulty: 2
title: Kodowanie RLE
---

# --description--

Kodowanie RLE (run-length encoding) to jedna z najstarszych sztuczek kompresji: zamiast zapisywać ten sam znak w kółko, zapisujesz, ile razy się powtarza, a następnie sam znak.

Faks skanujący w większości pustą stronę napotyka długie ciągi identycznych pikseli, więc rząd dwunastu `W` wędruje przez linię jako znacznie krótsze `12W`. Gdy jakiś znak pojawia się tylko raz, liczenie go niczego nie daje, więc jest on kopiowany samodzielnie.

# --instructions--

Napisz funkcję `encodeRun`, która przyjmuje ciąg znaków `text` i zwraca jego postać zakodowaną metodą RLE.

Każda seria tego samego znaku powtórzonego dwa lub więcej razy staje się długością serii zapisaną dziesiętnie, po której następuje ten znak. Seria o długości jeden jest kopiowana jako pojedynczy znak, bez liczby przed nim.

Przykłady:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- Tekst zawiera wyłącznie wielkie litery od `A` do `Z` oraz spacje.
- Seria dłuższa niż dziewięć znaków używa pełnej liczby dziesiętnej, więc dwanaście `W` daje `12W`, a nigdy `9W3W`.
- Spacje to zwykłe znaki: są liczone i kodowane dokładnie tak samo jak litery.
- Pusty ciąg znaków koduje się do pustego ciągu znaków.

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
function encodeRun(text) {
  
}
```

# --asserts--

Pusty ciąg znaków koduje się do pustego ciągu znaków

```javascript
tryCatch(encodeRun("") === "");
```

Pojedynczy znak jest kopiowany jako sam siebie

```javascript
tryCatch(encodeRun("A") === "A");
```

Ciąg znaków bez powtórzeń przechodzi bez zmian

```javascript
tryCatch(encodeRun("ABCDE") === "ABCDE");
```

Seria o długości dwa staje się liczbą, po której następuje znak

```javascript
tryCatch(encodeRun("AA") === "2A");
```

Mieszany przykład "AABCCCDEEEE" staje się "2AB3CD4E"

```javascript
tryCatch(encodeRun("AABCCCDEEEE") === "2AB3CD4E");
```

Seria dwunastu znaków używa pełnej liczby dziesiętnej, więc wynik zaczyna się od "12W"

```javascript
tryCatch(encodeRun("WWWWWWWWWWWWBWW") === "12WB2W");
```

Serie spacji są kodowane dokładnie tak samo jak serie liter

```javascript
tryCatch(encodeRun("  HI  ") === "2 HI2 ");
```

Seria dziesięciu znaków jest zapisywana jako "10A", a nigdy jako dwie krótsze serie

```javascript
tryCatch(encodeRun("AAAAAAAAAA") === "10A");
```

Naprzemiennie występujące pojedyncze znaki są wszystkie kopiowane jako sam siebie

```javascript
tryCatch(encodeRun("ABABAB") === "ABABAB");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function encodeRun(text) {
  let result = "";
  let i = 0;

  while (i < text.length) {
    let run = 1;
    while (i + run < text.length && text[i + run] === text[i]) {
      run++;
    }
    if (run > 1) {
      result += run;
    }
    result += text[i];
    i += run;
  }

  return result;
}
```
