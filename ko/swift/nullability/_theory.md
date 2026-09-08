때로는 값이 단순히 존재하지 않는 경우가 있습니다: 중간 이름이 없는 사용자, 아무것도 찾지 못한 검색, 숫자로 변환할 수 없는 텍스트 등입니다.
Swift는 값이 없음을 `nil`로 나타내지만, 일반 변수는 이를 담을 수 없습니다:
```swift
var age: Int = nil // error: 'nil' cannot initialize type 'Int'
```
값이 없을 수 있도록 하려면 타입 뒤에 물음표 `?`를 붙여 **옵셔널** 타입을 선언합니다.
`Int?`는 `Int` 또는 `nil` 중 하나를 담습니다:
```swift
var age: Int? = 30
age = nil // 허용됨
```
값 없이 선언된 옵셔널 변수는 `nil`로 시작합니다.

---

옵셔널은 `==`와 `!=`를 사용해 `nil`과 비교할 수 있고, 감싸인 타입의 일반 값과 직접 비교할 수도 있습니다:
```swift
var score: Int? = 10
print(score == nil) // false
print(score == 10)  // true
```
`Int?`와 `Int`는 서로 다른 타입임을 기억하세요. `Int?`는 비어 있을 수 있지만, `Int`는 절대 비어 있지 않습니다.

---

옵셔널은 상자와 같습니다. 안의 값을 사용하기 전에 열어야 하며, Swift에서는 이를 **언래핑**이라고 부릅니다.
가장 빠른 방법은 느낌표 `!`를 사용하는 **강제 언래핑**입니다:
```swift
let score: Int? = 10
print(score! + 5) // 15
```
`!`는 Swift에게 "여기에 값이 확실히 있다"라고 알려줍니다. 만약 그것이 틀려서 옵셔널이 `nil`이라면, 프로그램은 즉시 런타임 크래시로 멈춥니다:
```swift
let missing: Int? = nil
print(missing! + 5) // Fatal error: Unexpectedly found nil
```
그렇기 때문에 강제 언래핑은 위험한 것으로 간주되며, 값이 존재한다고 확신할 때만 사용해야 합니다.

---

강제 언래핑은 옵셔널이 `nil`이 아님을 이미 확인한 경우에만 안전합니다:
```swift
if score != nil {
    print(score! * 2)
}
```

---

`nil`인지 확인한 다음 강제 언래핑하는 것은 장황합니다. Swift는 `if let`을 사용한 **옵셔널 바인딩**을 제공하며, 이는 옵셔널을 언래핑하고 값을 새로운 상수에 한 번에 저장합니다:
```swift
let score: Int? = 10
if let value = score {
    print("Score: \(value)") // value는 Int?가 아니라 Int
} else {
    print("No score")
}
```
`if`의 본문은 옵셔널이 값을 담고 있을 때만 실행되며, 그 안에서 `value`는 `Int?`가 아닌 일반 `Int`이므로 `!`가 필요 없습니다.

---

값이 없는 것이 "여기서 멈춰야 함"을 의미할 때는, `guard let`이 `if let`보다 더 명확합니다.
이는 옵셔널을 언래핑하고, 실패하면 `else` 블록을 실행하며, 이 블록은 현재 스코프를 벗어나야 합니다(`return`, `break`, `continue`, `throw` 중 하나로):
```swift
func greet(_ name: String?) {
    guard let name = name else {
        print("Nobody here")
        return
    }
    print("Hello, \(name)!") // 여기서부터 name은 String
}
```
`if let`과 달리, 언래핑된 상수는 함수의 나머지 부분에서도 계속 사용할 수 있으므로, 정상 경로가 `if` 안에 중첩되지 않습니다.

---

`guard let`의 전형적인 사용법은 함수 상단에서 입력을 검증하고, 값이 없을 때 대체 값을 반환하는 것입니다:
```swift
func length(of text: String?) -> Int {
    guard let text = text else { return 0 }
    return text.count
}
```

---

옵셔널에서 원하는 것은 대부분 그 값이거나 기본값입니다.
**nil 병합 연산자** `??`는 정확히 그 일을 합니다. 옵셔널이 값을 가지고 있으면 언래핑하고, 그렇지 않으면 오른쪽 값을 반환합니다:
```swift
let score: Int? = nil
let points = score ?? 0 // points는 0인 Int
```
기본값은 감싸인 값과 같은 타입이어야 합니다.
`??`를 여러 번 연결할 수 있으며, 처음으로 `nil`이 아닌 값이 사용됩니다.
```swift
let a: Int? = nil
let b: Int? = 7
print(a ?? b ?? 0) // 7
```

---

`??`는 합리적인 기본값이 있을 때 옵셔널을 일반 값으로 바꾸는 가장 짧은 방법입니다:
```swift
func volume(from setting: Int?) -> Int {
    return setting ?? 50
}
```

---

`??`를 연결할 때, Swift는 왼쪽에서 오른쪽으로 평가하며 `nil`이 아닌 첫 번째 값에서 멈춥니다. 마지막 기본값은 그 앞의 모든 옵셔널이 `nil`일 때만 사용됩니다.

---

옵셔널에 대해 프로퍼티에 접근하거나 메서드를 호출하려면 먼저 언래핑해야 합니다.
`?.`를 사용한 **옵셔널 체이닝**이 이를 대신 처리해줍니다. 옵셔널이 `nil`이면 전체 표현식이 `nil`이 되고, 그렇지 않으면 접근이 이루어집니다:
```swift
let name: String? = "swift"
let upper = name?.uppercased() // "SWIFT"를 담은 String?
```
결과는 프로퍼티 자체가 옵셔널이 아니더라도 항상 옵셔널입니다.
체이닝은 필요한 만큼 길게 이어질 수 있으며, `??`와도 잘 어우러집니다:
```swift
class User {
    var nickname: String? = "ace"
}
let user: User? = User()
print(user?.nickname?.count ?? 0) // 3
```

---

옵셔널 체이닝은 데이터가 여러 단계에서 없을 수 있을 때 진가를 발휘합니다: 객체 자체가 `nil`일 수도 있고, 그 프로퍼티 중 하나도 `nil`일 수 있습니다.
하나의 `?.` 체인이 `if` 없이도 두 경우를 모두 처리합니다.

---

하나의 `if let`이나 `guard let`으로 여러 옵셔널을 한 번에 언래핑할 수 있습니다. 바인딩을 쉼표로 구분하세요.
본문은 모든 옵셔널이 값을 가지고 있을 때만 실행됩니다:
```swift
let first: String? = "Ada"
let last: String? = "Lovelace"
if let first = first, let last = last {
    print("\(first) \(last)")
}
```
바인딩 뒤에 `if let n = number, n > 0`처럼 불리언 조건을 추가할 수도 있습니다.

---

여러 옵셔널을 하나의 `if let`에 바인딩하면 코드가 평탄하게 유지됩니다: 하나의 `else` 분기가 값이 없는 모든 경우를 처리합니다.

---

많은 연산이 실패할 수 있으며, Swift는 옵셔널을 반환함으로써 실패를 알립니다.
텍스트를 숫자로 변환하는 것이 대표적인 예입니다: `Int("42")`는 `42`를 담은 `Int?`를 반환하고, `Int("abc")`는 `nil`을 반환합니다.
`Int("3.5")`도 텍스트가 정수가 아니므로 `nil`입니다. 소수에는 `Double("3.5")`를 사용하세요.
```swift
let typed = "42"
if let number = Int(typed) {
    print(number + 1) // 43
}
```
다른 예로는 `array.first`(빈 배열이면 `nil`)와 `dictionary[key]`(키가 없으면 `nil`)가 있습니다.

---

변환은 실패할 수 있기 때문에 그 결과는 항상 옵셔널이며, 텍스트가 유효한 숫자라고 확신하더라도 사용하기 전에 언래핑해야 합니다.

---

실패할 수 있는 변환은 `guard let`과 자연스럽게 어울립니다: 변환하고, 결과가 `nil`이면 중단한 뒤, 일반 값으로 작업합니다.

---

때로는 옵셔널 안의 값을 변환하면서도 그 결과를 옵셔널로 유지하고 싶을 때가 있습니다. 직접 언래핑하고 다시 래핑할 필요 없이 말이죠.
옵셔널에는 `map` 메서드가 있습니다: 값이 있으면 클로저를 적용하고, 없으면 `nil`을 반환합니다.
```swift
let score: Int? = 10
let doubled = score.map { $0 * 2 } // 20을 담은 Int?
let missing: Int? = nil
let stillMissing = missing.map { $0 * 2 } // nil
```
실패할 수 있는 변환과 결합하면 `Int(text).map { $0 + 1 }`처럼 간결한 파이프라인이 됩니다.
