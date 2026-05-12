---
language: swift
exerciseType: 1
difficulty: 1
title: 雨滴
---

# --description--

你的任务是将一个数字转换为包含与某些潜在因数对应的雨滴声的字符串。
因数是能够整除另一个数字且没有余数的数字。
测试一个数字是否是另一个数字的因数的最简单方法是使用取模运算。
雨滴的规则是，如果给定的数字：

- 有因数 3，则在结果中添加 'Pling'。
- 有因数 5，则在结果中添加 'Plang'。
- 有因数 7，则在结果中添加 'Plong'。
- 没有 3、5 或 7 作为因数，结果应该是该数字本身。

# --instructions--

编写一个返回正确字符串的函数，示例：

- 28 有因数 7，但没有 3 或 5，所以结果是 `"Plong"`。
- 30 同时有因数 3 和 5，但没有 7，所以结果是 `"PlingPlang"`。
- 34 不能被 3、5 或 7 整除，所以结果是 `"34"`。

> 提示：使用 `_`（下划线）省略参数标签

函数调用示例：
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

1 的声音是 "1"

```swift
tryCatch("1" == raindrops(1))
```

3 的声音是 "Pling"

```swift
tryCatch("Pling" == raindrops(3))
```

5 的声音是 "Plang"

```swift
tryCatch("Plang" == raindrops(5))
```

7 的声音是 "Plong"

```swift
tryCatch("Plong" == raindrops(7))
```

6 的声音是 "Pling"

```swift
tryCatch("Pling" == raindrops(6))
```

8 的声音是 "8"

```swift
tryCatch("8" == raindrops(8))
```

9 的声音是 "Pling"

```swift
tryCatch("Pling" == raindrops(9))
```

10 的声音是 "Plang"

```swift
tryCatch("Plang" == raindrops(10))
```

14 的声音是 "Plong"

```swift
tryCatch("Plong" == raindrops(14))
```

15 的声音是 "PlingPlang"

```swift
tryCatch("PlingPlang" == raindrops(15))
```

21 的声音是 "PlingPlong"

```swift
tryCatch("PlingPlong" == raindrops(21))
```

25 的声音是 "Plang"

```swift
tryCatch("Plang" == raindrops(25))
```

27 的声音是 "Pling"

```swift
tryCatch("Pling" == raindrops(27))
```

35 的声音是 "PlangPlong"

```swift
tryCatch("PlangPlong" == raindrops(35))
```

49 的声音是 "Plong"

```swift
tryCatch("Plong" == raindrops(49))
```

52 的声音是 "52"

```swift
tryCatch("52" == raindrops(52))
```

105 的声音是 "PlingPlangPlong"

```swift
tryCatch("PlingPlangPlong" == raindrops(105))
```

3125 的声音是 "Plang"

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


