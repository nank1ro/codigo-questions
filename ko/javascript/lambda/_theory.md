함수에는 이름이 필요 없습니다. **함수 표현식**은 함수를 값으로 만들며, 이 값은 변수에 저장하고 그 변수를 통해 호출할 수 있습니다:
```javascript
const add = function (a, b) {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
**화살표 함수**는 같은 것을 더 짧게 쓰는 방법입니다: `function` 키워드를 없애고 매개변수 목록과 본문 사이에 "fat arrow" `=>`를 넣습니다:
```javascript
const add = (a, b) => {
  return a + b;
};
console.log(add(2, 3));
// prints 5
```
화살표 함수는 보통 `const`에 저장되므로 이름이 실수로 다시 할당될 수 없고, 다른 함수와 똑같은 방식으로 호출됩니다.

---

화살표 함수는 두 가지 흔한 경우에 더 짧아집니다.
본문이 **단일 표현식**일 때는 중괄호와 `return` 키워드를 생략할 수 있습니다: 표현식의 값이 자동으로 반환됩니다(**암시적 반환**):
```javascript
const add = (a, b) => a + b;
console.log(add(2, 3));
// prints 5
```
매개변수가 **정확히 하나**일 때는 그 주위의 괄호도 생략할 수 있습니다:
```javascript
const double = n => n * 2;
console.log(double(4));
// prints 8
```
매개변수가 없거나 두 개 이상일 때는 괄호가 필요합니다: `() => 42`와 `(a, b) => a + b`.

---

암시적 반환에는 한 가지 함정이 있습니다. 본문이 `{`로 시작하는 화살표 함수는 객체 리터럴이 아니라 항상 **블록 본문**으로 읽힙니다:
```javascript
const make = (name) => { name: name };
console.log(make("Ana"));
// prints undefined
```
여기서 `{ name: name }`은 레이블 `name:`과 그 뒤의 표현식 `name`을 담고 있는 블록입니다. 아무것도 반환되지 않으므로 호출 결과는 `undefined`입니다.
한 줄에서 객체 리터럴을 반환하려면 JavaScript가 표현식으로 취급하도록 **괄호**로 감싸세요:
```javascript
const make = (name) => ({ name: name });
console.log(make("Ana"));
// prints { name: 'Ana' }
```

---

객체 리터럴을 괄호로 감싸는 것은 한 줄짜리 화살표 함수로 객체를 만드는 표준적인 방법입니다. 예를 들어 몇 개의 값을 레코드로 바꿀 때 그렇습니다:
```javascript
const user = (name, age) => ({ name: name, age: age });
console.log(user("Ana", 30).age);
// prints 30
```
매개변수가 없는 화살표 함수는 빈 괄호 쌍 `()`으로 시작합니다:
```javascript
const empty = () => ({});
console.log(empty());
// prints {}
```

---

화살표 함수는 **콜백**으로 사용될 때 진가를 발휘합니다. 콜백이란 다른 함수에 인수로 전달되는 함수입니다. 배열 메서드가 가장 흔한 예입니다.
`map(callback)`은 모든 요소에 대한 콜백의 결과를 담은 새 배열을 반환하고, `filter(callback)`은 콜백이 `true`를 반환하는 요소만 담은 새 배열을 반환합니다:
```javascript
const numbers = [1, 2, 3, 4];
console.log(numbers.map((n) => n * 10));
// prints [ 10, 20, 30, 40 ]
console.log(numbers.filter((n) => n > 2));
// prints [ 3, 4 ]
```
둘 다 새 배열을 반환하고 원본을 그대로 두므로 체이닝할 수 있습니다: `numbers.filter(...).map(...)`.

---

콜백을 받는 배열 메서드가 두 가지 더 있습니다.
`forEach(callback)`는 요소마다 콜백을 한 번씩 호출하고 아무것도 반환하지 않습니다. 출력 같은 부수 효과를 위해 사용하세요.
`reduce(callback, initialValue)`는 배열을 하나의 값으로 접어 나갑니다. 콜백은 지금까지 누적된 값과 현재 요소를 받아 새로운 누적 값을 반환합니다:
```javascript
const numbers = [1, 2, 3];
numbers.forEach((n) => console.log(n));
// prints 1, 2 and 3 on three lines
const total = numbers.reduce((sum, n) => sum + n, 0);
console.log(total);
// prints 6
```

---

`sort(compare)`는 두 요소를 받아 첫 번째가 먼저 와야 하면 음수를, 두 번째가 먼저 와야 하면 양수를, 같으면 `0`을 반환하는 콜백을 사용해 배열을 제자리에서 정렬합니다. 숫자의 경우 `(a, b) => a - b`는 오름차순으로, `(a, b) => b - a`는 내림차순으로 정렬합니다.
`find(callback)`은 콜백이 `true`를 반환하는 첫 번째 요소를 반환하며, 없으면 `undefined`를 반환합니다:
```javascript
const scores = [50, 90, 70];
scores.sort((a, b) => a - b);
console.log(scores);
// prints [ 50, 70, 90 ]
console.log(scores.find((s) => s > 60));
// prints 70
```

---

화살표 함수의 매개변수는 일반 함수 매개변수와 같은 기능을 지원합니다.
인수가 생략되거나 `undefined`일 때는 **기본값**이 사용됩니다:
```javascript
const greet = (name = "World") => `Hello, ${name}!`;
console.log(greet());
// prints Hello, World!
console.log(greet("Ana"));
// prints Hello, Ana!
```
기본값이 있는 매개변수는 하나뿐인 경우에도 항상 괄호가 필요합니다: `name = "World" => ...`은 문법 오류입니다.

---

**나머지 매개변수** `...name`은 몇 개든 인수를 배열로 모으며, 화살표 함수에서도 동작합니다:
```javascript
const count = (...items) => items.length;
console.log(count("a", "b", "c"));
// prints 3
```
일반 함수에는 받은 모든 인수를 담고 있는 숨겨진 배열 유사 객체 `arguments`도 있습니다. 화살표 함수에는 **없습니다**: 화살표 안에서 `arguments`는 둘러싼 함수의 `arguments`를 가리키거나 아예 존재하지 않습니다. 화살표 함수에서 "모든 인수"가 필요하다면 나머지 매개변수를 사용하세요.

---

함수는 그 범위의 실행이 끝난 뒤에도 자신이 **생성된** 범위의 변수를 기억합니다. 이를 **클로저**라고 합니다.
고전적인 예는 카운터 만들기입니다: `makeCounter`를 호출할 때마다 새로운 `count`가 만들어지고, 그 같은 `count`를 계속 사용하는 화살표 함수가 반환됩니다:
```javascript
const makeCounter = () => {
  let count = 0;
  return () => {
    count += 1;
    return count;
  };
};
const next = makeCounter();
console.log(next());
// prints 1
console.log(next());
// prints 2
```
다른 누구도 `count`를 읽거나 초기화할 수 없습니다: `count`는 반환된 함수 안에만 존재합니다. `makeCounter()`를 다시 호출하면 자체적인 `count`를 가진 독립적인 카운터가 만들어집니다.

---

함수는 값이므로, 화살표 함수는 **다른 화살표 함수를 반환**할 수 있습니다. 두 화살표를 체이닝하는 것은 함수를 만들어 내는 함수를 간결하게 쓰는 방법입니다:
```javascript
const makeAdder = (amount) => (n) => n + amount;
const addTen = makeAdder(10);
console.log(addTen(5));
// prints 15
console.log(makeAdder(1)(5));
// prints 6
```
왼쪽에서 오른쪽으로 읽어 보세요: `makeAdder`는 `amount`를 받아 `(n) => n + amount`, 즉 클로저를 통해 `amount`를 붙잡아 두는 화살표 함수를 반환합니다. `makeAdder(1)(5)`는 반환된 함수를 즉시 호출합니다.
