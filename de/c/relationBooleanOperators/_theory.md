Lassen Sie uns mit dem **Gleich** `==` Relationsoperator beginnen.
Er gibt einen **boolean** zuruck, true `1` oder false `0`, der angibt, ob zwei Ausdrucke gleich sind, zum Beispiel:
```c
>>> 2 == 2
1
>>> 2 == 3
0
```

---

Fahren wir mit dem **Ungleich** `!=` Relationsoperator fort.
Er gibt einen **boolean** zuruck, true `1` oder false `0`, der angibt, ob zwei Ausdrucke **NICHT** gleich sind, zum Beispiel:
```c
>>> 2 != 2
0
>>> 2 != 3
1
```
Er ist genau das Gegenteil des *Gleich*-Operators

---

Fahren wir mit dem **Groer als** `>` Relationsoperator fort.
Er gibt einen **boolean** zuruck, true `1` oder false `0`, der angibt, ob ein Ausdruck groer als der andere ist, zum Beispiel:
```c
>>> 2 > 2
0
>>> 3 > 2
1
```

---

Fahren wir mit dem **Kleiner als** `<` Relationsoperator fort.
Er gibt einen **boolean** zuruck, true `1` oder false `0`, der angibt, ob ein Ausdruck kleiner als der andere ist, zum Beispiel:
```c
>>> 2 < 2
0
>>> 2 < 3
1
```

---

Fahren wir mit dem **Groer oder gleich** `>=` Relationsoperator fort.
Er gibt einen **boolean** zuruck, true `1` oder false `0`, der angibt, ob ein Ausdruck groer oder gleich dem anderen ist, zum Beispiel:
```c
>>> 2 >= 2
1
>>> 3 >= 2
1
>>> 3 >= 4
0
```

---

Fahren wir mit dem **Kleiner oder gleich** `<=` Relationsoperator fort.
Er gibt einen **boolean** zuruck, true `1` oder false `0`, der angibt, ob ein Ausdruck kleiner oder gleich dem anderen ist, zum Beispiel:
```c
>>> 2 <= 2
1
>>> 3 <= 2
0
>>> 3 <= 4
1
```

---

Lassen Sie uns nun die **boolean** Operatoren sehen, beginnen wir mit dem ersten namens __und__ `&&`.
Er gibt den ersten Operanden zuruck, der zu *false* auswertet, oder den letzten, wenn alle *true* sind.
```c
>>> 2 == 2 && 2 == 3
0
>>> 1 == 1 && 1 == 1.0
1
```

---

Fahren wir mit dem **oder** `||` Boolean-Operator fort.
Er gibt den ersten Operanden zuruck, der zu *true* auswertet, oder den letzten, wenn alle *false* sind.
```c
>>> 2 == 2 || 2 == 3
1
>>> 1 == 2 || 1 == 3
0
```

---

Lassen Sie uns mit dem **nicht** `!` Boolean-Operator beenden.
Er gibt einen Boolean zuruck, der das Gegenteil des logischen Zustands eines Ausdrucks ist.
```c
>>> !true
0
>>> !false
1
>>> !(2 == 2)
0
```
