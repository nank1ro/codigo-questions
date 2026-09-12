Some operations do not finish immediately: downloading a file, reading from a database, waiting for a timer. JavaScript does not freeze while they run. Instead it hands you a **`Promise`**: an object that stands for a value which will be available **later**.

A function marked **`async`** always returns a promise. Whatever the function returns becomes the value inside that promise:
```javascript
async function fetchNumber() {
  return 42;
}
```
To take the value out of a promise you use **`await`**. It pauses the function until the promise has its value, then gives you the plain value. `await` is only allowed inside an `async` function:
```javascript
async function main() {
  const n = await fetchNumber();
  console.log(n);
  // prints 42
}

main();
```
Without `await`, `n` would be the promise itself and `console.log(n)` would print `Promise { 42 }` instead of the number.

---

Adding `async` in front of a function changes what it gives back: the body still computes an ordinary value, but the caller receives a promise wrapped around it.
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
The two functions contain the same code; only the way you read the result differs. `shoutLater("hi")` must be awaited inside another `async` function to give back `"HI"`.

Marking a function `async` costs nothing when there is no waiting to do, and it is what lets you use `await` inside it later.

---

When the value really does arrive later, you build the promise yourself with **`new Promise`**. It takes one function, which receives a **`resolve`** callback: call `resolve(value)` when the value is ready, and the promise is fulfilled with it.
```javascript
const soon = new Promise((resolve) => {
  setTimeout(() => resolve("done"), 1000);
});
```
`setTimeout(callback, ms)` schedules `callback` to run after `ms` milliseconds and returns immediately, so nothing is blocked in the meantime.

The function passed to `new Promise` runs straight away, but the promise stays **pending** until `resolve` is called. Awaiting it gives the value:
```javascript
async function main() {
  console.log(await soon);
  // prints done, about one second later
}

main();
```

---

A promise is always in one of three states:

- **pending**: the work is still going on;
- **fulfilled**: the work succeeded and the promise holds a value;
- **rejected**: the work failed and the promise holds an error.

A promise starts pending and changes state at most once. Once it is fulfilled or rejected it is **settled** and never changes again.

Calling an `async` function never waits: it starts the work and hands you a pending promise immediately, so the line after the call runs before the work is finished. That promise is a normal object, not the value inside it, which is why forgetting `await` is such a common mistake.

---

`await` is not the only way to read a promise. Every promise has a **`.then(callback)`** method: the callback receives the value as soon as the promise is fulfilled.
```javascript
Promise.resolve(21).then((n) => {
  console.log(n);
  // prints 21
});
```
**`Promise.resolve(value)`** builds a promise that is already fulfilled with `value`, which is handy when you have the value at hand but must return a promise.

`.then` returns a **new** promise fulfilled with whatever the callback returns, so calls can be **chained**, each step working on the result of the previous one:
```javascript
Promise.resolve(21)
  .then((n) => n * 2)
  .then((n) => console.log(n));
// prints 42
```

---

An `async` function reads from top to bottom like any other function: `await` simply pauses it until the awaited promise is fulfilled, then execution continues on the next line.
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
Notice the last line: an `async` function still has to be **called**. Writing `main` without the parentheses defines the work but never starts it, and nothing is printed.

---

Asynchronous work can also fail. The function given to `new Promise` receives a second callback, **`reject`**: call `reject(error)` and the promise becomes rejected instead of fulfilled.
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
Always reject with an `Error` object: it carries a `message` and a stack trace, which a bare string does not.

A rejection is read with **`.catch(callback)`**, the mirror image of `.then`. **`Promise.reject(error)`** builds a promise that is already rejected, just like `Promise.resolve` builds a fulfilled one:
```javascript
readAge(-1).catch((error) => {
  console.log(error.message);
  // prints negative age
});
```
Calling `resolve` and `reject` both, or twice, changes nothing: only the first call counts.

---

`.then`, `.catch` and `.finally` are links of the same chain. A rejection skips every `.then` until it meets a `.catch`; once the `.catch` callback returns a value, the chain is fulfilled again and continues normally.

**`.finally(callback)`** runs when the chain settles, no matter whether it was fulfilled or rejected. Its callback takes no argument and its return value is ignored, so the value keeps flowing to the next `.then`. It is the place for clean-up such as hiding a spinner:
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
