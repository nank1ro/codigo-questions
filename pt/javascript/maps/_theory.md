Um **Map** armazena **pares chave-valor**: cada valor é salvo sob uma chave, e você usa essa chave para encontrar o valor novamente.
Você cria um map vazio com `new Map()`, adiciona um par com `set(key, value)` e lê um valor com `get(key)`:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// prints 30
```
Chamar `set()` com uma chave que já existe substitui seu valor.

---

Um map tem mais alguns métodos e propriedades essenciais:
- `has(key)` retorna `true` se a chave existir
- `delete(key)` remove o par com essa chave
- `size` é o número de pares armazenados

```javascript
let stock = new Map();
stock.set("apple", 3);
stock.set("pear", 5);
console.log(stock.has("apple"));
// prints true
stock.delete("pear");
console.log(stock.size);
// prints 1
```
Note que `size` é uma propriedade, não um método, então não tem parênteses.

---

Pedir a um map uma chave que ele não contém não é um erro: `get()` simplesmente retorna `undefined`.
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// prints undefined
```
É por isso que `has()` existe: ele permite diferenciar uma chave ausente de uma chave cujo valor é `undefined`.
`set()` retorna o próprio map, então as chamadas podem ser encadeadas:
```javascript
ages.set("Bob", 25).set("Cy", 41);
```

---

Em um objeto comum, toda chave é convertida em string: `user[1]` e `user["1"]` são a mesma chave.
Um map preserva o **tipo** de suas chaves, então um número, uma string, um booleano ou até mesmo um objeto podem ser chaves diferentes:
```javascript
let lookup = new Map();
lookup.set(1, "number one");
lookup.set("1", "string one");
console.log(lookup.size);
// prints 2
let alice = { name: "Alice" };
lookup.set(alice, "an object key");
console.log(lookup.get(alice));
// prints an object key
```
Chaves de objeto são comparadas por identidade: apenas o mesmo objeto exato recebe o valor de volta.

---

Um map se lembra da ordem em que os pares foram adicionados, e você pode percorrê-lo com `for...of`.
O método `entries()` fornece cada par como um array `[key, value]`, que você pode desestruturar diretamente no loop:
```javascript
let stock = new Map();
stock.set("apple", 3);
stock.set("pear", 5);
for (const [name, qty] of stock.entries()) {
  console.log(`${name}: ${qty}`);
}
// prints apple: 3
// prints pear: 5
```
Percorrer o map diretamente, `for (const [name, qty] of stock)`, faz exatamente a mesma coisa.

---

Quando você precisa apenas de um lado dos pares, use `keys()` ou `values()` no loop em vez de `entries()`:
```javascript
let prices = new Map();
prices.set("tea", 2);
prices.set("cake", 4);
for (const name of prices.keys()) {
  console.log(name);
}
// prints tea
// prints cake
for (const price of prices.values()) {
  console.log(price);
}
// prints 2
// prints 4
```

---

Em vez de chamar `set()` várias vezes, você pode construir um map de uma vez passando um **array de pares** para `new Map()`:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// prints 2
```
Como `Object.entries(obj)` retorna exatamente esse array de pares, é a forma mais rápida de transformar um objeto em um map:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// prints 30
```
