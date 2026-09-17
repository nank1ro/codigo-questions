Una **stringa** è una sequenza di caratteri racchiusa tra virgolette, come `"hello"` o `'hello'`.
Ogni stringa ha una proprietà `length` che indica quanti caratteri contiene:
```javascript
let greeting = "hello";
console.log(greeting.length);
// stampa 5
```
Anche gli spazi e la punteggiatura contano come caratteri.

---

Ogni carattere di una stringa ha un **indice**, a partire da `0`.
Puoi leggere un singolo carattere con le parentesi quadre o con il metodo `charAt()`:
```javascript
let word = "hello";
console.log(word[0]);
// stampa h
console.log(word.charAt(1));
// stampa e
```
L'ultimo carattere si trova all'indice `length - 1`:
```javascript
console.log(word[word.length - 1]);
// stampa o
```

---

Le stringhe hanno molti **metodi** integrati. Due dei più semplici cambiano il maiuscolo/minuscolo di ogni lettera:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// stampa HELLO
console.log(word.toLowerCase());
// stampa hello
```
Entrambi i metodi non richiedono argomenti, quindi ricordati le parentesi.

---

Per verificare se una stringa ne contiene un'altra, usa questi metodi, che restituiscono tutti un booleano:
- `includes(text)` è `true` se `text` compare da qualche parte
- `startsWith(text)` è `true` se la stringa inizia con `text`
- `endsWith(text)` è `true` se la stringa termina con `text`

```javascript
let file = "photo.png";
console.log(file.includes("."));
// stampa true
console.log(file.startsWith("ph"));
// stampa true
console.log(file.endsWith(".jpg"));
// stampa false
```
Il confronto distingue tra maiuscole e minuscole: `"Hello".includes("h")` è `false`.

---

Il metodo `indexOf()` restituisce l'indice in cui un pezzo di testo compare **per la prima volta** nella stringa.
Se il testo non viene trovato, restituisce `-1`:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// stampa 2
console.log(word.indexOf("z"));
// stampa -1
```

---

Il metodo `slice(start, end)` estrae una parte di una stringa, dall'indice `start` fino a (ma escluso) l'indice `end`:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// stampa Java
console.log(word.slice(4));
// stampa Script
```
Se ometti `end`, la porzione arriva fino alla fine della stringa.
Un indice negativo conta a partire dalla fine: `word.slice(-3)` è `"ipt"`.
Il metodo `substring(start, end)` funziona allo stesso modo, ma non accetta indici negativi.

---

`indexOf()` e `slice()` funzionano bene insieme: trova dove si trova qualcosa, poi taglia la stringa lì.
```javascript
let time = "10:45";
let colon = time.indexOf(":");
console.log(time.slice(colon + 1));
// stampa 45
```

---

Il metodo `split(separator)` suddivide una stringa in un **array** di parti, tagliando a ogni `separator`:
```javascript
let sentence = "I like JavaScript";
let words = sentence.split(" ");
console.log(words);
// stampa [ 'I', 'like', 'JavaScript' ]
```
Il contrario è il metodo dell'array `join(separator)`, che incolla di nuovo i pezzi in una stringa:
```javascript
console.log(words.join("-"));
// stampa I-like-JavaScript
```

---

L'input dell'utente spesso ha spazi extra intorno. Il metodo `trim()` restituisce una copia della stringa con gli spazi rimossi da **entrambe** le estremità:
```javascript
let input = "   hello   ";
console.log(input.trim());
// stampa hello
```
`trimStart()` rimuove solo gli spazi iniziali e `trimEnd()` solo quelli finali.
Gli spazi nel mezzo della stringa non vengono mai toccati.

---

Il metodo `replace(search, replacement)` restituisce una nuova stringa in cui la **prima** occorrenza di `search` viene sostituita da `replacement`:
```javascript
let text = "red red";
console.log(text.replace("red", "blue"));
// stampa blue red
```
Per sostituire **ogni** occorrenza, usa `replaceAll()`:
```javascript
console.log(text.replaceAll("red", "blue"));
// stampa blue blue
```

---

Il metodo `repeat(count)` restituisce la stringa ripetuta `count` volte:
```javascript
console.log("ab".repeat(3));
// stampa ababab
console.log("ab".repeat(0));
// stampa una stringa vuota
```

---

Il metodo `padStart(targetLength, padString)` aggiunge `padString` all'**inizio** della stringa finché non raggiunge `targetLength` caratteri. `padEnd()` fa lo stesso alla fine:
```javascript
console.log("7".padStart(3, "0"));
// stampa 007
console.log("Tea".padEnd(6, "."));
// stampa Tea...
```
Se la stringa è già abbastanza lunga, viene restituita invariata.
I numeri non hanno metodi per stringhe, quindi convertili prima con `String(number)`.

---

Due stringhe sono uguali con `===` solo se hanno esattamente gli stessi caratteri, con la stessa maiuscola/minuscola:
```javascript
console.log("hello" === "hello");
// stampa true
console.log("hello" === "Hello");
// stampa false
```
Gli operatori `<` e `>` confrontano le stringhe in ordine alfabetico, carattere per carattere.
Le lettere maiuscole vengono prima di quelle minuscole, quindi `"Zoo" < "apple"` è `true`.

---

Le stringhe sono **immutabili**: una volta create, una stringa non può mai essere modificata.
Assegnare a un indice non fa nulla, e ogni metodo delle stringhe restituisce una **nuova** stringa invece di modificare quella originale:
```javascript
let word = "hello";
word[0] = "j";
console.log(word);
// stampa hello
word.toUpperCase();
console.log(word);
// stampa hello
```
Per conservare un risultato, riassegnalo alla variabile:
```javascript
word = word.toUpperCase();
```

---

Chiamare `split("")` con un separatore vuoto trasforma una stringa in un array dei suoi singoli caratteri.
Gli array hanno un metodo `reverse()`, quindi puoi invertire una stringa dividendola, invertendola e ricongiungendola:
```javascript
let word = "abc";
console.log(word.split("").reverse().join(""));
// stampa cba
```
