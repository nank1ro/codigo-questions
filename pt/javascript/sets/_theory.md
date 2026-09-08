Um **Set** é uma coleção de valores **únicos**: cada valor pode aparecer no máximo uma vez, e não existe um índice para acessar um valor pela posição.
Sets são perfeitos quando você só se importa com *quais* valores estão presentes, não quantas vezes ou em que ordem.
Você cria um set vazio com `new Set()`, adiciona um valor com `add(value)` e verifica se um valor está presente com `has(value)`:
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// prints true
console.log(colors.has("green"));
// prints false
```

---

Adicionar um valor que já está no set não faz **nada**: duplicatas são simplesmente ignoradas.
Mais duas coisas essenciais:
- `delete(value)` remove o valor do set
- `size` é o número de valores armazenados (uma propriedade, então sem parênteses)

```javascript
let tags = new Set();
tags.add("js");
tags.add("css");
tags.add("js");
console.log(tags.size);
// prints 2
tags.delete("css");
console.log(tags.size);
// prints 1
```

---

`add()` retorna o próprio set, então várias chamadas podem ser encadeadas:
```javascript
let letters = new Set();
letters.add("a").add("b");
```
Encadeando ou não, um valor que já está presente nunca é adicionado uma segunda vez, então `size` conta cada valor distinto apenas uma vez.

---

Você pode construir um set de uma vez passando um array para `new Set()`. Duplicatas no array são descartadas, então essa é a forma mais rápida de encontrar os valores distintos de um array:
```javascript
let nums = [1, 2, 2, 3, 3, 3];
let distinct = new Set(nums);
console.log(distinct.size);
// prints 3
```
O operador **spread** `...` funciona no sentido contrário e transforma um set de volta em um array:
```javascript
let unique = [...distinct];
console.log(unique);
// prints [ 1, 2, 3 ]
```
`Array.from(distinct)` faz a mesma coisa.

---

Um set lembra a ordem em que os valores foram adicionados, e você pode percorrê-lo com `for...of`:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// prints 3
// prints 1
// prints 2
```
Sets também têm um método `forEach()` que chama uma função para cada valor:
```javascript
nums.forEach((n) => console.log(n * 10));
// prints 30
// prints 10
// prints 20
```
