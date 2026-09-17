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
  // stampa 42
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
// stampa HI
console.log(shoutLater("hi"));
// stampa Promise { 'HI' }
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
  // stampa done, circa un secondo dopo
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
  // stampa 21
});
```
**`Promise.resolve(value)`** costruisce una promessa che è già adempiuta con `value`, il che è comodo quando hai il valore a portata di mano ma devi restituire una promessa.

`.then` restituisce una **nuova** promessa adempiuta con ciò che la callback restituisce, così le chiamate possono essere **incatenate**, ogni passo lavora sul risultato del precedente:
```javascript
Promise.resolve(21)
  .then((n) => n * 2)
  .then((n) => console.log(n));
// stampa 42
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
// stampa start, poi data, poi done
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
  // stampa negative age
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
// stampa cleanup, poi error: no network
```

---

Dentro una funzione `async` non serve `.catch`. Fare `await` di una promessa rifiutata **lancia** l'errore, quindi la normale istruzione `try` / `catch` / `finally` lo gestisce:
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
Funziona anche il percorso opposto: un `throw` dentro una funzione `async` non manda in crash il chiamante, ma rifiuta la promessa restituita dalla funzione.
```javascript
async function risky() {
  throw new Error("boom");
}
// risky() restituisce una promessa rifiutata con Error("boom")
```
Come in ogni blocco `try`, le righe dopo l'`await` che fallisce vengono saltate, il blocco `catch` viene eseguito, e il blocco `finally` viene eseguito in entrambi i casi.

---

Un uso comune di `try` / `catch` attorno a `await` è sostituire un fallimento con un valore predefinito sensato, così il chiamante non deve mai occuparsi dell'errore:
```javascript
async function sizeOf(path) {
  try {
    return await measure(path);
  } catch (error) {
    return 0;
  }
}
```
Mantieni `await` davanti a `measure(path)` anche se il valore viene restituito subito. Senza di esso la promessa lascerebbe la funzione senza mai passare per il blocco `try`, e un rifiuto sfuggirebbe al `catch`.

---

Quando servono più risultati, aspettarli uno dopo l'altro spreca tempo: ognuno parte solo quando il precedente è finito. **`Promise.all(promises)`** prende un array di promesse già in esecuzione e restituisce un'unica promessa adempiuta con un array di tutti i loro valori:
```javascript
const results = await Promise.all([fetchUser(), fetchOrders()]);
```
Due regole vale la pena ricordare:

- i valori tornano **nell'ordine dell'array**, non nell'ordine in cui sono terminati;
- se una qualsiasi promessa viene rifiutata, la promessa restituita da `Promise.all` viene rifiutata immediatamente con quel primo errore, e gli altri valori vengono persi.

---

`Promise.all` funziona con un array di qualsiasi lunghezza, incluso uno vuoto: fare `await` di `Promise.all([])` restituisce subito un array vuoto. Questo rende sicuro passare una lista costruita a runtime, senza bisogno di un caso speciale per "niente da aspettare".
```javascript
const values = await Promise.all(items);
console.log(values.length === items.length);
// stampa true
```
L'array restituito ha sempre esattamente lo stesso numero di elementi dell'array ricevuto, nelle stesse posizioni, quindi può essere ciclato come qualsiasi altro array.

---

La differenza tra attesa **sequenziale** e **parallela** dipende da *dove* metti `await`:
```javascript
// sequenziale: circa 300 + 300 = 600 ms
const a = await load("a");
const b = await load("b");

// parallela: circa 300 ms
const [a, b] = await Promise.all([load("a"), load("b")]);
```
Nella prima versione il secondo download parte solo quando il primo è finito, perché `await` mette in pausa la funzione a quella riga. Nella seconda, entrambe le chiamate vengono fatte prima che qualcosa venga atteso, quindi entrambi i download sono già in esecuzione mentre `Promise.all` aspetta.

Usa gli `await` sequenziali solo quando il secondo compito ha davvero bisogno del risultato del primo. Altrimenti avvia tutto per primo e aspetta insieme.

---

`Promise.all` si arrende non appena una promessa viene rifiutata. Quando vuoi comunque ogni risultato, usa **`Promise.allSettled(promises)`**: non viene mai rifiutata, ed è adempiuta con un piccolo oggetto per ogni promessa, nello stesso ordine:

- `{ status: "fulfilled", value: ... }` per quelle andate a buon fine;
- `{ status: "rejected", reason: ... }` per quelle fallite.

```javascript
const results = await Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("nope")),
]);
console.log(results[0].status);
// stampa fulfilled
console.log(results[1].reason.message);
// stampa nope
```
Leggi `value` solo quando `status` è `"fulfilled"`, e `reason` solo quando è `"rejected"`: l'altra proprietà è semplicemente assente.

---

**`Promise.race(promises)`** si conclude non appena la **prima** delle promesse si conclude, e ne copia l'esito: adempiuta con il primo valore, oppure rifiutata con il primo errore. Le altre non vengono annullate, continuano a girare, ma qualsiasi cosa producano viene ignorata.
```javascript
const winner = await Promise.race([slowServer(), fastServer()]);
```
L'uso tipico è una scadenza: fai gareggiare il lavoro vero contro una promessa che fallisce dopo un po', e ottieni il risultato oppure un errore di timeout.

Fai attenzione con un array vuoto: `Promise.race([])` resta in sospeso per sempre, perché non c'è niente che possa concluderla.

---

Mettendo insieme gli ultimi pezzi si ottiene un piccolo strumento usato in quasi ogni applicazione reale: una scadenza. Costruisci una promessa che viene rifiutata dopo `ms` millisecondi, falla gareggiare contro il lavoro vero, e qualunque delle due si concluda per prima decide l'esito:
```javascript
const timer = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("timeout")), ms);
});
return Promise.race([work, timer]);
```
Restituire una promessa da una funzione `async` va benissimo: la promessa restituita dalla funzione la segue, quindi il chiamante aspetta il valore finale e non una promessa di una promessa.
