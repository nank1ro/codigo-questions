Ya sabes que `extends` convierte una clase en hija de otra. Lo que esa palabra clave realmente te da es **herencia**: la hija obtiene gratis cada propiedad y método del padre, y puede añadir los suyos propios encima.

La pieza que hace útil la herencia es **`super`**. Dentro del constructor de una clase hija, `super(...)` llama al constructor del padre, de modo que el padre puede configurar la parte del objeto que le pertenece:
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
}
class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
}
```
Aquí `super(name)` le pasa `name` a `Animal`, que lo almacena, y `Dog` solo tiene que preocuparse de `breed`.

---

Una clase hija no tiene que redefinir nada de lo que el padre ya proporciona. Los métodos también se heredan, así que una instancia de la hija puede llamarlos como si fueran suyos:
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        return `${this.name} makes a sound`;
    }
}
class Dog extends Animal {}
console.log(new Dog("Max").speak());
// prints Max makes a sound
```
Cuando una hija declara su propio constructor, llamar a `super(...)` dentro de él es **obligatorio**: sin él el objeto nunca se inicializa y JavaScript lanza un `ReferenceError`. Una hija sin constructor alguno está bien, porque JavaScript escribe uno que reenvía cada argumento al padre.

---

La regla sobre `super()` es más estricta que "llámalo en algún sitio". En el constructor de una clase hija la palabra `this` no existe hasta que `super()` se ha ejecutado, porque es el constructor del padre el que crea el objeto. Tocar `this` antes de esa línea lanza un error:
```javascript
class Child extends Base {
    constructor() {
        this.x = 1; // ReferenceError
        super();
    }
}
```
Así que `super(...)` debe ser la **primera sentencia** de cualquier constructor hijo que use `this`.

---

Cuando una hija define un método que el padre ya tiene, gana la versión de la hija. Esto se llama **sobrescritura**:
```javascript
class Animal {
    speak() {
        return "some sound";
    }
}
class Dog extends Animal {
    speak() {
        return "Woof";
    }
}
console.log(new Dog().speak());
// prints Woof
```
La sobrescritura no elimina la versión del padre, solo la oculta. Dentro del método de la hija, `super.methodName(...)` todavía la alcanza, lo que te permite extender el comportamiento del padre en lugar de reemplazarlo:
```javascript
class Puppy extends Dog {
    speak() {
        return super.speak() + "!";
    }
}
console.log(new Puppy().speak());
// prints Woof!
```
Fíjate en la diferencia: `super(...)` llama al **constructor** del padre, `super.name(...)` llama a un **método** del padre.

---

Hasta ahora cada propiedad se creaba dentro del constructor. Un **campo de clase** te permite declararla directamente en el cuerpo de la clase, con un valor inicial opcional:
```javascript
class Counter {
    count = 0;
    step = 1;
}
console.log(new Counter().count);
// prints 0
```
Los campos se asignan a cada nueva instancia antes de que el cuerpo del constructor se ejecute, así que el constructor ya puede confiar en ellos. Un campo sin valor igualmente queda declarado, solo que empieza como `undefined`:
```javascript
class Task {
    done = false;
    title;
}
```
Fíjate en la sintaxis: ni `let`, ni `const`, ni `this` en la declaración, y la línea termina con punto y coma.

---

El orden importa cuando las clases heredan entre sí. Una declaración `class` **no** se eleva como lo hace una `function`: el nombre solo existe desde la línea donde la clase está escrita en adelante. Así que una clase hija tiene que aparecer *después* del padre que extiende, de lo contrario la cláusula `extends` falla con un `ReferenceError`.

---

Algunos comportamientos pertenecen a la clase misma y no a ninguna instancia en particular. Una conversión entre dos unidades, por ejemplo, no necesita un objeto sobre el que trabajar. Marcar un método como **`static`** lo pone en la clase:
```javascript
class MathUtils {
    static double(n) {
        return n * 2;
    }
}
console.log(MathUtils.double(4));
// prints 8
```
Un método estático se llama sobre el nombre de la clase, nunca sobre una instancia: `new MathUtils().double(4)` lanza un `TypeError`, porque las instancias no reciben los miembros estáticos. Dentro de un método estático `this` se refiere a la clase, así que un estático puede llamar a otro con `this.otherStatic(...)`.

---

`static` también funciona en los campos. Una **propiedad estática** se almacena una sola vez en la clase, no una vez por instancia, lo que la convierte en el lugar natural para un contador compartido o una constante:
```javascript
class Circle {
    static PI = 3.14;
}
console.log(Circle.PI);
// prints 3.14
```
Como solo hay una copia, cada instancia que la actualiza actualiza el mismo valor. Dentro de un constructor la accedes a través del nombre de la clase, `Circle.PI`, y no a través de `this`: `this.PI` buscaría una propiedad en la instancia, no encontraría nada y te daría `undefined`.

---

Un uso muy común de un método estático es una **fábrica**: un método que construye una instancia a partir de otra forma de datos y la devuelve. Mantiene `new` en un solo lugar y le da a la construcción un nombre que dice lo que hace:
```javascript
class Duration {
    constructor(seconds) {
        this.seconds = seconds;
    }
    static fromMinutes(minutes) {
        return new Duration(minutes * 60);
    }
}
console.log(Duration.fromMinutes(2).seconds);
// prints 120
```
Una fábrica puede llamarse antes de que exista cualquier instancia, algo que un método normal no puede hacer.

---

Un **getter** es un método que se lee como una propiedad. Escribe `get` delante de él y omite los paréntesis en el punto de llamada:
```javascript
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    get area() {
        return this.width * this.height;
    }
}
const r = new Rectangle(3, 4);
console.log(r.area);
// prints 12
```
`r.area` ejecuta el método y devuelve su resultado, así que es un número. Añadir paréntesis intentaría entonces llamar a ese número, lo que falla.

El reflejo es un **setter**, declarado con `set`, que se ejecuta cuando se asigna la propiedad. Recibe exactamente un parámetro:
```javascript
set area(value) {
    this.width = value / this.height;
}
```

---

El verdadero valor de un setter es que puede negarse. Entre la asignación y el valor almacenado tienes la oportunidad de comprobar, limitar o rechazar lo que llega:
```javascript
class Volume {
    constructor(level) {
        this._level = level;
    }
    get level() {
        return this._level;
    }
    set level(value) {
        if (value <= 10) {
            this._level = value;
        }
    }
}
const v = new Volume(3);
v.level = 50;
console.log(v.level);
// prints 3, the setter rejected 50
```
Un getter y un setter con el mismo nombre forman una sola propiedad, así que no pueden ser además un campo normal: el valor almacenado vive bajo un nombre distinto, por convención el mismo nombre con un guion bajo delante.

---

El guion bajo inicial de `_temperature` es solo una convención: nada impide que el mundo exterior escriba `v._level = 999` y pase de largo junto a tu setter. Un **campo privado** lo hace cumplir el lenguaje. Su nombre empieza con `#`, debe declararse en el cuerpo de la clase y solo puede leerse o escribirse desde dentro de esa clase:
```javascript
class Secret {
    #code = 1234;
    reveal() {
        return this.#code;
    }
}
const s = new Secret();
console.log(s.reveal());
// prints 1234
console.log(s.#code);
// SyntaxError: the field is not accessible here
```
Dos detalles hacen tropezar con facilidad. El `#` es parte del nombre, así que siempre escribes `this.#code`, nunca `this.code`. Y un campo privado no aparece en `Object.keys` ni en el `console.log` de la instancia.

---

Los métodos también pueden ser privados. Prefija el nombre con `#` y el método desaparece de la superficie pública de la clase, aunque sigue pudiéndose llamar desde cualquier otro método con `this.#name(...)`:
```javascript
class Receipt {
    #format(n) {
        return `$${n}`;
    }
    print(n) {
        return this.#format(n);
    }
}
console.log(new Receipt().print(7));
// prints $7
```
Así mantienes los pasos auxiliares fuera de la API: quien llama ve `print`, no el detalle de formato que hay detrás. Los campos privados y los métodos privados juntos le dan a una clase un interior y un exterior bien definidos.

---

Imprimir un objeto suele dar algo poco útil. Siempre que JavaScript necesita un string y obtiene un objeto en su lugar, llama al método **`toString`** del objeto, y el predeterminado devuelve `[object Object]`. Definir el tuyo propio reemplaza eso:
```javascript
class Money {
    constructor(amount) {
        this.amount = amount;
    }
    toString() {
        return `$${this.amount}`;
    }
}
console.log(`${new Money(7)}`);
// prints $7
```
El mismo método lo usan la concatenación de strings y `String(value)`. Si además quieres un **número** razonable, define `[Symbol.toPrimitive](hint)`, que recibe `"string"`, `"number"` o `"default"` y decide qué devolver; cuando existe gana sobre `toString`.

---

El operador **`instanceof`** pregunta si un objeto fue construido a partir de una clase, o de cualquier clase que herede de ella:
```javascript
class Animal {}
class Dog extends Animal {}
const max = new Dog();
console.log(max instanceof Dog);    // true
console.log(max instanceof Animal); // true, Dog extends Animal
```
JavaScript no tiene una palabra clave `abstract`, pero la misma idea se escribe a mano: una clase base define la forma y cada método que una hija *debe* proporcionar simplemente lanza un error:
```javascript
class Shape {
    area() {
        throw new Error("area() must be implemented");
    }
}
```
Una hija que olvida sobrescribir `area` falla estrepitosamente la primera vez que se usa, en lugar de devolver silenciosamente `undefined`.

---

`for...of` y el operador spread `...` no funcionan sobre cualquier objeto: funcionan sobre **iterables**, objetos que proporcionan un método guardado bajo la clave especial `Symbol.iterator`. Dale a tu clase ese método y se une al club:
```javascript
class Playlist {
    constructor(songs) {
        this.songs = songs;
    }
    *[Symbol.iterator]() {
        for (const song of this.songs) {
            yield song;
        }
    }
}
const list = new Playlist(["a", "b"]);
console.log([...list]);
// prints [ 'a', 'b' ]
```
El `*` delante del nombre lo convierte en un **generador**: una función que entrega valores de uno en uno con `yield` y hace una pausa entre ellos. Esa es la forma más corta de satisfacer el protocolo de iteración, y funciona para valores que se calculan en lugar de almacenarse.
