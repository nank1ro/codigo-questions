의사 결정은 특정 조건이 충족될 때만 코드를 실행하고 싶을 때 필요합니다.
날씨가 좋을 때만 밖에서 놀고 싶다고 가정해 봅시다.
프로그래밍에서는 불리언 변수 `niceWeather`를 저장하고, 이 변수가 `true`일 때 밖에서 노는 행동을 `if`로 수행할 수 있습니다:
```javascript
var niceWeather = true;
if (niceWeather) {
    // 밖에서 놀기
}
```

---

이전 예제를 계속 살펴봅시다.
```javascript
var niceWeather = true;
if (niceWeather) {
    // 밖에서 놀기
}
```
`if` 문은 조건이 `true`일 때만 코드 블록을 실행한다는 것을 확인했습니다.
또 하나 중요한 것은 코드 블록을 나타내는 **중괄호** `{}`입니다.

---

조건이 발생했을 때 코드 블록을 실행하는 방법을 살펴보았습니다. 이제 첫 번째 조건이 실패했을 때 다른 코드 블록을 실행하는 방법을 알아봅시다.
날씨가 좋으면 밖에서 놀고, 그렇지 않으면 집에 있습니다.
JavaScript에서는 `else` 문을 사용할 수 있습니다:
```javascript
var niceWeather = true;
if (niceWeather) {
    // 밖에서 놀기
} else {
    // 집에 있기
}
```

---

확인해야 할 조건이 하나 더 있다고 가정해 봅시다. 다음 예제를 보세요:
```javascript
var num = 3;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else {
    console.log("do something else");
}
```
이 코드의 출력은 `the number is 3`입니다.
먼저 숫자가 2와 같은지 확인합니다. 이것은 거짓입니다.
그래서 두 번째 조건으로 넘어가 `num`이 3과 같은지 확인합니다. 이것이 참이므로 다음 코드 블록을 실행하여 `the number is 3`을 출력합니다

---

`else if` 문은 원하는 만큼 추가할 수 있으며, 제한이 없습니다
```javascript
var num = 4;
if (num == 2) {
    console.log("the number is 2");
} else if (num == 3) {
    console.log("the number is 3");
} else if (num == 4) {
    console.log("the number is 4");
} else if (num == 5) {
    console.log("the number is 5");
} else if (num == 6) {
    console.log("the number is 6");
}
```
이 코드의 출력은 `the number is 4`입니다.

---

조건문(`if`, `else if` 또는 `else`)을 다른 조건문 안에 중첩하여 더 복잡한 구조를 만들 수도 있습니다.
```javascript
var num = 4;
if (num < 3) {
    console.log("the number is lower than 3");
} else {
    if (num == 3) {
        console.log("the number is 3");
    } else if (num == 4) {
        console.log("the number is 4");
    } else {
        console.log("the number is greather than 4");
    }
}
```
이 코드의 출력은 `the number is 4`입니다.

---

삼항 조건 연산자는 세 부분으로 이루어진 특별한 연산자로, `question ? answer1 : answer2` 형태를 가집니다.
`question`이 참인지 거짓인지에 따라 두 표현식 중 하나를 평가하는 단축 표현입니다.
`question`이 참이면 `answer1`을 평가하고 그 값을 반환합니다. 그렇지 않으면 `answer2`를 평가하고 그 값을 반환합니다.
```javascript
let a = 10, b = 20, c = 0;
if (a < b) {
    c = a;
} else {
    c = b;
}
console.log(c);
// 10 출력
```
위 코드의 단축 코드는 다음과 같습니다:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// 10 출력
```
조건 `a < b`가 참이었기 때문에 `c`는 `a`와 같은 값으로 설정됩니다

---

_nil 병합 연산자_ `a ?? b`는 옵셔널 `a`에 값이 있으면 그 값을 언래핑하고, `a`가 `nil`이면 기본값 `b`를 반환합니다.
표현식 `a`는 항상 옵셔널 타입입니다.
표현식 `b`는 `a` 안에 저장된 타입과 일치해야 합니다.
nil 병합 연산자는 아래 코드의 단축 표현입니다:
```javascript
a != nil ? a! : b;
```

---

`if`는 JavaScript에서 조건문을 시작하는 키워드입니다. 여기에는 `elif` 키워드가 없습니다 — 두 번째 조건은 두 단어로 나눠 쓰는 `else if`로 도입합니다.

---

JavaScript의 불리언 리터럴은 소문자입니다: `True`/`False`가 아니라 `true`와 `false`이며, 문자열 `"true"`/`"false"`도 아닙니다.

---

코드 블록이 실행되지 않게 하려면, 괄호 안의 조건이 `false`로 평가되어야 합니다.

---

`if`와 괄호 사이의 공백은 순전히 보기 좋게 하기 위한 것입니다: `if(true)`와 `if (true)`는 JavaScript에게 동일한 문장입니다.

---

중괄호는 여러 문장을 하나의 블록으로 묶는 역할을 합니다. 중괄호가 없으면 `if`는 바로 뒤에 오는 문장 하나만 제어하므로, `if (true) console.log("Hello!");`도 유효한 JavaScript입니다.

---

조건은 블록이 시작되기 전에 단 한 번만 평가됩니다. 중괄호 사이의 문장들이 실행되는 동안 JavaScript는 조건을 다시 확인하지 않습니다.

---

조건이 `false`이면 블록은 완전히 건너뛰어지고, 프로그램은 닫는 중괄호 뒤의 첫 번째 문장부터 계속 실행됩니다.

---

조건이 반드시 불리언일 필요는 없습니다: JavaScript는 무엇이 오든 불리언으로 변환하므로, `if (1)`은 블록을 실행하고 `if (0)`은 실행하지 않습니다. 리터럴 `true`는 변환이 전혀 필요 없습니다.

---

코드 블록은 한 줄로 제한되지 않습니다 — 조건이 `true`이면 중괄호 안의 모든 문장이 순서대로 실행됩니다.
```javascript
if (true) {
    console.log("First line");
    console.log("Second line");
}
```
그리고 출력은 `First line`에 이어 `Second line`이 나옵니다.

---

블록 안의 문장들은 위에서 아래로 하나씩 실행되므로, 같은 블록 안의 `console.log` 호출 두 개는 서로 다른 두 줄에 출력됩니다.

---

블록 안의 문장을 들여쓰는 것은 순전히 가독성을 위한 관례일 뿐입니다. JavaScript는 무엇이 블록에 속하는지 결정할 때 들여쓰기가 아니라 항상 중괄호를 기준으로 삼습니다.

---

조건이 `true`인지 `false`인지에 따라 코드를 실행하거나 건너뛰는 `if`, `else if`, `else`와 같은 문장을 **조건문**이라고 합니다.

---

`isAfternoon`처럼 `!` 부정으로 만들어진 것이라 해도, 불리언 변수는 비교 없이 그대로 `if` 조건으로 사용할 수 있습니다.

---

`if` 문의 조건은 항상 괄호 `()` 안에 들어가며, `if` 키워드 바로 뒤, 여는 중괄호 바로 앞에 위치합니다.

---

블록은 얼마든지 많은 문장을 담을 수 있고, 아예 없어도 됩니다: `if (true) {}`는 아무것도 하지 않는 유효한 JavaScript입니다.

---

`if` 문의 코드 블록은 중괄호 `{ }` 안에 있는 명령어들의 집합으로, 조건이 `true`일 때 실제로 실행되는 부분입니다.
