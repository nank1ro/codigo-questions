**Map** хранит **пары ключ-значение**: каждое значение сохраняется под ключом, и вы используете этот ключ, чтобы снова найти значение.
Вы создаёте пустой Map с помощью `new Map()`, добавляете пару с помощью `set(key, value)` и читаете значение с помощью `get(key)`:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// выводит 30
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
// выводит true
stock.delete("pear");
console.log(stock.size);
// выводит 1
```
Обратите внимание, что `size` — это свойство, а не метод, поэтому у него нет скобок.

---

Запрос к Map ключа, которого в нём нет, не является ошибкой: `get()` просто возвращает `undefined`.
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// выводит undefined
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
// выводит 2
let alice = { name: "Alice" };
lookup.set(alice, "an object key");
console.log(lookup.get(alice));
// выводит an object key
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
// выводит apple: 3
// выводит pear: 5
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
// выводит tea
// выводит cake
for (const price of prices.values()) {
  console.log(price);
}
// выводит 2
// выводит 4
```

---

Вместо того чтобы вызывать `set()` много раз, вы можете построить Map за один раз, передав **массив пар** в `new Map()`:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// выводит 2
```
Поскольку `Object.entries(obj)` возвращает именно такой массив пар, это самый быстрый способ превратить объект в Map:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// выводит 30
```

---

Map и обычные объекты оба хранят значения под ключами, но отличаются в нескольких важных аспектах:
- ключи объекта всегда являются строками (или символами), ключи Map могут быть **любого** типа
- Map сохраняет точный **порядок вставки** своих пар
- Map знает свой собственный `size`, тогда как для объекта нужно `Object.keys(obj).length`
- Map начинается по-настоящему пустым, тогда как объект наследует такие ключи, как `toString`, от своего прототипа

---

У Map нет методов массива, таких как `sort()` или `filter()`. Чтобы их использовать, преобразуйте Map (или его ключи, или значения) в массив с помощью `Array.from()` или оператора расширения `...`:
```javascript
let ages = new Map([["Bob", 25], ["Ann", 30]]);
let pairs = Array.from(ages);
console.log(pairs);
// выводит [ [ 'Bob', 25 ], [ 'Ann', 30 ] ]
let names = [...ages.keys()];
console.log(names);
// выводит [ 'Bob', 'Ann' ]
let values = [...ages.values()];
console.log(values);
// выводит [ 25, 30 ]
```
Обратное преобразование, `Object.fromEntries(ages)`, превращает Map обратно в обычный объект.

---

Как и массивы, Map имеет метод `forEach()`, который вызывает функцию для каждой пары.
Будьте внимательны с порядком параметров: колбэк получает сначала **значение**, а затем ключ:
```javascript
let stock = new Map([["apple", 3], ["pear", 5]]);
stock.forEach((qty, name) => {
  console.log(`${name} x${qty}`);
});
// выводит apple x3
// выводит pear x5
```

---

`delete(key)` возвращает `true`, если пара была удалена, и `false`, если такого ключа не было.
Чтобы удалить **все** пары сразу, вызовите `clear()`:
```javascript
let cart = new Map([["pen", 2], ["ink", 1]]);
console.log(cart.delete("pen"));
// выводит true
console.log(cart.delete("pen"));
// выводит false
cart.clear();
console.log(cart.size);
// выводит 0
```

---

Так когда же стоит использовать `Map` вместо обычного объекта?
- Используйте **Map**, когда ключи добавляются и удаляются во время выполнения, когда они не являются строками, или когда вам нужны `size` и надёжный порядок
- Используйте **объект** для фиксированной записи с известными именами полей, например `{ name, email }`, и всегда, когда нужно преобразовать данные в JSON, поскольку `JSON.stringify()` игнорирует содержимое Map
