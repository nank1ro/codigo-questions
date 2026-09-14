---
language: swift
exerciseType: 1
difficulty: 1
title: コラッツの予想
---

# --description--

コラッツの予想は、任意の正の整数`n`から始めて、1つの単純な規則を繰り返します。`n`が偶数ならそれを半分にし、`n`が奇数なら`3n + 1`で置き換えます。いずれ数列は1に到達します。

例えば、16から始めると数列は`16 -> 8 -> 4 -> 2 -> 1`となり、4ステップかかります。

これが常に起こると証明した人はまだいませんが、これまでテストされたすべての数で成り立っています。

# --instructions--

正の整数`n`を受け取り、1に到達するまでに必要なステップ数を返す関数`collatzSteps`を書いてください。

`collatzSteps(1)`は0になります。1はすでに数列の終わりだからです。`collatzSteps(12)`は9、`collatzSteps(27)`は111です。

関数呼び出しの例：
```swift
print(collatzSteps(16))
// prints 4
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
func collatzSteps(_ n: Int) -> Int {

}
```

# --asserts--

`collatzSteps(1)`は、1がすでに数列の終わりであるため、0を返すべきです。

```swift
tryCatch(collatzSteps(1) == 0)
```

`collatzSteps(2)`は1を返すべきです。

```swift
tryCatch(collatzSteps(2) == 1)
```

`collatzSteps(6)`は8を返すべきです。

```swift
tryCatch(collatzSteps(6) == 8)
```

`collatzSteps(7)`は16を返すべきです。

```swift
tryCatch(collatzSteps(7) == 16)
```

`collatzSteps(16)`は4を返すべきです。

```swift
tryCatch(collatzSteps(16) == 4)
```

`collatzSteps(12)`は9を返すべきです。

```swift
tryCatch(collatzSteps(12) == 9)
```

`collatzSteps(27)`は111を返すべきです。

```swift
tryCatch(collatzSteps(27) == 111)
```

`collatzSteps(97)`は118を返すべきです。

```swift
tryCatch(collatzSteps(97) == 118)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func collatzSteps(_ n: Int) -> Int {
    var value = n
    var steps = 0
    while value != 1 {
        value = value % 2 == 0 ? value / 2 : 3 * value + 1
        steps += 1
    }
    return steps
}
```
