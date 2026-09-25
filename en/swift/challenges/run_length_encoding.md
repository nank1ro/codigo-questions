---
language: swift
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
func encodeRun(_ text: String) -> String {
    
}
```

# --asserts--

The empty string encodes to the empty string

```swift
tryCatch(encodeRun("") == "")
```

A single character is copied as itself

```swift
tryCatch(encodeRun("A") == "A")
```

A string with no repeats travels through unchanged

```swift
tryCatch(encodeRun("ABCDE") == "ABCDE")
```

A run of two becomes the count followed by the character

```swift
tryCatch(encodeRun("AA") == "2A")
```

The mixed example "AABCCCDEEEE" becomes "2AB3CD4E"

```swift
tryCatch(encodeRun("AABCCCDEEEE") == "2AB3CD4E")
```

A run of twelve uses its full decimal count, so the result starts with "12W"

```swift
tryCatch(encodeRun("WWWWWWWWWWWWBWW") == "12WB2W")
```

Runs of spaces are encoded just like runs of letters

```swift
tryCatch(encodeRun("  HI  ") == "2 HI2 ")
```

A run of ten is written as "10A", never as two shorter runs

```swift
tryCatch(encodeRun("AAAAAAAAAA") == "10A")
```

Single characters that alternate are all copied as themselves

```swift
tryCatch(encodeRun("ABABAB") == "ABABAB")
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func encodeRun(_ text: String) -> String {
    let characters = Array(text)
    var result = ""
    var i = 0

    while i < characters.count {
        var run = 1
        while i + run < characters.count && characters[i + run] == characters[i] {
            run += 1
        }
        if run > 1 {
            result += String(run)
        }
        result.append(characters[i])
        i += run
    }

    return result
}
```
