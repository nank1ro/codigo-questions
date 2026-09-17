A tomada de decisão é necessária quando queremos executar um código apenas se uma determinada condição for satisfeita.
Vamos supor que queremos brincar ao ar livre apenas se o clima estiver bom.
Na programação, podemos salvar uma variável booleana `niceWeather` e executar a ação de brincar ao ar livre `if` (se) essa variável for `true`, assim:
```javascript
var niceWeather = true;
if (niceWeather) {
    // brincar ao ar livre
}
```

---

Vamos continuar com o exemplo anterior.
```javascript
var niceWeather = true;
if (niceWeather) {
    // brincar ao ar livre
}
```
Vimos que a instrução `if` executa o bloco de código apenas se a condição for `true`.
Outra coisa importante a considerar são as **chaves** `{}` que indicam um bloco de código.

---

Acabamos de ver como executar um bloco de código se uma condição ocorrer, agora vamos ver como executar outro bloco de código se a primeira condição falhar.
Vamos brincar ao ar livre se o clima estiver bom; caso contrário, ficamos em casa.
Em JavaScript podemos usar a instrução `else`, assim:
```javascript
var niceWeather = true;
if (niceWeather) {
    // brincar ao ar livre
} else {
    // ficar em casa
}
```

---

Vamos supor que temos outra condição para verificar, como neste exemplo:
```javascript
var num = 3;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else {
    console.log("do something else");
}
```
e a saída deste código é `the number is 3`.
Primeiro, vamos verificar se o número é igual a 2, isso é falso.
Então vamos para a segunda instrução e verificamos se `num` é igual a 3, sendo verdadeiro executamos o bloco de código seguinte imprimindo `the number is 3`

---

Podemos adicionar quantas instrucoes `else if` quisermos, nao ha limites
```javascript
var num = 4;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else if (num == 4) {
    console.log("the number is 4");
} else if (num == 5) {
    console.log("the number is 5");
} else if (num == 6) {
    console.log("the number is 6");
}
```
e a saida deste codigo e `the number is 4`.

---

Também podemos aninhar uma instrução condicional (`if`, `else if` ou `else`) dentro de outra instrução condicional, para criar uma estrutura mais complexa.
```javascript
var num = 4;
if (num < 3) {
    console.log("the number is lower than 3");
} else {
    if (num == 3) {
        console.log("the number is 3");
    } else if (num == 4) {
        console.log("the number is 4");
    } else {
        console.log("the number is greather than 4");
    }
}
```
e a saída deste código é `the number is 4`.

---

O operador condicional ternário é um operador especial com três partes, que assume a forma `pergunta ? resposta1 : resposta2`.
É um atalho para avaliar uma de duas expressões com base em se a `pergunta` é verdadeira ou falsa.
Se `pergunta` for verdadeira, ele avalia `resposta1` e retorna seu valor; caso contrário, ele avalia `resposta2` e retorna seu valor.
```javascript
let a = 10, b = 20, c = 0;
if (a < b) {
    c = a;
} else {
    c = b;
}
console.log(c);
// imprime 10
```
A forma abreviada do código acima é:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// imprime 10
```
`c` recebe o valor de `a`, porque a condição `a < b` era verdadeira

---

O _operador de coalescência nula_ `a ?? b` desempacota um opcional `a` se ele contiver um valor, ou retorna um valor padrão `b` se `a` for `nil`.
A expressão `a` é sempre de um tipo opcional.
A expressão `b` deve corresponder ao tipo que está armazenado dentro de a.
O operador de coalescência nula é uma forma abreviada do código abaixo:
```javascript
a != nil ? a! : b;
```

---

`if` é a palavra-chave que introduz uma instrução condicional em JavaScript. Não existe uma palavra-chave `elif` aqui — uma segunda condição é introduzida com `else if`, escrito como duas palavras separadas.

---

Os literais booleanos do JavaScript são em minúsculas: `true` e `false`, não `True`/`False`, e não as strings `"true"`/`"false"`.

---

Para impedir que um bloco de código seja executado, a condição dentro dos parênteses precisa resultar em `false`.

---

O espaço entre `if` e seus parênteses é puramente estético: `if(true)` e `if (true)` são a mesma instrução para o JavaScript.

---

As chaves são o que agrupa várias instruções em um único bloco. Sem elas, um `if` controla apenas a instrução que vem logo depois dele, então `if (true) console.log("Hello!");` é um JavaScript válido.

---

A condição é avaliada uma única vez, antes de o bloco começar. O JavaScript não a verifica novamente enquanto as instruções entre as chaves estão sendo executadas.

---

Uma condição `false` pula o bloco por completo, e o programa continua na primeira instrução depois da chave de fechamento.

---

Uma condição não precisa ser um booleano: o JavaScript converte o que quer que encontre para um, então `if (1)` executa seu bloco e `if (0)` não. Um literal `true` não precisa de nenhuma conversão.

---

Um bloco de código não se limita a uma única linha — toda instrução dentro das chaves é executada, em ordem, quando a condição é `true`.
```javascript
if (true) {
    console.log("First line");
    console.log("Second line");
}
```
e a saída é `First line` seguido de `Second line`.

---

As instruções dentro de um bloco são executadas uma depois da outra, de cima para baixo, então duas chamadas de `console.log` no mesmo bloco imprimem em duas linhas separadas.

---

Indentar as instruções dentro de um bloco é apenas uma convenção de legibilidade. O JavaScript usa as chaves, nunca a indentação, para decidir o que pertence ao bloco.

---

Instruções como `if`, `else if` e `else`, que executam ou pulam código dependendo se uma condição é `true` ou `false`, são chamadas de **instruções condicionais**.

---

Uma variável booleana, mesmo uma construída a partir de uma negação `!` como `isAfternoon`, pode ser usada diretamente como condição de um `if`, sem necessidade de comparação.

---

A condição de uma instrução `if` sempre vai dentro de parênteses `()`, colocados logo depois da palavra-chave `if` e antes da chave de abertura.

---

Um bloco pode conter qualquer número de instruções, e também pode não conter nenhuma: `if (true) {}` é um JavaScript válido que simplesmente não faz nada.

---

O bloco de código de uma instrução `if` é o conjunto de instruções dentro das chaves `{ }`, a parte que realmente é executada quando a condição é `true`.
