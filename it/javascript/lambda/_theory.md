Una funzione non ha bisogno di un nome. Una **espressione di funzione** crea una funzione come valore, che puoi memorizzare in una variabile e chiamare attraverso di essa:
```javascript
const add = function (a, b) {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
Una **funzione freccia** è un modo più breve di scrivere la stessa cosa: elimina la parola chiave `function` e metti una "freccia grassa" `=>` tra la lista dei parametri e il corpo:
```javascript
const add = (a, b) => {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
Le funzioni freccia sono di solito memorizzate in una `const`, così il nome non può essere riassegnato per errore, e si chiamano esattamente come qualsiasi altra funzione.

---

Le funzioni freccia diventano più corte in due casi comuni.
Quando il corpo è una **singola espressione**, puoi eliminare le parentesi graffe e la parola chiave `return`: il valore dell'espressione viene restituito automaticamente (un **return implicito**):
```javascript
const add = (a, b) => a + b;
console.log(add(2, 3));
// prints 5
```
Quando c'è **esattamente un parametro**, puoi eliminare anche le parentesi tonde attorno ad esso:
```javascript
const double = n => n * 2;
console.log(double(4));
// prints 8
```
Con zero parametri o con due o più, le parentesi sono obbligatorie: `() => 42` e `(a, b) => a + b`.

---

C'è una trappola con il return implicito. Una funzione freccia il cui corpo inizia con `{` viene letta come un **corpo di blocco**, mai come un oggetto letterale:
```javascript
const make = (name) => { name: name };
console.log(make("Ana"));
// prints undefined
```
Qui `{ name: name }` è un blocco che contiene l'etichetta `name:` seguita dall'espressione `name`. Non viene restituito nulla, quindi la chiamata dà `undefined`.
Per restituire un oggetto letterale su una sola riga, racchiudilo tra **parentesi** in modo che JavaScript lo tratti come un'espressione:
```javascript
const make = (name) => ({ name: name });
console.log(make("Ana"));
// prints { name: 'Ana' }
```

---

Racchiudere l'oggetto letterale tra parentesi è il modo standard di costruire oggetti con una funzione freccia su una sola riga, per esempio quando trasformi un paio di valori in un record:
```javascript
const user = (name, age) => ({ name: name, age: age });
console.log(user("Ana", 30).age);
// prints 30
```
Una funzione freccia senza parametri inizia con una coppia di parentesi vuote `()`:
```javascript
const empty = () => ({});
console.log(empty());
// prints {}
```

---

Le funzioni freccia danno il meglio come **callback**: funzioni passate come argomenti ad altre funzioni. I metodi degli array sono l'esempio più comune.
`map(callback)` restituisce un nuovo array con il risultato del callback per ogni elemento, e `filter(callback)` restituisce un nuovo array con solo gli elementi per cui il callback restituisce `true`:
```javascript
const numbers = [1, 2, 3, 4];
console.log(numbers.map((n) => n * 10));
// prints [ 10, 20, 30, 40 ]
console.log(numbers.filter((n) => n > 2));
// prints [ 3, 4 ]
```
Entrambi restituiscono un nuovo array e lasciano intatto l'originale, quindi puoi concatenarli: `numbers.filter(...).map(...)`.

---

Altri due metodi degli array accettano un callback.
`forEach(callback)` chiama il callback una volta per ogni elemento e non restituisce nulla; usalo per effetti collaterali come la stampa.
`reduce(callback, initialValue)` riduce l'array a un singolo valore: il callback riceve il valore accumulato fino a quel momento e l'elemento corrente, e restituisce il nuovo valore accumulato:
```javascript
const numbers = [1, 2, 3];
numbers.forEach((n) => console.log(n));
// prints 1, 2 and 3 on three lines
const total = numbers.reduce((sum, n) => sum + n, 0);
console.log(total);
// prints 6
```

---

`sort(compare)` ordina un array sul posto usando un callback che riceve due elementi e restituisce un numero negativo quando il primo deve venire prima, un numero positivo quando deve venire prima il secondo, o `0` quando sono uguali. Per i numeri, `(a, b) => a - b` ordina in modo crescente e `(a, b) => b - a` in modo decrescente.
`find(callback)` restituisce il primo elemento per cui il callback restituisce `true`, o `undefined` se non ce n'è nessuno:
```javascript
const scores = [50, 90, 70];
scores.sort((a, b) => a - b);
console.log(scores);
// prints [ 50, 70, 90 ]
console.log(scores.find((s) => s > 60));
// prints 70
```

---

I parametri delle funzioni freccia supportano le stesse funzionalità dei parametri delle funzioni normali.
Un **valore predefinito** viene usato quando l'argomento è omesso o è `undefined`:
```javascript
const greet = (name = "World") => `Hello, ${name}!`;
console.log(greet());
// prints Hello, World!
console.log(greet("Ana"));
// prints Hello, Ana!
```
Nota che un parametro con un valore predefinito ha sempre bisogno delle parentesi, anche quando è l'unico: `name = "World" => ...` è un errore di sintassi.

---

Un **parametro rest** `...name` raccoglie un numero qualsiasi di argomenti in un array, e funziona anche nelle funzioni freccia:
```javascript
const count = (...items) => items.length;
console.log(count("a", "b", "c"));
// prints 3
```
Anche le funzioni normali hanno un oggetto nascosto `arguments`, simile a un array, che contiene tutti gli argomenti ricevuti. Le funzioni freccia **no**: dentro una freccia, `arguments` si riferisce agli `arguments` della funzione circostante oppure non esiste affatto. Ogni volta che ti servono "tutti gli argomenti" in una funzione freccia, usa un parametro rest.

---

Una funzione ricorda le variabili dell'ambito in cui è stata **creata**, anche dopo che quell'ambito ha finito di essere eseguito. Questa si chiama **closure**.
L'esempio classico è un generatore di contatori: ogni chiamata a `makeCounter` crea un nuovo `count` e restituisce una funzione freccia che continua a usare quello stesso `count`:
```javascript
const makeCounter = () => {
  let count = 0;
  return () => {
    count += 1;
    return count;
  };
};
const next = makeCounter();
console.log(next());
// prints 1
console.log(next());
// prints 2
```
Nessun altro può leggere o azzerare `count`: vive solo dentro la funzione restituita. Una seconda chiamata a `makeCounter()` crea un contatore indipendente con il proprio `count`.

---

Dato che una funzione è un valore, una funzione freccia può **restituire un'altra funzione freccia**. Concatenare due frecce è un modo compatto di scrivere una funzione che costruisce funzioni:
```javascript
const makeAdder = (amount) => (n) => n + amount;
const addTen = makeAdder(10);
console.log(addTen(5));
// prints 15
console.log(makeAdder(1)(5));
// prints 6
```
Leggila da sinistra a destra: `makeAdder` prende `amount` e restituisce `(n) => n + amount`, una funzione freccia che cattura `amount` tramite una closure. `makeAdder(1)(5)` chiama immediatamente la funzione restituita.
