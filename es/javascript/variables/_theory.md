Las variables son contenedores para almacenar valores de datos.
Toda variable en JavaScript es un objeto.
Para crear una variable, necesitamos darle un **nombre** teniendo en cuenta que no debe contener espacios.
Una variable se crea en el momento en que le asignas un valor por primera vez.
En JavaScript declaras constantes con las palabras clave `let` o `const` y variables con la palabra clave `var`.
El valor de una constante no puede cambiar una vez que se establece, mientras que una variable puede establecerse a un valor diferente en el futuro.
Un ejemplo de creación de una variable llamada `x` es:
```javascript
var x = 1;
```
De esta manera hemos asignado el valor `1` a la variable llamada `x`.
Si imprimimos la variable `x` obtenemos el número `1`:
```javascript
console.log(x);
// prints 1
```

---

Las variables se llaman así porque el valor que almacenan puede cambiar.
Podemos actualizar `x` usando `=` y dándole un nuevo valor.
```javascript
var x = 1;
console.log(x); // prints 1
x = 2;
console.log(x); // prints 2
```

---

También podemos asignar a las variables los valores de otras variables.
Aquí, podemos asignar a la variable `y` el valor de `x`
```javascript
var x = 5;
var y = x;
console.log(y); // prints 5
```

---

Cuando actualizamos una variable, olvida su valor anterior.
Aquí podemos mostrar la variable `x` dos veces y ver cómo se actualiza su valor.
```javascript
var x = 5;
console.log(x); // prints 5
x = 10;
console.log(x); // prints 10
```

---

En JavaScript las variables de cadena se pueden declarar usando tanto comillas dobles como simples:
```javascript
let x = "May";
// both are the same string
let y = 'May';
console.log(x === y);
// prints true
```

---

Si queremos un nombre de variable con múltiples palabras, usamos **camelCase**.
Es la práctica de escribir frases de modo que cada palabra en el medio de la frase comience con una letra mayúscula
