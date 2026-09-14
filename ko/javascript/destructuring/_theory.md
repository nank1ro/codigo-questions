인덱스를 하나씩 사용해 배열에서 값을 읽어내는 것은 번거롭습니다:
```javascript
const point = [3, 7];
const x = point[0];
const y = point[1];
```
**구조 분해 할당(Destructuring)**은 같은 작업을 한 줄로 처리합니다. `=`의 왼쪽에 배열 모습 그대로처럼 생긴 패턴을 작성하면, 그 안의 각 이름이 같은 위치의 요소를 받습니다:
```javascript
const point = [3, 7];
const [x, y] = point;
console.log(x, y);
// prints 3 7
```
패턴이 배열 전체를 덮을 필요는 없습니다: 남는 요소는 단순히 무시되고, 대응되는 요소가 없는 이름은 `undefined`가 됩니다.

---

구조 분해 할당은 배열이 도착하는 바로 그 자리, 즉 함수 인수나 호출 결과에서 가장 유용합니다. 배열을 계속 들고 다니며 여기저기서 인덱스로 접근하는 대신, 한 번 풀어헤쳐 각 부분에 제대로 된 이름을 붙일 수 있습니다:
```javascript
function middle(range) {
    const [start, end] = range;
    return (start + end) / 2;
}
console.log(middle([0, 10]));
// prints 5
```
원본 배열은 복사되거나 변경되지 않으며, 패턴은 배열을 읽기만 합니다.

---

때로는 배열 깊숙이 있는 한 요소만 필요할 때가 있습니다. 패턴에서 위치를 비워 둘 수 있는데, 이때 위치를 구분하는 쉼표는 그대로 유지합니다: 이렇게 비워 둔 위치를 **구멍(hole)**이라고 하며, 이름을 붙이지 않은 채 해당 요소를 건너뜁니다:
```javascript
const rgb = [255, 128, 64];
const [, , blue] = rgb;
console.log(blue);
// prints 64
```
세어야 할 것은 이름이 아니라 쉼표입니다: 쉼표 하나하나가 앞에 이름이 있든 없든 패턴을 한 위치 앞으로 나아가게 합니다.

---

배열이 항상 패턴이 기대하는 길이만큼 있는 것은 아닙니다. 이름 뒤에 `= value`를 작성하면 **기본값(default)**이 주어지는데, 배열에 그 위치의 값이 없을 때마다 사용됩니다:
```javascript
const size = [1920];
const [width, height = 1080] = size;
console.log(width, height);
// prints 1920 1080
```
기본값은 필요할 때만 평가되므로 함수 호출이어도 되며, 기본값은 마지막 위치뿐 아니라 어떤 위치에든 줄 수 있습니다.

---

패턴은 `const`나 `let` 없이 일반 할당의 왼쪽에 놓일 수도 있는데, 이때는 이미 존재하는 변수에 값을 씁니다. 이렇게 하면 임시 변수 없이 두 값을 맞바꾸는 작업을 한 줄로 처리할 수 있습니다:
```javascript
let a = 1;
let b = 2;
[a, b] = [b, a];
console.log(a, b);
// prints 2 1
```
오른쪽이 먼저 만들어지므로, 할당이 일어나는 시점에는 두 이전 값이 이미 임시 배열 안에 안전하게 들어 있습니다. 앞 줄의 세미콜론에 주의하세요: 세미콜론이 없으면 `[`로 시작하는 줄은 앞에 있는 것의 인덱스로 읽힙니다.

---

객체도 구조 분해 할당할 수 있으며, 이때는 대괄호 대신 중괄호를 사용합니다. 여기서는 위치가 아무 의미가 없습니다: 각 이름은 똑같이 적힌 **키(key)**와 대응됩니다:
```javascript
const user = { name: "Ada", age: 36 };
const { age, name } = user;
console.log(name, age);
// prints Ada 36
```
패턴에서 `age`와 `name`의 순서를 바꿔도 아무것도 달라지지 않으며, 패턴이 언급하지 않는 키는 단순히 남겨집니다. 대응되는 키가 없는 이름은 `undefined`가 됩니다.

---

객체 패턴과 기본값은 배열과 완전히 같은 방식으로 결합되므로, 키가 있을 수도 있고 없을 수도 있는 설정 객체를 깔끔하게 읽는 방법이 됩니다:
```javascript
const options = { theme: "dark" };
const { theme, lang = "en" } = options;
console.log(theme, lang);
// prints dark en
```
패턴 전체가 하나의 문이므로, 함수는 첫 번째 줄에서 인수로부터 필요한 모든 것을 풀어낼 수 있습니다.

---

객체 패턴은 키와 같은 이름으로 변수를 만드는데, 키가 의미를 알 수 없거나 이미 사용 중인 이름이라면 곤란합니다. `key: newName`처럼 작성하면 변수의 **이름을 바꿀(renames)** 수 있습니다:
```javascript
const row = { n: "Ada", y: 1815 };
const { n: name, y: born } = row;
console.log(name, born);
// prints Ada 1815
```
"`n`을 가져와서 `name`이라고 부른다"고 읽으면 됩니다. 콜론은 타입을 선언하는 것이 아니며, `n` 자체는 결코 변수로 만들어지지 않고 `name`만 만들어집니다. 이름이 바뀐 변수에도 그 뒤에 기본값을 쓸 수 있습니다: `{ n: name = "unknown" }`.

---

기본값에는 모두를 놀라게 하는 규칙이 하나 있습니다. **오직** `undefined`에만 적용된다는 것입니다. 존재하는 키에 `null`, `0`, `""`, `false`가 담겨 있으면 그것은 진짜 값이므로, 패턴이 그 값을 가져가고 기본값은 결코 사용되지 않습니다:
```javascript
const { count = 10 } = { count: 0 };
console.log(count);
// prints 0
```
`null`은 API 응답에서 종종 "값 없음"을 의미하지만, 여기서는 `0`과 똑같이 동작합니다. `null`도 대체해야 한다면 먼저 구조 분해 할당을 하고 그 후에 `??`로 대체하세요.

---

키가 다른 객체나 배열을 담고 있다면, 패턴은 그대로 이어져 그 모양까지 기술할 수 있습니다:
```javascript
const user = { name: "Ada", address: { city: "London" } };
const { address: { city } } = user;
console.log(city);
// prints London
```
그 줄이 무엇을 만드는지 주의하세요: `address: { city }`는 "`address` 안으로 들어가라"는 뜻이지 "`address`를 주라"는 뜻이 아니므로, `city`만 변수가 됩니다. 둘 다 얻으려면 키를 두 번 언급하세요: `const { address, address: { city } } = user;`. 배열 패턴과 객체 패턴은 `{ tags: [first] }`처럼 서로 자유롭게 중첩됩니다.

---

배열의 머리를 꺼내고 나머지 꼬리를 유지하는 일은 워낙 흔한 필요라서 패턴에만 있는 전용 문법이 있습니다. 마지막 이름 앞의 점 세 개는 그 이름을 **나머지 요소(rest element)**로 만들고, 남은 모든 요소를 완전히 새로운 배열로 모읍니다:
```javascript
const queue = ["a", "b", "c"];
const [next, ...waiting] = queue;
console.log(next, waiting);
// prints a [ 'b', 'c' ]
```
나머지 요소는 패턴에서 맨 마지막에 와야 하며 기본값을 가질 수 없습니다: 남은 것이 없으면 단순히 빈 배열이 됩니다.

---

객체 패턴에도 나머지 요소가 있으며, 여기서는 패턴이 언급하지 않은 모든 키를 새로운 객체로 모읍니다:
```javascript
const user = { id: 1, name: "Ada", city: "London" };
const { id, ...profile } = user;
console.log(profile);
// prints { name: 'Ada', city: 'London' }
```
이것은 객체에서 하나의 키를 뺀 복사본을 만드는 가장 짧은 방법입니다: 원본은 결코 건드려지지 않으며, 나머지 객체는 남은 값들을 담은 완전히 새로운 객체입니다.

---

함수 선언에서 패턴이 매개변수 이름을 대신할 수 있으므로, 호출이 이루어지는 순간 풀어헤치기가 일어납니다:
```javascript
function area({ width, height }) {
    return width * height;
}
console.log(area({ width: 4, height: 3 }));
// prints 12
```
본문 안에는 객체 변수가 전혀 없고 `width`와 `height`만 있습니다. 호출자는 하나의 객체를 전달하지만, 시그니처가 함수가 읽는 키가 정확히 무엇인지 문서화하며, 키는 어떤 순서로 와도 됩니다.

---

기본값이 있는 구조 분해 매개변수는 깔끔한 옵션 객체를 만들지만, 호출자가 아무것도 전달하지 않으면 여전히 깨집니다: `undefined`에서 키를 읽으면 `TypeError`가 발생합니다. 패턴 전체에 `{}` 기본값을 주면 해결됩니다:
```javascript
function createUser({ name = "guest", admin = false } = {}) {
    return `${name}/${admin}`;
}
console.log(createUser());
// prints guest/false
```
그 줄은 바깥부터 안으로 읽으세요: 인수가 없을 때 `= {}`가 빈 객체를 공급하고, 그다음 각 안쪽 기본값이 자기 키를 채웁니다.

---

`Object.entries(obj)`는 객체를 `[key, value]` 쌍의 배열로 바꿉니다. `for...of` 루프의 머리에 배열 패턴을 놓으면, 루프가 도는 동안 매 쌍이 풀어헤쳐집니다:
```javascript
const ages = { ada: 36, bob: 41 };
for (const [name, age] of Object.entries(ages)) {
    console.log(`${name} is ${age}`);
}
// prints ada is 36
// prints bob is 41
```
이것이 객체를 순회하는 읽기 좋은 방법입니다: 인덱스도, 조회도 없이 관심 있는 두 이름만 있습니다. `Object.keys`와 `Object.values`는 각각 한쪽만 주고, `Object.entries`는 둘 다 줍니다.

---

지금까지 본 모든 것은 하나의 문법에 속하므로 조각들은 자유롭게 결합됩니다: 객체 패턴은 다른 객체 패턴을 중첩할 수 있고, 그 안에는 기본값이 있는 이름이 바뀐 키가, 그 옆에는 나머지 요소로 끝나는 배열 패턴이 들어갈 수 있습니다. 한 줄이면 함수가 기대하는 전체 모양을 기술합니다:
```javascript
function head({ title, tags: [main, ...extra] }) {
    return `${title} [${main}] +${extra.length}`;
}
console.log(head({ title: "Post", tags: ["js", "web", "dev"] }));
// prints Post [js] +2
```
읽기 좋게 유지하세요: 두어 줄에 더 이상 맞지 않는 패턴은 대개 함수가 너무 많은 것을 요구하고 있다는 신호입니다.
