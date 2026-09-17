Frequentemente na programação, precisamos repetir um bloco de código, por exemplo:
```c
printf("2 seconds\n");
printf("3 seconds\n");
printf("4 seconds\n");
printf("5 seconds\n");
```
Isso produz a seguinte saída:
```c
2 seconds
3 seconds
4 seconds
5 seconds
```
Obviamente, para instruções longas gastaríamos muito tempo escrevendo o código, mas felizmente, podemos usar laços de repetição.
Vamos aprender o laço `while`, obtendo a mesma saída acima.
```c
int count = 2;
while (count <= 5) {
    printf("%d seconds\n", count);
    count++;
}
```
Então criamos uma variável `count` atribuindo `2`, o valor inicial.
Depois usamos a instrução `while` que executará o bloco de código enquanto a condição `count <= 5` for `true`.
Dentro do bloco de código, **NÃO** devemos esquecer de adicionar a linha `count++;`.
Ela incrementa o valor de `count`, caso contrário, nosso laço será infinito

---

Para controlar quantas vezes um laço `while` se repete, começamos com uma variável definida com um número.
Chamamos essa variável de variável contadora

---

Depois, usamos uma comparacao na condicao para comparar a variavel `counter` com um numero.

---

Dentro do bloco de codigo, para parar o laco `while`, incrementamos a variavel `counter`.

---

A ordem em que voce escreve o codigo afeta a saida.
