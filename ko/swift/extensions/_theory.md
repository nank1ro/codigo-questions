**확장**은 기존 타입에 새로운 기능을 추가합니다: `Int`나 `String` 같은 표준 라이브러리 타입, 또는 직접 작성한 구조체나 클래스에도 가능합니다.
`extension` 키워드 뒤에 타입 이름을 적고, 중괄호 사이에 새로운 멤버를 넣습니다:
```swift
extension Int {
    func squared() -> Int {
        return self * self
    }
}
print(4.squared()) // 16
```
확장 안에서 `self`는 메서드가 호출되는 값입니다: `4.squared()`에서 `self`는 `4`입니다. 확장이 정의되면 프로그램의 모든 `Int`가 새로운 메서드를 갖게 되며, 마치 처음부터 `Int`의 일부였던 것과 똑같이 동작합니다.

---

확장은 소스 코드가 없는 타입을 포함해 모든 타입에 적용됩니다. `String`은 표준 라이브러리에서 제공되지만, 여전히 새로운 메서드를 추가할 수 있습니다:
```swift
extension String {
    func whisper() -> String {
        return self.lowercased() + "..."
    }
}
print("HELLO".whisper()) // hello...
```
확장 안에서는 타입의 다른 멤버를 호출할 때 `self.`를 생략할 수 있습니다: `lowercased()`만 쓰면 `self.lowercased()`를 의미합니다.

---

확장은 새로운 타입을 만들지 않고 기존 타입을 복사하지도 않습니다: 타입 자체에 멤버를 추가하므로, 해당 타입의 기존 값과 앞으로 만들어질 모든 값이 그 멤버를 갖게 됩니다.
이 때문에 확장은 표준 라이브러리나 프레임워크처럼 편집할 수 없는 타입에서 특히 유용합니다: `Int`가 정의된 파일을 열 수는 없지만, 프로그램의 어떤 파일에서든 이를 확장할 수 있습니다.
```swift
extension Int {
    func isDivisible(by other: Int) -> Bool {
        return self % other == 0
    }
}
let n = 12
print(n.isDivisible(by: 4)) // true
```

---

메서드 외에도 확장은 **연산 프로퍼티**를 추가할 수 있습니다: 값을 저장하지 않고 읽을 때마다 값을 계산하는 프로퍼티입니다.
연산 프로퍼티는 `var`, 타입 어노테이션, 그리고 값을 반환하는 중괄호 본문으로 선언합니다:
```swift
extension Int {
    var isNegative: Bool {
        return self < 0
    }
}
print((-3).isNegative) // true
print(7.isNegative)    // false
```
다른 프로퍼티와 마찬가지로 괄호 없이 읽습니다: `7.isNegative()`가 아니라 `7.isNegative`입니다.

---

확장의 연산 프로퍼티는 `String`에도 자연스럽게 어울립니다. `reversed()` 메서드는 문자들을 반대 순서로 반환하고, `String(...)`은 그것들을 다시 문자열로 만듭니다:
```swift
extension String {
    var backwards: String {
        return String(reversed())
    }
}
print("swift".backwards) // tfiws
```
메서드와 마찬가지로, 확장 안에서 `reversed()`는 `self.reversed()`를 의미합니다.

---

확장은 연산 프로퍼티를 추가할 수 있지만 **저장 프로퍼티**는 추가할 수 없습니다: 다음 코드는 컴파일되지 않습니다:
```swift
extension Int {
    var label = "number" // error: extensions must not contain stored properties
}
```
저장 프로퍼티는 타입의 모든 인스턴스 안에 공간이 필요합니다. `Int` 값은 이미 프로그램 곳곳에, 심지어 확장보다 훨씬 전에 컴파일된 코드에도 존재하므로, 그 메모리 레이아웃은 바꿀 수 없습니다. 연산 프로퍼티는 프로퍼티를 읽을 때 실행되는 코드일 뿐이므로 공간이 필요하지 않습니다.

---

`Int`, `String`, 배열, 구조체는 **값 타입**입니다: `mutating`으로 표시되지 않은 메서드는 자신이 호출된 값을 변경할 수 없습니다. 확장도 mutating 메서드를 추가할 수 있습니다:
```swift
extension Int {
    mutating func increment() {
        self += 1
    }
}
var count = 1
count.increment()
print(count) // 2
```
mutating 메서드 안에서는 `self`에 값을 할당할 수 있습니다. 값은 반드시 `var`에 저장되어 있어야 합니다: `let` 상수에 대해 `increment()`를 호출하면 컴파일 오류입니다.

---

mutating 메서드는 다른 메서드와 마찬가지로 매개변수를 받을 수 있고, 값을 제자리에서 갱신하는 대신 `self`를 완전히 교체할 수도 있습니다:
```swift
extension Int {
    mutating func reset(to value: Int) {
        self = value
    }
}
var score = 42
score.reset(to: 0)
print(score) // 0
```

---

확장은 타입에 새로운 **이니셜라이저**를 추가할 수 있습니다. 구조체의 경우 이곳이 이니셜라이저를 두기에 가장 좋은 자리입니다: 구조체 본문 안에 작성한 `init`은 자동 멤버와이즈 이니셜라이저를 대체하지만, 확장에 추가한 `init`은 그것을 그대로 남겨둡니다.
새 이니셜라이저는 보통 `self.init(...)`으로 기존 이니셜라이저에 위임합니다:
```swift
struct Size {
    var width: Double
    var height: Double
}
extension Size {
    init(square side: Double) {
        self.init(width: side, height: side)
    }
}
let a = Size(square: 3)          // from the extension
let b = Size(width: 2, height: 5) // memberwise, still available
```

---

확장은 다른 사람의 타입만을 위한 것이 아닙니다. 자신의 코드를 정리하는 흔한 방법은 저장 프로퍼티를 구조체나 클래스 본문에 두고, 동작은 관련된 멤버끼리 묶은 하나 이상의 확장에 추가하는 것입니다:
```swift
struct Circle {
    var radius: Double
}
extension Circle {
    var diameter: Double {
        return radius * 2
    }
    func grown(by amount: Double) -> Circle {
        return Circle(radius: radius + amount)
    }
}
```
확장에 추가된 멤버는 마치 타입 안에 작성된 것처럼 저장 프로퍼티를 직접 사용할 수 있습니다.

---

확장은 타입이 **프로토콜**을 준수하도록 만들 수도 있습니다. 프로토콜은 타입이 구현하기로 약속하는 요구사항 목록입니다. 타입 이름 뒤에 콜론으로 구분하여 프로토콜 이름을 쓰고, 본문에 요구되는 멤버를 추가합니다.
`CustomStringConvertible`은 요구사항이 하나뿐인 표준 프로토콜로, `String` 타입의 계산 프로퍼티 `description`을 요구하며 `print`가 값을 표시할 때 이를 사용합니다:
```swift
struct Dog {
    var name: String
}
extension Dog: CustomStringConvertible {
    var description: String {
        return "Dog named \(name)"
    }
}
print(Dog(name: "Rex")) // Dog named Rex
```
각 프로토콜 준수를 각자의 확장에 두는 것이 Swift 타입을 정리하는 일반적인 방식입니다.

---

`Array`는 제네릭 타입입니다: `[Int]`와 `[String]`은 둘 다 배열이지만 **`Element`** 타입이 다릅니다. `Array`의 확장은 이 모두에 적용되는데, 새 멤버가 일부 요소에만 의미가 있을 때는 문제가 됩니다: 문자열인 숫자를 더할 수는 없습니다.
`where` 절은 확장을 `Element`가 주어진 타입인 배열로 제한합니다:
```swift
extension Array where Element == Int {
    var largest: Int {
        var result = Int.min
        for number in self {
            if number > result {
                result = number
            }
        }
        return result
    }
}
print([3, 9, 2].largest) // 9
```
`[3, 9, 2].largest`는 동작하지만, `["a", "b"].largest`는 컴파일 오류입니다: 그 프로퍼티는 `[String]`에 존재하지 않습니다.

---

확장은 **static** 멤버를 추가할 수 있습니다: 하나의 값이 아니라 타입 자체에 속하는 프로퍼티와 메서드로, `static` 키워드로 표시하고 타입 이름을 통해 접근합니다.
`static let`은 값을 저장하는데도 허용되는데, 인스턴스마다 하나씩이 아니라 타입 전체에 사본이 하나만 있기 때문입니다:
```swift
extension Int {
    static let answer = 42
    static func zeroes(_ count: Int) -> [Int] {
        return Array(repeating: 0, count: count)
    }
}
print(Int.answer)     // 42
print(Int.zeroes(3))  // [0, 0, 0]
```
static 멤버에는 작업할 `self` 값이 없습니다: `Int.answer`는 숫자가 아니라 타입에서 읽습니다.

---

확장의 static 메서드는 해당 타입의 값을 만들어 주는 작은 팩토리 함수를 두기에 좋은 자리입니다. `String(repeating:count:)`는 텍스트 조각을 정해진 횟수만큼 반복하는 표준 이니셜라이저입니다:
```swift
extension String {
    static func dashes(_ count: Int) -> String {
        return String(repeating: "-", count: count)
    }
}
print(String.dashes(4)) // ----
```

---

확장은 멤버를 **추가**만 할 수 있고, 기존 멤버를 대체하거나 재정의할 수는 없습니다. `override`는 부모와 다른 타입인 서브클래스에 속합니다. 확장은 같은 타입이므로, 이미 존재하는 메서드를 선언하면 재선언 오류가 납니다:
```swift
struct Dog {
    func speak() -> String {
        return "Woof"
    }
}
extension Dog {
    func speak() -> String { // error: invalid redeclaration of 'speak()'
        return "Bark"
    }
}
```
다른 동작이 필요하면 새로운 이름의 메서드를 추가하거나, 타입이 클래스일 때는 서브클래스를 작성하세요.
