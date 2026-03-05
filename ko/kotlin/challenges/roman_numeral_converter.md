---
language: kotlin
exerciseType: 1
difficulty: 3
title: 로마 숫자 변환기
---

# --description--

양의 정수를 매개변수로 받아 해당 정수의 로마 숫자 표현을 포함하는 문자열을 반환하는 함수를 만드세요. 현대 로마 숫자는 각 자릿수를 개별적으로 표현하며, 가장 왼쪽 자릿수부터 시작하고 값이 0인 자릿수는 건너뜁니다.

# --instructions--

예시:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- 모든 로마 숫자는 대문자로 반환되어야 합니다.
- 이 표기법으로 표현할 수 있는 가장 큰 수는 3,999입니다.

# --seed--

```kotlin
fun convertToRoman(n: Int): String {
    
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

숫자 `2`는 `II`와 같아야 합니다

```kotlin
    tryCatch(convertToRoman(2) == "II")
```

숫자 `12`는 `XII`와 같아야 합니다

```kotlin
    tryCatch(convertToRoman(12) == "XII")
```

숫자 `16`은 `XVI`와 같아야 합니다

```kotlin
    tryCatch(convertToRoman(16) == "XVI")
```

숫자 `44`는 `XLIV`와 같아야 합니다

```kotlin
    tryCatch(convertToRoman(44) == "XLIV")
```

숫자 `68`은 `LXVIII`와 같아야 합니다

```kotlin
    tryCatch(convertToRoman(68) == "LXVIII")
```

숫자 `400`은 `CD`와 같아야 합니다

```kotlin
    tryCatch(convertToRoman(400) == "CD")
```

숫자 `798`은 `DCCXCVIII`와 같아야 합니다

```kotlin
    tryCatch(convertToRoman(798) == "DCCXCVIII")
```

숫자 `1000`은 `M`과 같아야 합니다

```kotlin
    tryCatch(convertToRoman(1000) == "M")
```

숫자 `3999`는 `MMMCMXCIX`와 같아야 합니다

```kotlin
    tryCatch(convertToRoman(3999) == "MMMCMXCIX")
```

숫자 `649`는 `DCXLIX`와 같아야 합니다

```kotlin
    tryCatch(convertToRoman(649) == "DCXLIX")
```

숫자 `1666`은 `MDCLXVI`와 같아야 합니다

```kotlin
    tryCatch(convertToRoman(1666) == "MDCLXVI")
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
fun convertToRoman(n: Int): String {
    var result = ""
    var number = n

    val values = listOf(
        Pair(1000, "M"),
        Pair(900, "CM"),
        Pair(500, "D"),
        Pair(400, "CD"),
        Pair(100, "C"),
        Pair(90, "XC"),
        Pair(50, "L"),
        Pair(40, "XL"),
        Pair(10, "X"),
        Pair(9, "IX"),
        Pair(5, "V"),
        Pair(4, "IV"),
        Pair(1, "I")
    )

    for (i in values.indices) {
        val value = values[i].first
        val letter = values[i].second

        while (number >= value) {
            result += letter
            number -= value
        }
    }

    return result
}
```
