---
language: kotlin
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

In a calendar year there are exactly 365.25 days. But, eventually, this will lead to confusion because humans normally count by exact divisibility of 1 and not with decimal points. So, to avoid the latter, it was decided to add up all 0.25 days every four-year cycle and give that year 366 days (including February 29 as an intercalary day) and call it a __leap year__. The other three years in the four-year cycle would only contain 365 days and __wouldn't be leap years__.

# --instructions--

In this challenge we'll take it to a new level, where you are to determine if it's a leap year or not without the use of the `Date` class, `switch` statements, __if blocks__, __if-else blocks__ or __ternary operation__ (`x ? a : b`) nor the logical operators __AND__ (`&&`) and __OR__ (`||`) with the exemption of the __NOT__ (`!`) operator.

Return `true` if it's a leap year, `false` otherwise.

Example of function call:
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

The use of `Date`, `switch`, `if`, `else`, `&&`, `||` or `?` is not allowed.

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

The year `2016` is a leap year.

```kotlin
    tryCatch(leapYear(2016) == true)
```

The year `1996` is a leap year.

```kotlin
    tryCatch(leapYear(1996) == true)
```

The year `1600` is a leap year.

```kotlin
    tryCatch(leapYear(1600) == true)
```

The year `2020` is a leap year.

```kotlin
    tryCatch(leapYear(2020) == true)
```

The year `2000` is a leap year.

```kotlin
    tryCatch(leapYear(2000) == true)
```

The year `2008` is a leap year.

```kotlin
    tryCatch(leapYear(2008) == true)
```

The year `1521` is not a leap year.

```kotlin
    tryCatch(leapYear(1521) == false)
```

The year `1800` is not a leap year.

```kotlin
    tryCatch(leapYear(1800) == false)
```

The year `2007` is not a leap year.

```kotlin
    tryCatch(leapYear(2007) == false)
```

The year `2002` is not a leap year.

```kotlin
    tryCatch(leapYear(2002) == false)
```

The year `1979` is not a leap year.

```kotlin
    tryCatch(leapYear(1979) == false)
```

The year `2006` is not a leap year.

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
