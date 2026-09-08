Una **Map** memorizza **coppie chiave-valore**: ogni valore è salvato sotto una chiave, e usi quella chiave per ritrovare il valore.
Crei una map vuota con `new Map()`, aggiungi una coppia con `set(key, value)` e leggi un valore con `get(key)`:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// prints 30
```
Chiamare `set()` con una chiave già esistente sostituisce il suo valore.

---

Una map ha alcuni altri metodi e proprietà essenziali:
- `has(key)` restituisce `true` se la chiave esiste
- `delete(key)` rimuove la coppia con quella chiave
- `size` è il numero di coppie memorizzate

```javascript
let stock = new Map();
stock.set("apple", 3);
stock.set("pear", 5);
console.log(stock.has("apple"));
// prints true
stock.delete("pear");
console.log(stock.size);
// prints 1
```
Nota che `size` è una proprietà, non un metodo, quindi non ha parentesi.

---

Chiedere a una map una chiave che non contiene non è un errore: `get()` restituisce semplicemente `undefined`.
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// prints undefined
```
Per questo esiste `has()`: ti permette di distinguere una chiave mancante da una chiave il cui valore è proprio `undefined`.
`set()` restituisce la map stessa, quindi le chiamate possono essere concatenate:
```javascript
ages.set("Bob", 25).set("Cy", 41);
```

---

In un oggetto semplice, ogni chiave viene trasformata in una stringa: `user[1]` e `user["1"]` sono la stessa chiave.
Una map conserva il **tipo** delle sue chiavi, quindi un numero, una stringa, un booleano o persino un oggetto possono essere ciascuno una chiave diversa:
```javascript
let lookup = new Map();
lookup.set(1, "number one");
lookup.set("1", "string one");
console.log(lookup.size);
// prints 2
let alice = { name: "Alice" };
lookup.set(alice, "an object key");
console.log(lookup.get(alice));
// prints an object key
```
Le chiavi oggetto vengono confrontate per identità: solo lo stesso identico oggetto recupera il valore.

---

Una map ricorda l'ordine in cui le coppie sono state aggiunte, e puoi scorrerla con `for...of`.
Il metodo `entries()` fornisce ogni coppia come un array `[key, value]`, che puoi destrutturare direttamente nel ciclo:
```javascript
let stock = new Map();
stock.set("apple", 3);
stock.set("pear", 5);
for (const [name, qty] of stock.entries()) {
  console.log(`${name}: ${qty}`);
}
// prints apple: 3
// prints pear: 5
```
Scorrere direttamente la map, `for (const [name, qty] of stock)`, fa esattamente la stessa cosa.

---

Quando ti serve solo un lato delle coppie, usa `keys()` o `values()` nel ciclo invece di `entries()`:
```javascript
let prices = new Map();
prices.set("tea", 2);
prices.set("cake", 4);
for (const name of prices.keys()) {
  console.log(name);
}
// prints tea
// prints cake
for (const price of prices.values()) {
  console.log(price);
}
// prints 2
// prints 4
```

---

Invece di chiamare `set()` molte volte, puoi costruire una map in un colpo solo passando un **array di coppie** a `new Map()`:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// prints 2
```
Poiché `Object.entries(obj)` restituisce esattamente un array di coppie del genere, è il modo più veloce per trasformare un oggetto in una map:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// prints 30
```
