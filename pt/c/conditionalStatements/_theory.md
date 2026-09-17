A tomada de decisão é necessária quando queremos executar código apenas se uma determinada condição for satisfeita.
Vamos supor que queremos brincar ao ar livre apenas se o tempo estiver bom.
Na programação, podemos salvar uma variável booleana `nice_weather` e executar a ação de brincar ao ar livre `if` se essa variável for `true`, assim:
```c
bool nice_weather = true;
if (nice_weather) {
    // brincar ao ar livre
}
```

---

Vamos continuar com o exemplo anterior.
```c
bool nice_weather = true;
if (nice_weather) {
    // brincar ao ar livre
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
    // brincar ao ar livre
} else {
    // ficar em casa
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

---

Hora de colocar em prática a sintaxe da instrução `if`: a palavra-chave, uma condição entre parênteses e um bloco de código entre chaves.
```c
if (condition) {
    // executa quando a condição é verdadeira
}
```

---

Os literais booleanos em C são `true` e `false`: em minúsculas, sem aspas, e definidos por `<stdbool.h>` em vez de fazerem parte da linguagem. Escrever `True` não compila como condição — apenas a forma em minúsculas funciona, e quando o valor é `true` o bloco é executado.

---

C não tem um teste booleano separado: uma condição é verdadeira sempre que seu valor for diferente de zero. O `false` de `<stdbool.h>` é simplesmente `0`, então um bloco protegido por ele nunca é executado.

---

Uma instrução `if` em C é composta por três partes: a palavra-chave `if`, uma condição entre parênteses e um bloco entre chaves. Os parênteses são obrigatórios — é assim que o compilador sabe onde a condição termina.

---

Toda instrução condicional começa com uma palavra-chave que avisa o compilador de que uma condição precisa ser verificada antes de decidir o que executar em seguida.

---

Uma condição literal `true` é sempre verdadeira, então o bloco é executado e o `printf` dentro dele roda exatamente como está escrito.

---

Uma condição literal `false` nunca é verdadeira, então o bloco é completamente ignorado e nada dentro dele é executado.

---

Condições são os valores que uma instrução `if` verifica: quando uma condição é `true` o bloco é executado, quando é `false` ele é ignorado.

---

A chave de abertura pode ficar na mesma linha da condição ou na linha seguinte. C ignora a quebra de linha, então os dois estilos compilam exatamente para o mesmo programa.

---

Os parênteses ao redor de uma condição fazem parte da sintaxe do `if` em C, não são um agrupamento opcional: `if true { ... }` não compila.

---

Um `"false"` entre aspas é uma string, não um booleano — e uma string usada como condição é um endereço não nulo, o que conta como verdadeiro. Somente o `false` sem aspas impede que o bloco seja executado.

---

O espaçamento entre as partes de uma linha `if` é livre em C: `if(true){` e `if (true) {` são a mesma instrução para o compilador, então só a ordem das partes importa.

---

Um bloco de código não se limita a uma única instrução. Toda instrução entre as chaves é executada, uma após a outra, na ordem em que foi escrita.

---

Uma variável booleana pode ser usada diretamente como condição, sem necessidade de comparação. Como `online` já guarda `true`, escrever apenas `if (online)` já é suficiente para executar o bloco.

---

Uma variável `bool` funciona como condição porque o `if` olha apenas para o valor armazenado nela naquele momento. Com `false` em `online`, `if (online)` se comporta exatamente como `if (false)`.

---

Apenas o código entre as chaves de uma instrução `if` é condicional. Qualquer coisa escrita depois da chave de fechamento é executada incondicionalmente, não importa qual era a condição.

---

Não há um limite fixo para quantas instruções um bloco de código pode conter — uma linha ou cem, todas são executadas juntas quando a condição é `true`.

---

Ler uma variável booleana como condição funciona exatamente como um literal: como `online` guarda `true`, o bloco é executado e o `printf` dentro dele roda.

---

Quando `online` guarda `false`, a condição é falsa, então o bloco é completamente ignorado e nada dentro daquelas chaves é impresso.
