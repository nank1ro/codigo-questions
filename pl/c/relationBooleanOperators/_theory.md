Zacznijmy od relacyjnego operatora **równości** `==`.
Zwraca **wartość logiczną** (boolean): prawda `1`  lub fałsz `0`, określając czy dwa wyrażenia są równe, na przykład:
```c
>>> 2 == 2
1
>>> 2 == 3
0
```

---

Kontynuujmy z relacyjnym operatorem **nierówności** `!=`.
Zwraca **wartość logiczną** (boolean): prawda `1`  lub fałsz `0`, określając czy dwa wyrażenia **NIE** są równe, na przykład:
```c
>>> 2 != 2
0
>>> 2 != 3
1
```
Jest dokładnie przeciwieństwem operatora *równości*

---

Kontynuujmy z relacyjnym operatorem **większości** `>`.
Zwraca **wartość logiczną** (boolean): prawda `1`  lub fałsz `0`, określając czy jedno wyrażenie jest większe od drugiego, na przykład:
```c
>>> 2 > 2
0
>>> 3 > 2
1
```

---

Kontynuujmy z relacyjnym operatorem **mniejszości** `<`.
Zwraca **wartość logiczną** (boolean): prawda `1`  lub fałsz `0`, określając czy jedno wyrażenie jest mniejsze od drugiego, na przykład:
```c
>>> 2 < 2
0
>>> 2 < 3
1
```

---

Kontynuujmy z relacyjnym operatorem **większości lub równości** `>=`.
Zwraca **wartość logiczną** (boolean): prawda `1`  lub fałsz `0`, określając czy jedno wyrażenie jest większe lub równe drugiemu, na przykład:
```c
>>> 2 >= 2
1
>>> 3 >= 2
1
>>> 3 >= 4
0
```

---

Kontynuujmy z relacyjnym operatorem **mniejszości lub równości** `<=`.
Zwraca **wartość logiczną** (boolean): prawda `1`  lub fałsz `0`, określając czy jedno wyrażenie jest mniejsze lub równe drugiemu, na przykład:
```c
>>> 2 <= 2
1
>>> 3 <= 2
0
>>> 3 <= 4
1
```

---

Teraz poznajmy operatory **logiczne** (boolean), zacznijmy od pierwszego zwanego __and__ `&&`.
Zwraca pierwszy operand, który ma wartość *fałsz*, lub ostatni, jeśli wszystkie mają wartość *prawda*.
```c
>>> 2 == 2 && 2 == 3
0
>>> 1 == 1 && 1 == 1.0
1
```

---

Kontynuujmy z logicznym operatorem **or** `||`.
Zwraca pierwszy operand, który ma wartość *prawda*, lub ostatni, jeśli wszystkie mają wartość *fałsz*.
```c
>>> 2 == 2 || 2 == 3
1
>>> 1 == 2 || 1 == 3
0
```

---

Zakończmy z logicznym operatorem **not** `!`.
Zwraca wartość logiczną będącą odwrotnością stanu logicznego wyrażenia.
```c
>>> !true
0
>>> !false
1
>>> !(2 == 2)
0
```
