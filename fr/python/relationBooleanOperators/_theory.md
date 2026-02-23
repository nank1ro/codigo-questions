Commençons par l'opérateur relationnel d'**égalité** `==`.
Il renvoie un **booléen** (`True` ou `False`) indiquant si deux expressions sont égales, par exemple :
```python
>>> 2 == 2
True
>>> 2 == 3
False
```

---

Continuons avec l'opérateur relationnel de **différence** `!=`.
Il renvoie un **booléen** (`True` ou `False`) indiquant si deux expressions ne sont **PAS** égales, par exemple :
```python
>>> 2 != 2
False
>>> 2 != 3
True
```
C'est exactement l'opposé de l'opérateur d'*égalité*

---

Continuons avec l'opérateur relationnel **supérieur à** `>`.
Il renvoie un **booléen** (`True` ou `False`) indiquant si une expression est supérieure à l'autre, par exemple :
```python
>>> 2 > 2
False
>>> 3 > 2
True
```

---

Continuons avec l'opérateur relationnel **inférieur à** `<`.
Il renvoie un **booléen** (`True` ou `False`) indiquant si une expression est inférieure à l'autre, par exemple :
```python
>>> 2 < 2
False
>>> 2 < 3
True
```

---

Continuons avec l'opérateur relationnel **supérieur ou égal** `>=`.
Il renvoie un **booléen** (`True` ou `False`) indiquant si une expression est supérieure ou égale à l'autre, par exemple :
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
Il renvoie un **booléen** (`True` ou `False`) indiquant si une expression est inférieure ou égale à l'autre, par exemple :
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
Il renvoie le premier opérande qui évalue à *False* ou le dernier si tous sont *True*.
```python
>>> 2 == 2 and 2 == 3
False
>>> 1 == 1 and 1 == 1.0
True
```

---

Continuons avec l'opérateur booléen **or**.
Il renvoie le premier opérande qui évalue à *True* ou le dernier si tous sont *False*.
```python
>>> 2 == 2 or 2 == 3
True
>>> 1 == 2 or 1 == 3
False
```

---

Terminons avec l'opérateur booléen **not**.
Il renvoie un booléen qui est l'inverse de l'état logique d'une expression.
```python
>>> not True
False
>>> not False
True
>>> not 2 == 2
False
```
