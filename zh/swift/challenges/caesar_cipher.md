---
language: swift
exerciseType: 1
difficulty: 2
title: 凯撒密码
---

# --description--

尤利乌斯·凯撒用密码学中最古老的技巧之一来保护他的私人信件：他将消息中的每个字母替换为字母表中向前移动固定个位置的字母。当移位为 3 时，`a` 变成 `d`，`b` 变成 `e`，`c` 变成 `f`。

字母表的行为就像一个圆圈，因此末尾的字母会绕回到开头：当移位为 3 时，`x` 变成 `a`，`y` 变成 `b`，`z` 变成 `c`。

任何不是字母的字符，例如空格、逗号、感叹号或数字，都会原样通过密码，不做任何改变。

# --instructions--

编写一个函数 `caesarCipher`，它接收一个消息 `text` 和一个整数 `shift`，并返回编码后的消息。

示例：
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- 消息始终为小写，因此你不需要处理大写字母。
- 不是字母的字符保持它们的位置和值不变。
- 移位永远不会为负。移位为 `0` 时消息保持不变，移位为 `26` 时也是如此。

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
func caesarCipher(_ text: String, _ shift: Int) -> String {
    
}
```

# --asserts--

移位为 3 时，“hello” 变成 “khoor”

```swift
tryCatch(caesarCipher("hello", 3) == "khoor")
```

字母表的末尾会绕回到开头，所以 “xyz” 变成 “abc”

```swift
tryCatch(caesarCipher("xyz", 3) == "abc")
```

移位为 0 时消息保持不变

```swift
tryCatch(caesarCipher("abc", 0) == "abc")
```

移位为 26 相当于绕了字母表一整圈，所以消息保持不变

```swift
tryCatch(caesarCipher("abc", 26) == "abc")
```

标点符号和空格原样通过，不做任何改变

```swift
tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

空消息保持为空

```swift
tryCatch(caesarCipher("", 4) == "")
```

单个字母之间的空格会被保留

```swift
tryCatch(caesarCipher("a b c", 1) == "b c d")
```

即使移位为 25，数字也保持不变

```swift
tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

移位为 13 时可以编码一个完整的句子

```swift
tryCatch(caesarCipher("the quick brown fox jumps over the lazy dog", 13) == "gur dhvpx oebja sbk whzcf bire gur ynml qbt")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func caesarCipher(_ text: String, _ shift: Int) -> String {
    let a = UInt8(ascii: "a")
    let z = UInt8(ascii: "z")
    let offset = UInt8(shift % 26)
    var bytes = Array(text.utf8)

    for i in 0..<bytes.count {
        let b = bytes[i]
        if b >= a && b <= z {
            bytes[i] = a + (b - a + offset) % 26
        }
    }

    return String(decoding: bytes, as: UTF8.self)
}
```
