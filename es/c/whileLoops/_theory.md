A menudo en la programación, necesitamos repetir un bloque de código, por ejemplo:
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
Obviamente, para declaraciones largas gastaríamos mucho tiempo escribiendo el código, pero afortunadamente, podemos usar bucles.
Aprendamos el bucle `while`, obteniendo la misma salida anterior.
```c
int count = 2;
while (count <= 5) {
    printf("%d seconds\n", count);
    count++;
}
```
Entonces creamos una variable `count` asignando `2`, el valor inicial.
Luego usamos la declaración `while` que ejecutará el bloque de código hasta que la condición `count <= 5` sea `true`.
Dentro del bloque de código, **NO** debemos olvidar agregar la línea `count++;`.
Incrementa el valor de `count`, de lo contrario, nuestro bucle será infinito

---

Para controlar cuántas veces se repite un bucle `while`, comenzamos con una variable establecida a un número.
Llamamos a esta variable una variable contadora

---

Luego, usamos una comparación en la condición para comparar la variable `counter` con un número.

---

Dentro del bloque de código, para detener el bucle `while`, incrementamos la variable `counter`.

---

El orden en que escribes el código afecta la salida.
