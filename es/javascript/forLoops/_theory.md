Sabemos cómo repetir código usando un bucle `while`.
Como este programa que repite instrucciones para mostrar `hello`
```javascript
var counter = 0;

while (counter < 5) {
    console.log("hello");
    counter++;
}
```
Pero podemos hacer lo mismo con bucles `for`:
```javascript
for (let i = 0; i < 5; i++) {
    console.log("hello");
}
```

---

En un bucle `for` podemos especificar cuántas veces queremos que se ejecute nuestro bucle

---

Podemos usar `<` para hacer un bucle hasta el siguiente número excluido, o `<=` para hacer un bucle hasta el siguiente número incluido

---

La variable llamada `i` es la variable contadora.
Podemos darle el nombre que queramos.
Cuenta en qué repetición del bucle nos encontramos

---

En JavaScript también tenemos el bucle `forEach`.
De hecho, `forEach` llama al cierre dado en cada elemento de la secuencia en el mismo orden que un bucle `for`:
```javascript
// esto es un array, hablaremos de eso pronto
let numbers = [1, 3, 5, 7, 9];
numbers.forEach((num) => console.log(num));}
```
El uso del método `forEach` es distinto de un bucle `for` en dos aspectos importantes:
1. Las instrucciones `break` o `continue` no se pueden usar para salir de la llamada actual de la clausura del cuerpo o para omitir llamadas posteriores.
2. El uso de la instrucción `return` en la clausura del cuerpo solo saldrá de la clausura y no del ámbito externo, y no omitirá llamadas posteriores.
NOTA: `=>` se llama _función flecha_ y es una sintaxis de función más corta de ES6 que reemplaza llaves {} y devuelve el valor (si es necesario)
