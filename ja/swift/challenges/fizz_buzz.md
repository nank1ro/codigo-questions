---
language: swift
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

数値を引数として受け取り、`"Fizz"`、`"Buzz"`、または `"FizzBuzz"` を返す関数を作成してください。

# --instructions--

- 数が `3` の倍数の場合、出力は `"Fizz"` になります
- 与えられた数が `5` の倍数の場合、出力は `"Buzz"` になります。
- 与えられた数が `3` と `5` の両方の倍数の場合、出力は `"FizzBuzz"` になります。
- 数が `3` でも `5` の倍数でもない場合、以下の例に示すように数値そのものを出力します。
- 出力は `3` や `5` の倍数でなくても常に文字列でなければなりません。

例:
```swift
fizz_buzz(3) // ➞ "Fizz"
fizz_buzz(5) // ➞ "Buzz"
fizz_buzz(15) // ➞ "FizzBuzz"
fizz_buzz(4) // ➞ "4"
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
func fizzBuzz() {
    
}
```

# --asserts--

数 `3` は `"Fizz"` に等しくなければなりません

```swift
tryCatch(fizzBuzz(3) == "Fizz")
```

数 `5` は `"Buzz"` に等しくなければなりません

```swift
tryCatch(fizzBuzz(5) == "Buzz")
```

数 `15` は `"FizzBuzz"` に等しくなければなりません

```swift
tryCatch(fizzBuzz(15) == "FizzBuzz")
```

数 `10` は `"Buzz"` に等しくなければなりません

```swift
tryCatch(fizzBuzz(10) == "Buzz")
```

数 `98` は `"98"` に等しくなければなりません

```swift
tryCatch(fizzBuzz(98) == "98")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func fizzBuzz(_ number: Int) -> String {
    if number % 3 == 0 && number % 5 == 0 {
        return "FizzBuzz"
    }
    if number % 3 == 0 {
        return "Fizz"
    }
    if number % 5 == 0 {
        return "Buzz"
    }
    return String(number)
}
```
