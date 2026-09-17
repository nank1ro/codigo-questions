**맵**은 **키-값 쌍**을 저장합니다: 각 값은 키 아래에 저장되고, 그 키를 사용해 값을 다시 찾을 수 있습니다.
`new Map()`으로 빈 맵을 만들고, `set(key, value)`로 쌍을 추가하고, `get(key)`로 값을 읽습니다:
```javascript
let ages = new Map();
ages.set("Ann", 30);
ages.set("Bob", 25);
console.log(ages.get("Ann"));
// 30 출력
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
// true 출력
stock.delete("pear");
console.log(stock.size);
// 1 출력
```
`size`는 메서드가 아니라 속성이므로 괄호가 없다는 점에 유의하세요.

---

맵에 없는 키를 요청해도 에러가 발생하지 않습니다: `get()`은 그냥 `undefined`를 반환합니다.
```javascript
let ages = new Map();
ages.set("Ann", 30);
console.log(ages.get("Zed"));
// undefined 출력
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
// 2 출력
let alice = { name: "Alice" };
lookup.set(alice, "an object key");
console.log(lookup.get(alice));
// an object key 출력
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
// apple: 3 출력
// pear: 5 출력
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
// tea 출력
// cake 출력
for (const price of prices.values()) {
  console.log(price);
}
// 2 출력
// 4 출력
```

---

`set()`을 여러 번 호출하는 대신, **쌍의 배열**을 `new Map()`에 전달해 한 번에 맵을 만들 수 있습니다:
```javascript
let pairs = [["red", "#f00"], ["blue", "#00f"]];
let colors = new Map(pairs);
console.log(colors.size);
// 2 출력
```
`Object.entries(obj)`가 정확히 그런 쌍의 배열을 반환하므로, 객체를 맵으로 바꾸는 가장 빠른 방법입니다:
```javascript
let user = { name: "Ann", age: 30 };
let userMap = new Map(Object.entries(user));
console.log(userMap.get("age"));
// 30 출력
```

---

맵과 일반 객체는 둘 다 키 아래에 값을 저장하지만, 몇 가지 중요한 차이가 있습니다:
- 객체의 키는 항상 문자열(또는 심볼)이지만, 맵의 키는 **어떤** 타입이든 될 수 있습니다
- 맵은 쌍의 정확한 **삽입 순서**를 유지합니다
- 맵은 자신의 `size`를 알고 있지만, 객체는 `Object.keys(obj).length`가 필요합니다
- 맵은 정말로 비어 있는 상태로 시작하지만, 객체는 프로토타입으로부터 `toString` 같은 키를 상속받습니다

---

맵에는 `sort()`나 `filter()` 같은 배열 메서드가 없습니다. 이를 사용하려면 `Array.from()`이나 스프레드 연산자 `...`로 맵(또는 그 키나 값)을 배열로 변환하세요:
```javascript
let ages = new Map([["Bob", 25], ["Ann", 30]]);
let pairs = Array.from(ages);
console.log(pairs);
// [ [ 'Bob', 25 ], [ 'Ann', 30 ] ] 출력
let names = [...ages.keys()];
console.log(names);
// [ 'Bob', 'Ann' ] 출력
let values = [...ages.values()];
console.log(values);
// [ 25, 30 ] 출력
```
반대 방향의 변환인 `Object.fromEntries(ages)`는 맵을 다시 일반 객체로 바꿉니다.

---

배열과 마찬가지로, 맵에도 모든 쌍에 대해 함수를 호출하는 `forEach()` 메서드가 있습니다.
매개변수의 순서에 주의하세요: 콜백은 **값을 먼저** 받고, 그다음 키를 받습니다:
```javascript
let stock = new Map([["apple", 3], ["pear", 5]]);
stock.forEach((qty, name) => {
  console.log(`${name} x${qty}`);
});
// apple x3 출력
// pear x5 출력
```

---

`delete(key)`는 쌍이 제거되었을 때 `true`를, 키가 없었을 때 `false`를 반환합니다.
**모든** 쌍을 한 번에 제거하려면 `clear()`를 호출하세요:
```javascript
let cart = new Map([["pen", 2], ["ink", 1]]);
console.log(cart.delete("pen"));
// true 출력
console.log(cart.delete("pen"));
// false 출력
cart.clear();
console.log(cart.size);
// 0 출력
```

---

그렇다면 일반 객체 대신 `Map`을 선택해야 하는 것은 언제일까요?
- 키가 실행 중에 추가되고 제거될 때, 키가 문자열이 아닐 때, 또는 `size`와 안정적인 순서가 필요할 때는 **Map**을 사용하세요
- `{ name, email }`처럼 필드 이름이 정해진 고정된 레코드나, 데이터를 JSON으로 변환해야 할 때는 **객체**를 사용하세요. `JSON.stringify()`는 맵의 내용을 무시하기 때문입니다
