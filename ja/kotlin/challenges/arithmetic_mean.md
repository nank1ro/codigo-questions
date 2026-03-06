---
language: kotlin
exerciseType: 1
difficulty: 1
title: 算術平均
---

# --description--

数値ベクトルの_算術平均_を求める`mean`という関数を書いてください。

# --instructions--

数値ベクトルの平均を返す関数を書いてください。

関数呼び出しの例：
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

`[1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0]`の平均は4.0に等しくなければなりません

```kotlin
    tryCatch(mean(doubleArrayOf(1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0)) == 4.0)
```

`[4.0, 5.0, 6.0]`の平均は5.0に等しくなければなりません

```kotlin
    tryCatch(mean(doubleArrayOf(4.0, 5.0, 6.0)) == 5.0)
```

`[12.0, 34.0, 56.0, 78.0]`の平均は45.0に等しくなければなりません

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
