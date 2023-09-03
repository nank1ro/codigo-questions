---
language: javascript
exerciseType: 1
difficulty: 3
title: Anno bisestile
---

# --description--

In un anno solare ci sono esattamente 365.25 giorni. Ma questo poteva portare confusione perché gli esseri umani normalmente contano in base all'esatta divisibilità di 1 e non con i punti decimali. Quindi, per evitare quest'ultimo problema, si decise di sommare tutti gli 0.25 giorni ogni ciclo di quattro anni e dare a quell'anno 366 giorni (includendo il 29 febbraio come giorno intercalare) e chiamarlo __anno bisestile__. Gli altri tre anni del ciclo quadriennale contengono solo 365 giorni e non sono __anni bisestili__.

# --instructions--

In questa sfida ci spingeremo ad un nuovo livello, in cui dovremo determinare se si tratta di un anno bisestile o meno senza l'uso della classe `DateTime`, delle dichiarazioni `switch`, dei blocchi __if__, __if-else__ o delle __operazioni ausiliarie__ (`x ? a : b`) né degli operatori logici __AND__ (`&&`) e __OR__ (`||`) con l'eccezione dell'operatore __NOT__ (`!`).

Restituisci `true` se è un anno bisestile, `false` altrimenti.

Esempio di chiamata di funzione:
```javascript
console.log(leapYear(2000));
// stampa true
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

The use of `Date`, `switch`, `if`, `else`, `&&`, `||` or `?` is not allowed.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

L'anno `2016` è bisestile.

```javascript
tryCatch(leapYear(2016) == true);
```

L'anno `1996` è bisestile.

```javascript
tryCatch(leapYear(1996) == true);
```

L'anno `1600` è bisestile.

```javascript
tryCatch(leapYear(1600) == true);
```

L'anno `2020` è bisestile.

```javascript
tryCatch(leapYear(2020) == true);
```

L'anno `2000` è bisestile.

```javascript
tryCatch(leapYear(2000) == true);
```

L'anno `2008` è bisestile.

```javascript
tryCatch(leapYear(2008) == true);
```

L'anno `1521` non è bisestile.

```javascript
tryCatch(leapYear(1521) == false);
```

L'anno `1800` non è bisestile.

```javascript
tryCatch(leapYear(1800) == false);
```

L'anno `2007` non è bisestile.

```javascript
tryCatch(leapYear(2007) == false);
```

L'anno `2002` non è bisestile.

```javascript
tryCatch(leapYear(2002) == false);
```

L'anno `1979` non è bisestile.

```javascript
tryCatch(leapYear(1979) == false);
```

L'anno `2006` non è bisestile.

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
