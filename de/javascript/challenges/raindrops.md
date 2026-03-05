---
language: javascript
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Ihre Aufgabe ist es, eine Zahl in einen String umzuwandeln, der Regengeräusche enthält, die bestimmten möglichen Faktoren entsprechen.
Ein Faktor ist eine Zahl, die eine andere Zahl gleichmäßig teilt, ohne Rest zu hinterlassen.
Der einfachste Weg, um zu testen, ob eine Zahl ein Faktor einer anderen ist, ist die Verwendung der Modulo-Operation.
Die Regeln des Regendrops sind wie folgt:

- hat 3 als Faktor, füge 'Pling' zum Ergebnis hinzu.
- hat 5 als Faktor, füge 'Plang' zum Ergebnis hinzu.
- hat 7 als Faktor, füge 'Plong' zum Ergebnis hinzu.
- hat keinen von 3, 5 oder 7 als Faktor, sollte das Ergebnis die Ziffern der Zahl sein.

# --instructions--

Schreiben Sie eine Funktion, die den korrekten String zurückgibt, Beispiele:

- 28 hat 7 als Faktor, aber nicht 3 oder 5, daher wäre das Ergebnis `"Plong"`.
- 30 hat sowohl 3 als auch 5 als Faktoren, aber nicht 7, daher wäre das Ergebnis `"PlingPlang"`.
- 34 wird nicht durch 3, 5 oder 7 faktorisiert, daher wäre das Ergebnis `"34"`.

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

Der Ton für 1 ist "1"

```javascript
tryCatch(convert(1) === "1");
```

Der Ton für 3 ist "Pling"

```javascript
tryCatch(convert(3) === "Pling");
```

Der Ton für 5 ist "Plang"

```javascript
tryCatch(convert(5) === "Plang");
```

Der Ton für 7 ist "Plong"

```javascript
tryCatch(convert(7) === "Plong");
```

Der Ton für 6 ist "Pling"

```javascript
tryCatch(convert(6) === "Pling");
```

Der Ton für 8 ist "8"

```javascript
tryCatch(convert(8) === "8");
```

Der Ton für 9 ist "Pling"

```javascript
tryCatch(convert(9) === "Pling");
```

Der Ton für 10 ist "Plang"

```javascript
tryCatch(convert(10) === "Plang");
```

Der Ton für 14 ist "Plong"

```javascript
tryCatch(convert(14) === "Plong");
```

Der Ton für 15 ist "PlingPlang"

```javascript
tryCatch(convert(15) === "PlingPlang");
```

Der Ton für 21 ist "PlingPlong"

```javascript
tryCatch(convert(21) === "PlingPlong");
```

Der Ton für 25 ist "Plang"

```javascript
tryCatch(convert(25) === "Plang");
```

Der Ton für 27 ist "Pling"

```javascript
tryCatch(convert(27) === "Pling");
```

Der Ton für 35 ist "PlangPlong"

```javascript
tryCatch(convert(35) === "PlangPlong");
```

Der Ton für 49 ist "Plong"

```javascript
tryCatch(convert(49) === "Plong");
```

Der Ton für 52 ist "52"

```javascript
tryCatch(convert(52) === "52");
```

Der Ton für 105 ist "PlingPlangPlong"

```javascript
tryCatch(convert(105) === "PlingPlangPlong");
```

Der Ton für 3125 ist "Plang"

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
