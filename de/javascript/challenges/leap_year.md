---
language: javascript
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

Im Kalenderjahr gibt es genau 365,25 Tage. Aber irgendwann wird dies zu Verwirrung führen, da Menschen normalerweise mit exakter Teilbarkeit durch 1 rechnen und nicht mit Dezimalzahlen. Um dies zu vermeiden, wurde beschlossen, alle 0,25 Tage in jedem vierjährigen Zyklus zu addieren und diesem Jahr 366 Tage (einschließlich 29. Februar als Schalttag) zu geben und es als __Schaltjahr__ zu bezeichnen. Die anderen drei Jahre im vierjährigen Zyklus würden nur 365 Tage enthalten und __wären keine Schaltjahre__.

# --instructions--

In dieser Herausforderung bringen wir es auf ein neues Niveau: Sie müssen bestimmen, ob es ein Schaltjahr ist oder nicht, ohne die Klasse `Date`, `switch`-Anweisungen, __if-Blöcke__, __if-else-Blöcke__ oder __Ternär-Operationen__ (`x ? a : b`) oder die logischen Operatoren __UND__ (`&&`) und __ODER__ (`||`) zu verwenden, mit Ausnahme des Operators __NICHT__ (`!`).

Geben Sie `true` zurück, wenn es ein Schaltjahr ist, `false` sonst.

Beispiel für einen Funktionsaufruf:
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

Die Verwendung von `Date`, `switch`, `if`, `else`, `&&`, `||` oder `?` ist nicht zulässig.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Das Jahr `2016` ist ein Schaltjahr.

```javascript
tryCatch(leapYear(2016) == true);
```

Das Jahr `1996` ist ein Schaltjahr.

```javascript
tryCatch(leapYear(1996) == true);
```

Das Jahr `1600` ist ein Schaltjahr.

```javascript
tryCatch(leapYear(1600) == true);
```

Das Jahr `2020` ist ein Schaltjahr.

```javascript
tryCatch(leapYear(2020) == true);
```

Das Jahr `2000` ist ein Schaltjahr.

```javascript
tryCatch(leapYear(2000) == true);
```

Das Jahr `2008` ist ein Schaltjahr.

```javascript
tryCatch(leapYear(2008) == true);
```

Das Jahr `1521` ist kein Schaltjahr.

```javascript
tryCatch(leapYear(1521) == false);
```

Das Jahr `1800` ist kein Schaltjahr.

```javascript
tryCatch(leapYear(1800) == false);
```

Das Jahr `2007` ist kein Schaltjahr.

```javascript
tryCatch(leapYear(2007) == false);
```

Das Jahr `2002` ist kein Schaltjahr.

```javascript
tryCatch(leapYear(2002) == false);
```

Das Jahr `1979` ist kein Schaltjahr.

```javascript
tryCatch(leapYear(1979) == false);
```

Das Jahr `2006` ist kein Schaltjahr.

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
