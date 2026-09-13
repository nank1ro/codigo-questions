**정규 표현식(regular expression, regex)**은 텍스트의 모양을 기술하는 작은 패턴입니다: "숫자 묶음", "등호가 뒤따르는 단어", "대문자 세 개". 문자마다 반복문을 작성하는 대신, 모양을 한 번만 기술하면 Swift가 찾아냅니다.

Swift는 정규 표현식을 `#/`와 `/#` 사이에 씁니다:
```swift
let digits = #/\d+/#
```
패턴 안에서 `\d`는 "임의의 숫자 한 개"를, `+`는 "앞의 것이 하나 이상"을 뜻하므로, `\d+`는 "하나 이상의 숫자 묶음"을 뜻합니다.

가장 단순한 질문은 텍스트가 매치를 포함하는지입니다. `contains(_:)`는 정규 표현식을 받아 `Bool`을 반환합니다:
```swift
print("order42".contains(#/\d+/#)) // true
print("order".contains(#/\d+/#))   // false
```
여기에 보이는 `#/ ... /#` 형태를 항상 사용하세요: 더 짧은 `/ ... /` 표기는 패턴이 메서드 호출 안에 직접 작성될 때 컴파일러를 혼란스럽게 만듭니다.

---

몇 가지 축약 표현만으로 대부분의 패턴을 다룰 수 있습니다. 각각은 정확히 **한** 문자와 일치합니다:
- `\d`는 숫자 한 개입니다
- `\w`는 글자, 숫자 또는 밑줄 한 개입니다
- `\s`는 공백, 탭 또는 줄바꿈 한 개입니다
- `.`는 임의의 문자 한 개입니다

한 개보다 많은 문자와 일치시키려면 패턴 바로 뒤에 **수량자(quantifier)**를 붙입니다:
- `+`는 하나 이상을 뜻합니다
- `*`는 0개 이상을 뜻합니다
- `?`는 0개 또는 1개를 뜻합니다

따라서 `\w+`는 단어, `\s*`는 있어도 없어도 되는 공백, `\d?`는 있어도 없어도 되는 숫자입니다:
```swift
print("hello world".contains(#/\w+\s\w+/#)) // true
print("hello".contains(#/\w+\s\w+/#))       // false
```
특별한 의미가 없는 문자는 자기 자신과 일치할 뿐이므로, `#/cat/#`는 세 글자 `cat`과 일치합니다.

---

기본적으로 패턴은 텍스트 안 어디든 일치할 수 있습니다. **앵커(anchor)**는 대신 패턴을 특정 위치에 묶습니다:
- `^`는 "텍스트의 시작"을 뜻합니다
- `$`는 "텍스트의 끝"을 뜻합니다

```swift
print("swift".contains(#/^sw/#))  // true, the text starts with sw
print("myswift".contains(#/^sw/#)) // false, sw is not at the start
print("swift".contains(#/ft$/#))  // true, the text ends with ft
```
앵커는 문자가 아니라 위치와 일치하므로, 매치에 아무것도 더하지 않습니다.

---

축약 표현이 맞지 않을 때는 받아들일 문자를 대괄호 사이에 나열합니다. `[abc]`는 `a` 한 개, `b` 한 개 또는 `c` 한 개와 일치하고, 대시는 범위를 씁니다:
```swift
print("f".contains(#/[a-f]/#))  // true
print("Z".contains(#/[A-Z]/#))  // true
print("5".contains(#/[0-9a-f]/#)) // true
```
중괄호 안의 숫자는 앞의 패턴이 정확히 몇 번 반복되는지 말해줍니다: `{3}`은 세 번, `{2,4}`는 두 번에서 네 번 사이를 뜻합니다:
```swift
print("aaa".contains(#/^a{3}$/#))  // true
print("aa".contains(#/^a{3}$/#))   // false
```
패턴을 `^`와 `$`로 감싸고 개수를 붙이는 것은 텍스트 전체가 주어진 모양을 갖는지 검사하는 일반적인 방법입니다.

---

`contains(_:)`는 예스나 노만 말해줍니다. 매치된 텍스트를 얻으려면 `firstMatch(of:)`를 사용하세요. 이 메서드는 **옵셔널 매치**를 반환합니다: 아무것도 일치하지 않으면 `nil`이므로, `if let`과 자연스럽게 어울립니다.

매치된 텍스트는 매치의 프로퍼티 `0`에 저장되며, `m.0`으로 씁니다:
```swift
let text = "order 42 today"
if let m = text.firstMatch(of: #/\d+/#) {
    print(m.0) // 42
}
```
`firstMatch(of:)`는 첫 번째 매치에서 멈춥니다. 텍스트에 더 많은 매치가 있어도 마찬가지입니다.

---

`m.0`은 `String`이 아니라 `Substring`입니다: 원본 텍스트를 들여다보는 뷰이지 복사본이 아닙니다. 문자열과 똑같이 출력되지만, `String`이 필요한 곳에서는 변환해야 합니다:
```swift
let text = "order 42"
if let m = text.firstMatch(of: #/\d+/#) {
    let found: String = String(m.0)
    print(found) // 42
}
```
숫자 이니셜라이저는 `Substring`을 바로 받아들이므로, `Int(m.0)`는 우회 없이 동작합니다.

---

`matches(of:)`는 첫 번째 대신 **모든** 매치를 배열로 반환합니다. 이 배열은 절대 `nil`이 아닙니다: 아무것도 일치하지 않으면 그저 비어 있을 뿐이므로, 바로 반복하거나 변환할 수 있습니다:
```swift
let text = "a1 b22"
print(text.matches(of: #/\d+/#).count) // 2
```
각 요소는 매치이므로, `map` 안에서 `$0.0`은 매치된 텍스트입니다:
```swift
let found = text.matches(of: #/\d+/#).map { String($0.0) }
print(found) // ["1", "22"]
```

---

`Int(_:)`가 `Substring`을 받아들이므로, 찾은 텍스트를 숫자로 바꾸는 것은 한 단계입니다. 여기서 `compactMap`이 유용합니다: `nil`로 돌아오는 값을 버립니다:
```swift
let text = "a1 b22"
let numbers = text.matches(of: #/\d+/#).compactMap { Int($0.0) }
print(numbers) // [1, 22]
```
모든 요소가 변환될 때는 `map`을, 일부가 실패할 수 있을 때는 `compactMap`을 사용하세요.

---

패턴의 일부를 둘러싼 둥근 괄호는 **캡처 그룹(capture group)**을 만듭니다: 전체 매치는 여전히 `m.0`이고, 괄호 안의 부분은 `m.1`이 됩니다:
```swift
let text = "id-42"
if let m = text.firstMatch(of: #/id-(\d+)/#) {
    print(m.0) // id-42
    print(m.1) // 42
}
```
이렇게 하면 관심 있는 부분은 남기고 주변 텍스트는 버릴 수 있습니다. 괄호가 없으면 `m.1`은 아예 존재하지 않고, 코드는 컴파일되지 않습니다.

---

패턴에는 그룹이 여러 개 들어갈 수 있습니다. 그룹은 여는 괄호를 기준으로 왼쪽에서 오른쪽으로 번호가 매겨지므로, 두 번째는 `m.2`, 세 번째는 `m.3`입니다:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/([a-z]+)=(\d+)/#) {
    print(m.1, m.2) // size 10
}
```
그룹의 개수와 상관없이 `m.0`은 언제나 전체 매치입니다.

---

패턴이 커지면 괄호를 세는 방식은 금방 불안정해집니다. 대신 여는 괄호 바로 뒤에 `?<name>`을 써서 그룹에 **이름**을 붙이고, 매치의 프로퍼티처럼 읽으세요:
```swift
let text = "size=10"
if let m = text.firstMatch(of: #/(?<key>[a-z]+)=(?<value>\d+)/#) {
    print(m.key)   // size
    print(m.value) // 10
}
```
이름 있는 그룹에도 번호는 그대로 매겨지므로 `m.1`은 계속 동작하지만, `m.key`는 무엇을 담고 있는지 알려 주고 패턴이 바뀌어도 살아남습니다.

---

`replacing(_:with:)`는 모든 매치를 고정된 텍스트로 바꾼 새 `String`을 반환하며, 원본은 그대로 둡니다:
```swift
let text = "a1 b22"
print(text.replacing(#/\d+/#, with: "#")) // a# b#
print(text)                               // a1 b22
```
`\d+`는 연속된 숫자 묶음 전체를 `#` 하나로 바꾸지만, `\d`는 숫자를 하나씩 바꾼다는 점에 주목하세요. 얼마나 사라질지는 패턴이 결정합니다.

---

`split(separator:)`도 정규 표현식을 받을 수 있어서, 항상 같은 모양으로 쓰이지 않는 구분자를 한 번의 호출로 처리할 수 있습니다:
```swift
let line = "a, b;c"
let parts = line.split(separator: #/[,;]\s*/#)
print(parts.joined(separator: "|")) // a|b|c
```
패턴 `[,;]\s*`는 "쉼표 또는 세미콜론 뒤에 오는 임의 개수의 공백"을 뜻하므로 구분자가 통째로 소비되고 빈 항목이 생기지 않습니다. 결과는 `Substring`의 배열입니다.

---

`^`와 `$`로 텍스트 전체를 검사할 수도 있지만, `wholeMatch(of:)`는 그 의도를 직접 표현합니다. 패턴이 첫 문자부터 마지막 문자까지 텍스트를 모두 덮을 때만 매치를 반환하고, 그렇지 않으면 `nil`을 반환합니다:
```swift
print("1a2b".wholeMatch(of: #/[0-9a-f]+/#) != nil) // true
print("1z".wholeMatch(of: #/[0-9a-f]+/#) != nil)   // false
```
텍스트 안에서 무언가를 찾을 때는 `firstMatch(of:)`를, 텍스트가 정확히 하나의 형태인지 확인할 때는 `wholeMatch(of:)`를 사용하세요.

---

`#/ ... /#` 리터럴은 컴파일 시점에 고정됩니다. 사용자가 입력한 경우처럼 패턴을 실행 중에야 알 수 있다면 `Regex(_:)`로 만드세요:
```swift
let regex = try Regex("[0-9]+")
print("abc123".contains(regex)) // true
```
이 이니셜라이저는 **throw**합니다. `"["` 같은 잘못된 패턴은 프로그램이 실행될 때에야 발견되므로 호출에 `try`가 필요하고, 에러는 `do`/`catch`(또는 `try?`)로 처리하거나 이 연습처럼 감싸는 함수에 `throws`를 붙여 전파해야 합니다. 이렇게 만든 정규 표현식에는 컴파일 시점에 알려진 번호 프로퍼티가 없지만, `contains`, `matches(of:)`, `replacing`은 이전과 똑같이 동작합니다.
