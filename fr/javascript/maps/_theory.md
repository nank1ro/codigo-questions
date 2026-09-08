Une **Map** stocke des **paires clé-valeur** : chaque valeur est enregistrée sous une clé, et vous utilisez cette clé pour retrouver la valeur.
Vous créez une map vide avec `new Map()`, ajoutez une paire avec `set(key, value)` et lisez une valeur avec `get(key)` :
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// prints 30
```
Appeler `set()` avec une clé qui existe déjà remplace sa valeur.

---

Une map possède quelques autres méthodes et propriétés essentielles :
- `has(key)` renvoie `true` si la clé existe
- `delete(key)` supprime la paire ayant cette clé
- `size` est le nombre de paires stockées

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
Notez que `size` est une propriété, pas une méthode, elle n'a donc pas de parenthèses.

---

Interroger une map sur une clé qu'elle ne contient pas n'est pas une erreur : `get()` renvoie simplement `undefined`.
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// prints undefined
```
C'est pourquoi `has()` existe : elle vous permet de distinguer une clé absente d'une clé dont la valeur est justement `undefined`.
`set()` renvoie la map elle-même, donc les appels peuvent être chaînés :
```javascript
ages.set("Bob", 25).set("Cy", 41);
```

---

Dans un objet simple, chaque clé est transformée en string : `user[1]` et `user["1"]` sont la même clé.
Une map conserve le **type** de ses clés, donc un nombre, un string, un booléen ou même un objet peuvent chacun être une clé différente :
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
Les clés objet sont comparées par identité : seul l'objet exact récupère la valeur associée.

---

Une map se souvient de l'ordre dans lequel les paires ont été ajoutées, et vous pouvez la parcourir avec `for...of`.
La méthode `entries()` donne chaque paire sous forme d'array `[key, value]`, que vous pouvez déstructurer directement dans la boucle :
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
Parcourir directement la map, `for (const [name, qty] of stock)`, fait exactement la même chose.

---

Quand vous n'avez besoin que d'un côté des paires, utilisez `keys()` ou `values()` dans la boucle au lieu de `entries()` :
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

Au lieu d'appeler `set()` plusieurs fois, vous pouvez construire une map en une seule fois en passant un **array de paires** à `new Map()` :
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// prints 2
```
Comme `Object.entries(obj)` renvoie exactement un tel array de paires, c'est le moyen le plus rapide de transformer un objet en map :
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// prints 30
```
