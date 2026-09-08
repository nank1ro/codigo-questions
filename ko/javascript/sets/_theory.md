**세트**는 **고유한** 값들의 컬렉션입니다: 각 값은 최대 한 번만 나타날 수 있으며, 위치로 값에 접근할 수 있는 인덱스가 없습니다.
세트는 값이 *몇 번* 또는 *어떤 순서로* 있는지가 아니라, *어떤* 값이 있는지에만 관심이 있을 때 유용합니다.
`new Set()`으로 빈 세트를 만들고, `add(value)`로 값을 추가하고, `has(value)`로 값이 있는지 확인합니다:
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
// prints 2
tags.delete("css");
console.log(tags.size);
// prints 1
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
// prints 3
```
**스프레드** 연산자 `...`는 반대로 세트를 다시 배열로 바꿔줍니다:
```javascript
let unique = [...distinct];
console.log(unique);
// prints [ 1, 2, 3 ]
```
`Array.from(distinct)`도 같은 일을 합니다.

---

세트는 값이 추가된 순서를 기억하며, `for...of`로 순회할 수 있습니다:
```javascript
let nums = new Set([3, 1, 2]);
for (const n of nums) {
  console.log(n);
}
// prints 3
// prints 1
// prints 2
```
세트에는 모든 값에 대해 함수를 호출하는 `forEach()` 메서드도 있습니다:
```javascript
nums.forEach((n) => console.log(n * 10));
// prints 30
// prints 10
// prints 20
```
