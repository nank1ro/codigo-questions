JavaScript의 모든 값에는 **타입**이 있습니다. 일곱 가지 **원시** 타입이 있습니다:
- 모든 숫자를 위한 `number`, 예를 들어 `42` 또는 `3.14`
- 텍스트를 위한 `string`, 예를 들어 `"Ana"`
- `true`와 `false`를 위한 `boolean`
- 한 번도 제공되지 않은 값을 위한 `undefined`
- 의도적으로 비어 있는 값을 위한 `null`
- `9007199254740993n`처럼 모든 크기의 정수를 위한 `bigint`
- `Symbol()`로 만든 고유한 식별자를 위한 `symbol`

그 외의 모든 것(배열, 함수, `{}`로 만든 객체, 날짜 등)은 `object`입니다.
`typeof` 연산자는 값의 타입을 문자열로 알려줍니다:
```javascript
console.log(typeof 42, typeof "Ana", typeof true);
// prints number string boolean
let city;
console.log(typeof city);
// prints undefined
```

---

JavaScript는 **동적 타입** 언어입니다: 변수 자체에는 타입이 없고, 현재 담고 있는 값에만 타입이 있습니다. 같은 변수가 지금은 숫자를, 나중에는 문자열을 가질 수 있으며, `typeof`는 값을 따라갑니다:
```javascript
let data = 10;
console.log(typeof data);
// prints number
data = "ten";
console.log(typeof data);
// prints string
```
이것은 편리하지만, 함수가 예상하지 못한 타입의 값을 받을 수도 있다는 뜻이기도 하므로, `typeof`로 확인하는 것은 흔한 첫 번째 단계입니다. `typeof`는 문자열을 반환하므로, 그 결과를 문자열과 비교합니다:
```javascript
if (typeof data === "string") {
  console.log("text");
}
```

---

`typeof`에는 사람들을 놀라게 하는 몇 가지 답이 있습니다.
함수는 객체임에도 불구하고 자신만의 답인 `"function"`을 받습니다:
```javascript
console.log(typeof function () {});
// prints function
console.log(typeof console.log);
// prints function
```
배열은 자신만의 답을 받지 **못합니다**: 배열은 `{}`와 마찬가지로 그저 `"object"`입니다:
```javascript
console.log(typeof [1, 2, 3]);
// prints object
```
그리고 `typeof null`은 `"object"`인데, 이는 한 번도 수정되지 않은 역사적인 버그입니다. 따라서 `typeof`는 원시 값과 함수는 잘 구별하지만, 배열, 객체, `null`은 서로 구별하지 못합니다.

---

타입을 함수처럼 호출하면 값을 다른 타입으로 **명시적으로** 변환할 수 있습니다:
- `Number(value)`는 숫자로 변환합니다: `Number("42")`는 `42`입니다
- `String(value)`는 문자열로 변환합니다: `String(42)`는 `"42"`입니다
- `Boolean(value)`는 불리언으로 변환합니다: `Boolean("")`은 `false`입니다

결과는 완전히 새로운 값이며, 원래 값은 변경되지 않습니다:
```javascript
const input = "7";
const count = Number(input) + 1;
console.log(count, typeof count);
// prints 8 number
console.log(String(count) + "!");
// prints 8!
```
명시적으로 변환하면 의도가 드러납니다: `Number(input)`을 읽는 사람이라면 `input`이 텍스트였음을 알 수 있습니다.

---

`Number()`는 엄격합니다: 문자열 전체가 숫자여야 하며, 그렇지 않으면 결과는 `NaN`("Not a Number")입니다:
```javascript
console.log(Number("12px"));
// prints NaN
```
`parseInt()`와 `parseFloat()`은 더 관대합니다: 문자열의 시작 부분부터 숫자를 읽어 들이고, 앞쪽 공백을 건너뛰며, 숫자의 일부가 아닌 첫 번째 문자에서 멈춥니다. `parseInt`는 정수 부분만 남깁니다:
```javascript
console.log(parseInt("12px"), parseFloat("1.5kg"));
// prints 12 1.5
console.log(parseInt("3.9em"), parseInt("-4px"));
// prints 3 -4
```
문자열이 숫자를 시작할 수 있는 것(선택적인 부호 뒤에 숫자)으로 시작하지 않으면, 이 함수들도 `NaN`을 반환합니다:
```javascript
console.log(parseInt("auto"));
// prints NaN
```
`NaN`은 자기 자신과도 같지 않은 유일한 값이므로 `x === NaN`은 항상 `false`입니다. 이를 감지하려면 `Number.isNaN(x)`를 사용하세요.

---

"이것이 `NaN`인가?"를 묻는 방법은 두 가지가 있으며, 두 방법은 서로 다른 질문에 답합니다.
오래된 전역 함수 `isNaN(value)`는 먼저 `value`를 숫자로 **변환한 다음** 검사합니다. 따라서 전혀 `NaN`이 아니더라도 숫자가 될 수 없는 모든 것에 대해 `true`를 말합니다:
```javascript
console.log(isNaN("hello"));
// prints true, because Number("hello") is NaN
console.log(isNaN("42"));
// prints false, because Number("42") is 42
```
`Number.isNaN(value)`는 변환하지 **않습니다**: `value`가 실제로 숫자 `NaN`일 때만 `true`입니다:
```javascript
console.log(Number.isNaN("hello"));
// prints false, a string is not NaN
console.log(Number.isNaN(Number("hello")));
// prints true
```
`Number.isNaN`을 선호하고, 변환이 실패했는지 알고 싶다면 먼저 변환하세요.

---

JavaScript는 **암묵적으로**도 변환하며, `+` 연산자는 이것이 가장 자주 문제를 일으키는 곳입니다. 한쪽이 문자열이면 `+`는 **연결**하고 다른 쪽은 문자열로 변환됩니다:
```javascript
console.log("5" + 3);
// prints 53
console.log(1 + 2 + "3");
// prints 33, because 1 + 2 is computed first
```
그 외의 모든 산술 연산자는 양쪽을 **숫자**로 변환합니다:
```javascript
console.log("6" - 2, "3" * "4");
// prints 4 12
```
따라서 텍스트에서 온 값(사용자 입력, 파일, URL)을 더하면 합 대신 조용히 문자열을 만들어 낼 수 있습니다. 안전하게 하려면 더하기 전에 `Number()`로 변환하세요.

---

문자열을 숫자로 변환하는 짧은 방법은 **단항 플러스**입니다: 단일 값 앞에 놓인 `+`는 `Number()`와 정확히 같게 변환합니다:
```javascript
console.log(+"5" + 5);
// prints 10
console.log(typeof +"5");
// prints number
```
간결하지만 덧셈과 혼동하기 쉬우므로, 많은 팀이 명시적인 `Number("5")`를 선호합니다.

---

**느슨한** 동등 비교 `==`는 비교하기 전에 기억하기 어려운 규칙에 따라 양쪽을 공통 타입으로 변환합니다:
```javascript
console.log("5" == 5);
// prints true, "5" becomes 5
console.log(0 == "");
// prints true, "" becomes 0
console.log(0 == false, "1" == true);
// prints true true
```
**엄격한** 동등 비교 `===`는 절대 변환하지 않습니다: 타입이 다른 값은 그냥 같지 않습니다:
```javascript
console.log("5" === 5, 0 === "", 0 === false);
// prints false false false
```
기본적으로는 `===`(그리고 `!==`)를 사용하세요. 유일하게 흔한 예외는 `null`과 `undefined`를 함께 검사하는 `value == null`입니다.

---

JavaScript는 `if` 조건이나 `Boolean(value)`처럼 불리언이 필요할 때 값을 변환합니다. `false`가 되는 값은 여덟 개뿐이며, 이를 **falsy**라고 부릅니다:
`false`, `0`, `-0`, `0n`, `""`, `null`, `undefined` 그리고 `NaN`입니다.
**그 외의 모든 것은 truthy입니다**. 빈 것처럼 보이는 일부 값도 포함됩니다:
```javascript
console.log(Boolean(0), Boolean(""), Boolean(NaN));
// prints false false false
console.log(Boolean("0"), Boolean("false"), Boolean([]), Boolean({}));
// prints true true true true
```
`"0"`은 비어 있지 않은 문자열이므로 truthy이고, 빈 배열은 객체이므로 역시 truthy입니다.

---

모든 값을 불리언으로 변환하는 흔한 방법은 **이중 부정** `!!`입니다: 첫 번째 `!`는 불리언으로 변환한 뒤 뒤집고, 두 번째는 다시 뒤집습니다:
```javascript
console.log(!!"text", !!0);
// prints true false
```
`!!value`와 `Boolean(value)`는 정확히 같은 결과를 냅니다. 명시적인 형태가 읽기 더 쉽습니다.

---

JavaScript에는 정수와 소수를 위한 단일 `number` 타입이 있습니다: 모든 숫자는 64비트 부동 소수점 값(*double*)입니다. 따라서 `5`와 `5.0`은 같은 값이며, 별도의 정수 타입은 없습니다:
```javascript
console.log(5 === 5.0, 10 / 2);
// prints true 5
```
숫자에 소수 부분이 없는지 묻으려면 `Number.isInteger`를 사용하세요:
```javascript
console.log(Number.isInteger(5.0), Number.isInteger(3.5));
// prints true false
```
템플릿 리터럴은 보간된 값을 `String()`과 같은 규칙으로 문자열로 변환하므로, `${5.0}`은 `"5.0"`이 아니라 `"5"`가 됩니다.

---

숫자는 double이기 때문에 일부 소수는 정확하게 저장될 수 없고 작은 오차가 나타납니다:
```javascript
console.log(0.1 + 0.2);
// prints 0.30000000000000004
console.log(0.1 + 0.2 === 0.3);
// prints false
```
`toFixed(digits)` 메서드는 숫자를 소수점 아래 `digits`자리로 반올림하지만 **문자열**을 반환합니다. 이것은 표시하기에는 좋지만 추가 계산에는 적합하지 않습니다:
```javascript
const price = (0.1 + 0.2).toFixed(2);
console.log(price, typeof price);
// prints 0.30 string
```
반올림된 **숫자**를 얻으려면 결과를 `Number()`로 다시 변환하세요:
```javascript
console.log(Number((0.1 + 0.2).toFixed(1)));
// prints 0.3
```

---

`number`는 `9007199254740991`인 `Number.MAX_SAFE_INTEGER`까지만 정수를 정확하게 표현할 수 있습니다. 그 이상에서는 자릿수가 사라집니다:
```javascript
console.log(9007199254740993);
// prints 9007199254740992
```
더 큰 정수에는 `bigint`를 사용하세요: 리터럴에 `n` 접미사를 붙여 쓰거나 `BigInt()`로 변환합니다:
```javascript
const big = 9007199254740993n;
console.log(typeof big, big + 1n);
// prints bigint 9007199254740994n
```
`console.log`는 `n` 접미사를 보여주고, `String(big)`은 순수한 숫자만 보여줍니다.
`bigint`와 `number`는 산술 연산에서 섞을 수 없습니다: `big + 1`은 `TypeError`를 던집니다. `BigInt(count)`나 `Number(big)`로 한쪽을 명시적으로 변환하세요.

---

`typeof`는 배열, 객체, `null`에 대해 `"object"`라고 답하므로, 이들을 구별하려면 두 가지 추가 검사가 필요합니다.
`Array.isArray(value)`는 배열에 대해서만 `true`입니다:
```javascript
console.log(Array.isArray([1, 2]), Array.isArray({}));
// prints true false
```
`null`에 대해서는 `value === null`처럼 직접 비교합니다. 이들을 결합하면 모든 값에 대한 완전한 그림이 됩니다:
```javascript
function kind(value) {
  if (value === null) return "null";
  if (Array.isArray(value)) return "array";
  return typeof value;
}
```
일반 `typeof`는 이들을 구별할 수 없으므로, `null`과 배열을 먼저 검사하세요.

---

폼, 파일 또는 URL에서 오는 텍스트는 숫자나 불리언을 나타내는 경우에도 항상 문자열입니다. 이것을 올바른 타입으로 되돌리는 일은 지금까지 본 내용을 결합합니다: 불리언은 `"true"`와 `"false"`를 비교하고, 숫자는 `Number()`를 시도하되, `Number("")`는 `0`이며 `Number.isNaN`이 변환이 실패했을 때 알려준다는 점을 기억하세요:
```javascript
console.log(Number("3.5"), Number(""), Number("12px"));
// prints 3.5 0 NaN
```
어떤 것에도 해당하지 않으면 문자열을 그대로 둡니다.
