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
println(a == b)  // true, same data
println(a === b) // false, two different objects
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
