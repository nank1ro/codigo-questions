---
language: kotlin
exerciseType: 1
difficulty: 1
title: 数字之和
---

# --description--

给定一个整数 `N`。
编写一个程序计算N的所有数字之和

# --instructions--

返回 `N` 的数字之和。

函数调用示例：
```kotlin
println(sumDigits(28))
// prints 10
```

# --seed--

```kotlin
fun sumDigits() {

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

12345的数字之和为15

```kotlin
    tryCatch(sumDigits(12345) == 15)
```

57253的数字之和为22

```kotlin
    tryCatch(sumDigits(57253) == 22)
```

122的数字之和为5

```kotlin
    tryCatch(sumDigits(122) == 5)
```

91979997的数字之和为60

```kotlin
    tryCatch(sumDigits(91979997) == 60)
```

2147483647的数字之和为46

```kotlin
    tryCatch(sumDigits(2147483647) == 46)
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
fun sumDigits(num: Int): Int {
    var n = num
    var result = 0
    while (n > 0) {
        result += n % 10
        n = (n / 10).toInt()
    }
    return result
}
```

