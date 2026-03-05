Variáveis são contêineres para armazenar valores de dados.
Toda variável em JavaScript é um objeto.
Para criar uma variável, precisamos dar a ela um **nome** lembrando que ele não deve conter espaços.
Uma variável é criada no momento em que você atribui um valor a ela pela primeira vez.
Em JavaScript você declara constantes com as palavras-chave `let` ou `const` e variáveis com a palavra-chave `var`.
O valor de uma constante não pode ser alterado depois de definido, enquanto uma variável pode receber um valor diferente no futuro.
Um exemplo de criação de variável chamada `x` é:
```javascript
var x = 1;
```
Dessa forma, atribuímos o valor `1` à variável chamada `x`.
Se imprimirmos a variável `x`, obtemos o número `1`:
```javascript
console.log(x);
// prints 1
```

---

Variáveis são chamadas assim porque o valor que armazenam pode mudar.
Podemos atualizar `x` usando `=` e atribuindo um novo valor.
```javascript
var x = 1;
console.log(x); // prints 1
x = 2;
console.log(x); // prints 2
```

---

Também podemos atribuir a variáveis os valores de outras variáveis.
Aqui, podemos atribuir à variável `y` o valor de `x`
```javascript
var x = 5;
var y = x;
console.log(y); // prints 5
```

---

Quando atualizamos uma variável, ela esquece seu valor anterior.
Aqui podemos exibir a variável `x` duas vezes e ver como seu valor é atualizado.
```javascript
var x = 5;
console.log(x); // prints 5
x = 10;
console.log(x); // prints 10
```

---

Em JavaScript, variáveis de string podem ser declaradas usando tanto aspas duplas quanto aspas simples:
```javascript
let x = "May";
// both are the same string
let y = 'May';
console.log(x === y);
// prints true
```

---

Se quisermos um nome de variável com várias palavras, usamos **camelCase**.
É a prática de escrever frases de forma que cada palavra no meio da frase comece com uma letra maiúscula
