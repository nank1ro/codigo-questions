Sabemos repetir cdigo usando un bucle `while`.
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

En un bucle `for` podemos especificar cuntas veces queremos que se ejecute nuestro bucle con la funcin `range()`

---

Agregar un nmero como `5`, dentro de la funcin `range()` significa que iterar sobre el bloque de cdigo 5 veces, desde `0` hasta `4`

---

La variable llamada `i` es la variable contadora.
Podemos darle el nombre que queramos.
Cuenta en qu repeticin del bucle estamos actualmente

---

La funcin `range()` devuelve una secuencia de nmeros, comenzando desde 0 por defecto, e incrementa en 1 (por defecto), y se detiene antes de un nmero especificado.
Esta es la sintaxis de la funcin:
```python
range(start, stop, step)
```
`start` y `step` son opcionales, mientras que `stop` es obligatorio
