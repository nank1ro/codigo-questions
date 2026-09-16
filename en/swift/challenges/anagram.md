---
language: swift
exerciseType: 1
difficulty: 2
title: Anagram
---

# --description--

Two words are anagrams when one is a rearrangement of the other: they use exactly the same letters, each letter the same number of times, only in a different order. `listen` and `silent` are anagrams, and so are `stone` and `tones`.

A word is never an anagram of itself. If the two words are exactly the same, nothing was rearranged, so the answer is `false`. Both words are given in lowercase and contain only the letters from `a` to `z`.

# --instructions--

Write a function `isAnagram` that takes two words, `first` and `second`, and returns `true` when they are anagrams of each other and `false` otherwise.

Examples:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Two identical words are not anagrams.
- Words of different lengths are never anagrams.
- Every letter must appear the same number of times in both words.

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
func isAnagram(_ first: String, _ second: String) -> Bool {
    
}
```

# --asserts--

The words "listen" and "silent" are anagrams

```swift
tryCatch(isAnagram("listen", "silent") == true)
```

The words "stone" and "tones" are anagrams

```swift
tryCatch(isAnagram("stone", "tones") == true)
```

A word is not an anagram of itself

```swift
tryCatch(isAnagram("stone", "stone") == false)
```

Words of different lengths are not anagrams

```swift
tryCatch(isAnagram("abc", "abcd") == false)
```

The same letters in different amounts are not an anagram

```swift
tryCatch(isAnagram("aab", "abb") == false)
```

The words "anagram" and "nagaram" are anagrams

```swift
tryCatch(isAnagram("anagram", "nagaram") == true)
```

Two words of the same length with different letters are not anagrams

```swift
tryCatch(isAnagram("rat", "car") == false)
```

Two empty words are identical, so they are not anagrams

```swift
tryCatch(isAnagram("", "") == false)
```

Two different single letters are not anagrams

```swift
tryCatch(isAnagram("a", "b") == false)
```

The words "evil" and "vile" are anagrams

```swift
tryCatch(isAnagram("evil", "vile") == true)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isAnagram(_ first: String, _ second: String) -> Bool {
    if first == second {
        return false
    }

    return first.sorted() == second.sorted()
}
```
