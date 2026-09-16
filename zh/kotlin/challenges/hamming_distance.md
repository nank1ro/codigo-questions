---
language: kotlin
exerciseType: 1
difficulty: 1
title: 汉明距离
---

# --description--

DNA 写成一条由核苷酸组成的链，每个核苷酸是单个字母：`A`、`C`、`G` 或 `T`。当两条等长的链并排排列时，有些位置上的核苷酸相同，有些位置上的核苷酸则不同。

两条链上不同位置的数目称为汉明距离，生物学家用它来衡量两条链已经分化得有多远。将 `GAGCCTACTAACGGGAT` 与 `CATCGTAATGACGGCCT` 并排对齐后有 7 个位置不同，因此它们的汉明距离是 7。

# --instructions--

编写一个函数 `hammingDistance`，它接收两条等长的 DNA 链，并返回它们不同位置的数目。

示例：
```
hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") ➞ 7
hammingDistance("A", "A") ➞ 0
hammingDistance("AG", "CT") ➞ 2
hammingDistance("", "") ➞ 0
```

- 两条链的长度总是相同的，所以你无需处理长度不同的链。
- 两条空链没有任何不同，所以它们的距离是 0。

# --seed--

```kotlin
fun hammingDistance(left: String, right: String): Int {
    
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

两条空链没有任何不同

```kotlin
    tryCatch(hammingDistance("", "") == 0)
```

两条相同的单核苷酸链没有差异

```kotlin
    tryCatch(hammingDistance("A", "A") == 0)
```

两条不同的单核苷酸链在一个位置上不同

```kotlin
    tryCatch(hammingDistance("A", "G") == 1)
```

两条在每个位置都不同的短链

```kotlin
    tryCatch(hammingDistance("AG", "CT") == 2)
```

两条只在第一个位置不同的短链

```kotlin
    tryCatch(hammingDistance("AT", "CT") == 1)
```

链的中间有一个不同的核苷酸

```kotlin
    tryCatch(hammingDistance("GGACG", "GGTCG") == 1)
```

相同核苷酸出现在不同位置也算作差异

```kotlin
    tryCatch(hammingDistance("TAG", "GAT") == 2)
```

一对有四个差异的较长的链

```kotlin
    tryCatch(hammingDistance("GATACA", "GCATAA") == 4)
```

将一条链移动一个位置会使几乎所有位置都不同

```kotlin
    tryCatch(hammingDistance("GGACGGATTCTG", "AGGACGGATTCT") == 9)
```

描述中的两条链的距离为 7

```kotlin
    tryCatch(hammingDistance("GAGCCTACTAACGGGAT", "CATCGTAATGACGGCCT") == 7)
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
fun hammingDistance(left: String, right: String): Int {
    var distance = 0

    for (i in left.indices) {
        if (left[i] != right[i]) {
            distance++
        }
    }

    return distance
}
```
