La toma de decisiones es necesaria cuando queremos ejecutar código solo si se cumple una cierta condición.
Supongamos que queremos jugar afuera solo si el clima es agradable.
En programación, podemos guardar una variable booleana `niceWeather` y realizar la acción de jugar afuera `if` esta variable es `true`, como:
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```

---

Continuemos con el ejemplo anterior.
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```
Hemos visto que la sentencia `if` ejecuta el bloque de código solo si la condición es `true`.
Otra cosa importante a considerar está representada por los **corchetes de apertura y cierre** `{}` que indican un bloque de código.

---

Acabamos de ver cómo ejecutar un bloque de código si se cumple una condición, ahora veamos cómo ejecutar otro bloque de código si la primera condición falla.
Vamos a jugar afuera si el clima es agradable; de lo contrario, nos quedamos en casa.
En JavaScript podemos usar la sentencia `else`, como:
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
} else {
    // stay home
}
```

---

Supongamos que tenemos otra condición que verificar, como en este ejemplo:
```javascript
var num = 3;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else {
    console.log("do something else");
}
```
y la salida de este código es `the number is 3`.
Primero, verifiquemos si el número es igual a 2, esto es false.
Entonces, continuemos con la segunda sentencia y verifiquemos si `num` es igual a 3, siendo true ejecutamos el siguiente bloque de código imprimiendo `the number is 3`

---

Podemos añadir tantas sentencias `else if` como queramos, no hay límites
```javascript
var num = 4;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else if (num == 4) {
    console.log("the number is 4");
} else if (num == 5) {
    console.log("the number is 5");
} else if (num == 6) {
    console.log("the number is 6");
}
```
y la salida de este código es `the number is 4`.

---

También podemos anidar una sentencia condicional (`if`, `else if` o `else`) dentro de otra sentencia condicional, para crear una estructura más compleja.
```javascript
var num = 4;
if (num < 3) {
    console.log("the number is lower than 3");
} else {
    if (num == 3) {
        console.log("the number is 3");
    } else if (num == 4) {
        console.log("the number is 4");
    } else {
        console.log("the number is greather than 4");
    }
}
```
y la salida de este código es `the number is 4`.

---

El operador condicional ternario es un operador especial con tres partes, que toma la forma `question ? answer1 : answer2`.
Es un atajo para evaluar una de dos expresiones basándose en si `question` es true o false.
Si `question` es true, evalúa `answer1` y devuelve su valor; de lo contrario, evalúa `answer2` y devuelve su valor.
```javascript
let a = 10, b = 20, c = 0;
if (a < b) {
    c = a;
} else {
    c = b;
}
console.log(c);
// prints 10
```
El código abreviado para el código anterior es:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// prints 10
```
`c` se establece igual a `a`, porque la condición `a < b` era true

---

El _operador coalescencia nula_ `a ?? b` desenvuelve un `a` opcional si contiene un valor, o devuelve un valor predeterminado `b` si `a` es `nil`.
La expresión `a` es siempre de tipo opcional.
La expresión `b` debe coincidir con el tipo que se almacena dentro de a.
El operador coalescencia nula es una abreviatura del código siguiente:
```javascript
a != nil ? a! : b;
```
