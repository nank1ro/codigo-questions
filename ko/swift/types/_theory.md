Swift의 모든 값에는 **타입**이 있으며, 타입은 컴파일러에게 그 값이 어떤 종류의 데이터인지, 무엇을 할 수 있는지 알려줍니다.
기본 타입은 다음과 같습니다:
- `Int`: `42`나 `-7` 같은 정수
- `Double`: `3.14`처럼 소수 부분이 있는 수
- `String`: `"Hello"` 같은 텍스트 조각
- `Character`: `"a"` 같은 하나의 문자
- `Bool`: `true` 또는 `false`

상수나 변수의 타입은 **타입 어노테이션**, 즉 이름 뒤에 콜론과 타입 이름을 붙여서 지정할 수 있습니다:
```swift
let age: Int = 36
let name: String = "Ada"
```
한 타입의 값은 다른 타입의 상수에 저장할 수 없습니다: `let age: Int = "36"`은 컴파일 오류입니다.

---

대부분의 경우 타입 어노테이션을 직접 작성하지 않습니다: Swift는 몇 가지 리터럴 규칙에 따라 대입하는 값으로부터 타입을 **추론**합니다.
- `42`처럼 소수점이 없는 수는 `Int`입니다
- `3.14`처럼 소수점이 있는 수는 `Double`입니다
- 큰따옴표 사이의 텍스트는 `String`입니다
- `true`와 `false`는 `Bool`입니다
```swift
let count = 42     // Int
let price = 9.99   // Double
let name = "Ada"   // String
let isOpen = true  // Bool
```
Swift에는 `Float`도 있습니다. 이는 `Double`의 절반 메모리를 사용하지만 정밀도가 떨어지는 소수이므로, 소수 리터럴이 `Float`로 추론되는 일은 없습니다: 어노테이션으로 직접 요청해야 합니다.
마찬가지로 `"a"`는 `String`으로 추론되므로, `Character`에는 항상 어노테이션이 필요합니다.

---

`type(of:)` 함수는 값의 타입을 반환하며, Swift가 무엇을 추론했는지 확인할 때 유용합니다:
```swift
print(type(of: 42))    // Int
print(type(of: 2.5))   // Double
print(type(of: "hi"))  // String
```
추론된 타입과 다른 타입을 원하면 어노테이션을 추가합니다. 정수 리터럴은 `Double`이나 `Float` 상수에 저장할 수 있고, 한 문자 리터럴은 `Character` 상수에 저장할 수 있습니다:
```swift
let ratio: Double = 3       // 3.0, not an Int
let half: Float = 0.5
let initial: Character = "S"
print(type(of: ratio))      // Double
```

---

Swift는 숫자 타입 간에 절대 자동으로 변환하지 않습니다: 둘 다 숫자이더라도 `Int`에 `Double`을 더하는 것은 컴파일 오류입니다.
```swift
let apples = 3
let price = 1.5
let total = apples * price // error: Int and Double can't be mixed
```
이들을 함께 사용하려면 값을 해당 타입의 이니셜라이저에 전달하여 필요한 타입의 새 값을 만듭니다:
```swift
let total = Double(apples) * price // 4.5
```
반대 방향도 마찬가지입니다: `Int(4.5)`는 `Int`를 만들며, 수의 정수 부분만 남깁니다.

---

`Int(x)`는 반올림하지 않습니다: 단순히 소수 부분을 버리는 **버림**을 하므로, `Int(3.99)`는 `3`이고 `Int(-3.99)`는 `-3`입니다.
가장 가까운 정수로 반올림하려면 먼저 `Double`에 `rounded()`를 호출한 다음 변환하세요:
```swift
let x = 3.99
print(Int(x))            // 3
print(Int(x.rounded()))  // 4
```
`2.5` 같은 중간 값은 0에서 멀어지는 방향으로 반올림됩니다: `2.5`는 `3.0`이 되고 `-2.5`는 `-3.0`이 됩니다.

---

피연산자의 타입이 나눗셈이 동작하는 방식을 결정합니다. 둘 다 `Int`일 때 `/` 연산자는 **정수 나눗셈**을 수행합니다: 결과는 `Int`이고 나머지는 버려집니다.
피연산자 중 하나라도 `Double`이면 `/`는 부동소수점 나눗셈을 수행하고 소수 부분을 유지합니다:
```swift
print(7 / 2)              // 3
print(7.0 / 2)            // 3.5
let slices = 7
print(Double(slices) / 2) // 3.5
```
따라서 두 `Int` 값으로 소수 결과를 얻으려면 나누기 **전에** 적어도 하나를 `Double`로 변환해야 합니다: `Double(7 / 2)`는 `3.0`인데, 정수 나눗셈이 이미 일어났기 때문입니다.

---

정수로부터 계산한 소수 결과를 함수가 반환해야 할 때는, 나누기 전에 피연산자를 `Double`로 변환하고 반환 타입을 `Double`로 선언합니다:
```swift
func ratio(_ part: Int, _ total: Int) -> Double {
    return Double(part) / Double(total)
}
print(ratio(1, 4)) // 0.25
```
배열의 `count`도 `Int`이므로 같은 변환이 필요하다는 점을 기억하세요.

---

숫자와 문자열은 같은 이니셜라이저 문법으로 변환합니다. `String(42)`은 수를 텍스트 `"42"`로 바꾸며, 이는 `"\(42)"`로 보간하는 것과 정확히 같습니다.
반대 방향은 실패할 수 있습니다. 모든 텍스트가 수는 아니기 때문입니다. 따라서 `Int("42")`는 **옵셔널** `Int?`를 반환합니다: 여기서는 `42`를 담지만, `Int("hello")`는 `nil`입니다.
옵셔널 단원에서 배웠듯이, `??`로 대체 값을 제공하거나 `if let`으로 언랩할 수 있습니다:
```swift
let typed = "42"
let number = Int(typed) ?? 0
print(number + 1) // 43
```

---

`Int(text)`는 전체 텍스트가 선택적 부호를 가진 유효한 정수일 때만 성공합니다:
```swift
print(Int("42"))   // Optional(42)
print(Int("-7"))   // Optional(-7)
print(Int("3.5"))  // nil, not a whole number
print(Int(" 42"))  // nil, spaces are not allowed
print(Int("abc"))  // nil
```
소수 텍스트에는 `Double(text)`을 사용하세요. 같은 방식으로 `Double?`을 반환합니다: `Double("3.5")`는 `Optional(3.5)`입니다.

---

**타입 별칭**은 `typealias` 키워드로 기존 타입에 새 이름을 부여합니다:
```swift
typealias Score = Int
let best: Score = 100
print(best + 1) // 101
```
`Score`와 `Int`는 같은 타입이므로 자유롭게 섞어 쓸 수 있습니다. 별칭은 안전성을 더하지 않습니다: 일반 타입이 프로그램에서 특별한 의미를 가질 때 코드를 더 잘 읽히게 할 뿐입니다.

---

`Int`는 64비트를 사용하므로 고정된 범위의 수만 표현할 수 있습니다. 가장 큰 값과 가장 작은 값은 `Int.max`와 `Int.min`로 제공됩니다:
```swift
print(Int.max) // 9223372036854775807
print(Int.min) // -9223372036854775808
```
이 한계를 넘어서는 것을 **오버플로**라고 합니다. 다른 많은 언어와 달리, Swift는 조용히 범위의 반대쪽 끝으로 되돌아가지 않습니다: 오버플로가 발생한 연산은 프로그램을 멈추는 **런타임 오류**입니다.

---

`Int.max`와 `Int.min`는 극값을 찾을 때 시작 값으로 유용합니다: 어떤 실제 수든 `Int.max`보다 작으므로, "지금까지 본 가장 작은 값"의 안전한 초기 값이 됩니다:
```swift
var smallest = Int.max
for number in [8, 3, 5] {
    if number < smallest {
        smallest = number
    }
}
print(smallest) // 3
```

---

문자열 단원에서 보았듯이, `String`을 반복하면 한 번에 하나의 `Character`가 주어집니다. `Character`는 `String`이 아니므로, 텍스트로 사용하려면 `String(c)`으로 변환합니다.
문자가 숫자(digit)일 때 `wholeNumberValue` 프로퍼티는 그 수 값을 `Int?`로 제공합니다: 숫자가 아닌 문자에 대해서는 `nil`입니다.
```swift
for c in "a1" {
    print(c.wholeNumberValue)
}
// nil
// Optional(1)
```

---

`Int(text)`와 `Double(text)`은 실패하면 `nil`을 반환하므로, 결과를 `nil`과 비교하면 그 텍스트가 해당 종류의 수인지 알 수 있습니다:
```swift
print(Int("42") != nil)     // true
print(Double("4.2") != nil) // true
print(Double("42") != nil)  // true, a whole number is also a valid Double
```
마지막 줄에 주목하세요: `Int`가 받아들이는 텍스트는 `Double`도 모두 받아들이므로, 둘을 구별하려면 먼저 `Int`로 확인해야 합니다.

---

때로는 서로 다른 타입의 값을 함께 저장해야 할 때가 있습니다. 특별한 타입 `Any`는 **어떤** 타입의 값이든 담을 수 있으므로, `[Any]`로 선언된 배열은 숫자, 문자열, 불리언을 섞을 수 있습니다:
```swift
let items: [Any] = [1, "two", true]
```
각 요소는 여전히 자신의 실제 타입을 기억하며, `type(of:)`가 이를 드러냅니다. 값을 실제 타입으로 다루려면 옵셔널을 반환하는 `as?`로 **조건부 캐스트**를 사용합니다: 타입이 일치하면 값을 담고, 그렇지 않으면 `nil`을 담습니다:
```swift
for item in items {
    if let number = item as? Int {
        print(number + 1) // runs only for 1
    }
}
```
`Any`는 최후의 수단입니다: 단일 구체 타입의 배열이 더 안전하고 사용하기 쉬우므로, 가능하면 항상 그쪽을 선호하세요.

---

조건부 캐스트는 `else if`와 함께 자연스럽게 연결되어 여러 가능한 타입을 처리하며, 각각을 결과에 필요한 타입으로 변환합니다:
```swift
let item: Any = 2.5
if let number = item as? Int {
    print(Double(number))
} else if let number = item as? Double {
    print(number)
}
```
`Any`에 저장된 `Int`는 여전히 `Int`입니다: 여기에 `as? Double`을 하면 `nil`이 반환되는데, `as?`는 타입을 확인할 뿐 숫자를 변환하지 않기 때문입니다.
