---
language: kotlin
exerciseType: 1
difficulty: 1
title: 100개의 문
---

# --description--

일렬로 늘어선 100개의 문이 있으며, 모두 처음에는 닫혀 있습니다.
100번의 순회를 합니다.
첫 번째 순회에서는 모든 문을 방문하여 문을 '토글'합니다 (문이 닫혀 있으면 열고, 열려 있으면 닫습니다).
두 번째 순회에서는 2번째 문만 방문하여 (즉, 문 #2, #4, #6, ...) 토글합니다.
세 번째 순회에서는 3번째 문마다 방문하여 (즉, 문 #3, #6, #9, ...) 토글하며, 100번째 문만 방문할 때까지 이를 반복합니다.

# --instructions--

마지막 순회 후 문의 상태를 결정하는 함수를 구현하세요.
최종 결과를 배열로 반환하되, 열려 있는 문의 번호만 배열에 포함시키세요.
> 이 메서드는 가변적인 수의 문에서도 작동할 수 있어야 합니다.

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

100개의 문이 주어졌을 때, 열린 문의 올바른 목록을 반환합니다

```kotlin
    val solution1 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
    tryCatch(getFinalOpenedDoors(100) == solution1)
```

10개의 문이 주어졌을 때, 열린 문의 올바른 목록을 반환합니다

```kotlin
    val solution2 = listOf(1, 4, 9)
    tryCatch(getFinalOpenedDoors(10) == solution2)
```

950개의 문이 주어졌을 때, 열린 문의 올바른 목록을 반환합니다

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
