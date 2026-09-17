Un **Map** almacena **pares clave-valor**: cada valor se guarda bajo una clave, y usas esa clave para volver a encontrar el valor.
Creas un map vacío con `new Map()`, agregas un par con `set(key, value)` y lees un valor con `get(key)`:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// imprime 30
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
// imprime true
stock.delete("pear");
console.log(stock.size);
// imprime 1
```
Ten en cuenta que `size` es una propiedad, no un método, así que no lleva paréntesis.

---

Preguntarle a un map por una clave que no contiene no es un error: `get()` simplemente devuelve `undefined`.
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// imprime undefined
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
// imprime 2
let alice = { name: "Alice" };
lookup.set(alice, "an object key");
console.log(lookup.get(alice));
// imprime una clave de objeto
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
// imprime apple: 3
// imprime pear: 5
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
// imprime tea
// imprime cake
for (const price of prices.values()) {
  console.log(price);
}
// imprime 2
// imprime 4
```

---

En lugar de llamar a `set()` muchas veces, puedes construir un map de una vez pasando un **array de pares** a `new Map()`:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// imprime 2
```
Como `Object.entries(obj)` devuelve exactamente ese array de pares, es la forma más rápida de convertir un objeto en un map:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// imprime 30
```

---

Los maps y los objetos simples almacenan ambos valores bajo claves, pero difieren en algunos aspectos importantes:
- las claves de objeto siempre son strings (o símbolos), las claves de map pueden ser de **cualquier** tipo
- un map conserva el **orden de inserción** exacto de sus pares
- un map conoce su propio `size`, mientras que para un objeto necesitas `Object.keys(obj).length`
- un map empieza realmente vacío, mientras que un objeto hereda claves como `toString` de su prototipo

---

Los maps no tienen métodos de array como `sort()` o `filter()`. Para usarlos, convierte el map (o sus claves o valores) en un array con `Array.from()` o el operador spread `...`:
```javascript
let ages = new Map([["Bob", 25], ["Ann", 30]]);
let pairs = Array.from(ages);
console.log(pairs);
// imprime [ [ 'Bob', 25 ], [ 'Ann', 30 ] ]
let names = [...ages.keys()];
console.log(names);
// imprime [ 'Bob', 'Ann' ]
let values = [...ages.values()];
console.log(values);
// imprime [ 25, 30 ]
```
La conversión opuesta, `Object.fromEntries(ages)`, vuelve a convertir un map en un objeto simple.

---

Como los arrays, los maps tienen un método `forEach()` que llama a una función por cada par.
Ten cuidado con el orden de los parámetros: el callback recibe primero el **valor**, y luego la clave:
```javascript
let stock = new Map([["apple", 3], ["pear", 5]]);
stock.forEach((qty, name) => {
  console.log(`${name} x${qty}`);
});
// imprime apple x3
// imprime pear x5
```

---

`delete(key)` devuelve `true` cuando se eliminó un par y `false` cuando la clave no estaba.
Para eliminar **todos** los pares de una vez, llama a `clear()`:
```javascript
let cart = new Map([["pen", 2], ["ink", 1]]);
console.log(cart.delete("pen"));
// imprime true
console.log(cart.delete("pen"));
// imprime false
cart.clear();
console.log(cart.size);
// imprime 0
```

---

Entonces, ¿cuándo deberías usar un `Map` en lugar de un objeto simple?
- Usa un **Map** cuando las claves se agregan y eliminan en tiempo de ejecución, cuando no son strings, o cuando necesitas `size` y un orden fiable
- Usa un **objeto** para un registro fijo con nombres de campo conocidos, como `{ name, email }`, y siempre que necesites convertir los datos a JSON, ya que `JSON.stringify()` ignora el contenido de un map
