Un **Set** es una colección de valores **únicos**: cada valor puede aparecer como máximo una vez, y no hay un índice para acceder a un valor por posición.
Los sets son perfectos cuando solo te importa *qué* valores están presentes, no cuántas veces ni en qué orden.
Creas un set vacío con `new Set()`, agregas un valor con `add(value)` y compruebas si un valor está presente con `has(value)`:
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// imprime true
console.log(colors.has("green"));
// imprime false
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
// imprime 2
tags.delete("css");
console.log(tags.size);
// imprime 1
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
// imprime 3
```
El operador **spread** `...` funciona al revés y convierte un set de nuevo en un array:
```javascript
let unique = [...distinct];
console.log(unique);
// imprime [ 1, 2, 3 ]
```
`Array.from(distinct)` hace lo mismo.

---

Un set recuerda el orden en que se agregaron los valores, y puedes recorrerlo con `for...of`:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// imprime 3
// imprime 1
// imprime 2
```
Los sets también tienen un método `forEach()` que llama a una función para cada valor:
```javascript
nums.forEach((n) => console.log(n * 10));
// imprime 30
// imprime 10
// imprime 20
```

---

`delete(value)` devuelve `true` cuando el valor fue eliminado y `false` cuando no estaba en el set.
Para eliminar **todos** los valores de una vez, llama a `clear()`:
```javascript
let cart = new Set(["pen", "ink"]);
console.log(cart.delete("pen"));
// imprime true
console.log(cart.delete("pen"));
// imprime false
cart.clear();
console.log(cart.size);
// imprime 0
```

---

Un set decide si dos valores son "iguales" con casi la misma regla que `===` (excepto que `NaN` cuenta como igual a sí mismo). Para strings y números esto compara el contenido, pero **los objetos se comparan por referencia**: dos objetos literales con campos idénticos son dos valores distintos.
```javascript
let alice = { name: "Alice" };
let people = new Set();
people.add(alice);
people.add(alice);
console.log(people.size);
// imprime 1
people.add({ name: "Alice" });
console.log(people.size);
// imprime 2
```
Solo se ignora agregar de nuevo exactamente el mismo objeto.

---

Combinar spread y `filter()` te da las operaciones clásicas de la teoría de conjuntos. Cada una construye una colección **nueva** y deja los originales sin cambios:
- **unión**, todo valor que esté en `a`, en `b` o en ambos: `new Set([...a, ...b])`
- **intersección**, solo los valores que están en **ambos**: `[...a].filter((x) => b.has(x))`
- **diferencia**, los valores de `a` que **no** están en `b`: `[...a].filter((x) => !b.has(x))`

```javascript
let a = new Set([1, 2, 3]);
let b = new Set([3, 4]);
console.log([...new Set([...a, ...b])]);
// imprime [ 1, 2, 3, 4 ]
console.log([...a].filter((x) => b.has(x)));
// imprime [ 3 ]
console.log([...a].filter((x) => !b.has(x)));
// imprime [ 1, 2 ]
```
Los motores de JavaScript recientes también ofrecen `a.union(b)`, `a.intersection(b)` y `a.difference(b)` directamente en los sets, pero las versiones con spread y filter funcionan en todas partes.

---

Para mantener la misma interfaz que `Map`, un set ofrece los métodos iteradores `values()`, `keys()` y `entries()`.
Como un set no tiene claves, `keys()` es simplemente otro nombre para `values()`, y `entries()` produce cada valor **dos veces**, como un par `[value, value]`:
```javascript
let letters = new Set(["a", "b"]);
console.log([...letters.values()]);
// imprime [ 'a', 'b' ]
console.log([...letters.entries()]);
// imprime [ [ 'a', 'a' ], [ 'b', 'b' ] ]
```
En la práctica rara vez los necesitas: `for...of` y spread ya recorren los valores directamente.

---

`new Set()` acepta cualquier **iterable**, no solo arrays. Un string es iterable carácter por carácter, así que te da los caracteres distintos de un texto:
```javascript
let letters = new Set("hello");
console.log([...letters]);
// imprime [ 'h', 'e', 'l', 'o' ]
```
