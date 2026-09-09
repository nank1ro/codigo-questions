JavaScript에서 함수는 **값**입니다. 변수에 저장하고, 배열에 넣고, 다른 함수에 인자로 전달할 수 있습니다. 함수를 인자로 받거나 함수를 반환하는 함수를 **고차 함수**라고 합니다. 전달된 함수는 **콜백**이라고 부르는데, 받은 쪽이 필요할 때 *다시 호출하기* 때문입니다:
```javascript
function shout(text) {
  return text.toUpperCase() + "!";
}
function twice(fn, value) {
  return fn(fn(value));
}
console.log(twice(shout, "hi"));
// prints HI!!
```
`shout`이 **괄호 없이** 전달된다는 점에 주목하세요. `twice(shout, "hi")`는 함수 자체를 넘기지만, `twice(shout("hi"), "hi")`는 먼저 `shout`을 호출해 그 결과인 문자열 `"HI!"`를 넘기게 되며, 문자열은 호출할 수 없습니다.

---

고차 함수는 *각 요소로 무엇을 할지*와 *요소를 어떻게 순회할지*를 분리해 줍니다. 순회하는 부분은 한 번만 작성하고, 나머지는 콜백이 결정합니다:
```javascript
function each(items, action) {
  for (let i = 0; i < items.length; i++) {
    action(items[i]);
  }
}
each(["a", "b"], (letter) => console.log(letter));
// prints a and b on two lines
```
콜백은 한 번에 요소 하나를 받습니다. 위처럼 인라인으로 쓴 화살표 함수일 수도 있고, 변수에 저장된 어떤 함수든 될 수 있습니다. 다음에 배울 내장 배열 메서드도 내부적으로는 정확히 이렇게 동작합니다.

---

내장 `map`은 `transform`이 하는 일을 합니다. 모든 요소에 대해 콜백을 호출하고 그 결과를 **새 배열**에 모읍니다. `forEach`도 모든 요소에 대해 콜백을 호출하지만 아무것도 모으지 않고 항상 `undefined`를 반환합니다. 출력처럼 부수 효과가 필요할 때만 사용하세요:
```javascript
const prices = [5, 10];
const doubled = prices.map((p) => p * 2);
prices.forEach((p) => console.log(p));
// prints 5 and 10 on two lines
console.log(doubled);
// prints [ 10, 20 ]
```
흔한 실수는 `forEach`의 결과를 저장하거나 그 뒤에 다른 메서드를 이어 붙이는 것입니다. `undefined`를 반환하므로 이어 붙일 것이 없습니다. 기준은 간단합니다. 새 값이 필요하면 `map`, 무언가를 *하기만* 하면 될 때는 `forEach`를 쓰세요.

---

또 다른 두 고차 메서드가 일상적인 필요의 대부분을 해결합니다.
`filter(callback)`는 콜백이 `true`를 반환한 요소만 담은 새 배열을 반환합니다. 이렇게 예/아니오로 답하는 콜백을 **술어**라고 합니다.
`reduce(callback, initialValue)`는 모든 요소를 하나의 값으로 합칩니다. 콜백은 **누적자**(지금까지의 결과)와 현재 요소를 받아 새 누적자를 반환합니다. `reduce`의 두 번째 인자가 시작 누적자입니다:
```javascript
const numbers = [3, 8, 5];
console.log(numbers.filter((n) => n > 4));
// prints [ 8, 5 ]
console.log(numbers.reduce((sum, n) => sum + n, 0));
// prints 16
```
`filter`와 `map`은 배열을 반환하므로 이어 붙인 뒤 `reduce`로 마무리할 수 있습니다: `numbers.filter(...).map(...).reduce(...)`.

---

세 가지 메서드가 술어로 배열에 대한 질문에 답합니다:
- `find(predicate)`는 술어가 `true`가 되는 **첫 번째** 요소를 반환하고, 없으면 `undefined`를 반환합니다
- `some(predicate)`는 **적어도 하나**의 요소가 술어를 만족하면 `true`를 반환합니다
- `every(predicate)`는 **모든** 요소가 만족하면 `true`를 반환합니다 (빈 배열에도 `true`)
```javascript
const scores = [72, 45, 90];
console.log(scores.find((s) => s < 60));
// prints 45
console.log(scores.some((s) => s === 90), scores.every((s) => s >= 60));
// prints true false
```
셋 다 답이 정해지는 즉시 멈추므로 필요한 것보다 많은 요소를 보지 않습니다.

---

`sort(compare)`는 두 요소를 받는 콜백을 사용해 배열을 **제자리에서** 정렬합니다. 콜백은 첫 번째가 앞에 와야 하면 음수를, 두 번째가 앞에 와야 하면 양수를, 같으면 `0`을 반환합니다. 숫자의 경우 `(a, b) => a - b`는 오름차순, `(a, b) => b - a`는 내림차순으로 정렬합니다.
비교 함수가 없으면 `sort()`는 각 요소를 **문자열**로 바꿔 한 글자씩 비교하므로, `"1"`이 `"9"`보다 작아서 `10`이 `9`보다 앞에 옵니다:
```javascript
console.log([10, 9, 1].sort());
// prints [ 1, 10, 9 ]
console.log([10, 9, 1].sort((a, b) => a - b));
// prints [ 1, 9, 10 ]
```
`sort`는 배열을 변경하므로 원래 순서도 필요하다면 복사본을 정렬하세요: `[...numbers].sort(...)`. 문자열에는 텍스트를 알파벳순으로 정렬하는 `(a, b) => a.localeCompare(b)`를 비교 함수로 사용하세요.

---

비교 함수는 요소의 어떤 부분이든 볼 수 있으므로, 객체 배열은 그 속성 하나를 비교하는 것만으로 그 속성 기준으로 정렬됩니다:
```javascript
const items = [{ name: "b", size: 3 }, { name: "a", size: 1 }];
const bySize = [...items].sort((x, y) => x.size - y.size);
console.log(bySize.map((item) => item.name));
// prints [ 'a', 'b' ]
```
복사본을 정렬하면 `items`는 원래 순서 그대로 남습니다.

---

고차 함수는 함수를 **반환**할 수도 있습니다. 반환된 함수는 바깥 함수가 끝난 뒤에도 자신이 만들어진 곳의 변수를 기억합니다. 이것을 **클로저**라고 합니다.
```javascript
function makeMultiplier(factor) {
  return function (n) {
    return n * factor;
  };
}
const triple = makeMultiplier(3);
console.log(triple(5));
// prints 15
console.log(makeMultiplier(10)(5));
// prints 50
```
`makeMultiplier`를 호출할 때마다 각자의 `factor`를 가진 새 함수가 만들어집니다. 이렇게 하나의 틀에서 비슷한 함수들의 가족을 만들 수 있습니다. 같은 것을 화살표 함수로도 쓸 수 있습니다: `const makeMultiplier = (factor) => (n) => n * factor;`.

---

클로저는 값의 복사본이 아니라 변수와의 **살아 있는** 연결을 유지합니다. 같은 호출에서 여러 함수가 만들어지면 그들은 같은 변수를 공유하고, 하나를 통해 이루어진 변경은 다른 함수에도 보입니다:
```javascript
function makeCounter() {
  let count = 0;
  return {
    increment: () => { count += 1; },
    value: () => count,
  };
}
const counter = makeCounter();
counter.increment();
counter.increment();
console.log(counter.value());
// prints 2
```
그 두 함수를 거치지 않고는 밖에서 아무도 `count`를 읽거나 되돌릴 수 없습니다. 이 변수는 **비공개**입니다. `makeCounter()`를 다시 호출하면 완전히 별개인 `count`가 만들어집니다.

---

함수가 값이기 때문에, 두 함수를 새로운 하나로 **결합**하는 고차 함수를 작성할 수 있습니다. `compose(f, g)`는 먼저 `g`를 적용하고 그 결과에 `f`를 적용하는 함수를 반환하며, 이는 수학 표기 *f(g(x))*와 같습니다:
```javascript
const compose = (f, g) => (x) => f(g(x));
const trim = (s) => s.trim();
const shout = (s) => s.toUpperCase();
const clean = compose(shout, trim);
console.log(clean("  hi  "));
// prints HI
```
순서가 중요합니다. `compose(f, g)`는 `g`를 먼저 실행하고 그다음 `f`를 실행합니다. 이렇게 작은 함수들을 이어 붙여 프로그램을 만드는 것을 **함수 합성**이라고 합니다.

---

함수를 반환하는 함수는 콜백을 **맞춰 쓰는** 자연스러운 방법이기도 합니다. 술어가 하나 있는데 `filter`에는 그 반대가 필요하다고 해 봅시다. 다시 작성하는 대신 감싸면 됩니다:
```javascript
const isLong = (word) => word.length > 4;
const isShort = (word) => !isLong(word);
console.log(["tree", "forest"].filter(isShort));
// prints [ 'tree' ]
```
일반적인 `not(predicate)`는 어떤 술어에 대해서도 이 일을 합니다. 같은 인자로 `predicate`를 호출하고 결과를 `!`로 뒤집는 새 함수를 반환합니다. `filter`, `find`, `some`, `every`의 술어는 요소를 첫 번째 인자로 받으므로, 래퍼는 그 값 하나만 전달하면 됩니다.

---

`reduce`의 누적자는 숫자일 필요가 없습니다. 문자열, 배열, 객체일 수도 있습니다. 빈 객체 `{}`에서 시작하면 한 번의 순회로 세거나 묶을 수 있습니다. 콜백에서 반드시 **누적자를 반환**하세요. 그러지 않으면 다음 단계가 `undefined`를 받습니다:
```javascript
const votes = ["yes", "no", "yes"];
const tally = votes.reduce((acc, vote) => {
  acc[vote] = (acc[vote] ?? 0) + 1;
  return acc;
}, {});
console.log(tally);
// prints { yes: 2, no: 1 }
```
`acc[vote] ?? 0`은 현재 개수를 읽고, 그 키가 아직 없으면 `0`을 읽습니다.

---

모든 함수에는 일부를 미리 고정한 **새** 함수를 반환하는 `bind` 메서드가 있습니다. 첫 번째 인자는 새 함수의 `this`가 되고, 나머지 인자는 새 함수를 호출할 때 넘기는 인자들 앞에 놓입니다(**부분 적용**):
```javascript
function multiply(a, b) {
  return a * b;
}
const double = multiply.bind(null, 2);
console.log(double(21));
// prints 42
```
`this`를 고정하는 것은 메서드에서 중요합니다. 메서드를 객체 밖으로 꺼내 단독으로 호출하면 `this`는 더 이상 그 객체를 가리키지 않으므로 `this.name`은 `undefined`가 됩니다. `bind`는 그것을 객체에 묶어 둡니다:
```javascript
const user = {
  name: "Ana",
  hello() { return `Hi ${this.name}`; },
};
const loose = user.hello;
console.log(loose());
// prints Hi undefined
const bound = user.hello.bind(user);
console.log(bound());
// prints Hi Ana
```
원래 함수는 절대 변경되지 않습니다. `bind`는 항상 새 함수를 만들며, 그 `name`은 원래 이름 앞에 `bound `가 붙은 것입니다.

---

실제 프로그램은 이 메서드들을 **파이프라인**으로 결합합니다. 관심 있는 요소를 걸러내고, 필요한 값으로 변환하고, 하나의 결과로 축약합니다. 중간 배열을 상수에 담아 두면 각 단계가 읽기 쉬워지고 재사용할 수도 있습니다:
```javascript
const adults = people.filter((p) => p.age >= 18);
const names = adults.map((p) => p.name);
const totalAge = adults.reduce((sum, p) => sum + p.age, 0);
```
`names.join(", ")`은 문자열 배열을 요소가 쉼표와 공백으로 구분된 하나의 문자열로 바꿉니다.

---

클로저는 반환된 함수가 호출 사이에 **비공개 상태**를 유지하게 해 줍니다. 이렇게 만든 대표적인 도구가 `once(fn)`입니다. 반환된 함수는 처음 호출될 때만 `fn`을 실행하고 결과를 기억한 뒤, 이후 호출에서는 `fn`을 다시 실행하지 않고 같은 결과를 반환합니다:
```javascript
let calls = 0;
const init = once(() => {
  calls += 1;
  return "ready";
});
console.log(init(), init(), calls);
// prints ready ready 1
```
래퍼에는 비공개 변수 두 개가 필요합니다. `fn`이 이미 실행됐는지 여부와 저장된 결과입니다. 둘 다 클로저 안에 있어 바깥에서는 보이지 않습니다. 래퍼의 모든 인자를 `fn`에 넘기려면 나머지 매개변수 `(...args)`로 래퍼를 선언하고 `fn(...args)`를 호출하세요.

---

모든 것이 `groupBy(items, keyFn)`으로 모입니다. 각 요소의 **그룹 키**를 정하는 콜백을 받아, 각 키에 그 키를 가진 요소들의 배열을 대응시킨 객체를 반환하는 고차 함수입니다. 객체를 누적자로 쓰는 `reduce`가 모든 일을 처리합니다:
```javascript
const byInitial = groupBy(["hi", "yo", "hey"], (w) => w[0]);
console.log(byInitial);
// prints { h: [ 'hi', 'hey' ], y: [ 'yo' ] }
```
각 요소마다 키를 계산하고, 그 키의 배열이 아직 없으면 만들고(`acc[key] ?? []`), 요소를 넣은 뒤 누적자를 반환하세요. `keyFn`을 호출하는 쪽이 정하므로, 같은 함수로 단어를 첫 글자별로, 사람을 도시별로, 숫자를 홀짝별로 묶을 수 있습니다.
