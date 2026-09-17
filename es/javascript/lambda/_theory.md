Una función no necesita un nombre. Una **expresión de función** crea una función como un valor, que puedes almacenar en una variable y llamar a través de ella:
```javascript
const add = function (a, b) {
  return a + b;
};
console.log(add(2, 3));
// imprime 5
```
Una **función flecha** es una forma más corta de escribir lo mismo: elimina la palabra clave `function` y pon una "flecha gruesa" `=>` entre la lista de parámetros y el cuerpo:
```javascript
const add = (a, b) => {
  return a + b;
};
console.log(add(2, 3));
// imprime 5
```
Las funciones flecha suelen almacenarse en una `const`, así el nombre no puede ser reasignado por error, y se llaman exactamente igual que cualquier otra función.

---

Las funciones flecha se acortan en dos casos comunes.
Cuando el cuerpo es una **única expresión**, puedes omitir las llaves y la palabra clave `return`: el valor de la expresión se devuelve automáticamente (un **retorno implícito**):
```javascript
const add = (a, b) => a + b;
console.log(add(2, 3));
// imprime 5
```
Cuando hay **exactamente un parámetro**, también puedes omitir los paréntesis a su alrededor:
```javascript
const double = n => n * 2;
console.log(double(4));
// imprime 8
```
Con cero parámetros o con dos o más, los paréntesis son obligatorios: `() => 42` y `(a, b) => a + b`.

---

Hay una trampa con el retorno implícito. Una función flecha cuyo cuerpo empieza con `{` se lee como un **cuerpo de bloque**, nunca como un objeto literal:
```javascript
const make = (name) => { name: name };
console.log(make("Ana"));
// imprime undefined
```
Aquí `{ name: name }` es un bloque que contiene la etiqueta `name:` seguida de la expresión `name`. No se devuelve nada, así que la llamada da `undefined`.
Para devolver un objeto literal en una sola línea, rodéalo con **paréntesis** para que JavaScript lo trate como una expresión:
```javascript
const make = (name) => ({ name: name });
console.log(make("Ana"));
// imprime { name: 'Ana' }
```

---

Rodear el objeto literal con paréntesis es la forma estándar de construir objetos con una función flecha de una sola línea, por ejemplo cuando conviertes un par de valores en un registro:
```javascript
const user = (name, age) => ({ name: name, age: age });
console.log(user("Ana", 30).age);
// imprime 30
```
Una función flecha sin parámetros empieza con un par vacío de paréntesis `()`:
```javascript
const empty = () => ({});
console.log(empty());
// imprime {}
```

---

Las funciones flecha brillan de verdad como **callbacks**: funciones pasadas como argumentos a otras funciones. Los métodos de array son el ejemplo más común.
`map(callback)` devuelve un nuevo array con el resultado del callback para cada elemento, y `filter(callback)` devuelve un nuevo array con solo los elementos para los que el callback devuelve `true`:
```javascript
const numbers = [1, 2, 3, 4];
console.log(numbers.map((n) => n * 10));
// imprime [ 10, 20, 30, 40 ]
console.log(numbers.filter((n) => n > 2));
// imprime [ 3, 4 ]
```
Ambos devuelven un nuevo array y dejan el original intacto, así que puedes encadenarlos: `numbers.filter(...).map(...)`.

---

Dos métodos de array más toman un callback.
`forEach(callback)` llama al callback una vez por elemento y no devuelve nada; úsalo para efectos secundarios como imprimir.
`reduce(callback, initialValue)` pliega el array en un único valor: el callback recibe el valor acumulado hasta ahora y el elemento actual, y devuelve el nuevo valor acumulado:
```javascript
const numbers = [1, 2, 3];
numbers.forEach((n) => console.log(n));
// imprime 1, 2 y 3 en tres líneas
const total = numbers.reduce((sum, n) => sum + n, 0);
console.log(total);
// imprime 6
```

---

`sort(compare)` ordena un array en el lugar usando un callback que recibe dos elementos y devuelve un número negativo cuando el primero debe ir primero, un número positivo cuando el segundo debe ir primero, o `0` cuando son iguales. Para números, `(a, b) => a - b` ordena en orden ascendente y `(a, b) => b - a` en orden descendente.
`find(callback)` devuelve el primer elemento para el que el callback devuelve `true`, o `undefined` si no hay ninguno:
```javascript
const scores = [50, 90, 70];
scores.sort((a, b) => a - b);
console.log(scores);
// imprime [ 50, 70, 90 ]
console.log(scores.find((s) => s > 60));
// imprime 70
```

---

Los parámetros de las funciones flecha admiten las mismas características que los parámetros de las funciones regulares.
Un **valor por defecto** se usa cuando el argumento se omite o es `undefined`:
```javascript
const greet = (name = "World") => `Hello, ${name}!`;
console.log(greet());
// imprime Hello, World!
console.log(greet("Ana"));
// imprime Hello, Ana!
```
Ten en cuenta que un parámetro con un valor por defecto siempre necesita los paréntesis, incluso cuando es el único: `name = "World" => ...` es un error de sintaxis.

---

Un **parámetro rest** `...name` recopila cualquier cantidad de argumentos en un array, y también funciona en las funciones flecha:
```javascript
const count = (...items) => items.length;
console.log(count("a", "b", "c"));
// imprime 3
```
Las funciones regulares también tienen un oculto objeto similar a un array llamado `arguments` que contiene todos los argumentos que recibieron. Las funciones flecha **no**: dentro de una flecha, `arguments` se refiere al `arguments` de la función que la rodea o no existe en absoluto. Siempre que necesites "todos los argumentos" en una función flecha, usa un parámetro rest.

---

Una función recuerda las variables del ámbito donde fue **creada**, incluso después de que ese ámbito haya terminado de ejecutarse. Esto se llama una **clausura**.
El ejemplo clásico es un fabricante de contadores: cada llamada a `makeCounter` crea un `count` nuevo y devuelve una función flecha que sigue usando ese mismo `count`:
```javascript
const makeCounter = () => {
  let count = 0;
  return () => {
    count += 1;
    return count;
  };
};
const next = makeCounter();
console.log(next());
// imprime 1
console.log(next());
// imprime 2
```
Nadie más puede leer o reiniciar `count`: vive solo dentro de la función devuelta. Una segunda llamada a `makeCounter()` crea un contador independiente con su propio `count`.

---

Como una función es un valor, una función flecha puede **devolver otra función flecha**. Encadenar dos flechas es una forma compacta de escribir una función que construye funciones:
```javascript
const makeAdder = (amount) => (n) => n + amount;
const addTen = makeAdder(10);
console.log(addTen(5));
// imprime 15
console.log(makeAdder(1)(5));
// imprime 6
```
Léela de izquierda a derecha: `makeAdder` toma `amount` y devuelve `(n) => n + amount`, una función flecha que captura `amount` mediante una clausura. `makeAdder(1)(5)` llama a la función devuelta inmediatamente.

---

No tienes que almacenar una función flecha para llamarla. Rodéala con paréntesis y añade la lista de argumentos justo después: esto es una función flecha **invocada inmediatamente**:
```javascript
const doubled = ((n) => n * 2)(5);
console.log(doubled);
// imprime 10
```
Los paréntesis alrededor de la flecha son obligatorios: sin ellos `(n) => n * 2(5)` intentaría llamar al número `2`. Las funciones invocadas inmediatamente son útiles para calcular un valor con unas pocas variables temporales que no deberían filtrarse al resto del programa.

---

La mayor diferencia entre una función regular y una función flecha es la palabra clave `this`.
Una `function` regular obtiene su **propio** `this`, decidido por *cómo se la llama*: en `team.intro()` es `team`, pero en un callback pasado a `map` nadie lo establece, así que `this.name` es `undefined` (o incluso un error en modo estricto).
Una función flecha **no** tiene un `this` propio: simplemente usa el `this` del código que la rodea (un `this` **léxico**). Por eso los callbacks flecha dentro de un método pueden seguir usando el objeto:
```javascript
const team = {
  name: "Tigers",
  players: ["Ana", "Bo"],
  intro() {
    return this.players.map((p) => `${p} plays for ${this.name}`);
  },
};
console.log(team.intro());
// imprime [ 'Ana plays for Tigers', 'Bo plays for Tigers' ]
```
Con `function (p) { return ... this.name ... }` como callback, el mismo código imprimiría `undefined` en lugar de `Tigers`.
El lado negativo: no uses una función flecha como **método** de un objeto que necesite `this`, porque no se referirá al objeto.
