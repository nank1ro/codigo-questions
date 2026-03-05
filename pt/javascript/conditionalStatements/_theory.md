A tomada de decisao e necessaria quando queremos executar um codigo apenas se uma determinada condicao for satisfeita.
Vamos supor que queremos brincar ao ar livre apenas se o clima estiver bom.
Na programacao, podemos salvar uma variavel booleana `niceWeather` e executar a acao de brincar ao ar livre `if` (se) essa variavel for `true`, assim:
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```

---

Vamos continuar com o exemplo anterior.
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```
Vimos que a instrucao `if` executa o bloco de codigo apenas se a condicao for `true`.
Outra coisa importante a considerar sao as **chaves** `{}` que indicam um bloco de codigo.

---

Acabamos de ver como executar um bloco de codigo se uma condicao ocorrer, agora vamos ver como executar outro bloco de codigo se a primeira condicao falhar.
Vamos brincar ao ar livre se o clima estiver bom; caso contrario, ficamos em casa.
Em JavaScript podemos usar a instrucao `else`, assim:
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
} else {
    // stay home
}
```

---

Vamos supor que temos outra condicao para verificar, como neste exemplo:
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
e a saida deste codigo e `the number is 3`.
Primeiro, vamos verificar se o numero e igual a 2, isso e falso.
Entao vamos para a segunda instrucao e verificamos se `num` e igual a 3, sendo verdadeiro executamos o bloco de codigo seguinte imprimindo `the number is 3`

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

Tambem podemos aninhar uma instrucao condicional (`if`, `else if` ou `else`) dentro de outra instrucao condicional, para criar uma estrutura mais complexa.
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
e a saida deste codigo e `the number is 4`.

---

O operador condicional ternario e um operador especial com tres partes, que assume a forma `pergunta ? resposta1 : resposta2`.
E um atalho para avaliar uma de duas expressoes com base em se a `pergunta` e verdadeira ou falsa.
Se `pergunta` for verdadeira, ele avalia `resposta1` e retorna seu valor; caso contrario, ele avalia `resposta2` e retorna seu valor.
```javascript
let a = 10, b = 20, c = 0;
if (a < b) {
    c = a;
} else {
    c = b;
}
console.log(c);
// prints 10
```
A forma abreviada do codigo acima e:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// prints 10
```
`c` recebe o valor de `a`, porque a condicao `a < b` era verdadeira

---

O _operador de coalescencia nula_ `a ?? b` desempacota um opcional `a` se ele contiver um valor, ou retorna um valor padrao `b` se `a` for `nil`.
A expressao `a` e sempre de um tipo opcional.
A expressao `b` deve corresponder ao tipo que esta armazenado dentro de a.
O operador de coalescencia nula e uma forma abreviada do codigo abaixo:
```javascript
a != nil ? a! : b;
```
