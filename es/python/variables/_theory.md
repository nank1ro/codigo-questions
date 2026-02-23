Las variables son contenedores para almacenar valores de datos.
Cada variable en Python es un objeto y, a diferencia de otros lenguajes de programación, Python no tiene un comando para declarar una variable.
Para crear una variable, necesitamos darle un **nombre** teniendo en cuenta que no debe contener espacios.
Una variable se crea en el momento en que le asignas un valor por primera vez.
Un ejemplo de creación de una variable llamada `x` es:
```python
x = 1
```
De esta forma hemos asignado el valor `1` a la variable llamada `x`.
Si imprimimos la variable `x` obtenemos el número `1`:
```python
>>> print(x)
1
```

---

También podemos dar a las variables los valores de otras variables. Aquí, podemos darle a la variable `y` el valor de `x`
```python
>>> x = 5
>>> y = x
>>> print(y)
5
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
