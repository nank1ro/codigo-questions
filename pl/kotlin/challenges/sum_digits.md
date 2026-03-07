---
language: kotlin
exerciseType: 1
difficulty: 1
title: Sum of digits
---

# --description--

Dana jest liczba całkowita `N`.
Napisz program obliczający sumę wszystkich cyfr liczby N.

# --instructions--

Zwróć sumę cyfr liczby `N`.

Przykład wywołania funkcji:
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

Suma cyfr liczby 12345 wynosi 15

```kotlin
    tryCatch(sumDigits(12345) == 15)
```

Suma cyfr liczby 57253 wynosi 22

```kotlin
    tryCatch(sumDigits(57253) == 22)
```

Suma cyfr liczby 122 wynosi 5

```kotlin
    tryCatch(sumDigits(122) == 5)
```

Suma cyfr liczby 91979997 wynosi 60

```kotlin
    tryCatch(sumDigits(91979997) == 60)
```

Suma cyfr liczby 2147483647 wynosi 46

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

