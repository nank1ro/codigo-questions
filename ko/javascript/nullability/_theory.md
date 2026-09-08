JavaScript에는 "여기에 값이 없다"고 말하는 두 가지 서로 다른 방식이 있습니다.
`undefined`는 값이 **한 번도 제공되지 않았다**는 뜻입니다. 값 없이 선언된 변수는 `undefined`를 가지며, 객체에 존재하지 않는 프로퍼티도 마찬가지입니다:
```javascript
let city;
console.log(city);
// prints undefined
const user = { name: "Ana" };
console.log(user.age);
// prints undefined
```
`null`은 "비어 있고, 그것을 알고 있다"고 말하기 위해 **여러분이** 의도적으로 할당하는 값입니다:
```javascript
let owner = null;
console.log(owner);
// prints null
```
즉, `undefined`는 보통 무언가 빠져 있다고 언어가 알려주는 것이고, `null`은 프로그래머가 무언가를 의도적으로 비워 두었다고 선언하는 것입니다.

---

함수는 두 가지 상황이 더 `undefined`를 만들어 냅니다.
함수를 선언된 것보다 **적은 수의 인자**로 호출하면, 빠진 매개변수는 `undefined`를 가집니다:
```javascript
function greet(name) {
  console.log(name);
}
greet();
// prints undefined
```
함수가 **`return` 없이** (또는 `return;`만으로) 끝나면, 호출 결과는 `undefined`입니다:
```javascript
function log(message) {
  console.log(message);
}
const result = log("hi");
console.log(result);
// prints hi, then undefined
```
`null`을 명시적으로 전달하는 것은 인자를 생략하는 것과 같지 않다는 점에 주의하세요: `greet(null)`은 `null`을 출력하는데, `null`은 함수에 전달된 실제 값이기 때문입니다.

---

`typeof` 연산자는 값의 타입을 문자열로 반환합니다. `undefined`에 대해서는 예상대로 `"undefined"`라고 답합니다:
```javascript
let city;
console.log(typeof city);
// prints undefined
```
그러나 `null`에 대해서는 `"object"`라고 답합니다. 이것은 너무 많은 코드가 이 동작에 의존하기 때문에 한 번도 수정되지 않은, JavaScript 첫 버전의 버그입니다:
```javascript
console.log(typeof null);
// prints object
```
따라서 `typeof`는 `undefined`를 감지하는 신뢰할 수 있는 방법이지만, `null`은 그렇지 않습니다. `null`을 확인하려면 직접 비교하세요: `value === null`.

---

`null`과 `undefined`는 서로 비교하면 어떻게 될까요? 연산자에 따라 다릅니다.
**느슨한** 동등 비교 `==`는 이 둘을 같은 것으로 취급하고, `0`, `""`, `false`를 포함한 다른 모든 값과는 다른 것으로 봅니다:
```javascript
console.log(null == undefined);
// prints true
console.log(null == 0, undefined == "");
// prints false false
```
**엄격한** 동등 비교 `===`는 타입까지 비교하는데, `null`과 `undefined`는 타입이 다릅니다:
```javascript
console.log(null === undefined);
// prints false
console.log(null === null);
// prints true
```

---

대부분의 경우 두 "값 없음" 표시 중 *어느 쪽*을 받았는지는 중요하지 않습니다. 그저 값이 있는지 없는지 알고 싶을 뿐입니다.
`null == undefined`는 `true`이고 `null`과 느슨하게 같은 다른 값은 없으므로, `value == null` 비교는 **둘**을 한 번에 잡아내는 표준 관용구입니다:
```javascript
function show(value) {
  if (value == null) {
    return "missing";
  }
  return "present";
}
console.log(show(null), show(undefined));
// prints missing missing
console.log(show(0), show(""));
// prints present present
```
이것은 `==`가 `===`보다 선호되는 유일한 경우입니다: `value === null || value === undefined`라고 써도 정확히 같은 일을 하지만 더 길어질 뿐입니다.
`0`, `""`, `false` 같은 값은 `null`이 *아닙니다*: 이것들은 우연히 falsy한 실제 값들입니다.

---

`null`이나 `undefined`의 프로퍼티를 읽으려고 하면 프로그램을 멈추는 에러가 발생합니다:
```javascript
const user = { name: "Ana" };
console.log(user.address.city);
// TypeError: Cannot read properties of undefined (reading 'city')
```
`user.address`는 `undefined`이고, `undefined`는 프로퍼티가 없습니다. **옵셔널 체이닝** 연산자 `?.`가 이것을 해결합니다: 왼쪽의 값이 `null`이나 `undefined`이면 전체 표현식이 중단되고, 에러를 던지는 대신 `undefined`로 평가됩니다:
```javascript
console.log(user.address?.city);
// prints undefined
console.log(user.name?.length);
// prints 3
```
왼쪽에 실제 값이 있으면 `?.`는 일반 `.`과 똑같이 동작합니다. 여러 개를 연결할 수도 있습니다: `user.address?.street?.name`은 체인 중 어느 하나라도 빠져 있으면 `undefined`를 반환합니다.

---

옵셔널 체이닝은 점 프로퍼티에만 국한되지 않습니다. 두 가지 형태가 더 있습니다.
`?.[]`는 왼쪽에 값이 있을 때만 요소나 계산된 키를 읽습니다:
```javascript
const post = { tags: ["js", "node"] };
console.log(post.tags?.[0]);
// prints js
const empty = {};
console.log(empty.tags?.[0]);
// prints undefined
```
`?.()`는 함수가 존재할 때만 호출하며, 선택적인 콜백에 유용합니다:
```javascript
const task = { name: "build" };
task.onDone?.();
// nothing happens, no error
```
어떤 형태에서든 검사는 `?.` **바로 앞의** 값에 적용됩니다: `post?.tags?.[0]`은 `post` 자체가 `null`이나 `undefined`일 때도 안전합니다.

---

값이 없을 수 있다는 것을 알고 나면 보통 그 자리에 **기본값**을 넣고 싶어집니다. 두 연산자가 이 일을 하며, 무엇을 "없음"으로 간주하는지가 다릅니다.
`a || b`는 `a`가 **falsy**일 때마다 `b`를 반환합니다: `null`과 `undefined`뿐만 아니라 `0`, `""`, `false`, `NaN`도 마찬가지입니다.
**널 병합** 연산자 `a ?? b`는 `a`가 `null`이나 `undefined`일 때만 `b`를 반환하고, 다른 모든 값은 그대로 유지합니다:
```javascript
const count = 0;
console.log(count || 10);
// prints 10
console.log(count ?? 10);
// prints 0
let name;
console.log(name ?? "Guest");
// prints Guest
```
`0`, `""`, `false`가 유지해야 할 정당한 값일 때는 `??`를, 정말로 모든 falsy 값을 바꾸고 싶을 때는 `||`를 사용하세요.

---

아주 흔한 패턴은 "이 프로퍼티가 아직 설정되지 않은 경우에만 채우기"입니다. `??`로 쓰면 이름을 반복하게 됩니다:
```javascript
options.timeout = options.timeout ?? 1000;
```
**널 병합 할당** 연산자 `??=`는 이것을 한 단계로 처리합니다: 왼쪽이 현재 `null`이나 `undefined`일 때만 오른쪽을 할당하고, 다른 값은 그대로 둡니다:
```javascript
const options = { retries: 0 };
options.retries ??= 3;
options.timeout ??= 1000;
console.log(options);
// prints { retries: 0, timeout: 1000 }
```
`retries`는 `0`이 nullish가 아니므로 `0`으로 유지되고, `timeout`은 존재하지 않았으므로 `1000`을 받습니다. 같은 아이디어가 `||`에는 `||=`로 존재하며, 이것은 모든 falsy 값을 덮어씁니다.

---

**기본 매개변수**는 호출자가 값을 제공하지 않을 때 매개변수에 값을 줍니다. 규칙은 정확합니다: 기본값은 인자가 `undefined`일 때만 사용되며, 인자를 생략하는 것도 여기에 포함됩니다. `null`을 전달하면 `null`은 값이므로 기본값이 트리거되지 **않습니다**:
```javascript
function repeat(text, times = 2) {
  return text.repeat(times);
}
console.log(repeat("ab"));
// prints abab
console.log(repeat("ab", undefined));
// prints abab
console.log(repeat("ab", null));
// prints an empty string, because null is converted to 0
```
기본 매개변수는 `undefined` 규칙을 따르는 반면, `??`는 `null`과 `undefined`를 모두 다룹니다: 함수가 호출되는 방식에 맞는 것을 선택하세요.

---

옵셔널 체이닝과 `== null` 검사는 잘 어울립니다: 체인은 에러를 던지지 않고 중첩된 값을 읽고, 검사는 결과가 없을 때 무엇을 할지 결정합니다:
```javascript
function cityOf(user) {
  if (user?.address?.city == null) {
    return "unknown";
  }
  return user.address.city;
}
```
마지막 `return` 안에서는 일반 `.`이 안전합니다. 검사가 이미 모든 연결이 존재한다는 것을 증명했기 때문입니다.

---

많은 내장 메서드는 "찾지 못했음"을 `undefined`를 반환해서 알립니다. 배열 메서드 `find(callback)`이 대표적인 예입니다. 콜백이 `true`인 첫 번째 요소를 반환하고, 일치하는 요소가 없으면 `undefined`를 반환합니다:
```javascript
const products = [{ name: "pen", price: 2 }];
const found = products.find((p) => p.name === "ink");
console.log(found);
// prints undefined
```
여기서 `found.price`를 읽으면 에러가 발생하므로, `?.`와 `??`는 `find`와 자연스럽게 함께 쓰입니다:
```javascript
console.log(products.find((p) => p.name === "ink")?.price ?? "no price");
// prints no price
```

---

`null`과 `undefined`는 `JSON.stringify()`로 객체를 JSON으로 변환할 때 서로 다르게 동작합니다.
JSON에는 `null` 값은 있지만 `undefined`는 없습니다. 그래서 값이 `undefined`인 프로퍼티는 그냥 **빠지고**, `null`인 프로퍼티는 유지됩니다:
```javascript
const user = { name: "Ana", nickname: undefined, email: null };
console.log(JSON.stringify(user));
// prints {"name":"Ana","email":null}
```
배열 안에서는 자리를 없앨 수 없기 때문에, 거기서는 `undefined`가 `null`이 됩니다:
```javascript
console.log(JSON.stringify([1, undefined, 3]));
// prints [1,null,3]
```

---

`obj.key === undefined` 검사는 두 가지 상황을 구분하지 못합니다. 프로퍼티가 존재하지 않는 경우와, 존재하지만 값이 `undefined`인 경우입니다.
`Object.hasOwn(obj, key)`는 첫 번째 질문에만 답합니다. 값과 상관없이 객체가 `key`라는 **자기 자신의** 프로퍼티를 가지고 있으면 `true`를 반환합니다:
```javascript
const config = { debug: undefined };
console.log(config.debug === undefined, config.level === undefined);
// prints true true
console.log(Object.hasOwn(config, "debug"), Object.hasOwn(config, "level"));
// prints true false
```
"자기 자신의"란 객체 자체에 선언되었다는 뜻입니다. `toString` 같은 상속된 멤버는 모든 객체에서 사용할 수 있지만 `Object.hasOwn(config, "toString")`은 `false`입니다.
