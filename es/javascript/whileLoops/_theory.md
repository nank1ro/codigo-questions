A menudo en programación, necesitamos repetir un bloque de código, por ejemplo:
```javascript
console.log("2 seconds");
console.log("3 seconds");
console.log("4 seconds");
console.log("5 seconds");
```
Esto produce la siguiente salida:
```javascript
2 seconds
3 seconds
4 seconds
5 seconds
```
Obviamente, para declaraciones largas pasaríamos mucho tiempo escribiendo el código, pero por suerte, podemos usar bucles.
Aprendamos el bucle `while`, obteniendo la misma salida anterior.
```javascript
var count = 2;
while (count <= 5) {
    console.log(`${count} seconds`);
    count += 1;
}
```
Así creamos una variable `count` asignando `2`, el valor inicial.
Luego hemos usado la declaración `while` que ejecutará el bloque de código hasta que la condición `count <= 5` sea `true`.
Dentro del bloque de código, **NO** debemos olvidar agregar la línea `count += 1`.
Incrementa el valor de `count`, de lo contrario, nuestro bucle será infinito

---

To control the times a `while` loop repeats, we start with a variable set to a number.
We call this variable a counter variable

---

Then, we use a comparison in the condition to compare the `counter` variable to a number.

---

Inside the block of code, in order to stop the `while` loop, we increment the `counter` variable.

---

The order you write code affects the output.

---

In JavaScript we also have the **do-while** variation of the `while` loop.
It performs a single pass through the loop block first, _before_ considering the loop's condition.
It then continues to repeat the loop until the condition is `false`.
