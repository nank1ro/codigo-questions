---
language: kotlin
exerciseType: 1
difficulty: 2
title: Luhn 체크섬
---

# --description--

Luhn 알고리즘은 신용카드 번호와 같은 식별 번호를 검증하는 데 사용되는 간단한 체크섬입니다.

수를 검사하기 전에 문자열에서 모든 공백을 제거합니다. 남은 부분이 한 문자보다 길고 원래 문자열이 숫자와 공백만을 담고 있을 때만 그 문자열은 유효합니다.

검사를 수행하려면 가장 오른쪽 자릿수부터 시작하여 왼쪽으로 이동하면서 한 칸 건너있는 자릿수마다 2배를 합니다. 2배한 값이 9보다 크면 9를 뺍니다. 그다음 모든 자릿수를 더합니다. 이 합계가 10으로 나누어떨어질 때만 그 수는 유효합니다.

예를 들어 `"059"`는 `0`이고, 그다음 `5`를 2배한 `10`은 `1`이 되며, 마지막은 `9`입니다. 이들의 합은 `10`이고 10으로 나누어떨어지므로 이 수는 유효합니다.

# --instructions--

문자열을 받아 수가 유효하면 `true`를, 그렇지 않으면 `false`를 반환하는 함수 `isValid`를 작성하세요.

- `"4539 3195 0343 6467"`은 체크섬을 통과하므로 결과는 `true`입니다.
- `"8273 1232 7352 0569"`는 체크섬을 통과하지 못하므로 결과는 `false`입니다.
- `"0"`은 길이가 한 문자뿐이므로 결과는 `false`입니다.
- `"055-444-285"`에는 숫자나 공백이 아닌 문자가 포함되어 있으므로 결과는 `false`입니다.

함수 호출 예시:
```kotlin
println(isValid("095 245 88"))
// true를 출력합니다
```

# --seed--

```kotlin
fun isValid(value: String): Boolean {
    
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

한 자리 숫자는 유효하지 않습니다.

```kotlin
    tryCatch(isValid("0") == false)
```

앞에 공백이 있는 한 자리 숫자는 유효하지 않습니다.

```kotlin
    tryCatch(isValid(" 0") == false)
```

숫자 `"059"`는 유효합니다.

```kotlin
    tryCatch(isValid("059") == true)
```

숫자 `"59"`는 유효합니다.

```kotlin
    tryCatch(isValid("59") == true)
```

숫자 `"055 444 285"`는 유효합니다.

```kotlin
    tryCatch(isValid("055 444 285") == true)
```

숫자 `"055 444 286"`은 유효하지 않습니다.

```kotlin
    tryCatch(isValid("055 444 286") == false)
```

숫자 `"8273 1232 7352 0569"`는 유효하지 않습니다.

```kotlin
    tryCatch(isValid("8273 1232 7352 0569") == false)
```

숫자 `"4539 3195 0343 6467"`은 유효합니다.

```kotlin
    tryCatch(isValid("4539 3195 0343 6467") == true)
```

숫자 `"1 2345 6789 1234 5678 9012"`는 유효하지 않습니다.

```kotlin
    tryCatch(isValid("1 2345 6789 1234 5678 9012") == false)
```

숫자 `"095 245 88"`는 유효합니다.

```kotlin
    tryCatch(isValid("095 245 88") == true)
```

영문자가 있으면 숫자는 유효하지 않습니다.

```kotlin
    tryCatch(isValid("055a 444 285") == false)
```

대시가 있으면 숫자는 유효하지 않습니다.

```kotlin
    tryCatch(isValid("055-444-285") == false)
```

문장 부호가 있으면 숫자는 유효하지 않습니다.

```kotlin
    tryCatch(isValid(":9") == false)
```

기호가 있으면 숫자는 유효하지 않습니다.

```kotlin
    tryCatch(isValid("055# 444\$ 285") == false)
```

빈 문자열은 유효하지 않습니다.

```kotlin
    tryCatch(isValid("") == false)
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
fun isValid(value: String): Boolean {
    var sum = 0
    var count = 0
    for (i in value.length - 1 downTo 0) {
        val character = value[i]
        if (character == ' ') {
            continue
        }
        if (character < '0' || character > '9') {
            return false
        }
        var digit = character - '0'
        if (count % 2 == 1) {
            digit *= 2
            if (digit > 9) {
                digit -= 9
            }
        }
        sum += digit
        count++
    }
    return count > 1 && sum % 10 == 0
}
```
