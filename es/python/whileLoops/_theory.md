A menudo en la programación, necesitamos repetir un bloque de código, por ejemplo:
```python
print("2 seconds")
print("3 seconds")
print("4 seconds")
print("5 seconds")
```
Esto produce el siguiente resultado:
```python
2 seconds
3 seconds
4 seconds
5 seconds
```
Obviamente, para sentencias largas pasaríamos mucho tiempo escribiendo el código, pero afortunadamente, podemos usar bucles.
Aprendamos el bucle `while`, obteniendo el mismo resultado anterior.
```python
count = 2
while (count <= 5):
    print(f"{count} seconds")
    count += 1
```
Entonces creamos una variable `count` asignándole `2`, el valor inicial.
Luego usamos la sentencia `while` que ejecutará el bloque de código hasta que la condición `count <= 5` sea `True`.
Dentro del bloque de código, **NO** debemos olvidar agregar la línea `count += 1`.
Incrementa el valor de `count`, de lo contrario, nuestro bucle será infinito

---

Para controlar cuántas veces se repite un bucle `while`, comenzamos con una variable establecida en un número.
Llamamos a esta variable una variable de contador

---

Luego, usamos una comparación en la condición para comparar la variable `counter` con un número.

---

Dentro del bloque de código, para detener el bucle `while`, incrementamos la variable `counter`.

---

El orden en que escribes el código afecta la salida.
