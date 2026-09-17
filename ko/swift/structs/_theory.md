**구조체**(struct, *structure*의 줄임말)는 관련된 값들을 함께 모아 두기 위해 직접 설계하는 타입입니다. 별개의 `title`과 별개의 `pages`를 따로따로 다루는 대신, `Book`을 한 번 정의해 두고 어디서든 사용할 수 있습니다.
`struct` 키워드로 선언하며, 그 안에 작성된 변수들이 **저장 프로퍼티**가 됩니다:
```swift
struct Book {
    var title: String
    var pages: Int
}
```
`Book`은 이제 `Int`나 `String`과 똑같은 타입입니다. 인스턴스의 프로퍼티에는 점으로 접근합니다:
```swift
let book = Book(title: "Swift", pages: 120)
print(book.title) // Swift
```

---

`Book`을 만드는 코드를 작성한 적이 없는데도 `Book(title: "Swift", pages: 120)`이 동작했습니다. Swift가 이 코드를 대신 작성해 주는 것입니다: 모든 구조체는 **멤버별 이니셜라이저**를 무료로 얻는데, 이는 저장 프로퍼티를 매개변수로 가지며 선언된 순서대로, 각 프로퍼티 이름을 인자 레이블로 사용하는 이니셜라이저입니다:
```swift
struct Point {
    var x: Int
    var y: Int
}

let p = Point(x: 3, y: 4)
print(p.x) // 3
```
클래스는 이를 무료로 얻지 못하며, 그래서 구조체가 값을 모델링하는 가장 빠른 방법 중 하나입니다.

---

저장 프로퍼티는 선언된 바로 그 자리에 **기본값**을 가질 수 있습니다. Swift는 그 값으로 타입을 추론하므로 타입 어노테이션을 생략할 수 있습니다:
```swift
struct Counter {
    var label: String
    var value = 0
}
```
멤버별 이니셜라이저는 기본값이 있는 모든 프로퍼티를 선택적 인자로 바꿉니다: 값을 전달하면 기본값을 덮어쓰고, 생략하면 기본값이 유지됩니다.
```swift
let a = Counter(label: "clicks")
print(a.value) // 0

let b = Counter(label: "clicks", value: 7)
print(b.value) // 7
```

---

구조체는 **메서드**도 가질 수 있습니다: 중괄호 안에 작성된 함수로, 호출된 인스턴스를 대상으로 동작합니다. 메서드 안에서는 접두사 없이 프로퍼티 이름을 바로 사용합니다:
```swift
struct Rectangle {
    var width: Int
    var height: Int

    func area() -> Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area()) // 12
```
메서드의 매개변수가 프로퍼티 이름을 가리는 경우, 인스턴스의 프로퍼티를 뜻한다는 것을 나타내려면 `self.width`라고 쓰면 됩니다.

---

**계산 프로퍼티**는 프로퍼티처럼 보이지만 메서드처럼 동작합니다: 아무것도 저장하지 않고, 읽을 때마다 값을 계산합니다. 타입을 쓰고 그다음 값을 반환하는 코드 블록을 작성합니다:
```swift
struct Rectangle {
    var width: Int
    var height: Int

    var area: Int {
        return width * height
    }
}

let r = Rectangle(width: 3, height: 4)
print(r.area) // 12, 괄호 없음
```
계산 프로퍼티는 저장할 것이 없기 때문에 멤버별 이니셜라이저에 포함되지 않습니다. 값이 다른 값들에서 파생될 때는 계산 프로퍼티를, 작업에 매개변수가 필요할 때는 메서드를 사용하세요.

---

구조체는 **값 타입**입니다: 다른 변수에 대입하거나 함수에 전달하면 *복사본*이 넘어갑니다. 복사본을 변경해도 원본은 그대로입니다.
```swift
struct Point {
    var x: Int
}

var a = Point(x: 1)
var b = a
b.x = 99
print(a.x) // 1
```
클래스는 **참조 타입**입니다: `b = a`가 두 이름이 같은 인스턴스를 가리키게 하므로, `b.x = 99`는 `a.x`도 `99`로 바꿉니다.

이것이 둘의 진짜 차이이며, Swift가 대부분의 데이터를 구조체로 모델링하는 이유이기도 합니다: 가지고 있는 값은 그 값을 받은 코드에 의해 몰래 수정될 수 없습니다.

---

구조체는 값이기 때문에, `mutating` 키워드로 그렇게 선언하지 않는 한 메서드가 프로퍼티를 변경하는 것은 허용되지 않습니다:
```swift
struct Counter {
    var value = 0

    mutating func increase(by amount: Int) {
        value += amount
    }
}

var c = Counter()
c.increase(by: 5)
print(c.value) // 5
```
mutating 메서드는 `var`에 저장된 인스턴스에만 호출할 수 있습니다. `let` 인스턴스의 값은 얼어 있으므로, `c.increase(by: 5)`는 컴파일되지 않습니다.

---

멤버별 이니셜라이저가 원하는 방식으로 타입을 만들어 주지 않는다면, 직접 **이니셜라이저**를 작성하면 됩니다. `init`으로 선언하고 원하는 매개변수를 받으며, 끝나기 전에 모든 저장 프로퍼티에 값을 부여해야 합니다. 그 안에서 `self`는 생성 중인 인스턴스입니다:
```swift
struct Square {
    var side: Int

    init(_ side: Int) {
        self.side = side
    }
}

let s = Square(5)
print(s.side) // 5
```
구조체의 중괄호 안에 `init`을 작성하면 멤버별 이니셜라이저를 대체하므로, 이후로는 `Square(side: 5)`가 더 이상 존재하지 않습니다.

---

어떤 값들은 개별 인스턴스가 아니라 타입 자체에 속합니다: 통화 코드, 공유되는 기본값, 흔한 케이스를 만들어 주는 팩토리 같은 것들입니다. 이런 값들은 `static`으로 표시하고 타입 이름을 통해 읽습니다:
```swift
struct Money {
    static let currency = "EUR"
    var amount: Int

    static func zero() -> Money {
        return Money(amount: 0)
    }
}

print(Money.currency)     // EUR
print(Money.zero().amount) // 0
```
여기서 `currency`는 절대 변하지 않으므로 `let`으로 선언되었고, 따라서 프로그램 전체가 공유하는 상수입니다. `Money.currency`는 `Money`를 하나도 만들지 않고 동작하는 반면, `amount`는 인스턴스가 필요합니다.

---

타입이 지원한다고 선언하기 전까지는 두 구조체를 `==`로 비교할 수 없습니다. 선언에서 콜론 뒤에 쓰는 `Equatable` **프로토콜**을 준수하면 됩니다:
```swift
struct Point: Equatable {
    var x: Int
    var y: Int
}

let a = Point(x: 1, y: 2)
let b = Point(x: 1, y: 2)
print(a == b) // true
```
`==`를 직접 작성할 필요는 없습니다: 모든 저장 프로퍼티가 이미 `Equatable`이라면 Swift가 프로퍼티를 하나씩 비교하는 `==`를 자동으로 만들어 줍니다. 두 인스턴스는 모든 프로퍼티가 같을 때 같으며, 이는 값에게 기대하는 바로 그 동작입니다.

---

구조체는 다른 타입과 마찬가지의 타입이므로 배열, 딕셔너리, 세트에 저장할 수 있고, 이미 알고 있는 모든 도구가 그대로 동작합니다:
```swift
struct Item {
    var name: String
    var price: Int
}

let items = [Item(name: "Tea", price: 3), Item(name: "Cake", price: 7)]

for item in items {
    print(item.name)
}

let names = items.map { $0.name }
let total = items.reduce(0) { $0 + $1.price }
print(total) // 10
```
배열은 *복사본*을 담는다는 점을 기억하세요: `items[0]`를 변수로 읽어 와 변경해도 배열은 바뀌지 않습니다.
