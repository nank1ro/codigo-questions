A tomada de decisão é necessária quando queremos executar código apenas se uma determinada condição for satisfeita.
Vamos supor que queremos brincar ao ar livre apenas se o tempo estiver bom.
Na programação, podemos salvar uma variável booleana `nice_weather` e executar a ação de brincar ao ar livre `if` se essa variável for `true`, assim:
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```

---

Vamos continuar com o exemplo anterior.
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```
Vimos que a instrução `if` executa o bloco de código apenas se a condição for `true`.
Outra coisa importante a considerar são as **chaves** `{}` que indicam um bloco de código.

---

Acabamos de ver como executar um bloco de código se uma condição ocorrer, agora vamos ver como executar outro bloco de código se a primeira condição falhar.
Vamos brincar ao ar livre se o tempo estiver bom; caso contrário, ficamos em casa.
Em C podemos usar a instrução `else`, assim:
```c
bool nice_weather = false;
if (nice_weather) {
    // play outside
} else {
    // stay home
}
```

---

Vamos supor que temos outra condição para verificar, como neste exemplo:
```c
int num = 3;
if (num == 2) {
    printf("the number is 2\n");
} else if (num == 3) {
    printf("the number is 3\n");
} else {
    printf("do something else\n");
}
```
e a saída deste código é `the number is 3`.
Primeiro, vamos verificar se o número é igual a 2, isso é falso.
Então vamos para a segunda instrução e verificamos se `num` é igual a 3, sendo verdadeiro executamos o bloco de código seguinte imprimindo `the number is 3`

---

Podemos adicionar quantas instruções `else if` quisermos, não há limites
```c
int num = 4;
if (num == 2) {
    printf("the number is 2");
} else if (num == 3) {
    printf("the number is 3");
} else if (num == 4) {
    printf("the number is 4");
} else if (num == 5) {
    printf("the number is 5");
} else if (num == 6) {
    printf("the number is 6");
}
```
e a saída deste código é `the number is 4`.

---

Também podemos aninhar uma instrução condicional (`if`, `else if` ou `else`) dentro de outra instrução condicional, para criar uma estrutura mais complexa.
```c
int num = 4;
if (num < 3) {
    printf("the number is lower than 3\n");
} else {
    if (num == 3) {
        printf("the number is 3\n");
  } else if (num == 4) {
        printf("the number is 4\n");
  } else {
        printf("the number is greather than 4\n");
  }
}
```
e a saída deste código é `the number is 4`.
