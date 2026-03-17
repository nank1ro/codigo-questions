**클래스**는 객체를 만들기 위한 설계도입니다. Kotlin에서는 `class` 키워드 뒤에 클래스 이름을 붙여 클래스를 선언합니다.

클래스는 **프로퍼티**(데이터)와 **메서드**(동작)를 가질 수 있습니다. 생성자에서 직접 프로퍼티를 선언하려면 `val` 또는 `var` 접두사를 사용합니다:

```kotlin
class Dog(val name: String)
```

이렇게 하면 `name` 프로퍼티를 가진 `Dog` 클래스가 만들어집니다. 클래스를 함수처럼 호출하여 인스턴스를 만듭니다:

```kotlin
val dog = Dog("Rex")
println(dog.name) // Rex
```

---

클래스는 **주 생성자**에 여러 프로퍼티를 가질 수 있습니다. 각 프로퍼티는 생성자 파라미터 목록에 `val`(읽기 전용) 또는 `var`(가변)로 직접 선언합니다:

```kotlin
class Person(val name: String, var age: Int)
```

`val` 키워드는 생성 후 `name`을 읽기 전용으로 만들고, `var`는 `age`를 가변으로 만듭니다 — 나중에 변경할 수 있습니다:

```kotlin
val p = Person("Alice", 30)
p.age = 31  // age가 var이므로 허용됨
```

---

**`init` 블록**은 주 생성자 직후에 실행됩니다. 객체 생성 시 유효성 검사나 설정 로직을 수행할 때 사용합니다:

```kotlin
class Circle(val radius: Double) {
    init {
        require(radius > 0) { "반지름은 양수여야 합니다" }
    }
}
```

`init` 안에서 추가 프로퍼티를 초기화할 수도 있습니다:

```kotlin
class Square(val side: Int) {
    val area: Int
    init {
        area = side * side
    }
}
```

---

클래스는 **메서드**를 포함할 수 있습니다 — 클래스에 속하며 프로퍼티를 조작하는 함수입니다:

```kotlin
class Counter(var count: Int) {
    fun increment() {
        count++
    }
    fun value(): Int {
        return count
    }
}
```

메서드는 인스턴스에 점 표기법을 사용하여 호출합니다:

```kotlin
val c = Counter(0)
c.increment()
println(c.value()) // 1
```

---

**`data class`**는 데이터를 저장하기 위해 설계된 특수 클래스입니다. Kotlin은 `equals()`, `hashCode()`, `toString()`, `copy()`를 자동으로 생성합니다:

```kotlin
data class Point(val x: Int, val y: Int)

val p = Point(1, 2)
println(p)           // Point(x=1, y=2)
println(p.toString()) // Point(x=1, y=2)
```

`copy()` 함수는 일부 프로퍼티를 변경한 새 인스턴스를 만듭니다:

```kotlin
val p2 = p.copy(y = 10)
println(p2) // Point(x=1, y=10)
```
