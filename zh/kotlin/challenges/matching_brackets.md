---
language: kotlin
exerciseType: 1
difficulty: 3
title: 括号匹配
---

# --description--

包含代码、数学式或标记的文本中充满了括号，每个开括号都需要一个同类型的闭括号。当字符串中的括号两两配对，并像洋葱的层层外皮一样嵌套时，它就是平衡的：`{[()]}` 是平衡的，而 `{[(])}` 则不是，因为圆括号对在包含它的方括号对之前就闭合了。

这里有三对括号：圆括号 `()`、方括号 `[]` 和花括号 `{}`。字符串中的其他所有字符都会被忽略。闭括号必须闭合最近一个仍处于打开状态的括号，并且在字符串结束时不能有任何括号保持打开。

# --instructions--

编写一个函数 `isBalanced`，它接收一个字符串，当其中的所有括号都配对且正确嵌套时返回 `true`，否则返回 `false`。

示例：
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- 空字符串是平衡的。
- 不是括号的字符会被忽略。
- 闭括号必须与最近一个仍处于打开状态的括号配对。
- 字符串结束时不能有任何括号保持打开。

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

空字符串是平衡的

```kotlin
    tryCatch(isBalanced("") == true)
```

单独的一对圆括号是平衡的

```kotlin
    tryCatch(isBalanced("()") == true)
```

三种括号对彼此嵌套是平衡的

```kotlin
    tryCatch(isBalanced("{[()]}") == true)
```

括号与其他文本混在一起时依然是平衡的

```kotlin
    tryCatch(isBalanced("{what is (42)}[?]") == true)
```

并排摆放的括号对是平衡的

```kotlin
    tryCatch(isBalanced("()[]{}") == true)
```

不含任何括号的字符串是平衡的

```kotlin
    tryCatch(isBalanced("no brackets in here at all") == true)
```

交叉的括号对不是平衡的

```kotlin
    tryCatch(isBalanced("{[(])}") == false)
```

从未被闭合的开括号不是平衡的

```kotlin
    tryCatch(isBalanced("(") == false)
```

出现在任何开括号之前的闭括号不是平衡的

```kotlin
    tryCatch(isBalanced(")(") == false)
```

字符串更深处的交叉括号对不是平衡的

```kotlin
    tryCatch(isBalanced("(([]{[}]))") == false)
```

结尾遗留的闭括号不是平衡的

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
