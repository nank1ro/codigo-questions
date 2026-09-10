Un **commento** è una nota scritta dentro il codice sorgente per chi lo legge. JavaScript ignora completamente i commenti, quindi non cambiano mai ciò che il programma fa.

Il commento più semplice è il **commento su una riga**: inizia con `//` e arriva fino alla fine della riga.
```javascript
// Greets the user
console.log("Hello");
```
Usa i commenti per spiegare a cosa serve una parte di codice, o perché è stata scritta in quel modo. Nota che, a differenza di altri linguaggi, `#` **non** inizia un commento in JavaScript.

---

Un commento non ha bisogno di una riga tutta sua: può seguire il codice sulla stessa riga. Questo è un **commento in linea** (o commento finale), ed è un buon posto per una breve nota su quella specifica istruzione:
```javascript
const retries = 3; // give up after three attempts
```
Tutto ciò che va da `//` alla fine della riga viene ignorato, mentre il codice che lo precede viene eseguito normalmente.

---

Poiché i commenti vengono ignorati, aggiungere o eliminare un commento non cambia mai ciò che un programma fa. Viene eseguito solo il codice che **non** è commentato.

Questo rende `//` un modo rapido per disattivare una riga di codice senza cancellarla. Si chiama **commentare via** il codice:
```javascript
let total = 10;
// total = total + 5;
console.log(total); // prints 10
```
La seconda riga ora è un commento, quindi `total` resta `10`. Togliendo il `//` la riga torna a vivere.

Commentare via è comodo mentre fai esperimenti, ma ricordati di fare pulizia: il codice che resta commentato a lungo confonde solo chi lo legge dopo di te.

---

Quando un commento ha bisogno di più di una riga, JavaScript offre il **commento su più righe** (chiamato anche commento a blocco): inizia con `/*` e finisce con `*/`, e tutto ciò che sta in mezzo viene ignorato, compresi gli a capo.
```javascript
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
console.log("Welcome!");
```
Un commento a blocco può anche essere breve e restare su una sola riga: `/* like this */`.

---

Qualunque tipo di commento tu usi, la regola è la stessa: il testo al suo interno **non è codice**. Un `console.log` dentro un commento non stampa mai nulla, e il codice scritto dopo `//` sulla stessa riga non viene mai eseguito, anche quando la riga inizia con codice vero:
```javascript
console.log("a"); // console.log("b");
/* console.log("c"); */
// prints only a
```
Quando non sei sicuro di cosa stampi un programma, cancella mentalmente ogni commento e leggi quello che resta.

---

A differenza di `//`, che si ferma alla fine della riga, un commento `/*` si ferma solo al `*/`. Se dimentichi di chiuderlo, JavaScript considera tutto il codice successivo come parte del commento e segnala un errore di sintassi:
```javascript
const width = 10; /* in centimetres
console.log(width); // still inside the comment: SyntaxError, the comment is never closed
```
Sia `//` sia `/* */` funzionano come commenti in linea, ma con `/*` assicurati sempre che il `*/` ci sia.

---

In JavaScript i commenti a blocco **non possono essere annidati**: il commento finisce al **primo** `*/` che incontra, non importa quanti `/*` ci siano stati prima.
```javascript
/* outer /* inner */ still a comment */
console.log("done");
```
Qui il commento finisce subito dopo `inner`, quindi `still a comment */` viene letto come codice e provoca un errore di sintassi. Tienilo a mente quando commenti via un blocco che contiene già un commento `/* */`: usa `//` su ogni riga, oppure elimina prima il commento interno.

---

Per commentare via più righe in una volta sola, racchiudile in un unico commento a blocco invece di aggiungere `//` a ogni riga:
```javascript
let total = 100;
/*
total = total - 30;
total = total - 20;
*/
console.log(total); // prints 100
```
Poiché le righe dentro al blocco vengono ignorate, `total` non cambia mai. Ricorda che questo funziona solo se nessuna di quelle righe contiene un `*/`.

---

JavaScript ha un terzo tipo di commento, il **commento di documentazione**, scritto nel formato **JSDoc**: un commento a blocco che inizia con `/**` (due asterischi) posizionato direttamente sopra una funzione. Al suo interno le righe di solito iniziano con ` * ` e speciali **tag** che iniziano con `@` descrivono la funzione:
- `@param {type} name description` per ogni parametro
- `@returns {type} description` per il valore restituito

```javascript
/**
 * Returns the greeting for a person.
 * @param {string} name the name of the person
 * @returns {string} the greeting, ending with an exclamation mark
 */
function greet(name) {
  return `Hi, ${name}!`;
}
```
Per JavaScript è solo un commento, ma gli editor lo leggono e lo mostrano come testo di aiuto per `greet`, insieme al tipo scritto tra parentesi graffe (`{number}`, `{string}`, `{boolean}`, `{number[]}`...).

---

La prima riga di un commento JSDoc è il **riepilogo**: una breve frase che dice cosa fa la funzione. Scrivila alla terza persona, come se descrivessi la funzione: "Returns...", "Adds...", "Checks...". Poi elenca i tag, uno per riga:
```javascript
/**
 * Returns true when n is divisible by two.
 * @param {number} n the number to check
 * @returns {boolean} true for even numbers, false otherwise
 */
function isEven(n) {
  return n % 2 === 0;
}
```
Il commento deve stare subito sopra la dichiarazione, senza righe vuote in mezzo, altrimenti gli editor non lo associano alla funzione.

---

Un commento JSDoc è anche un **contratto**: dice a chi chiama la funzione cosa passare e cosa aspettarsi in cambio, ancor prima che il corpo sia scritto. Leggere il commento spesso basta per implementare la funzione:
```javascript
/**
 * Returns the larger of two numbers.
 * @param {number} a the first number
 * @param {number} b the second number
 * @returns {number} a if it is greater than b, otherwise b
 */
function larger(a, b) {
  return a > b ? a : b;
}
```
Ogni `@param` corrisponde a un parametro, nello stesso ordine, e `@returns` descrive ogni possibile risultato.

---

L'ordine dentro un commento JSDoc è sempre lo stesso: prima il riepilogo, poi un `@param` per ogni parametro nell'ordine in cui sono dichiarati, e infine `@returns`. L'apertura `/**` e la chiusura ` */` racchiudono tutto, e il commento sta direttamente sopra la funzione che descrive:
```javascript
/**
 * Returns the number of seconds in the given minutes.
 * @param {number} minutes a whole number of minutes
 * @returns {number} minutes multiplied by sixty
 */
function toSeconds(minutes) {
  return minutes * 60;
}
```

---

Un file JavaScript può iniziare con una riga speciale chiamata **shebang** (o hashbang): `#!` seguito dal percorso del programma che deve eseguire il file. Sui sistemi Unix-like ti permette di eseguire uno script direttamente dal terminale, come `./hello.js`, senza scrivere prima `node`:
```javascript
#!/usr/bin/env node
console.log("Hello from Node");
```
JavaScript ignora questa riga esattamente come un commento, ma solo quando è la **primissima riga** del file: in qualsiasi altro punto, `#!` è un errore di sintassi. `/usr/bin/env node` significa "trova `node` su questo sistema e usalo".

---

Un buon commento spiega **perché** il codice fa qualcosa, non **cosa** fa. Il codice mostra già cosa succede; ripeterlo a parole aggiunge rumore e diventa obsoleto non appena il codice cambia:
```javascript
// set timeout to 30
const timeout = 30;
```
Il motivo dietro quel numero è ciò che chi legge non può indovinare:
```javascript
// the server drops idle connections after 35 seconds, so stop earlier
const timeout = 30;
```
Se un commento si limita a ripetere la riga sottostante, eliminalo o sostituiscilo con il motivo.

---

Alcuni commenti seguono una convenzione che gli editor riconoscono. I **marcatori** più comuni sono:
- `// TODO: ...` segnala qualcosa che deve ancora essere scritto
- `// FIXME: ...` segnala codice che si sa essere sbagliato e che va corretto

```javascript
const limit = 10;
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
Per JavaScript sono commenti ordinari; gli editor li elencano così il lavoro in sospeso è facile da trovare. Un `TODO` di solito sta accanto a un segnaposto che tiene in piedi il codice finché non viene scritta l'implementazione vera. Quando completi il lavoro, sostituisci il segnaposto ed elimina il marcatore nella stessa modifica: un `TODO` obsoleto è fuorviante.

---

Un `FIXME` è diverso da un `TODO`: il codice esiste già, ma si sa che è sbagliato. Un buon `FIXME` dice qual è il bug e, quando è possibile, dà un esempio che lo mostra, così la prossima persona può correggerlo in fretta. Come per `TODO`, elimina il marcatore una volta corretto il bug, ma mantieni il commento JSDoc, che è ancora vero.
