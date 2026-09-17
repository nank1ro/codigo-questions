**클로저**는 나중에 전달하고 호출할 수 있는 코드 블록으로, 이름이 없는 함수와 같습니다.
클로저 표현식의 전체 문법은 매개변수와 반환 타입을 중괄호 안에 쓰고, 그 뒤에 `in` 키워드와 본문을 씁니다:
```swift
{ (parameters) -> ReturnType in
    body
}
```
다른 값과 마찬가지로 클로저는 상수에 저장한 뒤 그 상수의 이름으로 호출할 수 있습니다:
```swift
let greet = { (name: String) -> String in
    return "Hello, \(name)!"
}
print(greet("Ada")) // Hello, Ada!
```

---

클로저 안에 모든 타입을 적는 것은 대부분 불필요합니다. 상수가 명시적인 **함수 타입**을 가지면 Swift가 매개변수와 반환 타입을 추론하므로, `in` 앞에 매개변수 이름만 나열하면 됩니다:
```swift
let triple: (Int) -> Int = { n in
    return n * 3
}
```
`(Int) -> Int`라는 타입은 "`Int`를 받아 `Int`를 반환하는 함수"라고 읽습니다.
본문이 단일 표현식일 때는 `return` 키워드도 생략할 수 있는데, 이를 **암묵적 반환**이라고 합니다:
```swift
let triple: (Int) -> Int = { n in n * 3 }
print(triple(4)) // 12
```

---

Swift는 한 걸음 더 나아가, 클로저 안에서는 매개변수를 선언하거나 `in` 키워드를 쓰지 않고도 **축약 인수 이름**인 `$0`, `$1`, `$2` 등으로 인수를 참조할 수 있습니다.
`$0`은 첫 번째 인수, `$1`은 두 번째 인수입니다:
```swift
let add: (Int, Int) -> Int = { $0 + $1 }
print(add(2, 3)) // 5
```
타입은 여전히 `(Int, Int) -> Int`라는 주석에서 옵니다.

---

클로저는 값이므로 함수가 이를 매개변수로 받을 수 있습니다. 매개변수의 타입은 그냥 함수 타입입니다:
```swift
func apply(_ n: Int, _ operation: (Int) -> Int) -> Int {
    return operation(n)
}
print(apply(5, { $0 + 1 })) // 6
```
함수 `apply`는 `operation`이 무엇을 하는지 모릅니다. `Int`를 받아 `Int`를 반환한다는 것만 알고, 다른 함수와 마찬가지로 그것을 호출합니다.

---

클로저가 함수의 **마지막** 인수일 때는 호출의 닫는 괄호 뒤에 그것을 쓸 수 있습니다. 이것이 **후행 클로저** 문법입니다:
```swift
print(apply(5) { $0 + 1 }) // 6
```
클로저가 유일한 인수라면 괄호를 아예 생략할 수도 있습니다:
```swift
func run(_ task: () -> Int) -> Int {
    return task()
}
print(run { 42 }) // 42
```
두 형태 모두 정확히 같은 함수를 호출하지만, 클로저가 길 때는 후행 문법이 읽기 더 쉽습니다.

---

클로저는 이를 인수로 받는 배열 메서드에서 진가를 발휘합니다. `map`은 모든 요소에 대해 클로저를 호출하고 그 결과로 이루어진 새 배열을 반환합니다:
```swift
let nums = [1, 2, 3]
let doubled = nums.map { $0 * 2 }
print(doubled) // [2, 4, 6]
```
원래 배열은 변경되지 않습니다. `map`은 클로저 인수를 하나만 받으므로, 후행 클로저 문법이 이를 호출하는 일반적인 방식입니다.

---

`filter`는 클로저가 `true`를 반환한 요소만 남깁니다. 클로저는 요소 하나를 받아 `Bool`을 반환해야 합니다:
```swift
let nums = [5, 12, 8, 20]
let big = nums.filter { $0 > 10 }
print(big) // [12, 20]
```
요소는 원래 순서를 유지하며, 결과는 같은 요소 타입의 새 배열입니다.

---

`reduce`는 모든 요소를 하나의 값으로 합칩니다. 초깃값과, 두 개의 인수(지금까지 누적된 값과 현재 요소)를 받는 클로저를 인수로 받습니다. 클로저는 새로운 누적값을 반환합니다:
```swift
let nums = [1, 2, 3, 4]
let product = nums.reduce(1) { $0 * $1 }
print(product) // 24
```
여기서 `$0`은 `1`에서 시작해 `1 * 1`, `1 * 2`, `2 * 3`, 그리고 마지막으로 `6 * 4`가 됩니다.
`map`, `filter`, `reduce`는 모두 값을 반환하므로 `nums.filter { $0 > 1 }.map { $0 * 10 }`처럼 연결할 수 있습니다.

---

`sorted(by:)`는 새로 정렬된 배열을 반환합니다. 클로저는 두 요소를 받아 첫 번째 요소가 두 번째 요소보다 **앞에** 와야 할 때 `true`를 반환합니다:
```swift
let nums = [3, 1, 2]
print(nums.sorted { $0 < $1 }) // [1, 2, 3]
print(nums.sorted { $0 > $1 }) // [3, 2, 1]
```
클로저는 무엇이든 비교할 수 있습니다. 예를 들어 `words.sorted { $0.count < $1.count }`는 문자열을 짧은 것부터 긴 것 순으로 정렬합니다.

---

클로저는 자신의 본문 밖에서 선언된 변수를 사용할 수 있습니다. 클로저는 그 변수를 **캡처**합니다. 즉, 그 변수를 선언한 함수가 이미 반환되었더라도, 클로저가 존재하는 한 그 변수는 계속 살아 있습니다.
이를 통해 함수는 자신만의 프라이빗한 상태를 가진 클로저를 만들 수 있습니다:
```swift
func makeCounter() -> () -> Int {
    var count = 0
    return {
        count += 1
        return count
    }
}
```
`() -> Int`는 매개변수가 없고 `Int`를 반환하는 클로저의 타입입니다. 반환된 클로저를 호출할 때마다 캡처된 같은 `count`가 증가합니다:
```swift
let counter = makeCounter()
print(counter()) // 1
print(counter()) // 2
```

---

클로저를 반환하는 것은 커스터마이즈된 함수를 만드는 편리한 방법입니다. 바깥 함수의 매개변수는 그 함수가 반환하는 클로저에 캡처됩니다:
```swift
func makeAdder(_ amount: Int) -> (Int) -> Int {
    return { $0 + amount }
}
let addFive = makeAdder(5)
print(addFive(10)) // 15
```
반환 타입 `(Int) -> Int`는 그 클로저를 나타내며, 축약형 `$0`은 `makeAdder`의 인수가 아니라 그 클로저의 인수를 가리킵니다.

---

상수에 저장된 클로저는 매개변수의 인자 레이블을 사용해 클로저 인수가 필요한 곳이라면 어디든 전달할 수 있습니다:
```swift
let ascending = { (a: Int, b: Int) -> Bool in a < b }
print([3, 1, 2].sorted(by: ascending)) // [1, 2, 3]
```

---

클로저를 반환하는 함수를 호출할 때마다 **새로운** 캡처 변수가 만들어집니다. 서로 다른 호출로 만들어진 두 클로저는 상태를 공유하지 않습니다:
```swift
let first = makeCounter()
let second = makeCounter()
print(first())  // 1
print(first())  // 2
print(second()) // 1
```
상태는 같은 클로저를 호출할 때만 공유됩니다.

---

기본적으로 함수에 전달된 클로저는 그 함수가 실행되는 동안에만 사용될 수 있습니다. 함수가 클로저를 저장하거나 그것을 사용하는 다른 클로저를 반환하면, 그 클로저는 함수를 **탈출**한다고 하며, 해당 매개변수에는 `@escaping`을 표시해야 합니다:
```swift
func twice(_ task: @escaping () -> Int) -> () -> Int {
    return { task() * 2 }
}
let answer = twice { 21 }
print(answer()) // 42
```
`@escaping`이 없으면 컴파일러가 오류를 보고합니다. 반환된 클로저가 `twice`가 끝난 뒤에 `task`를 사용하게 되기 때문입니다.

---

클로저는 다른 값과 마찬가지로 배열에 저장할 수 있습니다. 요소의 타입은 함수 타입입니다:
```swift
let steps: [(Int) -> Int] = [{ $0 + 1 }, { $0 * 10 }]
print(steps[1](3)) // 30
```
이런 배열을 반복하면서 각 클로저를 순서대로 호출하면 작은 변환 **파이프라인**을 만들 수 있습니다.
