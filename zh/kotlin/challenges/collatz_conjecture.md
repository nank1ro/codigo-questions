---
language: kotlin
exerciseType: 1
difficulty: 1
title: 考拉兹猜想
---

# --description--

考拉兹猜想从任意正整数 `n` 出发，重复一条简单的规则：如果 `n` 是偶数，就把它减半；如果 `n` 是奇数，就把它替换为 `3n + 1`。这个序列迟早会到达 1。

例如，从 16 开始，序列是 `16 -> 8 -> 4 -> 2 -> 1`，因此需要 4 步。

从来没有人证明过这一规律总是成立，但对于每一个被测试过的数它都成立。

# --instructions--

编写一个函数 `collatzSteps`，它接收一个正整数 `n`，并返回到达 1 所需的步数。

`collatzSteps(1)` 为 0，因为 1 已经是序列的终点。`collatzSteps(12)` 为 9，而 `collatzSteps(27)` 为 111。

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
```

# --seed--

```kotlin
fun collatzSteps(n: Int): Int {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`collatzSteps(1)` 应返回 0，因为 1 已经是序列的终点。

```kotlin
    tryCatch(collatzSteps(1) == 0)
```

`collatzSteps(2)` 应返回 1。

```kotlin
    tryCatch(collatzSteps(2) == 1)
```

`collatzSteps(6)` 应返回 8。

```kotlin
    tryCatch(collatzSteps(6) == 8)
```

`collatzSteps(7)` 应返回 16。

```kotlin
    tryCatch(collatzSteps(7) == 16)
```

`collatzSteps(16)` 应返回 4。

```kotlin
    tryCatch(collatzSteps(16) == 4)
```

`collatzSteps(12)` 应返回 9。

```kotlin
    tryCatch(collatzSteps(12) == 9)
```

`collatzSteps(27)` 应返回 111。

```kotlin
    tryCatch(collatzSteps(27) == 111)
```

`collatzSteps(97)` 应返回 118。

```kotlin
    tryCatch(collatzSteps(97) == 118)
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
fun collatzSteps(n: Int): Int {
    var value = n
    var steps = 0
    while (value != 1) {
        value = if (value % 2 == 0) value / 2 else 3 * value + 1
        steps++
    }
    return steps
}
```
