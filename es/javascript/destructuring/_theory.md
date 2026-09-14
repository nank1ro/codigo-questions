Leer valores de un array un índice a la vez es engorroso:
```javascript
const point = [3, 7];
const x = point[0];
const y = point[1];
```
**La destructuración** hace el mismo trabajo en una línea. A la izquierda de `=` escribes un patrón que se parece al propio array, y cada nombre dentro de él recibe el elemento en la misma posición:
```javascript
const point = [3, 7];
const [x, y] = point;
console.log(x, y);
// prints 3 7
```
El patrón no tiene que cubrir todo el array: los elementos extra simplemente se ignoran, y un nombre sin elemento correspondiente se convierte en `undefined`.

---

La destructuración es más útil justo donde llega un array: un argumento de función, o el resultado de una llamada. En lugar de conservar el array e indexarlo por todas partes, lo desempaquetas una vez y das a las partes nombres reales:
```javascript
function middle(range) {
    const [start, end] = range;
    return (start + end) / 2;
}
console.log(middle([0, 10]));
// prints 5
```
No se copia ni se cambia nada en el array original, el patrón solo lee de él.

---

A veces solo importa un elemento del interior del array. Puedes dejar una posición vacía en el patrón, conservando la coma que la separa: una posición vacía así se llama un **hueco**, y se salta el elemento sin nombrarlo:
```javascript
const rgb = [255, 128, 64];
const [, , blue] = rgb;
console.log(blue);
// prints 64
```
Cuenta las comas, no los nombres: cada coma adelanta el patrón una posición, haya o no un nombre delante de ella.

---

Un array no siempre es tan largo como el patrón espera. Escribir `= value` después de un nombre le da un **valor por defecto**, que se usa cada vez que el array no tiene nada en esa posición:
```javascript
const size = [1920];
const [width, height = 1080] = size;
console.log(width, height);
// prints 1920 1080
```
El valor por defecto solo se evalúa cuando hace falta, así que incluso puede ser una llamada a una función, y se puede dar un valor por defecto a cualquier posición, no solo a la última.

---

Un patrón también puede quedar a la izquierda de una asignación normal, sin `const` ni `let` delante, y entonces escribe en variables que ya existen. Eso convierte el intercambio de dos valores en una sola línea, sin variable temporal:
```javascript
let a = 1;
let b = 2;
[a, b] = [b, a];
console.log(a, b);
// prints 2 1
```
El lado derecho se construye primero, así que ambos valores antiguos ya están a salvo dentro del array temporal cuando ocurre la asignación. Ojo al punto y coma de la línea anterior: de lo contrario, una línea que empieza con `[` se leería como un índice de lo que venga antes.

---

Los objetos también se pueden destructurar, con llaves en lugar de corchetes. Aquí la posición no significa nada: cada nombre se empareja con la **clave** que se escribe igual:
```javascript
const user = { name: "Ada", age: 36 };
const { age, name } = user;
console.log(name, age);
// prints Ada 36
```
Intercambiar `age` y `name` en el patrón no cambia nada, y las claves que el patrón no menciona simplemente se quedan fuera. Un nombre sin clave correspondiente se convierte en `undefined`.

---

Los patrones de objeto y los valores por defecto se combinan exactamente igual que los de array, lo que los convierte en una forma ordenada de leer un objeto de configuración cuyas claves pueden estar o no:
```javascript
const options = { theme: "dark" };
const { theme, lang = "en" } = options;
console.log(theme, lang);
// prints dark en
```
Como el patrón entero es una sola sentencia, una función puede desempaquetar todo lo que necesita de su argumento en su misma primera línea.

---

Un patrón de objeto nombra sus variables a partir de las claves, lo cual resulta incómodo cuando las claves son crípticas o ya están ocupadas. Escribir `key: newName` **renombra** la variable:
```javascript
const row = { n: "Ada", y: 1815 };
const { n: name, y: born } = row;
console.log(name, born);
// prints Ada 1815
```
Léelo como "toma `n`, llámalo `name`". Los dos puntos no declaran un tipo, y `n` en sí nunca se crea como variable, solo se crea `name`. Un nombre renombrado todavía puede recibir un valor por defecto, escrito después: `{ n: name = "unknown" }`.

---

Los valores por defecto tienen una regla que sorprende a todo el mundo: se aplican **solo** a `undefined`. Una clave que existe y contiene `null`, `0`, `""` o `false` es un valor real, así que el patrón la toma y el valor por defecto nunca se usa:
```javascript
const { count = 10 } = { count: 0 };
console.log(count);
// prints 0
```
`null` se comporta aquí igual que `0`, aunque a menudo significa "sin valor" en una respuesta de una API. Cuando `null` también deba reemplazarse, destructura primero y recurre después a `??`.

---

Cuando una clave contiene otro objeto o un array, el patrón simplemente puede continuar y describir también esa forma:
```javascript
const user = { name: "Ada", address: { city: "London" } };
const { address: { city } } = user;
console.log(city);
// prints London
```
Cuidado con lo que esa línea crea: `address: { city }` significa "entra en `address`", no "dame `address`", así que solo `city` se convierte en variable. Para conseguir ambos, menciona la clave dos veces: `const { address, address: { city } } = user;`. Los patrones de array y de objeto se anidan libremente entre sí, como en `{ tags: [first] }`.

---

Tomar la cabeza de un array y conservar la cola es una necesidad tan común que los patrones tienen su propia sintaxis para ello. Tres puntos delante del último nombre lo convierten en un **elemento rest**, y recoge todos los elementos restantes en un array completamente nuevo:
```javascript
const queue = ["a", "b", "c"];
const [next, ...waiting] = queue;
console.log(next, waiting);
// prints a [ 'b', 'c' ]
```
Un elemento rest debe ir al final del patrón y no puede tener un valor por defecto: cuando no queda nada, es simplemente un array vacío.

---

Los patrones de objeto también tienen un rest, y en ellos recoge cada clave que el patrón no mencionó en un objeto nuevo:
```javascript
const user = { id: 1, name: "Ada", city: "London" };
const { id, ...profile } = user;
console.log(profile);
// prints { name: 'Ada', city: 'London' }
```
Esta es la forma más corta de construir una copia de un objeto sin una de sus claves: el original nunca se toca, y el objeto rest es uno nuevo que contiene los valores restantes.

---

Un patrón puede sustituir al nombre de un parámetro en la declaración de una función, así que el desempaquetado ocurre en el momento de hacer la llamada:
```javascript
function area({ width, height }) {
    return width * height;
}
console.log(area({ width: 4, height: 3 }));
// prints 12
```
Dentro del cuerpo no hay ninguna variable de objeto en absoluto, solo `width` y `height`. Quien llama pasa un objeto, pero la firma documenta exactamente qué claves lee la función, y las claves pueden llegar en cualquier orden.

---

Un parámetro destructurado con valores por defecto forma un objeto de opciones elegante, pero sigue fallando cuando quien llama no pasa nada: leer una clave de `undefined` lanza un `TypeError`. Dar al patrón entero un valor por defecto `{}` lo arregla:
```javascript
function createUser({ name = "guest", admin = false } = {}) {
    return `${name}/${admin}`;
}
console.log(createUser());
// prints guest/false
```
Lee la línea de fuera hacia dentro: `= {}` aporta un objeto vacío cuando falta el argumento, y después cada valor por defecto interno rellena su propia clave.

---

`Object.entries(obj)` convierte un objeto en un array de pares `[key, value]`. Coloca un patrón de array en la cabecera de un bucle `for...of` y cada par se desempaqueta mientras el bucle avanza:
```javascript
const ages = { ada: 36, bob: 41 };
for (const [name, age] of Object.entries(ages)) {
    console.log(`${name} is ${age}`);
}
// prints ada is 36
// prints bob is 41
```
Esta es la forma legible de recorrer un objeto: sin índice, sin búsquedas, solo los dos nombres que te importan. `Object.keys` y `Object.values` dan cada uno solo un lado, `Object.entries` da ambos.

---

Todo lo visto hasta ahora pertenece a una sola sintaxis, así que las piezas se combinan con libertad: un patrón de objeto puede anidar otro patrón de objeto, que puede contener una clave renombrada con un valor por defecto, junto a un patrón de array que termina en un elemento rest. Una línea describe entonces toda la forma que espera una función:
```javascript
function head({ title, tags: [main, ...extra] }) {
    return `${title} [${main}] +${extra.length}`;
}
console.log(head({ title: "Post", tags: ["js", "web", "dev"] }));
// prints Post [js] +2
```
Mantenlo legible: un patrón que ya no cabe en un par de líneas suele ser señal de que la función está pidiendo demasiado.
