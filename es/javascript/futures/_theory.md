Algunas operaciones no terminan de inmediato: descargar un archivo, leer de una base de datos, esperar un temporizador. JavaScript no se congela mientras se ejecutan. En su lugar, te entrega una **`Promise`**: un objeto que representa un valor que estará disponible **más tarde**.

Una función marcada con **`async`** siempre devuelve una promesa. Lo que la función devuelva se convierte en el valor dentro de esa promesa:
```javascript
async function fetchNumber() {
  return 42;
}
```
Para sacar el valor de una promesa usas **`await`**. Pausa la función hasta que la promesa tenga su valor y luego te entrega el valor puro. `await` solo está permitido dentro de una función `async`:
```javascript
async function main() {
  const n = await fetchNumber();
  console.log(n);
  // prints 42
}

main();
```
Sin `await`, `n` sería la promesa en sí y `console.log(n)` imprimiría `Promise { 42 }` en lugar del número.

---

Agregar `async` delante de una función cambia lo que entrega: el cuerpo sigue calculando un valor ordinario, pero quien la llama recibe una promesa que lo envuelve.
```javascript
function shout(text) {
  return text.toUpperCase();
}
async function shoutLater(text) {
  return text.toUpperCase();
}

console.log(shout("hi"));
// prints HI
console.log(shoutLater("hi"));
// prints Promise { 'HI' }
```
Las dos funciones contienen el mismo código; solo cambia la forma de leer el resultado. `shoutLater("hi")` debe esperarse con `await` dentro de otra función `async` para que devuelva `"HI"`.

Marcar una función como `async` no cuesta nada cuando no hay nada que esperar, y es lo que te permite usar `await` dentro de ella más adelante.

---

Cuando el valor realmente llega más tarde, construyes la promesa tú mismo con **`new Promise`**. Recibe una función, que a su vez recibe un callback **`resolve`**: llama a `resolve(value)` cuando el valor esté listo y la promesa quedará cumplida con él.
```javascript
const soon = new Promise((resolve) => {
  setTimeout(() => resolve("done"), 1000);
});
```
`setTimeout(callback, ms)` programa que `callback` se ejecute después de `ms` milisegundos y devuelve de inmediato, así que mientras tanto nada queda bloqueado.

La función que se pasa a `new Promise` se ejecuta enseguida, pero la promesa permanece **pending** hasta que se llama a `resolve`. Esperarla con `await` da el valor:
```javascript
async function main() {
  console.log(await soon);
  // prints done, about one second later
}

main();
```

---

Una promesa está siempre en uno de tres estados:

- **pending**: el trabajo aún está en curso;
- **fulfilled**: el trabajo tuvo éxito y la promesa contiene un valor;
- **rejected**: el trabajo falló y la promesa contiene un error.

Una promesa comienza pendiente y cambia de estado como mucho una vez. Una vez que está fulfilled o rejected queda **settled** y nunca vuelve a cambiar.

Llamar a una función `async` nunca espera: inicia el trabajo y te entrega de inmediato una promesa pendiente, así que la línea posterior a la llamada se ejecuta antes de que el trabajo termine. Esa promesa es un objeto normal, no el valor que hay dentro de ella, y por eso olvidar `await` es un error tan común.

---

`await` no es la única forma de leer una promesa. Toda promesa tiene un método **`.then(callback)`**: el callback recibe el valor en cuanto la promesa se cumple.
```javascript
Promise.resolve(21).then((n) => {
  console.log(n);
  // prints 21
});
```
**`Promise.resolve(value)`** construye una promesa que ya está cumplida con `value`, lo cual resulta útil cuando ya tienes el valor a mano pero debes devolver una promesa.

`.then` devuelve una promesa **nueva** cumplida con lo que devuelva el callback, así que las llamadas se pueden **encadenar**, y cada paso trabaja sobre el resultado del anterior:
```javascript
Promise.resolve(21)
  .then((n) => n * 2)
  .then((n) => console.log(n));
// prints 42
```

---

Una función `async` se lee de arriba abajo como cualquier otra función: `await` simplemente la pausa hasta que la promesa esperada se cumple, y luego la ejecución continúa en la línea siguiente.
```javascript
async function main() {
  console.log("start");
  const value = await Promise.resolve("data");
  console.log(value);
  console.log("done");
}

main();
// prints start, then data, then done
```
Fíjate en la última línea: una función `async` igual hay que **llamarla**. Escribir `main` sin los paréntesis define el trabajo pero nunca lo inicia, y no se imprime nada.

---

El trabajo asincrónico también puede fallar. La función que se pasa a `new Promise` recibe un segundo callback, **`reject`**: llama a `reject(error)` y la promesa queda rechazada en lugar de cumplida.
```javascript
function readAge(age) {
  return new Promise((resolve, reject) => {
    if (age >= 0) {
      resolve(age);
    } else {
      reject(new Error("negative age"));
    }
  });
}
```
Rechaza siempre con un objeto `Error`: lleva un `message` y un stack trace, algo que una cadena simple no tiene.

Un rechazo se lee con **`.catch(callback)`**, el reflejo de `.then`. **`Promise.reject(error)`** construye una promesa que ya está rechazada, igual que `Promise.resolve` construye una cumplida:
```javascript
readAge(-1).catch((error) => {
  console.log(error.message);
  // prints negative age
});
```
Llamar a `resolve` y a `reject` a la vez, o dos veces, no cambia nada: solo cuenta la primera llamada.

---

`.then`, `.catch` y `.finally` son eslabones de la misma cadena. Un rechazo se salta todos los `.then` hasta que encuentra un `.catch`; una vez que el callback del `.catch` devuelve un valor, la cadena vuelve a estar cumplida y continúa con normalidad.

**`.finally(callback)`** se ejecuta cuando la cadena se asienta, sin importar si se cumplió o se rechazó. Su callback no recibe argumentos y su valor de retorno se ignora, así que el valor sigue fluyendo hacia el siguiente `.then`. Es el lugar para la limpieza, como ocultar un spinner:
```javascript
Promise.reject(new Error("no network"))
  .then((value) => `ok: ${value}`)
  .catch((error) => `error: ${error.message}`)
  .finally(() => console.log("cleanup"))
  .then((message) => console.log(message));
// prints cleanup, then error: no network
```

---

Dentro de una función `async` no necesitas `.catch`. Esperar con `await` una promesa rechazada **lanza** el error, así que la sentencia ordinaria `try` / `catch` / `finally` lo maneja:
```javascript
async function main() {
  try {
    const data = await load();
    console.log(data);
  } catch (error) {
    console.log(`failed: ${error.message}`);
  } finally {
    console.log("end");
  }
}
```
El otro sentido también funciona: un `throw` dentro de una función `async` no rompe a quien la llama, sino que rechaza la promesa que la función devolvió.
```javascript
async function risky() {
  throw new Error("boom");
}
// risky() returns a promise rejected with Error("boom")
```
Como en cualquier bloque `try`, las líneas posteriores al `await` que falla se omiten, el bloque `catch` se ejecuta y el bloque `finally` se ejecuta en ambos casos.

---

Un uso común de `try` / `catch` alrededor de `await` es reemplazar un fallo por un valor predeterminado razonable, para que quien llama nunca tenga que lidiar con el error:
```javascript
async function sizeOf(path) {
  try {
    return await measure(path);
  } catch (error) {
    return 0;
  }
}
```
Conserva el `await` delante de `measure(path)` aunque el valor se devuelva de inmediato. Sin él, la promesa sale de la función sin pasar nunca por el bloque `try`, y un rechazo escaparía del `catch`.

---

Cuando se necesitan varios resultados, esperarlos uno tras otro pierde tiempo: cada uno comienza solo cuando el anterior ha terminado. **`Promise.all(promises)`** recibe un array de promesas que ya se están ejecutando y devuelve una única promesa cumplida con un array con todos sus valores:
```javascript
const results = await Promise.all([fetchUser(), fetchOrders()]);
```
Dos reglas que vale la pena recordar:

- los valores vuelven **en el orden del array**, no en el orden en que terminaron;
- si alguna promesa se rechaza, la promesa devuelta por `Promise.all` se rechaza de inmediato con ese primer error, y los demás valores se pierden.

---

`Promise.all` funciona con un array de cualquier longitud, incluido uno vacío: esperar `Promise.all([])` devuelve un array vacío de inmediato. Eso hace que sea seguro pasar una lista construida en tiempo de ejecución, sin un caso especial para "nada que esperar".
```javascript
const values = await Promise.all(items);
console.log(values.length === items.length);
// prints true
```
El array que devuelve siempre tiene exactamente tantos elementos como el array que recibió, en las mismas posiciones, así que se puede recorrer como cualquier otro array.

---

La diferencia entre esperar de forma **secuencial** y de forma **paralela** la decide *dónde* colocas `await`:
```javascript
// sequential: about 300 + 300 = 600 ms
const a = await load("a");
const b = await load("b");

// parallel: about 300 ms
const [a, b] = await Promise.all([load("a"), load("b")]);
```
En la primera versión la segunda descarga solo comienza cuando la primera ha terminado, porque `await` pausa la función en esa línea. En la segunda, ambas llamadas se hacen antes de esperar nada, así que las dos descargas ya se están ejecutando mientras `Promise.all` espera.

Usa `await` secuenciales solo cuando la segunda tarea realmente necesite el resultado de la primera. Si no, inicia todo primero y espera todo junto.

---

`Promise.all` se rinde en cuanto una promesa se rechaza. Cuando quieres todos los resultados de todos modos, usa **`Promise.allSettled(promises)`**: nunca se rechaza, y se cumple con un pequeño objeto por promesa, en el mismo orden:

- `{ status: "fulfilled", value: ... }` para las que tuvieron éxito;
- `{ status: "rejected", reason: ... }` para las que fallaron.

```javascript
const results = await Promise.allSettled([
  Promise.resolve(1),
  Promise.reject(new Error("nope")),
]);
console.log(results[0].status);
// prints fulfilled
console.log(results[1].reason.message);
// prints nope
```
Lee `value` solo cuando `status` sea `"fulfilled"`, y `reason` solo cuando sea `"rejected"`: la otra propiedad simplemente no existe.

---

**`Promise.race(promises)`** se asienta en cuanto se asienta la **primera** de las promesas, y copia su desenlace: se cumple con el primer valor, o se rechaza con el primer error. Las demás no se cancelan, siguen ejecutándose, pero lo que produzcan se ignora.
```javascript
const winner = await Promise.race([slowServer(), fastServer()]);
```
El uso típico es un plazo límite: haz competir el trabajo real contra una promesa que falla al cabo de un rato, y obtienes o el resultado o un error de tiempo de espera.

Ten cuidado con un array vacío: `Promise.race([])` queda pendiente para siempre, porque no hay nada que pueda asentarla.

---

Unir las últimas piezas da como resultado una pequeña herramienta que se usa en casi toda aplicación real: un plazo límite. Construye una promesa que se rechace después de `ms` milisegundos, hazla competir contra el trabajo real, y la que se asiente primero decide el desenlace:
```javascript
const timer = new Promise((resolve, reject) => {
  setTimeout(() => reject(new Error("timeout")), ms);
});
return Promise.race([work, timer]);
```
Devolver una promesa desde una función `async` está bien: la promesa que la función entrega sigue a esa promesa, así que quien llama espera el valor final y no una promesa de una promesa.
