**열거형**(*enum*)은 요일, 카드의 무늬, 주문의 상태처럼 관련된 값들의 작고 고정된 그룹을 위한 공통 타입입니다.
다른 많은 언어와 달리 JavaScript에는 `enum` 키워드가 **없습니다**. 관용적인 대체 방법은 멤버를 프로퍼티로 갖는 일반 객체를 `Object.freeze()`에 전달하여 이후에 아무도 변경할 수 없게 만드는 것입니다:
```javascript
const Color = Object.freeze({
  RED: "red",
  GREEN: "green",
  BLUE: "blue",
});
console.log(Color.RED);
// red 출력
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
// done 출력
```
한 번 동결된 객체는 새로운 프로퍼티도 받을 수 없으며, `Object.isFrozen(obj)`로 객체가 동결되었는지 확인할 수 있습니다:
```javascript
console.log(Object.isFrozen(Status));
// true 출력
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
// s 출력
console.log(Size.MEDIUM);
// undefined 출력
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
// true 출력
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
// [ 'RED', 'BLUE' ] 출력
console.log(Object.values(Color));
// [ 'red', 'blue' ] 출력
```
`Object.values()`와 배열 메서드 `includes()`를 함께 사용하는 것은, 예를 들어 사용자 입력에서 읽은 값처럼 임의의 값이 유효한 멤버인지 확인하는 표준적인 방법입니다:
```javascript
console.log(Object.values(Color).includes("red"));
// true 출력
console.log(Object.values(Color).includes("pink"));
// false 출력
```

---

열거형은 `switch`문과 자연스럽게 어울립니다. `switch`문은 하나의 값을 여러 `case` 레이블 목록과 비교하여 처음으로 일치하는 것의 코드를 실행합니다.
각 분기는 `return` 또는 `break`로 끝나며, 선택적인 `default` 분기는 어느 것도 일치하지 않을 때 실행됩니다:
```javascript
const Light = Object.freeze({ RED: "red", GREEN: "green" });

function action(light) {
  switch (light) {
    case Light.RED:
      return "stop";
    case Light.GREEN:
      return "go";
    default:
      return "unknown";
  }
}
console.log(action(Light.GREEN));
// go 출력
```
항상 원시 값(`"red"`)이 아니라 멤버(`Light.RED`)와 비교하세요. 그러면 값이 나중에 바뀌더라도 `switch`가 계속 동작합니다.

---

값에서 멤버 이름으로 되돌아가는 것을 **역방향 조회**라고 합니다. `Object.keys()`로 이름들을 순회하며, 배열 메서드 `find()`를 사용해 값이 일치하는 첫 번째 이름을 고릅니다. `find()`는 콜백이 `true`가 되는 첫 번째 요소를 반환합니다(없으면 `undefined`를 반환합니다):
```javascript
const Priority = Object.freeze({ LOW: 1, HIGH: 3 });
let name = Object.keys(Priority).find((key) => Priority[key] === 3);
console.log(name);
// HIGH 출력
```
`Priority[key]`는 변수 `key`에 저장된 이름을 가진 멤버를 읽습니다. 이는 어떤 객체에서든 사용하는 것과 같은 대괄호 표기법입니다.

---

문자열 멤버에는 한 가지 약점이 있습니다. 같은 텍스트를 가진 어떤 문자열이든 멤버로 인정된다는 점입니다.
```javascript
const Color = Object.freeze({ RED: "red" });
console.log(Color.RED === "red");
// true 출력
```
오직 자기 자신과만 같은 멤버를 원한다면 `Symbol`을 사용하세요. `Symbol(description)`은 같은 설명으로 만들어진 것이라도 다른 모든 심볼과 다른, 완전히 새로운 값을 만듭니다:
```javascript
const Suit = Object.freeze({
  HEARTS: Symbol("hearts"),
  SPADES: Symbol("spades"),
});
console.log(Suit.HEARTS === Suit.HEARTS);
// true 출력
console.log(Suit.HEARTS === Symbol("hearts"));
// false 출력
console.log(typeof Suit.HEARTS);
// symbol 출력
```
전달하는 텍스트는 디버깅용 라벨일 뿐이며, `description` 프로퍼티로 다시 읽을 수 있습니다(`Suit.HEARTS.description`은 `"hearts"`입니다).

---

열거형 값은 예를 들어 모든 멤버를 라벨이나 가격에 대응시키기 위해, 다른 객체의 **키**로 자주 사용됩니다. 객체 리터럴 안에서 키를 대괄호 `[ ]`로 감싸면 표현식이 평가되고 그 결과가 키로 사용됩니다(**계산된 키**). 이는 문자열 멤버와 심볼 멤버 모두에서 동작합니다:
```javascript
const Status = Object.freeze({ ACTIVE: "active", DONE: "done" });
const labels = {
  [Status.ACTIVE]: "In progress",
  [Status.DONE]: "Completed",
};
console.log(labels[Status.DONE]);
// Completed 출력
```
대괄호가 없다면 `Status.DONE: "Completed"`는 구문 오류가 되고, `"Status.DONE"`은 그냥 문자열 키가 됩니다.

---

각 멤버가 여러 데이터나 자신만의 메서드를 필요로 할 때는 **클래스**가 열거형의 역할을 할 수 있습니다. 모든 멤버는 그 클래스의 인스턴스이며, `static` 프로퍼티, 즉 각 인스턴스가 아니라 클래스 자체에 속하는 프로퍼티에 저장됩니다:
```javascript
class Planet {
  static MERCURY = new Planet("Mercury", 0.4);
  static EARTH = new Planet("Earth", 1);

  constructor(name, gravity) {
    this.name = name;
    this.gravity = gravity;
  }
}
console.log(Planet.EARTH.name);
// Earth 출력
```
클래스 뒤에 `Object.freeze(Planet)`을 호출해 아무도 멤버를 추가하거나 교체하지 못하게 막고, 생성자 안에서 `Object.freeze(this)`로 각 인스턴스를 동결하여 멤버 자체를 읽기 전용으로 유지하세요.
