A **Map** stores **key-value pairs**: every value is saved under a key, and you use that key to find the value again.
You create an empty map with `new Map()`, add a pair with `set(key, value)` and read a value with `get(key)`:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// prints 30
```
Calling `set()` with a key that already exists replaces its value.

---

A map has a few more essential methods and properties:
- `has(key)` returns `true` if the key exists
- `delete(key)` removes the pair with that key
- `size` is the number of pairs stored

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
Note that `size` is a property, not a method, so it has no parentheses.

---

Asking a map for a key it does not contain is not an error: `get()` simply returns `undefined`.
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// prints undefined
```
That is why `has()` exists: it lets you tell apart a missing key from a key whose value happens to be `undefined`.
`set()` returns the map itself, so calls can be chained:
```javascript
ages.set("Bob", 25).set("Cy", 41);
```

---

In a plain object every key is turned into a string: `user[1]` and `user["1"]` are the same key.
A map keeps the **type** of its keys, so a number, a string, a boolean or even an object can each be a different key:
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
Object keys are compared by identity: only the very same object gets the value back.

---

A map remembers the order in which pairs were added, and you can loop over it with `for...of`.
The `entries()` method gives every pair as a `[key, value]` array, which you can unpack right in the loop:
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
Looping directly over the map, `for (const [name, qty] of stock)`, does exactly the same thing.

---

When you only need one side of the pairs, use `keys()` or `values()` in the loop instead of `entries()`:
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

Instead of calling `set()` many times, you can build a map in one go by passing an **array of pairs** to `new Map()`:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// prints 2
```
Because `Object.entries(obj)` returns exactly such an array of pairs, it is the quickest way to turn an object into a map:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// prints 30
```

---

Maps and plain objects both store values under keys, but they differ in some important ways:
- object keys are always strings (or symbols), map keys can be **any** type
- a map keeps the exact **insertion order** of its pairs
- a map knows its own `size`, while for an object you need `Object.keys(obj).length`
- a map starts truly empty, while an object inherits keys like `toString` from its prototype

---

Maps do not have array methods like `sort()` or `filter()`. To use them, convert the map (or its keys or values) into an array with `Array.from()` or the spread operator `...`:
```javascript
let ages = new Map([["Bob", 25], ["Ann", 30]]);
let pairs = Array.from(ages);
console.log(pairs);
// prints [ [ 'Bob', 25 ], [ 'Ann', 30 ] ]
let names = [...ages.keys()];
console.log(names);
// prints [ 'Bob', 'Ann' ]
let values = [...ages.values()];
console.log(values);
// prints [ 25, 30 ]
```
The opposite conversion, `Object.fromEntries(ages)`, turns a map back into a plain object.

---

Like arrays, maps have a `forEach()` method that calls a function for every pair.
Be careful with the order of the parameters: the callback receives the **value first**, then the key:
```javascript
let stock = new Map([["apple", 3], ["pear", 5]]);
stock.forEach((qty, name) => {
  console.log(`${name} x${qty}`);
});
// prints apple x3
// prints pear x5
```

---

`delete(key)` returns `true` when a pair was removed and `false` when the key was not there.
To remove **every** pair at once, call `clear()`:
```javascript
let cart = new Map([["pen", 2], ["ink", 1]]);
console.log(cart.delete("pen"));
// prints true
console.log(cart.delete("pen"));
// prints false
cart.clear();
console.log(cart.size);
// prints 0
```

---

So when should you reach for a `Map` instead of a plain object?
- Use a **Map** when keys are added and removed at runtime, when they are not strings, or when you need `size` and reliable ordering
- Use an **object** for a fixed record with known field names, like `{ name, email }`, and whenever you need to convert the data to JSON, since `JSON.stringify()` ignores the content of a map
