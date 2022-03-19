Iniziamo con l'operatore relazionale **uguale** `==`.
Restituisce un valore **booleano** (`True` o `False`) affermando se due espressioni sono uguali, ad esempio:
```python
>>> 2 == 2
True
>>> 2 == 3
False
```

---

Continuiamo con l'operatore relazionale **non uguale** `!=`.
Restituisce un valore **booleano** (`True` o `False`) affermando se due espressioni **NON** sono uguali, ad esempio:
```python
>>> 2 != 2
False
>>> 2 != 3
True
```
E' esattamente l'opposto dell'operatore *uguale*

---

Continuiamo con l'operatore relazionale **maggiore di** `>`.
Restituisce un valore **booleano** (`True` o `False`) affermando se un'espressione e' maggiore dell'altra, per esempio:
```python
>>> 2 > 2
False
>>> 3 > 2
True
```

---

Continuiamo con l'operatore relazionale **minore di** `<`.
Restituisce un valore **booleano** (`True` o `False`) affermando se un'espressione e' minore dell'altra, per esempio:
```python
>>> 2 < 2
False
>>> 2 < 3
True
```

---

Continuiamo con l'operatore relazionale **maggiore di o uguale a** `>=`.
Restituisce un valore **booleano** (`True` o `False`) affermando se un'espressione e' maggiore o uguale all'altra, per esempio:
```python
>>> 2 >= 2
True
>>> 3 >= 2
True
>>> 3 >= 4
False
```

---

Continuiamo con l'operatore relazionale **minore di o uguale a** `<=`.
Restituisce un valore **booleano** (`True` o `False`) affermando se un'espressione e' minore o uguale all'altra, per esempio:
```python
>>> 2 <= 2
True
>>> 3 <= 2
False
>>> 3 <= 4
True
```

---

Ora vediamo gli operatori **booleani**, iniziamo con il primo chiamato `and`.
L'operatore restituisce il primo operando che e' uguale a *False* o l'ultimo se tutti sono *True*.
```python
>>> 2 == 2 and 2 == 3
False
>>> 1 == 1 and 1 == 1.0
True
```

---

Continuiamo con l'operatore booleano **or**.
L'operatore restituisce il primo operando che e' uguale a *True* o l'ultimo se tutti sono *False*.
```python
>>> 2 == 2 or 2 == 3
True
>>> 1 == 2 or 1 == 3
False
```

---

Concludiamo con l'operatore booleano **not**.
L'operatore restituisce un valore booleano che e' il contrario dello stato logico di un'espressione.
```python
>>> not True
False
>>> not False
True
>>> not 2 == 2
False
```
