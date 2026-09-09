Cada valor en JavaScript tiene un **tipo**. Hay siete tipos **primitivos**:
- `number` para cualquier número, como `42` o `3.14`
- `string` para texto, como `"Ana"`
- `boolean` para `true` y `false`
- `undefined` para un valor que nunca fue proporcionado
- `null` para un valor vacío intencionadamente
- `bigint` para números enteros de cualquier tamaño, como `9007199254740993n`
- `symbol` para identificadores únicos creados con `Symbol()`

Todo lo demás (arrays, funciones, objetos creados con `{}`, fechas...) es un `object`.
El operador `typeof` te dice el tipo de un valor, como una cadena:
```javascript
console.log(typeof 42, typeof "Ana", typeof true);
// prints number string boolean
let city;
console.log(typeof city);
// prints undefined
```

---

JavaScript tiene **tipado dinámico**: una variable no tiene tipo propio, solo el valor que contiene en cada momento tiene uno. La misma variable puede contener un número ahora y una cadena después, y `typeof` sigue al valor:
```javascript
let data = 10;
console.log(typeof data);
// prints number
data = "ten";
console.log(typeof data);
// prints string
```
Esto es cómodo, pero también significa que una función puede recibir un valor de un tipo inesperado, así que comprobar con `typeof` es un primer paso habitual. Como `typeof` devuelve una cadena, comparas su resultado con una cadena:
```javascript
if (typeof data === "string") {
  console.log("text");
}
```

---

`typeof` tiene algunas respuestas que sorprenden a la gente.
Las funciones obtienen su propia respuesta, `"function"`, aunque son objetos:
```javascript
console.log(typeof function () {});
// prints function
console.log(typeof console.log);
// prints function
```
Los arrays **no** obtienen su propia respuesta: son simplemente `"object"`, igual que `{}`:
```javascript
console.log(typeof [1, 2, 3]);
// prints object
```
Y `typeof null` es `"object"`, un error histórico que nunca se corrigió. Así que `typeof` distingue bien los primitivos y las funciones, pero no puede diferenciar un array, un objeto y `null`.

---

Puedes convertir un valor a otro tipo **explícitamente** llamando al tipo como una función:
- `Number(value)` convierte a un número: `Number("42")` es `42`
- `String(value)` convierte a una cadena: `String(42)` es `"42"`
- `Boolean(value)` convierte a un booleano: `Boolean("")` es `false`

El resultado es un valor completamente nuevo; el original no se cambia:
```javascript
const input = "7";
const count = Number(input) + 1;
console.log(count, typeof count);
// prints 8 number
console.log(String(count) + "!");
// prints 8!
```
Convertir explícitamente hace visible tu intención: quien lee `Number(input)` sabe que `input` era texto.

---

`Number()` es estricto: la cadena entera debe ser un número, de lo contrario el resultado es `NaN` ("Not a Number"):
```javascript
console.log(Number("12px"));
// prints NaN
```
`parseInt()` y `parseFloat()` son más tolerantes: leen dígitos desde el inicio de la cadena, omiten los espacios iniciales y se detienen en el primer carácter que no forma parte de un número. `parseInt` conserva solo la parte entera:
```javascript
console.log(parseInt("12px"), parseFloat("1.5kg"));
// prints 12 1.5
console.log(parseInt("3.9em"), parseInt("-4px"));
// prints 3 -4
```
Cuando la cadena no empieza con algo que pueda iniciar un número (un signo opcional, seguido de un dígito), también devuelven `NaN`:
```javascript
console.log(parseInt("auto"));
// prints NaN
```
`NaN` es el único valor que no es igual a sí mismo, así que `x === NaN` siempre es `false`; para detectarlo usa `Number.isNaN(x)`.

---

Hay dos formas de preguntar "¿es esto `NaN`?", y responden a preguntas diferentes.
La antigua función global `isNaN(value)` primero **convierte** `value` a un número y luego comprueba. Así que dice `true` para cualquier cosa que no pueda convertirse en un número, aunque no sea `NaN` en absoluto:
```javascript
console.log(isNaN("hello"));
// prints true, because Number("hello") is NaN
console.log(isNaN("42"));
// prints false, because Number("42") is 42
```
`Number.isNaN(value)` **no** convierte: es `true` solo cuando `value` es realmente el número `NaN`:
```javascript
console.log(Number.isNaN("hello"));
// prints false, a string is not NaN
console.log(Number.isNaN(Number("hello")));
// prints true
```
Prefiere `Number.isNaN`, y convierte primero si quieres saber si una conversión falló.

---

JavaScript también convierte **implícitamente**, y el operador `+` es donde esto suele causar más problemas. Si cualquiera de los lados es una cadena, `+` **concatena** y el otro lado se convierte a una cadena:
```javascript
console.log("5" + 3);
// prints 53
console.log(1 + 2 + "3");
// prints 33, because 1 + 2 is computed first
```
Todos los demás operadores aritméticos convierten ambos lados a **números**:
```javascript
console.log("6" - 2, "3" * "4");
// prints 4 12
```
Así que sumar valores que vienen de texto (entrada del usuario, archivos, URLs) puede construir silenciosamente una cadena en lugar de una suma. Convierte con `Number()` antes de sumar para ir sobre seguro.

---

Una forma corta de convertir una cadena en un número es el **más unario**: un `+` colocado delante de un solo valor lo convierte exactamente como lo hace `Number()`:
```javascript
console.log(+"5" + 5);
// prints 10
console.log(typeof +"5");
// prints number
```
Es compacto, pero fácil de confundir con una suma, así que muchos equipos prefieren el `Number("5")` explícito.

---

La igualdad **débil** `==` convierte los dos lados a un tipo común antes de comparar, siguiendo reglas difíciles de recordar:
```javascript
console.log("5" == 5);
// prints true, "5" becomes 5
console.log(0 == "");
// prints true, "" becomes 0
console.log(0 == false, "1" == true);
// prints true true
```
La igualdad **estricta** `===` nunca convierte: los valores de tipos diferentes simplemente no son iguales:
```javascript
console.log("5" === 5, 0 === "", 0 === false);
// prints false false false
```
Usa `===` (y `!==`) por defecto. La única excepción común es `value == null`, que comprueba `null` y `undefined` a la vez.

---

Cuando JavaScript necesita un booleano, por ejemplo en una condición `if` o en `Boolean(value)`, convierte el valor. Solo ocho valores se vuelven `false`; se llaman **falsy**:
`false`, `0`, `-0`, `0n`, `""`, `null`, `undefined` y `NaN`.
**Todo lo demás es truthy**, incluidos algunos valores que parecen vacíos:
```javascript
console.log(Boolean(0), Boolean(""), Boolean(NaN));
// prints false false false
console.log(Boolean("0"), Boolean("false"), Boolean([]), Boolean({}));
// prints true true true true
```
`"0"` es una cadena no vacía, así que es truthy; un array vacío es un objeto, así que también es truthy.

---

Un atajo común para convertir cualquier valor en un booleano es la **doble negación** `!!`: el primer `!` convierte a un booleano y lo invierte, el segundo lo invierte de nuevo:
```javascript
console.log(!!"text", !!0);
// prints true false
```
`!!value` y `Boolean(value)` dan exactamente el mismo resultado; la forma explícita es más fácil de leer.

---

JavaScript tiene un único tipo `number` para enteros y decimales: cada número es un valor de punto flotante de 64 bits (un *double*). Así que `5` y `5.0` son el mismo valor, y no hay un tipo entero separado:
```javascript
console.log(5 === 5.0, 10 / 2);
// prints true 5
```
Para preguntar si un número no tiene parte fraccionaria, usa `Number.isInteger`:
```javascript
console.log(Number.isInteger(5.0), Number.isInteger(3.5));
// prints true false
```
Los literales de plantilla convierten el valor interpolado a una cadena con las mismas reglas que `String()`, así que `${5.0}` se vuelve `"5"`, no `"5.0"`.

---

Como los números son doubles, algunos decimales no pueden almacenarse con exactitud y aparecen pequeños errores:
```javascript
console.log(0.1 + 0.2);
// prints 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);
// prints false
```
El método `toFixed(digits)` redondea un número a `digits` decimales, pero devuelve una **cadena**, lo cual está bien para mostrar y es incorrecto para seguir haciendo cálculos:
```javascript
const price = (0.1 + 0.2).toFixed(2);
console.log(price, typeof price);
// prints 0.30 string
```
Para obtener un **número** redondeado, convierte el resultado de nuevo con `Number()`:
```javascript
console.log(Number((0.1 + 0.2).toFixed(1)));
// prints 0.3
```

---

Un `number` puede representar enteros con exactitud solo hasta `Number.MAX_SAFE_INTEGER`, que es `9007199254740991`. Más allá de eso, se pierden dígitos:
```javascript
console.log(9007199254740993);
// prints 9007199254740992
```
Para enteros más grandes usa `bigint`: escribe el literal con un sufijo `n`, o convierte con `BigInt()`:
```javascript
const big = 9007199254740993n;
console.log(typeof big, big + 1n);
// prints bigint 9007199254740994n
```
`console.log` muestra el sufijo `n`; `String(big)` da los dígitos tal cual.
Un `bigint` y un `number` no pueden mezclarse en la aritmética: `big + 1` lanza un `TypeError`. Convierte un lado explícitamente, con `BigInt(count)` o `Number(big)`.

---

Como `typeof` responde `"object"` para arrays, objetos y `null`, diferenciarlos necesita dos comprobaciones extra.
`Array.isArray(value)` es `true` solo para arrays:
```javascript
console.log(Array.isArray([1, 2]), Array.isArray({}));
// prints true false
```
Para `null` compara directamente, `value === null`. Combinarlos da una imagen completa de cualquier valor:
```javascript
function kind(value) {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}
```
Comprueba `null` y los arrays primero, porque el `typeof` simple no puede distinguirlos.

---

El texto que viene de formularios, archivos o URLs siempre es una cadena, incluso cuando representa un número o un booleano. Devolverlo al tipo correcto combina lo que ya has visto: compara con `"true"` y `"false"` para los booleanos, y prueba `Number()` para los números, recordando que `Number("")` es `0` y que `Number.isNaN` te dice cuándo la conversión falló:
```javascript
console.log(Number("3.5"), Number(""), Number("12px"));
// prints 3.5 0 NaN
```
Cuando nada coincide, conserva la cadena tal como está.
