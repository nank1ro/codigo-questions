**Los diccionarios** son similares a las listas y tuplas, pero accedes a los valores buscando una *clave* en lugar de un índice.
Una clave puede ser cualquier cadena o número.
Los diccionarios se cierran entre llaves, así:
```python
d = {"key1": 1, "key2": 2, "key3": 3}
```
Este es un diccionario llamado `d` con tres *pares clave-valor*.
La clave `key1` apunta al valor `1`, `key2` a `2`, y así sucesivamente.

---

Acceder a los valores del diccionario por clave es como acceder a los valores de la lista por índice:
```python
user['age']
# obtiene el valor de edad del diccionario de usuario
```

---

Como las listas, los diccionarios son _mutables_.
Esto significa que se pueden cambiar después de ser creados.
Una ventaja de esto es que podemos agregar nuevos _pares clave/valor_ al diccionario después de que se cree así:
```python
dict_name[new_key_name] = new_value
```

---

La longitud `len()` de un diccionario es el número de _pares clave-valor_ que tiene.
Cada par cuenta solo una vez, incluso si el valor es una lista. (¡Así es: también puedes poner listas dentro de diccionarios!)

---

Debido a que los diccionarios son mutables, se pueden cambiar de muchas formas. Los elementos se pueden eliminar de un diccionario con el comando `del`:
```python
del dict_name[key_name]
```
eliminará la clave `key_name` y su valor asociado del diccionario.

---

¿Qué pasa si queremos enumerar todas las claves del diccionario?
Bueno, existe el método `keys()`.

---

¿Qué pasa si queremos enumerar todos los valores del diccionario?
Bueno, existe el método `values()`.

---

Como con las listas, podemos hacer un bucle entre elementos del diccionario usando las palabras clave `for..in`
Para obtener tanto la clave como el valor en el bucle, podemos usar el método `items()`:
```python
for key, value in dict_name:
    print(key, value)
```

---

También podemos usar la palabra clave `in` que usamos con bucles para determinar si un diccionario contiene una cierta __clave__

---

Para __agregar__ o __cambiar__ valores en un diccionario, también podemos usar el método `update()` con los _pares clave-valor_ que queremos agregar entre llaves

---

¿Qué pasa si queremos __eliminar__ un valor de un diccionario?
Existe el método `pop()`:
```python
dict_name.pop("key_name")
```
