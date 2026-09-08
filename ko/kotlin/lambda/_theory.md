**람다**는 이름이 없는 작은 함수로, 중괄호 사이의 식으로 바로 작성합니다.
매개변수가 먼저 오고, 그다음 화살표 `->`, 그다음 본문이 옵니다:
```kotlin
val add = { a: Int, b: Int -> a + b }
```
람다는 다른 값과 마찬가지로 하나의 값입니다: 변수에 저장했다가 나중에 함수와 똑같이 괄호로 호출할 수 있습니다:
```kotlin
println(add(2, 3)) // 5
```
매개변수가 없는 람다에는 화살표가 아예 없습니다: `val hello = { println("Hello!") }`.

---

모든 람다에는 **함수 타입**이 있습니다. 이는 매개변수 타입을 괄호로 감싸고, 화살표, 반환 타입을 이어서 쓴 것입니다.
람다 `{ a: Int, b: Int -> a + b }`의 타입은 `(Int, Int) -> Int`입니다: 두 개의 `Int` 값을 받아 `Int`를 반환합니다.
변수에 함수 타입을 선언하면 컴파일러가 이미 알고 있기 때문에 람다 안의 매개변수 타입은 생략할 수 있습니다:
```kotlin
val add: (Int, Int) -> Int = { a, b -> a + b }
val greet: (String) -> Unit = { name -> println("Hi, $name") }
```
아무것도 반환하지 않는 람다의 반환 타입은 `Unit`입니다.

---

람다의 본문은 여러 줄에 걸칠 수 있습니다. `return` 키워드는 없습니다: **마지막 식**의 값이 람다가 반환하는 값입니다.
```kotlin
val describe: (Int) -> String = { n ->
    val half = n / 2
    "half of $n is $half" // returned
}
println(describe(10)) // half of 10 is 5
```
Kotlin에서 `if`는 식이므로 마지막 줄에 두어 결과를 결정할 수 있습니다:
```kotlin
val parity: (Int) -> String = { n -> if (n % 2 == 0) "even" else "odd" }
```

---

람다에 정확히 **하나의** 매개변수만 있다면 매개변수 선언을 생략할 수 있습니다: Kotlin이 자동으로 `it`이라는 이름을 붙여 줍니다.
```kotlin
// val double: (Int) -> Int = { n -> n * 2 }
val double: (Int) -> Int = { it * 2 } // same thing
```
`it`은 매개변수를 명시적으로 선언하지 않았을 때만 존재하며, 매개변수가 하나인 람다에서만 사용할 수 있습니다.
짧은 람다를 간결하게 유지해 주지만, 본문이 길어지면 실제 이름을 쓰는 것이 더 명확합니다.

---

람다는 주로 다른 함수의 인수로 사용됩니다. 컬렉션은 람다를 받는 많은 함수를 제공합니다:
- `forEach`는 모든 요소마다 람다를 한 번씩 실행합니다
- `map`은 모든 요소에 대한 람다의 결과로 새 리스트를 만듭니다
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map({ it * 2 }) // [2, 4, 6]
```
람다가 **마지막** 인수일 때는 괄호 밖으로 꺼낼 수 있고, 유일한 인수일 때는 괄호를 아예 생략할 수 있습니다. 이것을 **trailing 람다** 문법이라고 하며, 보통 이렇게 작성합니다:
```kotlin
val doubled = numbers.map { it * 2 }
doubled.forEach { println(it) }
```

---

`Boolean`을 반환하는 람다를 **술어**라고 합니다. 여러 컬렉션 함수가 술어를 받습니다:
- `filter`는 술어가 `true`인 요소만 남깁니다
- `count`는 술어를 만족하는 요소가 몇 개인지 반환합니다
- `any`와 `all`은 일부 또는 모든 요소가 술어를 만족하는지 알려 줍니다
```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6)
println(numbers.filter { it % 2 == 0 }) // [2, 4, 6]
println(numbers.count { it > 4 })        // 2
println(numbers.any { it > 5 })          // true
```
호출은 **연쇄**할 수 있습니다: 각 함수는 새 리스트를 반환하고 다음 함수가 그 리스트를 다룹니다.
```kotlin
println(numbers.filter { it % 2 == 0 }.map { it * 10 }) // [20, 40, 60]
```

---

람다는 정렬과 집계에도 사용됩니다:
- `sortedBy`는 각 요소에 대해 람다가 계산한 값을 기준으로 정렬된 새 리스트를 반환하며, `sortedByDescending`은 그 반대입니다
- `reduce`는 모든 요소를 하나의 값으로 합칩니다: 람다는 지금까지 누적된 결과와 다음 요소를 받습니다
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })          // [fig, kiwi, banana]
println(words.sortedByDescending { it.length }) // [banana, kiwi, fig]

val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n })   // 10
```
`reduce`는 첫 번째 요소를 `acc`로 시작하여, 남은 모든 요소에 대해 람다를 실행합니다.

---

`reduce`에서 결과의 형태는 람다가 결정합니다. 두 값을 하나로 합치는 연산이라면 무엇이든 가능합니다: 합, 곱, 둘 중 더 큰 값을 유지하는 것 등입니다.
```kotlin
val numbers = listOf(3, 9, 4)
println(numbers.reduce { acc, n -> if (n > acc) n else acc }) // 9
```
`reduce`는 빈 리스트에서 예외를 던진다는 점에 주의하세요. 시작할 첫 번째 요소가 없기 때문입니다.

---

람다는 주변에서 선언된 변수를 사용할 수 있으며, 주변 코드가 끝난 뒤에도 계속 사용할 수 있습니다. 이것을 **클로저**라고 합니다: 람다는 필요한 변수를 *캡처*합니다.
다른 많은 언어와 달리 Kotlin에서는 람다가 캡처한 `var`를 **수정**할 수 있습니다:
```kotlin
var clicks = 0
val onClick = { clicks++ }
onClick()
onClick()
println(clicks) // 2
```
`onClick`을 호출할 때마다 바깥 코드가 보는 같은 `clicks` 변수가 갱신됩니다.

---

람다는 값이므로 함수가 람다를 **반환**할 수도 있습니다. 반환 타입은 함수 타입입니다:
```kotlin
fun multiplier(factor: Int): (Int) -> Int {
    return { it * factor }
}
val triple = multiplier(3)
println(triple(5)) // 15
```
반환된 람다는 `factor`를 캡처하므로, `multiplier`를 호출할 때마다 서로 다른 함수가 만들어집니다.
다른 함수를 받거나 반환하는 함수를 **고차 함수**라고 합니다.

---

반환된 람다는 함수 안에서 선언된 `var`를 캡처할 수 있습니다. 그 변수는 함수가 반환된 뒤에도 살아 있으며, 오직 그 람다만 접근할 수 있습니다: 비공개 상태입니다.
```kotlin
fun makeGreeter(): () -> String {
    var calls = 0
    return { calls++; "hello #$calls" }
}
val greeter = makeGreeter()
println(greeter()) // hello #1
println(greeter()) // hello #2
```
`makeGreeter()`를 호출할 때마다 새로운 `calls`가 선언되므로, 두 greeter는 서로 독립적으로 셉니다.

---

고차 함수를 직접 작성할 수도 있습니다: 함수 타입을 가진 매개변수는 그 모양의 람다라면 무엇이든 받아들이며, 함수 안에서는 일반 함수처럼 호출합니다.
```kotlin
fun repeatTwice(text: String, transform: (String) -> String): String {
    return transform(transform(text))
}
println(repeatTwice("a", { it + "!" })) // a!!
println(repeatTwice("a") { it + "!" })  // same, with a trailing lambda
```
함수 매개변수를 **마지막**에 두어야 호출자가 trailing 람다 문법을 사용할 수 있습니다.

---

필요한 함수가 이미 존재한다면 람다로 감쌀 필요가 없습니다: **함수 참조** `::name`은 이름이 있는 함수를 일치하는 함수 타입의 값으로 바꿉니다.
```kotlin
fun isEven(n: Int) = n % 2 == 0
val numbers = listOf(1, 2, 3, 4)
println(numbers.filter { isEven(it) }) // [2, 4]
println(numbers.filter(::isEven))      // [2, 4], same thing
```
멤버 함수는 타입을 통해 참조합니다. 예를 들어 `String::uppercase`처럼 참조합니다:
```kotlin
println(listOf("a", "b").map(String::uppercase)) // [A, B]
```

---

**익명 함수**는 `fun`으로 선언하지만 이름이 없는 함수입니다. 함수 값을 만드는 또 다른 방법입니다:
```kotlin
val square = fun(x: Int): Int {
    return x * x
}
println(square(4)) // 16
```
람다와 달리 반환 타입을 명시적으로 선언할 수 있고, 값을 만들 때 `return`을 사용합니다.
익명 함수와 람다는 서로 바꿔 쓸 수 있습니다: 둘 다 `map`, `filter` 또는 함수 타입을 받는 어떤 함수에도 전달할 수 있습니다.

---

고차 함수는 함수를 받을 수도 있고 반환할 수도 있습니다. 고전적인 예가 **합성**입니다: 한 함수를 실행하고 그 결과를 다른 함수에 넘기는 새 함수를 만드는 것입니다.
```kotlin
fun andThen(first: (Int) -> Int, second: (Int) -> Int): (Int) -> Int {
    return { n -> second(first(n)) }
}
val addOneThenDouble = andThen({ it + 1 }, { it * 2 })
println(addOneThenDouble(3)) // 8
```
반환된 람다는 `first`와 `second`를 모두 캡처하므로, `andThen`이 반환된 지 오랜 뒤에도 계속 동작합니다.

---

일부 함수는 **수신 객체가 있는 람다**를 받습니다: 람다 안에서 `this`는 특정 객체이므로, 객체 이름을 붙이지 않고 바로 그 멤버를 호출할 수 있습니다.
`buildString`이 대표적인 예입니다: 그 람다 안에서 `this`는 `StringBuilder`이므로, `append`를 로컬 함수처럼 호출할 수 있습니다:
```kotlin
val text = buildString {
    append("Hello")
    append(", ")
    append("world")
}
println(text) // Hello, world
```
`buildString`은 최종 문자열을 반환합니다. 반복문에서 `+`로 이어 붙이는 것을 편리하게 대신하는 방법입니다.
