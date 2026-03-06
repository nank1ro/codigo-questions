---
language: kotlin
exerciseType: 1
difficulty: 1
title: 雨滴
---

# --description--

你的任务是将一个数字转换为包含与特定潜在因数对应的雨滴声的字符串。
因数是能整除另一个数字且没有余数的数。
测试一个数字是否是另一个数字的因数，最简单的方法是使用取模运算。
雨滴的规则如下：

- 如果给定数字有因数3，将 'Pling' 添加到结果中。
- 如果给定数字有因数5，将 'Plang' 添加到结果中。
- 如果给定数字有因数7，将 'Plong' 添加到结果中。
- 如果给定数字没有3、5或7作为因数，结果应为该数字本身。

# --instructions--

编写一个返回正确字符串的函数，示例：

- 28有因数7，但没有3或5，所以结果为 `"Plong"`。
- 30同时有因数3和5，但没有7，所以结果为 `"PlingPlang"`。
- 34不能被3、5或7整除，所以结果为 `"34"`。

函数调用示例：
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

1的声音是 "1"

```kotlin
    tryCatch(raindrops(1) == "1")
```

3的声音是 "Pling"

```kotlin
    tryCatch(raindrops(3) == "Pling")
```

5的声音是 "Plang"

```kotlin
    tryCatch(raindrops(5) == "Plang")
```

7的声音是 "Plong"

```kotlin
    tryCatch(raindrops(7) == "Plong")
```

6的声音是 "Pling"

```kotlin
    tryCatch(raindrops(6) == "Pling")
```

8的声音是 "8"

```kotlin
    tryCatch(raindrops(8) == "8")
```

9的声音是 "Pling"

```kotlin
    tryCatch(raindrops(9) == "Pling")
```

10的声音是 "Plang"

```kotlin
    tryCatch(raindrops(10) == "Plang")
```

14的声音是 "Plong"

```kotlin
    tryCatch(raindrops(14) == "Plong")
```

15的声音是 "PlingPlang"

```kotlin
    tryCatch(raindrops(15) == "PlingPlang")
```

21的声音是 "PlingPlong"

```kotlin
    tryCatch(raindrops(21) == "PlingPlong")
```

25的声音是 "Plang"

```kotlin
    tryCatch(raindrops(25) == "Plang")
```

27的声音是 "Pling"

```kotlin
    tryCatch(raindrops(27) == "Pling")
```

35的声音是 "PlangPlong"

```kotlin
    tryCatch(raindrops(35) == "PlangPlong")
```

49的声音是 "Plong"

```kotlin
    tryCatch(raindrops(49) == "Plong")
```

52的声音是 "52"

```kotlin
    tryCatch(raindrops(52) == "52")
```

105的声音是 "PlingPlangPlong"

```kotlin
    tryCatch(raindrops(105) == "PlingPlangPlong")
```

3125的声音是 "Plang"

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
