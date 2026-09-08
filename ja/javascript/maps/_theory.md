**マップ**は**キーと値のペア**を格納します：それぞれの値はキーの下に保存され、そのキーを使って値を再び見つけることができます。
`new Map()`で空のマップを作成し、`set(key, value)`でペアを追加し、`get(key)`で値を読み取ります：
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// prints 30
```
すでに存在するキーで`set()`を呼び出すと、その値が置き換えられます。

---

マップにはさらにいくつかの重要なメソッドとプロパティがあります：
- `has(key)`はキーが存在すれば`true`を返す
- `delete(key)`はそのキーを持つペアを削除する
- `size`は格納されているペアの数

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
`size`はメソッドではなくプロパティなので、括弧がないことに注意してください。

---

マップに存在しないキーを尋ねてもエラーにはなりません：`get()`は単に`undefined`を返します。
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// prints undefined
```
だからこそ`has()`が存在します：存在しないキーと、値がたまたま`undefined`であるキーを区別できます。
`set()`はマップ自身を返すので、呼び出しを連結できます：
```javascript
ages.set("Bob", 25).set("Cy", 41);
```

---

プレーンなオブジェクトでは、すべてのキーが文字列に変換されます：`user[1]`と`user["1"]`は同じキーです。
マップはキーの**型**を保持するので、数値・文字列・真偽値、さらにはオブジェクトさえもそれぞれ別のキーになります：
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
オブジェクトのキーは同一性で比較されるため、まったく同じオブジェクトだけが値を取り戻せます。

---

マップはペアが追加された順序を記憶しており、`for...of`でループできます。
`entries()`メソッドは各ペアを`[key, value]`の配列として返すので、ループの中でそのまま分割代入できます：
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
マップを直接ループする`for (const [name, qty] of stock)`も、まったく同じことをします。

---

ペアの片方だけが必要なときは、`entries()`の代わりにループで`keys()`や`values()`を使います：
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

`set()`を何度も呼び出す代わりに、**ペアの配列**を`new Map()`に渡すことで一度にマップを作ることができます：
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// prints 2
```
`Object.entries(obj)`はまさにそのようなペアの配列を返すので、オブジェクトをマップに変換する最も手早い方法です：
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// prints 30
```
