> `for` 키워드는 시퀀스의 각 값에 대해 코드 블록을 실행합니다.

`for` 루프는 이터레이터를 제공하는 모든 것을 순회합니다.

`for`의 구문은 다음과 같습니다:
```kotlin
for (item in collection) print(item)
```

`for`의 본문은 블록이 될 수도 있습니다
```kotlin
for (item in collection) {
    print(item)
}
```

루프를 통과할 때마다 `item`에는 값의 다음 요소가 할당됩니다.

다음은 고정된 횟수만큼 동작을 반복하는 `for` 루프입니다:

```kotlin
for (i in 1..3) {
    println(i)
}
// prints 1, 2, 3
```

출력은 인덱스 `i`가 _1_부터 _3_까지의 범위에서 각 값을 받는 것을 보여줍니다.

---

_범위_는 한 쌍의 끝점으로 정의된 값의 구간입니다.
범위를 정의하는 두 가지 기본 방법이 있습니다:

```kotlin
var firstRange = 1..3           // [1]
var secondRange = 1 until 3     // [2]
println(firstRange)
println(secondRange)

/* prints
1..3
1..2
*/
```

- __[1]__ `..` 구문을 사용하면 결과 범위에 양쪽 끝점이 모두 포함됩니다.
- __[2]__ `until`은 끝 값을 제외합니다. 출력에서 _3_이 범위에 포함되지 않는 것을 확인할 수 있습니다.

---

범위를 역순으로 순회할 수 있습니다.

`3..1`이 작동할 것이라고 예상하겠지만, 안타깝게도 Kotlin 팀은 이 기능을 다른 방식으로 가져오기로 결정했습니다.

실제로 다음 코드를 실행하면:
```kotlin
for (i in 3..1) println(i)
```

아무것도 출력되지 않는 것을 확인할 수 있습니다.
이것이 작동하도록 하려면 `downTo` 키워드를 사용해야 합니다:

```kotlin
for (i in 3 downTo 1) println(i)
// prints 3, 2, 1
```

`downTo`는 감소하는 범위를 생성합니다.

---

범위의 기본 _스텝_은 __1__이지만, 다른 값을 명시적으로 설정할 수 있습니다.

`step` 키워드를 사용하여 `for` 루프의 __스텝__을 정의할 수 있습니다.

```kotlin
for (i in 1..10 step 2) {
    println(i)
}
// prints 1, 3, 5, 7, 9
```

보시다시피, 코드 블록이 _1_ 대신 _2_의 스텝으로 실행되어 출력이 완전히 달라집니다.

---

_문자_의 범위도 생성할 수 있습니다.
```kotlin
for (char in 'a'..'z') print(char)
// prints abcdefghijklmnopqrstuvwxyz
```

---

__문자열__을 순회할 수 있습니다.
```kotlin
for (char in 'abc') print(char + 1)
// prints bdc
```

위의 예시에서는 각 문자 + 1을 출력했으므로, `'a'`는 `'b'`가 되고, `'b'`는 `'c'`가 되는 식입니다.

이것은 문자가 [ASCII 코드](https://en.wikipedia.org/wiki/ASCII)에 해당하는 숫자로 저장되기 때문에 가능합니다.

따라서 문자에 정수를 더하면 새로운 코드 값에 해당하는 새로운 문자가 생성됩니다.

---

단순히 코드 블록을 `n`번 반복해야 하는 경우, `repeat(times: Int)` 함수를 사용할 수 있습니다.

```kotlin
repeat(3) {
    println("repeat")
}
// prints repeat 3 times
```

인덱스에도 접근할 수 있습니다
```kotlin
repeat(3) { index ->
    println(index)
}
// prints 0, 1, 2
```

---

Kotlin에서는 `for-in`을 사용하여 반복 가능한 컬렉션의 각 요소에 주어진 클로저를 호출할 수도 있습니다:
```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(2, 4, 6, 8, 10)
for (num in numbers) {
    println(num)
}
// prints (2, 4, 6, 8, 10)
```

---

Kotlin에는 `forEach` 루프도 있습니다.
`for-in` 루프와 동일한 순서로 시퀀스의 각 요소에 주어진 클로저를 호출합니다:

```kotlin
// this is a list, we'll see about that soon
val numbers = listOf(1, 3, 5, 7, 9)
numbers.forEach {
    println(it)
}
```

`forEach` 메서드를 사용하는 것은 `for-in` 루프와 두 가지 중요한 차이점이 있습니다:
1. `break` 또는 `continue` 문을 사용하여 현재 본문 클로저 호출을 종료하거나 후속 호출을 건너뛸 수 없습니다. (_사실 어노테이션을 사용하면 가능하지만, 지금은 다루지 않을 좀 더 복잡한 주제입니다._)
2. 본문 클로저에서 `return` 문을 사용하면 외부 스코프가 아닌 클로저만 종료하며, 후속 호출을 건너뛰지 않습니다.
