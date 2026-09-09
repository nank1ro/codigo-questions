Em JavaScript uma função é um **valor**: podes guardá-la numa variável, colocá-la num array e passá-la a outra função como argumento. Uma função que recebe uma função como argumento, ou que devolve uma, chama-se **função de ordem superior**. A função passada chama-se **callback**, porque quem a recebe *chama-a de volta* quando precisa:
```javascript
function shout(text) {
  return text.toUpperCase() + "!";
}
function twice(fn, value) {
  return fn(fn(value));
}
console.log(twice(shout, "hi"));
// prints HI!!
```
Repara que `shout` é passada **sem parênteses**: `twice(shout, "hi")` entrega a própria função, enquanto `twice(shout("hi"), "hi")` chamaria primeiro `shout` e passaria o seu resultado, a string `"HI!"`, que não pode ser chamada.

---

As funções de ordem superior permitem separar *o que fazer com cada elemento* de *como percorrer os elementos*. A parte que percorre é escrita uma só vez, e o callback decide o resto:
```javascript
function each(items, action) {
  for (let i = 0; i < items.length; i++) {
    action(items[i]);
  }
}
each(["a", "b"], (letter) => console.log(letter));
// prints a and b on two lines
```
O callback recebe um elemento de cada vez. Pode ser uma arrow function escrita em linha, como acima, ou qualquer função guardada numa variável. É exatamente assim que funcionam por dentro os métodos de array que vais conhecer a seguir.

---

O método integrado `map` faz o que `transform` faz: chama o callback para cada elemento e recolhe os resultados num **novo array**. `forEach` também chama o callback para cada elemento, mas não recolhe nada e devolve sempre `undefined`; usa-o apenas para efeitos secundários, como imprimir:
```javascript
const prices = [5, 10];
const doubled = prices.map((p) => p * 2);
prices.forEach((p) => console.log(p));
// prints 5 and 10 on two lines
console.log(doubled);
// prints [ 10, 20 ]
```
Um erro comum é guardar o resultado de `forEach` ou encadear outro método a seguir: não há nada para encadear, porque devolve `undefined`. Regra prática: usa `map` quando precisas dos novos valores, `forEach` quando só precisas de *fazer* algo.

---

Mais dois métodos de ordem superior cobrem a maior parte das necessidades do dia a dia.
`filter(callback)` devolve um novo array apenas com os elementos para os quais o callback devolve `true`; um callback que responde sim ou não desta forma chama-se **predicado**.
`reduce(callback, initialValue)` combina todos os elementos num único valor: o callback recebe o **acumulador** (o resultado até ao momento) e o elemento atual, e devolve o novo acumulador. O segundo argumento de `reduce` é o acumulador inicial:
```javascript
const numbers = [3, 8, 5];
console.log(numbers.filter((n) => n > 4));
// prints [ 8, 5 ]
console.log(numbers.reduce((sum, n) => sum + n, 0));
// prints 16
```
Como `filter` e `map` devolvem arrays, podes encadeá-los e terminar com `reduce`: `numbers.filter(...).map(...).reduce(...)`.

---

Três métodos respondem a perguntas sobre um array com um predicado:
- `find(predicate)` devolve o **primeiro** elemento para o qual o predicado é `true`, ou `undefined` se não houver nenhum
- `some(predicate)` devolve `true` se **pelo menos um** elemento satisfizer o predicado
- `every(predicate)` devolve `true` se **todos** os elementos o satisfizerem (e `true` para um array vazio)
```javascript
const scores = [72, 45, 90];
console.log(scores.find((s) => s < 60));
// prints 45
console.log(scores.some((s) => s === 90), scores.every((s) => s >= 60));
// prints true false
```
Os três param assim que a resposta é conhecida, por isso nunca olham para mais elementos do que o necessário.

---

`sort(compare)` ordena um array **no lugar** usando um callback que recebe dois elementos e devolve um número negativo quando o primeiro deve vir primeiro, um número positivo quando deve vir primeiro o segundo, ou `0` quando são iguais. Para números, `(a, b) => a - b` ordena de forma crescente e `(a, b) => b - a` de forma decrescente.
Sem comparador, `sort()` converte cada elemento numa **string** e compara-os caráter a caráter, por isso `10` vem antes de `9` porque `"1"` é menor do que `"9"`:
```javascript
console.log([10, 9, 1].sort());
// prints [ 1, 10, 9 ]
console.log([10, 9, 1].sort((a, b) => a - b));
// prints [ 1, 9, 10 ]
```
Como `sort` modifica o array, ordena uma cópia quando também precisas da ordem original: `[...numbers].sort(...)`. Para strings usa `(a, b) => a.localeCompare(b)` como comparador, que ordena o texto alfabeticamente.

---

O comparador pode olhar para qualquer parte dos elementos, por isso um array de objetos ordena-se por uma das suas propriedades apenas comparando essa propriedade:
```javascript
const items = [{ name: "b", size: 3 }, { name: "a", size: 1 }];
const bySize = [...items].sort((x, y) => x.size - y.size);
console.log(bySize.map((item) => item.name));
// prints [ 'a', 'b' ]
```
Ordenar a cópia deixa `items` na sua ordem original.

---

Uma função de ordem superior também pode **devolver** uma função. A função devolvida lembra-se das variáveis do sítio onde foi criada, mesmo depois de a função exterior ter terminado: a isto chama-se **closure**.
```javascript
function makeMultiplier(factor) {
  return function (n) {
    return n * factor;
  };
}
const triple = makeMultiplier(3);
console.log(triple(5));
// prints 15
console.log(makeMultiplier(10)(5));
// prints 50
```
Cada chamada a `makeMultiplier` cria uma nova função com o seu próprio `factor`. É assim que se constrói uma família de funções semelhantes a partir de um único modelo. O mesmo pode escrever-se com arrow functions: `const makeMultiplier = (factor) => (n) => n * factor;`.

---

Uma closure mantém uma ligação **viva** à variável, não uma cópia do seu valor. Quando várias funções são criadas na mesma chamada, partilham a mesma variável, e qualquer alteração feita através de uma é visível para as outras:
```javascript
function makeCounter() {
  let count = 0;
  return {
    increment: () => { count += 1; },
    value: () => count,
  };
}
const counter = makeCounter();
counter.increment();
counter.increment();
console.log(counter.value());
// prints 2
```
Ninguém consegue ler ou repor `count` a partir de fora, exceto através dessas duas funções: a variável é **privada**. Uma segunda chamada a `makeCounter()` cria um `count` completamente separado.

---

Como as funções são valores, podes escrever uma função de ordem superior que **combina** duas funções numa nova. `compose(f, g)` devolve uma função que aplica primeiro `g` e depois `f` ao resultado, tal como a notação matemática *f(g(x))*:
```javascript
const compose = (f, g) => (x) => f(g(x));
const trim = (s) => s.trim();
const shout = (s) => s.toUpperCase();
const clean = compose(shout, trim);
console.log(clean("  hi  "));
// prints HI
```
A ordem importa: `compose(f, g)` executa primeiro `g`, depois `f`. Construir programas colando pequenas funções desta forma chama-se **composição de funções**.

---

Uma função que devolve uma função é também a forma natural de **adaptar** um callback. Supõe que tens um predicado e precisas do seu oposto para `filter`: em vez de o reescrever, envolve-o:
```javascript
const isLong = (word) => word.length > 4;
const isShort = (word) => !isLong(word);
console.log(["tree", "forest"].filter(isShort));
// prints [ 'tree' ]
```
Um `not(predicate)` genérico faria isto para qualquer predicado: devolve uma nova função que chama `predicate` com o mesmo argumento e inverte o resultado com `!`. Os predicados de `filter`, `find`, `some` e `every` recebem o elemento como primeiro argumento, por isso o wrapper só precisa de reencaminhar esse valor.

---

O acumulador de `reduce` não tem de ser um número: pode ser uma string, um array ou um objeto. A partir de um objeto vazio `{}` podes contar ou agrupar coisas numa só passagem. Lembra-te de **devolver o acumulador** a partir do callback, caso contrário o passo seguinte recebe `undefined`:
```javascript
const votes = ["yes", "no", "yes"];
const tally = votes.reduce((acc, vote) => {
  acc[vote] = (acc[vote] ?? 0) + 1;
  return acc;
}, {});
console.log(tally);
// prints { yes: 2, no: 1 }
```
`acc[vote] ?? 0` lê a contagem atual, ou `0` quando essa chave ainda não existe.

---

Todas as funções têm um método `bind` que devolve uma **nova** função com algumas coisas fixadas antecipadamente. O seu primeiro argumento passa a ser o `this` da nova função; os restantes argumentos são colocados à frente daqueles com que a nova função for chamada (uma **aplicação parcial**):
```javascript
function multiply(a, b) {
  return a * b;
}
const double = multiply.bind(null, 2);
console.log(double(21));
// prints 42
```
Fixar `this` é importante nos métodos. Quando um método é copiado para fora do seu objeto e chamado sozinho, `this` deixa de se referir ao objeto, por isso `this.name` passa a ser `undefined`. `bind` fixa-o ao objeto:
```javascript
const user = {
  name: "Ana",
  hello() { return `Hi ${this.name}`; },
};
const loose = user.hello;
console.log(loose());
// prints Hi undefined
const bound = user.hello.bind(user);
console.log(bound());
// prints Hi Ana
```
A função original nunca é alterada: `bind` constrói sempre uma nova, cujo `name` é o nome original precedido de `bound `.

---

Os programas reais combinam estes métodos num **pipeline**: filtra os elementos que te interessam, mapeia-os para os valores de que precisas e reduz tudo a um resultado. Guardar os arrays intermédios em constantes mantém cada passo legível e permite reutilizá-los:
```javascript
const adults = people.filter((p) => p.age >= 18);
const names = adults.map((p) => p.name);
const totalAge = adults.reduce((sum, p) => sum + p.age, 0);
```
`names.join(", ")` transforma um array de strings numa única string com os elementos separados por uma vírgula e um espaço.

---

As closures permitem que uma função devolvida mantenha **estado privado** entre chamadas. Um utilitário clássico construído assim é `once(fn)`: devolve uma função que executa `fn` apenas na primeira vez que é chamada, guarda o resultado e devolve esse mesmo resultado em todas as chamadas seguintes sem executar `fn` de novo:
```javascript
let calls = 0;
const init = once(() => {
  calls += 1;
  return "ready";
});
console.log(init(), init(), calls);
// prints ready ready 1
```
O wrapper precisa de duas variáveis privadas: se `fn` já foi executada, e o resultado guardado. Ambas vivem na closure, invisíveis para o exterior. Para reencaminhar para `fn` todos os argumentos do wrapper, declara o wrapper com um parâmetro rest `(...args)` e chama `fn(...args)`.

---

Tudo se junta em `groupBy(items, keyFn)`: uma função de ordem superior que recebe um callback que decide a **chave de grupo** de cada elemento e devolve um objeto que associa cada chave ao array dos elementos com essa chave. `reduce` com um acumulador objeto faz todo o trabalho:
```javascript
const byInitial = groupBy(["hi", "yo", "hey"], (w) => w[0]);
console.log(byInitial);
// prints { h: [ 'hi', 'hey' ], y: [ 'yo' ] }
```
Para cada elemento, calcula a chave, cria o array dessa chave se ainda não existir (`acc[key] ?? []`), adiciona o elemento e devolve o acumulador. Como é quem chama que escolhe `keyFn`, a mesma função agrupa palavras por inicial, pessoas por cidade ou números por paridade.
