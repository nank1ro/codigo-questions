In JavaScript una funzione è un **valore**: puoi salvarla in una variabile, inserirla in un array e passarla a un'altra funzione come argomento. Una funzione che riceve una funzione come argomento, o che ne restituisce una, si chiama **funzione di ordine superiore**. La funzione passata si chiama **callback**, perché chi la riceve *la richiama* quando ne ha bisogno:
```javascript
function shout(text) {
  return text.toUpperCase() + "!";
}
function twice(fn, value) {
  return fn(fn(value));
}
console.log(twice(shout, "hi"));
// prints HI!!
```
Nota che `shout` viene passata **senza parentesi**: `twice(shout, "hi")` consegna la funzione stessa, mentre `twice(shout("hi"), "hi")` chiamerebbe prima `shout` e passerebbe il suo risultato, la stringa `"HI!"`, che non può essere chiamata.

---

Le funzioni di ordine superiore ti permettono di separare *cosa fare con ogni elemento* da *come scorrere gli elementi*. La parte che scorre viene scritta una volta sola, e la callback decide il resto:
```javascript
function each(items, action) {
  for (let i = 0; i < items.length; i++) {
    action(items[i]);
  }
}
each(["a", "b"], (letter) => console.log(letter));
// prints a and b on two lines
```
La callback riceve un elemento alla volta. Può essere una arrow function scritta in linea, come sopra, o qualsiasi funzione salvata in una variabile. È esattamente così che funzionano internamente i metodi degli array che incontrerai a breve.

---

Il metodo integrato `map` fa quello che fa `transform`: chiama la callback per ogni elemento e raccoglie i risultati in un **nuovo array**. Anche `forEach` chiama la callback per ogni elemento, ma non raccoglie nulla e restituisce sempre `undefined`; usalo solo per gli effetti collaterali, come stampare:
```javascript
const prices = [5, 10];
const doubled = prices.map((p) => p * 2);
prices.forEach((p) => console.log(p));
// prints 5 and 10 on two lines
console.log(doubled);
// prints [ 10, 20 ]
```
Un errore comune è salvare il risultato di `forEach` o concatenare un altro metodo dopo di esso: non c'è nulla da concatenare, perché restituisce `undefined`. Regola pratica: usa `map` quando ti servono i nuovi valori, `forEach` quando devi solo *fare* qualcosa.

---

Altri due metodi di ordine superiore coprono la maggior parte delle esigenze quotidiane.
`filter(callback)` restituisce un nuovo array con i soli elementi per cui la callback restituisce `true`; una callback che risponde sì o no in questo modo si chiama **predicato**.
`reduce(callback, initialValue)` combina tutti gli elementi in un unico valore: la callback riceve l'**accumulatore** (il risultato ottenuto finora) e l'elemento corrente, e restituisce il nuovo accumulatore. Il secondo argomento di `reduce` è l'accumulatore iniziale:
```javascript
const numbers = [3, 8, 5];
console.log(numbers.filter((n) => n > 4));
// prints [ 8, 5 ]
console.log(numbers.reduce((sum, n) => sum + n, 0));
// prints 16
```
Poiché `filter` e `map` restituiscono array, puoi concatenarli e concludere con `reduce`: `numbers.filter(...).map(...).reduce(...)`.

---

Tre metodi rispondono a domande su un array usando un predicato:
- `find(predicate)` restituisce il **primo** elemento per cui il predicato è `true`, o `undefined` se non ce n'è nessuno
- `some(predicate)` restituisce `true` se **almeno un** elemento soddisfa il predicato
- `every(predicate)` restituisce `true` se lo fanno **tutti** gli elementi (e `true` per un array vuoto)
```javascript
const scores = [72, 45, 90];
console.log(scores.find((s) => s < 60));
// prints 45
console.log(scores.some((s) => s === 90), scores.every((s) => s >= 60));
// prints true false
```
Tutti e tre si fermano appena la risposta è nota, quindi non guardano mai più elementi del necessario.

---

`sort(compare)` ordina un array **sul posto** usando una callback che riceve due elementi e restituisce un numero negativo quando il primo deve venire prima, un numero positivo quando deve venire prima il secondo, o `0` quando sono uguali. Per i numeri, `(a, b) => a - b` ordina in modo crescente e `(a, b) => b - a` in modo decrescente.
Senza un comparatore, `sort()` converte ogni elemento in una **stringa** e li confronta carattere per carattere, quindi `10` viene prima di `9` perché `"1"` è minore di `"9"`:
```javascript
console.log([10, 9, 1].sort());
// prints [ 1, 10, 9 ]
console.log([10, 9, 1].sort((a, b) => a - b));
// prints [ 1, 9, 10 ]
```
Poiché `sort` modifica l'array, ordina una copia quando ti serve anche l'ordine originale: `[...numbers].sort(...)`. Per le stringhe usa `(a, b) => a.localeCompare(b)` come comparatore, che ordina il testo alfabeticamente.

---

Il comparatore può guardare qualsiasi parte degli elementi, quindi un array di oggetti si ordina in base a una delle loro proprietà semplicemente confrontando quella proprietà:
```javascript
const items = [{ name: "b", size: 3 }, { name: "a", size: 1 }];
const bySize = [...items].sort((x, y) => x.size - y.size);
console.log(bySize.map((item) => item.name));
// prints [ 'a', 'b' ]
```
Ordinare la copia lascia `items` nel suo ordine originale.

---

Una funzione di ordine superiore può anche **restituire** una funzione. La funzione restituita ricorda le variabili del posto in cui è stata creata, anche dopo che la funzione esterna è terminata: questa si chiama **closure**.
```javascript
function makeMultiplier(factor) {
  return function (n) {
    return n * factor;
  };
}
const triple = makeMultiplier(3);
console.log(triple(5));
// prints 15
console.log(makeMultiplier(10)(5));
// prints 50
```
Ogni chiamata a `makeMultiplier` crea una nuova funzione con il proprio `factor`. È così che costruisci una famiglia di funzioni simili a partire da un unico modello. Lo stesso si può scrivere con le arrow function: `const makeMultiplier = (factor) => (n) => n * factor;`.

---

Una closure mantiene un collegamento **vivo** alla variabile, non una copia del suo valore. Quando più funzioni vengono create nella stessa chiamata, condividono la stessa variabile, e ogni modifica fatta attraverso una è visibile alle altre:
```javascript
function makeCounter() {
  let count = 0;
  return {
    increment: () => { count += 1; },
    value: () => count,
  };
}
const counter = makeCounter();
counter.increment();
counter.increment();
console.log(counter.value());
// prints 2
```
Nessuno può leggere o azzerare `count` dall'esterno se non attraverso quelle due funzioni: la variabile è **privata**. Una seconda chiamata a `makeCounter()` crea un `count` completamente separato.

---

Poiché le funzioni sono valori, puoi scrivere una funzione di ordine superiore che **combina** due funzioni in una nuova. `compose(f, g)` restituisce una funzione che applica prima `g` e poi `f` al risultato, come la notazione matematica *f(g(x))*:
```javascript
const compose = (f, g) => (x) => f(g(x));
const trim = (s) => s.trim();
const shout = (s) => s.toUpperCase();
const clean = compose(shout, trim);
console.log(clean("  hi  "));
// prints HI
```
L'ordine conta: `compose(f, g)` esegue prima `g`, poi `f`. Costruire programmi incollando insieme piccole funzioni in questo modo si chiama **composizione di funzioni**.

---

Una funzione che restituisce una funzione è anche il modo naturale per **adattare** una callback. Supponi di avere un predicato e di averne bisogno dell'opposto per `filter`: invece di riscriverlo, avvolgilo:
```javascript
const isLong = (word) => word.length > 4;
const isShort = (word) => !isLong(word);
console.log(["tree", "forest"].filter(isShort));
// prints [ 'tree' ]
```
Un `not(predicate)` generico farebbe questo per qualsiasi predicato: restituisce una nuova funzione che chiama `predicate` con lo stesso argomento e inverte il risultato con `!`. I predicati per `filter`, `find`, `some` ed `every` ricevono l'elemento come primo argomento, quindi il wrapper deve inoltrare solo quel valore.

---

L'accumulatore di `reduce` non deve essere per forza un numero: può essere una stringa, un array o un oggetto. Partendo da un oggetto vuoto `{}` puoi contare o raggruppare cose in un solo passaggio. Ricorda di **restituire l'accumulatore** dalla callback, altrimenti il passo successivo riceve `undefined`:
```javascript
const votes = ["yes", "no", "yes"];
const tally = votes.reduce((acc, vote) => {
  acc[vote] = (acc[vote] ?? 0) + 1;
  return acc;
}, {});
console.log(tally);
// prints { yes: 2, no: 1 }
```
`acc[vote] ?? 0` legge il conteggio attuale, o `0` quando quella chiave non esiste ancora.

---

Ogni funzione ha un metodo `bind` che restituisce una **nuova** funzione con alcune cose fissate in anticipo. Il suo primo argomento diventa il `this` della nuova funzione; gli argomenti restanti vengono messi davanti a quelli con cui la nuova funzione viene chiamata (un'**applicazione parziale**):
```javascript
function multiply(a, b) {
  return a * b;
}
const double = multiply.bind(null, 2);
console.log(double(21));
// prints 42
```
Fissare `this` è importante per i metodi. Quando un metodo viene copiato fuori dal suo oggetto e chiamato da solo, `this` non si riferisce più all'oggetto, quindi `this.name` diventa `undefined`. `bind` lo blocca sull'oggetto:
```javascript
const user = {
  name: "Ana",
  hello() { return `Hi ${this.name}`; },
};
const loose = user.hello;
console.log(loose());
// prints Hi undefined
const bound = user.hello.bind(user);
console.log(bound());
// prints Hi Ana
```
La funzione originale non viene mai modificata: `bind` costruisce sempre una nuova funzione, il cui `name` è il nome originale preceduto da `bound `.

---

I programmi reali combinano questi metodi in una **pipeline**: filtra gli elementi che ti interessano, mappali sui valori che ti servono e riducili a un risultato. Salvare gli array intermedi in costanti mantiene ogni passo leggibile e ti permette di riutilizzarli:
```javascript
const adults = people.filter((p) => p.age >= 18);
const names = adults.map((p) => p.name);
const totalAge = adults.reduce((sum, p) => sum + p.age, 0);
```
`names.join(", ")` trasforma un array di stringhe in un'unica stringa con gli elementi separati da una virgola e uno spazio.

---

Le closure permettono a una funzione restituita di mantenere uno **stato privato** tra le chiamate. Un helper classico costruito così è `once(fn)`: restituisce una funzione che esegue `fn` solo la prima volta che viene chiamata, ricorda il risultato e restituisce quello stesso risultato a ogni chiamata successiva senza eseguire di nuovo `fn`:
```javascript
let calls = 0;
const init = once(() => {
  calls += 1;
  return "ready";
});
console.log(init(), init(), calls);
// prints ready ready 1
```
Il wrapper ha bisogno di due variabili private: se `fn` è già stata eseguita e il risultato salvato. Entrambe vivono nella closure, invisibili al mondo esterno. Per inoltrare a `fn` ogni argomento del wrapper, dichiara il wrapper con un parametro rest `(...args)` e chiama `fn(...args)`.

---

Tutto si unisce in `groupBy(items, keyFn)`: una funzione di ordine superiore che riceve una callback che decide la **chiave di gruppo** di ogni elemento e restituisce un oggetto che associa ogni chiave all'array degli elementi con quella chiave. `reduce` con un accumulatore oggetto fa tutto il lavoro:
```javascript
const byInitial = groupBy(["hi", "yo", "hey"], (w) => w[0]);
console.log(byInitial);
// prints { h: [ 'hi', 'hey' ], y: [ 'yo' ] }
```
Per ogni elemento, calcola la chiave, crea l'array per quella chiave se non esiste ancora (`acc[key] ?? []`), inserisci l'elemento e restituisci l'accumulatore. Poiché è il chiamante a scegliere `keyFn`, la stessa funzione raggruppa parole per iniziale, persone per città o numeri per parità.
