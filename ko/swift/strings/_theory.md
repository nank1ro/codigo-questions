**문자열**은 텍스트 조각입니다. Swift에서는 큰따옴표 사이에 문자열 리터럴을 작성하며, 그 타입은 `String`입니다:
```swift
let greeting: String = "Hello"
var city = "Rome"
```
다른 값과 마찬가지로, `let`은 변경할 수 없는 상수를 만들고 `var`는 변경할 수 있는 변수를 만듭니다.
Swift는 리터럴로부터 `String` 타입을 추론하므로, 타입 어노테이션은 생략할 수 있습니다.

---

**문자열 보간**은 표현식의 값을 문자열 리터럴 안에 삽입합니다. 표현식은 `\()`로 감쌉니다:
```swift
let name = "Ada"
let age = 36
print("\(name) is \(age) years old") // Ada is 36 years old
```
어떤 타입이든 보간할 수 있습니다: 숫자, 불리언, 다른 문자열 모두 자동으로 텍스트로 변환됩니다.

---

두 문자열은 `+` 연산자로 결합할 수 있으며, 새로운 문자열이 만들어집니다:
```swift
let full = "Hello" + " " + "world" // Hello world
```
기존 문자열 변수의 끝에 텍스트를 추가하려면 `+=`를 사용하세요. 값이 변경되므로 해당 변수는 `var`로 선언되어야 합니다:
```swift
var log = "Start"
log += "..."
print(log) // Start...
```

---

`count` 프로퍼티는 문자열에 포함된 문자 수를 반환하고, `isEmpty`는 문자열에 문자가 전혀 없을 때 `true`가 됩니다:
```swift
print("Swift".count) // 5
print("".isEmpty)    // true
```
공백과 문장 부호를 포함해 모든 문자가 세어집니다.

---

`String`은 `Character` 값들의 컬렉션입니다. `Character`는 하나의 문자, 숫자, 기호, 또는 공백이며, 문자열과 같은 큰따옴표로 작성되므로 이를 얻으려면 타입 어노테이션이 필요합니다:
```swift
let letter: Character = "a"
let text = "abc"
print(text.count) // 3
```
`count`를 `0`과 비교하는 것보다 `isEmpty`를 확인하는 편이 더 좋습니다: 더 읽기 좋고, 모든 문자를 셀 필요도 없기 때문입니다.

---

**여러 줄 문자열 리터럴**은 각각 자기 줄에 놓인 3개의 큰따옴표 `"""`로 시작하고 끝납니다. 그 사이의 모든 줄이 문자열의 일부가 되며, 줄바꿈은 그대로 유지됩니다:
```swift
let poem = """
Roses are red
Violets are blue
"""
print(poem)
```
이렇게 하면 작성된 그대로 두 줄이 출력됩니다. 닫는 `"""`는 들여쓰기도 정합니다: 그 앞에 있는 공백은 모든 줄의 시작 부분에서 제거됩니다.

---

문자열은 문자의 컬렉션이므로 `for`-`in` 루프로 순회할 수 있습니다. 각 반복마다 하나의 `Character`를 얻습니다:
```swift
for letter in "hey" {
    print(letter)
}
// h
// e
// y
```
`Character`는 `==`로 문자 리터럴과 비교할 수 있으므로, 어떤 문자가 몇 번 나타나는지 세는 것은 루프와 카운터만으로 충분합니다.

---

배열과 달리, 문자열은 `text[2]`처럼 정수로 첨자 접근을 할 수 없습니다: 어떤 문자는 다른 문자보다 더 많은 메모리를 차지하기 때문에, Swift는 위치를 가리키는 전용 `String.Index` 타입을 사용합니다.
`startIndex`는 첫 번째 문자의 위치이고, `endIndex`는 마지막 문자 *다음*의 위치입니다. 인덱스를 이동하려면 `index(_:offsetBy:)`를 사용한 다음, 그 결과로 문자열에 첨자 접근을 하세요:
```swift
let word = "Swift"
let second = word.index(word.startIndex, offsetBy: 1)
print(word[second]) // w
```
문자열의 끝을 넘어가면 런타임에 충돌하므로, 오프셋은 `count` 범위 안에 있어야 합니다.

---

인덱스를 다루는 것은 장황하므로, Swift는 가장 흔한 경우를 위한 지름길을 제공합니다:
- `first`와 `last`는 첫 번째와 마지막 문자를 옵셔널 `Character?`로 반환합니다(빈 문자열이면 `nil`)
- `prefix(n)`은 처음 `n`개의 문자를, `suffix(n)`은 마지막 `n`개의 문자를 반환합니다
```swift
let word = "Swift"
print(word.first!)     // S
print(word.prefix(2))  // Sw
print(word.suffix(3))  // ift
```
`prefix`와 `suffix`는 원본 텍스트에 대한 뷰인 `Substring`을 반환합니다. 실제 `String`으로 저장하려면 `String(...)`으로 감싸세요. `n`이 `count`보다 크면 그냥 전체 문자열을 얻습니다.

---

세 가지 메서드가 문자열 내용에 대한 가장 흔한 질문에 답해주며, 모두 `Bool`을 반환합니다:
- `contains(_:)`는 주어진 텍스트(또는 문자)가 어디든 포함되어 있으면 `true`입니다
- `hasPrefix(_:)`는 문자열이 주어진 텍스트로 시작하면 `true`입니다
- `hasSuffix(_:)`는 문자열이 주어진 텍스트로 끝나면 `true`입니다
```swift
let email = "ada@example.com"
print(email.contains("@"))          // true
print(email.hasPrefix("ada"))       // true
print(email.hasSuffix(".org"))      // false
```
셋 다 대소문자를 구분합니다: `"Swift".hasPrefix("s")`는 `false`입니다.

---

`contains`, `hasPrefix`, `hasSuffix`는 불리언을 반환하므로, `||`와 `&&`와 자연스럽게 조합해 더 복잡한 검사를 만들 수 있습니다.

---

`uppercased()`와 `lowercased()`는 모든 글자를 대문자 또는 소문자로 바꾼 **새로운** 문자열을 반환합니다. 원본 문자열은 수정되지 않습니다:
```swift
let name = "Swift"
print(name.uppercased()) // SWIFT
print(name.lowercased()) // swift
print(name)              // Swift
```
둘 다 메서드이므로 괄호를 잊지 마세요.

---

소문자로 변환하는 것은 대소문자를 무시하고 텍스트를 비교하는 일반적인 방법입니다: 대소문자만 다른 두 문자열은 둘 다 소문자로 바꾸면 같아집니다.

---

`split(separator:)`는 구분자 문자가 나타날 때마다 문자열을 조각 배열로 나눕니다. `joined(separator:)`는 그 반대로, 배열의 요소들을 하나의 문자열로 이어붙이면서 그 사이에 구분자를 넣습니다:
```swift
let parts = "a-b-c".split(separator: "-") // ["a", "b", "c"]
print(parts.count)                         // 3
print(parts.joined(separator: ", "))       // a, b, c
```
`prefix`와 마찬가지로 `split`은 `Substring` 값을 반환합니다. `String`으로 저장해야 한다면 `String(...)`으로 감싸세요.

---

공백으로 분할하는 것은 문장을 단어로 나누는 가장 간단한 방법이며, 결합은 배열로부터 텍스트를 다시 만드는 방법입니다.

---

Foundation 프레임워크는 다양한 추가 문자열 메서드를 제공합니다. 가장 유용한 것 중 하나가 `replacingOccurrences(of:with:)`로, 첫 번째 텍스트의 모든 출현을 두 번째 텍스트로 바꾼 새 문자열을 반환합니다:
```swift
import Foundation

let path = "a/b/c"
print(path.replacingOccurrences(of: "/", with: "-")) // a-b-c
```
파일 맨 위에서 `import Foundation`을 잊지 마세요. 그렇지 않으면 이 메서드를 사용할 수 없습니다. 메서드 호출은 체이닝할 수 있으므로, `text.lowercased().replacingOccurrences(of: " ", with: "_")`도 유효합니다.

---

문자열은 숫자와 같은 연산자로 비교할 수 있습니다. `==`는 두 문자열이 정확히 같은 문자를 가지는지 확인하고, `<`와 `>`는 문자 단위로 사전순으로 비교합니다:
```swift
print("apple" == "apple")  // true
print("apple" < "banana")  // true
print("car" < "cat")       // true
```
이 비교는 대소문자를 구분하며, 모든 대문자는 모든 소문자보다 **앞**에 옵니다. 그래서 `"B" < "a"`는 `true`입니다.

---

`Character`는 `String`이 아니므로 `+`로 문자열에 직접 결합할 수 없습니다. 먼저 `String(...)`으로 변환하세요:
```swift
let letter: Character = "a"
let text = String(letter) + "bc" // abc
```
이를 `for`-`in` 루프와 결합하면, 예를 들어 새 문자를 지금까지 모은 것들 앞에 두는 식으로, 한 번에 한 문자씩 문자열을 다시 만들 수 있습니다.
