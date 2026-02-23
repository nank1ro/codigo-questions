Para controlar las veces que un bucle `while` se repite, comenzamos con una variable establecida en un número.
A esta variable la llamamos variable contador

---

A menudo en programación, necesitamos repetir un bloque de código, por ejemplo:
```python
print("2 segundos")
print("3 segundos")
print("4 segundos")
print("5 segundos")
```
Esto produce la siguiente salida:
```python
2 segundos
3 segundos
4 segundos
5 segundos
```
Obviamente, para declaraciones largas gastaríamos mucho tiempo escribiendo el código, pero afortunadamente, podemos usar bucles.
Aprendamos el bucle `while`, obteniendo la misma salida anterior.
```python
contador = 2
while (contador <= 5):
    print(f"{contador} segundos")
    contador += 1
```
Así creamos una variable `contador` asignando `2`, el valor inicial.
Luego usamos la sentencia `while` que ejecutará el bloque de código hasta que la condición `contador <= 5` sea `True`.
Dentro del bloque de código, **NO** debemos olvidar agregar la línea `contador += 1`.
Incrementa el valor de `contador`, de lo contrario, nuestro bucle será infinito

---

Luego, usamos una comparación en la condición para comparar la variable `contador` con un número.

---

Dentro del bloque de código, para detener el bucle `while`, incrementamos la variable `contador`.

---

El orden en que escribes el código afecta la salida.
