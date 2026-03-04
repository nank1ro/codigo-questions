Las variables son contenedores para almacenar valores de datos.
Cada variable en Python es un objeto y a diferencia de otros lenguajes de programación, Python no tiene un comando para declarar una variable.
Para crear una variable, necesitamos darle un **nombre** teniendo en cuenta que no debe contener espacios.
Una variable se crea en el momento en que le asignas un valor por primera vez.
Un ejemplo de creación de una variable nombrada `x` es:
```python
x = 1
```
De esta manera hemos asignado el valor `1` a la variable nombrada `x`.
Si imprimimos la variable `x` obtenemos el número `1`:
```python
>>> print(x)
1
```

---

Las variables se llaman así porque el valor que almacenan puede cambiar.
Podemos actualizar `x` usando `=` y dándole un nuevo valor.
```python
>>> x = 1
>>> print(x)
1
>>> x = 2
>>> print(x)
2
```

---

También podemos darles a las variables los valores de otras variables. Aquí, podemos darle a la variable `y` el valor de `x`
```python
>>> x = 5
>>> y = x
>>> print(y)
5
```

---

Cuando actualizamos una variable, olvida su valor anterior. Aquí podemos mostrar la variable `x` dos veces y ver cómo se actualiza su valor.
```python
>>> x = 5
>>> print(x)
5
>>> x = 10
>>> print(x)
10
```

---

Las variables de cadena se pueden declarar usando comillas simples o dobles:
```python
>>> x = "May"
>>> x = 'May'
```
Ambas son lo mismo.

---

Si queremos un nombre de variable con múltiples palabras, usamos **snake case**.
Significa usar `_` para conectar las palabras adicionales.
