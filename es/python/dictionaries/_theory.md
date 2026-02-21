**Los Diccionarios** son similares a las listas y tuplas, pero accedes a los valores buscando una *clave* en lugar de un índice.
Una clave puede ser cualquier cadena o número.
Los diccionarios se encierran entre llaves, así:
```python
d = {"clave1": 1, "clave2": 2, "clave3": 3}
```
Este es un diccionario llamado `d` con tres *pares clave-valor*.
La clave `clave1` apunta al valor `1`, `clave2` a `2`, y así sucesivamente.

---

Acceder a los valores de un diccionario por clave es igual que acceder a los valores de una lista por índice:
```python
usuario['edad']
# obtiene el valor de edad del diccionario usuario
```

---

Como las Listas, los Diccionarios son _mutables_.
Esto significa que pueden cambiar después de ser creados.
Una ventaja de esto es que podemos agregar nuevos _pares clave/valor_ al diccionario después de que se crea, así:
```python
nombre_diccionario[nueva_clave] = nuevo_valor
```

---

La longitud `len()` de un diccionario es el número de _pares clave-valor_ que tiene.
Cada par cuenta solo una vez, incluso si el valor es una lista. (Es correcto: ¡también puedes poner listas dentro de los diccionarios!)

---

Debido a que los diccionarios son mutables, pueden cambiar de muchas maneras. Los elementos pueden eliminarse de un diccionario con el comando `del`:
```python
del nombre_diccionario[clave]
```
eliminará la clave `clave` y su valor asociado del diccionario.

---

¿Qué pasa si queremos listar todas las claves del diccionario?
Bueno, está el método `keys()`.

---

¿Qué pasa si queremos listar todos los valores del diccionario?
Bueno, está el método `values()`.

---

Como con las listas, podemos iterar entre los elementos del diccionario usando las palabras clave `for..in`
Para obtener tanto la clave como el valor en el bucle, podemos usar el método `items()`:
```python
for clave, valor in nombre_diccionario:
    print(clave, valor)
```

---

También podemos usar la palabra clave `in` que usamos con los bucles para determinar si un diccionario contiene cierta __clave__

---

Para __agregar__ o __cambiar__ valores a un diccionario, también podemos usar el método `update()` con los _pares clave-valor_ que queremos agregar entre llaves

---

¿Qué pasa si queremos __eliminar__ un valor de un diccionario?
Está el método `pop()`:
```python
nombre_diccionario.pop("clave")
```
