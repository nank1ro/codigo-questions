---
language: kotlin
exerciseType: 1
difficulty: 3
title: 윤년
---

# --description--

달력의 한 해에는 정확히 365.25일이 있습니다. 하지만 결국 이것은 혼란을 야기할 수 있는데, 인간은 보통 소수점이 아닌 1의 정확한 나눗셈으로 계산하기 때문입니다. 그래서 이를 피하기 위해, 4년 주기마다 0.25일을 모두 합산하여 그 해에 366일을 부여하고 (2월 29일을 윤일로 포함) 이를 __윤년__이라고 부르기로 했습니다. 4년 주기의 나머지 3년은 365일만 포함하며 __윤년이 아닙니다__.

# --instructions--

이 챌린지에서는 한 단계 더 나아가, `Date` 클래스, `switch` 문, __if 블록__, __if-else 블록__ 또는 __삼항 연산__ (`x ? a : b`)을 사용하지 않고, __NOT__ (`!`) 연산자를 제외한 논리 연산자 __AND__ (`&&`)와 __OR__ (`||`)도 사용하지 않고 윤년인지 판별해야 합니다.

윤년이면 `true`를, 그렇지 않으면 `false`를 반환하세요.

함수 호출 예시:
```kotlin
println(leapYear(2000))
// prints true
```

# --seed--

```kotlin
fun leapYear(year: Int): Boolean {
    
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

`Date`, `switch`, `if`, `else`, `&&`, `||` 또는 `?`의 사용은 허용되지 않습니다.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

`2016`년은 윤년입니다.

```kotlin
    tryCatch(leapYear(2016) == true)
```

`1996`년은 윤년입니다.

```kotlin
    tryCatch(leapYear(1996) == true)
```

`1600`년은 윤년입니다.

```kotlin
    tryCatch(leapYear(1600) == true)
```

`2020`년은 윤년입니다.

```kotlin
    tryCatch(leapYear(2020) == true)
```

`2000`년은 윤년입니다.

```kotlin
    tryCatch(leapYear(2000) == true)
```

`2008`년은 윤년입니다.

```kotlin
    tryCatch(leapYear(2008) == true)
```

`1521`년은 윤년이 아닙니다.

```kotlin
    tryCatch(leapYear(1521) == false)
```

`1800`년은 윤년이 아닙니다.

```kotlin
    tryCatch(leapYear(1800) == false)
```

`2007`년은 윤년이 아닙니다.

```kotlin
    tryCatch(leapYear(2007) == false)
```

`2002`년은 윤년이 아닙니다.

```kotlin
    tryCatch(leapYear(2002) == false)
```

`1979`년은 윤년이 아닙니다.

```kotlin
    tryCatch(leapYear(1979) == false)
```

`2006`년은 윤년이 아닙니다.

```kotlin
    tryCatch(leapYear(2006) == false)
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
fun leapYear(year: Int): Boolean {
  var tempYear = year
  while (tempYear % 100 == 0) {
    tempYear = tempYear / 100
  }
  return tempYear % 4 == 0
}
```
