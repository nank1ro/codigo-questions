Las listas son un tipo de dato que puedes usar para almacenar una colección de diferentes piezas de información como una secuencia bajo un solo nombre de variable.
Una lista almacena múltiples valores de cualquier tipo y usa **índices** para distinguir estos valores.
Puedes asignar elementos a una lista con una expresión de la forma:
```python
nombre_lista = [elemento1, elemento2]
```

---

Al igual que las cadenas, las listas tienen una **longitud**.
La longitud de una lista es el número de elementos que contiene

---

Una lista no tiene que tener una longitud fija.
Puedes agregar elementos al final de una lista en cualquier momento que desees.
Para agregar un elemento a una lista usamos la palabra clave `append`:
```python
>>> letras = ["a", "b"]
>>> letras.append("c")
>>> print(letras)
['a', 'b', 'c']
```

---

Al igual que las cadenas, las listas tienen una **longitud**.
La longitud de una lista es el número de elementos que contiene

---

Un índice de lista se comporta como cualquier otro nombre de variable. Puede usarse tanto para acceder como para asignar valores.
Viste cómo acceder a un índice de lista así:
```python
nombres = ["Jeremías", "Bernardo", "Iván", "Noel"]
nombres[0] # Obtiene el valor "Jeremías"
```
Así funciona una asignación:
```python
nombres = ["Jeremías", "Bernardo", "Iván", "Noel"]
nombres[0] = "Jordán"
nombres[0] # Obtiene el nuevo valor "Jordán"
```

---

A veces, solo quieres acceder a una porción de una lista.
Considera el siguiente código:
```python
>>> numeros = [1, 2, 3, 4]
>>> porcion = numeros[1:3]
>>> print(porcion)
[2, 3]
```
Primero, creamos una lista llamada `numeros`.
Luego, tomamos una subsección de la lista y la almacenamos en la lista porcion.
Hacemos esto definiendo los índices que queremos incluir después del nombre de la lista: `numeros[1:3]`.
En Python, cuando especificamos una porción de una lista de esta manera, incluimos el elemento con el primer índice, `1`, pero excluimos el elemento con el segundo índice, `3`.

---

A veces necesitas buscar un elemento en una lista.
En Python podemos usar el método `index()`:
```python
>>> nombres = ["Trevor", "Zac", "Glenn"]
>>> print(nombres.index("Zac"))
1
```
El código anterior imprime el primer índice que contiene la cadena `"Zac"`, `1` en este caso.
También podemos insertar elementos en una lista en un índice específico, usando el método `insert()`:
```python
>>> nombres.insert(1, "Ali")
>>> print(nombres)
['Trevor', 'Ali', 'Zac', 'Glenn']
```
El código anterior inserta `"Ali"` en el índice `1`, lo que mueve todo, después de este índice, hacia abajo en 1

---

Las **tuplas** son como las listas pero son mucho más rápidas.
Sin embargo, los valores de las tuplas no pueden cambiar.
Tendemos a usar tuplas para datos de **solo lectura** que permanecen constantes mientras se ejecuta el programa.
Para crear una tupla usamos los paréntesis `()`

---

A veces, solo quieres acceder a una porción de una lista.
Considera el siguiente código:
```python
>>> numeros = [1, 2, 3, 4]
>>> porcion = numeros[1:3]
>>> print(porcion)
[2, 3]
```
Primero, creamos una lista llamada `numeros`.
Luego, tomamos una subsección de la lista y la almacenamos en la lista porcion.
Hacemos esto definiendo los índices que queremos incluir después del nombre de la lista: `numeros[1:3]`.
En Python, cuando especificamos una porción de una lista de esta manera, incluimos el elemento con el primer índice, `1`, pero excluimos el elemento con el segundo índice, `3`.

---

Los elementos de la lista pueden ser de cualquier tipo:
```python
nombre_lista = ["uno", 2, True]
```
De hecho, arriba tenemos, en orden, una cadena, un entero y un booleano.
¡Pero también podemos tener listas con listas!

---

Puedes dividir una cadena exactamente igual que una lista. De hecho, puedes pensar en las cadenas como listas de caracteres: cada carácter es un elemento secuencial en la lista, comenzando desde el índice `0`.
```python
nombre_lista[:2]
# Toma los dos primeros elementos
nombre_lista[3:]
# Toma desde el cuarto hasta los últimos elementos
```
Si tu porción de lista incluye el primer o último elemento de una lista (o una cadena), no es necesario incluir el índice de ese elemento.

---

Puede haber veces en las que queramos cambiar nuestra tupla a una lista.
Para hacer esto, podemos usar la función `list()`

---

De igual manera, podemos convertir una lista en una tupla
