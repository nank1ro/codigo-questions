---
language: kotlin
exerciseType: 1
difficulty: 1
title: 算术平均值
---

# --description--

编写一个名为 `mean` 的函数来计算数值向量的_算术平均值_。

# --instructions--

编写一个返回数值向量平均值的函数。

函数调用示例：
```kotlin
val numbers = doubleArrayOf(1.0, 2.0, 3.0)
print(mean(numbers))
// prints 2.0
```

# --seed--

```kotlin
fun mean() {
    
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

`[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]` 的平均值必须等于4.0

```kotlin
    tryCatch(mean(doubleArrayOf(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0)) == 4.0)
```

`[4.0, 5.0, 6.0]` 的平均值必须等于5.0

```kotlin
    tryCatch(mean(doubleArrayOf(4.0, 5.0, 6.0)) == 5.0)
```

`[12.0, 34.0, 56.0, 78.0]` 的平均值必须等于45.0

```kotlin
    tryCatch(mean(doubleArrayOf(12.0, 34.0, 56.0, 78.0)) == 45.0)
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
fun mean(numbers: DoubleArray): Double {
  return numbers.average()
}
```
