Es posible que hayas considerado la situación en la que te gustaría reutilizar una parte del código, solo con algunos valores diferentes.
En lugar de reescribir todo el código, es mucho más limpio definir una función, que luego se puede usar repetidamente.
En JavaScript usamos la palabra clave `function` seguida del nombre de la función:
```javascript
function sayHi() {
    console.log("Hello!");
}
sayHi();
// prints "Hello!"
```

---

Los paréntesis en la __definición de función__ no tienen que estar vacíos si queremos especificar parámetros

---

A veces queremos que una función __devuelva__ un valor.
Bueno, existe la palabra clave `return`.

---

Las funciones pueden tener múltiples parámetros de entrada, que se escriben dentro de los paréntesis de la función, separados por comas.
```javascript
function sayHello(name, newUser) {
  var greet = `Hello ${name}!`;
  if (newUser) {
    greet += " Welcome on board :)";
  }
  return greet;
}
// prints "Hello Smith! Welcome on board :)"
console.log(sayHello("Smith", true));
```

---

Puedes definir un valor _predeterminado_ para cualquier parámetro en una función asignando un valor al parámetro después del tipo de ese parámetro.
Si se define un valor predeterminado, puedes omitir ese parámetro cuando llames a la función
```javascript
function someFunction(parameterWithoutDefault, parameterWithDefault = 12) {
    // do stuff here
}
```

---

La sintaxis del __parámetro rest__ nos permite representar un número indefinido de argumentos como un array.
Escribe parámetros rest insertando tres caracteres de punto `...` antes del nombre del parámetro.
Los valores pasados a un parámetro rest están disponibles dentro del cuerpo de la función como un array.
Por ejemplo, un parámetro rest con un nombre de `numbers` está disponible dentro del cuerpo de la función como un array constante llamado numbers

---

En las funciones podemos añadir un _comentario opcional_ que explique qué hace la función:
```javascript
// Prints 'Hello World' to the console.
function helloWorld() {
    console.log("Hello, World!");
}
```
Podemos usar `//` para un comentario de una línea y `/** */` para un comentario de varias líneas
