**예외(exception)**는 Kotlin에서 어떤 명령문을 수행할 수 없음을 보고하는 방식입니다. `"abc"`를 숫자로 바꾸거나, 정수를 0으로 나누거나, 리스트의 끝을 넘어 읽는 일은 모두 예외를 던집니다.

```kotlin
fun main() {
    println("before")
    val n = "abc".toInt()
    println("after")
}
```
이 프로그램은 `before`를 출력한 뒤 멈춥니다. `toInt()`는 `"abc"`를 읽을 수 없으므로 `NumberFormatException`을 **던집니다**; 프로그램 안에서 이를 처리하는 곳이 없으므로 Kotlin은 오류 보고와 함께 프로그램을 종료하고 `after`는 결코 출력되지 않습니다.

`throw` 키워드를 사용하여 직접 예외를 던질 수도 있습니다:
```kotlin
throw Exception("something went wrong")
```

아무도 처리하지 않는 예외는 경고가 아닙니다: 그것이 곧 실행의 끝입니다.

---

프로그램을 계속 살아 있게 하려면 위험한 명령문을 `try` 블록 안에 넣고 복구 방법을 `catch` 블록에 기술합니다:
```kotlin
try {
    println("abc".toInt())
} catch (e: Exception) {
    println("cannot read that number")
}
println("still running")
```
Kotlin은 `try` 블록을 실행합니다; 그 안의 명령문이 던지는 즉시 블록의 나머지 부분은 건너뛰어지고 제어가 `catch` 블록으로 이동합니다. 괄호 안의 이름 — 여기서는 `e` — 는 예외 객체이고, `Exception`은 잡히는 타입입니다.

`catch` 블록이 끝나면 프로그램은 전체 `try`/`catch` 뒤의 줄에서 정상적으로 계속됩니다.

---

`Exception`을 잡으면 모든 것이 잡히는데, 이는 바라는 경우가 드뭅니다: 블록 안 다른 곳의 오타도 함께 삼켜지기 때문입니다. 대신 복구 방법을 아는 **정확한 타입**을 명시하세요.

각 실패에는 고유한 타입이 있습니다. `"abc".toInt()`는 `NumberFormatException`을 던지므로, 잡을 타입은 이것입니다:
```kotlin
try {
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("that is not a number")
}
```
블록 안에서 다른 종류의 예외가 던져지면 이 `catch`는 일치하지 않고, 예외는 함수 바깥으로 계속 전파됩니다.

---

하나의 `try` 뒤에는 여러 개의 `catch` 블록이 올 수 있으며, 각각 다른 타입을 처리합니다:
```kotlin
val letters = listOf("a", "b")
val index = 5
val text = "abc"
try {
    println(letters[index] + text.toInt())
} catch (e: NumberFormatException) {
    println("not a number")
} catch (e: IndexOutOfBoundsException) {
    println("no such letter")
} catch (e: Exception) {
    println("something else went wrong")
}
```
Kotlin은 블록을 **위에서 아래로** 시도해 보고 타입이 일치하는 첫 번째 블록을 실행합니다. 단 하나의 블록만 실행됩니다.

따라서 순서가 중요합니다. `NumberFormatException`과 `IndexOutOfBoundsException`은 모두 `Exception`의 한 종류이므로, `catch (e: Exception)`을 먼저 쓰면 모든 실패와 일치하여 그 아래 블록들은 결코 실행되지 않습니다. 가장 구체적인 타입을 먼저 쓰고 가장 일반적인 타입을 마지막에 쓰세요.

---

`finally` 블록을 마지막에 추가할 수 있습니다. 이 블록은 **무슨 일이 있어도** 실행됩니다: `try`가 성공한 후에도, `catch`가 복구한 후에도, 심지어 예외가 전혀 잡히지 않을 때에도 실행됩니다.

```kotlin
try {
    println("reading")
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("bad number")
} finally {
    println("closing")
}
```
```
reading
bad number
closing
```
그래서 파일 닫기처럼 건너뛰어서는 안 되는 정리 작업을 넣는 장소가 됩니다. `try`에는 최소한 `catch`나 `finally` 중 하나가 필요하지만, 둘 다 가질 수도 있습니다.

---

Kotlin에서 `try`는 단순한 명령문이 아닙니다: 값을 산출하는 **표현식**입니다. 그 값은 실행된 블록의 마지막 표현식입니다 — 아무것도 실패하지 않으면 `try` 블록, 실패했으면 `catch` 블록입니다.

```kotlin
val n = try { "abc".toInt() } catch (e: NumberFormatException) { 0 }
println(n) // 0
```
이것이 Kotlin에서 관용적인 형태입니다. `var`를 선언하고 두 곳에서 대입한 뒤 모든 경로가 값을 설정하리라 희망하는 대신, 언제나 사용 가능한 값을 담는 하나의 `val`을 얻습니다.

`finally` 블록은 결코 그 값을 바꾸지 않는다는 점에 유의하세요: 오직 부수 효과를 위해서만 실행됩니다.

---

`try`가 표현식이기 때문에 값이 기대되는 어디에서든 사용할 수 있습니다 — `=`로 작성된 함수의 전체 본문으로도 사용할 수 있습니다:
```kotlin
fun length(text: String): Int = try {
    text.toInt()
} catch (e: NumberFormatException) {
    -1
}
```
두 블록은 모두 같은 타입의 값을 산출해야 하며, 여기서는 `Int`입니다. 대체 값을 `catch` 블록의 마지막 표현식으로 쓰세요; 어느 블록 안에도 `return`은 없습니다.

---

던지고 잡는 데는 비용이 들며, 흔한 변환을 위해 Kotlin은 던지는 대신 단순히 `null`을 반환하는 더 저렴한 변형을 제공합니다: `toIntOrNull()`, `toDoubleOrNull()`, `toLongOrNull()`.

```kotlin
println("42".toIntOrNull())  // 42
println("abc".toIntOrNull()) // null
```
왼쪽 값이 `null`일 때 대체 값을 공급하는 엘비스(Elvis) 연산자 `?:`와 결합하면, 전체 `try`/`catch`가 한 줄로 압축됩니다:
```kotlin
val n = "abc".toIntOrNull() ?: 0
println(n) // 0
```
실패가 정말로 예외적인 상황일 때는 `try`/`catch`를, 잘못된 입력이 예상될 때는 `toIntOrNull()`을 사용하세요.

---

여러분의 함수도 표준 라이브러리와 똑같이 `throw`를 사용하여 잘못된 입력을 거절할 수 있습니다. 라이브러리는 가장 흔한 경우를 위한 타입을 이미 제공합니다: `IllegalArgumentException`은 "넘겨받은 값이 받아들일 수 없다"는 뜻입니다.

```kotlin
fun half(n: Int): Int {
    if (n < 0) throw IllegalArgumentException("n must not be negative")
    return n / 2
}
```
`throw`는 함수를 즉시 끝냅니다 — 그 아래의 `return`은 결코 도달하지 못합니다. 이를 어떻게 처리할지는 호출자가 결정합니다:
```kotlin
try { println(half(-4)) }
catch (e: IllegalArgumentException) { println("rejected") }
```
만들어낸 값을 조용히 반환하는 것보다 던지는 것이 낫습니다: 잘못된 답은 멀리까지 퍼지지만, 예외는 처리할 준비가 된 첫 번째 호출자에서 멈춥니다.

---

모든 예외는 생성될 때 받은 텍스트를 담고 있습니다. `catch` 블록 안에서는 예외 객체의 `message` 프로퍼티를 통해 이를 읽습니다:
```kotlin
try {
    throw IllegalArgumentException("price must be positive")
} catch (e: IllegalArgumentException) {
    println(e.message) // price must be positive
}
```
`message`는 널 가능합니다. 예외는 텍스트 없이 만들어질 수도 있기 때문입니다; 일반 `String`이 필요할 때는 `e.message ?: "unknown"`이 안전한 대체 값을 제공합니다.

예외 객체 자체를 출력하기보다 `e.message`를 출력하는 것이 좋습니다: 객체 자체의 텍스트에는 클래스 이름도 포함되는데, 이는 출력을 읽는 사람에게는 잡음입니다.

---

모든 인자에 `if (...) throw IllegalArgumentException(...)`을 쓰면 코드가 번잡해지므로, Kotlin은 평이한 문장처럼 읽히는 두 가지 축약형을 제공합니다:

```kotlin
require(n >= 0) { "n must not be negative" }   // IllegalArgumentException을 던집니다
check(started) { "not started" }               // IllegalStateException을 던집니다
```
둘 다 조건과 메시지를 만들어내는 블록을 받으며, 둘 다 **조건이 거짓일 때** 던집니다. 유일한 차이는 예외 타입이고, 그 차이는 읽는 사람에게 전달되는 메시지입니다:

* `require`는 호출자가 넘긴 **인자**를 보호하며, `IllegalArgumentException`으로 실패합니다.
* `check`는 객체나 프로그램의 **상태**를 보호하며, `IllegalStateException`으로 실패합니다.

블록은 검사가 실패할 때만 평가되므로, 정상 경로에서는 메시지를 만드는 비용이 들지 않습니다.

---

내장 타입 중 어느 것도 여러분의 실패를 잘 설명하지 못할 때는 직접 선언하세요. 예외는 `Exception`을 확장하고 자신의 텍스트를 부모에 넘겨주는 평범한 클래스입니다:

```kotlin
class InsufficientFundsException(message: String) : Exception(message)
```
이 한 줄이 완전한 예외 타입입니다. 다른 예외와 똑같이 던지고 잡을 수 있으며, `e.message`는 생성될 때 받은 텍스트를 반환합니다:
```kotlin
try {
    throw InsufficientFundsException("balance too low")
} catch (e: InsufficientFundsException) {
    println(e.message) // balance too low
}
```
얻는 것은 정밀함입니다: 호출자는 `InsufficientFundsException`만 따로 잡고 다른 모든 실패는 계속 전파되도록 할 수 있습니다.

---

`runCatching`은 블록을 실행하며 예외가 밖으로 새어 나가지 않게 합니다. 대신 `Result`를 돌려주는데, 이는 블록이 만들어낸 값 **또는** 블록이 던진 예외를 담는 객체입니다:

```kotlin
val ok = runCatching { "42".toInt() }
val bad = runCatching { "abc".toInt() }

println(ok.isSuccess)   // true
println(bad.isFailure)  // true
```
값은 그 후에 읽어내며, 실패가 무엇이 될지는 여러분이 선택합니다:
```kotlin
println(ok.getOrNull())      // 42
println(bad.getOrNull())     // null
println(bad.getOrElse { 0 }) // 0
```
`getOrNull()`은 실패를 `null`로 바꾸고, `getOrElse { ... }`는 블록을 실행하여 대체 값을 만듭니다. 호출 지점에서는 아무것도 던져지지 않으므로, 실패를 가지고 돌아다니다가 나중에 처리할 수 있습니다.

---

`Result`는 평범한 값이므로 `val`에 저장해 두고 원하는 만큼 여러 번 확인할 수 있습니다:

```kotlin
val result = runCatching { "abc".toInt() }

println(result.getOrElse { 0 })  // 0
println(result.getOrNull())      // null
println(result.isSuccess)        // false
```
`try`/`catch`는 이렇게 할 수 없습니다. 그곳에서는 결과가 실패가 일어난 바로 그 지점에서 한 번만 처리되고, 그 후에는 사라져 버립니다. `Result`는 실패를 계속 간직하기 때문에, 그것에 반응하는 코드가 실패가 일어난 곳에 있을 필요가 없습니다.

---

`Result`는 풀어내지 않고도 검사할 수 있습니다. `onFailure`는 결과가 예외를 담고 있을 때만 그 블록을 실행하고, `onSuccess`는 값을 담고 있을 때만 실행하며, **둘 다 같은 `Result`를 돌려주므로** 호출을 연쇄할 수 있습니다:

```kotlin
runCatching { "abc".toInt() }
    .onFailure { println("could not read it") }
    .onSuccess { println("read $it") }
```
블록 안에서는 예외(또는 값)를 `it`으로 사용할 수 있으므로, `it.message`가 실패의 텍스트입니다.

이것이 "기록하고 계속 진행"하는 형태입니다: 문제가 발생한 곳에서 보고한 뒤 계속 진행하며, 이른 `return`도 두 곳에서 설정되는 `var`도 없습니다.

---

`try`가 어디에 놓이는지에 따라 하나의 나쁜 값이 얼마나 많은 작업을 파괴하는지 결정됩니다. **루프 전체**를 감싸면 첫 번째 실패가 나머지 일괄 작업을 포기하고, **본문**을 감싸면 그 한 요소만 잃습니다:

```kotlin
var total = 0
for (value in listOf("3", "x", "5")) {
    try {
        total += value.toInt()
    } catch (e: NumberFormatException) {
        // 이 값은 건너뜁니다
    }
}
println(total) // 8
```
이것은 던지는 검증 함수와 자연스럽게 짝을 이룹니다: 함수는 하나의 규칙을 명시하고 그 규칙을 깨는 것은 무엇이든 거절하며, 루프는 거절이 한 요소의 비용만 치른다고 결정합니다.
