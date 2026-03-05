Já aprendemos que para atribuir um valor a uma variável podemos usar o sinal `=`, como:
```c
int a = 5;
```

---

Já temos uma variável inicializada `total`
```c
int total = 5;
```
Digamos que queremos adicionar o número `2` à variável `total`, podemos escrever
```c
total = total + 2;
```
Ok, funciona! Mas existe uma versão mais curta para fazer a mesma coisa:
```c
total += 2;
```
O sinal `+=` é chamado de **atribuição com adição**.
Ele adiciona um valor ao valor da variável e atribui o resultado a essa variável.

---

Assim como na atribuição com adição, temos a **atribuição com subtração** `-=`.
A funcionalidade é a mesma, a única diferença é que ela realiza a subtração.
Portanto, as seguintes expressões são exatamente iguais
```c
num = num - 5;
// é igual a
num -= 5;
```

---

Vamos ver o operador de **atribuição com multiplicação** `*=`.
Ele multiplica a variável por um valor e atribui o resultado a essa variável.
Portanto, as seguintes expressões são exatamente iguais
```c
num = num * 5;
// é igual a
num *= 5;
```

---

Vamos ver o operador de **atribuição com divisão** `/=`.
Ele divide a variável por um valor e atribui o resultado a essa variável.
Portanto, as seguintes expressões são exatamente iguais
```c
num = num / 5;
// é igual a
num /= 5;
```

---

Vamos ver o operador de **atribuição com módulo** `%=`.
Ele calcula o módulo da variável e um valor e atribui o resultado a essa variável.
Portanto, as seguintes expressões são exatamente iguais
```c
num = num % 5;
// é igual a
num %= 5;
```
