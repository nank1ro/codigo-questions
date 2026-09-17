Frequentemente na programação, precisamos repetir um bloco de código, por exemplo:
```javascript
console.log("2 seconds");
console.log("3 seconds");
console.log("4 seconds");
console.log("5 seconds");
```
Isso produz a seguinte saída:
```javascript
2 seconds
3 seconds
4 seconds
5 seconds
```
Obviamente, para instruções longas gastaríamos muito tempo escrevendo o código, mas felizmente, podemos usar laços de repetição.
Vamos aprender o laço `while`, obtendo a mesma saída acima.
```javascript
var count = 2;
while (count <= 5) {
    console.log(`${count} seconds`);
    count += 1;
}
```
Então criamos uma variável `count` atribuindo `2`, o valor inicial.
Depois usamos a instrução `while` que executará o bloco de código enquanto a condição `count <= 5` for `true`.
Dentro do bloco de código, **NÃO** devemos esquecer de adicionar a linha `count += 1`.
Ela incrementa o valor de `count`, caso contrário, nosso laço será infinito

---

Para controlar quantas vezes um laço `while` se repete, começamos com uma variável definida como um número.
Chamamos essa variável de variável contadora

---

Depois, usamos uma comparação na condição para comparar a variável `counter` com um número.

---

Dentro do bloco de código, para parar o laço `while`, incrementamos a variável `counter`.

---

A ordem em que você escreve o código afeta a saída.

---

Em JavaScript também temos a variação **do-while** do laço `while`.
Ela executa uma única passagem pelo bloco do laço primeiro, _antes_ de considerar a condição do laço.
Depois continua repetindo o laço até que a condição seja `false`.
