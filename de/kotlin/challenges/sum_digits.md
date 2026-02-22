---
language: kotlin
exerciseType: 1
difficulty: 1
title: Sum of digits
---

# --description--

You're given an integer `N`.
Write a program to calculate the sum of all the digits of N

# --instructions--

Return the sum of digits of `N`.

Example of function call:
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

The sum of the digits of 12345 is 15

```kotlin
    tryCatch(sumDigits(12345) == 15)
```

The sum of the digits of 57253 is 22

```kotlin
    tryCatch(sumDigits(57253) == 22)
```

The sum of the digits of 122 is 5

```kotlin
    tryCatch(sumDigits(122) == 5)
```

The sum of the digits of 91979997 is 60

```kotlin
    tryCatch(sumDigits(91979997) == 60)
```

The sum of the digits of 2147483647 is 46

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

