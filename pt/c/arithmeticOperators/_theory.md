Operadores são usados para realizar operações em variáveis e valores.
Vamos começar com os operadores aritméticos, em particular com o operador de **adição** `+`.
Ele é usado para somar dois números, assim:
```
>>> 5 + 3
8
```

---

Vamos continuar com o operador de **subtração** `-`.
Ele é usado para subtrair um número de outro, assim:
```
>>> 5 - 3
2
```

---

Vamos ver o operador de **multiplicação** `*`.
Ele é usado para multiplicar dois números, assim:
```
>>> 5 * 3
15
```

---

Vamos ver o operador de **divisão** `/`.
Ele é usado para dividir dois números, assim:
```c
>>> 10 / 5
2
```

---

Vamos ver o operador de **módulo** `%`.
Ele é usado para encontrar o resto de uma divisão entre dois números, assim:
```
>>> 5 % 2
1
```
Isso resulta em 1 porque 5 dividido por 2 tem um quociente de 2 e um resto de 1
```
>>> 9 % 3
0
```
Este outro resulta em 0 porque 9 dividido por 3 tem um quociente de 3 e deixa um resto de 0

---

C não possui um operador de **exponenciação**, então precisamos usar a função `pow()` incluída na biblioteca `math.h`.
A exponenciação corresponde à multiplicação repetida da base: ou seja, **b** com expoente *n* é o produto da multiplicação de *n* bases:
![exponentiation](https://bit.ly/3zcz6Lt)
```
>>> pow(5, 2);
25
```

---

Vamos ver a **divisão inteira** usando a função `floor()`.
Esta função retorna a parte inteira do quociente, por exemplo:
```
>>> 5.0 / 2
2.5
>>> floor(2.5)
2.0
```
Também chamada de divisão inteira. O valor resultante é um número inteiro, embora o *tipo* do resultado não seja necessariamente int.
