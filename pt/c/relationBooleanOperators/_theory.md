Vamos comecar com o operador relacional **igual** `==`.
Ele retorna um **booleano**, verdadeiro `1` ou falso `0`, indicando se duas expressoes sao iguais, por exemplo:
```c
>>> 2 == 2
1
>>> 2 == 3
0
```

---

Vamos continuar com o operador relacional **diferente** `!=`.
Ele retorna um **booleano**, verdadeiro `1` ou falso `0`, indicando se duas expressoes **NAO** sao iguais, por exemplo:
```c
>>> 2 != 2
0
>>> 2 != 3
1
```
E exatamente o oposto do operador *igual*

---

Vamos continuar com o operador relacional **maior que** `>`.
Ele retorna um **booleano**, verdadeiro `1` ou falso `0`, indicando se uma expressao e maior que a outra, por exemplo:
```c
>>> 2 > 2
0
>>> 3 > 2
1
```

---

Vamos continuar com o operador relacional **menor que** `<`.
Ele retorna um **booleano**, verdadeiro `1` ou falso `0`, indicando se uma expressao e menor que a outra, por exemplo:
```c
>>> 2 < 2
0
>>> 2 < 3
1
```

---

Vamos continuar com o operador relacional **maior ou igual** `>=`.
Ele retorna um **booleano**, verdadeiro `1` ou falso `0`, indicando se uma expressao e maior ou igual a outra, por exemplo:
```c
>>> 2 >= 2
1
>>> 3 >= 2
1
>>> 3 >= 4
0
```

---

Vamos continuar com o operador relacional **menor ou igual** `<=`.
Ele retorna um **booleano**, verdadeiro `1` ou falso `0`, indicando se uma expressao e menor ou igual a outra, por exemplo:
```c
>>> 2 <= 2
1
>>> 3 <= 2
0
>>> 3 <= 4
1
```

---

Agora vamos ver os operadores **booleanos**, comecando pelo primeiro chamado __and__ `&&`.
Ele retorna o primeiro operando que e avaliado como *false* ou o ultimo se todos forem *true*.
```c
>>> 2 == 2 && 2 == 3
0
>>> 1 == 1 && 1 == 1.0
1
```

---

Vamos continuar com o operador booleano **or** `||`.
Ele retorna o primeiro operando que e avaliado como *true* ou o ultimo se todos forem *false*.
```c
>>> 2 == 2 || 2 == 3
1
>>> 1 == 2 || 1 == 3
0
```

---

Vamos finalizar com o operador booleano **not** `!`.
Ele retorna um booleano que e o inverso do estado logico de uma expressao.
```c
>>> !true
0
>>> !false
1
>>> !(2 == 2)
0
```
