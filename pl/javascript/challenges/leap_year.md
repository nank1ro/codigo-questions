---
language: javascript
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

W roku kalendarzowym jest dokładnie 365,25 dnia. Jednak z czasem prowadziłoby to do zamieszania, ponieważ ludzie zazwyczaj liczą przy użyciu dokładnej podzielności przez 1, a nie z użyciem miejsc po przecinku. Aby tego uniknąć, postanowiono zsumować wszystkie 0,25 dnia w każdym cyklu czteroletnim i dać temu rokowi 366 dni (wliczając 29 lutego jako dzień przestępny) i nazwać go __rokiem przestępnym__. Pozostałe trzy lata w cyklu czteroletnim miałyby tylko 365 dni i __nie byłyby latami przestępnymi__.

# --instructions--

W tym wyzwaniu pójdziemy o krok dalej — musisz określić, czy dany rok jest przestępny, bez użycia klasy `Date`, instrukcji `switch`, __bloków if__, __bloków if-else__ ani __operatora trójargumentowego__ (`x ? a : b`), a także operatorów logicznych __AND__ (`&&`) i __OR__ (`||`), z wyjątkiem operatora __NOT__ (`!`).

Zwróć `true`, jeśli rok jest przestępny, w przeciwnym razie `false`.

Przykład wywołania funkcji:
```javascript
console.log(leapYear(2000));
// prints true
```

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
function leapYear(year) {
  
}
```

# --asserts--

Użycie `Date`, `switch`, `if`, `else`, `&&`, `||` lub `?` jest niedozwolone.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Rok `2016` jest rokiem przestępnym.

```javascript
tryCatch(leapYear(2016) == true);
```

Rok `1996` jest rokiem przestępnym.

```javascript
tryCatch(leapYear(1996) == true);
```

Rok `1600` jest rokiem przestępnym.

```javascript
tryCatch(leapYear(1600) == true);
```

Rok `2020` jest rokiem przestępnym.

```javascript
tryCatch(leapYear(2020) == true);
```

Rok `2000` jest rokiem przestępnym.

```javascript
tryCatch(leapYear(2000) == true);
```

Rok `2008` jest rokiem przestępnym.

```javascript
tryCatch(leapYear(2008) == true);
```

Rok `1521` nie jest rokiem przestępnym.

```javascript
tryCatch(leapYear(1521) == false);
```

Rok `1800` nie jest rokiem przestępnym.

```javascript
tryCatch(leapYear(1800) == false);
```

Rok `2007` nie jest rokiem przestępnym.

```javascript
tryCatch(leapYear(2007) == false);
```

Rok `2002` nie jest rokiem przestępnym.

```javascript
tryCatch(leapYear(2002) == false);
```

Rok `1979` nie jest rokiem przestępnym.

```javascript
tryCatch(leapYear(1979) == false);
```

Rok `2006` nie jest rokiem przestępnym.

```javascript
tryCatch(leapYear(2006) == false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function leapYear(year) {
  return (year % 4 === 0) ^ ((year % 100 === 0) & (year % 400 !== 0));
}
```

```javascript
function leapYear(year){
   while(year % 100 === 0) {
     year = year / 100;
   }
  return year % 4 === 0; 
}
```
