Puede que hayas considerado la situación en la que te gustaría reutilizar un pedazo de código, solo con algunos valores diferentes.
En lugar de reescribir todo el código, es mucho más limpio definir una función, que luego puede ser usada repetidamente.
En Python usamos la palabra clave `def` seguida del nombre de la función:
```python
def say_hi():
    print("Hello!")
```

---

A veces queremos que una función __devuelva__ un valor.
Bueno, está la palabra clave `return`

---

Los paréntesis en la __definición de función__ no tienen por qué estar vacíos.
Dentro de ellos, podemos especificar parámetros

---

En las funciones podemos agregar un _comentario opcional_ que explica lo que hace la función:
```python
"""
Imprime 'Hello World' en la consola.
"""
```
