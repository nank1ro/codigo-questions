---
language: kotlin
exerciseType: 1
difficulty: 2
title: 数列の中の最大積
---

# --description--

1000桁の数の中で、積が最も大きい4つの連続した数字は 9 × 9 × 8 × 9 = 5832 です。

# --instructions--

1000桁の数の中でn個の連続した数字の最大積を求める関数を書いてください。

関数呼び出しの例：
```kotlin
println(largestProductInASeries(4))
// 5832 を出力
```

# --seed--

```kotlin
fun largestProductInASeries(n: Int): Long {

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

4つの連続した数字の最大積は5832でなければならない

```kotlin
    tryCatch(largestProductInASeries(4) == 5832L)
```

13個の連続した数字の最大積は23514624000でなければならない

```kotlin
    tryCatch(largestProductInASeries(13) == 23514624000L)
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
fun largestProductInASeries(n: Int): Long {
    val number = "73167176531330624919225119674426574742355349194934" +
        "96983520312774506326239578318016984801869478851843" +
        "85861560789112949495459501737958331952853208805511" +
        "12540698747158523863050715693290963295227443043557" +
        "66896648950445244523161731856403098711121722383113" +
        "62229893423380308135336276614282806444486645238749" +
        "30358907296290491560440772390713810515859307960866" +
        "70172427121883998797908792274921901699720888093776" +
        "65727333001053367881220235421809751254540594752243" +
        "52584907711670556013604839586446706324415722155397" +
        "53697817977846174064955149290862569321978468622482" +
        "83972241375657056057490261407972968652414535100474" +
        "82166370484403199890008895243450658541227588666881" +
        "16427171479924442928230863465674813919123162824586" +
        "17866458359124566529476545682848912883142607690042" +
        "24219022671055626321111109370544217506941658960408" +
        "07198403850962455444362981230987879927244284909188" +
        "84580156166097919133875499200524063689912560717606" +
        "05886116467109405077541002256983155200055935729725" +
        "71636269561882670428252483600823257530420752963450"
    var largest = 0L
    for (i in 0..number.length - n) {
        var product = 1L
        for (j in i until i + n) {
            product *= number[j].digitToInt()
        }
        if (product > largest) largest = product
    }
    return largest
}
```
