---
language: javascript
exerciseType: 1
difficulty: 3
title: Année bissextile
---

# --description--

Dans une année civile, il y a exactement 365,25 jours. Mais, éventuellement, cela mènera à la confusion car les humains comptent normalement par divisibilité exacte de 1 et non avec des décimales. Donc, pour éviter ce dernier, il a été décidé d'additionner tous les 0,25 jours tous les quatre ans et de donner à cette année 366 jours (y compris le 29 février comme jour supplémentaire) et l'appeler une __année bissextile__. Les trois autres années du cycle de quatre ans ne contiendraient que 365 jours et __ne seraient pas des années bissextiles__.

# --instructions--

Dans ce défi, nous allons passer à un nouveau niveau, où vous devez déterminer si c'est une année bissextile ou non sans utiliser la classe `Date`, les déclarations `switch`, les __blocs if__, les __blocs if-else__ ou l'__opération ternaire__ (`x ? a : b`) ni les opérateurs logiques __AND__ (`&&`) et __OR__ (`||`) à l'exception de l'opérateur __NOT__ (`!`).

Retournez `true` si c'est une année bissextile, `false` sinon.

Exemple d'appel de fonction :
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

The use of `Date`, `switch`, `if`, `else`, `&&`, `||` or `?` is not allowed.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

The year `2016` is a leap year.

```javascript
tryCatch(leapYear(2016) == true);
```

The year `1996` is a leap year.

```javascript
tryCatch(leapYear(1996) == true);
```

The year `1600` is a leap year.

```javascript
tryCatch(leapYear(1600) == true);
```

The year `2020` is a leap year.

```javascript
tryCatch(leapYear(2020) == true);
```

The year `2000` is a leap year.

```javascript
tryCatch(leapYear(2000) == true);
```

The year `2008` is a leap year.

```javascript
tryCatch(leapYear(2008) == true);
```

The year `1521` is not a leap year.

```javascript
tryCatch(leapYear(1521) == false);
```

The year `1800` is not a leap year.

```javascript
tryCatch(leapYear(1800) == false);
```

The year `2007` is not a leap year.

```javascript
tryCatch(leapYear(2007) == false);
```

The year `2002` is not a leap year.

```javascript
tryCatch(leapYear(2002) == false);
```

The year `1979` is not a leap year.

```javascript
tryCatch(leapYear(1979) == false);
```

The year `2006` is not a leap year.

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
