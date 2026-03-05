Beginnen wir mit dem **Gleichheits**-Operator `==`.
Er gibt einen **booleschen** Wert zurück, wahr `1` oder falsch `0`, der angibt, ob zwei Ausdrücke gleich sind. Zum Beispiel:
```c
>>> 2 == 2
1
>>> 2 == 3
0
```

---

Fahren wir mit dem **Ungleicheits**-Operator `!=` fort.
Er gibt einen **booleschen** Wert zurück, wahr `1` oder falsch `0`, der angibt, ob zwei Ausdrücke **NICHT** gleich sind. Zum Beispiel:
```c
>>> 2 != 2
0
>>> 2 != 3
1
```
Es ist genau das Gegenteil des *Gleichheits*-Operators

---

Fahren wir mit dem **Größer-als**-Operator `>` fort.
Er gibt einen **booleschen** Wert zurück, wahr `1` oder falsch `0`, der angibt, ob ein Ausdruck größer als der andere ist. Zum Beispiel:
```c
>>> 2 > 2
0
>>> 3 > 2
1
```

---

Fahren wir mit dem **Kleiner-als**-Operator `<` fort.
Er gibt einen **booleschen** Wert zurück, wahr `1` oder falsch `0`, der angibt, ob ein Ausdruck kleiner als der andere ist. Zum Beispiel:
```c
>>> 2 < 2
0
>>> 2 < 3
1
```

---

Fahren wir mit dem **Größer-als-oder-gleich**-Operator `>=` fort.
Er gibt einen **booleschen** Wert zurück, wahr `1` oder falsch `0`, der angibt, ob ein Ausdruck größer als oder gleich dem anderen ist. Zum Beispiel:
```c
>>> 2 >= 2
1
>>> 3 >= 2
1
>>> 3 >= 4
0
```

---

Fahren wir mit dem **Kleiner-als-oder-gleich**-Operator `<=` fort.
Er gibt einen **booleschen** Wert zurück, wahr `1` oder falsch `0`, der angibt, ob ein Ausdruck kleiner als oder gleich dem anderen ist. Zum Beispiel:
```c
>>> 2 <= 2
1
>>> 3 <= 2
0
>>> 3 <= 4
1
```

---

Jetzt schauen wir uns die **booleschen** Operatoren an. Beginnen wir mit dem ersten, dem **und**-Operator `&&`.
Er gibt den ersten Operanden zurück, der zu *falsch* evaluiert wird, oder den letzten, wenn alle *wahr* sind.
```c
>>> 2 == 2 && 2 == 3
0
>>> 1 == 1 && 1 == 1.0
1
```

---

Fahren wir mit dem **oder**-Operator `||` fort.
Er gibt den ersten Operanden zurück, der zu *wahr* evaluiert wird, oder den letzten, wenn alle *falsch* sind.
```c
>>> 2 == 2 || 2 == 3
1
>>> 1 == 2 || 1 == 3
0
```

---

Beenden wir mit dem **nicht**-Operator `!`.
Er gibt einen booleschen Wert zurück, der das Gegenteil des logischen Zustands eines Ausdrucks ist.
```c
>>> !true
0
>>> !false
1
>>> !(2 == 2)
0
```
