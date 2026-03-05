---
language: kotlin
exerciseType: 1
difficulty: 1
title: 数字の合計
---

# --description--

整数`N`が与えられます。
Nのすべての桁の合計を計算するプログラムを書いてください

# --instructions--

`N`の桁の合計を返してください。

関数呼び出しの例：
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

12345の桁の合計は15です

```kotlin
    tryCatch(sumDigits(12345) == 15)
```

57253の桁の合計は22です

```kotlin
    tryCatch(sumDigits(57253) == 22)
```

122の桁の合計は5です

```kotlin
    tryCatch(sumDigits(122) == 5)
```

91979997の桁の合計は60です

```kotlin
    tryCatch(sumDigits(91979997) == 60)
```

2147483647の桁の合計は46です

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

