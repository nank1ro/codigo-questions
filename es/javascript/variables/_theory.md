Las variables son contenedores para almacenar valores de datos.
Cada variable en JavaScript es un objeto.
Para crear una variable, necesitamos darle un **nombre** teniendo en cuenta que no debe contener espacios.
Una variable se crea en el momento en que le asignas un valor por primera vez.
En JavaScript declaras constantes con las palabras clave `let` o `const` y variables con la palabra clave `var`.
El valor de una constante no se puede cambiar una vez establecido, mientras que una variable puede establecerse a un valor diferente en el futuro.
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

Variables are called in this way because the value they store can change.
We can update `x` by using `=` and giving it a new value.
```javascript
var x = 1;
console.log(x); // prints 1
x = 2;
console.log(x); // prints 2
```

---

We can also give variables the values of other variables.
Here, we can give to the `y` variable the value of `x`
```javascript
var x = 5;
var y = x;
console.log(y); // prints 5
```

---

When we update a variable, it forgets its previous value.
Here we can display the `x` variable twice and see how its value updates.
```javascript
var x = 5;
console.log(x); // prints 5
x = 10;
console.log(x); // prints 10
```

---

In JavaScript string variables can be declared using both double quotes and single quotes:
```javascript
let x = "May";
// both are the same string
let y = 'May';
console.log(x === y);
// prints true
```

---

If we want a variable name with multiple words, we use **camelCase**.
It is the practice of writing phrases such that each word in the middle of the phrase begins with a capital letter
