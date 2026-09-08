**Map** хранит **пары ключ-значение**: каждое значение сохраняется под ключом, и вы используете этот ключ, чтобы снова найти значение.
Вы создаёте пустой Map с помощью `new Map()`, добавляете пару с помощью `set(key, value)` и читаете значение с помощью `get(key)`:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// prints 30
```
Вызов `set()` с ключом, который уже существует, заменяет его значение.

---

У Map есть ещё несколько важных методов и свойств:
- `has(key)` возвращает `true`, если ключ существует
- `delete(key)` удаляет пару с этим ключом
- `size` — это количество хранимых пар

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
Обратите внимание, что `size` — это свойство, а не метод, поэтому у него нет скобок.

---

Запрос к Map ключа, которого в нём нет, не является ошибкой: `get()` просто возвращает `undefined`.
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// prints undefined
```
Именно поэтому существует `has()`: он позволяет отличить отсутствующий ключ от ключа, значение которого оказалось `undefined`.
`set()` возвращает сам Map, поэтому вызовы можно объединять в цепочку:
```javascript
ages.set("Bob", 25).set("Cy", 41);
```

---

В обычном объекте каждый ключ превращается в строку: `user[1]` и `user["1"]` — это один и тот же ключ.
Map сохраняет **тип** своих ключей, поэтому число, строка, логическое значение или даже объект могут быть разными ключами:
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
Ключи-объекты сравниваются по идентичности: значение получает обратно только тот же самый объект.

---

Map запоминает порядок, в котором были добавлены пары, и вы можете перебирать его с помощью `for...of`.
Метод `entries()` возвращает каждую пару в виде массива `[key, value]`, который можно сразу распаковать в цикле:
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
Перебор самого Map, `for (const [name, qty] of stock)`, делает ровно то же самое.

---

Когда вам нужна только одна сторона пар, используйте в цикле `keys()` или `values()` вместо `entries()`:
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

Вместо того чтобы вызывать `set()` много раз, вы можете построить Map за один раз, передав **массив пар** в `new Map()`:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// prints 2
```
Поскольку `Object.entries(obj)` возвращает именно такой массив пар, это самый быстрый способ превратить объект в Map:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// prints 30
```
