Commençons par l'opérateur relationnel **égal** `==`.
Il retourne un **booléen**, vrai `1` ou faux `0`, indiquant si deux expressions sont égales, par exemple:
```c
>>> 2 == 2
1
>>> 2 == 3
0
```

---

Continuons avec l'opérateur relationnel **non égal** `!=`.
Il retourne un **booléen**, vrai `1` ou faux `0`, indiquant si deux expressions ne sont **PAS** égales, par exemple:
```c
>>> 2 != 2
0
>>> 2 != 3
1
```
C'est exactement l'opposé de l'opérateur *égal*

---

Continuons avec l'opérateur relationnel **plus grand que** `>`.
Il retourne un **booléen**, vrai `1` ou faux `0`, indiquant si une expression est plus grande que l'autre, par exemple:
```c
>>> 2 > 2
0
>>> 3 > 2
1
```

---

Continuons avec l'opérateur relationnel **moins que** `<`.
Il retourne un **booléen**, vrai `1` ou faux `0`, indiquant si une expression est moins que l'autre, par exemple:
```c
>>> 2 < 2
0
>>> 2 < 3
1
```

---

Continuons avec l'opérateur relationnel **plus grand ou égal** `>=`.
Il retourne un **booléen**, vrai `1` ou faux `0`, indiquant si une expression est plus grande ou égale à l'autre, par exemple:
```c
>>> 2 >= 2
1
>>> 3 >= 2
1
>>> 3 >= 4
0
```

---

Continuons avec l'opérateur relationnel **moins que ou égal** `<=`.
Il retourne un **booléen**, vrai `1` ou faux `0`, indiquant si une expression est moins que ou égale à l'autre, par exemple:
```c
>>> 2 <= 2
1
>>> 3 <= 2
0
>>> 3 <= 4
1
```

---

Maintenant, regardons les opérateurs **booléens**, commençons par le premier appelé __et__ `&&`.
Il retourne le premier opérande qui s'évalue à *faux* ou le dernier si tous sont *vrais*.
```c
>>> 2 == 2 && 2 == 3
0
>>> 1 == 1 && 1 == 1.0
1
```

---

Continuons avec l'opérateur booléen **ou** `||`.
Il retourne le premier opérande qui s'évalue à *vrai* ou le dernier si tous sont *faux*.
```c
>>> 2 == 2 || 2 == 3
1
>>> 1 == 2 || 1 == 3
0
```

---

Terminons avec l'opérateur booléen **non** `!`.
Il retourne un booléen qui est l'inverse de l'état logique d'une expression.
```c
>>> !true
0
>>> !false
1
>>> !(2 == 2)
0
```
