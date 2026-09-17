Una **cadena** (string) es una secuencia de caracteres entre comillas, como `"hello"` o `'hello'`.
Toda cadena tiene una propiedad `length` que indica cuántos caracteres contiene:
```javascript
let greeting = "hello";
console.log(greeting.length);
// imprime 5
```
Los espacios y la puntuación también cuentan como caracteres.

---

Cada carácter de una cadena tiene un **índice**, empezando desde `0`.
Puedes leer un carácter individual con corchetes o con el método `charAt()`:
```javascript
let word = "hello";
console.log(word[0]);
// imprime h
console.log(word.charAt(1));
// imprime e
```
El último carácter está en el índice `length - 1`:
```javascript
console.log(word[word.length - 1]);
// imprime o
```

---

Las cadenas incluyen muchos **métodos** integrados. Dos de los más simples cambian las mayúsculas y minúsculas de cada letra:
```javascript
let word = "Hello";
console.log(word.toUpperCase());
// imprime HELLO
console.log(word.toLowerCase());
// imprime hello
```
Ninguno de los dos métodos recibe argumentos, así que no olvides los paréntesis.

---

Para comprobar si una cadena contiene otra cadena, usa estos métodos, que devuelven todos un booleano:
- `includes(text)` es `true` si `text` aparece en cualquier parte
- `startsWith(text)` es `true` si la cadena empieza con `text`
- `endsWith(text)` es `true` si la cadena termina con `text`

```javascript
let file = "photo.png";
console.log(file.includes("."));
// imprime true
console.log(file.startsWith("ph"));
// imprime true
console.log(file.endsWith(".jpg"));
// imprime false
```
La comparación distingue mayúsculas de minúsculas: `"Hello".includes("h")` es `false`.

---

El método `indexOf()` devuelve el índice donde aparece **por primera vez** un fragmento de texto en la cadena.
Si el texto no se encuentra, devuelve `-1`:
```javascript
let word = "hello";
console.log(word.indexOf("l"));
// imprime 2
console.log(word.indexOf("z"));
// imprime -1
```

---

El método `slice(start, end)` extrae una parte de una cadena, desde el índice `start` hasta (sin incluir) el índice `end`:
```javascript
let word = "JavaScript";
console.log(word.slice(0, 4));
// imprime Java
console.log(word.slice(4));
// imprime Script
```
Si omites `end`, el fragmento llega hasta el final de la cadena.
Un índice negativo cuenta desde el final: `word.slice(-3)` es `"ipt"`.
El método `substring(start, end)` funciona igual, pero no acepta índices negativos.

---

`indexOf()` y `slice()` funcionan bien juntos: encuentra dónde está algo y luego corta la cadena ahí.
```javascript
let time = "10:45";
let colon = time.indexOf(":");
console.log(time.slice(colon + 1));
// imprime 45
```

---

El método `split(separator)` divide una cadena en un **array** de partes, cortando en cada `separator`:
```javascript
let sentence = "I like JavaScript";
let words = sentence.split(" ");
console.log(words);
// imprime [ 'I', 'like', 'JavaScript' ]
```
Lo contrario es el método de array `join(separator)`, que une las partes de nuevo en una cadena:
```javascript
console.log(words.join("-"));
// imprime I-like-JavaScript
```

---

La entrada del usuario a menudo tiene espacios extra alrededor. El método `trim()` devuelve una copia de la cadena con los espacios en blanco eliminados en **ambos** extremos:
```javascript
let input = "   hello   ";
console.log(input.trim());
// imprime hello
```
`trimStart()` elimina solo los espacios iniciales y `trimEnd()` solo los finales.
Los espacios en medio de la cadena nunca se tocan.

---

El método `replace(search, replacement)` devuelve una nueva cadena en la que la **primera** aparición de `search` se sustituye por `replacement`:
```javascript
let text = "red red";
console.log(text.replace("red", "blue"));
// imprime blue red
```
Para reemplazar **todas** las apariciones, usa `replaceAll()`:
```javascript
console.log(text.replaceAll("red", "blue"));
// imprime blue blue
```

---

El método `repeat(count)` devuelve la cadena repetida `count` veces:
```javascript
console.log("ab".repeat(3));
// imprime ababab
console.log("ab".repeat(0));
// imprime una cadena vacía
```

---

El método `padStart(targetLength, padString)` añade `padString` al **inicio** de la cadena hasta alcanzar `targetLength` caracteres. `padEnd()` hace lo mismo al final:
```javascript
console.log("7".padStart(3, "0"));
// imprime 007
console.log("Tea".padEnd(6, "."));
// imprime Tea...
```
Si la cadena ya es lo bastante larga, se devuelve sin cambios.
Los números no tienen métodos de cadena, así que conviértelos primero con `String(number)`.

---

Dos cadenas son iguales con `===` solo si tienen exactamente los mismos caracteres, en las mismas mayúsculas o minúsculas:
```javascript
console.log("hello" === "hello");
// imprime true
console.log("hello" === "Hello");
// imprime false
```
Los operadores `<` y `>` comparan cadenas alfabéticamente, carácter por carácter.
Las mayúsculas van antes que las minúsculas, así que `"Zoo" < "apple"` es `true`.

---

Las cadenas son **inmutables**: una vez creada, una cadena nunca puede cambiarse.
Asignar a un índice no hace nada, y todo método de cadena devuelve una **nueva** cadena en lugar de modificar la original:
```javascript
let word = "hello";
word[0] = "j";
console.log(word);
// imprime hello
word.toUpperCase();
console.log(word);
// imprime hello
```
Para conservar un resultado, asígnalo de nuevo a la variable:
```javascript
word = word.toUpperCase();
```

---

Llamar a `split("")` con un separador vacío convierte una cadena en un array de sus caracteres individuales.
Los arrays tienen un método `reverse()`, así que puedes invertir una cadena dividiéndola, invirtiéndola y uniéndola de nuevo:
```javascript
let word = "abc";
console.log(word.split("").reverse().join(""));
// imprime cba
```
