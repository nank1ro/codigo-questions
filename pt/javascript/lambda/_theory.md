Uma função não precisa de um nome. Uma **function expression** cria uma função como um valor, que você pode armazenar em uma variável e chamar através dela:
```javascript
const add = function (a, b) {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
Uma **arrow function** é uma forma mais curta de escrever a mesma coisa: elimine a palavra-chave `function` e coloque uma "seta gorda" `=>` entre a lista de parâmetros e o corpo:
```javascript
const add = (a, b) => {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
Arrow functions geralmente são armazenadas em uma `const`, para que o nome não possa ser reatribuído por engano, e são chamadas exatamente como qualquer outra função.

---

Arrow functions ficam mais curtas em dois casos comuns.
Quando o corpo é uma **expressão única**, você pode eliminar as chaves e a palavra-chave `return`: o valor da expressão é retornado automaticamente (um **retorno implícito**):
```javascript
const add = (a, b) => a + b;
console.log(add(2, 3));
// prints 5
```
Quando há **exatamente um parâmetro**, você também pode eliminar os parênteses ao redor dele:
```javascript
const double = n => n * 2;
console.log(double(4));
// prints 8
```
Com zero parâmetros ou com dois ou mais, os parênteses são obrigatórios: `() => 42` e `(a, b) => a + b`.

---

Há uma armadilha com o retorno implícito. Uma arrow function cujo corpo começa com `{` é interpretada como um **corpo de bloco**, nunca como um objeto literal:
```javascript
const make = (name) => { name: name };
console.log(make("Ana"));
// prints undefined
```
Aqui, `{ name: name }` é um bloco contendo o rótulo `name:` seguido pela expressão `name`. Nada é retornado, então a chamada resulta em `undefined`.
Para retornar um objeto literal em uma linha, envolva-o em **parênteses** para que o JavaScript o trate como uma expressão:
```javascript
const make = (name) => ({ name: name });
console.log(make("Ana"));
// prints { name: 'Ana' }
```

---

Envolver o objeto literal em parênteses é a forma padrão de construir objetos com uma arrow function de uma linha, por exemplo quando você transforma um par de valores em um registro:
```javascript
const user = (name, age) => ({ name: name, age: age });
console.log(user("Ana", 30).age);
// prints 30
```
Uma arrow function sem parâmetros começa com um par vazio de parênteses `()`:
```javascript
const empty = () => ({});
console.log(empty());
// prints {}
```

---

Arrow functions realmente brilham como **callbacks**: funções passadas como argumentos para outras funções. Os métodos de array são o exemplo mais comum.
`map(callback)` retorna um novo array com o resultado do callback para cada elemento, e `filter(callback)` retorna um novo array apenas com os elementos para os quais o callback retorna `true`:
```javascript
const numbers = [1, 2, 3, 4];
console.log(numbers.map((n) => n * 10));
// prints [ 10, 20, 30, 40 ]
console.log(numbers.filter((n) => n > 2));
// prints [ 3, 4 ]
```
Ambos retornam um novo array e deixam o original intocado, então você pode encadeá-los: `numbers.filter(...).map(...)`.

---

Dois outros métodos de array recebem um callback.
`forEach(callback)` chama o callback uma vez por elemento e não retorna nada; use-o para efeitos colaterais, como imprimir.
`reduce(callback, initialValue)` reduz o array a um único valor: o callback recebe o valor acumulado até o momento e o elemento atual, e retorna o novo valor acumulado:
```javascript
const numbers = [1, 2, 3];
numbers.forEach((n) => console.log(n));
// prints 1, 2 and 3 on three lines
const total = numbers.reduce((sum, n) => sum + n, 0);
console.log(total);
// prints 6
```

---

`sort(compare)` ordena um array no próprio lugar usando um callback que recebe dois elementos e retorna um número negativo quando o primeiro deve vir primeiro, um número positivo quando o segundo deve vir primeiro, ou `0` quando são iguais. Para números, `(a, b) => a - b` ordena em ordem crescente e `(a, b) => b - a` em ordem decrescente.
`find(callback)` retorna o primeiro elemento para o qual o callback retorna `true`, ou `undefined` se não houver nenhum:
```javascript
const scores = [50, 90, 70];
scores.sort((a, b) => a - b);
console.log(scores);
// prints [ 50, 70, 90 ]
console.log(scores.find((s) => s > 60));
// prints 70
```

---

Os parâmetros de arrow functions suportam os mesmos recursos que os parâmetros de funções regulares.
Um **valor padrão** é usado quando o argumento é omitido ou é `undefined`:
```javascript
const greet = (name = "World") => `Hello, ${name}!`;
console.log(greet());
// prints Hello, World!
console.log(greet("Ana"));
// prints Hello, Ana!
```
Note que um parâmetro com um valor padrão sempre precisa dos parênteses, mesmo quando é o único: `name = "World" => ...` é um erro de sintaxe.

---

Um **parâmetro rest** `...name` coleta qualquer quantidade de argumentos em um array, e também funciona em arrow functions:
```javascript
const count = (...items) => items.length;
console.log(count("a", "b", "c"));
// prints 3
```
Funções regulares também têm um objeto `arguments` oculto, semelhante a um array, que guarda cada argumento recebido. Arrow functions **não**: dentro de uma arrow, `arguments` refere-se ao `arguments` da função ao redor ou não existe de forma alguma. Sempre que precisar de "todos os argumentos" em uma arrow function, use um parâmetro rest.

---

Uma função lembra as variáveis do escopo onde ela foi **criada**, mesmo depois que esse escopo terminou de executar. Isso é chamado de **closure**.
O exemplo clássico é um criador de contadores: cada chamada a `makeCounter` cria um novo `count` e retorna uma arrow function que continua usando esse mesmo `count`:
```javascript
const makeCounter = () => {
  let count = 0;
  return () => {
    count += 1;
    return count;
  };
};
const next = makeCounter();
console.log(next());
// prints 1
console.log(next());
// prints 2
```
Ninguém mais pode ler ou redefinir `count`: ele vive apenas dentro da função retornada. Uma segunda chamada a `makeCounter()` cria um contador independente com o seu próprio `count`.

---

Como uma função é um valor, uma arrow function pode **retornar outra arrow function**. Encadear duas arrows é uma forma compacta de escrever uma função que constrói funções:
```javascript
const makeAdder = (amount) => (n) => n + amount;
const addTen = makeAdder(10);
console.log(addTen(5));
// prints 15
console.log(makeAdder(1)(5));
// prints 6
```
Leia da esquerda para a direita: `makeAdder` recebe `amount` e retorna `(n) => n + amount`, uma arrow function que captura `amount` por meio de uma closure. `makeAdder(1)(5)` chama a função retornada imediatamente.
