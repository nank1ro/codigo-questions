---
language: kotlin
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

# --seed--

```kotlin
fun caesarCipher(text: String, shift: Int): String {
    
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

A shift of 3 turns "hello" into "khoor"

```kotlin
    tryCatch(caesarCipher("hello", 3) == "khoor")
```

The end of the alphabet wraps around, so "xyz" becomes "abc"

```kotlin
    tryCatch(caesarCipher("xyz", 3) == "abc")
```

A shift of 0 leaves the message unchanged

```kotlin
    tryCatch(caesarCipher("abc", 0) == "abc")
```

A shift of 26 is a full turn of the alphabet, so the message is unchanged

```kotlin
    tryCatch(caesarCipher("abc", 26) == "abc")
```

Punctuation and spaces pass through unchanged

```kotlin
    tryCatch(caesarCipher("codigo, rocks!", 5) == "htinlt, wthpx!")
```

An empty message stays empty

```kotlin
    tryCatch(caesarCipher("", 4) == "")
```

Spaces between single letters are preserved

```kotlin
    tryCatch(caesarCipher("a b c", 1) == "b c d")
```

Digits are not shifted, even with a shift of 25

```kotlin
    tryCatch(caesarCipher("abc 123!", 25) == "zab 123!")
```

A shift of 13 encodes a whole sentence

```kotlin
    tryCatch(caesarCipher("the quick brown fox jumps over the lazy dog", 13) == "gur dhvpx oebja sbk whzcf bire gur ynml qbt")
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
fun caesarCipher(text: String, shift: Int): String {
    val result = StringBuilder()

    for (char in text) {
        if (char in 'a'..'z') {
            result.append('a' + (char - 'a' + shift) % 26)
        } else {
            result.append(char)
        }
    }

    return result.toString()
}
```
