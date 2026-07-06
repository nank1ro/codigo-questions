함수는 특정 작업을 수행하고 프로그램 전체에서 재사용할 수 있는 코드 블록입니다.
Kotlin에서는 `fun` 키워드 뒤에 함수 이름과 괄호를 사용하여 함수를 정의합니다:
```kotlin
fun greet() {
    println("Hello!")
}
```
함수를 호출(실행)하려면, 이름 뒤에 괄호를 사용합니다:
```kotlin
greet() // prints Hello!
```
값을 반환하지 않는 함수는 암묵적으로 `Unit`을 반환합니다.

---

함수는 값을 반환할 수 있습니다. 괄호 뒤에 콜론을 사용하여 반환 타입을 지정합니다:
```kotlin
fun getNumber(): Int {
    return 42
}
```
`return` 키워드는 호출자에게 값을 돌려줍니다:
```kotlin
var result = getNumber()
println(result) // prints 42
```
반환 타입은 반환하는 값의 타입과 일치해야 합니다.

---

함수는 매개변수를 받을 수 있습니다. 매개변수는 함수를 호출할 때 전달하는 입력값입니다.
매개변수는 이름과 타입으로 괄호 안에 선언합니다:
```kotlin
fun greet(name: String) {
    println("Hello, $name!")
}
```
함수를 호출할 때 인수를 전달합니다:
```kotlin
greet("Alice") // prints Hello, Alice!
```
매개변수를 사용하면 다양한 값으로 동작하는 재사용 가능한 코드를 작성할 수 있습니다.

---

Kotlin은 기본 매개변수 값을 지원합니다. 호출자가 인수를 제공하지 않으면 기본값이 사용됩니다:
```kotlin
fun greet(name: String = "World") {
    println("Hello, $name!")
}
greet()         // prints Hello, World!
greet("Alice")  // prints Hello, Alice!
```
기본값을 사용하면 매개변수를 선택 사항으로 만들 수 있어 오버로드된 함수의 필요성이 줄어듭니다.

---

함수 본문이 단일 표현식으로 구성된 경우, `=`를 사용하는 단일 표현식 구문을 사용할 수 있습니다:
```kotlin
fun square(n: Int): Int = n * n
```
이는 블록 본문 형식보다 더 간결합니다. Kotlin은 반환 타입을 추론할 수 있는 경우가 많아 다음과 같이 작성할 수도 있습니다:
```kotlin
fun square(n: Int) = n * n
```
단일 표현식 함수는 단순한 계산에 자주 사용되는 Kotlin 관용구입니다.

---

함수는 `Boolean` 값을 반환할 수 있으며, 이는 조건을 확인하는 데 유용합니다:
```kotlin
fun isEven(n: Int): Boolean {
    return n % 2 == 0
}
println(isEven(4)) // prints true
println(isEven(7)) // prints false
```
`Boolean` 함수는 `true` 또는 `false`를 반환합니다.

---

함수는 서로 다른 타입의 여러 매개변수를 가질 수 있습니다:
```kotlin
fun introduce(name: String, age: Int): String {
    return "My name is $name and I am $age years old."
}
println(introduce("Bob", 30))
// prints My name is Bob and I am 30 years old.
```
이름 있는 인수를 사용하면 매개변수 이름을 사용하여 임의의 순서로 값을 전달할 수 있습니다:
```kotlin
println(introduce(age = 30, name = "Bob"))
```

---

Kotlin의 기본 함수는 `fun` 키워드 뒤에 이름과 괄호를 사용합니다:
```kotlin
fun sayBye() {
    println("Bye!")
}
```

---

함수의 반환 타입을 선언하려면 괄호 뒤에 콜론과 타입을 추가합니다:
```kotlin
fun getName(): String {
    return "Alice"
}
```

---

함수 매개변수는 이름, 콜론, 타입으로 선언합니다:
```kotlin
fun greet(name: String) {
    println("Hi, $name!")
}
```

---

단일 표현식 함수는 블록 본문 대신 `=`를 사용합니다:
```kotlin
fun triple(n: Int) = n * 3
```
이것은 다음의 약어입니다:
```kotlin
fun triple(n: Int): Int {
    return n * 3
}
```
