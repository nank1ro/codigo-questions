---
language: swift
exerciseType: 1
difficulty: 1
title: Pangram
---

# --description--

A pangram is a sentence that uses every letter of the English alphabet at least once. The best known example is "the quick brown fox jumps over the lazy dog", which fits all 26 letters into nine short words.

The check is case-insensitive, so `A` and `a` count as the same letter. Digits, punctuation and spaces are ignored: they are not letters, but they are not a reason to reject a sentence either.

# --instructions--

Write a function `isPangram` that takes a sentence and returns `true` if the sentence is a pangram and `false` otherwise.

Examples:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- An empty sentence is not a pangram.
- Only the 26 letters from `a` to `z` count.

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
func isPangram(_ sentence: String) -> Bool {
    
}
```

# --asserts--

An empty sentence is not a pangram

```swift
tryCatch(isPangram("") == false)
```

The classic sentence "the quick brown fox jumps over the lazy dog" is a pangram

```swift
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") == true)
```

A sentence missing the letter `x` is not a pangram

```swift
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") == false)
```

The sentence "the five boxing wizards jump quickly" is a pangram

```swift
tryCatch(isPangram("the five boxing wizards jump quickly") == true)
```

Underscores are ignored, so the sentence is still a pangram

```swift
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") == true)
```

Digits are ignored, so the sentence is still a pangram

```swift
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") == true)
```

Digits do not replace the letters `e`, `i` and `t`

```swift
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") == false)
```

An uppercase sentence is a pangram too

```swift
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") == true)
```

Mixing the cases of the same half of the alphabet is not enough

```swift
tryCatch(isPangram("abcdefghijklm ABCDEFGHIJKLM") == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isPangram(_ sentence: String) -> Bool {
    var letters = Set<Character>()

    for char in sentence.lowercased() {
        if char.isASCII && char.isLetter {
            letters.insert(char)
        }
    }

    return letters.count == 26
}
```
