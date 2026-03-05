---
language: kotlin
exerciseType: 1
difficulty: 1
title: 100のドア
---

# --description--

一列に並んだ100枚のドアがあり、最初はすべて閉じています。
あなたはドアの前を100回通ります。
1回目は、すべてのドアを訪れて「切り替え」ます（ドアが閉じていれば開け、開いていれば閉じます）。
2回目は、2番目ごとのドア（つまり、#2、#4、#6、...）だけを訪れて切り替えます。
3回目は、3番目ごとのドア（つまり、#3、#6、#9、...）を訪れます。これを100番目のドアだけを訪れるまで続けます。

# --instructions--

最後の通過後のドアの状態を決定する関数を実装してください。
最終結果を配列で返し、開いているドアの番号のみを配列に含めてください。
> このメソッドは可変数のドアで動作できなければなりません。

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

100枚のドアが与えられた場合、開いているドアの正しいリストを返す

```kotlin
    val solution1 = listOf(1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
    tryCatch(getFinalOpenedDoors(100) == solution1)
```

10枚のドアが与えられた場合、開いているドアの正しいリストを返す

```kotlin
    val solution2 = listOf(1, 4, 9)
    tryCatch(getFinalOpenedDoors(10) == solution2)
```

950枚のドアが与えられた場合、開いているドアの正しいリストを返す

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
