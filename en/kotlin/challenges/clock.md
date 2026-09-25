---
language: kotlin
exerciseType: 1
difficulty: 2
title: Clock
---

# --description--

A 24-hour clock shows the time of day as `HH:MM`, starting at `00:00` just after midnight and ending at `23:59` one minute before the next midnight. Both parts are always written with two digits, so nine minutes past eleven in the morning reads `11:09`.

A whole day lasts 1440 minutes. Once the clock passes `23:59` it rolls over to `00:00` and starts the day again, and winding it backwards past `00:00` lands on `23:59`.

# --instructions--

Write a function `clockTime` that takes two whole numbers, `hours` and `minutes`, and returns the reading of a 24-hour clock as the string `"HH:MM"`, with both parts padded to two digits.

Examples:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- Either number may be negative, or larger than a real clock allows.
- Work out the total number of minutes as `hours * 60 + minutes`, then wrap that total into the range `0` to `1439` so the clock rolls over in both directions.
- `clockTime(24, 0)` is exactly one day, so it reads `"00:00"`.

# --seed--

```kotlin
fun clockTime(hours: Int, minutes: Int): String {
    
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

Eight in the morning reads `08:00`

```kotlin
    tryCatch(clockTime(8, 0) == "08:00")
```

Single digits are padded to two, so nine minutes past eleven reads `11:09`

```kotlin
    tryCatch(clockTime(11, 9) == "11:09")
```

Exactly one full day of hours rolls over to `00:00`

```kotlin
    tryCatch(clockTime(24, 0) == "00:00")
```

Minutes over 60 carry into the hours

```kotlin
    tryCatch(clockTime(25, 160) == "03:40")
```

A negative hour winds the clock backwards past midnight

```kotlin
    tryCatch(clockTime(-1, 15) == "23:15")
```

A negative minute count also winds the clock backwards

```kotlin
    tryCatch(clockTime(0, -90) == "22:30")
```

More than a whole day backwards keeps rolling over

```kotlin
    tryCatch(clockTime(-25, 0) == "23:00")
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
fun clockTime(hours: Int, minutes: Int): String {
    // % keeps the sign of the left operand, but mod() always wraps forward
    // into 0..1439.
    val total = (hours * 60 + minutes).mod(1440)

    return "%02d:%02d".format(total / 60, total % 60)
}
```
