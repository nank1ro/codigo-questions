**프로토콜(protocol)**은 방법은 말하지 않고, 타입이 무엇을 가져야 하는지를 기술합니다. 프로토콜은 그것을 채택하는 모든 타입이 제공하기로 약속하는 요구사항(프로퍼티와 메서드)의 목록입니다.

프로토콜은 `protocol` 키워드로 선언합니다. 프로퍼티 요구사항은 타입을 쓴 뒤에 어떻게 접근할 수 있는지를 나타내는 블록을 덧붙여 씁니다: `{ get }`은 그 타입이 최소한 값을 읽을 수 있게 해야 한다는 뜻입니다.
```swift
protocol Named {
    var name: String { get }
}
```
타입은 콜론 뒤에 프로토콜 이름을 쓰고 프로토콜이 요구하는 모든 것을 제공하여 프로토콜을 **준수(conform)**합니다:
```swift
struct Cat: Named {
    var name: String
}

let cat = Cat(name: "Luna")
print(cat.name) // Luna
```
프로토콜은 자신의 데이터를 전혀 가지지 않습니다: 프로토콜은 계약입니다. 이를 만족하는 모든 타입은 코드의 나머지 부분에서 똑같이 다룰 수 있습니다.

---

프로토콜은 **메서드**도 요구할 수 있습니다. 시그니처(이름, 매개변수, 반환 타입)만 쓰고, 본문 없이 거기서 멈춥니다:
```swift
protocol Greeter {
    func greet() -> String
}
```
준수하는 타입은 정확히 그 시그니처를 가진 메서드를 선언해야 하며, 본문은 그 타입이 제공합니다:
```swift
struct Robot: Greeter {
    func greet() -> String {
        return "BEEP"
    }
}

print(Robot().greet()) // BEEP
```
이름, 매개변수 타입, 반환 타입 중 무엇이라도 다르면 그 타입은 준수하지 않으며, 컴파일러가 어떤 요구사항이 빠졌는지 알려줍니다.

---

프로퍼티 요구사항은 그 프로퍼티를 어떻게 사용할 수 있는지를 항상 명시합니다. `{ get }`은 값을 읽을 수 있기만 하면 되고, `{ get set }`은 읽을 수 있고 **동시에** 대입할 수도 있어야 합니다:
```swift
protocol Account {
    var owner: String { get }
    var balance: Int { get set }
}
```
준수하는 타입은 계약이 요구하는 것보다 더 많이 제공해도 됩니다: `var` 저장 프로퍼티는 `{ get }`을 아주 잘 만족합니다. 하지만 더 적게 제공할 수는 없습니다 — `let` 상수나 읽기 전용 연산 프로퍼티는 `{ get set }`을 만족할 수 없습니다.

---

프로토콜은 구조체에만 쓰이는 것이 아닙니다. **클래스**도 콜론 뒤에 프로토콜을 나열하는, 정확히 같은 방식으로 준수합니다:
```swift
protocol Openable {
    func open() -> String
}

class Door: Openable {
    func open() -> String {
        return "creak"
    }
}
```
클래스가 다른 클래스를 상속하기도 한다면, 목록에서 상위 클래스가 먼저 오고 프로토콜이 그 뒤를 따릅니다. 하나의 타입은 쉼표로 구분하여 여러 프로토콜을 한 번에 채택할 수 있습니다.

---

**열거형(enum)**도 준수할 수 있습니다. 열거형에는 저장 프로퍼티가 없으므로, 프로퍼티 요구사항은 보통 케이스를 `switch`로 나누는 연산 프로퍼티로 만족시킵니다:
```swift
protocol Priced {
    var price: Int { get }
}

enum Ticket: Priced {
    case child, adult

    var price: Int {
        switch self {
        case .child: return 5
        case .adult: return 12
        }
    }
}

print(Ticket.adult.price) // 12
```
구조체, 클래스, 열거형 셋 모두 같은 방식으로 프로토콜을 채택하며, 프로토콜을 기준으로 작성된 코드는 이 셋 모두와 함께 동작합니다.

---

프로토콜은 보통 하나 이상의 요구사항을 모아 두며, 준수하는 타입은 그 모두를 만족해야 합니다:
```swift
protocol Vehicle {
    var wheels: Int { get }
    func move() -> String
}

struct Bike: Vehicle {
    var wheels = 2

    func move() -> String {
        return "pedalling"
    }
}
```
중괄호 안에서 요구사항이 어떤 순서로 적혀 있는지는 중요하지 않고, 준수하는 타입이 그것들을 제공하는 순서도 중요하지 않습니다: 컴파일러는 빠진 것이 없는지만 확인합니다.

---

구조체는 값 타입이므로, 저장 프로퍼티 중 하나를 바꾸는 메서드에는 `mutating`을 표시해야 합니다. 그 메서드가 프로토콜 요구사항이라면 프로토콜에도 그렇게 적어야 합니다:
```swift
protocol Togglable {
    mutating func toggle()
}

struct Light: Togglable {
    var isOn = false

    mutating func toggle() {
        isOn = !isOn
    }
}

var lamp = Light()
lamp.toggle()
print(lamp.isOn) // true
```
프로토콜에 `mutating`이 없다면 구조체는 그 요구사항을 결코 만족시킬 수 없습니다. 클래스는 참조 타입이라 이 키워드가 전혀 필요 없습니다: 클래스는 평범한 메서드로 `mutating` 요구사항을 충족합니다. mutating 메서드를 호출하려면 `var`가 필요합니다 — `let`에서 호출하면 컴파일 오류입니다.

---

준수 선언을 반드시 타입 옆에 둘 필요는 없습니다. **익스텐션(extension)**으로 나중에 추가할 수 있으며, 그러면 타입 자체의 선언은 데이터에만 집중할 수 있습니다:
```swift
protocol Resettable {
    mutating func reset()
}

struct Timer {
    var seconds = 0
}

extension Timer: Resettable {
    mutating func reset() {
        seconds = 0
    }
}
```
이 방법은 직접 작성하지 않은 타입에도 통합니다: 표준 라이브러리 타입의 소스를 건드리지 않고도 자신의 프로토콜을 준수하게 만들 수 있습니다.

---

**프로토콜**의 익스텐션은 다른 도구입니다: 현재와 미래를 통틀어 그것을 준수하는 모든 타입에 멤버를 추가합니다. 요구사항에 **기본 구현(default implementation)**을 주는 방법이 바로 이것입니다:
```swift
protocol Greeter {
    var name: String { get }
    func greet() -> String
}

extension Greeter {
    func greet() -> String {
        return "Hi, \(name)"
    }
}

struct Person: Greeter {
    var name: String
}

print(Person(name: "Ada").greet()) // Hi, Ada
```
`Person`은 `greet()`를 전혀 작성하지 않고도 준수합니다. 프로토콜 익스텐션 안에서는 프로토콜의 모든 요구사항(여기서는 `name`)을 사용할 수 있습니다. 준수하는 타입이라면 반드시 그것을 가지고 있음이 보장되기 때문입니다.

---

프로토콜 익스텐션은 프로토콜이 요구사항으로 나열하지 않은 멤버도 추가할 수 있습니다. 그것들은 준수하는 모든 타입에서 쓸 수 있는 추가 편의 기능입니다:
```swift
protocol Sized {
    var count: Int { get }
}

extension Sized {
    var isEmpty: Bool {
        return count == 0
    }
}
```
`isEmpty`는 요구사항이 아니므로 준수하는 타입이 제공할 필요가 없습니다 — 그냥 얻게 됩니다.

---

프로토콜은 다른 프로토콜 위에 세울 수 있습니다. 콜론 뒤에 프로토콜 이름을 쓰면 새 프로토콜이 기존 프로토콜의 모든 요구사항을 **상속**합니다:
```swift
protocol Named {
    var name: String { get }
}

protocol Aged: Named {
    var age: Int { get }
}
```
`Aged`를 준수하는 타입은 `age`*와* `name`을 모두 제공해야 하며, 어디에서나 `Named` 타입으로도 취급됩니다. 프로토콜은 쉼표로 구분하여 여러 프로토콜을 한 번에 상속할 수 있습니다.

---

기본 구현은 규칙이 아니라 대비책입니다. 준수하는 타입이 요구사항의 자체 버전을 제공하면, 실행되는 것은 그 타입의 버전입니다:
```swift
protocol Priced {
    var price: Int { get }
}

extension Priced {
    var price: Int { return 0 }
}

struct Ticket: Priced {
    var price = 12
}

print(Ticket().price) // 12, not 0
```
기본 구현은 타입이 비워 둔 빈자리만 채웁니다.

---

표준 라이브러리는 프로토콜로 만들어져 있으며, 여러분이 만든 타입도 그 프로토콜들을 채택할 수 있습니다.

`Equatable`은 타입에 `==` 연산자를 부여합니다. 저장 프로퍼티가 모두 `Equatable`인 구조체라면 준수를 선언하는 것만으로 충분합니다 — Swift가 `==`를 대신 작성해 줍니다:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

print(Point(x: 1, y: 2) == Point(x: 1, y: 2)) // true
```
`Comparable`은 `Equatable`을 상속하고 순서를 추가합니다. 두 값을 받는 `static func`로 작성하는 `<` 연산자 하나만 구현하면, `>`, `<=`, `>=`와 컬렉션의 `sorted()`, `min()`, `max()`를 공짜로 얻습니다:
```swift
struct Version: Comparable {
    var number: Int

    static func < (lhs: Version, rhs: Version) -> Bool {
        return lhs.number < rhs.number
    }
}
```

---

`CustomStringConvertible`은 여러분의 타입을 `print`가 어떻게 보여줄지 결정합니다. 유일한 요구사항은 `description` 프로퍼티입니다:
```swift
struct Coin: CustomStringConvertible {
    var value: Int

    var description: String {
        return "\(value)c"
    }
}

print(Coin(value: 25)) // 25c
```
이 준수가 없으면 구조체 출력은 `Coin(value: 25)` 같은 기본 덤프로 되돌아가며, `description` 프로퍼티만 있어서는 아무것도 달라지지 않습니다 — `print`는 프로토콜을 찾습니다. 문자열 보간도 `description`을 사용합니다.

---

프로토콜 이름 자체는 타입이 아니라 제약이므로, Swift는 두 가지 중 무엇을 뜻하는지 밝혀 달라고 요구합니다.

`some Shape`는 *컴파일 시점에 정해지는 하나의 특정한 준수 타입*을 뜻합니다. 호출하는 쪽은 그것이 무엇인지 절대 알 수 없지만, 언제나 같은 타입입니다:
```swift
func unitSquare() -> some Shape {
    return Square(side: 1)
}
```
`any Shape`는 *준수하는 어떤 타입이든 담을 수 있는 상자*를 뜻하며, 그 타입의 두 값이 서로 다른 타입을 담고 있을 수도 있습니다. 혼합 배열 안처럼 구체 타입이 달라질 수 있는 곳에서는 이것이 필요합니다:
```swift
let shapes: [any Shape] = [Square(side: 2), Rect(width: 2, height: 3)]
```
둘 다 프로토콜의 요구사항을 호출할 수 있게 해 줍니다. 하나의 타입으로 충분하다면 실행 시점 비용이 없는 `some`을 택하고, 정말로 타입을 섞어야 할 때 `any`를 쓰세요.
