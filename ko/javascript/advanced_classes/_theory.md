이미 `extends`가 한 클래스를 다른 클래스의 자식으로 만든다는 것은 알고 있습니다. 이 키워드가 실제로 제공하는 것은 **상속**입니다. 자식 클래스는 부모의 모든 프로퍼티와 메서드를 공짜로 물려받고, 그 위에 자신만의 것을 추가할 수 있습니다.

상속을 유용하게 만드는 요소는 바로 **`super`**입니다. 자식 생성자 안에서 `super(...)`는 부모 생성자를 호출하므로, 부모가 자신이 소유한 객체의 부분을 설정할 수 있습니다:
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
}
class Dog extends Animal {
    constructor(name, breed) {
        super(name);
        this.breed = breed;
    }
}
```
여기서 `super(name)`은 `name`을 `Animal`에 넘겨 저장하게 하고, `Dog`는 `breed`만 신경 쓰면 됩니다.

---

자식 클래스는 부모가 이미 제공하는 것을 다시 정의할 필요가 없습니다. 메서드도 상속되므로, 자식의 인스턴스는 자기 것인 것처럼 메서드를 호출할 수 있습니다:
```javascript
class Animal {
    constructor(name) {
        this.name = name;
    }
    speak() {
        return `${this.name} makes a sound`;
    }
}
class Dog extends Animal {}
console.log(new Dog("Max").speak());
// prints Max makes a sound
```
자식이 자신의 생성자를 선언하면, 그 안에서 `super(...)`를 호출하는 것은 **필수**입니다. 호출하지 않으면 객체가 초기화되지 않은 채로 남아 JavaScript가 `ReferenceError`를 던집니다. 생성자가 전혀 없는 자식은 괜찮습니다. JavaScript가 모든 인자를 부모에게 전달하는 생성자를 작성해 주기 때문입니다.

---

`super()`에 대한 규칙은 "어딘가에서 호출하라"는 것보다 더 엄격합니다. 자식 생성자 안에서 `this`는 `super()`가 실행되기 전까지 존재하지 않습니다. 객체를 만드는 것은 부모 생성자이기 때문입니다. 그 줄 전에 `this`를 사용하면 오류가 발생합니다:
```javascript
class Child extends Base {
    constructor() {
        this.x = 1; // ReferenceError
        super();
    }
}
```
따라서 `super(...)`는 `this`를 사용하는 자식 생성자의 **첫 번째 문장**이어야 합니다.

---

자식이 부모가 이미 가진 메서드를 정의하면 자식 버전이 이깁니다. 이것을 **재정의(오버라이딩)**라고 합니다:
```javascript
class Animal {
    speak() {
        return "some sound";
    }
}
class Dog extends Animal {
    speak() {
        return "Woof";
    }
}
console.log(new Dog().speak());
// prints Woof
```
재정의는 부모 버전을 삭제하지 않고 숨길 뿐입니다. 자식 메서드 안에서 `super.methodName(...)`는 여전히 부모 버전에 도달할 수 있으므로, 부모 동작을 대체하는 대신 확장할 수 있습니다:
```javascript
class Puppy extends Dog {
    speak() {
        return super.speak() + "!";
    }
}
console.log(new Puppy().speak());
// prints Woof!
```
차이에 주의하세요. `super(...)`는 부모 **생성자**를 호출하고, `super.name(...)`는 부모 **메서드**를 호출합니다.

---

지금까지는 모든 프로퍼티가 생성자 안에서 만들어졌습니다. **클래스 필드**를 사용하면 클래스 본문에 직접 선언할 수 있고, 시작 값을 줄 수도 있습니다:
```javascript
class Counter {
    count = 0;
    step = 1;
}
console.log(new Counter().count);
// prints 0
```
필드는 생성자 본문이 실행되기 전에 각 새 인스턴스에 할당되므로, 생성자는 이미 필드를 믿고 사용할 수 있습니다. 값이 없는 필드도 선언은 되지만 `undefined`로 시작합니다:
```javascript
class Task {
    done = false;
    title;
}
```
문법에 주의하세요. 선언에는 `let`도 `const`도 `this`도 없으며, 줄은 세미콜론으로 끝납니다.

---

클래스가 서로 상속할 때는 순서가 중요합니다. `class` 선언은 `function`처럼 호이스팅되지 **않습니다**. 그 이름은 클래스가 작성된 줄부터 존재합니다. 따라서 자식 클래스는 자신이 상속하는 부모보다 *나중에* 나타나야 하며, 그렇지 않으면 `extends` 절이 `ReferenceError`로 실패합니다.

---

일부 동작은 특정 인스턴스가 아니라 클래스 자체에 속합니다. 예를 들어 두 단위 사이의 변환은 작업할 객체가 필요하지 않습니다. 메서드에 **`static`**을 표시하면 클래스에 배치됩니다:
```javascript
class MathUtils {
    static double(n) {
        return n * 2;
    }
}
console.log(MathUtils.double(4));
// prints 8
```
정적 메서드는 클래스 이름으로 호출되며, 인스턴스로는 호출하지 않습니다. `new MathUtils().double(4)`는 `TypeError`를 던집니다. 인스턴스는 정적 멤버를 받지 않기 때문입니다. 정적 메서드 안에서 `this`는 클래스를 가리키므로, `this.otherStatic(...)`으로 다른 정적 메서드를 호출할 수 있습니다.

---

`static`은 필드에도 적용됩니다. **정적 프로퍼티**는 인스턴스마다 하나씩이 아니라 클래스에 한 번만 저장되므로, 공유 카운터나 상수를 두기에 자연스러운 장소입니다:
```javascript
class Circle {
    static PI = 3.14;
}
console.log(Circle.PI);
// prints 3.14
```
사본이 하나뿐이므로, 값을 갱신하는 모든 인스턴스는 같은 값을 갱신합니다. 생성자 안에서는 `this`가 아니라 클래스 이름인 `Circle.PI`로 접근합니다. `this.PI`는 인스턴스의 프로퍼티를 찾는데 아무것도 없어서 `undefined`를 줍니다.

---

정적 메서드의 아주 흔한 용도는 **팩토리**입니다. 다른 모양의 데이터로부터 인스턴스를 만들어 반환하는 메서드입니다. 팩토리는 `new`를 한 곳에 모아 주고, 무엇을 하는지 말해 주는 이름을 생성에 붙여 줍니다:
```javascript
class Duration {
    constructor(seconds) {
        this.seconds = seconds;
    }
    static fromMinutes(minutes) {
        return new Duration(minutes * 60);
    }
}
console.log(Duration.fromMinutes(2).seconds);
// prints 120
```
팩토리는 인스턴스가 존재하기 전에 호출될 수 있으며, 일반 메서드로는 불가능합니다.

---

**게터**는 프로퍼티처럼 읽히는 메서드입니다. 이름 앞에 `get`을 쓰고, 호출하는 곳에서는 괄호를 붙이지 않습니다:
```javascript
class Rectangle {
    constructor(width, height) {
        this.width = width;
        this.height = height;
    }
    get area() {
        return this.width * this.height;
    }
}
const r = new Rectangle(3, 4);
console.log(r.area);
// prints 12
```
`r.area`는 메서드를 실행하고 그 결과를 돌려주므로 숫자입니다. 여기에 괄호를 붙이면 그 숫자를 호출하려 하기 때문에 실패합니다.

거울상에 해당하는 것은 `set`으로 선언하는 **세터**이며, 프로퍼티에 값이 대입될 때 실행됩니다. 정확히 하나의 매개변수를 받습니다:
```javascript
set area(value) {
    this.width = value / this.height;
}
```

---

세터의 진짜 가치는 값을 거절할 수 있다는 점입니다. 대입과 저장된 값 사이에서 도착한 값을 검사하거나, 제한하거나, 거절할 기회를 얻습니다:
```javascript
class Volume {
    constructor(level) {
        this._level = level;
    }
    get level() {
        return this._level;
    }
    set level(value) {
        if (value <= 10) {
            this._level = value;
        }
    }
}
const v = new Volume(3);
v.level = 50;
console.log(v.level);
// prints 3, the setter rejected 50
```
같은 이름의 게터와 세터는 하나의 프로퍼티를 이루므로, 동시에 일반 필드일 수는 없습니다. 저장된 값은 다른 이름 아래 있으며, 관례상 앞에 밑줄을 붙인 같은 이름을 사용합니다.

---

`_temperature`의 앞부분 밑줄은 관례일 뿐입니다. 바깥에서 `v._level = 999`를 써서 세터를 그냥 지나쳐 가는 것을 막을 수 없습니다. **비공개 필드**는 언어가 강제합니다. 이름은 `#`으로 시작하고, 클래스 본문에서 선언해야 하며, 그 클래스 안에서만 읽거나 쓸 수 있습니다:
```javascript
class Secret {
    #code = 1234;
    reveal() {
        return this.#code;
    }
}
const s = new Secret();
console.log(s.reveal());
// prints 1234
console.log(s.#code);
// SyntaxError: the field is not accessible here
```
두 가지 세부 사항에서 쉽게 넘어질 수 있습니다. `#`은 이름의 일부이므로 항상 `this.#code`라고 쓰지 `this.code`라고 쓰지 않습니다. 그리고 비공개 필드는 `Object.keys`나 인스턴스의 `console.log`에 나타나지 않습니다.

---

메서드도 비공개일 수 있습니다. 이름 앞에 `#`을 붙이면 그 메서드는 클래스의 공개 표면에서 사라지지만, 다른 어떤 메서드에서든 `this.#name(...)`으로 호출할 수 있습니다:
```javascript
class Receipt {
    #format(n) {
        return `$${n}`;
    }
    print(n) {
        return this.#format(n);
    }
}
console.log(new Receipt().print(7));
// prints $7
```
이렇게 하면 도우미 단계를 API 밖에 둘 수 있습니다. 호출자는 그 뒤의 포매팅 세부 사항이 아니라 `print`를 봅니다. 비공개 필드와 비공개 메서드가 함께 클래스에 명확한 안과 밖을 만들어 줍니다.

---

객체를 출력하면 보통 쓸모없는 결과가 나옵니다. JavaScript가 문자열이 필요한데 객체를 받으면 객체의 **`toString`** 메서드를 호출하며, 기본 구현은 `[object Object]`를 반환합니다. 직접 정의하면 그것을 대체합니다:
```javascript
class Money {
    constructor(amount) {
        this.amount = amount;
    }
    toString() {
        return `$${this.amount}`;
    }
}
console.log(`${new Money(7)}`);
// prints $7
```
같은 메서드는 문자열 연결과 `String(value)`에서도 사용됩니다. 적절한 **숫자** 변환도 원한다면 `[Symbol.toPrimitive](hint)`를 정의하세요. 이것은 `"string"`, `"number"` 또는 `"default"`를 받고 무엇을 반환할지 결정하며, 존재하면 `toString`보다 우선합니다.

---

**`instanceof`** 연산자는 객체가 어떤 클래스, 또는 그 클래스를 상속하는 클래스로부터 만들어졌는지를 묻습니다:
```javascript
class Animal {}
class Dog extends Animal {}
const max = new Dog();
console.log(max instanceof Dog);    // true
console.log(max instanceof Animal); // true, Dog extends Animal
```
JavaScript에는 `abstract` 키워드가 없지만, 같은 아이디어를 손으로 쓸 수 있습니다. 기본 클래스가 모양을 정의하고, 자식이 *반드시* 제공해야 하는 모든 메서드는 단순히 예외를 던집니다:
```javascript
class Shape {
    area() {
        throw new Error("area() must be implemented");
    }
}
```
`area`를 재정의하는 것을 잊은 자식은 조용히 `undefined`를 반환하는 대신, 처음 사용되는 시점에 크게 실패합니다.

---

`for...of`와 스프레드 연산자 `...`는 아무 객체에나 동작하지 않습니다. 특수한 키 `Symbol.iterator` 아래 저장된 메서드를 제공하는 객체인 **이터러블**에 동작합니다. 클래스에 그 메서드를 주면 이터러블의 자격을 갖추게 됩니다:
```javascript
class Playlist {
    constructor(songs) {
        this.songs = songs;
    }
    *[Symbol.iterator]() {
        for (const song of this.songs) {
            yield song;
        }
    }
}
const list = new Playlist(["a", "b"]);
console.log([...list]);
// prints [ 'a', 'b' ]
```
이름 앞의 `*`는 그것을 **제너레이터**로 만듭니다. `yield`로 값을 한 번에 하나씩 넘겨주고 그 사이에 멈추는 함수입니다. 반복 프로토콜을 만족하는 가장 짧은 방법이며, 저장된 값이 아니라 계산된 값에도 동작합니다.
