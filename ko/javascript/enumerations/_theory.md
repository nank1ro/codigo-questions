**열거형**(*enum*)은 요일, 카드의 무늬, 주문의 상태처럼 관련된 값들의 작고 고정된 그룹을 위한 공통 타입입니다.
다른 많은 언어와 달리 JavaScript에는 `enum` 키워드가 **없습니다**. 관용적인 대체 방법은 멤버를 프로퍼티로 갖는 일반 객체를 `Object.freeze()`에 전달하여 이후에 아무도 변경할 수 없게 만드는 것입니다:
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// prints red
```
관례상 이 객체는 `const`로 선언하고, 이름은 대문자로 시작하며, 멤버 이름은 다른 상수와 마찬가지로 `UPPER_CASE`로 작성합니다.

---

각 멤버에 저장할 값은 자유롭게 선택할 수 있습니다. **문자열**은 출력하거나 로그로 남기거나 파일에 저장할 때 읽기 쉽기 때문에 가장 흔한 선택입니다:
```javascript
const Status = Object.freeze({
  ACTIVE: "active",
  DONE: "done",
});
console.log(Status.DONE);
// prints done
```
한 번 동결된 객체는 새로운 프로퍼티도 받을 수 없으며, `Object.isFrozen(obj)`로 객체가 동결되었는지 확인할 수 있습니다:
```javascript
console.log(Object.isFrozen(Status));
// prints true
```

---

애초에 왜 객체를 동결할까요? 동결된 객체는 모든 변경을 거부합니다. 기존 멤버에 값을 대입하거나, 새 멤버를 추가하거나, 삭제해도 아무 효과가 없습니다.
이 거부가 어떻게 나타나는지는 코드가 실행되는 모드에 따라 다릅니다.
- **비엄격 모드**(일반 스크립트의 기본값)에서는 대입이 **조용히 무시됩니다**
- **엄격 모드**(`"use strict"`로 시작하는 파일, ES 모듈, 클래스 본문)에서는 `TypeError`가 **발생합니다**

```javascript
const Size = Object.freeze({ SMALL: "s", LARGE: "l" });
Size.SMALL = "xs";
Size.MEDIUM = "m";
console.log(Size.SMALL);
// prints s
console.log(Size.MEDIUM);
// prints undefined
```
어느 쪽이든 열거형은 여러분이 정의한 값을 그대로 유지하며, 이는 상수 집합에 정확히 바라는 동작입니다.

---

멤버는 **숫자**도 가질 수 있습니다. 숫자 값은 멤버 사이에 자연스러운 순서가 있을 때, 일반적인 연산자로 비교할 수 있어 유용합니다:
```javascript
const Priority = Object.freeze({
  LOW: 1,
  MEDIUM: 2,
  HIGH: 3,
});
console.log(Priority.HIGH > Priority.LOW);
// prints true
```
그 대가는 가독성입니다. `Priority.HIGH`를 출력하면 `3`이 표시되는데, 이는 문자열 `"high"`보다 훨씬 적은 정보를 전달합니다.

---

열거형은 단지 객체이므로, 일반적인 객체용 헬퍼를 사용해 내부를 살펴볼 수 있습니다.
- `Object.keys(Enum)`은 멤버의 **이름**을 담은 배열을 반환합니다
- `Object.values(Enum)`은 멤버의 **값**을 담은 배열을 반환합니다
- `Object.entries(Enum)`은 `[이름, 값]` 쌍의 배열을 반환합니다

```javascript
const Color = Object.freeze({ RED: "red", BLUE: "blue" });
console.log(Object.keys(Color));
// prints [ 'RED', 'BLUE' ]
console.log(Object.values(Color));
// prints [ 'red', 'blue' ]
```
`Object.values()`와 배열 메서드 `includes()`를 함께 사용하는 것은, 예를 들어 사용자 입력에서 읽은 값처럼 임의의 값이 유효한 멤버인지 확인하는 표준적인 방법입니다:
```javascript
console.log(Object.values(Color).includes("red"));
// prints true
console.log(Object.values(Color).includes("pink"));
// prints false
```
