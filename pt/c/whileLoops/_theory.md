Frequentemente na programacao, precisamos repetir um bloco de codigo, por exemplo:
```c
printf("2 seconds\n");
printf("3 seconds\n");
printf("4 seconds\n");
printf("5 seconds\n");
```
Isso produz a seguinte saida:
```c
2 seconds
3 seconds
4 seconds
5 seconds
```
Obviamente, para instrucoes longas gastariamos muito tempo escrevendo o codigo, mas felizmente, podemos usar lacos de repeticao.
Vamos aprender o laco `while`, obtendo a mesma saida acima.
```c
int count = 2;
while (count <= 5) {
    printf("%d seconds\n", count);
    count++;
}
```
Entao criamos uma variavel `count` atribuindo `2`, o valor inicial.
Depois usamos a instrucao `while` que executara o bloco de codigo enquanto a condicao `count <= 5` for `true`.
Dentro do bloco de codigo, **NAO** devemos esquecer de adicionar a linha `count++;`.
Ela incrementa o valor de `count`, caso contrario, nosso laco sera infinito

---

Para controlar quantas vezes um laco `while` se repete, comecamos com uma variavel definida com um numero.
Chamamos essa variavel de variavel contadora

---

Depois, usamos uma comparacao na condicao para comparar a variavel `counter` com um numero.

---

Dentro do bloco de codigo, para parar o laco `while`, incrementamos a variavel `counter`.

---

A ordem em que voce escreve o codigo afeta a saida.
