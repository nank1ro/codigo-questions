Les opérateurs sont utilisés pour effectuer des opérations sur les variables et les valeurs.
Commençons par les opérateurs arithmétiques, en particulier par l'opérateur **addition** `+`.
Il est utilisé pour ajouter deux nombres, comme:
```
>>> 5 + 3
8
```

---

Continuons avec l'opérateur **soustraction** `-`.
Il est utilisé pour soustraire un nombre d'un autre, comme:
```
>>> 5 - 3
2
```

---

Voyons l'opérateur **multiplication** `*`.
Il est utilisé pour multiplier deux nombres ensemble, comme:
```
>>> 5 * 3
15
```

---

Voyons l'opérateur **division** `/`.
Il est utilisé pour diviser deux nombres ensemble, comme:
```c
>>> 10 / 5
2
```

---

Voyons l'opérateur **modulo** `%`.
Il est utilisé pour trouver le reste après une division entre deux nombres, comme:
```
>>> 5 % 2
1
```
Cela donne 1 car 5 divisé par 2 a un quotient de 2 et un reste de 1
```
>>> 9 % 3
0
```
Cela donne 0 car 9 divisé par 3 a un quotient de 3 et laisse un reste de 0

---

C n'a pas d'opérateur **exponentiation**, donc nous devons utiliser la fonction `pow()` incluse dans la bibliothèque `math.h`.
L'exponentiation correspond à une multiplication répétée de la base: c'est-à-dire, **b** avec l'exposant *n* est le produit de la multiplication de *n* bases:
![exponentiation](https://bit.ly/3zcz6Lt)
```
>>> pow(5, 2);
25
```

---

Voyons la **division entière** en utilisant la fonction `floor()`.
Cette fonction retourne la partie entière du quotient, par exemple:
```
>>> 5.0 / 2
2.5
>>> floor(2.5)
2.0
```
Aussi appelée division entière. La valeur résultante est un nombre entier, bien que le *type* du résultat ne soit pas nécessairement int.
