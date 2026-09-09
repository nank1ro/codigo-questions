Kotlin의 모든 값에는 **타입**이 있으며, 컴파일러에게 그것이 어떤 종류의 데이터인지, 무엇을 할 수 있는지 알려줍니다.
기본 타입은 다음과 같습니다:
- `Int`: `42`나 `-7` 같은 정수
- `Long`: `Int`보다 훨씬 큰 수를 담을 수 있는 정수
- `Double`: `3.14`처럼 소수 부분이 있는 수
- `Float`: `Double`의 절반 메모리를 사용하지만 정밀도가 떨어지는 소수
- `Char`: `'a'`처럼 작은따옴표로 감싼 하나의 문자
- `Boolean`: `true` 또는 `false`
- `String`: `"Hello"`처럼 큰따옴표로 감싼 텍스트

변수 단원에서 보았듯이, 이름 뒤에 콜론을 붙여 타입을 명시할 수 있습니다:
```kotlin
val age: Int = 36
val name: String = "Ada"
```
한 타입의 값은 다른 타입의 변수에 저장할 수 없습니다: `val age: Int = "36"`은 컴파일 오류입니다.

---

대부분의 경우 타입을 직접 쓰지 않습니다: Kotlin이 할당하는 값을 보고 몇 가지 리터럴 규칙에 따라 타입을 **추론**합니다:
- `42` 같은 정수는 `Int`입니다
- `3.14`처럼 소수점이 있는 수는 `Double`입니다
- 큰따옴표로 감싼 텍스트는 `String`입니다
- 작은따옴표로 감싼 문자는 `Char`입니다
- `true`와 `false`는 `Boolean`입니다
```kotlin
val count = 42     // Int
val price = 9.99   // Double
val name = "Ada"   // String
val grade = 'A'    // Char
val isOpen = true  // Boolean
```
Kotlin이 무엇을 추론했는지 확인하려면 `::class.simpleName`으로 값의 타입 이름을 출력할 수 있습니다:
```kotlin
println(count::class.simpleName) // Int
println(price::class.simpleName) // Double
```
소수 리터럴은 절대 `Float`로 추론되지 않습니다: `val ratio = 0.5`는 `Double`입니다.

---

`Int`는 약 20억까지의 정수를 담을 수 있으며, 더 정확히는 `2147483647`인 `Int.MAX_VALUE`까지 담을 수 있습니다.
`Int`에는 너무 큰 정수 리터럴은 자동으로 `Long`으로 추론되고, 접미사 `L`을 붙여 어떤 리터럴이든 `Long`으로 강제할 수 있습니다:
```kotlin
val big = 3000000000  // Long, too big for an Int
val small = 3L        // Long, thanks to the suffix
```
같은 방식으로 접미사 `f`는 소수 리터럴을 `Float`로 만듭니다: `val ratio = 0.5f`.
긴 숫자는 읽기 어렵기 때문에, Kotlin은 숫자 사이 어디든 밑줄 `_`을 넣을 수 있게 해주며, 컴파일러는 이를 무시합니다:
```kotlin
val population = 8_000_000_000L
val million = 1_000_000
println(million) // 1000000
```

---

Kotlin은 값을 할당할 때 숫자 타입 간에 절대 자동으로 변환하지 않으며, 작은 타입에서 큰 타입으로의 변환조차 예외입니다: `Int`를 `Long`이나 `Double` 변수에 저장하는 것은 컴파일 오류입니다.
```kotlin
val count = 3
val total: Long = count      // error: Int is not a Long
val price: Double = count    // error: Int is not a Double
```
모든 숫자 타입에는 필요한 타입의 새 값을 만드는 **변환 함수**가 있습니다: `toInt()`, `toLong()`, `toDouble()`, `toFloat()`, 그리고 텍스트를 얻기 위한 `toString()`입니다.
```kotlin
val total: Long = count.toLong()
val price: Double = count.toDouble() // 3.0
println(count.toString() + "!")      // 3!
```
소수를 정수로 바꿀 때는 **잘라냅니다**: `toInt()`는 단순히 소수 부분을 버리므로, `3.99.toInt()`는 `3`이고 `(-3.99).toInt()`는 `-3`입니다.

---

피연산자의 타입이 나눗셈의 동작 방식을 결정합니다. 둘 다 `Int`일 때 `/` 연산자는 **정수 나눗셈**을 수행합니다: 결과는 `Int`이고 나머지는 버려집니다.
피연산자 중 하나라도 `Double`이면 `/`는 부동소수점 나눗셈을 수행하고 소수 부분을 유지합니다:
```kotlin
println(7 / 2)              // 3
println(7.0 / 2)            // 3.5
val slices = 7
println(slices.toDouble() / 2) // 3.5
```
따라서 두 `Int` 변수로 소수 결과를 얻으려면 나누기 **전에** 최소 하나를 변환해야 합니다: `(7 / 2).toDouble()`은 `3.0`인데, 이는 정수 나눗셈이 이미 일어났기 때문입니다.

---

함수가 정수로 계산한 소수 결과를 반환해야 할 때는, 나누기 전에 피연산자를 `Double`로 변환하고 반환 타입을 `Double`로 선언합니다:
```kotlin
fun ratio(part: Int, total: Int): Double {
    return part.toDouble() / total
}
println(ratio(1, 4)) // 0.25
```
`List<Int>`의 `sum()`과 `size`도 `Int` 값이므로 같은 변환이 필요하다는 점을 기억하세요.

---

모든 `Char`는 숫자, 즉 자신의 **코드**로 저장됩니다. `code` 프로퍼티는 문자 뒤에 있는 `Int`를 알려주고, `toChar()`는 그 반대로 `Int`를 해당 코드의 `Char`로 바꿉니다:
```kotlin
println('A'.code)        // 65
println(66.toChar())     // B
println(('A'.code + 2).toChar()) // C
```
문자들의 코드는 연속적이므로, 코드에 더하면 알파벳을 따라 이동합니다.
`'7'`의 코드는 `7`이 아니라 `55`라는 점에 주의하세요: `Char`가 나타내는 숫자를 읽으려면 `7`을 반환하는 `digitToInt()`를 사용하세요.

---

`Char`의 코드는 `Int`이므로, 코드에 산술 연산을 하고 그 결과를 다시 `Char`로 변환할 수 있습니다. 알파벳을 따라 이동하는 방법은 다음과 같습니다:
```kotlin
val next = ('a'.code + 1).toChar() // 'b'
```
Kotlin에서는 `Int`를 `Char`에 직접 더할 수도 있습니다: `'a' + 1`은 `'b'`이고, 두 문자의 차이 `'d' - 'a'`는 `Int`인 `3`입니다.

---

사용자가 입력한 텍스트는 숫자처럼 보이더라도 항상 `String`으로 전달됩니다. 이것으로 계산을 하려면 **파싱**해야 합니다: `toInt()`는 `"42"`를 `Int`인 `42`로, `toDouble()`은 `"3.5"`를 `Double`인 `3.5`로 바꿉니다.
```kotlin
val typed = "42"
println(typed.toInt() + 1) // 43
```
모든 텍스트가 숫자는 아닙니다: `"4x2".toInt()`는 `NumberFormatException`을 던지고 프로그램을 멈춥니다.
안전한 대안인 `toIntOrNull()`과 `toDoubleOrNull()`은 예외를 던지는 대신 `null`을 반환하므로, 널 가능성 단원에서 배웠듯이 `?:`로 기본값을 제공할 수 있습니다:
```kotlin
println("4x2".toIntOrNull())      // null
println("4x2".toIntOrNull() ?: 0) // 0
```

---

`toIntOrNull()`은 선택적인 부호를 포함해 텍스트 전체가 유효한 정수일 때만 성공합니다:
```kotlin
println("42".toIntOrNull())   // 42
println("-7".toIntOrNull())   // -7
println("3.5".toIntOrNull())  // null, not a whole number
println(" 42".toIntOrNull())  // null, spaces are not allowed
println("abc".toIntOrNull())  // null
```
소수 텍스트에는 `toDoubleOrNull()`을 사용하세요. 이 함수는 같은 방식으로 `"3.5"`를 받아들여 `Double?`을 반환합니다.

---

`Int`는 크기가 고정되어 있으므로 가장 작은 값과 가장 큰 값이 있습니다: `Int.MIN_VALUE`는 `-2147483648`이고 `Int.MAX_VALUE`는 `2147483647`입니다.
한계를 넘어도 오류는 발생하지 **않습니다**: 값이 범위의 반대쪽 끝으로 조용히 **되돌아가는데**, 이 동작을 오버플로라고 합니다.
```kotlin
println(Int.MAX_VALUE)     // 2147483647
println(Int.MAX_VALUE + 1) // -2147483648
```
결과가 20억을 넘을 수 있다면 `Long`을 사용하세요. `Long`의 한계인 `Long.MAX_VALUE`는 약 922경입니다. 연산 전에 변환하는 것을 잊지 마세요: `Int.MAX_VALUE.toLong() + 1`은 `2147483648`입니다.

---

`Double`은 소수를 이진수로 저장하기 때문에, 일부 값은 정확하게 표현될 수 없고 마지막 자릿수에 작은 오차가 나타납니다:
```kotlin
println(0.1 + 0.2) // 0.30000000000000004
```
고정된 소수 자릿수를 표시하려면 형식 문자열과 함께 `String.format`을 사용하세요: `"%.2f"`는 "점 뒤에 숫자 2개를 가진 소수"를 의미합니다. 결과는 그 자릿수만큼 반올림된 `String`입니다:
```kotlin
println(String.format("%.2f", 0.1 + 0.2)) // 0.30
println(String.format("%.1f", 3.14159))   // 3.1
println(String.format("%.2f", 2.0))       // 2.00
```

---

`Any`는 계층의 꼭대기에 있는 타입입니다: 모든 Kotlin 값은 `Any`이므로, `Any` 타입의 변수는 `Int`, `String`, `Boolean` 등 무엇이든 담을 수 있습니다.
실제로 무엇이 담겨 있는지 알아보려면 `is` 연산자를 사용하세요. 이 연산자는 값이 그 타입일 때 `true`를 반환합니다:
```kotlin
val value: Any = 42
println(value is Int)    // true
println(value is String) // false
```
검사를 통과하면 컴파일러가 값을 **스마트 캐스트**합니다: `if` 안(또는 `when` 분기 안)에서는 변환 없이 그 타입으로 사용할 수 있습니다:
```kotlin
if (value is Int) println(value + 1) // 43, value is an Int here
when (value) {
    is String -> println(value.length)
    is Boolean -> println(!value)
}
```
