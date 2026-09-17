Una **enumeración** (o *enum*) es un tipo común para un pequeño grupo de valores fijos y relacionados: los días de la semana, los palos de una baraja, los posibles estados de un pedido.
A diferencia de muchos lenguajes, JavaScript **no** tiene la palabra clave `enum`. El reemplazo idiomático es un objeto simple cuyas propiedades son los miembros, pasado a `Object.freeze()` para que nadie pueda cambiarlo después:
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// imprime red
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
// imprime done
```
Una vez congelado, el objeto tampoco puede recibir nuevas propiedades, y `Object.isFrozen(obj)` te dice si un objeto ha sido congelado:
```javascript
console.log(Object.isFrozen(Status));
// imprime true
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
// imprime s
console.log(Size.MEDIUM);
// imprime undefined
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
// imprime true
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
// imprime [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// imprime [ 'red', 'blue' ]
```
Combinar `Object.values()` con el método de array `includes()` es la forma estándar de comprobar si un valor arbitrario, por ejemplo uno leído de una entrada de usuario, es un miembro válido:
```javascript
console.log(Object.values(Color).includes("red"));
// imprime true
console.log(Object.values(Color).includes("pink"));
// imprime false
```

---

Las enumeraciones combinan naturalmente con la sentencia `switch`, que compara un valor con una lista de etiquetas `case` y ejecuta el código de la primera que coincida.
Cada rama termina con `return` o `break`, y la rama opcional `default` se ejecuta cuando nada coincide:
```javascript
const Light = Object.freeze({ RED: "red", GREEN: "green" });

function action(light) {
  switch (light) {
    case Light.RED:
      return "stop";
    case Light.GREEN:
      return "go";
    default:
      return "unknown";
  }
}
console.log(action(Light.GREEN));
// imprime go
```
Compara siempre con los miembros (`Light.RED`), nunca con los valores en bruto (`"red"`): si el valor cambia alguna vez, el `switch` sigue funcionando.

---

Ir de un valor de vuelta a su nombre de miembro se llama una **búsqueda inversa**. Recorre los nombres con `Object.keys()` y elige el primero cuyo valor coincida, usando el método de array `find()`, que devuelve el primer elemento para el que el callback es `true` (o `undefined` si no hay ninguno):
```javascript
const Priority = Object.freeze({ LOW: 1, HIGH: 3 });
let name = Object.keys(Priority).find((key) => Priority[key] === 3);
console.log(name);
// imprime HIGH
```
`Priority[key]` lee el miembro cuyo nombre está almacenado en la variable `key`, la misma notación de corchetes que usas para cualquier objeto.

---

Los miembros de tipo cadena tienen una debilidad: cualquier cadena con el mismo texto es aceptada como miembro.
```javascript
const Color = Object.freeze({ RED: "red" });
console.log(Color.RED === "red");
// imprime true
```
Cuando quieras miembros que sean iguales **solo** a sí mismos, usa un `Symbol`. `Symbol(description)` crea un valor totalmente nuevo que es diferente de cualquier otro símbolo, incluso uno creado con la misma descripción:
```javascript
const Suit = Object.freeze({
  HEARTS: Symbol("hearts"),
  SPADES: Symbol("spades"),
});
console.log(Suit.HEARTS === Suit.HEARTS);
// imprime true
console.log(Suit.HEARTS === Symbol("hearts"));
// imprime false
console.log(typeof Suit.HEARTS);
// imprime symbol
```
El texto que pasas es solo una etiqueta para depuración; puedes leerlo de vuelta con la propiedad `description` (`Suit.HEARTS.description` es `"hearts"`).

---

Los valores de enumeración se usan a menudo como **claves** de otro objeto, por ejemplo para asociar cada miembro a una etiqueta o un precio. Dentro de un objeto literal, envolver una clave entre corchetes `[ ]` evalúa la expresión y usa su resultado como clave (una **clave calculada**). Esto funciona tanto con miembros de tipo cadena como de tipo símbolo:
```javascript
const Status = Object.freeze({ ACTIVE: "active", DONE: "done" });
const labels = {
  [Status.ACTIVE]: "In progress",
  [Status.DONE]: "Completed",
};
console.log(labels[Status.DONE]);
// imprime Completed
```
Sin los corchetes, `Status.DONE: "Completed"` sería un error de sintaxis, y `"Status.DONE"` sería una simple clave de tipo cadena.

---

Cuando cada miembro necesita varios datos o sus propios métodos, una **clase** puede jugar el papel de la enumeración. Cada miembro es una instancia de la clase, almacenada en una propiedad `static`, es decir, una propiedad que pertenece a la clase misma en lugar de a cada instancia:
```javascript
class Planet {
  static MERCURY = new Planet("Mercury", 0.4);
  static EARTH = new Planet("Earth", 1);

  constructor(name, gravity) {
    this.name = name;
    this.gravity = gravity;
  }
}
console.log(Planet.EARTH.name);
// imprime Earth
```
Llama a `Object.freeze(Planet)` después de la clase para evitar que alguien añada o reemplace miembros, y congela cada instancia en el constructor con `Object.freeze(this)` para que los propios miembros permanezcan de solo lectura.
