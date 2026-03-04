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
Obviamente, para sentencias largas gastaríamos mucho tiempo escribiendo el código, pero afortunadamente, podemos usar bucles.
Aprendamos el bucle `while`, obteniendo la misma salida anterior.
```javascript
var count = 2;
while (count <= 5) {
    console.log(`${count} seconds`);
    count += 1;
}
```
Así que creamos una variable `count` asignando `2`, el valor inicial.
Luego usamos la sentencia `while` que ejecutará el bloque de código hasta que la condición `count <= 5` sea `true`.
Dentro del bloque de código, **NO** debes olvidar agregar la línea `count += 1`.
Incrementa el valor de `count`, de lo contrario, nuestro bucle será infinito

---

Para controlar cuántas veces se repite un bucle `while`, comenzamos con una variable establecida en un número.
Llamamos a esta variable una variable de contador

---

Luego, usamos una comparación en la condición para comparar la variable `counter` con un número.

---

Dentro del bloque de código, para detener el bucle `while`, incrementamos la variable `counter`.

---

El orden en el que escribes el código afecta la salida.

---

En JavaScript también tenemos la variación **do-while** del bucle `while`.
Realiza un único paso a través del bloque de bucle primero, _antes_ de considerar la condición del bucle.
Luego continúa repitiendo el bucle hasta que la condición sea `false`.
