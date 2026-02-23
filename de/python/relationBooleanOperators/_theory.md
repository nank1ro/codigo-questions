Lassen Sie uns mit dem **Gleich** `==` Relationsoperator beginnen.
Er gibt einen **Boolean** (`True` oder `False`) zuruck, der angibt, ob zwei Ausdrucke gleich sind, zum Beispiel:
```python
>>> 2 == 2
True
>>> 2 == 3
False
```

---

Fahren wir mit dem **Ungleich** `!=` Relationsoperator fort.
Er gibt einen **Boolean** (`True` oder `False`) zuruck, der angibt, ob zwei Ausdrucke **NICHT** gleich sind, zum Beispiel:
```python
>>> 2 != 2
False
>>> 2 != 3
True
```
Er ist genau das Gegenteil des *Gleich*-Operators

---

Fahren wir mit dem **Groer als** `>` Relationsoperator fort.
Er gibt einen **Boolean** (`True` oder `False`) zuruck, der angibt, ob ein Ausdruck groer als der andere ist, zum Beispiel:
```python
>>> 2 > 2
False
>>> 3 > 2
True
```

---

Fahren wir mit dem **Kleiner als** `<` Relationsoperator fort.
Er gibt einen **Boolean** (`True` oder `False`) zuruck, der angibt, ob ein Ausdruck kleiner als der andere ist, zum Beispiel:
```python
>>> 2 < 2
False
>>> 2 < 3
True
```

---

Fahren wir mit dem **Groer oder gleich** `>=` Relationsoperator fort.
Er gibt einen **Boolean** (`True` oder `False`) zuruck, der angibt, ob ein Ausdruck groer oder gleich dem anderen ist, zum Beispiel:
```python
>>> 2 >= 2
True
>>> 3 >= 2
True
>>> 3 >= 4
False
```

---

Fahren wir mit dem **Kleiner oder gleich** `<=` Relationsoperator fort.
Er gibt einen **Boolean** (`True` oder `False`) zuruck, der angibt, ob ein Ausdruck kleiner oder gleich dem anderen ist, zum Beispiel:
```python
>>> 2 <= 2
True
>>> 3 <= 2
False
>>> 3 <= 4
True
```

---

Lassen Sie uns nun die **Boolean** Operatoren sehen, beginnen wir mit dem ersten namens `and`.
Er gibt den ersten Operanden zuruck, der zu *False* auswertet, oder den letzten, wenn alle *True* sind.
```python
>>> 2 == 2 and 2 == 3
False
>>> 1 == 1 and 1 == 1.0
True
```

---

Fahren wir mit dem **oder** Boolean-Operator fort.
Er gibt den ersten Operanden zuruck, der zu *True* auswertet, oder den letzten, wenn alle *False* sind.
```python
>>> 2 == 2 or 2 == 3
True
>>> 1 == 2 or 1 == 3
False
```

---

Lassen Sie uns mit dem **nicht** Boolean-Operator beenden.
Er gibt einen Boolean zuruck, der das Gegenteil des logischen Zustands eines Ausdrucks ist.
```python
>>> not True
False
>>> not False
True
>>> not 2 == 2
False
```
