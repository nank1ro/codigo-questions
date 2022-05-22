---
language: kotlin
exerciseType: 1
difficulty: 1
title: Raindrops
---

# --description--

Your task is to convert a number into a string that contains raindrop sounds corresponding to certain potential factors.
A factor is a number that evenly divides into another number, leaving no remainder.
The simplest way to test if a number is a factor of another is to use the modulo operation.
The rules of raindrops are that if a given number:

- has 3 as a factor, add 'Pling' to the result.
- has 5 as a factor, add 'Plang' to the result.
- has 7 as a factor, add 'Plong' to the result.
- does not have any of 3, 5, or 7 as a factor, the result should be the digits of the number.

# --instructions--

Write a function that returns the correct string, examples:

- 28 has 7 as a factor, but not 3 or 5, so the result would be `"Plong"`.
- 30 has both 3 and 5 as factors, but not 7, so the result would be `"PlingPlang"`.
- 34 is not factored by 3, 5, or 7, so the result would be `"34"`.

Example of function call:
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

The sound for 1 is "1"

```kotlin
    tryCatch(raindrops(1) == "1")
```

The sound for 3 is "Pling"

```kotlin
    tryCatch(raindrops(3) == "Pling")
```

The sound for 5 is "Plang"

```kotlin
    tryCatch(raindrops(5) == "Plang")
```

The sound for 7 is "Plong"

```kotlin
    tryCatch(raindrops(7) == "Plong")
```

The sound for 6 is "Pling"

```kotlin
    tryCatch(raindrops(6) == "Pling")
```

The sound for 8 is "8"

```kotlin
    tryCatch(raindrops(8) == "8")
```

The sound for 9 is "Pling"

```kotlin
    tryCatch(raindrops(9) == "Pling")
```

The sound for 10 is "Plang"

```kotlin
    tryCatch(raindrops(10) == "Plang")
```

The sound for 14 is "Plong"

```kotlin
    tryCatch(raindrops(14) == "Plong")
```

The sound for 15 is "PlingPlang"

```kotlin
    tryCatch(raindrops(15) == "PlingPlang")
```

The sound for 21 is "PlingPlong"

```kotlin
    tryCatch(raindrops(21) == "PlingPlong")
```

The sound for 25 is "Plang"

```kotlin
    tryCatch(raindrops(25) == "Plang")
```

The sound for 27 is "Pling"

```kotlin
    tryCatch(raindrops(27) == "Pling")
```

The sound for 35 is "PlangPlong"

```kotlin
    tryCatch(raindrops(35) == "PlangPlong")
```

The sound for 49 is "Plong"

```kotlin
    tryCatch(raindrops(49) == "Plong")
```

The sound for 52 is "52"

```kotlin
    tryCatch(raindrops(52) == "52")
```

The sound for 105 is "PlingPlangPlong"

```kotlin
    tryCatch(raindrops(105) == "PlingPlangPlong")
```

The sound for 3125 is "Plang"

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
