**스코프 함수**는 객체의 컨텍스트 *안에서* 코드 블록을 실행합니다. 언어에 새로운 기능을 추가하는 것이 아니라, 하나의 객체를 다루는 코드를 더 짧고 읽기 쉽게 만들어 줄 뿐입니다. Kotlin에는 `let`, `run`, `with`, `apply`, `also` 다섯 가지가 있습니다.

이 둘은 **두** 가지 점에서만 다릅니다: 블록 안에서 객체를 어떻게 참조하는지, 그리고 호출이 무엇을 돌려주는지입니다. `let`부터 시작해 보겠습니다: 블록 안에서 객체는 `it`이라고 불리고, 호출은 블록의 **마지막 표현식의 결과**를 반환합니다.
```kotlin
val word = "kotlin"
val letters = word.let { it.length } // 6
println(letters)
```
`let`이 없다면 임시 변수가 필요할 것입니다; `let`을 사용하면 블록이 지속되는 동안 객체를 짧은 이름 `it`으로 사용할 수 있습니다.

---

`let`은 마지막 표현식의 값을 반환하기 때문에, 중간 변수에 이름을 붙이지 않고도 **값을 다른 것으로 바꾸는** 편리한 방법입니다:
```kotlin
val price = 12
val label = price.let { "$it EUR" }
println(label) // 12 EUR
```
블록 안에서는 `it`을 필요한 만큼 몇 번이든 사용할 수 있습니다:
```kotlin
println("kiwi".let { "${it.uppercase()} has ${it.length} letters" })
// KIWI has 4 letters
```

---

`let`은 안전 호출 뒤에서 진가를 발휘합니다. `?.let { ... }`는 값이 `null`이 **아닐 때만** 블록을 실행하며, 블록 안에서 `it`은 널이 아닌 값이므로 추가 검사가 필요 없습니다:
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to ${it.uppercase()}") }
```
값이 `null`이면 전체 표현식은 `null`이 되고 블록은 절대 실행되지 않으므로, 대체 값을 제공할 때는 엘비스(Elvis) 연산자 `?:`가 자연스러운 짝입니다:
```kotlin
fun label(city: String?): String {
    return city?.let { "City: $it" } ?: "No city"
}
```

---

`let` 블록 안에서 객체를 꼭 `it`이라고 부를 필요는 없습니다: 람다 매개변수에 이름을 붙일 수 있는데, 블록이 중첩되거나 `it`으로는 아무 의미도 전달되지 않을 때 코드를 읽기 쉽게 유지해 줍니다.
```kotlin
val price: Int? = 12
println(price?.let { amount -> "$amount EUR" }) // 12 EUR
```
이런 식의 이름 붙이기는 `it`을 사용하는 모든 스코프 함수, 즉 `let`과 `also`에서도 동작합니다.

---

`apply`는 두 축을 한꺼번에 움직입니다: 블록 안에서 객체는 리시버 `this`이고(따라서 멤버를 **어떤 접두사 없이도** 사용할 수 있습니다), 호출은 블록의 결과가 아니라 **객체 자체**를 반환합니다.

이 조합 때문에 `apply`는 객체를 만들자마자 **설정**하는 도구로 쓰입니다:
```kotlin
class Server {
    var host = "localhost"
    var port = 80
}

val server = Server().apply {
    host = "example.com"
    port = 8080
}
println("${server.host}:${server.port}") // example.com:8080
```
블록 안의 `host`와 `port`는 `this.host`와 `this.port`입니다; `apply`가 설정이 끝난 `Server`를 그대로 돌려주기 때문에 곧바로 변수에 할당할 수 있습니다.

---

`apply`는 방금 만든 객체에만 국한되지 않습니다: 어떤 객체에든 동작하며, 객체를 그대로 돌려주기 때문에 객체가 필요한 어디에서든 전체 표현식을 사용할 수 있습니다.
```kotlin
val box = Box()
box.apply { label = "tools" }        // box를 변경하고 반환합니다
println(listOf(Box().apply { label = "nails" }).size) // 1
```
블록은 일반적인 코드 블록이므로 필요한 만큼 많은 문을 담을 수 있습니다.

---

`also`는 `apply`의 거울상입니다: 객체는 `it`으로 참조되고, 호출은 **객체 자체**를 반환합니다. 블록의 결과는 버려지므로, `also`는 로깅이나 검사 같은 **부수 효과**를 위한 것이며 체인이 만들어내는 결과를 바꾸지 않고 체인 중간에 끼워 넣을 수 있습니다:
```kotlin
val total = listOf(1, 2, 3)
    .also { println("size: ${it.size}") } // size: 3
    .sum()
println(total) // 6
```
*"그리고 그 값으로 이것도 하라"*고 읽으면 됩니다: 값은 그대로 다음 단계로 흘러갑니다.

---

블록이 객체를 다른 것의 **인자**로 필요로 할 때는 `apply`보다 `also`가 더 자연스럽게 읽힙니다: `it`은 곧바로 넘겨줄 수 있지만, `this`는 직접 써 주어야 합니다.
```kotlin
val names = mutableListOf<String>()
val user = "ada".also { names.add(it) }
println(user)  // ada
println(names) // [ada]
```
표현식의 값은 여전히 `"ada"`입니다: `also`는 그 값이 지나가는 것을 지켜볼 뿐입니다.

---

`run`은 객체를 부르는 방식만 다른 `let`입니다: 블록 안에서 객체는 `this`이므로 멤버에 접두사가 필요 없고, 호출은 **마지막 표현식의 결과**를 반환합니다.

하나의 값을 계산하기 위해 같은 객체의 여러 멤버를 읽을 때 어울립니다:
```kotlin
class Rect(val w: Int, val h: Int)

val area = Rect(3, 4).run { w * h }
println(area) // 12
```
`this`를 똑같은 방식으로 사용하지만 블록의 결과 대신 객체를 돌려주는 `apply`와 비교해 보세요.

---

`with`는 `run`과 같은 일을 하지만 **확장 함수가 아닙니다**: 객체가 점 호출의 리시버가 아니라 첫 번째 인자로 전달됩니다.
```kotlin
val text = with(StringBuilder()) {
    append("Hello")
    append(", world")
    toString()
}
println(text) // Hello, world
```
블록 안에서 객체는 `this`이고 호출은 마지막 표현식을 반환하며, 이는 `run`과 정확히 같습니다. 널이 아닌 객체를 이미 가지고 있고 그 객체에 대한 여러 호출을 묶고 싶을 때는 `with`를, 객체가 체인에서 나오거나 안전 호출이 필요할 수 있을 때는 (`obj?.run { ... }`) `run`을 선택하세요.

---

다섯 스코프 함수가 모두 준비되었고, 각각은 두 축 위의 한 점일 뿐입니다:
- `let` - 객체는 `it`, 블록의 결과를 반환
- `run` - 객체는 `this`, 블록의 결과를 반환
- `with` - 객체는 `this` (인자로 전달), 블록의 결과를 반환
- `apply` - 객체는 `this`, 객체를 반환
- `also` - 객체는 `it`, 객체를 반환

필요한 행을 고르세요: 객체를 다른 곳으로 넘길 때는 `it`이 더 자연스럽고, 멤버를 많이 다룰 때는 `this`가 더 자연스럽습니다; 새 값을 원하면 블록의 결과를 반환하고, 객체를 계속 다루고 싶으면 객체를 반환하세요.
