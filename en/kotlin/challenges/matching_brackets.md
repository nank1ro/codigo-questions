---
language: kotlin
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

# --seed--

```kotlin
fun isBalanced(text: String): Boolean {
    
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

An empty string is balanced

```kotlin
    tryCatch(isBalanced("") == true)
```

A single pair of round brackets is balanced

```kotlin
    tryCatch(isBalanced("()") == true)
```

The three kinds of pair nested inside each other are balanced

```kotlin
    tryCatch(isBalanced("{[()]}") == true)
```

Brackets mixed with other text are still balanced

```kotlin
    tryCatch(isBalanced("{what is (42)}[?]") == true)
```

Pairs placed side by side are balanced

```kotlin
    tryCatch(isBalanced("()[]{}") == true)
```

A string without any brackets is balanced

```kotlin
    tryCatch(isBalanced("no brackets in here at all") == true)
```

A crossed pair is not balanced

```kotlin
    tryCatch(isBalanced("{[(])}") == false)
```

An opening bracket that is never closed is not balanced

```kotlin
    tryCatch(isBalanced("(") == false)
```

A closing bracket before any opening one is not balanced

```kotlin
    tryCatch(isBalanced(")(") == false)
```

Crossed pairs deeper in the string are not balanced

```kotlin
    tryCatch(isBalanced("(([]{[}]))") == false)
```

A closing bracket left over at the end is not balanced

```kotlin
    tryCatch(isBalanced("())") == false)
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
fun isBalanced(text: String): Boolean {
    val pairs = mapOf(')' to '(', ']' to '[', '}' to '{')
    val stack = ArrayDeque<Char>()

    for (char in text) {
        if (char == '(' || char == '[' || char == '{') {
            stack.addLast(char)
        } else if (pairs.containsKey(char)) {
            if (stack.isEmpty() || stack.removeLast() != pairs[char]) {
                return false
            }
        }
    }

    return stack.isEmpty()
}
```
