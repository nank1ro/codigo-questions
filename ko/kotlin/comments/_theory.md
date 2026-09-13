**주석(comment)**은 소스 코드 안에 작성된, 코드를 읽는 사람을 위한 메모입니다. 컴파일러는 주석을 완전히 무시하므로 주석은 프로그램의 동작을 절대 바꾸지 않습니다.

가장 간단한 주석은 **한 줄 주석(single-line comment)**입니다: `//`로 시작하여 줄 끝까지 이어집니다.
```kotlin
// Greets the user
println("Hello")
```
주석을 사용하여 코드가 어떤 용도인지, 왜 그렇게 작성했는지 설명하세요.

---

주석이 꼭 자기 줄을 가질 필요는 없습니다: 같은 줄에서 코드 뒤에 이어붙일 수도 있습니다. 이를 **후행 주석(trailing comment)**이라고 하며, 해당 명령문에 대한 짧은 메모를 남기기에 좋은 자리입니다:
```kotlin
val retries = 3 // give up after three attempts
```
`//`부터 줄 끝까지의 모든 내용은 무시되고, 그 앞의 코드는 평소처럼 실행됩니다.

---

컴파일러는 주석을 완전히 제거하므로, 주석을 추가하거나 삭제해도 프로그램의 동작은 절대 바뀌지 않습니다. **주석이 아닌** 코드만 실행됩니다.

덕분에 `//`는 코드를 삭제하지 않고 한 줄을 끄는 빠른 방법이 됩니다. 이를 **주석 처리(commenting out)**라고 합니다:
```kotlin
var total = 10
// total = total + 5
println(total) // prints 10
```
두 번째 줄은 이제 주석이므로 `total`은 `10`을 유지합니다. `//`를 제거하면 그 줄은 다시 살아납니다.

주석 처리는 실험할 때 유용하지만, 나중에 정리하는 것을 잊지 마세요: 오랫동안 주석 처리된 채로 남아 있는 코드는 다음에 읽는 사람을 혼란스럽게 할 뿐입니다.

---

주석이 여러 줄에 걸쳐야 할 때는 Kotlin이 **여러 줄 주석(multi-line comment)**(블록 주석이라고도 함)을 제공합니다: `/*`로 시작하여 `*/`로 끝나며, 줄 바꿈을 포함해 그 사이의 모든 내용은 무시됩니다.
```kotlin
/*
  Prints the welcome banner.
  Called once when the app starts.
*/
println("Welcome!")
```
블록 주석은 짧게 한 줄에 머물 수도 있습니다: `/* like this */`.

---

줄 끝에서 멈추는 `//`와 달리, `/*` 주석은 `*/`에서만 멈춥니다. 닫는 것을 잊으면 컴파일러는 이후의 모든 코드를 주석의 일부로 취급하고 오류를 보고합니다:
```kotlin
val width = 10 /* in centimetres
println(width) // still inside the comment: error, the comment is never closed
```
`//`와 `/* */` 모두 후행 주석으로 쓸 수 있지만, `/*`를 사용할 때는 항상 `*/`가 있는지 확인하세요.

---

Java에서 블록 주석은 다른 블록 주석을 포함할 수 없지만, Kotlin에서는 **중첩할 수 있습니다**: 모든 `/*`는 자신만의 `*/`와 짝을 이루어야 하며, 주석은 가장 바깥쪽 것이 닫힐 때 끝납니다.
```kotlin
/* outer /* inner */ still a comment */
println("done")
```
여기서 `still a comment */`는 바깥쪽 주석의 일부이므로 `done`만 출력됩니다. 이 덕분에 코드 블록 전체를 주석 처리할 때, 그 블록 안에 이미 `/* */` 주석이 있어도 괜찮습니다.

---

여러 줄을 한 번에 주석 처리하려면 모든 줄에 `//`를 붙이는 대신 하나의 블록 주석으로 감싸세요:
```kotlin
var total = 100
/*
total = total - 30
total = total - 20
*/
println(total) // prints 100
```
중첩 덕분에 그 줄 중 하나에 이미 `/* */` 주석이 있어도 잘 동작합니다.

---

블록 주석의 흔한 용도는 **헤더 주석(header comment)**입니다: 함수 바로 위에 놓이는 짧은 블록으로, 함수가 하는 일과 매개변수의 의미를 설명합니다.
```kotlin
/*
Returns the number of seconds in the given minutes.
minutes is a whole number, never negative.
*/
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
`toSeconds`를 호출하는 사람은 이제 본문 대신 헤더를 읽으면 됩니다. 헤더는 함수 바로 옆에 두어 함께 업데이트되도록 하세요.

---

Kotlin에는 세 번째 종류의 주석인 **문서화 주석(documentation comment)**이 있으며, **KDoc**이라 불리는 형식으로 작성됩니다: `/**`(슬래시와 별표 두 개)로 시작하여 `*/`로 끝나고, 함수, 클래스 또는 프로퍼티 바로 위에 놓입니다.
```kotlin
/**
 * Returns the greeting for [name].
 */
fun greet(name: String): String {
    return "Hi, $name!"
}
```
컴파일러에게는 그저 주석이지만, IntelliJ IDEA 같은 도구는 이를 읽어 `greet`의 도움말 텍스트로 표시합니다. 안쪽 줄 시작 부분의 `*`는 블록을 정렬된 상태로 유지하는 관례일 뿐입니다. KDoc 안에서는 Markdown을 사용할 수 있고, `[name]` 같은 대괄호는 해당 매개변수로의 링크로 바뀝니다.

---

문서화 주석의 첫 줄은 **요약(summary)**입니다: 함수가 하는 일을 말하는 짧은 문장입니다. 함수를 설명하는 것처럼 3인칭으로 작성하세요: "Returns...", "Adds...", "Checks...".
```kotlin
/**
 * Returns `true` when [n] is divisible by two.
 */
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
```
주석은 다른 명령문 없이 선언 바로 위에 위치해야 합니다. 그렇지 않으면 도구가 주석을 함수에 연결하지 않습니다.

---

요약 다음에는 문서화 주석이 항상 `@`로 시작하는 **KDoc 태그**로 매개변수와 반환값을 설명할 수 있습니다:
```kotlin
/**
 * Returns the number of seconds in the given minutes.
 * @param minutes a whole number of minutes, never negative
 * @return [minutes] multiplied by sixty
 */
fun toSeconds(minutes: Int): Int {
    return minutes * 60
}
```
`@param` 뒤에는 매개변수의 이름과 그 설명이 이어집니다; 매개변수마다 `@param`이 하나씩 있습니다. `@return`은 함수가 돌려주는 값을 설명합니다. 순서는 항상 같습니다: 먼저 요약, 그다음 `@param` 태그, 그다음 `@return`입니다.

---

매개변수가 둘 이상인 함수는 각 매개변수마다 하나의 `@param` 태그를 가지며, 매개변수와 같은 순서로 작성합니다:
```kotlin
/**
 * Returns the area of a rectangle.
 * @param width the horizontal side, in centimetres
 * @param height the vertical side, in centimetres
 * @return the product of [width] and [height]
 */
fun area(width: Int, height: Int): Int {
    return width * height
}
```
태그는 여전히 그저 주석일 뿐입니다: 매개변수 이름을 바꾸고 태그를 잊어도 아무것도 깨지지 않지만, 문서는 거짓말을 시작합니다. KDoc은 시그니처와 함께 업데이트하세요.

---

컴파일러는 코드 안에서만 주석을 찾으며, **문자열 리터럴** 안에서는 절대 찾지 않습니다. 큰따옴표 사이에서 `//`와 `/* */`는 그저 평범한 문자입니다:
```kotlin
println("50 // 2") // prints 50 // 2
```
첫 번째 `//`는 텍스트의 일부이고, 두 번째 것이 진짜 주석을 시작합니다. 사람들이 이것에 가장 자주 놀라는 경우는 프로토콜 바로 뒤에 `//`가 포함된 웹 주소입니다.

---

일부 주석은 편집기가 이해하는 관례를 따릅니다. 가장 흔한 **마커(marker)**는 다음과 같습니다:
- `// TODO: ...`는 아직 작성해야 할 것이 있음을 표시합니다
- `// FIXME: ...`는 잘못되었음이 알려져 수정이 필요한 코드를 표시합니다

```kotlin
val limit = 10
// TODO: read the limit from the settings
```
컴파일러에게 이들은 평범한 주석이지만, IntelliJ IDEA는 전용 도구 창에 모아 두어 남은 작업을 쉽게 찾게 해 줍니다. `TODO`는 보통 실제 구현이 작성될 때까지 코드가 컴파일된 상태로 유지되게 해 주는 자리표시자 옆에 놓입니다. 작업을 완료하면 같은 변경에서 자리표시자를 교체하고 마커를 제거하여, 주석이 코드의 상태에 대해 거짓말을 하지 않도록 하세요.

---

`FIXME`는 `TODO`와 다릅니다: 코드는 이미 존재하지만, 잘못되었음이 알려져 있습니다. 좋은 `FIXME`는 버그가 무엇인지 말해 주고, 가능하다면 그것을 보여주는 예시를 제공하여 다음 사람이 빠르게 고칠 수 있게 합니다. `TODO`와 마찬가지로 버그가 고쳐지면 마커를 삭제하되, 여전히 사실인 문서화 주석은 그대로 두세요.

---

좋은 주석은 코드가 **무엇**을 하는지가 아니라 **왜** 그러는지를 설명합니다. 코드는 이미 무슨 일이 일어나는지 보여주므로, 그것을 말로 반복하면 잡음만 더해지고 코드가 바뀌는 순간 낡아 버립니다:
```kotlin
// set timeout to 30
val timeout = 30
```
그 숫자 뒤에 있는 이유가야말로 읽는 사람이 추측할 수 없는 것입니다:
```kotlin
// the server drops idle connections after 35 seconds, so stop earlier
val timeout = 30
```
주석이 아랫줄을 그저 다시 말할 뿐이라면 삭제하거나 이유로 바꾸세요. 최고의 주석은 코드가 말할 수 없는 것을 말하는 주석입니다.
