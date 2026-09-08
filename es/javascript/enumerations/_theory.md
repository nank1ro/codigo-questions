Una **enumeración** (o *enum*) es un tipo común para un pequeño grupo de valores fijos y relacionados: los días de la semana, los palos de una baraja, los posibles estados de un pedido.
A diferencia de muchos lenguajes, JavaScript **no** tiene la palabra clave `enum`. El reemplazo idiomático es un objeto simple cuyas propiedades son los miembros, pasado a `Object.freeze()` para que nadie pueda cambiarlo después:
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// prints red
```
Por convención, el objeto se declara con `const`, su nombre empieza con mayúscula y los nombres de los miembros se escriben en `UPPER_CASE`, igual que otras constantes.

---

El valor almacenado en cada miembro depende de ti. Las **cadenas** son la opción más común porque son legibles al imprimirlas, registrarlas o guardarlas en un archivo:
```javascript
const Status = Object.freeze({
  ACTIVE: "active",
  DONE: "done",
});
console.log(Status.DONE);
// prints done
```
Una vez congelado, el objeto tampoco puede recibir nuevas propiedades, y `Object.isFrozen(obj)` te dice si un objeto ha sido congelado:
```javascript
console.log(Object.isFrozen(Status));
// prints true
```

---

¿Por qué congelar el objeto? Un objeto congelado rechaza cualquier cambio: asignar a un miembro existente, agregar uno nuevo o eliminar uno no tiene efecto.
Cómo se muestra el rechazo depende del modo en que se ejecute tu código:
- en **modo no estricto** (*sloppy mode*, el predeterminado para scripts simples) la asignación se **ignora silenciosamente**
- en **modo estricto** (archivos que empiezan con `"use strict"`, módulos ES y cuerpos de clase) se **lanza** un `TypeError`

```javascript
const Size = Object.freeze({ SMALL: "s", LARGE: "l" });
Size.SMALL = "xs";
Size.MEDIUM = "m";
console.log(Size.SMALL);
// prints s
console.log(Size.MEDIUM);
// prints undefined
```
De cualquier forma, la enumeración conserva los valores que definiste, que es exactamente lo que quieres de un conjunto de constantes.

---

Los miembros también pueden contener **números**. Los valores numéricos son útiles cuando los miembros tienen un orden natural, porque puedes compararlos con los operadores habituales:
```javascript
const Priority = Object.freeze({
  LOW: 1,
  MEDIUM: 2,
  HIGH: 3,
});
console.log(Priority.HIGH > Priority.LOW);
// prints true
```
La contrapartida es la legibilidad: imprimir `Priority.HIGH` muestra `3`, lo que te dice mucho menos que la cadena `"high"`.

---

Como una enumeración es solo un objeto, los ayudantes de objeto habituales te permiten inspeccionarla:
- `Object.keys(Enum)` devuelve un array con los **nombres** de los miembros
- `Object.values(Enum)` devuelve un array con los **valores** de los miembros
- `Object.entries(Enum)` devuelve un array de pares `[name, value]`

```javascript
const Color = Object.freeze({ RED: "red", BLUE: "blue" });
console.log(Object.keys(Color));
// prints [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// prints [ 'red', 'blue' ]
```
Combinar `Object.values()` con el método de array `includes()` es la forma estándar de comprobar si un valor arbitrario, por ejemplo uno leído de una entrada de usuario, es un miembro válido:
```javascript
console.log(Object.values(Color).includes("red"));
// prints true
console.log(Object.values(Color).includes("pink"));
// prints false
```
