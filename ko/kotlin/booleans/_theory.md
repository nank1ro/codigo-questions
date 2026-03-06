Kotlin에는 `Boolean`이라는 기본 불리언 타입이 있습니다.
불리언 값은 참 또는 거짓만 가질 수 있기 때문에 논리값이라고 합니다.
Kotlin에서 어떤 표현식이든 평가하면 `true` 또는 `false` 두 가지 답 중 하나를 얻을 수 있습니다.

---

숫자나 문자열처럼 불리언 값 `true`를 변수에 저장할 수 있습니다.

---

`true`의 반대 값은 `false`입니다

---

불리언 값은 앞에 `!`를 사용하여 부정할 수도 있습니다. 예를 들면:
```kotlin
println(!true) // prints false
println(!false) // prints true
```

---

`&&` (_and_)와 `||` (_or_)를 사용하여 불리언 표현식을 만들 수도 있습니다:

- `&&` (_and_): 연산자의 왼쪽과 오른쪽 불리언 표현식이 모두 참일 때만 참을 반환합니다.
- `||` (_or_): 연산자의 왼쪽 또는 오른쪽 표현식 중 하나라도 참이거나, 둘 다 참이면 참을 반환합니다.

```kotlin
println(true && true) // prints true
println(true && false) // prints false
println(false && false) // prints false
println(true || true) // prints true
println(true || false) // prints true
println(false || false) // prints false
```
