---
language: swift
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

> HINT: omit the argument label with the `_` (underscore)

Example of function call:
```swift
print(raindrops(28))
// prints "Plong"
```

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func raindrops() {
    
}
```

# --asserts--

The sound for 1 is "1"

```swift
tryCatch("1" == raindrops(1))
```

The sound for 3 is "Pling"

```swift
tryCatch("Pling" == raindrops(3))
```

The sound for 5 is "Plang"

```swift
tryCatch("Plang" == raindrops(5))
```

The sound for 7 is "Plong"

```swift
tryCatch("Plong" == raindrops(7))
```

The sound for 6 is "Pling"

```swift
tryCatch("Pling" == raindrops(6))
```

The sound for 8 is "8"

```swift
tryCatch("8" == raindrops(8))
```

The sound for 9 is "Pling"

```swift
tryCatch("Pling" == raindrops(9))
```

The sound for 10 is "Plang"

```swift
tryCatch("Plang" == raindrops(10))
```

The sound for 14 is "Plong"

```swift
tryCatch("Plong" == raindrops(14))
```

The sound for 15 is "PlingPlang"

```swift
tryCatch("PlingPlang" == raindrops(15))
```

The sound for 21 is "PlingPlong"

```swift
tryCatch("PlingPlong" == raindrops(21))
```

The sound for 25 is "Plang"

```swift
tryCatch("Plang" == raindrops(25))
```

The sound for 27 is "Pling"

```swift
tryCatch("Pling" == raindrops(27))
```

The sound for 35 is "PlangPlong"

```swift
tryCatch("PlangPlong" == raindrops(35))
```

The sound for 49 is "Plong"

```swift
tryCatch("Plong" == raindrops(49))
```

The sound for 52 is "52"

```swift
tryCatch("52" == raindrops(52))
```

The sound for 105 is "PlingPlangPlong"

```swift
tryCatch("PlingPlangPlong" == raindrops(105))
```

The sound for 3125 is "Plang"

```swift
tryCatch("Plang" == raindrops(3125))
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func raindrops(_ num: Int) -> String {
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
    if (result.isEmpty) {
        result = String(num);         
    }

    return result
}
```


