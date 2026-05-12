---
language: swift
exerciseType: 1
difficulty: 1
title: 雨粒
---

# --description--

あなたのタスクは、数値を特定の因数に対応する雨音を含む文字列に変換することです。
因数とは、別の数を余りなく割り切れる数のことです。
ある数が別の数の因数であるかどうかをテストする最も簡単な方法は、剰余演算を使用することです。
雨粒のルールは、与えられた数が:

- 3を因数に持つ場合、結果に 'Pling' を追加します。
- 5を因数に持つ場合、結果に 'Plang' を追加します。
- 7を因数に持つ場合、結果に 'Plong' を追加します。
- 3、5、7のいずれも因数に持たない場合、結果はその数の数字になります。

# --instructions--

正しい文字列を返す関数を書いてください。例:

- 28は7を因数に持ちますが、3や5は持たないので、結果は `"Plong"` になります。
- 30は3と5の両方を因数に持ちますが、7は持たないので、結果は `"PlingPlang"` になります。
- 34は3、5、7のいずれの因数も持たないので、結果は `"34"` になります。

> ヒント: `_`（アンダースコア）で引数ラベルを省略してください

関数呼び出しの例:
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

1の音は "1"

```swift
tryCatch("1" == raindrops(1))
```

3の音は "Pling"

```swift
tryCatch("Pling" == raindrops(3))
```

5の音は "Plang"

```swift
tryCatch("Plang" == raindrops(5))
```

7の音は "Plong"

```swift
tryCatch("Plong" == raindrops(7))
```

6の音は "Pling"

```swift
tryCatch("Pling" == raindrops(6))
```

8の音は "8"

```swift
tryCatch("8" == raindrops(8))
```

9の音は "Pling"

```swift
tryCatch("Pling" == raindrops(9))
```

10の音は "Plang"

```swift
tryCatch("Plang" == raindrops(10))
```

14の音は "Plong"

```swift
tryCatch("Plong" == raindrops(14))
```

15の音は "PlingPlang"

```swift
tryCatch("PlingPlang" == raindrops(15))
```

21の音は "PlingPlong"

```swift
tryCatch("PlingPlong" == raindrops(21))
```

25の音は "Plang"

```swift
tryCatch("Plang" == raindrops(25))
```

27の音は "Pling"

```swift
tryCatch("Pling" == raindrops(27))
```

35の音は "PlangPlong"

```swift
tryCatch("PlangPlong" == raindrops(35))
```

49の音は "Plong"

```swift
tryCatch("Plong" == raindrops(49))
```

52の音は "52"

```swift
tryCatch("52" == raindrops(52))
```

105の音は "PlingPlangPlong"

```swift
tryCatch("PlingPlangPlong" == raindrops(105))
```

3125の音は "Plang"

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


