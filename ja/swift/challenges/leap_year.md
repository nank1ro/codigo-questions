---
language: swift
exerciseType: 1
difficulty: 3
title: うるう年
---

# --description--

暦年にはちょうど365.25日あります。しかし、最終的にこれは混乱を招きます。なぜなら、人間は通常、小数点ではなく1の正確な割り切りで数えるからです。そこで、後者を避けるために、4年周期ごとに0.25日をすべて足し合わせ、その年を366日（閏日として2月29日を含む）にして__うるう年__と呼ぶことが決められました。4年周期の他の3年は365日のみで、__うるう年ではありません__。

# --instructions--

このチャレンジでは、`Date` クラス、`switch` 文、__ifブロック__、__if-elseブロック__、__三項演算子__（`x ? a : b`）、論理演算子 __AND__（`&&`）および __OR__（`||`）を使用せずに、うるう年かどうかを判定します。ただし __NOT__（`!`）演算子は例外として使用できます。

うるう年の場合は `true` を、そうでない場合は `false` を返してください。

関数呼び出しの例:
```swift
print(leapYear(2000))
// prints true
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
func leapYear(_ year: Int) -> Bool {
    
}
```

# --asserts--

`Date`、`switch`、`if`、`else`、`&&`、`||`、`?` の使用は許可されていません。

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

年 `2016` はうるう年です。

```swift
tryCatch(leapYear(2016) == true)
```

年 `1996` はうるう年です。

```swift
tryCatch(leapYear(1996) == true)
```

年 `1600` はうるう年です。

```swift
tryCatch(leapYear(1600) == true)
```

年 `2020` はうるう年です。

```swift
tryCatch(leapYear(2020) == true)
```

年 `2000` はうるう年です。

```swift
tryCatch(leapYear(2000) == true)
```

年 `2008` はうるう年です。

```swift
tryCatch(leapYear(2008) == true)
```

年 `1521` はうるう年ではありません。

```swift
tryCatch(leapYear(1521) == false)
```

年 `1800` はうるう年ではありません。

```swift
tryCatch(leapYear(1800) == false)
```

年 `2007` はうるう年ではありません。

```swift
tryCatch(leapYear(2007) == false)
```

年 `2002` はうるう年ではありません。

```swift
tryCatch(leapYear(2002) == false)
```

年 `1979` はうるう年ではありません。

```swift
tryCatch(leapYear(1979) == false)
```

年 `2006` はうるう年ではありません。

```swift
tryCatch(leapYear(2006) == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func leapYear(_ year: Int) -> Bool {
    var yr = year
    while yr % 100 == 0 {
        yr = yr / 100
    }
    return yr % 4 == 0
}
```
