Vamos começar com o operador relacional **igual** `==`.
Ele retorna um **booleano**, verdadeiro `1` ou falso `0`, indicando se duas expressões são iguais, por exemplo:
```c
>>> 2 == 2
1
>>> 2 == 3
0
```

---

Vamos continuar com o operador relacional **diferente** `!=`.
Ele retorna um **booleano**, verdadeiro `1` ou falso `0`, indicando se duas expressões **NÃO** são iguais, por exemplo:
```c
>>> 2 != 2
0
>>> 2 != 3
1
```
É exatamente o oposto do operador *igual*

---

Vamos continuar com o operador relacional **maior que** `>`.
Ele retorna um **booleano**, verdadeiro `1` ou falso `0`, indicando se uma expressão é maior que a outra, por exemplo:
```c
>>> 2 > 2
0
>>> 3 > 2
1
```

---

Vamos continuar com o operador relacional **menor que** `<`.
Ele retorna um **booleano**, verdadeiro `1` ou falso `0`, indicando se uma expressão é menor que a outra, por exemplo:
```c
>>> 2 < 2
0
>>> 2 < 3
1
```

---

Vamos continuar com o operador relacional **maior ou igual** `>=`.
Ele retorna um **booleano**, verdadeiro `1` ou falso `0`, indicando se uma expressão é maior ou igual a outra, por exemplo:
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
Ele retorna um **booleano**, verdadeiro `1` ou falso `0`, indicando se uma expressão é menor ou igual a outra, por exemplo:
```c
>>> 2 <= 2
1
>>> 3 <= 2
0
>>> 3 <= 4
1
```

---

Agora vamos ver os operadores **booleanos**, começando pelo primeiro chamado __and__ `&&`.
Ele retorna o primeiro operando que é avaliado como *false* ou o último se todos forem *true*.
```c
>>> 2 == 2 && 2 == 3
0
>>> 1 == 1 && 1 == 1.0
1
```

---

Vamos continuar com o operador booleano **or** `||`.
Ele retorna o primeiro operando que é avaliado como *true* ou o último se todos forem *false*.
```c
>>> 2 == 2 || 2 == 3
1
>>> 1 == 2 || 1 == 3
0
```

---

Vamos finalizar com o operador booleano **not** `!`.
Ele retorna um booleano que é o inverso do estado lógico de uma expressão.
```c
>>> !true
0
>>> !false
1
>>> !(2 == 2)
0
```
