Sabemos como repetir código usando um loop `while`.
Como este programa que repete instruções para exibir `hello`
```javascript
var counter = 0;

while (counter < 5) {
    console.log("hello");
    counter++;
}
```
Mas podemos fazer o mesmo com loops `for`:
```javascript
for (let i = 0; i < 5; i++) {
    console.log("hello");
}
```

---

Em um loop `for` podemos especificar quantas vezes queremos que o loop execute

---

Podemos usar `<` para iterar até o próximo número excluído, ou `<=` para iterar até o próximo número incluído

---

A variável chamada `i` é a variável contadora.
Podemos dar a ela o nome que quisermos.
Ela conta em qual repetição do loop estamos atualmente

---

Em JavaScript também temos o loop `forEach`.
Na verdade, `forEach` chama a closure fornecida em cada elemento da sequência na mesma ordem que um loop `for`:
```javascript
// this is an array, we'll see about that soon
let numbers = [1, 3, 5, 7, 9];
numbers.forEach((num) => console.log(num));}
```
Usar o método `forEach` é diferente de um loop `for` de duas maneiras importantes:
1. As instruções `break` ou `continue` não podem ser usadas para sair da chamada atual da closure ou para pular chamadas subsequentes.
2. Usar a instrução `return` na closure só sairá da closure e não do escopo externo, e não pulará chamadas subsequentes.
NOTA: `=>` isso é chamado de _arrow function_ e é uma sintaxe de função mais curta do ES6 que substitui as chaves {} e retorna o valor (se necessário)
