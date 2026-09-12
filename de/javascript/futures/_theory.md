Manche Operationen sind nicht sofort fertig: das Herunterladen einer Datei, das Lesen aus einer Datenbank, das Warten auf einen Timer. JavaScript friert nicht ein, während sie laufen. Stattdessen gibt es dir ein **`Promise`**: ein Objekt, das für einen Wert steht, der erst **später** verfügbar ist.

Eine mit **`async`** markierte Funktion gibt immer ein Promise zurück. Was auch immer die Funktion zurückgibt, wird zum Wert innerhalb dieses Promises:
```javascript
async function fetchNumber() {
  return 42;
}
```
Um den Wert aus einem Promise zu holen, verwendest du **`await`**. Es pausiert die Funktion, bis das Promise seinen Wert hat, und gibt dir dann den reinen Wert. `await` ist nur innerhalb einer `async`-Funktion erlaubt:
```javascript
async function main() {
  const n = await fetchNumber();
  console.log(n);
  // prints 42
}

main();
```
Ohne `await` wäre `n` das Promise selbst und `console.log(n)` würde `Promise { 42 }` statt der Zahl ausgeben.

---

Das Setzen von `async` vor eine Funktion verändert, was sie zurückgibt: Der Körper berechnet weiterhin einen gewöhnlichen Wert, aber der Aufrufer erhält ein Promise, das ihn umschließt.
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
Die beiden Funktionen enthalten denselben Code; nur die Art, wie du das Ergebnis liest, unterscheidet sich. `shoutLater("hi")` muss innerhalb einer anderen `async`-Funktion abgewartet werden, um `"HI"` zurückzubekommen.

Eine Funktion mit `async` zu markieren kostet nichts, wenn es nichts zu warten gibt, und genau das erlaubt dir später, darin `await` zu verwenden.

---

Wenn der Wert wirklich erst später ankommt, baust du das Promise selbst mit **`new Promise`**. Es nimmt eine Funktion entgegen, die einen **`resolve`**-Callback erhält: Rufe `resolve(value)` auf, wenn der Wert bereit ist, und das Promise wird mit ihm erfüllt.
```javascript
const soon = new Promise((resolve) => {
  setTimeout(() => resolve("done"), 1000);
});
```
`setTimeout(callback, ms)` plant, dass `callback` nach `ms` Millisekunden ausgeführt wird, und kehrt sofort zurück, sodass in der Zwischenzeit nichts blockiert wird.

Die an `new Promise` übergebene Funktion läuft sofort los, aber das Promise bleibt **pending**, bis `resolve` aufgerufen wird. Das Abwarten mit `await` liefert den Wert:
```javascript
async function main() {
  console.log(await soon);
  // prints done, about one second later
}

main();
```

---

Ein Promise befindet sich immer in einem von drei Zuständen:

- **pending**: die Arbeit läuft noch;
- **fulfilled**: die Arbeit war erfolgreich und das Promise hält einen Wert;
- **rejected**: die Arbeit ist fehlgeschlagen und das Promise hält einen Fehler.

Ein Promise startet pending und ändert seinen Zustand höchstens einmal. Sobald es fulfilled oder rejected ist, ist es **settled** und ändert sich nie wieder.

Der Aufruf einer `async`-Funktion wartet nie: Sie startet die Arbeit und gibt dir sofort ein pending Promise zurück, sodass die Zeile nach dem Aufruf ausgeführt wird, bevor die Arbeit fertig ist. Dieses Promise ist ein normales Objekt, nicht der Wert darin, weshalb das Vergessen von `await` so ein häufiger Fehler ist.

---

`await` ist nicht die einzige Möglichkeit, ein Promise zu lesen. Jedes Promise hat eine **`.then(callback)`**-Methode: Der Callback erhält den Wert, sobald das Promise erfüllt ist.
```javascript
Promise.resolve(21).then((n) => {
  console.log(n);
  // prints 21
});
```
**`Promise.resolve(value)`** baut ein Promise, das bereits mit `value` erfüllt ist, was praktisch ist, wenn du den Wert schon zur Hand hast, aber ein Promise zurückgeben musst.

`.then` gibt ein **neues** Promise zurück, das mit dem erfüllt ist, was der Callback zurückgibt, sodass sich Aufrufe **verketten** lassen, wobei jeder Schritt mit dem Ergebnis des vorherigen arbeitet:
```javascript
Promise.resolve(21)
  .then((n) => n * 2)
  .then((n) => console.log(n));
// prints 42
```

---

Eine `async`-Funktion liest sich von oben nach unten wie jede andere Funktion auch: `await` pausiert sie einfach, bis das abgewartete Promise erfüllt ist, dann läuft die Ausführung in der nächsten Zeile weiter.
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
Beachte die letzte Zeile: Eine `async`-Funktion muss immer noch **aufgerufen** werden. `main` ohne die Klammern zu schreiben, definiert die Arbeit, startet sie aber nie, und es wird nichts ausgegeben.

---

Asynchrone Arbeit kann auch fehlschlagen. Die Funktion, der `new Promise` übergeben wird, erhält einen zweiten Callback, **`reject`**: Rufe `reject(error)` auf, und das Promise wird statt erfüllt abgelehnt.
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
Lehne immer mit einem `Error`-Objekt ab: Es trägt eine `message` und einen Stack-Trace mit sich, ein bloßer String nicht.

Eine Ablehnung liest man mit **`.catch(callback)`**, dem Spiegelbild von `.then`. **`Promise.reject(error)`** baut ein Promise, das bereits abgelehnt ist, so wie `Promise.resolve` ein erfülltes baut:
```javascript
readAge(-1).catch((error) => {
  console.log(error.message);
  // prints negative age
});
```
Sowohl `resolve` als auch `reject` aufzurufen oder eines davon zweimal ändert nichts: Nur der erste Aufruf zählt.

---

`.then`, `.catch` und `.finally` sind Glieder derselben Kette. Eine Ablehnung überspringt jedes `.then`, bis sie auf ein `.catch` trifft; sobald der `.catch`-Callback einen Wert zurückgibt, wird die Kette wieder erfüllt und läuft normal weiter.

**`.finally(callback)`** läuft, wenn sich die Kette settled, egal ob sie erfüllt oder abgelehnt wurde. Sein Callback nimmt kein Argument entgegen und sein Rückgabewert wird ignoriert, sodass der Wert zum nächsten `.then` weiterfließt. Es ist der richtige Ort für Aufräumarbeiten wie das Ausblenden eines Spinners:
```javascript
Promise.reject(new Error("no network"))
  .then((value) => `ok: ${value}`)
  .catch((error) => `error: ${error.message}`)
  .finally(() => console.log("cleanup"))
  .then((message) => console.log(message));
// prints cleanup, then error: no network
```

---

Innerhalb einer `async`-Funktion brauchst du kein `.catch`. Das Abwarten eines abgelehnten Promises mit `await` **wirft** den Fehler, sodass die gewöhnliche `try` / `catch` / `finally`-Anweisung ihn behandelt:
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
Umgekehrt gilt dasselbe: Ein `throw` innerhalb einer `async`-Funktion lässt den Aufrufer nicht abstürzen, sondern lehnt das Promise ab, das die Funktion zurückgegeben hat.
```javascript
async function risky() {
  throw new Error("boom");
}
// risky() returns a promise rejected with Error("boom")
```
Wie bei jedem `try`-Block werden die Zeilen nach dem fehlgeschlagenen `await` übersprungen, der `catch`-Block läuft, und der `finally`-Block läuft in beiden Fällen.

---

Eine häufige Verwendung von `try` / `catch` um `await` ist es, einen Fehler durch einen sinnvollen Standardwert zu ersetzen, sodass der Aufrufer sich nie mit dem Fehler befassen muss:
```javascript
async function sizeOf(path) {
  try {
    return await measure(path);
  } catch (error) {
    return 0;
  }
}
```
Behalte das `await` vor `measure(path)` bei, auch wenn der Wert sofort zurückgegeben wird. Ohne es verlässt das Promise die Funktion, ohne je durch den `try`-Block zu gehen, und eine Ablehnung würde das `catch` umgehen.

---

Wenn mehrere Ergebnisse benötigt werden, verschwendet es Zeit, sie nacheinander abzuwarten: Jedes startet erst, wenn das vorherige fertig ist. **`Promise.all(promises)`** nimmt ein Array von Promises, die bereits laufen, entgegen und gibt ein einzelnes Promise zurück, das mit einem Array aller ihrer Werte erfüllt wird:
```javascript
const results = await Promise.all([fetchUser(), fetchOrders()]);
```
Zwei Regeln sind merkenswert:

- die Werte kommen **in der Reihenfolge des Arrays** zurück, nicht in der Reihenfolge, in der sie fertig wurden;
- wenn ein Promise abgelehnt wird, wird das von `Promise.all` zurückgegebene Promise sofort mit diesem ersten Fehler abgelehnt, und die anderen Werte gehen verloren.

---

`Promise.all` funktioniert mit einem Array beliebiger Länge, auch mit einem leeren: Das Abwarten von `Promise.all([])` liefert sofort ein leeres Array zurück. So kann man gefahrlos eine zur Laufzeit erstellte Liste übergeben, ohne einen Sonderfall für „nichts zu warten“ zu brauchen.
```javascript
const values = await Promise.all(items);
console.log(values.length === items.length);
// prints true
```
Das zurückgegebene Array hat immer genau so viele Einträge wie das übergebene Array, an denselben Positionen, sodass man darüber iterieren kann wie über jedes andere Array.

---

Der Unterschied zwischen **sequenziellem** und **parallelem** Warten entscheidet sich danach, *wo* du `await` setzt:
```javascript
// sequential: about 300 + 300 = 600 ms
const a = await load("a");
const b = await load("b");

// parallel: about 300 ms
const [a, b] = await Promise.all([load("a"), load("b")]);
```
In der ersten Version startet der zweite Download erst, wenn der erste fertig ist, weil `await` die Funktion in dieser Zeile pausiert. In der zweiten werden beide Aufrufe getätigt, bevor irgendetwas abgewartet wird, sodass beide Downloads bereits laufen, während `Promise.all` wartet.

Verwende sequenzielles Warten nur, wenn die zweite Aufgabe wirklich das Ergebnis der ersten braucht. Sonst starte zuerst alles und warte gemeinsam ab.

---

`Promise.all` gibt auf, sobald ein Promise abgelehnt wird. Wenn du trotzdem jedes Ergebnis willst, verwende **`Promise.allSettled(promises)`**: Es wird nie abgelehnt, sondern mit einem kleinen Objekt je Promise erfüllt, in derselben Reihenfolge:

- `{ status: "fulfilled", value: ... }` für die erfolgreichen;
- `{ status: "rejected", reason: ... }` für die fehlgeschlagenen.

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
Lies `value` nur, wenn `status` `"fulfilled"` ist, und `reason` nur, wenn es `"rejected"` ist: Die andere Eigenschaft fehlt schlicht.

---

**`Promise.race(promises)`** settled, sobald das **erste** der Promises settled, und übernimmt sein Ergebnis: erfüllt mit dem ersten Wert oder abgelehnt mit dem ersten Fehler. Die anderen werden nicht abgebrochen, sie laufen weiter, aber was auch immer sie liefern, wird ignoriert.
```javascript
const winner = await Promise.race([slowServer(), fastServer()]);
```
Die typische Verwendung ist eine Frist: Lies die eigentliche Arbeit gegen ein Promise, das nach einer Weile fehlschlägt, und du erhältst entweder das Ergebnis oder einen Timeout-Fehler.

Vorsicht bei einem leeren Array: `Promise.race([])` bleibt für immer pending, weil nichts da ist, das es setzen könnte.

---

Setzt man die letzten Bausteine zusammen, entsteht ein kleines Werkzeug, das in fast jeder echten Anwendung verwendet wird: eine Frist. Baue ein Promise, das nach `ms` Millisekunden abgelehnt wird, lies es gegen die eigentliche Arbeit, und welches auch immer zuerst settled, bestimmt das Ergebnis:
```javascript
const timer = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("timeout")), ms);
});
return Promise.race([work, timer]);
```
Ein Promise aus einer `async`-Funktion zurückzugeben ist in Ordnung: Das Promise, das die Funktion zurückgibt, folgt ihm, sodass der Aufrufer den endgültigen Wert abwartet und kein Promise in einem Promise.
