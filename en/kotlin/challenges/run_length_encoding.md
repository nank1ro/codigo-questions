---
language: kotlin
exerciseType: 1
difficulty: 2
title: Run-length encoding
---

# --description--

Run-length encoding is one of the oldest compression tricks there is: instead of writing the same character over and over, you write how many times it repeats and then the character itself.

A fax machine scanning a mostly blank page meets long stretches of identical pixels, so a row of twelve `W` travels down the line as the much shorter `12W`. When a character shows up only once there is nothing to gain from counting it, so it is copied across on its own.

# --instructions--

Write a function `encodeRun` that takes a string `text` and returns its run-length encoded form.

Every run of the same character repeated two or more times becomes the length of the run written in decimal, followed by that character. A run of length one is copied as the single character, with no number in front of it.

Examples:
```
encodeRun("") ➞ ""
encodeRun("AB") ➞ "AB"
encodeRun("AABCCCDEEEE") ➞ "2AB3CD4E"
encodeRun("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encodeRun("  HI  ") ➞ "2 HI2 "
```

- The text contains only uppercase letters from `A` to `Z` and spaces.
- A run longer than nine characters uses its full decimal count, so twelve `W` become `12W` and never `9W3W`.
- Spaces are ordinary characters: they are counted and encoded exactly like letters.
- The empty string encodes to the empty string.

# --seed--

```kotlin
fun encodeRun(text: String): String {
    
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

The empty string encodes to the empty string

```kotlin
    tryCatch(encodeRun("") == "")
```

A single character is copied as itself

```kotlin
    tryCatch(encodeRun("A") == "A")
```

A string with no repeats travels through unchanged

```kotlin
    tryCatch(encodeRun("ABCDE") == "ABCDE")
```

A run of two becomes the count followed by the character

```kotlin
    tryCatch(encodeRun("AA") == "2A")
```

The mixed example "AABCCCDEEEE" becomes "2AB3CD4E"

```kotlin
    tryCatch(encodeRun("AABCCCDEEEE") == "2AB3CD4E")
```

A run of twelve uses its full decimal count, so the result starts with "12W"

```kotlin
    tryCatch(encodeRun("WWWWWWWWWWWWBWW") == "12WB2W")
```

Runs of spaces are encoded just like runs of letters

```kotlin
    tryCatch(encodeRun("  HI  ") == "2 HI2 ")
```

A run of ten is written as "10A", never as two shorter runs

```kotlin
    tryCatch(encodeRun("AAAAAAAAAA") == "10A")
```

Single characters that alternate are all copied as themselves

```kotlin
    tryCatch(encodeRun("ABABAB") == "ABABAB")
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
fun encodeRun(text: String): String {
    val result = StringBuilder()
    var i = 0

    while (i < text.length) {
        var run = 1
        while (i + run < text.length && text[i + run] == text[i]) {
            run++
        }
        if (run > 1) {
            result.append(run)
        }
        result.append(text[i])
        i += run
    }

    return result.toString()
}
```
