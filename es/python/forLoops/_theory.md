Sabemos cómo repetir código usando un bucle `while`.
Como este programa que repite sentencias para mostrar `hello`
```python
counter = 0

while counter < 5:
    print("hello")
    counter += 1
```
Pero podemos hacer lo mismo con bucles `for`:
```python
for i in range(5):
    print("hello")
```

---

En un bucle `for` podemos especificar cuántas veces queremos que se ejecute nuestro bucle con la función `range()`

---

Añadir un número como `5`, dentro de la función `range()` significa que hará un bucle sobre el bloque de código 5 veces, desde `0` hasta `4`

---

La variable llamada `i` es la variable de contador.
Podemos darle el nombre que queramos.
Cuenta en qué repetición del bucle nos encontramos actualmente

---

La función `range()` devuelve una secuencia de números, comenzando desde 0 por defecto, e incrementa por 1 (por defecto), y se detiene antes de un número especificado.
Esta es la sintaxis de la función:
```python
range(start, stop, step)
```
`start` y `step` son opcionales, mientras que `stop` es obligatorio
