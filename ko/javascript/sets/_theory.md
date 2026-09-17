**세트**는 **고유한** 값들의 컬렉션입니다: 각 값은 최대 한 번만 나타날 수 있으며, 위치로 값에 접근할 수 있는 인덱스가 없습니다.
세트는 값이 *몇 번* 또는 *어떤 순서로* 있는지가 아니라, *어떤* 값이 있는지에만 관심이 있을 때 유용합니다.
`new Set()`으로 빈 세트를 만들고, `add(value)`로 값을 추가하고, `has(value)`로 값이 있는지 확인합니다:
```javascript
let colors = new Set();
colors.add("red");
colors.add("blue");
console.log(colors.has("red"));
// true 출력
console.log(colors.has("green"));
// false 출력
```

---

이미 세트에 있는 값을 추가해도 **아무 일도 일어나지 않습니다**: 중복은 그냥 무시됩니다.
두 가지 더 중요한 것들이 있습니다:
- `delete(value)`는 세트에서 값을 제거합니다
- `size`는 저장된 값의 개수입니다 (프로퍼티이므로 괄호가 없습니다)

```javascript
let tags = new Set();
tags.add("js");
tags.add("css");
tags.add("js");
console.log(tags.size);
// 2 출력
tags.delete("css");
console.log(tags.size);
// 1 출력
```

---

`add()`는 세트 자신을 반환하므로 여러 호출을 체이닝할 수 있습니다:
```javascript
let letters = new Set();
letters.add("a").add("b");
```
체이닝을 하든 안 하든, 이미 존재하는 값은 두 번째로 추가되지 않으므로 `size`는 각 고유한 값을 한 번만 셉니다.

---

배열을 `new Set()`에 전달하면 한 번에 세트를 만들 수 있습니다. 배열 안의 중복은 제거되므로, 이는 배열의 고유한 값을 찾는 가장 빠른 방법입니다:
```javascript
let nums = [1, 2, 2, 3, 3, 3];
let distinct = new Set(nums);
console.log(distinct.size);
// 3 출력
```
**스프레드** 연산자 `...`는 반대로 세트를 다시 배열로 바꿔줍니다:
```javascript
let unique = [...distinct];
console.log(unique);
// [ 1, 2, 3 ] 출력
```
`Array.from(distinct)`도 같은 일을 합니다.

---

세트는 값이 추가된 순서를 기억하며, `for...of`로 순회할 수 있습니다:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// 3 출력
// 1 출력
// 2 출력
```
세트에는 모든 값에 대해 함수를 호출하는 `forEach()` 메서드도 있습니다:
```javascript
nums.forEach((n) => console.log(n * 10));
// 30 출력
// 10 출력
// 20 출력
```

---

`delete(value)`는 값이 제거되었으면 `true`를, 세트에 없었으면 `false`를 반환합니다.
**모든** 값을 한 번에 제거하려면 `clear()`를 호출하세요:
```javascript
let cart = new Set(["pen", "ink"]);
console.log(cart.delete("pen"));
// true 출력
console.log(cart.delete("pen"));
// false 출력
cart.clear();
console.log(cart.size);
// 0 출력
```

---

세트는 `===`와 거의 같은 규칙으로 두 값이 "같은지" 판단합니다 (단, `NaN`은 자기 자신과 같다고 취급됩니다). 문자열과 숫자는 내용을 비교하지만, **객체는 참조로 비교됩니다**: 필드가 동일한 두 객체 리터럴은 서로 다른 두 값입니다.
```javascript
let alice = { name: "Alice" };
let people = new Set();
people.add(alice);
people.add(alice);
console.log(people.size);
// 1 출력
people.add({ name: "Alice" });
console.log(people.size);
// 2 출력
```
정확히 같은 객체를 다시 추가하는 경우에만 무시됩니다.

---

스프레드와 `filter()`를 결합하면 집합론의 고전적인 연산을 할 수 있습니다. 각각은 **새로운** 컬렉션을 만들고 원본은 그대로 둡니다:
- **합집합**, `a`, `b` 또는 둘 다에 있는 모든 값: `new Set([...a, ...b])`
- **교집합**, **둘 다**에 있는 값만: `[...a].filter((x) => b.has(x))`
- **차집합**, `a`의 값 중 `b`에 **없는** 값: `[...a].filter((x) => !b.has(x))`

```javascript
let a = new Set([1, 2, 3]);
let b = new Set([3, 4]);
console.log([...new Set([...a, ...b])]);
// [ 1, 2, 3, 4 ] 출력
console.log([...a].filter((x) => b.has(x)));
// [ 3 ] 출력
console.log([...a].filter((x) => !b.has(x)));
// [ 1, 2 ] 출력
```
최신 JavaScript 엔진은 세트에 직접 `a.union(b)`, `a.intersection(b)`, `a.difference(b)`도 제공하지만, 스프레드와 filter 버전은 어디서나 동작합니다.

---

`Map`과 같은 인터페이스를 유지하기 위해, 세트도 이터레이터 메서드 `values()`, `keys()`, `entries()`를 제공합니다.
세트에는 키가 없으므로 `keys()`는 `values()`의 또 다른 이름일 뿐이며, `entries()`는 각 값을 `[value, value]` 쌍으로 **두 번** 반환합니다:
```javascript
let letters = new Set(["a", "b"]);
console.log([...letters.values()]);
// [ 'a', 'b' ] 출력
console.log([...letters.entries()]);
// [ [ 'a', 'a' ], [ 'b', 'b' ] ] 출력
```
실제로는 이 메서드들이 거의 필요하지 않습니다: `for...of`와 스프레드가 이미 값을 직접 순회하기 때문입니다.

---

`new Set()`은 배열뿐만 아니라 모든 **이터러블**을 받습니다. 문자열도 한 글자씩 순회할 수 있으므로, 텍스트의 고유한 문자들을 얻을 수 있습니다:
```javascript
let letters = new Set("hello");
console.log([...letters]);
// [ 'h', 'e', 'l', 'o' ] 출력
```
