Una **stringa** è una sequenza di caratteri racchiusa tra virgolette, come `"hello"` o `'hello'`.
Ogni stringa ha una proprietà `length` che indica quanti caratteri contiene:
```javascript
let greeting = "hello";
console.log(greeting.length);
// prints 5
```
Anche gli spazi e la punteggiatura contano come caratteri.

---

Ogni carattere di una stringa ha un **indice**, a partire da `0`.
Puoi leggere un singolo carattere con le parentesi quadre o con il metodo `charAt()`:
```javascript
let word = "hello";
console.log(word[0]);
// prints h
console.log(word.charAt(1));
// prints e
```
L'ultimo carattere si trova all'indice `length - 1`:
```javascript
console.log(word[word.length - 1]);
// prints o
```

---

Le stringhe hanno molti **metodi** integrati. Due dei più semplici cambiano il maiuscolo/minuscolo di ogni lettera:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// prints HELLO
console.log(word.toLowerCase());
// prints hello
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
// prints true
console.log(file.startsWith("ph"));
// prints true
console.log(file.endsWith(".jpg"));
// prints false
```
Il confronto distingue tra maiuscole e minuscole: `"Hello".includes("h")` è `false`.

---

Il metodo `indexOf()` restituisce l'indice in cui un pezzo di testo compare **per la prima volta** nella stringa.
Se il testo non viene trovato, restituisce `-1`:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// prints 2
console.log(word.indexOf("z"));
// prints -1
```

---

Il metodo `slice(start, end)` estrae una parte di una stringa, dall'indice `start` fino a (ma escluso) l'indice `end`:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// prints Java
console.log(word.slice(4));
// prints Script
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
// prints 45
```
