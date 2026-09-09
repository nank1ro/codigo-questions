En JavaScript una función es un **valor**: puedes guardarla en una variable, ponerla en un array y pasarla a otra función como argumento. Una función que recibe una función como argumento, o que devuelve una, se llama **función de orden superior**. La función que se pasa se llama **callback**, porque quien la recibe *la llama de vuelta* cuando la necesita:
```javascript
function shout(text) {
  return text.toUpperCase() + "!";
}
function twice(fn, value) {
  return fn(fn(value));
}
console.log(twice(shout, "hi"));
// prints HI!!
```
Fíjate en que `shout` se pasa **sin paréntesis**: `twice(shout, "hi")` entrega la función en sí, mientras que `twice(shout("hi"), "hi")` llamaría primero a `shout` y pasaría su resultado, la cadena `"HI!"`, que no se puede llamar.

---

Las funciones de orden superior te permiten separar *qué hacer con cada elemento* de *cómo recorrer los elementos*. La parte que recorre se escribe una sola vez, y el callback decide el resto:
```javascript
function each(items, action) {
  for (let i = 0; i < items.length; i++) {
    action(items[i]);
  }
}
each(["a", "b"], (letter) => console.log(letter));
// prints a and b on two lines
```
El callback recibe un elemento cada vez. Puede ser una función flecha escrita en línea, como arriba, o cualquier función guardada en una variable. Así es exactamente como funcionan por dentro los métodos de array que verás a continuación.

---

El método integrado `map` hace lo que hace `transform`: llama al callback para cada elemento y recoge los resultados en un **nuevo array**. `forEach` también llama al callback para cada elemento, pero no recoge nada y siempre devuelve `undefined`; úsalo solo para efectos secundarios, como imprimir:
```javascript
const prices = [5, 10];
const doubled = prices.map((p) => p * 2);
prices.forEach((p) => console.log(p));
// prints 5 and 10 on two lines
console.log(doubled);
// prints [ 10, 20 ]
```
Un error habitual es guardar el resultado de `forEach` o encadenar otro método después: no hay nada que encadenar, porque devuelve `undefined`. Regla práctica: usa `map` cuando necesitas los nuevos valores, `forEach` cuando solo necesitas *hacer* algo.

---

Otros dos métodos de orden superior cubren casi todas las necesidades del día a día.
`filter(callback)` devuelve un nuevo array solo con los elementos para los que el callback devuelve `true`; un callback que responde sí o no de esta forma se llama **predicado**.
`reduce(callback, initialValue)` combina todos los elementos en un solo valor: el callback recibe el **acumulador** (el resultado hasta ese momento) y el elemento actual, y devuelve el nuevo acumulador. El segundo argumento de `reduce` es el acumulador inicial:
```javascript
const numbers = [3, 8, 5];
console.log(numbers.filter((n) => n > 4));
// prints [ 8, 5 ]
console.log(numbers.reduce((sum, n) => sum + n, 0));
// prints 16
```
Como `filter` y `map` devuelven arrays, puedes encadenarlos y terminar con `reduce`: `numbers.filter(...).map(...).reduce(...)`.

---

Tres métodos responden preguntas sobre un array con un predicado:
- `find(predicate)` devuelve el **primer** elemento para el que el predicado es `true`, o `undefined` si no hay ninguno
- `some(predicate)` devuelve `true` si **al menos un** elemento cumple el predicado
- `every(predicate)` devuelve `true` si lo cumplen **todos** los elementos (y `true` para un array vacío)
```javascript
const scores = [72, 45, 90];
console.log(scores.find((s) => s < 60));
// prints 45
console.log(scores.some((s) => s === 90), scores.every((s) => s >= 60));
// prints true false
```
Los tres se detienen en cuanto se conoce la respuesta, así que nunca miran más elementos de los necesarios.

---

`sort(compare)` ordena un array **en el sitio** usando un callback que recibe dos elementos y devuelve un número negativo cuando el primero debe ir antes, un número positivo cuando debe ir antes el segundo, o `0` cuando son iguales. Para números, `(a, b) => a - b` ordena de forma ascendente y `(a, b) => b - a` de forma descendente.
Sin comparador, `sort()` convierte cada elemento en una **cadena** y los compara carácter a carácter, así que `10` va antes que `9` porque `"1"` es menor que `"9"`:
```javascript
console.log([10, 9, 1].sort());
// prints [ 1, 10, 9 ]
console.log([10, 9, 1].sort((a, b) => a - b));
// prints [ 1, 9, 10 ]
```
Como `sort` modifica el array, ordena una copia cuando también necesitas el orden original: `[...numbers].sort(...)`. Para cadenas usa `(a, b) => a.localeCompare(b)` como comparador, que ordena el texto alfabéticamente.

---

El comparador puede mirar cualquier parte de los elementos, así que un array de objetos se ordena por una de sus propiedades simplemente comparando esa propiedad:
```javascript
const items = [{ name: "b", size: 3 }, { name: "a", size: 1 }];
const bySize = [...items].sort((x, y) => x.size - y.size);
console.log(bySize.map((item) => item.name));
// prints [ 'a', 'b' ]
```
Ordenar la copia deja `items` en su orden original.

---

Una función de orden superior también puede **devolver** una función. La función devuelta recuerda las variables del lugar donde se creó, incluso después de que la función externa haya terminado: esto se llama **closure**.
```javascript
function makeMultiplier(factor) {
  return function (n) {
    return n * factor;
  };
}
const triple = makeMultiplier(3);
console.log(triple(5));
// prints 15
console.log(makeMultiplier(10)(5));
// prints 50
```
Cada llamada a `makeMultiplier` crea una nueva función con su propio `factor`. Así se construye una familia de funciones parecidas a partir de una sola plantilla. Lo mismo se puede escribir con funciones flecha: `const makeMultiplier = (factor) => (n) => n * factor;`.

---

Una closure mantiene un enlace **vivo** con la variable, no una copia de su valor. Cuando se crean varias funciones en la misma llamada, comparten la misma variable, y cualquier cambio hecho a través de una es visible para las demás:
```javascript
function makeCounter() {
  let count = 0;
  return {
    increment: () => { count += 1; },
    value: () => count,
  };
}
const counter = makeCounter();
counter.increment();
counter.increment();
console.log(counter.value());
// prints 2
```
Nadie puede leer ni reiniciar `count` desde fuera salvo a través de esas dos funciones: la variable es **privada**. Una segunda llamada a `makeCounter()` crea un `count` completamente separado.

---

Como las funciones son valores, puedes escribir una función de orden superior que **combine** dos funciones en una nueva. `compose(f, g)` devuelve una función que aplica primero `g` y luego `f` al resultado, igual que la notación matemática *f(g(x))*:
```javascript
const compose = (f, g) => (x) => f(g(x));
const trim = (s) => s.trim();
const shout = (s) => s.toUpperCase();
const clean = compose(shout, trim);
console.log(clean("  hi  "));
// prints HI
```
El orden importa: `compose(f, g)` ejecuta primero `g` y luego `f`. Construir programas pegando funciones pequeñas de esta forma se llama **composición de funciones**.

---

Una función que devuelve una función también es la forma natural de **adaptar** un callback. Supón que tienes un predicado y necesitas el contrario para `filter`: en vez de reescribirlo, envuélvelo:
```javascript
const isLong = (word) => word.length > 4;
const isShort = (word) => !isLong(word);
console.log(["tree", "forest"].filter(isShort));
// prints [ 'tree' ]
```
Un `not(predicate)` general haría esto para cualquier predicado: devuelve una nueva función que llama a `predicate` con el mismo argumento e invierte el resultado con `!`. Los predicados de `filter`, `find`, `some` y `every` reciben el elemento como primer argumento, así que el envoltorio solo necesita reenviar ese valor.

---

El acumulador de `reduce` no tiene por qué ser un número: puede ser una cadena, un array o un objeto. Partiendo de un objeto vacío `{}` puedes contar o agrupar cosas en una sola pasada. Recuerda **devolver el acumulador** desde el callback, o el siguiente paso recibirá `undefined`:
```javascript
const votes = ["yes", "no", "yes"];
const tally = votes.reduce((acc, vote) => {
  acc[vote] = (acc[vote] ?? 0) + 1;
  return acc;
}, {});
console.log(tally);
// prints { yes: 2, no: 1 }
```
`acc[vote] ?? 0` lee el recuento actual, o `0` cuando esa clave todavía no existe.

---

Toda función tiene un método `bind` que devuelve una función **nueva** con algunas cosas fijadas de antemano. Su primer argumento pasa a ser el `this` de la nueva función; los argumentos restantes se colocan delante de aquellos con los que se llame a la nueva función (una **aplicación parcial**):
```javascript
function multiply(a, b) {
  return a * b;
}
const double = multiply.bind(null, 2);
console.log(double(21));
// prints 42
```
Fijar `this` importa en los métodos. Cuando un método se copia fuera de su objeto y se llama por su cuenta, `this` ya no se refiere al objeto, así que `this.name` pasa a ser `undefined`. `bind` lo fija al objeto:
```javascript
const user = {
  name: "Ana",
  hello() { return `Hi ${this.name}`; },
};
const loose = user.hello;
console.log(loose());
// prints Hi undefined
const bound = user.hello.bind(user);
console.log(bound());
// prints Hi Ana
```
La función original nunca cambia: `bind` siempre construye una nueva, cuyo `name` es el nombre original precedido por `bound `.

---

Los programas reales combinan estos métodos en una **tubería**: filtra los elementos que te interesan, mapéalos a los valores que necesitas y redúcelos a un resultado. Guardar los arrays intermedios en constantes hace legible cada paso y permite reutilizarlos:
```javascript
const adults = people.filter((p) => p.age >= 18);
const names = adults.map((p) => p.name);
const totalAge = adults.reduce((sum, p) => sum + p.age, 0);
```
`names.join(", ")` convierte un array de cadenas en una sola cadena con los elementos separados por una coma y un espacio.

---

Las closures permiten que una función devuelta mantenga **estado privado** entre llamadas. Un ayudante clásico construido así es `once(fn)`: devuelve una función que ejecuta `fn` solo la primera vez que se la llama, recuerda el resultado y devuelve ese mismo resultado en cada llamada posterior sin ejecutar `fn` de nuevo:
```javascript
let calls = 0;
const init = once(() => {
  calls += 1;
  return "ready";
});
console.log(init(), init(), calls);
// prints ready ready 1
```
El envoltorio necesita dos variables privadas: si `fn` ya se ejecutó y el resultado guardado. Ambas viven en la closure, invisibles desde fuera. Para reenviar a `fn` todos los argumentos del envoltorio, declara el envoltorio con un parámetro rest `(...args)` y llama a `fn(...args)`.

---

Todo se junta en `groupBy(items, keyFn)`: una función de orden superior que recibe un callback que decide la **clave de grupo** de cada elemento y devuelve un objeto que asocia cada clave con el array de elementos que tienen esa clave. `reduce` con un acumulador objeto hace todo el trabajo:
```javascript
const byInitial = groupBy(["hi", "yo", "hey"], (w) => w[0]);
console.log(byInitial);
// prints { h: [ 'hi', 'hey' ], y: [ 'yo' ] }
```
Para cada elemento, calcula la clave, crea el array de esa clave si todavía no existe (`acc[key] ?? []`), añade el elemento y devuelve el acumulador. Como quien llama elige `keyFn`, la misma función agrupa palabras por inicial, personas por ciudad o números por paridad.
