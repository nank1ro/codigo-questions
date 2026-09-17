Swift에서 오류는 크래시가 아니라 **값**입니다. `Error` 프로토콜을 준수하면 어떤 타입이든 오류가 될 수 있는데, 무엇이 잘못될 수 있는지를 케이스 이름으로 정확히 표현할 수 있어서 보통 열거형을 씁니다:
```swift
enum LoginError: Error {
    case wrongPassword
}
```
실패할 수 있는 함수에는 `throws`를 표시하고, 실패는 `throw`로 알립니다:
```swift
func login(_ password: String) throws {
    if password != "swift" {
        throw LoginError.wrongPassword
    }
    print("welcome")
}
```
그런 함수를 호출하려면 `try`가 필요하고, 그 호출은 `do` 블록 안에 있어야 하며, 그 뒤에는 실패했을 때 무엇을 할지 적는 `catch` 블록이 따라옵니다:
```swift
do {
    try login("hunter2")
} catch {
    print("login failed")
}
// login failed
```
`throw`가 실행되면 `do` 블록의 나머지는 건너뛰고 `catch`가 이어받습니다. 크래시는 일어나지 않습니다. 프로그램은 `catch` 뒤로 계속 진행됩니다.

---

스로우하는 함수도 값을 반환할 수 있습니다. `throws` 키워드는 매개변수 목록과 반환 화살표 사이에 씁니다:
```swift
func square(_ n: Int) throws -> Int {
    if n < 0 {
        throw SquareError.negative
    }
    return n * n
}
```
소리 내어 읽으면 이렇습니다. *square는 `Int`를 받고, 스로우할 수 있으며, `Int`를 반환한다*.

호출하는 쪽에서는 아무것도 던져지지 않았을 때만 값이 존재하므로, 대입은 `do` 블록 안에 둡니다:
```swift
do {
    let result = try square(4)
    print(result) // 16
} catch {
    print("failed")
}
```
`try`는 선택적인 장식이 아닙니다. 컴파일러는 `try` 없이는 호출을 거부하므로, 읽는 사람은 어느 줄이 실패할 수 있는지 항상 알 수 있습니다.

---

패턴 없는 `catch`는 모든 오류를 똑같이 처리합니다. 대개는 특정한 실패 하나에 반응하고 싶으므로, `catch`에 **패턴**을 붙일 수 있습니다. 그 `catch`가 처리하려는 케이스를 적는 것입니다.
```swift
do {
    try check("")
} catch ValidationError.empty {
    print("the text is empty")
} catch {
    print("something else")
}
```
Swift는 `catch` 절을 위에서 아래로 시도하고, 패턴이 맞는 첫 번째 절을 실행합니다.

마지막 `catch`에 패턴이 없는 것은 의도적입니다. 패턴이 있는 `catch`는 그것이 지목한 케이스만 다루는데, Swift는 모든 오류가 어딘가에서 처리되기를 요구합니다. 그래서 패턴을 나열한 `do` 블록에는 나머지를 쓸어 담을 패턴 없는 `catch`가 마지막에 필요합니다.

---

순서가 중요합니다. Swift는 던져진 값을 작성된 순서대로 각 `catch` 패턴과 비교하고 처음 일치하는 곳에서 멈추므로, 패턴 없는 `catch`를 맨 위에 두면 그 아래 모든 것을 삼켜 버립니다. 구체적인 케이스를 위에, 모두 잡는 `catch`를 아래에 두세요.

어떤 패턴에도 맞지 않는 오류는 무시되지 않습니다. 마지막의 패턴 없는 `catch`로 갑니다.

---

오류 케이스는 데이터를 담을 수 있습니다. 케이스에 **연관 값**을 주면 `throw`가 그 값을 채워 넣고, 처리하는 쪽은 *무엇이* 실패했는지뿐 아니라 *얼마나* 모자랐는지까지 알게 됩니다:
```swift
enum ValidationError: Error {
    case tooShort(minimum: Int)
}

throw ValidationError.tooShort(minimum: 8)
```
대응하는 `catch`는 `let`으로 그 값을 바인딩합니다:
```swift
} catch ValidationError.tooShort(let minimum) {
    print("needs at least \(minimum) characters")
}
```
`let` 뒤의 이름은 마음대로 정하면 됩니다. 그 `catch` 블록 안에서만 쓸 수 있는 새 상수입니다. 이렇게 하면 실패가 일어나는 지점에서 숫자를 문자열에 직접 끼워 넣지 않고도 오류가 유용한 정보를 함께 실어 나를 수 있습니다.

---

보통 하나의 열거형이 한 작업이 실패할 수 있는 모든 방식을 담습니다. 이유마다 케이스 하나입니다:
```swift
enum FormError: Error {
    case empty
    case tooLong
}
```
케이스마다 `catch`를 쓰면 반복이 심해집니다. 대신 타입 전체를 한 번에 잡고 그 값을 `switch`하세요:
```swift
} catch let error as FormError {
    switch error {
    case .empty: print("empty")
    case .tooLong: print("too long")
    }
} catch {
    print("unknown")
}
```
`catch let error as FormError`는 *`FormError`인 것은 무엇이든 잡아서 `error`라고 부른다*는 뜻입니다. 블록 안에서 `error`는 열거형 타입이므로 `switch`가 케이스들을 알아보고 전부 다뤘는지 확인해 줍니다. 마지막의 패턴 없는 `catch`는 여전히 필요합니다. 다른 타입의 오류가 이 `do` 블록에 도달할 수도 있기 때문입니다.

---

검증 함수는 거절을 먼저 적고 실제 작업을 들여쓰기 없이 아래에 남길 때 가장 잘 읽힙니다. `guard`가 바로 그것을 위한 것입니다. 반드시 성립해야 하는 조건을 적고, 성립하지 않으면 `else` 블록이 실행됩니다.
```swift
func priceFor(_ quantity: Int) throws -> Int {
    guard quantity > 0 else {
        throw OrderError.notPositive
    }
    return quantity * 3
}
```
`guard`의 `else` 블록은 반드시 현재 스코프를 벗어나야 하는데, `throw`는 `return`, `break`, `continue`와 함께 그 방법 중 하나입니다. 함수 맨 위에 쌓인 여러 개의 `guard`는 입력이 만족해야 할 규칙 목록처럼 읽힙니다.

---

때로는 무언가가 *왜* 실패했는지는 중요하지 않고, 실패했다는 사실만 알면 됩니다. `try?`는 스로우하는 호출을 **옵셔널**로 바꿉니다. 성공하면 값이고, 오류를 던지면 `nil`입니다.
```swift
enum ParseError: Error {
    case notANumber
}

func toInt(_ text: String) throws -> Int {
    guard let value = Int(text) else {
        throw ParseError.notANumber
    }
    return value
}

if let number = try? toInt("42") {
    print(number) // 42
}
```
`do`도 `catch`도 없습니다. 실패가 이미 익숙한 옵셔널 언래핑 안으로 접혀 들어갑니다. 대가는 오류 값이 버려진다는 점이므로, 정말로 보고할 것이 없을 때만 `try?`를 쓰세요.

---

`try?`가 옵셔널을 만들어 주므로, nil 병합 연산자 `??`가 대체 값을 공급하며 마무리합니다:
```swift
let port = (try? readPort(text)) ?? 8080
```
괄호가 중요합니다. 괄호가 없으면 `try?`가 `??`까지 포함한 식 전체를 덮으려 하고, 컴파일러는 실패할 수 있는 호출이 어디서 끝나는지 명확히 밝히라고 요구합니다.

이 줄은 한 문장처럼 읽힙니다. *읽어 낸 포트를 쓰고, 안 되면 8080을 쓴다*. 복구가 정말로 기본값 하나뿐일 때는 `do`/`catch` 두 줄이 한 줄로 줄어듭니다.

---

세 번째 형태가 있습니다. `try!`입니다. 컴파일러에게 *이 호출은 실패할 수 없다*고 말하는 것이라 `do`도 `catch`도 옵셔널도 없습니다. 그래도 실패하면 프로그램은 즉시 멈춥니다.
```swift
let pattern = try! Regex("[0-9]+")
```
`try!`가 정당화되는 모양이 바로 이것입니다. 인자가 여러분이 직접 소스에 쓴 리터럴이고, 그것이 틀렸다면 코드 자체가 망가진 것이므로 첫 테스트 실행에서 멈추는 편이 낫습니다.

반면 실행 중에 들어오는 것은 무엇이든 — 사용자가 입력한 줄, 파일, 네트워크 응답 — 코드를 쓸 때는 보이지 않는 방식으로 잘못될 수 있고, 거기에 `try!`를 쓰면 복구 가능한 실패가 사용자 눈앞의 크래시로 바뀝니다. 그런 곳에는 `do`/`catch`나 `try?`를 쓰세요.

---

함수가 오류를 던지면 `throw` 뒤의 모든 것이 건너뛰어집니다. 파일을 닫거나 잠금을 푸는 줄까지 포함해서 말이죠. `defer`가 그 문제를 해결합니다. 지금 블록을 등록해 두면 현재 스코프가 어떤 식으로 끝나든 그때 실행됩니다.
```swift
func load() throws {
    print("open")
    defer { print("close") }
    throw FileError.missing
}
```
이 호출은 `open`을 출력하고 그다음 `close`를 출력한 뒤에야 오류가 호출자에게 전달됩니다. 함수가 정상적으로 반환했더라도 `close`는 똑같이 출력되었을 것입니다. 바로 그것이 핵심입니다. 정리 코드를 준비 코드 바로 옆에 두고, 어느 출구로 나가는지 더는 신경 쓰지 마세요.

---

하나의 스코프에는 `defer`를 여러 개 등록할 수 있습니다. 이들은 **역순**으로 실행됩니다. 마지막에 등록된 것이 가장 먼저 실행됩니다.

이것은 임의의 규칙이 아닙니다. 정리 작업은 보통 순서대로 진행된 준비 작업을 되돌립니다. 파일을 열고 나서 잠갔다면, 되돌릴 때는 반대 방향이어야 합니다. 잠금을 풀고 나서 닫는 것이죠. 역순 실행은 각 `defer`를 바로 윗줄의 거울상으로 만들어 줍니다.

---

클로저를 받는 함수에는 문제가 하나 있습니다. 건네받은 클로저가 오류를 던질지 알 수 없다는 점입니다. 함수에 `throws`를 붙이면 해를 끼치지 않는 클로저를 넘기는 호출자까지 전부 `try`를 써야 합니다. `rethrows`는 *당신이 준 클로저가 던질 때만 나도 던진다*고 말합니다:
```swift
func applyTwice(_ value: Int, _ transform: (Int) throws -> Int) rethrows -> Int {
    return try transform(transform(value))
}
```
본문 안에서는 여전히 `try`를 씁니다. 그 호출은 정말로 실패할 수 있기 때문입니다. 호출하는 쪽에서는 컴파일러가 넘긴 클로저를 살펴봅니다:
```swift
let doubled = applyTwice(3, { (n: Int) -> Int in n * 2 }) // try가 필요 없습니다
```
표준 라이브러리는 이것을 곳곳에서 씁니다. `map`, `filter`, `sorted(by:)`가 모두 `rethrows`이고, 그래서 평범한 `map` 앞에는 `try`를 쓸 일이 없는 것입니다.

---

`do` 블록이 오류 타입 하나에만 묶여 있는 것은 아닙니다. 각 단계는 저마다의 방식으로 실패할 수 있고, 실패마다 자기 `catch`를 가집니다:
```swift
do {
    let text = try load(false)
    let value = try parse(text)
    print(value)
} catch NetworkError.offline {
    print("offline")
} catch ParseError.badFormat {
    print("bad format")
} catch {
    print("unknown")
}
```
오류를 던지는 첫 `try`가 블록을 끝내므로 이후 단계는 실행되지 않습니다. 그 값은 아예 존재한 적이 없는 것이죠. 이 모양이 읽기 좋은 이유가 바로 그것입니다. 정상 경로는 위쪽에 한 줄로 곧게 이어지고, 잘못될 수 있는 모든 방식은 그 아래에 나열됩니다.
