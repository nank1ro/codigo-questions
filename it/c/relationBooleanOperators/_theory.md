Iniziamo con l'operatore relazionale **uguale** `==`.
Restituisce un valore **booleano**, vero `1` o falso `0`, affermando se due espressioni sono uguali, ad esempio:
```c
>>> 2 == 2
1
>>> 2 == 3
0
```

---

Continuiamo con l'operatore relazionale **non uguale** `!=`.
Restituisce un valore **booleano**, vero `1` o falso `0`, affermando se due espressioni **NON** sono uguali, ad esempio:
```c
>>> 2 != 2
0
>>> 2 != 3
1
```
È esattamente l'opposto dell'operatore *uguale*

---

Continuiamo con l'operatore relazionale **maggiore di** `>`.
Restituisce un valore **booleano**, vero `1` o falso `0` , affermando se un'espressione e' maggiore dell'altra, per esempio:
```c
>>> 2 > 2
0
>>> 3 > 2
1
```

---

Continuiamo con l'operatore relazionale **minore di** `<`.
Restituisce un valore **booleano**, vero `1` o falso `0` ,affermando se un'espressione e' minore dell'altra, per esempio:
```c
>>> 2 < 2
0
>>> 2 < 3
1
```

---

Continuiamo con l'operatore relazionale **maggiore di o uguale a** `>=`.
Restituisce un valore **booleano**, vero `1` o falso `0`, affermando se un'espressione e' maggiore o uguale all'altra, per esempio:
```c
>>> 2 >= 2
1
>>> 3 >= 2
1
>>> 3 >= 4
0
```

---

Continuiamo con l'operatore relazionale **minore di o uguale a** `<=`.
Restituisce un valore **booleano**, vero `1` o falso `0` , affermando se un'espressione e' minore o uguale all'altra, per esempio:
```c
>>> 2 <= 2
1
>>> 3 <= 2
0
>>> 3 <= 4
1
```

---

Ora vediamo gli operatori **booleani**, iniziamo con il primo chiamato __and__ `&&`.
L'operatore restituisce il primo operando che e' uguale a *false* o l'ultimo se tutti sono *true*.
```c
>>> 2 == 2 && 2 == 3
0
>>> 1 == 1 && 1 == 1.0
1
```

---

Continuiamo con l'operatore booleano **or**.
L'operatore restituisce il primo operando che e' uguale a *true* o l'ultimo se tutti sono *false*.
```c
>>> 2 == 2 || 2 == 3
1
>>> 1 == 2 || 1 == 3
0
```

---

Concludiamo con l'operatore booleano **not** `!`.
L'operatore restituisce un valore booleano che e' il contrario dello stato logico di un'espressione.
```c
>>> !true
0
>>> !false
1
>>> !(2 == 2)
0
```
