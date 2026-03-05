Você pode ter considerado a situação em que gostaria de reutilizar um trecho de código, apenas com alguns valores diferentes.
Em vez de reescrever todo o código, é muito mais limpo definir uma função, que pode ser usada repetidamente.
Em JavaScript, usamos a palavra-chave `function` seguida pelo nome da função:
```javascript
function sayHi() {
    console.log("Hello!");
}
sayHi();
// prints "Hello!"
```

---

Os parênteses na __definição da função__ não precisam estar vazios se quisermos especificar parâmetros

---

Às vezes queremos que uma função __retorne__ um valor.
Bem, existe a palavra-chave `return`.

---

Funções podem ter múltiplos parâmetros de entrada, que são escritos dentro dos parênteses da função, separados por vírgulas.
```javascript
function sayHello(name, newUser) {
  var greet = `Hello ${name}!`;
  if (newUser) {
    greet += " Welcome on board :)";
  }
  return greet;
}
// prints "Hello Smith! Welcome on board :)"
console.log(sayHello("Smith", true));
```

---

Você pode definir um valor _padrão_ para qualquer parâmetro em uma função atribuindo um valor ao parâmetro após o tipo desse parâmetro.
Se um valor padrão for definido, você pode omitir esse parâmetro ao chamar a função
```javascript
function someFunction(parameterWithoutDefault, parameterWithDefault = 12) {
    // do stuff here
}
```

---

A sintaxe do __parâmetro rest__ nos permite representar um número indefinido de argumentos como um array.
Escreva parâmetros rest inserindo três caracteres de ponto `...` antes do nome do parâmetro.
Os valores passados para um parâmetro rest ficam disponíveis dentro do corpo da função como um array.
Por exemplo, um parâmetro rest com o nome `numbers` fica disponível dentro do corpo da função como um array constante chamado numbers

---

Nas funções podemos adicionar um _comentário opcional_ que explica o que a função faz:
```javascript
// Prints 'Hello World' to the console.
function helloWorld() {
    console.log("Hello, World!");
}
```
Podemos usar `//` para um comentário de uma linha e `/** */` para um comentário de múltiplas linhas
