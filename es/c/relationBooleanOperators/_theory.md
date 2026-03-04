Comencemos con el operador relacional **igual** `==`.
Devuelve un **booleano**, verdadero `1` o falso `0`, indicando si dos expresiones son iguales, por ejemplo:
```c
>>> 2 == 2
1
>>> 2 == 3
0
```

---

Continuemos con el operador relacional **no igual** `!=`.
Devuelve un **booleano**, verdadero `1` o falso `0`, indicando si dos expresiones **NO** son iguales, por ejemplo:
```c
>>> 2 != 2
0
>>> 2 != 3
1
```
Es exactamente lo opuesto al operador *igual*

---

Continuemos con el operador relacional **mayor que** `>`.
Devuelve un **booleano**, verdadero `1` o falso `0`, indicando si una expresión es mayor que la otra, por ejemplo:
```c
>>> 2 > 2
0
>>> 3 > 2
1
```

---

Continuemos con el operador relacional **menor que** `<`.
Devuelve un **booleano**, verdadero `1` o falso `0`, indicando si una expresión es menor que la otra, por ejemplo:
```c
>>> 2 < 2
0
>>> 2 < 3
1
```

---

Continuemos con el operador relacional **mayor que o igual** `>=`.
Devuelve un **booleano**, verdadero `1` o falso `0`, indicando si una expresión es mayor o igual que la otra, por ejemplo:
```c
>>> 2 >= 2
1
>>> 3 >= 2
1
>>> 3 >= 4
0
```

---

Continuemos con el operador relacional **menor que o igual** `<=`.
Devuelve un **booleano**, verdadero `1` o falso `0`, indicando si una expresión es menor o igual que la otra, por ejemplo:
```c
>>> 2 <= 2
1
>>> 3 <= 2
0
>>> 3 <= 4
1
```

---

Ahora veamos los operadores **booleanos**, comencemos con el primero llamado __y__ `&&`.
Devuelve el primer operando que evalúa a *falso* o el último si todos son *verdaderos*.
```c
>>> 2 == 2 && 2 == 3
0
>>> 1 == 1 && 1 == 1.0
1
```

---

Continuemos con el operador booleano **o** `||`.
Devuelve el primer operando que evalúa a *verdadero* o el último si todos son *falsos*.
```c
>>> 2 == 2 || 2 == 3
1
>>> 1 == 2 || 1 == 3
0
```

---

Terminemos con el operador booleano **no** `!`.
Devuelve un booleano que es el inverso del estado lógico de una expresión.
```c
>>> !true
0
>>> !false
1
>>> !(2 == 2)
0
```
