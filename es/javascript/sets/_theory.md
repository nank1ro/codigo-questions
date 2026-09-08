Un **Set** es una colección de valores **únicos**: cada valor puede aparecer como máximo una vez, y no hay un índice para acceder a un valor por posición.
Los sets son perfectos cuando solo te importa *qué* valores están presentes, no cuántas veces ni en qué orden.
Creas un set vacío con `new Set()`, agregas un valor con `add(value)` y compruebas si un valor está presente con `has(value)`:
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// prints true
console.log(colors.has("green"));
// prints false
```

---

Agregar un valor que ya está en el set no hace **nada**: los duplicados simplemente se ignoran.
Dos elementos esenciales más:
- `delete(value)` elimina el valor del set
- `size` es la cantidad de valores almacenados (una propiedad, así que sin paréntesis)

```javascript
let tags = new Set();
tags.add("js");
tags.add("css");
tags.add("js");
console.log(tags.size);
// prints 2
tags.delete("css");
console.log(tags.size);
// prints 1
```

---

`add()` devuelve el propio set, así que varias llamadas se pueden encadenar:
```javascript
let letters = new Set();
letters.add("a").add("b");
```
Encadenes o no, un valor que ya está presente nunca se agrega una segunda vez, así que `size` cuenta cada valor distinto solo una vez.

---

Puedes crear un set de una sola vez pasando un array a `new Set()`. Los duplicados del array se eliminan, así que esta es la forma más rápida de encontrar los valores distintos de un array:
```javascript
let nums = [1, 2, 2, 3, 3, 3];
let distinct = new Set(nums);
console.log(distinct.size);
// prints 3
```
El operador **spread** `...` funciona al revés y convierte un set de nuevo en un array:
```javascript
let unique = [...distinct];
console.log(unique);
// prints [ 1, 2, 3 ]
```
`Array.from(distinct)` hace lo mismo.

---

Un set recuerda el orden en que se agregaron los valores, y puedes recorrerlo con `for...of`:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// prints 3
// prints 1
// prints 2
```
Los sets también tienen un método `forEach()` que llama a una función para cada valor:
```javascript
nums.forEach((n) => console.log(n * 10));
// prints 30
// prints 10
// prints 20
```
