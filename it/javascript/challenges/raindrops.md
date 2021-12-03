---
language: javascript
exerciseType: 1
difficulty: 1
title: Gocce di pioggia
---

# --description--

Il tuo compito e' quello di convertire un numero in una stringa che contiene suoni di gocce di pioggia corrispondenti a determinati fattori potenziali.
Un fattore e' un numero che si divide uniformemente in un altro numero, senza lasciare alcun resto.
Il modo piu' semplice per verificare se un numero e' un fattore di un altro e' utilizzare l'operazione modulo.
Le regole delle gocce di pioggia sono che se un dato numero:

- ha 3 come fattore, aggiungi 'Pling' al risultato.
- ha 5 come fattore, aggiungi 'Plang' al risultato.
- ha 7 come fattore, aggiungi 'Plong' al risultato.
- non ha 3, 5 o 7 come fattore, il risultato dovrebbe essere costituito dalle cifre del numero.

# --instructions--

Scrivi una funzione che restituisca la stringa corretta, ad esempio:

- 28 ha 7 come fattore, ma non 3 o 5, quindi il risultato e' `"Plong"`.
- 30 ha sia 3 che 5 come fattori, ma non 7, quindi il risultato e' `"PlingPlang"`.
- 34 non e' fattorizzato da 3, 5, o 7, quindi il risultato e' `"34"`.

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE (implements error handler)
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
function converti(num) {
  
}
```

# --asserts--

Il suono per 1 è "1"

```javascript
tryCatch(converti(1) === "1");
```

Il suono per 3 è "Pling"

```javascript
tryCatch(converti(3) === "Pling");
```

Il suono per 5 è "Plang"

```javascript
tryCatch(converti(5) === "Plang");
```

Il suono per 7 è "Plong"

```javascript
tryCatch(converti(7) === "Plong");
```

Il suono per 6 è "Pling"

```javascript
tryCatch(converti(6) === "Pling");
```

Il suono per 8 è "8"

```javascript
tryCatch(converti(8) === "8");
```

Il suono per 9 è "Pling"

```javascript
tryCatch(converti(9) === "Pling");
```

Il suono per 10 è "Plang"

```javascript
tryCatch(converti(10) === "Plang");
```

Il suono per 14 è "Plong"

```javascript
tryCatch(converti(14) === "Plong");
```

Il suono per 15 è "PlingPlang"

```javascript
tryCatch(converti(15) === "PlingPlang");
```

Il suono per 21 è "PlingPlong"

```javascript
tryCatch(converti(21) === "PlingPlong");
```

Il suono per 25 è "Plang"

```javascript
tryCatch(converti(25) === "Plang");
```

Il suono per 27 è "Pling"

```javascript
tryCatch(converti(27) === "Pling");
```

Il suono per 35 è "PlangPlong"

```javascript
tryCatch(converti(35) === "PlangPlong");
```

Il suono per 49 è "Plong"

```javascript
tryCatch(converti(49) === "Plong");
```

Il suono per 52 è "52"

```javascript
tryCatch(converti(52) === "52");
```

Il suono per 105 è "PlingPlangPlong"

```javascript
tryCatch(converti(105) === "PlingPlangPlong");
```

Il suono per 3125 è "Plang"

```javascript
tryCatch(converti(3125) === "Plang");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function converti(num) {
  var risultato = ""
  if (num % 3 == 0) {
    risultato += "Pling"
  }
  if (num % 5 == 0) {
    risultato += "Plang"
  }
  if (num % 7 == 0) {
    risultato += "Plong"
  }
  if (!risultato) {
    risultato = num.toString()
  }
  return risultato
}
```
