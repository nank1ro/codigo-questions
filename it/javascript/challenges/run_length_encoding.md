---
language: javascript
exerciseType: 1
difficulty: 2
title: Codifica run-length
---

# --description--

La codifica run-length è uno dei trucchi di compressione più antichi che esistano: invece di scrivere più e più volte lo stesso carattere, scrivi quante volte si ripete e poi il carattere stesso.

Un fax che scansiona una pagina quasi tutta bianca incontra lunghe distese di pixel identici, così una riga di dodici `W` viaggia lungo la linea come la ben più corta `12W`. Quando un carattere compare una sola volta, contarlo non porta nessun vantaggio, quindi viene copiato da solo.

# --instructions--

Scrivi una funzione `encodeRun` che riceve una stringa `text` e restituisce la sua forma codificata run-length.

Ogni sequenza dello stesso carattere ripetuto due o più volte diventa la lunghezza della sequenza scritta in decimale, seguita da quel carattere. Una sequenza di lunghezza uno viene copiata come singolo carattere, senza nessun numero davanti.

Esempi:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- Il testo contiene solo lettere maiuscole dalla `A` alla `Z` e spazi.
- Una sequenza più lunga di nove caratteri usa il suo conteggio decimale completo, quindi dodici `W` diventano `12W` e mai `9W3W`.
- Gli spazi sono caratteri normali: vengono contati e codificati esattamente come le lettere.
- La stringa vuota si codifica nella stringa vuota.

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

La stringa vuota si codifica nella stringa vuota

```javascript
tryCatch(encodeRun("") === "");
```

Un singolo carattere viene copiato così com'è

```javascript
tryCatch(encodeRun("A") === "A");
```

Una stringa senza ripetizioni attraversa il processo invariata

```javascript
tryCatch(encodeRun("ABCDE") === "ABCDE");
```

Una sequenza di due diventa il conteggio seguito dal carattere

```javascript
tryCatch(encodeRun("AA") === "2A");
```

L'esempio misto "AABCCCDEEEE" diventa "2AB3CD4E"

```javascript
tryCatch(encodeRun("AABCCCDEEEE") === "2AB3CD4E");
```

Una sequenza di dodici usa il suo conteggio decimale completo, quindi il risultato inizia con "12W"

```javascript
tryCatch(encodeRun("WWWWWWWWWWWWBWW") === "12WB2W");
```

Le sequenze di spazi vengono codificate esattamente come le sequenze di lettere

```javascript
tryCatch(encodeRun("  HI  ") === "2 HI2 ");
```

Una sequenza di dieci viene scritta come "10A", mai come due sequenze più corte

```javascript
tryCatch(encodeRun("AAAAAAAAAA") === "10A");
```

I caratteri singoli che si alternano vengono tutti copiati così come sono

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
