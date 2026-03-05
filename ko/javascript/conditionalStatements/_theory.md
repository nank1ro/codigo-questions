의사 결정은 특정 조건이 충족될 때만 코드를 실행하고 싶을 때 필요합니다.
날씨가 좋을 때만 밖에서 놀고 싶다고 가정해 봅시다.
프로그래밍에서는 불리언 변수 `niceWeather`를 저장하고, 이 변수가 `true`일 때 밖에서 노는 행동을 `if`로 수행할 수 있습니다:
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
}
```

---

이전 예제를 계속 살펴봅시다.
```javascript
var niceWeather = true;
if (niceWeather) {
    // play outside
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
    // play outside
} else {
    // stay home
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
// prints 10
```
위 코드의 단축 코드는 다음과 같습니다:
```javascript
let a = 10, b = 20, c = 0;
c = a < b ? a : b;
console.log(c);
// prints 10
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
