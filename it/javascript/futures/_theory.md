Alcune operazioni non finiscono subito: scaricare un file, leggere da un database, aspettare un timer. JavaScript non si blocca mentre girano. Invece ti consegna una **`Promise`**: un oggetto che rappresenta un valore che sarà disponibile **più tardi**.

Una funzione contrassegnata **`async`** restituisce sempre una promessa. Qualsiasi cosa restituisca la funzione diventa il valore dentro quella promessa:
```javascript
async function fetchNumber() {
  return 42;
}
```
Per estrarre il valore da una promessa usi **`await`**. Mette in pausa la funzione finché la promessa non ha il suo valore, poi ti dà il valore puro. `await` è consentito solo dentro una funzione `async`:
```javascript
async function main() {
  const n = await fetchNumber();
  console.log(n);
  // prints 42
}

main();
```
Senza `await`, `n` sarebbe la promessa stessa e `console.log(n)` stamperebbe `Promise { 42 }` invece del numero.

---

Aggiungere `async` davanti a una funzione cambia ciò che restituisce: il corpo calcola ancora un valore ordinario, ma chi chiama riceve una promessa che lo avvolge.
```javascript
function shout(text) {
  return text.toUpperCase();
}
async function shoutLater(text) {
  return text.toUpperCase();
}

console.log(shout("hi"));
// prints HI
console.log(shoutLater("hi"));
// prints Promise { 'HI' }
```
Le due funzioni contengono lo stesso codice; cambia solo il modo di leggere il risultato. `shoutLater("hi")` deve essere oggetto di `await` dentro un'altra funzione `async` per restituire `"HI"`.

Contrassegnare una funzione `async` non costa nulla quando non c'è niente da aspettare, ed è ciò che ti permette di usare `await` al suo interno in seguito.

---

Quando il valore arriva davvero più tardi, costruisci la promessa da te con **`new Promise`**. Prende una funzione, che riceve una callback **`resolve`**: chiama `resolve(value)` quando il valore è pronto, e la promessa viene adempiuta con esso.
```javascript
const soon = new Promise((resolve) => {
  setTimeout(() => resolve("done"), 1000);
});
```
`setTimeout(callback, ms)` pianifica l'esecuzione di `callback` dopo `ms` millisecondi e restituisce subito, quindi nel frattempo non viene bloccato nulla.

La funzione passata a `new Promise` viene eseguita subito, ma la promessa resta **in sospeso** finché `resolve` non viene chiamato. Fare `await` su di essa dà il valore:
```javascript
async function main() {
  console.log(await soon);
  // prints done, about one second later
}

main();
```

---

Una promessa si trova sempre in uno di tre stati:

- **in sospeso** (*pending*): il lavoro sta ancora procedendo;
- **adempiuta** (*fulfilled*): il lavoro è riuscito e la promessa contiene un valore;
- **rifiutata** (*rejected*): il lavoro è fallito e la promessa contiene un errore.

Una promessa parte in sospeso e cambia stato al massimo una volta. Una volta adempiuta o rifiutata è **conclusa** (*settled*) e non cambia più.

Chiamare una funzione `async` non aspetta mai: avvia il lavoro e ti consegna subito una promessa in sospeso, quindi la riga dopo la chiamata viene eseguita prima che il lavoro sia finito. Quella promessa è un oggetto normale, non il valore al suo interno, ed è per questo che dimenticare `await` è un errore così comune.

---

`await` non è l'unico modo per leggere una promessa. Ogni promessa ha un metodo **`.then(callback)`**: la callback riceve il valore non appena la promessa viene adempiuta.
```javascript
Promise.resolve(21).then((n) => {
  console.log(n);
  // prints 21
});
```
**`Promise.resolve(value)`** costruisce una promessa che è già adempiuta con `value`, il che è comodo quando hai il valore a portata di mano ma devi restituire una promessa.

`.then` restituisce una **nuova** promessa adempiuta con ciò che la callback restituisce, così le chiamate possono essere **incatenate**, ogni passo lavora sul risultato del precedente:
```javascript
Promise.resolve(21)
  .then((n) => n * 2)
  .then((n) => console.log(n));
// prints 42
```

---

Una funzione `async` si legge dall'alto verso il basso come qualsiasi altra funzione: `await` semplicemente la mette in pausa finché la promessa attesa viene adempiuta, poi l'esecuzione continua alla riga successiva.
```javascript
async function main() {
  console.log("start");
  const value = await Promise.resolve("data");
  console.log(value);
  console.log("done");
}

main();
// prints start, then data, then done
```
Notate l'ultima riga: una funzione `async` deve comunque essere **chiamata**. Scrivere `main` senza le parentesi definisce il lavoro ma non lo avvia mai, e non viene stampato nulla.

---

Anche il lavoro asincrono può fallire. La funzione data a `new Promise` riceve una seconda callback, **`reject`**: chiama `reject(error)` e la promessa diventa rifiutata invece che adempiuta.
```javascript
function readAge(age) {
  return new Promise((resolve, reject) => {
    if (age >= 0) {
      resolve(age);
    } else {
      reject(new Error("negative age"));
    }
  });
}
```
Rifiuta sempre con un oggetto `Error`: porta con sé un `message` e uno stack trace, cosa che una stringa nuda non fa.

Un rifiuto si legge con **`.catch(callback)`**, l'immagine speculare di `.then`. **`Promise.reject(error)`** costruisce una promessa che è già rifiutata, proprio come `Promise.resolve` ne costruisce una adempiuta:
```javascript
readAge(-1).catch((error) => {
  console.log(error.message);
  // prints negative age
});
```
Chiamare `resolve` e `reject` entrambi, o due volte, non cambia nulla: conta solo la prima chiamata.

---

`.then`, `.catch` e `.finally` sono anelli della stessa catena. Un rifiuto salta ogni `.then` finché non incontra un `.catch`; una volta che la callback di `.catch` restituisce un valore, la catena viene adempiuta di nuovo e continua normalmente.

**`.finally(callback)`** viene eseguito quando la catena si conclude, indipendentemente dal fatto che sia stata adempiuta o rifiutata. La sua callback non prende argomenti e il suo valore di ritorno viene ignorato, quindi il valore continua a fluire verso il successivo `.then`. È il posto per le pulizie, come nascondere uno spinner:
```javascript
Promise.reject(new Error("no network"))
  .then((value) => `ok: ${value}`)
  .catch((error) => `error: ${error.message}`)
  .finally(() => console.log("cleanup"))
  .then((message) => console.log(message));
// prints cleanup, then error: no network
```

---

Inside an `async` function you do not need `.catch`. Awaiting a rejected promise **throws** the error, so the ordinary `try` / `catch` / `finally` statement handles it:
```javascript
async function main() {
  try {
    const data = await load();
    console.log(data);
  } catch (error) {
    console.log(`failed: ${error.message}`);
  } finally {
    console.log("end");
  }
}
```
The other direction works too: a `throw` inside an `async` function does not crash the caller, it rejects the promise that the function returned.
```javascript
async function risky() {
  throw new Error("boom");
}
// risky() returns a promise rejected with Error("boom")
```
As with any `try` block, the lines after the failing `await` are skipped, the `catch` block runs, and the `finally` block runs in both cases.

---

A common use of `try` / `catch` around `await` is to replace a failure with a sensible default, so the caller never has to deal with the error:
```javascript
async function sizeOf(path) {
  try {
    return await measure(path);
  } catch (error) {
    return 0;
  }
}
```
Keep the `await` in front of `measure(path)` even though the value is returned straight away. Without it the promise leaves the function without ever passing through the `try` block, and a rejection would escape the `catch`.

---

When several results are needed, awaiting them one after another wastes time: each one starts only when the previous has finished. **`Promise.all(promises)`** takes an array of promises that are already running and returns a single promise fulfilled with an array of all their values:
```javascript
const results = await Promise.all([fetchUser(), fetchOrders()]);
```
Two rules are worth remembering:

- the values come back **in the order of the array**, not in the order in which they finished;
- if any promise is rejected, the promise returned by `Promise.all` is rejected immediately with that first error, and the other values are lost.

---

`Promise.all` works with an array of any length, including an empty one: awaiting `Promise.all([])` gives back an empty array straight away. That makes it safe to pass a list built at run time, without a special case for "nothing to wait for".
```javascript
const values = await Promise.all(items);
console.log(values.length === items.length);
// prints true
```
The array it gives back always has exactly as many entries as the array it received, in the same positions, so it can be looped over like any other array.

---

The difference between **sequential** and **parallel** waiting is decided by *where* you put `await`:
```javascript
// sequential: about 300 + 300 = 600 ms
const a = await load("a");
const b = await load("b");

// parallel: about 300 ms
const [a, b] = await Promise.all([load("a"), load("b")]);
```
In the first version the second download only starts once the first has finished, because `await` pauses the function on that line. In the second, both calls are made before anything is awaited, so both downloads are already running while `Promise.all` waits.

Use sequential awaits only when the second task really needs the result of the first. Otherwise start everything first and await together.

---

`Promise.all` gives up as soon as one promise is rejected. When you want every result anyway, use **`Promise.allSettled(promises)`**: it is never rejected, and it is fulfilled with one small object per promise, in the same order:

- `{ status: "fulfilled", value: ... }` for the ones that succeeded;
- `{ status: "rejected", reason: ... }` for the ones that failed.

```javascript
const results = await Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("nope")),
]);
console.log(results[0].status);
// prints fulfilled
console.log(results[1].reason.message);
// prints nope
```
Read `value` only when `status` is `"fulfilled"`, and `reason` only when it is `"rejected"`: the other property is simply absent.

---

**`Promise.race(promises)`** settles as soon as the **first** of the promises settles, and copies its outcome: fulfilled with the first value, or rejected with the first error. The others are not cancelled, they keep running, but whatever they produce is ignored.
```javascript
const winner = await Promise.race([slowServer(), fastServer()]);
```
The typical use is a deadline: race the real work against a promise that fails after a while, and you get either the result or a timeout error.

Be careful with an empty array: `Promise.race([])` stays pending forever, because there is nothing that could settle it.

---

Putting the last pieces together gives a small tool used in almost every real application: a deadline. Build a promise that is rejected after `ms` milliseconds, race it against the real work, and whichever settles first decides the outcome:
```javascript
const timer = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("timeout")), ms);
});
return Promise.race([work, timer]);
```
Returning a promise from an `async` function is fine: the promise the function gives back follows it, so the caller awaits the final value and not a promise of a promise.
