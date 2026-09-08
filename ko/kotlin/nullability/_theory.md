때로는 값이 아예 없는 경우가 있습니다: 중간 이름이 없는 사용자, 아무것도 찾지 못한 검색, 숫자로 변환할 수 없는 텍스트가 그 예입니다.
Kotlin은 없는 값을 `null`로 나타내지만, 일반 변수에는 절대 담을 수 없습니다. 모든 타입은 기본적으로 **널이 아닌(non-null)** 타입입니다:
```kotlin
var city: String = null // error: Null can not be a value of a non-null type String
```
없는 값을 허용하려면 타입 뒤에 물음표 `?`를 붙여 **널 가능(nullable)** 타입으로 선언합니다.
`String?`은 `String` 또는 `null`을 담습니다:
```kotlin
var city: String? = "Rome"
city = null // allowed
println(city) // null
```
`String`과 `String?`은 서로 다른 두 타입입니다: `String`은 없을 수 없고, `String?`은 없을 수 있습니다.

---

`String`과 `String?`의 차이는 런타임이 아니라 **컴파일러**가 검사합니다.
널이 아닌 타입에 `null`을 대입하거나, 널이 아닌 값이 필요한 곳에 널 가능 값을 전달하는 것은 컴파일 오류이므로 프로그램은 아예 시작되지도 않습니다:
```kotlin
val name: String = null        // does not compile
val maybe: String? = "hi"
val sure: String = maybe       // does not compile: String? is not a String
```
이것이 Kotlin이 다른 언어에서 흔한 "널 포인터" 크래시를 피하는 방법입니다: 값은 `?`로 명시적으로 선언한 곳에서만 없을 수 있습니다.

---

`?`는 타입이 쓰이는 어디에서든 동작합니다: 함수는 널 가능 매개변수를 받고 널 가능 값을 반환할 수 있습니다.
```kotlin
fun firstChar(text: String?): Char? {
    ...
}
```
`null`일 수 있기 때문에 널 가능 값에 대해 메서드를 직접 호출할 수 없습니다.
**안전 호출(safe call)** 연산자 `?.`는 값이 `null`이 아닐 때만 메서드를 호출하고, 그렇지 않으면 전체 표현식은 `null`이 됩니다:
```kotlin
val word: String? = "kotlin"
println(word?.length)   // 6
val none: String? = null
println(none?.length)   // null
```
안전 호출의 결과는 항상 널 가능입니다: `word?.length`는 `Int`가 아니라 `Int?`입니다.

---

널 가능 값에서 원하는 것은 대부분 값 그 자체이거나 기본값입니다.
**엘비스(Elvis) 연산자** `?:`가 바로 그 일을 합니다: `null`이 아닐 때는 왼쪽을 반환하고, 그렇지 않으면 오른쪽의 값을 반환합니다:
```kotlin
val name: String? = null
val shown = name ?: "Guest" // shown is a String equal to "Guest"
```
왼쪽이 `null`일 때만 오른쪽이 사용되므로, 기본값이 널이 아닐 때 결과도 널이 아닙니다.
`?:`는 `?.`와 잘 어울려서 안전 호출을 다시 평범한 값으로 되돌려 줍니다:
```kotlin
val len = name?.length ?: 0 // len is an Int, 0 when name is null
```

---

안전 호출은 **연쇄**할 수 있습니다: 연쇄의 한 고리가 `null`이 되는 순간 나머지는 건너뛰어지고 전체 표현식은 `null`이 됩니다.
```kotlin
val text: String? = "  hi  "
println(text?.trim()?.uppercase())   // HI
val none: String? = null
println(none?.trim()?.uppercase())   // null, trim() and uppercase() never run
```
`?:`로 끝나는 연쇄는 한 줄에서 널이 아닌 결과를 줍니다:
```kotlin
val cleaned = text?.trim()?.uppercase() ?: ""
```

---

안전 호출 연쇄는 어느 단계든 없을 수 있는 중첩된 객체에서 빛을 발합니다:
```kotlin
class Address(val city: String?)
class User(val address: Address?)

val user = User(Address("Rome"))
println(user.address?.city ?: "unknown") // Rome
val nobody = User(null)
println(nobody.address?.city ?: "unknown") // unknown
```
각 `?.`는 다음 단계를 보호하고, 마지막 `?:`는 기본값을 제공합니다.

---

**널 아님 단언(not-null assertion)** 연산자 `!!`는 널 가능 값을 널이 아닌 값으로 바꾸며, 컴파일러에게 "이것은 `null`이 아니라고 확신한다"고 말해 줍니다:
```kotlin
val word: String? = "kotlin"
println(word!!.length) // 6
```
잘못되어 값이 `null`이었다면 프로그램은 런타임에 `NullPointerException`과 함께 크래시됩니다. 이것이 바로 Kotlin이 설계상 막으려 한 바로 그 오류입니다:
```kotlin
val none: String? = null
println(none!!.length) // NullPointerException
```
`!!`는 값이 정말로 `null`일 수 없을 때만 사용하고, 그 외의 모든 곳에서는 `?.`, `?:`와 널 검사를 선호하세요.

---

`if`로 값이 `null`인지 검사하면 컴파일러가 그 사실을 기억합니다: 값이 널이 아닌 것으로 알려진 분기 안에서는 널이 아닌 타입으로 **스마트 캐스트**되므로, `?.`나 `!!` 없이도 직접 사용할 수 있습니다:
```kotlin
fun greet(name: String?): String {
    if (name != null) {
        return "Hello, " + name.uppercase() // name is a String here
    }
    return "Hello, stranger"
}
```
조기 반환 후에도 같은 일이 일어납니다:
```kotlin
fun greet(name: String?): String {
    if (name == null) return "Hello, stranger"
    return "Hello, " + name.uppercase() // name is a String from here on
}
```
스마트 캐스트는 검사와 사용 사이에 값이 바뀔 수 없는 `val` 변수와 함수 매개변수에 동작합니다.

---

`let`은 호출된 값과 함께 코드 블록을 실행하며, 그 값은 블록 안에서 `it`으로 사용할 수 있습니다.
안전 호출과 결합하면 `?.let`은 값이 `null`이 **아닐 때만** 블록을 실행하고, 블록 안에서 `it`은 널이 아닙니다:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to $it") } // prints Sending to ada@example.com
val missing: String? = null
missing?.let { println("Sending to $it") } // nothing happens
```
블록 안에서만 값이 필요할 때 `if (x != null) { ... }`의 간결한 대안이 됩니다.

---

`let`은 블록 안 마지막 표현식의 값을 **반환**하기도 합니다. 따라서 `?.let`으로 널 가능 값을 변환하고, 값이 `null`일 때 `?:`로 기본값을 채울 수 있습니다:
```kotlin
fun priceLabel(price: Double?): String {
    return price?.let { "$it EUR" } ?: "free"
}
println(priceLabel(9.5))  // 9.5 EUR
println(priceLabel(null)) // free
```
`price`가 `null`이면 `let` 블록은 건너뛰어지고 표현식은 `null`이 되어, 엘비스 연산자가 `"free"`를 반환합니다.

---

컬렉션도 널 가능 요소를 담을 수 있습니다: `List<Int?>`는 `null` 항목을 포함할 수 있지만, `List<Int>`는 절대 그렇지 않습니다.
`filterNotNull()`은 `null` 항목이 제거된 새 리스트를 반환하고 요소 타입은 널이 아닌 타입이 되므로, 요소를 자유롭게 사용할 수 있습니다:
```kotlin
val scores: List<Int?> = listOf(10, null, 20)
val valid = scores.filterNotNull() // List<Int> [10, 20]
println(valid.sum())               // 30
```

---

많은 표준 함수는 실패하는 대신 `null`을 반환합니다. `toIntOrNull()`은 문자열을 `Int`로 변환하고, 텍스트가 정수가 아니면 `null`을 반환합니다:
```kotlin
println("42".toIntOrNull())  // 42
println("4x2".toIntOrNull()) // null
```
`mapNotNull`은 `map`처럼 모든 요소를 변환하지만, `null`인 결과는 버립니다:
```kotlin
val words = listOf("1", "two", "3")
println(words.mapNotNull { it.toIntOrNull() }) // [1, 3]
```

---

때로는 객체를 생성할 때 프로퍼티에 값을 줄 수 없지만, 사용되기 전에는 설정될 것을 알고 있는 경우가 있습니다.
널 가능으로 만드는 대신 `lateinit`을 붙이세요: 타입은 널이 아닌 상태로 유지되고, 읽을 때 `?.`가 필요 없습니다:
```kotlin
class Game {
    lateinit var player: String

    fun start(name: String) {
        player = name
    }
}
```
`lateinit`에는 몇 가지 규칙이 있습니다: `var` 프로퍼티에만 동작하고, 널이 아닌 타입에만 사용할 수 있으며, `Int`나 `Boolean` 같은 기본 타입에는 사용할 수 없습니다.
`lateinit` 프로퍼티를 대입하기 전에 읽으면 `UninitializedPropertyAccessException`이 발생합니다; `::player.isInitialized`로 먼저 확인할 수 있습니다.

---

`null`이 호출자의 실수를 의미한다면, `requireNotNull`로 조기에 실패하세요.
값이 있으면 널이 아닌 값으로 반환하고, `null`이면 선택적인 메시지와 함께 `IllegalArgumentException`을 던집니다:
```kotlin
fun greet(name: String?): String {
    val safeName = requireNotNull(name) { "name is required" }
    return "Hello, $safeName"
}
greet(null) // IllegalArgumentException: name is required
```
호출 후에는 컴파일러가 `name` 자체를 `String`으로 스마트 캐스트하므로, 그 줄부터는 `name.length`가 허용됩니다.
`!!`와 달리, 실패는 명확한 메시지를 담고 *인자*가 잘못되었다고 알려 줍니다.

---

확장 함수는 **널 가능 수신 객체**에 대해 선언할 수 있으므로, `null` 값에 대해서도 호출할 수 있습니다. 내부에서 `this`는 널 가능이므로 검사해야 합니다:
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val none: String? = null
println(none.orDash()) // -
```
호출 지점에서는 `?.`가 필요 없다는 점에 유의하세요: 함수 자체가 `null` 경우를 처리합니다.
표준 라이브러리는 이 트릭을 `isNullOrEmpty()`와 `orEmpty()`에 사용하며, 이들은 어떤 `String?`에도 안전하게 호출할 수 있습니다.

---

`?:`의 오른쪽에는 `return`을 포함한 어떤 표현식도 올 수 있습니다. 이 덕분에 값이 없는 순간 함수에서 곧바로 빠져나가는 간결한 방법을 만들 수 있습니다:
```kotlin
fun firstUpper(text: String?): Char? {
    val first = text?.firstOrNull() ?: return null
    return first.uppercaseChar() // first is a Char here
}
```
지금까지 본 모든 도구는 서로 잘 어울립니다: 널 가능 매개변수와 반환 타입은 값이 *어디에서* 없을 수 있는지 나타내고, `?.`, `?:`, `let`, 스마트 캐스트, `toIntOrNull`은 한 번도 크래시되지 않고 그것을 처리합니다.
