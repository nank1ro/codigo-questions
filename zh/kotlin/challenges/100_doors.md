---
language: kotlin
exerciseType: 1
difficulty: 1
title: 100扇门
---

# --description--

有100扇门排成一排，最初都是关闭的。
你要经过这些门100次。
第一次经过时，访问每扇门并"切换"门的状态（如果门是关闭的，就打开它；如果是打开的，就关闭它）。
第二次，只访问每第2扇门（即第2、4、6号门...）并切换状态。
第三次，访问每第3扇门（即第3、6、9号门...），以此类推，直到你只访问第100扇门。

# --instructions--

实现一个函数来确定最后一次经过后门的状态。
将最终结果以数组形式返回，数组中只包含打开的门的编号。
> 该方法必须能够处理可变数量的门。

# --seed--

```kotlin
fun getFinalOpenedDoors(numDoors: Int): ArrayList<Int> {
    
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

给定100扇门，返回正确的开门列表

```kotlin
    val solution1 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
    tryCatch(getFinalOpenedDoors(100) == solution1)
```

给定10扇门，返回正确的开门列表

```kotlin
    val solution2 = listOf(1, 4, 9)
    tryCatch(getFinalOpenedDoors(10) == solution2)
```

给定950扇门，返回正确的开门列表

```kotlin
    val solution3 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900)
    tryCatch(getFinalOpenedDoors(950) == solution3)
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
fun square(num: Int): Int {
    return Math.pow(num.toDouble(), 2.0).toInt()
}

fun getFinalOpenedDoors(numDoors: Int): ArrayList<Int> {
    val openDoors = ArrayList<Int>()
    var i = 1
    while (square(i) <= numDoors) {
        openDoors.add(square(i))
        i += 1
    }
    return openDoors
}
```
