---
language: javascript
exerciseType: 1
difficulty: 2
title: Orologio
---

# --description--

Un orologio a 24 ore mostra l'ora del giorno come `HH:MM`, partendo da `00:00` subito dopo la mezzanotte e arrivando a `23:59` un minuto prima della mezzanotte successiva. Entrambe le parti sono sempre scritte con due cifre, così nove minuti dopo le undici del mattino si legge `11:09`.

Un giorno intero dura 1440 minuti. Quando l'orologio supera `23:59` riparte da `00:00` e ricomincia il giorno, e riavvolgendolo all'indietro oltre `00:00` si torna a `23:59`.

# --instructions--

Scrivi una funzione `clockTime` che riceve due numeri interi, `hours` e `minutes`, e restituisce la lettura di un orologio a 24 ore come stringa `"HH:MM"`, con entrambe le parti portate a due cifre.

Esempi:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Ciascuno dei due numeri può essere negativo, oppure più grande di quanto un orologio reale consenta.
- Calcola il numero totale di minuti come `hours * 60 + minutes`, poi riporta quel totale nell'intervallo da `0` a `1439`, così l'orologio riparte in entrambe le direzioni.
- `clockTime(24, 0)` è esattamente un giorno, quindi si legge `"00:00"`.

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

Le otto del mattino si legge `08:00`

```javascript
tryCatch(clockTime(8, 0) === "08:00");
```

Le cifre singole vengono portate a due cifre, così nove minuti dopo le undici si legge `11:09`

```javascript
tryCatch(clockTime(11, 9) === "11:09");
```

Esattamente un giorno intero di ore fa ripartire l'orologio da `00:00`

```javascript
tryCatch(clockTime(24, 0) === "00:00");
```

I minuti oltre 60 vengono riportati nelle ore

```javascript
tryCatch(clockTime(25, 160) === "03:40");
```

Un'ora negativa riavvolge l'orologio all'indietro oltre la mezzanotte

```javascript
tryCatch(clockTime(-1, 15) === "23:15");
```

Anche un numero di minuti negativo riavvolge l'orologio all'indietro

```javascript
tryCatch(clockTime(0, -90) === "22:30");
```

Più di un giorno intero all'indietro continua a ripartire

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
  // % mantiene il segno dell'operando di sinistra, quindi aggiungi un giorno
  // intero prima di riportare di nuovo per atterrare in 0..1439.
  const total = (((hours * 60 + minutes) % 1440) + 1440) % 1440;

  const hh = String(Math.floor(total / 60)).padStart(2, "0");
  const mm = String(total % 60).padStart(2, "0");
  return `${hh}:${mm}`;
}
```
