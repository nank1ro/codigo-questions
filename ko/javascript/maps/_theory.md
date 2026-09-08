**맵**은 **키-값 쌍**을 저장합니다: 각 값은 키 아래에 저장되고, 그 키를 사용해 값을 다시 찾을 수 있습니다.
`new Map()`으로 빈 맵을 만들고, `set(key, value)`로 쌍을 추가하고, `get(key)`로 값을 읽습니다:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// prints 30
```
이미 존재하는 키로 `set()`을 호출하면 그 값을 대체합니다.

---

맵에는 몇 가지 더 중요한 메서드와 속성이 있습니다:
- `has(key)`는 키가 존재하면 `true`를 반환합니다
- `delete(key)`는 그 키를 가진 쌍을 제거합니다
- `size`는 저장된 쌍의 개수입니다

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
`size`는 메서드가 아니라 속성이므로 괄호가 없다는 점에 유의하세요.

---

맵에 없는 키를 요청해도 에러가 발생하지 않습니다: `get()`은 그냥 `undefined`를 반환합니다.
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// prints undefined
```
그래서 `has()`가 존재합니다: 이를 통해 없는 키와 값이 우연히 `undefined`인 키를 구분할 수 있습니다.
`set()`은 맵 자신을 반환하므로, 호출을 연결할 수 있습니다:
```javascript
ages.set("Bob", 25).set("Cy", 41);
```

---

일반 객체에서는 모든 키가 문자열로 바뀝니다: `user[1]`과 `user["1"]`은 같은 키입니다.
맵은 키의 **타입**을 그대로 유지하므로, 숫자, 문자열, 불리언, 심지어 객체까지도 각각 다른 키가 될 수 있습니다:
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
객체 키는 동일성으로 비교되므로, 바로 그 객체만 값을 다시 얻을 수 있습니다.

---

맵은 쌍이 추가된 순서를 기억하며, `for...of`로 반복할 수 있습니다.
`entries()` 메서드는 각 쌍을 `[key, value]` 배열로 제공하므로, 루프 안에서 바로 구조 분해할 수 있습니다:
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
맵을 직접 반복하는 `for (const [name, qty] of stock)`도 정확히 같은 동작을 합니다.

---

쌍의 한쪽만 필요할 때는, `entries()` 대신 루프에서 `keys()`나 `values()`를 사용하세요:
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

`set()`을 여러 번 호출하는 대신, **쌍의 배열**을 `new Map()`에 전달해 한 번에 맵을 만들 수 있습니다:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// prints 2
```
`Object.entries(obj)`가 정확히 그런 쌍의 배열을 반환하므로, 객체를 맵으로 바꾸는 가장 빠른 방법입니다:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// prints 30
```
