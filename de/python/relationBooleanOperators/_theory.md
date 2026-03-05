Lassen Sie uns mit dem **Gleichheits**-Operator `==` beginnen.
Er gibt einen **Boolean** (`True` oder `False`) zurück, der angibt, ob zwei Ausdrücke gleich sind, zum Beispiel:
```python
>>> 2 == 2
True
>>> 2 == 3
False
```

---

Lassen Sie uns mit dem **Ungleichheits**-Operator `!=` fortfahren.
Er gibt einen **Boolean** (`True` oder `False`) zurück, der angibt, ob zwei Ausdrücke **NICHT** gleich sind, zum Beispiel:
```python
>>> 2 != 2
False
>>> 2 != 3
True
```
Dies ist genau das Gegenteil des *Gleichheits*-Operators

---

Lassen Sie uns mit dem **Größer als**-Operator `>` fortfahren.
Er gibt einen **Boolean** (`True` oder `False`) zurück, der angibt, ob ein Ausdruck größer als der andere ist, zum Beispiel:
```python
>>> 2 > 2
False
>>> 3 > 2
True
```

---

Lassen Sie uns mit dem **Kleiner als**-Operator `<` fortfahren.
Er gibt einen **Boolean** (`True` oder `False`) zurück, der angibt, ob ein Ausdruck kleiner als der andere ist, zum Beispiel:
```python
>>> 2 < 2
False
>>> 2 < 3
True
```

---

Lassen Sie uns mit dem **Größer als oder gleich**-Operator `>=` fortfahren.
Er gibt einen **Boolean** (`True` oder `False`) zurück, der angibt, ob ein Ausdruck größer als oder gleich dem anderen ist, zum Beispiel:
```python
>>> 2 >= 2
True
>>> 3 >= 2
True
>>> 3 >= 4
False
```

---

Lassen Sie uns mit dem **Kleiner als oder gleich**-Operator `<=` fortfahren.
Er gibt einen **Boolean** (`True` oder `False`) zurück, der angibt, ob ein Ausdruck kleiner als oder gleich dem anderen ist, zum Beispiel:
```python
>>> 2 <= 2
True
>>> 3 <= 2
False
>>> 3 <= 4
True
```

---

Jetzt schauen wir uns die **Boolean**-Operatoren an, lassen Sie uns mit dem ersten beginnen, der `and` heißt.
Er gibt den ersten Operanden zurück, der zu *False* ausgewertet wird, oder den letzten, wenn alle *True* sind.
```python
>>> 2 == 2 and 2 == 3
False
>>> 1 == 1 and 1 == 1.0
True
```

---

Lassen Sie uns mit dem **oder**-Boolean-Operator fortfahren.
Er gibt den ersten Operanden zurück, der zu *True* ausgewertet wird, oder den letzten, wenn alle *False* sind.
```python
>>> 2 == 2 or 2 == 3
True
>>> 1 == 2 or 1 == 3
False
```

---

Lassen Sie uns mit dem **nicht**-Boolean-Operator abschließen.
Er gibt einen booleschen Wert zurück, der das Gegenteil des logischen Zustands eines Ausdrucks ist.
```python
>>> not True
False
>>> not False
True
>>> not 2 == 2
False
```
