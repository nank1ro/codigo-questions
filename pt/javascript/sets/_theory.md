Um **Set** é uma coleção de valores **únicos**: cada valor pode aparecer no máximo uma vez, e não existe um índice para acessar um valor pela posição.
Sets são perfeitos quando você só se importa com *quais* valores estão presentes, não quantas vezes ou em que ordem.
Você cria um set vazio com `new Set()`, adiciona um valor com `add(value)` e verifica se um valor está presente com `has(value)`:
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// imprime true
console.log(colors.has("green"));
// imprime false
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
// imprime 2
tags.delete("css");
console.log(tags.size);
// imprime 1
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
// imprime 3
```
O operador **spread** `...` funciona no sentido contrário e transforma um set de volta em um array:
```javascript
let unique = [...distinct];
console.log(unique);
// imprime [ 1, 2, 3 ]
```
`Array.from(distinct)` faz a mesma coisa.

---

Um set lembra a ordem em que os valores foram adicionados, e você pode percorrê-lo com `for...of`:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// imprime 3
// imprime 1
// imprime 2
```
Sets também têm um método `forEach()` que chama uma função para cada valor:
```javascript
nums.forEach((n) => console.log(n * 10));
// imprime 30
// imprime 10
// imprime 20
```

---

`delete(value)` retorna `true` quando o valor foi removido e `false` quando ele não estava no set.
Para remover **todos** os valores de uma vez, chame `clear()`:
```javascript
let cart = new Set(["pen", "ink"]);
console.log(cart.delete("pen"));
// imprime true
console.log(cart.delete("pen"));
// imprime false
cart.clear();
console.log(cart.size);
// imprime 0
```

---

Um set decide se dois valores são "iguais" com quase a mesma regra do `===` (exceto que `NaN` conta como igual a si mesmo). Para strings e números isso compara o conteúdo, mas **objetos são comparados por referência**: dois objetos literais com campos idênticos são dois valores diferentes.
```javascript
let alice = { name: "Alice" };
let people = new Set();
people.add(alice);
people.add(alice);
console.log(people.size);
// imprime 1
people.add({ name: "Alice" });
console.log(people.size);
// imprime 2
```
Apenas adicionar o mesmíssimo objeto novamente é ignorado.

---

Combinar spread e `filter()` te dá as operações clássicas da teoria dos conjuntos. Cada uma constrói uma **nova** coleção e deixa as originais inalteradas:
- **união**, todo valor que está em `a`, em `b` ou em ambos: `new Set([...a, ...b])`
- **interseção**, apenas os valores que estão em **ambos**: `[...a].filter((x) => b.has(x))`
- **diferença**, os valores de `a` que **não** estão em `b`: `[...a].filter((x) => !b.has(x))`

```javascript
let a = new Set([1, 2, 3]);
let b = new Set([3, 4]);
console.log([...new Set([...a, ...b])]);
// imprime [ 1, 2, 3, 4 ]
console.log([...a].filter((x) => b.has(x)));
// imprime [ 3 ]
console.log([...a].filter((x) => !b.has(x)));
// imprime [ 1, 2 ]
```
Motores JavaScript recentes também oferecem `a.union(b)`, `a.intersection(b)` e `a.difference(b)` diretamente nos sets, mas as versões com spread e filter funcionam em qualquer lugar.

---

Para manter a mesma interface do `Map`, um set oferece os métodos iteradores `values()`, `keys()` e `entries()`.
Como um set não tem chaves, `keys()` é apenas outro nome para `values()`, e `entries()` produz cada valor **duas vezes**, como um par `[value, value]`:
```javascript
let letters = new Set(["a", "b"]);
console.log([...letters.values()]);
// imprime [ 'a', 'b' ]
console.log([...letters.entries()]);
// imprime [ [ 'a', 'a' ], [ 'b', 'b' ] ]
```
Na prática você raramente precisa deles: `for...of` e spread já percorrem os valores diretamente.

---

`new Set()` aceita qualquer **iterável**, não apenas arrays. Uma string é iterável caractere por caractere, então ela te dá os caracteres distintos de um texto:
```javascript
let letters = new Set("hello");
console.log([...letters]);
// imprime [ 'h', 'e', 'l', 'o' ]
```
