---
language: swift
exerciseType: 1
difficulty: 3
title: Matching brackets
---

# --description--

Text that carries code, maths or markup is full of brackets, and every opening bracket needs a closing one of the same kind. A string is balanced when its brackets pair up and nest like the layers of an onion: `{[()]}` is balanced, while `{[(])}` is not, because the round pair is closed before the square pair it sits inside.

Three pairs count here: round `()`, square `[]` and curly `{}`. Every other character in the string is ignored. A closing bracket must close the most recently opened bracket that is still open, and when the string ends no bracket may be left open.

# --instructions--

Write a function `isBalanced` that takes a string and returns `true` when all the brackets in it are matched and properly nested, and `false` otherwise.

Examples:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- An empty string is balanced.
- Characters that are not brackets are ignored.
- A closing bracket must match the most recently opened bracket that is still open.
- No bracket may be left open when the string ends.

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
func isBalanced(_ text: String) -> Bool {
    
}
```

# --asserts--

An empty string is balanced

```swift
tryCatch(isBalanced("") == true)
```

A single pair of round brackets is balanced

```swift
tryCatch(isBalanced("()") == true)
```

The three kinds of pair nested inside each other are balanced

```swift
tryCatch(isBalanced("{[()]}") == true)
```

Brackets mixed with other text are still balanced

```swift
tryCatch(isBalanced("{what is (42)}[?]") == true)
```

Pairs placed side by side are balanced

```swift
tryCatch(isBalanced("()[]{}") == true)
```

A string without any brackets is balanced

```swift
tryCatch(isBalanced("no brackets in here at all") == true)
```

A crossed pair is not balanced

```swift
tryCatch(isBalanced("{[(])}") == false)
```

An opening bracket that is never closed is not balanced

```swift
tryCatch(isBalanced("(") == false)
```

A closing bracket before any opening one is not balanced

```swift
tryCatch(isBalanced(")(") == false)
```

Crossed pairs deeper in the string are not balanced

```swift
tryCatch(isBalanced("(([]{[}]))") == false)
```

A closing bracket left over at the end is not balanced

```swift
tryCatch(isBalanced("())") == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isBalanced(_ text: String) -> Bool {
    let pairs: [Character: Character] = [")": "(", "]": "[", "}": "{"]
    var stack: [Character] = []

    for char in text {
        if char == "(" || char == "[" || char == "{" {
            stack.append(char)
        } else if let opening = pairs[char] {
            if stack.popLast() != opening {
                return false
            }
        }
    }

    return stack.isEmpty
}
```
