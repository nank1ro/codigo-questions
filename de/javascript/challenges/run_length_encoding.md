---
language: javascript
exerciseType: 1
difficulty: 2
title: Lauflängencodierung
---

# --description--

Lauflängencodierung ist einer der ältesten Kompressionstricks überhaupt: Statt dasselbe Zeichen immer wieder zu schreiben, schreiben Sie, wie oft es sich wiederholt, und danach das Zeichen selbst.

Ein Faxgerät, das eine überwiegend leere Seite scannt, trifft auf lange Strecken identischer Pixel, deshalb wandert eine Reihe von zwölf `W` als viel kürzeres `12W` durch die Leitung. Taucht ein Zeichen nur einmal auf, bringt das Zählen nichts, also wird es einfach einzeln übernommen.

# --instructions--

Schreiben Sie eine Funktion `encodeRun`, die einen String `text` entgegennimmt und seine lauflängencodierte Form zurückgibt.

Jede Folge desselben Zeichens, das zwei- oder mehrmals hintereinander wiederholt wird, wird zu der Länge der Folge in Dezimalschreibweise, gefolgt von dem Zeichen selbst. Eine Folge der Länge eins wird als einzelnes Zeichen übernommen, ohne Zahl davor.

Beispiele:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- Der Text enthält nur Großbuchstaben von `A` bis `Z` sowie Leerzeichen.
- Eine Folge von mehr als neun Zeichen schreibt ihre vollständige Dezimalzahl, zwölf `W` werden also zu `12W` und nie zu `9W3W`.
- Leerzeichen sind ganz normale Zeichen: Sie werden genauso gezählt und codiert wie Buchstaben.
- Der leere String wird zu dem leeren String codiert.

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

Der leere String wird zu dem leeren String codiert

```javascript
tryCatch(encodeRun("") === "");
```

Ein einzelnes Zeichen wird unverändert als es selbst übernommen

```javascript
tryCatch(encodeRun("A") === "A");
```

Ein String ohne Wiederholungen durchläuft die Codierung unverändert

```javascript
tryCatch(encodeRun("ABCDE") === "ABCDE");
```

Eine Folge von zwei wird zu der Anzahl, gefolgt von dem Zeichen

```javascript
tryCatch(encodeRun("AA") === "2A");
```

Das gemischte Beispiel "AABCCCDEEEE" wird zu "2AB3CD4E"

```javascript
tryCatch(encodeRun("AABCCCDEEEE") === "2AB3CD4E");
```

Eine Folge von zwölf schreibt ihre vollständige Dezimalzahl, deshalb beginnt das Ergebnis mit "12W"

```javascript
tryCatch(encodeRun("WWWWWWWWWWWWBWW") === "12WB2W");
```

Folgen von Leerzeichen werden genauso codiert wie Folgen von Buchstaben

```javascript
tryCatch(encodeRun("  HI  ") === "2 HI2 ");
```

Eine Folge von zehn wird als "10A" geschrieben, nie als zwei kürzere Folgen

```javascript
tryCatch(encodeRun("AAAAAAAAAA") === "10A");
```

Einzelne Zeichen, die sich abwechseln, werden alle unverändert als sie selbst übernommen

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
