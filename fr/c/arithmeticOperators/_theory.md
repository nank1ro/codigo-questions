Les opérateurs sont utilisés pour effectuer des opérations sur des variables et des valeurs.
Commençons par les opérateurs arithmétiques, en particulier par l'opérateur d'**addition** `+`.
Il est utilisé pour additionner deux nombres, par exemple :
```
>>> 5 + 3
8
```

---

Continuons avec l'opérateur de **soustraction** `-`.
Il est utilisé pour soustraire un nombre d'un autre, par exemple :
```
>>> 5 - 3
2
```

---

Voyons l'opérateur de **multiplication** `*`.
Il est utilisé pour multiplier deux nombres ensemble, par exemple :
```
>>> 5 * 3
15
```

---

Voyons l'opérateur de **division** `/`.
Il est utilisé pour diviser deux nombres ensemble, par exemple :
```c
>>> 10 / 5
2
```

---

Voyons l'opérateur de **modulo** `%`.
Il est utilisé pour trouver le reste après une division entre deux nombres, par exemple :
```
>>> 5 % 2
1
```
Cela évalue à 1 car 5 divisé par 2 a un quotient de 2 et un reste de 1
```
>>> 9 % 3
0
```
Cela évalue à 0 car 9 divisé par 3 a un quotient de 3 et laisse un reste de 0

---

Le C n'a pas d'opérateur d'**exponentiation**, nous devons donc utiliser la fonction `pow()` incluse dans la bibliothèque `math.h`.
L'exponentiation correspond à une multiplication répétée de la base : c'est-à-dire que **b** avec l'exposant *n* est le produit de la multiplication de *n* bases :
![exponentiation](https://bit.ly/3zcz6Lt)
```
>>> pow(5, 2);
25
```

---

Voyons la **division entière** en utilisant la fonction `floor()`.
Cette fonction renvoie la partie entière du quotient, par exemple :
```
>>> 5.0 / 2
2.5
>>> floor(2.5)
2.0
```
Aussi appelée division entière. La valeur résultante est un entier, bien que le *type* du résultat ne soit pas nécessairement int.
