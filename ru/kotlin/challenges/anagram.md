---
language: kotlin
exerciseType: 1
difficulty: 2
title: Анаграмма
---

# --description--

Два слова являются анаграммами, когда одно из них является перестановкой другого: они используют ровно одни и те же буквы, и каждая буква встречается одно и то же число раз, просто в другом порядке. `listen` и `silent` — анаграммы, как и `stone` и `tones`.

Слово никогда не является анаграммой самого себя. Если два слова полностью совпадают, ничего не переставлялось, поэтому ответ — `false`. Оба слова заданы в нижнем регистре и содержат только буквы от `a` до `z`.

# --instructions--

Напишите функцию `isAnagram`, которая принимает два слова, `first` и `second`, и возвращает `true`, если они являются анаграммами друг друга, и `false` в противном случае.

Примеры:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- Два одинаковых слова не являются анаграммами.
- Слова разной длины никогда не являются анаграммами.
- Каждая буква должна встречаться в обоих словах одинаковое число раз.

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

Слова "listen" и "silent" являются анаграммами

```kotlin
    tryCatch(isAnagram("listen", "silent") == true)
```

Слова "stone" и "tones" являются анаграммами

```kotlin
    tryCatch(isAnagram("stone", "tones") == true)
```

Слово не является анаграммой самого себя

```kotlin
    tryCatch(isAnagram("stone", "stone") == false)
```

Слова разной длины не являются анаграммами

```kotlin
    tryCatch(isAnagram("abc", "abcd") == false)
```

Одни и те же буквы в разном количестве не являются анаграммой

```kotlin
    tryCatch(isAnagram("aab", "abb") == false)
```

Слова "anagram" и "nagaram" являются анаграммами

```kotlin
    tryCatch(isAnagram("anagram", "nagaram") == true)
```

Два слова одинаковой длины с разными буквами не являются анаграммами

```kotlin
    tryCatch(isAnagram("rat", "car") == false)
```

Два пустых слова идентичны, поэтому они не являются анаграммами

```kotlin
    tryCatch(isAnagram("", "") == false)
```

Две разные одиночные буквы не являются анаграммами

```kotlin
    tryCatch(isAnagram("a", "b") == false)
```

Слова "evil" и "vile" являются анаграммами

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
