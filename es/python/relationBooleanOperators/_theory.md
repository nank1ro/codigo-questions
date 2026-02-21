Empecemos con el operador relacional **igual** `==`.
Devuelve un **Booleano** (`True` o `False`) indicando si dos expresiones son iguales, por ejemplo:
```python
>>> 2 == 2
True
>>> 2 == 3
False
```

---

Continuemos con el operador relacional **no igual** `!=`.
Devuelve un **Booleano** (`True` o `False`) indicando si dos expresiones **NO** son iguales, por ejemplo:
```python
>>> 2 != 2
False
>>> 2 != 3
True
```
Es exactamente lo opuesto al operador *igual*

---

Continuemos con el operador relacional **mayor que** `>`.
Devuelve un **Booleano** (`True` o `False`) indicando si una expresin es mayor que la otra, por ejemplo:
```python
>>> 2 > 2
False
>>> 3 > 2
True
```

---

Continuemos con el operador relacional **menor que** `<`.
Devuelve un **Booleano** (`True` o `False`) indicando si una expresin es menor que la otra, por ejemplo:
```python
>>> 2 < 2
False
>>> 2 < 3
True
```

---

Continuemos con el operador relacional **mayor o igual que** `>=`.
Devuelve un **Booleano** (`True` o `False`) indicando si una expresin es mayor o igual que la otra, por ejemplo:
```python
>>> 2 >= 2
True
>>> 3 >= 2
True
>>> 3 >= 4
False
```

---

Continuemos con el operador relacional **menor o igual que** `<=`.
Devuelve un **Booleano** (`True` o `False`) indicando si una expresin es menor o igual que la otra, por ejemplo:
```python
>>> 2 <= 2
True
>>> 3 <= 2
False
>>> 3 <= 4
True
```

---

Ahora veamos los operadores **Booleanos**, empecemos con el primero llamado `and`.
Devuelve el primer operando que se evala como *False* o el ltimo si todos son *True*.
```python
>>> 2 == 2 and 2 == 3
False
>>> 1 == 1 and 1 == 1.0
True
```

---

Continuemos con el operador booleano **or**.
Devuelve el primer operando que se evala como *True* o el ltimo si todos son *False*.
```python
>>> 2 == 2 or 2 == 3
True
>>> 1 == 2 or 1 == 3
False
```

---

Terminemos con el operador booleano **not**.
Devuelve un booleano que es lo opuesto del estado lgico de una expresin.
```python
>>> not True
False
>>> not False
True
>>> not 2 == 2
False
```
