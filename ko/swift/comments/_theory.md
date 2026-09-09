**주석(comment)**은 코드를 읽는 사람을 위해 소스 코드 안에 작성하는 메모입니다. 컴파일러는 주석을 완전히 무시하므로, 주석은 프로그램의 동작을 절대 바꾸지 않습니다.

가장 간단한 주석은 **한 줄 주석**입니다: `//`로 시작하여 줄의 끝까지 이어집니다.
```swift
// Greets the user
print("Hello")
```
주석을 사용하여 어떤 코드가 어떤 역할을 하는지, 왜 그렇게 작성되었는지 설명하세요.

---

주석은 꼭 자신만의 줄을 가질 필요는 없습니다: 같은 줄에서 코드 뒤에 이어서 작성할 수도 있습니다. 이를 **후행 주석**이라고 하며, 해당 문장에 대한 짧은 메모를 남기기에 좋은 자리입니다.
```swift
let retries = 3 // give up after three attempts
```
`//`부터 줄의 끝까지는 모두 무시되고, 그 앞의 코드는 평소처럼 실행됩니다.

---

컴파일러는 주석을 완전히 제거하므로, 주석을 추가하거나 삭제해도 프로그램의 동작은 절대 바뀌지 않습니다. 주석 처리되지 **않은** 코드만 실행됩니다.

덕분에 `//`는 코드를 삭제하지 않고도 한 줄을 실행 대상에서 빼는 빠른 방법이 됩니다. 이를 **주석 처리(commenting out)**라고 합니다:
```swift
var total = 10
// total = total + 5
print(total) // prints 10
```
두 번째 줄은 이제 주석이므로 `total`은 `10`으로 유지됩니다. `//`를 제거하면 그 줄은 다시 살아납니다.

주석 처리는 실험할 때 유용하지만, 나중에 정리하는 것을 잊지 마세요: 오랫동안 주석 처리된 채로 남아 있는 코드는 다음에 읽는 사람을 혼란스럽게 만들 뿐입니다.

---

주석이 여러 줄에 걸쳐 필요할 때는 Swift가 **여러 줄 주석**(블록 주석이라고도 함)을 제공합니다: `/*`로 시작하여 `*/`로 끝나며, 줄 바꿈을 포함해 그 사이의 모든 내용은 무시됩니다.
```swift
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
print("Welcome!")
```
블록 주석은 짧게 한 줄에 두는 것도 가능합니다: `/* like this */`.

---

줄 끝에서 멈추는 `//`와 달리, `/*` 주석은 `*/`에서만 끝납니다. 닫는 것을 잊으면 컴파일러는 뒤따르는 모든 코드를 주석의 일부로 취급하고 오류를 보고합니다:
```swift
let width = 10 /* in centimetres
print(width) // still inside the comment: error, the comment is never closed
```
`//`와 `/* */` 모두 뒤따라오는 주석으로 쓸 수 있지만, `/*`를 쓸 때는 항상 `*/`가 있는지 확인하세요.

---

많은 언어에서 블록 주석은 다른 블록 주석을 포함할 수 없지만, Swift에서는 **중첩할 수 있습니다**: 모든 `/*`는 각자의 `*/`와 짝을 이루어야 하며, 주석은 가장 바깥쪽이 닫힐 때에만 끝납니다.
```swift
/* outer /* inner */ still a comment */
print("done")
```
여기서 `still a comment */`는 바깥 주석의 일부이므로 `done`만 출력됩니다. 이 덕분에 이미 `/* */` 주석을 포함한 코드 블록 전체도 주석 처리할 수 있습니다.

---

여러 줄을 한 번에 주석 처리하려면 각 줄에 `//`를 붙이는 대신 하나의 블록 주석으로 감싸세요:
```swift
var total = 100
/*
total = total - 30
total = total - 20
*/
print(total) // prints 100
```
중첩이 가능하므로 그 줄들 중 하나에 이미 `/* */` 주석이 있어도 동작합니다.

---

블록 주석의 흔한 용도는 **헤더 주석**입니다: 함수 바로 위에 두어 그 함수가 무엇을 하는지, 매개변수가 무엇을 뜻하는지 설명하는 짧은 블록입니다.
```swift
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
이제 `toSeconds`를 호출하는 사람은 본문 대신 헤더를 읽을 수 있습니다. 헤더는 함수 옆에 두어 함께 갱신되도록 하세요.

---

Swift에는 세 번째 종류의 주석인 **문서화 주석**이 있습니다: 함수, 타입 또는 프로퍼티 바로 위에 두며 `///`(슬래시 세 개)로 시작하는 한 줄 주석입니다.
```swift
/// Returns the greeting for `name`.
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
컴파일러에게는 그저 주석이지만, Xcode 같은 도구는 이를 읽어 `greet`의 도움말로 보여 줍니다. 문서화 주석은 **마크다운**을 지원하므로 코드에는 백틱을, 그리고 `**굵게**`와 목록을 쓸 수 있습니다.

---

문서화 주석의 첫 줄은 **요약**입니다: 함수가 무엇을 하는지 알려 주는 짧은 문장이죠. 함수를 설명하듯 3인칭으로 쓰세요: "Returns...", "Adds...", "Checks...".
```swift
/// Returns `true` when `n` is divisible by two.
func isEven(_ n: Int) -> Bool {
    return n % 2 == 0
}
```
주석은 선언 바로 위에, 사이에 빈 줄 없이 있어야 합니다. 그렇지 않으면 Xcode가 함수에 연결하지 않습니다.

---

문서화 주석에는 블록 형태도 있습니다: `/**`로 열고 `*/`로 닫으며, 여러 줄 주석과 똑같지만 시작 부분에 별표가 하나 더 붙습니다.
```swift
/**
 Returns the greeting for `name`.

 The result always ends with an exclamation mark.
 */
func greet(_ name: String) -> String {
    return "Hi, \(name)!"
}
```
도구에게 `/// 텍스트`와 `/** 텍스트 */`는 같은 의미입니다. Swift 코드에서는 `///`가 가장 흔하고, `/** */`는 긴 설명에 편리합니다. 함수 위에 두더라도 평범한 `/* */`이나 `//` 주석은 문서화가 **아닙니다**.

---

요약 다음에는 Xcode가 인식하는 특별한 마크다운 목록 항목으로 매개변수와 반환 값을 설명할 수 있습니다:
```swift
/// Returns the number of seconds in the given minutes.
/// - Parameter minutes: a whole number of minutes, never negative
/// - Returns: `minutes` multiplied by sixty
func toSeconds(_ minutes: Int) -> Int {
    return minutes * 60
}
```
순서는 항상 같습니다: 먼저 요약, 그다음 각 매개변수마다 `- Parameter 이름:`, 그리고 `- Returns:`.

---

일부 주석은 편집기가 이해하는 관례를 따릅니다. Swift에서 가장 흔한 **마커**는 다음과 같습니다:
- `// MARK: - 제목`은 파일의 한 구역에 이름을 붙여 Xcode의 탐색 메뉴에 나타나게 합니다
- `// TODO: ...`는 아직 작성해야 할 것을 표시합니다
- `// FIXME: ...`는 잘못된 것으로 알려져 있어 고쳐야 하는 코드를 표시합니다

```swift
// MARK: - Setup
let limit = 10
// TODO: read the limit from the settings
// FIXME: crashes when the list is empty
```
컴파일러에게는 평범한 주석이지만, Xcode가 목록으로 보여 주므로 남은 작업을 찾기 쉽습니다. 작업이 끝나면 마커를 지우세요: 오래된 `TODO`는 오해를 부릅니다.

---

`TODO`는 보통 실제 구현이 작성될 때까지 코드가 컴파일되도록 유지해 주는 자리표시자 옆에 있습니다. 작업을 마치면 같은 변경에서 자리표시자를 바꾸고 마커도 제거하세요. 그래야 주석이 코드 상태에 대해 거짓말하지 않습니다.

---

`FIXME`는 `TODO`와 다릅니다: 코드는 이미 존재하지만 잘못된 것으로 알려져 있습니다. 좋은 `FIXME`는 버그가 무엇인지 말하고, 가능하면 그것을 보여 주는 예를 제시하여 다음 사람이 빠르게 고칠 수 있게 합니다. `TODO`와 마찬가지로 버그를 고치면 마커를 지우되, 여전히 유효한 문서화 주석은 남겨 두세요.

---

좋은 주석은 코드가 **무엇을** 하는지가 아니라 **왜** 그렇게 하는지를 설명합니다. 무슨 일이 일어나는지는 코드가 이미 보여 줍니다. 그것을 말로 반복하면 잡음만 늘고, 코드가 바뀌는 순간 낡은 내용이 됩니다:
```swift
// set timeout to 30
let timeout = 30
```
읽는 사람이 짐작할 수 없는 것은 그 숫자의 이유입니다:
```swift
// the server drops idle connections after 35 seconds, so stop earlier
let timeout = 30
```
주석이 아래 줄을 되풀이하기만 한다면 지우거나 이유로 바꾸세요.
