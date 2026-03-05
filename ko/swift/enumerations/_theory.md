`enumeration`(열거형)은 관련된 값들의 그룹에 대한 공통 타입을 정의하며, 코드 내에서 해당 값들을 타입 안전하게 사용할 수 있게 합니다.
열거형은 `enum` 키워드를 사용하여 선언합니다:
```swift
enum Colors {
    case blue
    case red
    case green
}
```
열거형에 정의된 값들(`blue`, `red`, `green` 등)은 _열거형 케이스_라고 합니다.
`case` 키워드를 사용하여 새로운 열거형 케이스를 추가합니다.

---

여러 케이스를 쉼표로 구분하여 한 줄에 작성할 수 있습니다:
```swift
enum Colors {
    case blue, red, green
}
```

---

`switch` 문을 사용하여 개별 열거형 값을 매칭할 수 있습니다:
```swift
let color = Colors.red
switch color {
    case .blue:
        print("Blue")
    case .red:
        print("Red")
    case .green:
        print("Green")
}
// prints "Red"
```
모든 열거형 케이스에 대해 `case`를 제공할 필요가 없는 경우, `default` 케이스를 사용하여 명시적으로 처리되지 않은 케이스를 포괄할 수 있다는 점을 기억하세요

---

일부 열거형에서는 해당 열거형의 모든 케이스를 컬렉션으로 갖는 것이 유용합니다.
열거형 이름 뒤에 `: CaseIterable`을 작성하면 이 기능을 활성화할 수 있습니다.
Swift는 열거형 타입의 `allCases` 속성으로 모든 케이스의 컬렉션을 제공합니다:
```swift
enum Colors: CaseIterable {
    case blue, red, green
}
for color in Colors.allCases {
    print(color)
}
// prints blue, red, green
```
