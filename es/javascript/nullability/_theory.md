JavaScript tiene dos formas distintas de decir "aquí no hay ningún valor".
`undefined` significa que un valor **nunca fue proporcionado**. Una variable declarada sin valor contiene `undefined`, y también una propiedad que no existe en un objeto:
```javascript
let city;
console.log(city);
// prints undefined
const user = { name: "Ana" };
console.log(user.age);
// prints undefined
```
`null` es un valor que **tú** asignas a propósito para decir "vacío, y lo sé":
```javascript
let owner = null;
console.log(owner);
// prints null
```
Así que `undefined` suele ser el lenguaje diciéndote que algo falta, mientras que `null` es el programador afirmando que algo está vacío a propósito.

---

Las funciones producen `undefined` en dos situaciones más.
Cuando llamas a una función con **menos argumentos** de los que declara, los parámetros que faltan contienen `undefined`:
```javascript
function greet(name) {
  console.log(name);
}
greet();
// prints undefined
```
Cuando una función termina **sin un `return`** (o con un `return;` desnudo), llamarla da `undefined`:
```javascript
function log(message) {
  console.log(message);
}
const result = log("hi");
console.log(result);
// prints hi, then undefined
```
Fíjate en que pasar `null` explícitamente no es lo mismo que omitir el argumento: `greet(null)` imprime `null`, porque `null` es un valor real que se entregó a la función.

---

El operador `typeof` devuelve el tipo de un valor como una cadena. Para `undefined` responde `"undefined"`, como cabría esperar:
```javascript
let city;
console.log(typeof city);
// prints undefined
```
Para `null`, sin embargo, responde `"object"`. Este es un error de la primera versión de JavaScript que nunca se corrigió, porque demasiado código depende de él:
```javascript
console.log(typeof null);
// prints object
```
Así que `typeof` es una forma fiable de detectar `undefined`, pero no `null`. Para comprobar si hay `null`, compáralo directamente: `value === null`.

---

¿Cómo se comparan `null` y `undefined` entre sí? Depende del operador.
La igualdad **débil** `==` los trata como lo mismo, y los considera diferentes de cualquier otro valor, incluidos `0`, `""` y `false`:
```javascript
console.log(null == undefined);
// prints true
console.log(null == 0, undefined == "");
// prints false false
```
La igualdad **estricta** `===` también compara el tipo, y `null` y `undefined` tienen tipos diferentes:
```javascript
console.log(null === undefined);
// prints false
console.log(null === null);
// prints true
```

---

La mayoría de las veces no te importa *cuál* de los dos marcadores de "sin valor" recibiste: solo quieres saber si hay un valor.
Como `null == undefined` es `true` y nada más es débilmente igual a `null`, la comparación `value == null` es la expresión idiomática estándar para capturar **ambos** a la vez:
```javascript
function show(value) {
  if (value == null) {
    return "missing";
  }
  return "present";
}
console.log(show(null), show(undefined));
// prints missing missing
console.log(show(0), show(""));
// prints present present
```
Este es el único caso en el que se prefiere `==` sobre `===`: escribir `value === null || value === undefined` hace exactamente el mismo trabajo, solo que más largo.
Valores como `0`, `""` y `false` *no* son `null`: son valores reales que resultan ser falsy.

---

Leer una propiedad de `null` o `undefined` es un error que detiene el programa:
```javascript
const user = { name: "Ana" };
console.log(user.address.city);
// TypeError: Cannot read properties of undefined (reading 'city')
```
`user.address` es `undefined`, y `undefined` no tiene propiedades. El operador de **encadenamiento opcional** `?.` resuelve esto: si el valor a su izquierda es `null` o `undefined`, toda la expresión se detiene y evalúa a `undefined` en lugar de lanzar un error:
```javascript
console.log(user.address?.city);
// prints undefined
console.log(user.name?.length);
// prints 3
```
Cuando el lado izquierdo sí tiene un valor, `?.` se comporta exactamente como un `.` normal. Puedes encadenar varios: `user.address?.street?.name` devuelve `undefined` en cuanto falta cualquier eslabón.

---

El encadenamiento opcional no se limita a propiedades con punto. Hay dos formas más.
`?.[]` lee un elemento o una clave calculada solo cuando el lado izquierdo tiene un valor:
```javascript
const post = { tags: ["js", "node"] };
console.log(post.tags?.[0]);
// prints js
const empty = {};
console.log(empty.tags?.[0]);
// prints undefined
```
`?.()` llama a una función solo cuando existe, lo cual es útil para callbacks opcionales:
```javascript
const task = { name: "build" };
task.onDone?.();
// nothing happens, no error
```
En todas las formas, la comprobación se aplica al valor situado **justo antes** del `?.`: `post?.tags?.[0]` es seguro incluso cuando `post` en sí es `null` o `undefined`.

---

Una vez que sabes que un valor puede faltar, normalmente quieres un **valor por defecto** en su lugar. Dos operadores hacen eso, y se diferencian en qué consideran que "falta".
`a || b` devuelve `b` siempre que `a` sea **falsy**: no solo `null` y `undefined`, sino también `0`, `""`, `false` y `NaN`.
El operador de **coalescencia nula** `a ?? b` devuelve `b` solo cuando `a` es `null` o `undefined`, y conserva cualquier otro valor:
```javascript
const count = 0;
console.log(count || 10);
// prints 10
console.log(count ?? 10);
// prints 0
let name;
console.log(name ?? "Guest");
// prints Guest
```
Usa `??` cuando `0`, `""` o `false` son valores legítimos que deben conservarse, y `||` cuando realmente quieras reemplazar cada valor falsy.

---

Un patrón muy común es "rellenar esta propiedad solo si aún no está establecida". Escrito con `??` repite el nombre:
```javascript
options.timeout = options.timeout ?? 1000;
```
El operador de **asignación con coalescencia nula** `??=` hace lo mismo en un paso: asigna el lado derecho solo cuando el lado izquierdo es actualmente `null` o `undefined`, y deja cualquier otro valor intacto:
```javascript
const options = { retries: 0 };
options.retries ??= 3;
options.timeout ??= 1000;
console.log(options);
// prints { retries: 0, timeout: 1000 }
```
`retries` se queda en `0` porque `0` no es nullish; `timeout` no existía, así que recibe `1000`. La misma idea existe para `||` como `||=`, que sobrescribe cada valor falsy.

---

Un **parámetro por defecto** le da a un parámetro un valor cuando quien llama no proporciona uno. La regla es precisa: el valor por defecto se usa solo cuando el argumento es `undefined`, lo cual incluye omitirlo. Pasar `null` **no** activa el valor por defecto, porque `null` es un valor:
```javascript
function repeat(text, times = 2) {
  return text.repeat(times);
}
console.log(repeat("ab"));
// prints abab
console.log(repeat("ab", undefined));
// prints abab
console.log(repeat("ab", null));
// prints an empty string, because null is converted to 0
```
Los parámetros por defecto siguen la regla de `undefined`, mientras que `??` cubre tanto `null` como `undefined`: elige el que coincida con cómo se llamará tu función.

---

El encadenamiento opcional y la comprobación `== null` funcionan bien juntos: la cadena lee el valor anidado sin lanzar un error, y la comprobación decide qué hacer cuando el resultado falta:
```javascript
function cityOf(user) {
  if (user?.address?.city == null) {
    return "unknown";
  }
  return user.address.city;
}
```
Dentro del último `return` un `.` normal es seguro, porque la comprobación ya ha demostrado que cada eslabón existe.

---

Muchos métodos integrados informan de "nada encontrado" devolviendo `undefined`. El método de arrays `find(callback)` es el ejemplo típico: devuelve el primer elemento para el cual el callback es `true`, o `undefined` cuando ningún elemento coincide:
```javascript
const products = [{ name: "pen", price: 2 }];
const found = products.find((p) => p.name === "ink");
console.log(found);
// prints undefined
```
Leer `found.price` aquí lanzaría un error, así que `?.` y `??` son los compañeros naturales de `find`:
```javascript
console.log(products.find((p) => p.name === "ink")?.price ?? "no price");
// prints no price
```

---

`null` y `undefined` se comportan de forma diferente cuando un objeto se convierte a JSON con `JSON.stringify()`.
JSON tiene un valor `null` pero no `undefined`, así que una propiedad cuyo valor es `undefined` simplemente se **omite**, mientras que una propiedad `null` se conserva:
```javascript
const user = { name: "Ana", nickname: undefined, email: null };
console.log(JSON.stringify(user));
// prints {"name":"Ana","email":null}
```
Dentro de los arrays las posiciones no pueden desaparecer, así que allí `undefined` se convierte en `null`:
```javascript
console.log(JSON.stringify([1, undefined, 3]));
// prints [1,null,3]
```

---

Comprobar `obj.key === undefined` no puede distinguir dos situaciones: la propiedad no existe, o existe y contiene el valor `undefined`.
`Object.hasOwn(obj, key)` responde solo a la primera pregunta: devuelve `true` cuando el objeto tiene su propiedad **propia** llamada `key`, sea cual sea su valor:
```javascript
const config = { debug: undefined };
console.log(config.debug === undefined, config.level === undefined);
// prints true true
console.log(Object.hasOwn(config, "debug"), Object.hasOwn(config, "level"));
// prints true false
```
"Propia" significa declarada en el objeto mismo: los miembros heredados como `toString` están disponibles en todos los objetos, pero `Object.hasOwn(config, "toString")` es `false`.
