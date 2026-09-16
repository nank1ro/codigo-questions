---
language: kotlin
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

# --seed--

```kotlin
fun isAnagram(first: String, second: String): Boolean {
    
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

The words "listen" and "silent" are anagrams

```kotlin
    tryCatch(isAnagram("listen", "silent") == true)
```

The words "stone" and "tones" are anagrams

```kotlin
    tryCatch(isAnagram("stone", "tones") == true)
```

A word is not an anagram of itself

```kotlin
    tryCatch(isAnagram("stone", "stone") == false)
```

Words of different lengths are not anagrams

```kotlin
    tryCatch(isAnagram("abc", "abcd") == false)
```

The same letters in different amounts are not an anagram

```kotlin
    tryCatch(isAnagram("aab", "abb") == false)
```

The words "anagram" and "nagaram" are anagrams

```kotlin
    tryCatch(isAnagram("anagram", "nagaram") == true)
```

Two words of the same length with different letters are not anagrams

```kotlin
    tryCatch(isAnagram("rat", "car") == false)
```

Two empty words are identical, so they are not anagrams

```kotlin
    tryCatch(isAnagram("", "") == false)
```

Two different single letters are not anagrams

```kotlin
    tryCatch(isAnagram("a", "b") == false)
```

The words "evil" and "vile" are anagrams

```kotlin
    tryCatch(isAnagram("evil", "vile") == true)
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
fun isAnagram(first: String, second: String): Boolean {
    if (first == second) {
        return false
    }

    return first.toList().sorted() == second.toList().sorted()
}
```
