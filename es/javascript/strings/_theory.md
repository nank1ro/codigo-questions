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
