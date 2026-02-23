A menudo en programación, necesitamos repetir un bloque de código, por ejemplo:
```c
printf("2 seconds\n");
printf("3 seconds\n");
printf("4 seconds\n");
printf("5 seconds\n");
```
Esto produce la siguiente salida:
```c
2 seconds
3 seconds
4 seconds
5 seconds
```
Obviamente, para sentencias largas gastaríamos mucho tiempo escribiendo el código, pero afortunadamente, podemos usar bucles.
Aprendamos el bucle `while`, obteniendo la misma salida anterior.
```c
int count = 2;
while (count <= 5) {
    printf("%d seconds\n", count);
    count++;
}
```
Así creamos una variable `count` asignando `2`, el valor inicial.
Luego hemos usado la sentencia `while` que ejecutará el bloque de código hasta que la condición `count <= 5` sea `true`.
Dentro del bloque de código, **NO** debemos olvidar agregar la línea `count++;`.
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
