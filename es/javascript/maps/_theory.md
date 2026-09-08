Un **Map** almacena **pares clave-valor**: cada valor se guarda bajo una clave, y usas esa clave para volver a encontrar el valor.
Creas un map vacío con `new Map()`, agregas un par con `set(key, value)` y lees un valor con `get(key)`:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// prints 30
```
Llamar a `set()` con una clave que ya existe reemplaza su valor.

---

Un map tiene algunos otros métodos y propiedades esenciales:
- `has(key)` devuelve `true` si la clave existe
- `delete(key)` elimina el par con esa clave
- `size` es el número de pares almacenados

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
Ten en cuenta que `size` es una propiedad, no un método, así que no lleva paréntesis.

---

Preguntarle a un map por una clave que no contiene no es un error: `get()` simplemente devuelve `undefined`.
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// prints undefined
```
Por eso existe `has()`: te permite distinguir una clave ausente de una clave cuyo valor resulta ser `undefined`.
`set()` devuelve el propio map, así que las llamadas se pueden encadenar:
```javascript
ages.set("Bob", 25).set("Cy", 41);
```

---

En un objeto simple, cada clave se convierte en un string: `user[1]` y `user["1"]` son la misma clave.
Un map conserva el **tipo** de sus claves, así que un número, un string, un booleano o incluso un objeto pueden ser cada uno una clave distinta:
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
Las claves de objeto se comparan por identidad: solo el mismísimo objeto recupera el valor.

---

Un map recuerda el orden en que se agregaron los pares, y puedes recorrerlo con `for...of`.
El método `entries()` da cada par como un array `[key, value]`, que puedes desestructurar directamente en el bucle:
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
Recorrer el map directamente, `for (const [name, qty] of stock)`, hace exactamente lo mismo.

---

Cuando solo necesitas un lado de los pares, usa `keys()` o `values()` en el bucle en lugar de `entries()`:
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

En lugar de llamar a `set()` muchas veces, puedes construir un map de una vez pasando un **array de pares** a `new Map()`:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// prints 2
```
Como `Object.entries(obj)` devuelve exactamente ese array de pares, es la forma más rápida de convertir un objeto en un map:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// prints 30
```
