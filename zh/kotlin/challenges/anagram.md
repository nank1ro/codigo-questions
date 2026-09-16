---
language: kotlin
exerciseType: 1
difficulty: 2
title: 变位词
---

# --description--

如果一个单词是另一个单词的重新排列，那么这两个单词就互为变位词：它们使用的字母完全相同，每个字母出现的次数也相同，只是顺序不同。`listen` 和 `silent` 是变位词，`stone` 和 `tones` 也是变位词。

一个单词永远不会是它自身的变位词。如果两个单词完全相同，就没有任何东西被重新排列，所以答案是 `false`。两个单词都以小写形式给出，并且只包含从 `a` 到 `z` 的字母。

# --instructions--

编写一个函数 `isAnagram`，它接收两个单词 `first` 和 `second`，当它们互为变位词时返回 `true`，否则返回 `false`。

示例：
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- 两个完全相同的单词不是变位词。
- 长度不同的单词永远不会是变位词。
- 每个字母在两个单词中出现的次数必须相同。

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

单词 "listen" 和 "silent" 互为变位词

```kotlin
    tryCatch(isAnagram("listen", "silent") == true)
```

单词 "stone" 和 "tones" 互为变位词

```kotlin
    tryCatch(isAnagram("stone", "tones") == true)
```

一个单词不是它自身的变位词

```kotlin
    tryCatch(isAnagram("stone", "stone") == false)
```

长度不同的单词不是变位词

```kotlin
    tryCatch(isAnagram("abc", "abcd") == false)
```

字母相同但出现次数不同则不是变位词

```kotlin
    tryCatch(isAnagram("aab", "abb") == false)
```

单词 "anagram" 和 "nagaram" 互为变位词

```kotlin
    tryCatch(isAnagram("anagram", "nagaram") == true)
```

长度相同但字母不同的两个单词不是变位词

```kotlin
    tryCatch(isAnagram("rat", "car") == false)
```

两个空单词是完全相同的，所以它们不是变位词

```kotlin
    tryCatch(isAnagram("", "") == false)
```

两个不同的单个字母不是变位词

```kotlin
    tryCatch(isAnagram("a", "b") == false)
```

单词 "evil" 和 "vile" 互为变位词

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
