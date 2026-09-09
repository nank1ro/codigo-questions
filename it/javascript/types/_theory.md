Ogni valore in JavaScript ha un **tipo**. Esistono sette tipi **primitivi**:
- `number` per qualsiasi numero, come `42` o `3.14`
- `string` per il testo, come `"Ana"`
- `boolean` per `true` e `false`
- `undefined` per un valore che non è mai stato fornito
- `null` per un valore volutamente vuoto
- `bigint` per numeri interi di qualsiasi dimensione, come `9007199254740993n`
- `symbol` per identificatori unici creati con `Symbol()`

Tutto il resto (array, funzioni, oggetti creati con `{}`, date...) è un `object`.
L'operatore `typeof` ti dice il tipo di un valore, come stringa:
```javascript
console.log(typeof 42, typeof "Ana", typeof true);
// prints number string boolean
let city;
console.log(typeof city);
// prints undefined
```

---

JavaScript è **dinamicamente tipizzato**: una variabile non ha un tipo proprio, solo il valore che contiene in un dato momento ne ha uno. La stessa variabile può contenere un numero ora e una stringa dopo, e `typeof` segue il valore:
```javascript
let data = 10;
console.log(typeof data);
// prints number
data = "ten";
console.log(typeof data);
// prints string
```
Questo è comodo, ma significa anche che una funzione può ricevere un valore di un tipo inatteso, quindi controllare con `typeof` è un primo passo comune. Poiché `typeof` restituisce una stringa, confronti il suo risultato con una stringa:
```javascript
if (typeof data === "string") {
  console.log("text");
}
```

---

`typeof` ha alcune risposte che sorprendono.
Le funzioni hanno una risposta propria, `"function"`, anche se sono oggetti:
```javascript
console.log(typeof function () {});
// prints function
console.log(typeof console.log);
// prints function
```
Gli array **non** hanno una risposta propria: sono semplicemente `"object"`, proprio come `{}`:
```javascript
console.log(typeof [1, 2, 3]);
// prints object
```
E `typeof null` è `"object"`, un bug storico mai corretto. Quindi `typeof` distingue bene i primitivi e le funzioni, ma non sa distinguere un array, un oggetto e `null`.

---

Puoi convertire un valore in un altro tipo **esplicitamente** chiamando il tipo come una funzione:
- `Number(value)` converte in un numero: `Number("42")` è `42`
- `String(value)` converte in una stringa: `String(42)` è `"42"`
- `Boolean(value)` converte in un booleano: `Boolean("")` è `false`

Il risultato è un valore completamente nuovo; l'originale non viene modificato:
```javascript
const input = "7";
const count = Number(input) + 1;
console.log(count, typeof count);
// prints 8 number
console.log(String(count) + "!");
// prints 8!
```
Convertire esplicitamente rende visibile la tua intenzione: chi legge `Number(input)` sa che `input` era testo.

---

`Number()` è rigoroso: l'intera stringa deve essere un numero, altrimenti il risultato è `NaN` ("Not a Number"):
```javascript
console.log(Number("12px"));
// prints NaN
```
`parseInt()` e `parseFloat()` sono più tolleranti: leggono le cifre dall'inizio della stringa, ignorano gli spazi iniziali e si fermano al primo carattere che non fa parte di un numero. `parseInt` conserva solo la parte intera:
```javascript
console.log(parseInt("12px"), parseFloat("1.5kg"));
// prints 12 1.5
console.log(parseInt("3.9em"), parseInt("-4px"));
// prints 3 -4
```
Quando la stringa non inizia con qualcosa che può iniziare un numero (un segno opzionale, poi una cifra), restituiscono anch'esse `NaN`:
```javascript
console.log(parseInt("auto"));
// prints NaN
```
`NaN` è l'unico valore che non è uguale a se stesso, quindi `x === NaN` è sempre `false`; per rilevarlo usa `Number.isNaN(x)`.

---

Ci sono due modi per chiedere "questo è `NaN`?", e rispondono a domande diverse.
La vecchia globale `isNaN(value)` prima **converte** `value` in un numero, poi controlla. Quindi dice `true` per qualsiasi cosa non possa diventare un numero, anche se non è per niente `NaN`:
```javascript
console.log(isNaN("hello"));
// prints true, because Number("hello") is NaN
console.log(isNaN("42"));
// prints false, because Number("42") is 42
```
`Number.isNaN(value)` **non** converte: è `true` solo quando `value` è davvero il numero `NaN`:
```javascript
console.log(Number.isNaN("hello"));
// prints false, a string is not NaN
console.log(Number.isNaN(Number("hello")));
// prints true
```
Preferisci `Number.isNaN`, e converti prima se vuoi sapere se una conversione è fallita.

---

JavaScript converte anche **implicitamente**, e l'operatore `+` è dove questo morde più spesso. Se uno dei due lati è una stringa, `+` **concatena** e l'altro lato viene convertito in una stringa:
```javascript
console.log("5" + 3);
// prints 53
console.log(1 + 2 + "3");
// prints 33, because 1 + 2 is computed first
```
Tutti gli altri operatori aritmetici convertono entrambi i lati in **numeri**:
```javascript
console.log("6" - 2, "3" * "4");
// prints 4 12
```
Quindi sommare valori che vengono dal testo (input dell'utente, file, URL) può costruire silenziosamente una stringa invece di una somma. Converti con `Number()` prima di sommare per sicurezza.

---

Un modo breve per convertire una stringa in un numero è il **più unario**: un `+` posto davanti a un singolo valore lo converte esattamente come fa `Number()`:
```javascript
console.log(+"5" + 5);
// prints 10
console.log(typeof +"5");
// prints number
```
È compatto, ma facile da confondere con l'addizione, quindi molti team preferiscono l'esplicito `Number("5")`.

---

L'uguaglianza **debole** `==` converte i due lati in un tipo comune prima di confrontarli, seguendo regole difficili da ricordare:
```javascript
console.log("5" == 5);
// prints true, "5" becomes 5
console.log(0 == "");
// prints true, "" becomes 0
console.log(0 == false, "1" == true);
// prints true true
```
L'uguaglianza **stretta** `===` non converte mai: valori di tipi diversi semplicemente non sono uguali:
```javascript
console.log("5" === 5, 0 === "", 0 === false);
// prints false false false
```
Usa `===` (e `!==`) per default. L'unica eccezione comune è `value == null`, che controlla `null` e `undefined` insieme.

---

Quando JavaScript ha bisogno di un booleano, per esempio in una condizione `if` o in `Boolean(value)`, converte il valore. Solo otto valori diventano `false`; sono chiamati **falsy**:
`false`, `0`, `-0`, `0n`, `""`, `null`, `undefined` e `NaN`.
**Tutto il resto è truthy**, compresi alcuni valori che sembrano vuoti:
```javascript
console.log(Boolean(0), Boolean(""), Boolean(NaN));
// prints false false false
console.log(Boolean("0"), Boolean("false"), Boolean([]), Boolean({}));
// prints true true true true
```
`"0"` è una stringa non vuota, quindi è truthy; un array vuoto è un oggetto, quindi è truthy anch'esso.

---

Una scorciatoia comune per convertire qualsiasi valore in un booleano è la **doppia negazione** `!!`: il primo `!` converte in un booleano e lo inverte, il secondo lo inverte di nuovo:
```javascript
console.log(!!"text", !!0);
// prints true false
```
`!!value` e `Boolean(value)` danno esattamente lo stesso risultato; la forma esplicita è più facile da leggere.

---

JavaScript ha un unico tipo `number` per interi e decimali: ogni numero è un valore in virgola mobile a 64 bit (un *double*). Quindi `5` e `5.0` sono lo stesso valore, e non esiste un tipo intero separato:
```javascript
console.log(5 === 5.0, 10 / 2);
// prints true 5
```
Per chiedere se un numero non ha parte frazionaria, usa `Number.isInteger`:
```javascript
console.log(Number.isInteger(5.0), Number.isInteger(3.5));
// prints true false
```
Le stringhe template convertono il valore interpolato in una stringa con le stesse regole di `String()`, quindi `${5.0}` diventa `"5"`, non `"5.0"`.

---

Poiché i numeri sono double, alcuni decimali non possono essere memorizzati esattamente e appaiono piccoli errori:
```javascript
console.log(0.1 + 0.2);
// prints 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);
// prints false
```
Il metodo `toFixed(digits)` arrotonda un numero a `digits` decimali, ma restituisce una **stringa**, che va bene per la visualizzazione e non va bene per ulteriori calcoli:
```javascript
const price = (0.1 + 0.2).toFixed(2);
console.log(price, typeof price);
// prints 0.30 string
```
Per ottenere un **numero** arrotondato, riconverti il risultato con `Number()`:
```javascript
console.log(Number((0.1 + 0.2).toFixed(1)));
// prints 0.3
```

---

Un `number` può rappresentare interi esattamente solo fino a `Number.MAX_SAFE_INTEGER`, che è `9007199254740991`. Oltre, le cifre si perdono:
```javascript
console.log(9007199254740993);
// prints 9007199254740992
```
Per numeri interi più grandi usa `bigint`: scrivi il letterale con un suffisso `n`, oppure converti con `BigInt()`:
```javascript
const big = 9007199254740993n;
console.log(typeof big, big + 1n);
// prints bigint 9007199254740994n
```
`console.log` mostra il suffisso `n`; `String(big)` dà le semplici cifre.
Un `bigint` e un `number` non possono essere mescolati in aritmetica: `big + 1` lancia un `TypeError`. Converti esplicitamente uno dei due lati, con `BigInt(count)` o `Number(big)`.

---

Poiché `typeof` risponde `"object"` per array, oggetti e `null`, distinguerli richiede due controlli extra.
`Array.isArray(value)` è `true` solo per gli array:
```javascript
console.log(Array.isArray([1, 2]), Array.isArray({}));
// prints true false
```
Per `null` confronta direttamente, `value === null`. Combinandli si ottiene un quadro completo di qualsiasi valore:
```javascript
function kind(value) {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}
```
Controlla prima `null` e gli array, perché il semplice `typeof` non può distinguerli.

---

Il testo che viene da moduli, file o URL è sempre una stringa, anche quando rappresenta un numero o un booleano. Riportarlo al tipo giusto combina ciò che hai visto: confronta con `"true"` e `"false"` per i booleani, e prova `Number()` per i numeri, ricordando che `Number("")` è `0` e che `Number.isNaN` ti dice quando la conversione è fallita:
```javascript
console.log(Number("3.5"), Number(""), Number("12px"));
// prints 3.5 0 NaN
```
Quando nulla corrisponde, mantieni la stringa com'è.
