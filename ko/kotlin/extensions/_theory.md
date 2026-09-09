**확장 함수**는 기존 타입의 소스 코드를 건드리지 않고 새로운 함수를 추가합니다.
`fun`을 쓰고, 확장하려는 타입(**리시버 타입**), 점, 함수 이름 순서로 작성합니다.
```kotlin
fun Int.squared(): Int {
    return this * this
}
println(4.squared()) // 16
```
함수 안에서 `this`는 함수가 호출된 값이며, **리시버**라고 부릅니다. `4.squared()`에서는 `4`입니다.
확장이 정의되면 처음부터 `Int`의 일부였던 함수처럼 점으로 호출할 수 있습니다.

---

확장은 어떤 타입에서도 동작하며, 소스 코드가 없는 타입도 마찬가지입니다. `String`은 표준 라이브러리에서 오지만 여전히 새 함수를 추가할 수 있습니다.
```kotlin
fun String.whisper(): String {
    return this.lowercase() + "..."
}
println("HELLO".whisper()) // hello...
```
확장 안에서 리시버의 다른 멤버를 사용할 때는 `this.`를 생략할 수 있습니다. `lowercase()`만 쓰면 `this.lowercase()`를 뜻하고, `length`만 쓰면 `this.length`를 뜻합니다.

---

확장 함수도 다른 함수처럼 매개변수를 받을 수 있습니다. 리시버는 점의 왼쪽에 그대로 있고, 매개변수는 괄호 안에 들어갑니다.
```kotlin
fun Int.isDivisibleBy(other: Int): Boolean {
    return this % other == 0
}
println(12.isDivisibleBy(4)) // true
println(12.isDivisibleBy(5)) // false
```
점 앞의 타입은 평범한 타입이므로, 같은 방식으로 `List<Int>`, `Double`, 또는 직접 작성한 클래스도 확장할 수 있습니다.

---

확장은 확장 대상 클래스를 수정하지 **않으며**, 새 멤버를 집어넣지도 않습니다. 컴파일러는 단지 호출을 다시 쓸 뿐입니다. `"kotlin".first3()`는 `"kotlin"`을 `this`로 넘기는 함수 호출이 됩니다.
```kotlin
fun String.first3(): String = take(3)
val word = "kotlin"
println(word.first3()) // kot
```
그래서 `String`이나 `Int` 같은 final 클래스도 확장할 수 있습니다. 그 안의 것은 아무것도 바뀌지 않고, 확장은 여러분의 코드 안에만 존재합니다.

---

함수 외에 **확장 프로퍼티**도 추가할 수 있습니다. `val`, 리시버 타입, 점, 이름 순으로 선언하고, 이어서 프로퍼티를 읽을 때마다 값을 계산하는 `get()`을 씁니다.
```kotlin
val String.wordCount: Int
    get() = split(" ").size

println("Kotlin is fun".wordCount) // 3
```
확장 프로퍼티는 아무것도 저장할 수 없습니다. 백킹 필드가 없기 때문에 `val String.label = "text"` 같은 초기화는 컴파일 오류입니다. 리시버로부터 값을 계산하는 것만 가능합니다.
확장 함수와 달리 확장 프로퍼티는 함수 안에서 선언할 수 없습니다(지역 확장 프로퍼티는 허용되지 않습니다).

---

확장 프로퍼티는 `String`의 기본 제공 `length`와 똑같이 괄호 없이 읽습니다. 값이 리시버로 무언가를 하는 것이 아니라 리시버를 설명할 때 자연스러운 선택입니다.
```kotlin
val Int.isNegative: Boolean
    get() = this < 0

println((-3).isNegative) // true
println(7.isNegative)    // false
```
`-3`을 감싼 괄호에 주의하세요. 괄호가 없으면 `-3.isNegative`는 먼저 `3`의 프로퍼티를 읽고 그다음 `Boolean`에 음수 부호를 붙이려 하므로 컴파일되지 않습니다.

---

리시버 타입은 **널 허용**일 수 있습니다. `String?`에 대한 확장은 `null`을 담고 있을 수 있는 변수에서도 호출할 수 있고, 함수 안의 `this`는 `String?`이므로 `null` 경우는 직접 처리합니다. 보통 널 가능성 수업에서 만난 엘비스 연산자 `?:`를 사용합니다.
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val name: String? = null
println(name.orDash())  // -
println("Ada".orDash()) // Ada
```
`null` 값에서 `name.orDash()`를 호출하는 것은 안전합니다. 함수 자체가 `null` 리시버를 받아들이므로 `?.`가 필요 없습니다.

---

리시버가 널 허용인 확장 안에서는 안전 호출 `this?.`를 사용해 값이 `null`이 아닐 때만 그 멤버에 접근할 수도 있습니다. 표준 라이브러리도 `isNullOrEmpty()` 같은 함수에서 같은 아이디어를 사용합니다.
```kotlin
fun String?.firstOrQuestion(): Char {
    return this?.firstOrNull() ?: '?'
}
val text: String? = null
println(text.firstOrQuestion())    // ?
println("Kotlin".firstOrQuestion()) // K
```

---

클래스에 확장과 이름과 매개변수가 같은 멤버가 이미 있으면 **항상 멤버가 이깁니다**. 확장은 결코 호출되지 않으며, 컴파일러는 가려졌다고 경고합니다.
```kotlin
class Box {
    fun describe(): String = "member"
}
fun Box.describe(): String = "extension"

println(Box().describe()) // member
```
확장은 기존 동작을 오버라이드하거나 대체할 수 없고, 새로운 함수와 프로퍼티를 추가할 수만 있습니다. 선택되려면 확장은 클래스가 아직 갖고 있지 않은 이름이나 매개변수 목록이 필요합니다.

---

**타입 매개변수** 덕분에 확장은 한 번에 여러 타입의 계열에서 동작할 수 있습니다. 타입 매개변수는 타입의 자리표시자로, `fun` 바로 뒤 꺾쇠괄호 안에 선언하며 Kotlin이 호출할 때마다 채워 넣습니다. 이것이 확장을 **제네릭**하게 만듭니다.
```kotlin
fun <T> List<T>.second(): T {
    return this[1]
}
println(listOf(1, 2, 3).second())      // 2
println(listOf("a", "b").second())     // b
```
`listOf(1, 2, 3)`에서는 자리표시자 `T`가 `Int`이고 `listOf("a", "b")`에서는 `String`이므로, 같은 함수가 매번 올바른 타입을 반환합니다.

---

타입 매개변수는 시그니처의 어디에서든 쓸 수 있습니다. 반환 타입으로, 널 허용 `T?`로, 또는 다른 타입 안에서도 쓸 수 있습니다. 아무것도 찾지 못할 수 있는 제네릭 확장은 기본 제공 `firstOrNull()`처럼 `T?`를 반환합니다.
```kotlin
fun <T> List<T>.lastOrDefault(default: T): T {
    return if (isEmpty()) default else this[size - 1]
}
println(listOf(1, 2).lastOrDefault(0))          // 2
println(emptyList<String>().lastOrDefault("-")) // -
```
리시버가 `List<T>`이므로 함수 안에서 `size`, `isEmpty()`, 인덱싱을 어떤 리스트에서와 똑같이 사용할 수 있습니다.

---

클래스가 **컴패니언 객체**를 선언하고 있다면, 비어 있더라도 그것을 확장할 수 있습니다. 리시버 타입은 `ClassName.Companion`으로 쓰고, 확장은 팩토리 함수처럼 클래스 이름에서 호출합니다.
```kotlin
class Temperature(val degrees: Int) {
    companion object
}
fun Temperature.Companion.freezing(): Temperature = Temperature(0)

println(Temperature.freezing().degrees) // 0
```
클래스와 확장은 모두 최상위 선언이므로 `main` 바깥에 작성해야 합니다.

---

컴패니언 확장은 매개변수를 받을 수 있어서, 다른 단위나 형식에서 변환하는 대체 생성자를 두기에 편리한 자리입니다.
```kotlin
class Distance(val meters: Int) {
    companion object
}
fun Distance.Companion.fromKilometers(km: Int): Distance = Distance(km * 1000)

println(Distance.fromKilometers(3).meters) // 3000
```

---

확장을 어디에 선언하는지가 어디에서 쓸 수 있는지, 즉 그 **스코프**를 결정합니다.
- 파일의 최상위에 선언하면 파일 전체와 패키지의 나머지 부분에서 사용할 수 있습니다
- 함수 안에 선언하면 지역 확장이 되어 그 함수 안에서만 사용할 수 있습니다
- 클래스 안에 선언하면 **멤버 확장**이 되어 그 클래스 안에서만 사용할 수 있습니다

멤버 확장은 자신이 속한 클래스의 프로퍼티를 읽을 수 있으므로 두 리시버를 결합합니다. 클래스 인스턴스와 호출 대상 값입니다.
```kotlin
class Greeter(val greeting: String) {
    fun String.greet(): String = "$greeting, $this!"
    fun welcome(name: String): String = name.greet()
}
println(Greeter("Hello").welcome("Ada")) // Hello, Ada!
```
`greet` 안에서 `greeting`은 `Greeter`에서 오고, `this`는 함수가 호출된 `String`입니다. 클래스 바깥에서 `"Ada".greet()`는 컴파일 오류입니다.

---

매개변수가 정확히 **하나**인 확장 함수는 `infix`로 표시할 수 있습니다. 중위 함수는 점과 괄호 없이 리시버를 왼쪽에, 인자를 오른쪽에 두고 호출할 수 있어 거의 문장처럼 읽힙니다.
```kotlin
infix fun Int.percentOf(total: Int): Int = total * this / 100

println(20 percentOf 50)   // 10
println(20.percentOf(50))  // 10, the normal call still works
```
Kotlin은 일부 기본 제공 함수에서도 이것을 사용합니다. `1 to "one"`은 `Pair`를 만들고, `1 until 5`는 범위를 만듭니다.

---

`infix`로 표시하려면 함수가 멤버이거나 확장이어야 하고, 매개변수를 정확히 하나만 받아야 하며, 그 매개변수에 기본값이 없어야 합니다. 그 외의 경우는 모두 컴파일 오류입니다.
```kotlin
infix fun Int.add(other: Int): Int = this + other          // ok
infix fun add(a: Int, b: Int): Int = a + b                 // error: not a member or extension
infix fun Int.add(a: Int, b: Int): Int = this + a + b      // error: two parameters
```
중위 호출의 우선순위는 산술 연산과 비교 연산 사이에 있습니다. `1 add 2 * 3`은 `1 add 6`이고, `1 add 2 == 3`은 결과를 `3`과 비교합니다.
