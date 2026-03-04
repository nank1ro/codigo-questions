Las listas son un tipo de dato que puedes usar para almacenar una colección de diferentes piezas de información como una secuencia bajo un único nombre de variable.
Una lista almacena múltiples valores de cualquier tipo y utiliza **índices** para distinguir estos valores.
Puedes asignar elementos a una lista con una expresión de la forma:
```python
list_name = [item1, item2]
```

---

Puedes acceder a un elemento individual de la lista por su índice.
Un índice es como una dirección que identifica el lugar del elemento en la lista.
El índice aparece directamente después del nombre de la lista, entre corchetes, así:
```python
list_name[index]
```

Los índices de lista comienzan con `0`, **¡no** con `1`! Accedes al primer elemento de una lista así: `list_name[0]`.
El segundo elemento en una lista está en el índice 1: `list_name[1]`.

---

¡Un índice de lista se comporta como cualquier otro nombre de variable! Se puede usar tanto para acceder como para asignar valores.
Viste cómo acceder a un índice de lista así:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] # Gets the value "Jeremiah"
```
Así es como funciona una asignación:
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] = "Jordan"
names[0] # Gets the new value "Jordan"
```

---

Al igual que las cadenas, las listas tienen una **longitud**.
La longitud de una lista es el número de elementos que contiene

---

Una lista no tiene que tener una longitud fija.
¡Puedes agregar elementos al final de una lista en cualquier momento!
Para agregar un elemento a una lista usamos la palabra clave `append`:
```python
>>> letters = ["a", "b"]
>>> letters.append("c")
>>> print(letters)
['a', 'b', 'c']
```

---

A veces, solo quieres acceder a una parte de una lista.
Considera el siguiente código:
```python
>>> numbers = [1, 2, 3, 4]
>>> slice = numbers[1:3]
>>> print(slice)
[2, 3]
```
Primero, creamos una lista llamada `numbers`.
Luego, tomamos una subsección de la lista y la almacenamos en la lista slice.
Lo hacemos definiendo los índices que queremos incluir después del nombre de la lista: `numbers[1:3]`.
En Python, cuando especificamos una parte de una lista de esta manera, incluimos el elemento con el primer índice, `1`, pero excluimos el elemento con el segundo índice, `3`.

---

¡Puedes dividir una cadena exactamente como una lista! De hecho, puedes pensar en las cadenas como listas de caracteres: cada carácter es un elemento secuencial en la lista, comenzando desde el índice `0`.
```python
list_name[:2]
# Grabs the first two items
list_name[3:]
# Grabs the fourth through last items
```
Si tu porción de lista incluye el primer o último elemento en una lista (o una cadena), el índice de ese elemento no tiene que incluirse.

---

Los elementos de una lista pueden ser de cualquier tipo:
```python
list_name = ["one", 2, True]
```
De hecho, arriba tenemos, en orden, una cadena, un entero y un booleano.
¡Pero también podemos tener listas con listas!

---

A veces necesitas buscar un elemento en una lista.
En Python podemos usar el método `index()`:
```python
>>> names = ["Trevor", "Zac", "Glenn"]
>>> print(names.index("Zac"))
1
```
El código anterior imprime el primer índice que contiene la cadena `"Zac"`, `1` en este caso.
También podemos insertar elementos en una lista en un índice específico, usando el método `insert()`:
```python
>>> names.insert(1, "Ali")
>>> print(names)
['Trevor', 'Ali', 'Zac', 'Glenn']
```
El código anterior inserta `"Ali"` en el índice `1`, lo que desplaza todo lo que viene después de este índice hacia abajo en 1

---

En Python podemos recorrer una lista de una manera muy simple usando las palabras clave `for..in`:
```python
>>> numbers = [1, 2, 3]
>>> for num in numbers:
>>>     print(num)
1
2
3
```
Un nombre de variable sigue a la palabra clave `for`, se le asignará el valor de cada elemento de la lista a su vez.

---

Las **tuplas** son como listas pero mucho más rápidas.
Sin embargo, los valores de las tuplas no se pueden cambiar.
Tendemos a usar tuplas para datos de **solo lectura** que permanecen constantes mientras se ejecuta el programa.
Para crear una tupla usamos paréntesis `()`

---

Puede haber momentos en los que queramos cambiar nuestra tupla a una lista.
Para hacer esto, podemos usar la función `list()`

---

De manera similar, podemos convertir una lista en una tupla
