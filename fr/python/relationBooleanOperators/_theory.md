Commençons par l'opérateur relationnel **égal** `==`.
Il retourne une valeur **booléenne** (`True` ou `False`) indiquant si deux expressions sont égales, par exemple :
```python
>>> 2 == 2
True
>>> 2 == 3
False
```

---

Continuons avec l'opérateur relationnel **non égal** `!=`.
Il retourne une valeur **booléenne** (`True` ou `False`) indiquant si deux expressions ne sont **pas** égales, par exemple :
```python
>>> 2 != 2
False
>>> 2 != 3
True
```
It is exactly the opposite of the *equal* operator

---

Continuons avec l'opérateur relationnel **supérieur à** `>`.
Il retourne une valeur **booléenne** (`True` ou `False`) indiquant si une expression est supérieure à l'autre, for example:
```python
>>> 2 > 2
False
>>> 3 > 2
True
```

---

Continuons avec l'opérateur relationnel **inférieur à** `<`.
Il retourne une valeur **booléenne** (`True` ou `False`) indiquant si une expression est inférieure à l'autre, for example:
```python
>>> 2 < 2
False
>>> 2 < 3
True
```

---

Continuons avec l'opérateur relationnel **supérieur ou égal** `>=`.
Il retourne un **Booléen** (`True` ou `False`) indiquant si une expression est supérieure ou égale à l'autre, par exemple :
```python
>>> 2 >= 2
True
>>> 3 >= 2
True
>>> 3 >= 4
False
```

---

Continuons avec l'opérateur relationnel **inférieur ou égal** `<=`.
Il retourne un **Booléen** (`True` ou `False`) indiquant si une expression est inférieure ou égale à l'autre, par exemple :
```python
>>> 2 <= 2
True
>>> 3 <= 2
False
>>> 3 <= 4
True
```

---

Voyons maintenant les opérateurs **booléens**, commençons par le premier appelé `and`.
Il retourne le premier opérande qui évalue à *False* ou le dernier s'ils sont tous *True*.
```python
>>> 2 == 2 and 2 == 3
False
>>> 1 == 1 and 1 == 1.0
True
```

---

Continuons avec l'opérateur booléen **or**.
Il retourne le premier opérande qui évalue à *True* ou le dernier s'ils sont tous *False*.
```python
>>> 2 == 2 or 2 == 3
True
>>> 1 == 2 or 1 == 3
False
```

---

Finissons avec l'opérateur booléen **not**.
Il retourne une valeur booléenne qui est l'inverse de l'état logique d'une expression.
```python
>>> not True
False
>>> not False
True
>>> not 2 == 2
False
```
