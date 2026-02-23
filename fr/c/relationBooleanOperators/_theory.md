Commençons par l'opérateur relationnel d'**égalité** `==`.
Il renvoie un **booléen**, vrai `1` ou faux `0`, indiquant si deux expressions sont égales, par exemple :
```c
>>> 2 == 2
1
>>> 2 == 3
0
```

---

Continuons avec l'opérateur relationnel de **différence** `!=`.
Il renvoie un **booléen**, vrai `1` ou faux `0`, indiquant si deux expressions ne sont **PAS** égales, par exemple :
```c
>>> 2 != 2
0
>>> 2 != 3
1
```
C'est exactement l'opposé de l'opérateur d'*égalité*

---

Continuons avec l'opérateur relationnel **supérieur à** `>`.
Il renvoie un **booléen**, vrai `1` ou faux `0`, indiquant si une expression est supérieure à l'autre, par exemple :
```c
>>> 2 > 2
0
>>> 3 > 2
1
```

---

Continuons avec l'opérateur relationnel **inférieur à** `<`.
Il renvoie un **booléen**, vrai `1` ou faux `0`, indiquant si une expression est inférieure à l'autre, par exemple :
```c
>>> 2 < 2
0
>>> 2 < 3
1
```

---

Continuons avec l'opérateur relationnel **supérieur ou égal** `>=`.
Il renvoie un **booléen**, vrai `1` ou faux `0`, indiquant si une expression est supérieure ou égale à l'autre, par exemple :
```c
>>> 2 >= 2
1
>>> 3 >= 2
1
>>> 3 >= 4
0
```

---

Continuons avec l'opérateur relationnel **inférieur ou égal** `<=`.
Il renvoie un **booléen**, vrai `1` ou faux `0`, indiquant si une expression est inférieure ou égale à l'autre, par exemple :
```c
>>> 2 <= 2
1
>>> 3 <= 2
0
>>> 3 <= 4
1
```

---

Voyons maintenant les opérateurs **booléens**, commençons par le premier appelé __et__ `&&`.
Il renvoie le premier opérande qui évalue à *faux* ou le dernier si tous sont *vrais*.
```c
>>> 2 == 2 && 2 == 3
0
>>> 1 == 1 && 1 == 1.0
1
```

---

Continuons avec l'opérateur booléen **ou** `||`.
Il renvoie le premier opérande qui évalue à *vrai* ou le dernier si tous sont *faux*.
```c
>>> 2 == 2 || 2 == 3
1
>>> 1 == 2 || 1 == 3
0
```

---

Terminons avec l'opérateur booléen **non** `!`.
Il renvoie un booléen qui est l'inverse de l'état logique d'une expression.
```c
>>> !true
0
>>> !false
1
>>> !(2 == 2)
0
```
