**열거형**(*enum*)은 관련된 값들의 그룹에 대한 공통 타입을 정의하여, 그 값들을 타입 안전하게 다룰 수 있게 합니다.
Kotlin에서는 `enum class` 키워드로 선언하고, **항목**을 쉼표로 구분하여 나열합니다:
```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
```
관례상 항목 이름은 대문자로 작성합니다. 각 항목은 enum 타입의 값이며, 클래스 이름을 통해 접근합니다:
```kotlin
val heading = Direction.NORTH
println(heading) // NORTH
```
enum 클래스는 파일의 최상위 레벨(또는 다른 클래스 내부)에 선언되어야 하며, 함수 내부에는 선언할 수 없습니다.

---

모든 enum 항목에는 두 가지 내장 프로퍼티가 있습니다:

- `name`은 해당 항목의 이름을 나타내는 `String`입니다
- `ordinal`은 선언 순서에서의 위치이며, `0`부터 시작합니다

```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
println(Direction.EAST.name)    // EAST
println(Direction.EAST.ordinal) // 2
```

---

enum 항목은 `==`로 비교합니다:
```kotlin
val heading = Direction.NORTH
println(heading == Direction.NORTH) // true
```

`when` 표현식은 enum을 분기하는 자연스러운 방법입니다. **모든** 항목을 다루면 *완전함*(exhaustive)으로 간주되어 `else` 분기가 필요 없습니다:
```kotlin
fun arrow(direction: Direction): String = when (direction) {
    Direction.NORTH -> "^"
    Direction.SOUTH -> "v"
    Direction.EAST -> ">"
    Direction.WEST -> "<"
}
```
항목을 하나라도 빠뜨리면, 버그가 런타임까지 남아있는 대신 컴파일러가 에러를 알려줍니다.

---

enum 클래스는 일반 클래스와 마찬가지로 **생성자**를 가질 수 있습니다. 각 항목은 자신만의 인자를 전달하고, 그 값들은 프로퍼티에 저장됩니다:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2)
}
println(Planet.MARS.moons) // 2
```
항목의 데이터는 보통 바뀌지 않기 때문에, 생성자 프로퍼티는 대개 `val`로 선언합니다.

---

enum 클래스는 **메서드**도 선언할 수 있습니다. 멤버 선언 전에 항목 목록을 세미콜론 `;`으로 닫아야 합니다:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2);

    fun hasMoons(): Boolean {
        return moons > 0
    }
}
println(Planet.EARTH.hasMoons()) // true
```
메서드 내부에서는 해당 항목의 프로퍼티는 물론 `name`과 `ordinal`에도 접근할 수 있습니다.

---

모든 enum 클래스는 `entries` 프로퍼티를 제공합니다. 이는 선언 순서대로 정렬된 모든 항목의 리스트입니다. 반복 작업에 유용합니다:
```kotlin
for (direction in Direction.entries) {
    println(direction.name)
}
// NORTH
// SOUTH
// EAST
// WEST
```
리스트이기 때문에 `entries`는 `size`와 인덱싱도 지원합니다. 예를 들어 `Direction.entries[0]`은 `NORTH`입니다.

예전 코드에서는 대신 배열을 반환하는 `values()` 함수를 사용합니다. Kotlin 1.9부터는 `entries`가 권장되는 방식입니다.

---

`String`에서 다시 항목으로 되돌리려면 `valueOf` 함수를 사용합니다. 이 함수는 `name`이 정확히 일치하는 항목을 찾습니다:
```kotlin
val direction = Direction.valueOf("EAST")
println(direction == Direction.EAST) // true
```
이 비교는 대소문자를 구분합니다. `Direction.valueOf("east")`는 그런 이름을 가진 항목이 없기 때문에 `IllegalArgumentException`을 던집니다.

---

enum 클래스는 **추상 메서드**를 선언하여, 각 항목이 중괄호로 감싼 본문에서 자신만의 구현을 제공하도록 할 수 있습니다:
```kotlin
enum class Operation {
    ADD {
        override fun apply(a: Int, b: Int): Int = a + b
    },
    SUBTRACT {
        override fun apply(a: Int, b: Int): Int = a - b
    };

    abstract fun apply(a: Int, b: Int): Int
}
println(Operation.ADD.apply(2, 3)) // 5
```
각 항목은 동일한 타입과 메서드 시그니처를 공유하면서도 서로 다르게 동작합니다.

---

**인터페이스**는 본문 없이 메서드를 선언합니다. 이를 구현하는 모든 타입은 그 메서드들을 반드시 제공해야 합니다:
```kotlin
interface Greeter {
    fun greet(): String
}
```
enum 클래스는 인터페이스를 구현할 수 있습니다. 콜론 뒤에 인터페이스를 나열하고, 각 구현에 `override`를 표시합니다. enum 본문 안에서는 현재 항목이 `this`이며, 다른 항목은 클래스 이름 없이 참조할 수 있습니다:
```kotlin
enum class Language : Greeter {
    ENGLISH, ITALIAN;

    override fun greet(): String = when (this) {
        ENGLISH -> "Hello"
        ITALIAN -> "Ciao"
    }
}
println(Language.ITALIAN.greet()) // Ciao
```
