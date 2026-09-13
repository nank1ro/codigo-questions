모든 작업이 즉시 끝나는 것은 아닙니다: 파일 다운로드, 데이터베이스 읽기, 타이머 대기가 그렇습니다. 프로그램이 그냥 멈춰서 기다린다면, 그 동안에는 다른 어떤 일도 일어날 수 없습니다. Swift는 **비동기 함수**로 이 문제를 해결합니다.

**`async`**가 표시된 함수는 도중에 멈췄다가 나중에 다시 시작할 수 있습니다. 이 키워드는 매개변수 목록 뒤, 화살표 앞에 씁니다:
```swift
func fetchNumber() async -> Int {
    return 42
}
```
호출하는 방법도 다릅니다: 호출 앞에 **`await`**를 써야 합니다. `await`는 프로그램이 멈출 수 있는 정확한 지점을 표시하고, 함수가 끝나면 평범한 값을 돌려줍니다:
```swift
let n = await fetchNumber()
print(n)
// prints 42
```
Swift 스크립트에서는 최상위 레벨이 이미 `await`를 지원하므로, 별도의 설정 없이도 비동기 함수를 직접 호출할 수 있습니다. `async`나 `await`를 잊으면 조용한 버그가 아니라 컴파일 오류가 됩니다.

---

비동기 함수는 여전히 평범한 함수입니다: 매개변수를 받고 어떤 타입의 값이든 반환할 수 있습니다. 달라지는 것은 두 가지뿐입니다, 시그니처 안의 `async` 키워드와 모든 호출 지점의 `await`입니다:
```swift
func price(of quantity: Int) async -> Double {
    return Double(quantity) * 2.5
}

let total = await price(of: 4)
print(total)
// prints 10.0
```
반환된 값은 래퍼가 아니라 평범한 `Double`입니다: `await`가 끝나면 그 값을 평소와 똑같이 다룹니다.

---

비동기 함수는 보통 서로를 쌓아 만듭니다. `async` 함수 안에서는 다른 `async` 함수를 `await`할 수 있으며, 그 결과는 평범한 값처럼 사용합니다:
```swift
func base() async -> Int {
    return 10
}

func withBonus() async -> Int {
    let value = await base()
    return value + 5
}

print(await withBonus())
// prints 15
```
`await`는 비동기 컨텍스트 안에서만 허용됩니다: `async` 함수 또는 스크립트의 최상위 레벨입니다. 평범한, `async`가 아닌 함수는 아무것도 `await`할 수 없습니다.

---

시간이 걸리는 작업은 실패하기 쉽습니다: 서버가 죽었거나, 파일이 없거나, 입력이 잘못되었을 수 있습니다. 그런 함수는 **`async throws`**로 표시되며 **`try await`**로 호출합니다:
```swift
enum LoadError: Error {
    case missing
}

func load(_ name: String) async throws -> String {
    if name.isEmpty {
        throw LoadError.missing
    }
    return "file: \(name)"
}
```
오류를 처리하려면 호출을 `do` 블록으로 감싸고 catch하세요:
```swift
do {
    let text = try await load("")
    print(text)
} catch {
    print("could not load")
}
// prints could not load
```
키워드의 순서는 정해져 있습니다: `try`가 먼저 오고, 그다음 `await`가 옵니다.

---

호출이 *왜* 실패했는지 신경 쓰지 않을 때는 `try?`가 `do` 블록보다 짧습니다. `try?`는 오류를 던지는 호출을 **옵셔널**로 바꿉니다: 성공하면 값, 실패하면 `nil`입니다. `await`와 결합하면 `try? await`라고 씁니다:
```swift
let value = try? await parse("42")  // Optional(42)
let broken = try? await parse("x")  // nil
```
결과가 옵셔널이므로 `if let`에 그대로 들어맞습니다:
```swift
if let value = try? await parse("x") {
    print(value)
} else {
    print("not a number")
}
```
빠른 폴백에는 `try? await`를, 오류 자체가 중요할 때는 `do` / `catch`를 사용하세요.

---

여러 `await` 호출을 차례로 쓰면 **순차적으로** 실행됩니다: 두 번째 호출은 첫 번째가 반환되기 전에는 시작조차 하지 않습니다. 코드는 위에서 아래로 읽히며, 평범한 코드와 똑같습니다:
```swift
func step(_ name: String) async -> String {
    print("start \(name)")
    return "done \(name)"
}

let a = await step("A")
print(a)
let b = await step("B")
print(b)
// start A
// done A
// start B
// done B
```
두 번째 호출이 첫 번째의 결과를 필요로 할 때는 이것이 바로 원하는 동작입니다. 호출들이 서로 독립적이라면, 하나를 시작하기 전에 다른 하나를 기다리는 것은 낭비이며, 다음 연습문제들은 이를 피하는 방법을 보여줍니다.

---

두 개의 독립적인 호출을 동시에 실행하려면 **`async let`**으로 선언하세요. 작업은 즉시 시작되고, 프로그램은 기다리지 않고 계속 진행됩니다:
```swift
async let left = step("A")
async let right = step("B")
```
값은 아직 준비되지 않았으므로 바인딩을 바로 쓸 수 없습니다: 최종적으로 필요한 지점에서 `await`해야 합니다. 표현식 앞의 `await` 하나가 그 안의 모든 `async let`을 처리합니다:
```swift
let both = await left + right
```
각 호출이 1초 걸린다면 순차 버전은 2초가 필요하지만 `async let` 버전은 두 호출이 겹치기 때문에 약 1초면 충분합니다.

---

결과를 따로따로 필요로 할 때는 여러 `async let` 바인딩을 튜플로 모아 튜플 전체를 한 번에 `await`하세요:
```swift
async let city = fetchCity()
async let country = fetchCountry()
let (a, b) = await (city, country)
```
두 호출은 이미 실행 중이었습니다; `await` 하나는 둘 중 느린 쪽이 끝날 때까지 기다립니다. `async let`은 작업을 시작할 뿐이라는 점을 기억하세요: await하지 않은 `async let`은 스코프가 끝날 때 취소되고 암묵적으로 await됩니다.

---

`async let`은 쓰인 스코프에 묶여 있습니다. 동시 작업을 시작하면서 그 핸들을 유지하려면 **`Task`**를 사용하세요. `Task { }`에 전달된 클로저는 자체적으로 실행되며, 작업은 저장되거나 전달되거나 반환될 수 있습니다:
```swift
let job = Task {
    return await double(21)
}
```
결과는 나중에 **`.value`**로 읽으며, 이는 await됩니다:
```swift
print(await job.value)
// prints 42
```
핸들의 타입은 무엇을 만들어내고 무엇을 던질 수 있는지 말해줍니다: `Task<Int, Never>`는 `Int`를 반환하고 결코 오류를 던지지 않는 작업입니다. `async let`과 달리 `Task`는 평범한, 비동기가 아닌 코드에서 만들 수 있습니다.

---

`Task.sleep`은 다른 것을 막지 않으면서 현재 작업을 잠시 멈춥니다. 중단될 수 있으므로 오류를 던지는 비동기 호출이며 `try await`가 필요합니다. 지속 시간은 `.seconds`, `.milliseconds`, `.nanoseconds` 같은 헬퍼로 지정합니다:
```swift
func slowGreeting() async throws -> String {
    try await Task.sleep(for: .milliseconds(50))
    return "hello"
}
```
이것은 실제 네트워크 호출 대신 예제에서 느린 작업을 시뮬레이션하는 표준 방법입니다. 프로그램을 얼리지 않는다는 점에 주의하세요: 한 작업이 잠들어 있는 동안에도 다른 작업들은 계속 실행됩니다.

---

이제 순차와 동시의 차이를 측정할 수 있습니다. `work`가 반환하기 전에 1초간 잠든다고 해봅시다:
```swift
func work(_ n: Int) async -> Int {
    try? await Task.sleep(for: .seconds(1))
    return n
}
```
호출을 하나씩 await하면 약 **2**초가 걸립니다, 두 번째 잠듦은 첫 번째가 끝나야 시작되기 때문입니다:
```swift
let a = await work(1)
let b = await work(2)
```
`async let`으로 시작하면 약 **1**초가 걸립니다, 두 잠듦이 겹치기 때문입니다:
```swift
async let a = work(1)
async let b = work(2)
let sum = await a + b
```
`await work(1) + await work(2)`를 한 줄에 써도 아무것도 바뀌지 않습니다: 두 호출은 여전히 하나가 끝난 뒤 하나씩 평가됩니다. 동시성은 `async let`이나 작업에서 나오며, 줄을 어떻게 꾸미느냐에서는 결코 나오지 않습니다.

---

`async let`은 코드를 작성하는 시점에 호출이 몇 개인지 알 때 유용합니다. 크기를 실행 시점에만 알 수 있는 목록에는 **작업 그룹**을 사용하세요.

`withTaskGroup(of:)`가 그룹을 열고, `addTask`가 항목마다 하나의 자식 작업을 시작하며, 그룹은 그다음 `for await`로 읽히고, 이는 결과를 끝나는 대로 전달합니다:
```swift
let total = await withTaskGroup(of: Int.self) { group in
    for n in numbers {
        group.addTask {
            return await square(n)
        }
    }
    var sum = 0
    for await value in group {
        sum += value
    }
    return sum
}
```
`of: Int.self`는 모든 자식 작업이 무엇을 반환하는지 선언합니다. `withTaskGroup` 호출 전체는 하나의 표현식이므로 앞에 `await`를 하나 붙여야 하며, 모든 자식 작업이 끝나기 전에는 반환되지 않습니다.

---

작업 그룹은 결과를 추가된 순서가 아니라 **완료 순서**로 건네줍니다. 가장 빠른 자식 작업이 먼저 도착하므로, 값을 배열에 모으면 순서를 예측할 수 없습니다.

순서가 중요할 때는 두 가지 해결책이 있습니다. 값들을 단순히 재정렬해도 된다면 마지막에 정렬하세요:
```swift
return values.sorted()
```
각 결과가 특정 위치에 속한다면 모든 작업이 `(index, value)` 쌍을 반환하게 하고, 미리 준비한 배열에 쓰세요:
```swift
for (index, word) in words.enumerated() {
    group.addTask {
        return (index, await lengthOf(word))
    }
}
var result = Array(repeating: 0, count: words.count)
for await (index, value) in group {
    result[index] = value
}
```
합, 최댓값, 개수는 어느 해결책도 필요하지 않습니다, 값의 순서가 답을 바꾸지 않기 때문입니다.
