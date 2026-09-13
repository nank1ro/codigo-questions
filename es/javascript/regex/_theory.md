Una **expresión regular** (o **regex**) es un patrón pequeño que describe una forma de texto. La usas para responder preguntas como "¿esta cadena contiene un número?" o "¿dónde aparece la palabra `cat`?".

En JavaScript la forma más corta de escribir una es un **literal regex**: el patrón entre dos barras.
```javascript
const pattern = /cat/;
```
Los caracteres ordinarios de un patrón coinciden consigo mismos, así que `/cat/` coincide con las tres letras `c`, `a`, `t` en cualquier lugar dentro de una cadena.

Lo más simple que puedes hacer con un patrón es preguntar si aparece en una cadena. El método **`test`** recibe el texto y devuelve `true` o `false`:
```javascript
console.log(/cat/.test("the cat sleeps"));
// prints true
console.log(/cat/.test("the dog sleeps"));
// prints false
```
Ten en cuenta que `test` busca el patrón en *algún lugar* de la cadena; no hace falta que toda la cadena coincida.

---

Los patrones se vuelven útiles cuando describen un *tipo* de carácter en lugar de un carácter exacto. Unas pocas **secuencias de escape** cubren la mayoría de las necesidades:
- `\d` cualquier dígito, del `0` al `9`
- `\w` cualquier carácter de palabra: una letra, un dígito o `_`
- `\s` cualquier espacio en blanco: un espacio, un tabulador, un salto de línea

```javascript
console.log(/\d/.test("room 12"));
// prints true
console.log(/\d/.test("lobby"));
// prints false
```
Un **cuantificador** indica cuántas veces puede repetirse la pieza anterior. El más común es `+`, que significa "uno o más":
```javascript
console.log(/\d+/.test("42"));
// prints true
```
Así, `/\d/` coincide con un solo dígito y `/\d+/` coincide con una racha de dígitos. Para un simple `test` ambos se comportan igual, porque a los dos les basta con que haya un dígito presente.

---

Un literal como `/\d+/` queda fijo en cuanto lo escribes. Cuando el patrón tiene que **construirse en tiempo de ejecución**, usa el **constructor `RegExp`**, que recibe el patrón como una cadena:
```javascript
const word = "cat";
const pattern = new RegExp(word);
console.log(pattern.test("the cat sleeps"));
// prints true
```
Hay una trampa. Dentro de una cadena, una barra invertida inicia una secuencia de escape *de la cadena*, así que desaparece antes de que la regex la vea. Para poner una barra invertida real en el patrón debes duplicarla:
```javascript
const digits = new RegExp("\\d+");
// the same pattern as /\d+/
```
Escribir `new RegExp("\d+")` en su lugar produce el patrón `/d+/`, que coincide con la letra `d`, no con un dígito.

Prefiere el literal cuando el patrón se conoce mientras escribes el código; es más corto y no necesita barras invertidas duplicadas.

---

Dos bloques de construcción más te permiten describir casi cualquier forma de texto.

Una **clase de caracteres** es un conjunto de caracteres entre corchetes; coincide con exactamente uno de ellos. Un guion escribe un rango, y una `^` al inicio niega el conjunto:
```javascript
/[aeiou]/   // one vowel
/[a-z]/     // one lowercase letter
/[A-Z0-9]/  // one uppercase letter or one digit
/[^0-9]/    // one character that is not a digit
```
Los **cuantificadores** indican cuántas veces se repite la pieza anterior: `+` una o más, `*` cero o más, `?` cero o una, y `{n}` exactamente `n` veces.

Por último, los **anclajes** atan el patrón a los extremos del texto: `^` significa "empieza aquí" y `$` significa "termina aquí". Sin ellos un patrón puede coincidir en cualquier lugar dentro de la cadena, así que `/\d{2}/.test("abc12def")` es `true`. Con ambos anclajes toda la cadena tiene que coincidir:
```javascript
console.log(/^\d{2}$/.test("abc12def"));
// prints false
console.log(/^\d{2}$/.test("12"));
// prints true
```

---

`test` solo responde sí o no. Para obtener el texto coincidente en sí, llama a **`match`** sobre la cadena:
```javascript
const match = "order 42 shipped".match(/\d+/);
```
Cuando nada coincide, `match` devuelve `null`. Cuando algo coincide, devuelve un resultado parecido a un array:
- `match[0]` es el texto que coincidió
- `match.index` es la posición donde empieza la coincidencia
- `match.input` es toda la cadena que se buscó

```javascript
console.log(match[0]);
// prints 42
console.log(match.index);
// prints 6
```
Como el resultado puede ser `null`, compruébalo antes de leer `match[0]`.

---

Como `match` devuelve `null` cuando el patrón no está presente, leer `match[0]` directamente lanza `TypeError: Cannot read properties of null`. Protégelo:
```javascript
function firstWord(text) {
  const match = text.match(/[a-z]+/);
  if (match === null) {
    return "";
  }
  return match[0];
}
```
El operador de coalescencia nula escribe la misma protección en una sola línea, porque `match?.[0]` es `undefined` cuando `match` es `null`:
```javascript
return text.match(/[a-z]+/)?.[0] ?? "";
```

---

Los paréntesis alrededor de una parte del patrón crean un **grupo de captura**: el texto con el que esa parte coincidió se guarda aparte para que puedas leerlo después.

Los grupos aparecen después de `match[0]`, numerados de izquierda a derecha según su paréntesis de apertura:
```javascript
const match = "2026-09-12".match(/(\d{4})-(\d{2})-(\d{2})/);
console.log(match[0]);
// prints 2026-09-12
console.log(match[1]);
// prints 2026
console.log(match[3]);
// prints 12
```
Así, `match[0]` es siempre la coincidencia completa, y `match[1]`, `match[2]`, ... son los grupos. Un grupo que forma parte de un patrón que no coincide en absoluto hace que todo `match` devuelva `null`.

---

Captura solo lo que necesitas. Un grupo no es solo una forma de leer una pieza después; también le dice al lector qué parte del patrón importa. En un patrón de hora donde solo quieres los minutos, agrupa únicamente los minutos y deja el resto sin agrupar:
```javascript
const minutes = "at 14:35:02".match(/\d{2}:(\d{2}):\d{2}/)?.[1];
console.log(minutes);
// prints 35
```
Todo el patrón sigue teniendo que coincidir, así que las horas y los segundos siguen siendo obligatorios; simplemente no se capturan. Menos grupos significan menos números que recordar cuando lees `match[1]`, `match[2]` y así sucesivamente.

---

Contar paréntesis cansa, y añadir un grupo en medio de un patrón renumera todo lo que viene después. Un **grupo con nombre** evita ambos problemas: escribe `?<name>` justo después del paréntesis de apertura y lee la pieza desde `match.groups`:
```javascript
const match = "2026-09-12".match(/(?<year>\d{4})-(?<month>\d{2})-\d{2}/);
console.log(match.groups.year);
// prints 2026
console.log(match.groups.month);
// prints 09
```
Los grupos con nombre siguen numerados, así que `match[1]` sigue funcionando, pero `match.groups.year` dice qué significa el valor. Cuando el patrón no tiene ningún grupo con nombre, `match.groups` es `undefined`.

---

Todo lo visto hasta ahora se detenía en la primera coincidencia. Las **banderas** (*flags*), escritas después de la barra de cierre de un literal, cambian eso y otros detalles de la búsqueda:
- `g` global: encuentra cada coincidencia, no solo la primera
- `i` ignora mayúsculas y minúsculas, así que `/cat/i` también coincide con `Cat` y `CAT`

Con la bandera `g`, `match` se comporta diferente: devuelve un array simple de las **cadenas** coincidentes, sin `index` y sin grupos, o `null` cuando no hay coincidencia:
```javascript
const numbers = "a1 b22 c333".match(/\d+/g);
console.log(numbers);
// prints [ '1', '22', '333' ]
console.log(numbers.length);
// prints 3
```
Las banderas pueden combinarse en cualquier orden, como en `/cat/gi`. Con el constructor `RegExp` van en el segundo argumento: `new RegExp("\\d+", "g")`.

---

La bandera `g` te da cada cadena coincidente, pero descarta los grupos. Cuando necesitas los grupos de *todas* las coincidencias, usa **`matchAll`**. Devuelve un iterador de objetos de coincidencia completos, cada uno exactamente igual al resultado de un `match` normal:
```javascript
const text = "a=1;b=2";
for (const match of text.matchAll(/(?<key>\w+)=(?<value>\w+)/g)) {
  console.log(`${match.groups.key} -> ${match.groups.value}`);
}
// prints a -> 1
// prints b -> 2
```
`matchAll` requiere la bandera `g`; sin ella, lanza un `TypeError`. Como devuelve un iterador, extiéndelo con `[...text.matchAll(pattern)]` cuando quieras un array real, y ten en cuenta que no produce nada en absoluto cuando el patrón nunca coincide.

---

**`replace`** devuelve una nueva cadena con la coincidencia sustituida por otra cosa. La cadena original nunca se modifica.
```javascript
console.log("the cat sleeps".replace(/cat/, "dog"));
// prints the dog sleeps
```
Dentro de la cadena de reemplazo unas pocas secuencias tienen un significado especial:
- `$1`, `$2`, ... el texto capturado por el grupo 1, el grupo 2, ...
- `$<name>` el texto capturado por un grupo con nombre
- `$&` la coincidencia completa

Eso es lo que convierte a `replace` en una herramienta de reescritura y no solo de intercambio:
```javascript
console.log("2026-09-12".replace(/(\d{4})-(\d{2})-(\d{2})/, "$3/$2/$1"));
// prints 12/09/2026
```
Sin la bandera `g` solo se reemplaza la **primera** coincidencia.

---

Para reescribir **todas** las coincidencias en lugar de la primera tienes dos opciones:
```javascript
console.log("a1 b2".replace(/\d/g, "#"));
// prints a# b#
console.log("a1 b2".replaceAll(/\d/g, "#"));
// prints a# b#
```
**`replaceAll`** es la más clara de las dos, y además acepta una cadena simple como patrón. Cuando le das una regex, esa regex **debe** llevar la bandera `g`, de lo contrario lanza un `TypeError`; esto es exactamente lo que evita el error silencioso de escribir `replace` y arreglar solo la primera coincidencia.

---

El reemplazo no tiene que ser una cadena. Cuando pasas una **función**, se llama una vez por cada coincidencia y lo que devuelva se inserta en el lugar de esa coincidencia.

La función recibe primero la coincidencia completa y luego cada grupo de captura:
```javascript
console.log("hello world".replace(/\w+/g, (word) => word.length));
// prints 5 5

console.log("ann lee".replace(/(\w)(\w*)/g, (whole, first, rest) => first.toUpperCase() + rest));
// prints Ann Lee
```
Esta es la única forma de calcular el reemplazo a partir del texto coincidente, algo que `$1` por sí solo no puede hacer.

---

**`split`** corta una cadena en un array. Con una cadena simple corta en ese texto exacto, pero con una regex corta en cada coincidencia del patrón, lo que permite que una sola llamada maneje separadores que varían:
```javascript
console.log("a, b;c".split(", "));
// prints [ 'a', 'b;c' ]
console.log("a, b;c".split(/[,;]\s*/));
// prints [ 'a', 'b', 'c' ]
```
Los separadores en sí no forman parte del resultado. Cuidado con un separador al principio o al final de la cadena: produce una cadena vacía en el array, porque hay un campo vacío en ese lado.

---

Una última bandera completa el conjunto. Por defecto `^` y `$` significan el principio y el final de **toda la cadena**, así que un patrón anclado con `^` solo puede coincidir al mismísimo principio, incluso cuando el texto tiene varias líneas.

La bandera **`m`** (multilínea) cambia eso: `^` y `$` pasan a coincidir también justo después y justo antes de cada salto de línea, así que cada línea queda anclada por su cuenta:
```javascript
const text = "note a\nb\nnote c";
console.log(text.match(/^note.*/g));
// prints [ 'note a' ]
console.log(text.match(/^note.*/gm));
// prints [ 'note a', 'note c' ]
```
Dos detalles importan aquí. Por defecto el `.` no coincide con un salto de línea (solo la bandera `s` cambia eso), así que `.*` se detiene al final de la línea por sí solo. Y `match` con la bandera `g` devuelve `null`, no un array vacío, cuando nada coincide, así que combínalo con `?? []` cuando prometes devolver un array.
