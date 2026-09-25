---
language: javascript
exerciseType: 1
difficulty: 2
title: Uhr
---

# --description--

Eine 24-Stunden-Uhr zeigt die Tageszeit als `HH:MM` an, beginnend mit `00:00` direkt nach Mitternacht und endend mit `23:59` eine Minute vor der nächsten Mitternacht. Beide Teile werden immer zweistellig geschrieben, daher zeigt neun Minuten nach elf Uhr morgens `11:09` an.

Ein ganzer Tag dauert 1440 Minuten. Sobald die Uhr über `23:59` hinausgeht, springt sie auf `00:00` und beginnt den Tag von vorne, und dreht man sie über `00:00` zurück, landet sie auf `23:59`.

# --instructions--

Schreiben Sie eine Funktion `clockTime`, die zwei ganze Zahlen, `hours` und `minutes`, entgegennimmt und die Anzeige einer 24-Stunden-Uhr als Zeichenkette `"HH:MM"` zurückgibt, wobei beide Teile zweistellig aufgefüllt sind.

Beispiele:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Eine der beiden Zahlen darf negativ sein oder größer, als es eine echte Uhr erlaubt.
- Berechnen Sie die Gesamtzahl der Minuten als `hours * 60 + minutes` und rechnen Sie diese Summe in den Bereich von `0` bis `1439` um, damit die Uhr in beide Richtungen überläuft.
- `clockTime(24, 0)` ist genau ein Tag, daher zeigt die Uhr `"00:00"` an.

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
function clockTime(hours, minutes) {
  
}
```

# --asserts--

Acht Uhr morgens zeigt `08:00` an

```javascript
tryCatch(clockTime(8, 0) === "08:00");
```

Einzelne Ziffern werden zweistellig aufgefüllt, daher zeigt neun Minuten nach elf `11:09` an

```javascript
tryCatch(clockTime(11, 9) === "11:09");
```

Genau ein ganzer Tag Stunden springt auf `00:00` zurück

```javascript
tryCatch(clockTime(24, 0) === "00:00");
```

Minuten über 60 werden in die Stunden übertragen

```javascript
tryCatch(clockTime(25, 160) === "03:40");
```

Eine negative Stunde dreht die Uhr über Mitternacht hinaus zurück

```javascript
tryCatch(clockTime(-1, 15) === "23:15");
```

Eine negative Minutenanzahl dreht die Uhr ebenfalls zurück

```javascript
tryCatch(clockTime(0, -90) === "22:30");
```

Mehr als ein ganzer Tag zurück läuft immer weiter über

```javascript
tryCatch(clockTime(-25, 0) === "23:00");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function clockTime(hours, minutes) {
  // % behält das Vorzeichen des linken Operanden, daher zuerst einen ganzen
  // Tag addieren und erneut wrappen, um in 0..1439 zu landen.
  const total = (((hours * 60 + minutes) % 1440) + 1440) % 1440;

  const hh = String(Math.floor(total / 60)).padStart(2, "0");
  const mm = String(total % 60).padStart(2, "0");
  return `${hh}:${mm}`;
}
```
