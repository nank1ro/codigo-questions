Podrías haber considerado la situación en la que deseas reutilizar un fragmento de código, solo con unos pocos valores diferentes.
En lugar de reescribir todo el código, es mucho más limpio definir una función, que luego se puede usar repetidamente.
En Python usamos la palabra clave `def` seguida del nombre de la función:
```python
def say_hi():
    print("Hello!")
```

---

Los paréntesis en la __definición de función__ no tienen que estar vacíos.
Dentro de ellos, podemos especificar parámetros

---

A veces queremos que una función __devuelva__ un valor.
Bueno, existe la palabra clave `return`

---

En las funciones podemos agregar un _comentario opcional_ que explique qué hace la función:
```python
"""
Prints 'Hello World' to the console.
"""
```
