Un **comentario** es una nota escrita dentro del código fuente para quienes lo leen. JavaScript ignora los comentarios por completo, así que nunca cambian lo que hace el programa.

El comentario más simple es el **comentario de una línea**: empieza con `//` y llega hasta el final de la línea.
```javascript
// Greets the user
console.log("Hello");
```
Usa los comentarios para explicar para qué sirve un fragmento de código, o por qué se escribió de esa manera. Ten en cuenta que, a diferencia de otros lenguajes, `#` **no** inicia un comentario en JavaScript.

---

Un comentario no necesita una línea propia: puede seguir al código en la misma línea. Este es un **comentario en línea** (o comentario final), y es un buen lugar para una nota breve sobre esa instrucción concreta:
```javascript
const retries = 3; // give up after three attempts
```
Todo lo que va desde `//` hasta el final de la línea se ignora, mientras que el código anterior se ejecuta con normalidad.

---

Como los comentarios se ignoran, añadir o borrar un comentario nunca cambia lo que hace un programa. Solo se ejecuta el código que **no** está comentado.

Esto convierte a `//` en una forma rápida de desactivar una línea de código sin borrarla. Esto se llama **comentar** el código:
```javascript
let total = 10;
// total = total + 5;
console.log(total); // prints 10
```
La segunda línea ahora es un comentario, así que `total` sigue siendo `10`. Quitar el `//` devuelve la línea a la vida.

Comentar código es cómodo mientras experimentas, pero acuérdate de limpiar: el código que queda comentado mucho tiempo solo confunde a quien lo lea después.

---

Cuando un comentario necesita más de una línea, JavaScript ofrece el **comentario de varias líneas** (también llamado comentario de bloque): empieza con `/*` y termina con `*/`, y todo lo que hay en medio se ignora, incluidos los saltos de línea.
```javascript
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
console.log("Welcome!");
```
Un comentario de bloque también puede ser corto y quedarse en una sola línea: `/* like this */`.

---

Sea cual sea el tipo de comentario que uses, la regla es la misma: el texto que hay dentro **no es código**. Un `console.log` dentro de un comentario nunca imprime nada, y el código escrito después de `//` en la misma línea nunca se ejecuta, incluso cuando la línea empieza con código real:
```javascript
console.log("a"); // console.log("b");
/* console.log("c"); */
// prints only a
```
Cuando no estés seguro de lo que imprime un programa, borra mentalmente todos los comentarios y lee lo que queda.

---

A diferencia de `//`, que se detiene al final de la línea, un comentario `/*` solo se detiene en el `*/`. Si olvidas cerrarlo, JavaScript trata todo el código siguiente como parte del comentario e informa de un error de sintaxis:
```javascript
const width = 10; /* in centimetres
console.log(width); // still inside the comment: SyntaxError, the comment is never closed
```
Tanto `//` como `/* */` funcionan como comentarios en línea, pero con `/*` asegúrate siempre de que el `*/` esté ahí.

---

En JavaScript los comentarios de bloque **no se pueden anidar**: el comentario termina en el **primer** `*/` que encuentra, sin importar cuántos `/*` hubiera antes.
```javascript
/* outer /* inner */ still a comment */
console.log("done");
```
Aquí el comentario termina justo después de `inner`, así que `still a comment */` se lee como código y provoca un error de sintaxis. Tenlo en cuenta cuando comentes un bloque que ya contiene un comentario `/* */`: usa `//` en cada línea, o elimina antes el comentario interior.

---

Para comentar varias líneas de una vez, envuélvelas en un único comentario de bloque en lugar de añadir `//` a cada línea:
```javascript
let total = 100;
/*
total = total - 30;
total = total - 20;
*/
console.log(total); // prints 100
```
Como las líneas de dentro del bloque se ignoran, `total` nunca cambia. Recuerda que esto solo funciona si ninguna de esas líneas contiene un `*/`.

---

JavaScript tiene un tercer tipo de comentario, el **comentario de documentación**, escrito en el formato **JSDoc**: un comentario de bloque que empieza con `/**` (dos asteriscos) colocado directamente encima de una función. Dentro, las líneas suelen empezar con ` * ` y unas **etiquetas** especiales que empiezan por `@` describen la función:
- `@param {type} name description` para cada parámetro
- `@returns {type} description` para el valor devuelto

```javascript
/**
 * Returns the greeting for a person.
 * @param {string} name the name of the person
 * @returns {string} the greeting, ending with an exclamation mark
 */
function greet(name) {
  return `Hi, ${name}!`;
}
```
Para JavaScript es solo un comentario, pero los editores lo leen y lo muestran como texto de ayuda de `greet`, junto con el tipo escrito entre llaves (`{number}`, `{string}`, `{boolean}`, `{number[]}`...).

---

La primera línea de un comentario JSDoc es el **resumen**: una frase corta que dice qué hace la función. Escríbela en tercera persona, como si describieras la función: "Returns...", "Adds...", "Checks...". Después enumera las etiquetas, una por línea:
```javascript
/**
 * Returns true when n is divisible by two.
 * @param {number} n the number to check
 * @returns {boolean} true for even numbers, false otherwise
 */
function isEven(n) {
  return n % 2 === 0;
}
```
El comentario debe estar justo encima de la declaración, sin ninguna línea en blanco en medio, o los editores no lo asociarán a la función.

---

Un comentario JSDoc también es un **contrato**: le dice a quien llama a la función qué pasar y qué esperar a cambio, incluso antes de que el cuerpo esté escrito. Leer el comentario suele bastar para implementar la función:
```javascript
/**
 * Returns the larger of two numbers.
 * @param {number} a the first number
 * @param {number} b the second number
 * @returns {number} a if it is greater than b, otherwise b
 */
function larger(a, b) {
  return a > b ? a : b;
}
```
Cada `@param` corresponde a un parámetro, en el mismo orden, y `@returns` describe todos los resultados posibles.

---

El orden dentro de un comentario JSDoc es siempre el mismo: primero el resumen, después un `@param` por cada parámetro en el orden en que están declarados, y al final `@returns`. La apertura `/**` y el cierre ` */` lo envuelven todo, y el comentario se sitúa directamente encima de la función que describe:
```javascript
/**
 * Returns the number of seconds in the given minutes.
 * @param {number} minutes a whole number of minutes
 * @returns {number} minutes multiplied by sixty
 */
function toSeconds(minutes) {
  return minutes * 60;
}
```

---

Un archivo JavaScript puede empezar con una línea especial llamada **shebang** (o hashbang): `#!` seguido de la ruta del programa que debe ejecutar el archivo. En los sistemas tipo Unix te permite ejecutar un script directamente desde el terminal, como `./hello.js`, sin escribir antes `node`:
```javascript
#!/usr/bin/env node
console.log("Hello from Node");
```
JavaScript ignora esta línea exactamente igual que un comentario, pero solo cuando es la **primerísima línea** del archivo: en cualquier otro sitio, `#!` es un error de sintaxis. `/usr/bin/env node` significa "busca `node` en este sistema y úsalo".

---

Un buen comentario explica **por qué** el código hace algo, no **qué** hace. El código ya muestra lo que ocurre; repetirlo con palabras añade ruido y queda obsoleto en cuanto el código cambia:
```javascript
// set timeout to 30
const timeout = 30;
```
La razón que hay detrás del número es lo que quien lee no puede adivinar:
```javascript
// the server drops idle connections after 35 seconds, so stop earlier
const timeout = 30;
```
Si un comentario solo repite la línea que tiene debajo, bórralo o sustitúyelo por la razón.

---

Algunos comentarios siguen una convención que los editores entienden. Los **marcadores** más comunes son:
- `// TODO: ...` señala algo que todavía hay que escribir
- `// FIXME: ...` señala código que se sabe que está mal y que hay que corregir

```javascript
const limit = 10;
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
Para JavaScript son comentarios corrientes; los editores los listan para que el trabajo pendiente sea fácil de encontrar. Un `TODO` suele estar junto a un marcador de posición que mantiene el código funcionando hasta que se escribe la implementación real. Cuando termines el trabajo, sustituye el marcador de posición y elimina la marca en el mismo cambio: un `TODO` obsoleto induce a error.

---

Un `FIXME` es distinto de un `TODO`: el código ya existe, pero se sabe que está mal. Un buen `FIXME` dice cuál es el error y, cuando es posible, da un ejemplo que lo muestra, para que la siguiente persona pueda corregirlo rápido. Igual que con `TODO`, borra la marca en cuanto el error esté corregido, pero conserva el comentario JSDoc, que sigue siendo cierto.
