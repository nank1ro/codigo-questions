`data class`는 **데이터를 보관**하는 것이 임무인 클래스입니다. 주 생성자에서 선언한 프로퍼티로부터 컴파일러가 네 가지 멤버를 자동으로 생성해 줍니다:

- `toString()`, 읽기 쉬운 `ClassName(prop=value, ...)` 형태의 텍스트
- `equals()`와 `hashCode()`, 같은 데이터를 가진 두 인스턴스가 동등하게 취급되도록 합니다
- `copy()`, 현재 값을 재사용하여 새 인스턴스를 만듭니다

```kotlin
data class Book(val title: String, val pages: Int)

val book = Book("Dune", 412)
println(book)          // Book(title=Dune, pages=412)
println(book.copy())   // Book(title=Dune, pages=412)
```

`copy()`는 **이름 있는 인자(named arguments)**와 함께 사용할 때 진가를 발휘합니다: 변경하려는 프로퍼티만 이름으로 지정하면 나머지 값은 모두 그대로 유지됩니다.

```kotlin
println(book.copy(pages = 500)) // Book(title=Dune, pages=500)
```

원본은 절대 수정되지 않습니다: `copy()`는 완전히 새로운 객체를 반환합니다.

---

주 생성자의 각 프로퍼티에 대해 데이터 클래스는 `componentN()` 함수도 생성합니다: 첫 번째 프로퍼티에는 `component1()`, 두 번째에는 `component2()` 등입니다.

이 함수들은 **구조 분해 선언(destructuring declarations)**을 가능하게 합니다. 객체를 한 줄에서 여러 변수로 풀어냅니다:

```kotlin
data class Point(val x: Int, val y: Int)

val point = Point(3, 7)
val (x, y) = point
println(x)               // 3
println(point.component2()) // 7
```

변수의 순서는 이름이 아닌 프로퍼티의 순서를 따릅니다. 필요 없는 프로퍼티는 `_`로 건너뛸 수 있습니다:

```kotlin
val (_, onlyY) = point
```

---

생성된 `equals()`는 `==`를 **구조적(structural)** 비교로 만듭니다: 주 생성자의 모든 프로퍼티가 같으면 두 인스턴스는 동등합니다. `===` 연산자는 다르며, 두 이름이 메모리의 **정확히 동일한 객체**를 가리키는지를 묻습니다.

```kotlin
data class User(val id: Int, val name: String)

val a = User(1, "Ann")
val b = User(1, "Ann")
println(a == b)  // true, 데이터가 같습니다
println(a === b) // false, 서로 다른 두 객체입니다
println(a === a) // true
```

`hashCode()`가 `equals()`와 함께 생성되기 때문에, 데이터 클래스 인스턴스는 `Set` 안에서나 `Map` 키로 사용될 때도 올바르게 동작합니다: 중복은 하나로 합쳐집니다.

```kotlin
println(setOf(a, b).size) // 1
```

일반 클래스는 이 중 아무것도 생성하지 않으므로, 일반 클래스에서 `==`는 동일성(identity) 비교로 대체됩니다.

---

생성된 멤버들은 **주 생성자**에 선언된 프로퍼티만 봅니다. 클래스 **본문**에 선언된 프로퍼티는 일반 프로퍼티입니다: `toString()`, `equals()`, `hashCode()`, `copy()`의 일부가 아닙니다.

```kotlin
data class Item(val name: String) {
    var quantity: Int = 0
}

val a = Item("nail")
a.quantity = 5
println(a) // Item(name=nail)
```

이것은 잊기 쉬우므로, 객체를 식별하는 모든 것은 주 생성자에 넣고, 파생되거나 임시적인 상태는 본문에 두세요.

---

`sealed` 클래스는 **닫힌(closed)** 선택 집합을 기술합니다: 같은 패키지와 모듈에 작성된 하위 클래스만 허용되므로, 컴파일러는 그 모든 것을 알 수 있습니다.

```kotlin
sealed class Shape
data class Circle(val radius: Int) : Shape()
data class Square(val side: Int) : Shape()
```

그 대가는 **모든 경우를 다루는(exhaustive) `when`**입니다: sealed 타입에 대해 분기하고 모든 하위 클래스를 다루면 `else` 분기를 생략할 수 있습니다. 나중에 새 하위 클래스를 추가하면, 컴파일러가 조용히 `else`를 택하는 대신 업데이트를 잊은 모든 `when`을 알려줍니다.

```kotlin
fun name(shape: Shape): String = when (shape) {
    is Circle -> "circle"
    is Square -> "square"
}
```

`is Circle` 이후에는 값이 스마트 캐스트되므로, 그 분기 안에서는 수동 캐스트 없이도 `shape.radius`를 사용할 수 있습니다.

---

때로는 로거, 레지스트리, 애플리케이션 설정처럼 어떤 것의 **정확히 하나의** 인스턴스가 필요합니다. `class`를 `object`로 바꾸면 해당 싱글턴을 선언해 줍니다:

```kotlin
object Registry {
    var size = 0
    fun add() {
        size++
    }
}

Registry.add()
println(Registry.size) // 1
```

인스턴스는 처음 접근할 때 생성되며, 이름 자체를 사용합니다. `Registry()` 호출도 없고 생성자도 없습니다. `object`는 프로퍼티, 메서드, `init` 블록을 가질 수 있고, 인터페이스를 구현하거나 클래스를 확장할 수도 있습니다.

---

`companion object`는 클래스에 속한 싱글턴입니다. 상수 외에도 그 자연스러운 역할은 **팩토리 함수**를 담는 것입니다: 인스턴스를 만들기 전에 입력을 검사하거나 변환하고, 입력이 말이 되지 않으면 `null`을 반환할 수 있는 함수들입니다.

생성자를 `private`로 표시하면 모든 호출자가 팩토리를 통해서만 접근하게 됩니다:

```kotlin
class Age private constructor(val years: Int) {
    companion object {
        fun of(years: Int): Age? = if (years >= 0) Age(years) else null
    }
}

println(Age.of(30)?.years) // 30
println(Age.of(-1))        // null
```

컴패니언은 클래스 이름으로 호출합니다, `Age.of(...)`. 그리고 클래스 내부에 존재하기 때문에 private 생성자에 접근할 수 있습니다.

---

`interface`는 타입이 무엇을 할 수 있는지 나열합니다. 그 멤버들은 기본적으로 추상이지만, 인터페이스는 **기본 구현(default implementation)**, 즉 구현하는 모든 클래스가 공짜로 상속하고 재정의할 수 있는 본문을 제공할 수도 있습니다:

```kotlin
interface Greeter {
    val name: String              // abstract, 클래스가 반드시 제공해야 함
    fun greet(): String = "Hi, $name"  // 기본 구현
}

class Person(override val name: String) : Greeter

class Robot(override val name: String) : Greeter {
    override fun greet(): String = "BEEP $name"
}

println(Person("Ann").greet()) // Hi, Ann
println(Robot("R2").greet())   // BEEP R2
```

인터페이스는 상태를 저장할 수 없으므로(백킹 필드가 없음), 추상 프로퍼티는 보통 생성자에서 `override val`로 클래스가 구현해야 합니다. 클래스와 달리, 타입은 원하는 만큼 많은 인터페이스를 구현할 수 있습니다.

---

`abstract` 클래스는 인터페이스와 일반 클래스 사이에 위치합니다: 인스턴스화할 수 없으며, 본문이 없고 반드시 재정의해야 하는 **추상** 멤버와, 하위 클래스가 그대로 상속하는 구체적인 멤버를 섞어 가질 수 있습니다.

```kotlin
abstract class Vehicle(val name: String) {
    abstract fun wheels(): Int
    fun describe(): String = "$name has ${wheels()} wheels"
}

class Bike(name: String) : Vehicle(name) {
    override fun wheels(): Int = 2
}

println(Bike("BMX").describe()) // BMX has 2 wheels
```

인터페이스와 달리 추상 클래스는 생성자를 가지고 프로퍼티에 상태를 저장할 수 있으므로, 하위 클래스가 `: Vehicle(name)`으로 `name`을 전달하는 것입니다. 클래스는 하나의 클래스만 확장할 수 있으므로, 하위 클래스들이 데이터를 공유할 때는 추상 클래스를, 동작만 공유할 때는 인터페이스를 사용하세요. 추상 멤버는 `open`을 추가하지 않아도 재정의할 수 있습니다.

---

다른 클래스 안에 선언된 클래스는 기본적으로 **중첩(nested)**됩니다. 내부 클래스는 외부 인스턴스에 대해 아무것도 모르며, 외부 클래스 이름으로 생성합니다:

```kotlin
class Outer {
    class Nested {
        fun hello() = "hi"
    }
}

println(Outer.Nested().hello()) // hi
```

`inner` 키워드를 추가하면 상황이 달라집니다: `inner` 클래스는 외부 인스턴스에 대한 참조를 가지므로 외부 프로퍼티를 읽을 수 있고, **인스턴스로부터** 생성합니다:

```kotlin
class Counter(val step: Int) {
    inner class Doubler {
        fun value() = step * 2
    }
}

println(Counter(5).Doubler().value()) // 10
```

`inner` 클래스 안에서 `this`는 내부 객체입니다. 외부 객체가 명시적으로 필요하면 `this@Counter`를 사용하세요.

---

이 주제의 구성 요소들은 보통 결합되어 사용됩니다: 각 항목이 자신만의 프로퍼티를 가지는 `enum class`는 고정된 태그 집합을 모델링하고, `data class`는 그와 함께 가는 페이로드를 담습니다.

```kotlin
enum class Speed(val surcharge: Int) {
    STANDARD(0),
    EXPRESS(15)
}

data class Order(val total: Int, val speed: Speed)

val order = Order(100, Speed.EXPRESS)
println(order.total + order.speed.surcharge) // 115
```
