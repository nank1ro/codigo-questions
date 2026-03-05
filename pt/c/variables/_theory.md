Variáveis são contêineres para armazenar valores de dados.
Cada variável em C é um objeto e, assim como outras linguagens de programação, C possui comandos para declarar uma variável.
Para criar uma variável, precisamos dar a ela um **tipo** e um **nome**, lembrando que não deve conter espaços.
Uma variável é criada no momento em que você atribui um valor a ela pela primeira vez.
Um exemplo de criação de uma variável chamada `x` é:
```c
int x = 1;
```
Dessa forma, atribuímos o valor `1` à variável do tipo _inteiro_ chamada `x`.
Se imprimirmos a variável `x`, obtemos o número `1`:
```c
>>> printf("%i\n", x);
1
```

---

As variáveis são chamadas assim porque o valor que armazenam pode mudar.
Podemos atualizar `x` usando `=` e atribuindo um novo valor.
```c
>>> x = 1;
>>> printf("%i\n", x);
1
>>> x = 2;
>>> printf("%i\n", x);
2
```

---

Também podemos atribuir a variáveis os valores de outras variáveis. Aqui, podemos atribuir à variável `y` o valor de `x`
```c
>>> int x = 5;
>>> int y = x;
>>> printf("%i\n", y);
5
```

---

Quando atualizamos uma variável, ela esquece seu valor anterior.
Aqui podemos exibir a variável `x` duas vezes e ver como seu valor é atualizado.
```c
>>> int x = 5;
>>> printf("%i\n", x);
5
>>> x = 10;
>>> printf("%i\n", x);
10
```

---

Em C, variáveis do tipo string podem ser declaradas apenas usando aspas duplas:
```c
char x[] = "May";
```

---

Se quisermos um nome de variável com várias palavras, usamos **snake case**.
Isso significa usar `_` para conectar as palavras adicionais.
