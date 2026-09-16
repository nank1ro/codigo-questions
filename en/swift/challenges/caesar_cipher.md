---
language: swift
exerciseType: 1
difficulty: 2
title: Caesar cipher
---

# --description--

Julius Caesar protected his private letters with one of the oldest tricks in cryptography: he replaced every letter of a message with the letter a fixed number of places further along the alphabet. With a shift of 3, `a` becomes `d`, `b` becomes `e` and `c` becomes `f`.

The alphabet behaves like a circle, so the letters at the end wrap back to the start: with a shift of 3, `x` becomes `a`, `y` becomes `b` and `z` becomes `c`.

Anything that is not a letter, such as a space, a comma, an exclamation mark or a digit, travels through the cipher untouched.

# --instructions--

Write a function `caesarCipher` that takes a message `text` and a whole number `shift`, and returns the encoded message.

Examples:
```
caesarCipher("hello", 3) ➞ "khoor"
caesarCipher("xyz", 3) ➞ "abc"
caesarCipher("codigo, rocks!", 5) ➞ "htinlt, wthpx!"
```

- The message is always lowercase, so you never have to deal with uppercase letters.
- Characters that are not letters keep their place and their value.
- The shift is never negative. A shift of `0` leaves the message unchanged, and so does a shift of `26`.

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

A shift of 3 turns "hello" into "khoor"

```swift
tryCatch(caesarCipher("hello", 3) == "khoor")
```

The end of the alphabet wraps around, so "xyz" becomes "abc"

```swift
tryCatch(caesarCipher("xyz", 3) == "abc")
```

A shift of 0 leaves the message unchanged

```swift
tryCatch(caesarCipher("abc", 0) == "abc")
```

A shift of 26 is a full turn of the alphabet, so the message is unchanged

```swift
tryCatch(caesarCipher("abc", 26) == "abc")
```

Punctuation and spaces pass through unchanged

```swift
tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

An empty message stays empty

```swift
tryCatch(caesarCipher("", 4) == "")
```

Spaces between single letters are preserved

```swift
tryCatch(caesarCipher("a b c", 1) == "b c d")
```

Digits are not shifted, even with a shift of 25

```swift
tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

A shift of 13 encodes a whole sentence

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
