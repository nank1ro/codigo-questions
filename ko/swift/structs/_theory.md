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
print(r.area) // 12, no parentheses
```
계산 프로퍼티는 저장할 것이 없기 때문에 멤버별 이니셜라이저에 포함되지 않습니다. 값이 다른 값들에서 파생될 때는 계산 프로퍼티를, 작업에 매개변수가 필요할 때는 메서드를 사용하세요.
