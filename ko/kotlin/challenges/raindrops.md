---
language: kotlin
exerciseType: 1
difficulty: 1
title: 빗방울
---

# --description--

주어진 숫자를 특정 인수에 해당하는 빗방울 소리가 포함된 문자열로 변환하는 것이 과제입니다.
인수란 나머지 없이 다른 숫자를 균등하게 나누는 수입니다.
어떤 수가 다른 수의 인수인지 확인하는 가장 간단한 방법은 나머지 연산을 사용하는 것입니다.
빗방울의 규칙은 주어진 숫자가 다음과 같을 때입니다:

- 3을 인수로 가지면, 결과에 'Pling'을 추가합니다.
- 5를 인수로 가지면, 결과에 'Plang'을 추가합니다.
- 7을 인수로 가지면, 결과에 'Plong'을 추가합니다.
- 3, 5, 7 중 어느 것도 인수로 가지지 않으면, 결과는 해당 숫자의 자릿수여야 합니다.

# --instructions--

올바른 문자열을 반환하는 함수를 작성하세요. 예시:

- 28은 7을 인수로 가지지만, 3이나 5는 아니므로, 결과는 `"Plong"`입니다.
- 30은 3과 5를 모두 인수로 가지지만, 7은 아니므로, 결과는 `"PlingPlang"`입니다.
- 34는 3, 5, 7의 인수가 아니므로, 결과는 `"34"`입니다.

함수 호출 예시:
```kotlin
println(raindrops(28))
// prints "Plong"
```

# --seed--

```kotlin
fun raindrops(): String {
    
}
```

# --before-seed--

```kotlin
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
fun tryCatch(assertion: Boolean) {
  _testCount++
    try { 
        if (!assertion) throw Exception()
    }
    catch (e: Throwable) {
        _testFailedCount++
        println("Test Case '--err-t$_testCount--' failed");
  }
};
// DO NOT EDIT UNTIL HERE
fun main() {
```

# --asserts--

1의 소리는 "1"입니다

```kotlin
    tryCatch(raindrops(1) == "1")
```

3의 소리는 "Pling"입니다

```kotlin
    tryCatch(raindrops(3) == "Pling")
```

5의 소리는 "Plang"입니다

```kotlin
    tryCatch(raindrops(5) == "Plang")
```

7의 소리는 "Plong"입니다

```kotlin
    tryCatch(raindrops(7) == "Plong")
```

6의 소리는 "Pling"입니다

```kotlin
    tryCatch(raindrops(6) == "Pling")
```

8의 소리는 "8"입니다

```kotlin
    tryCatch(raindrops(8) == "8")
```

9의 소리는 "Pling"입니다

```kotlin
    tryCatch(raindrops(9) == "Pling")
```

10의 소리는 "Plang"입니다

```kotlin
    tryCatch(raindrops(10) == "Plang")
```

14의 소리는 "Plong"입니다

```kotlin
    tryCatch(raindrops(14) == "Plong")
```

15의 소리는 "PlingPlang"입니다

```kotlin
    tryCatch(raindrops(15) == "PlingPlang")
```

21의 소리는 "PlingPlong"입니다

```kotlin
    tryCatch(raindrops(21) == "PlingPlong")
```

25의 소리는 "Plang"입니다

```kotlin
    tryCatch(raindrops(25) == "Plang")
```

27의 소리는 "Pling"입니다

```kotlin
    tryCatch(raindrops(27) == "Pling")
```

35의 소리는 "PlangPlong"입니다

```kotlin
    tryCatch(raindrops(35) == "PlangPlong")
```

49의 소리는 "Plong"입니다

```kotlin
    tryCatch(raindrops(49) == "Plong")
```

52의 소리는 "52"입니다

```kotlin
    tryCatch(raindrops(52) == "52")
```

105의 소리는 "PlingPlangPlong"입니다

```kotlin
    tryCatch(raindrops(105) == "PlingPlangPlong")
```

3125의 소리는 "Plang"입니다

```kotlin
    tryCatch(raindrops(3125) == "Plang")
```

# --after-asserts--

```kotlin
// DO NOT EDIT FROM HERE 
    println("Executed $_testCount tests, with $_testFailedCount failures");
}
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```kotlin
fun raindrops(num: Int): String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty()) {
        result = num.toString()     
    }
    return result
}
```
