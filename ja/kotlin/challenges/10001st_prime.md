---
language: kotlin
exerciseType: 1
difficulty: 2
title: 10001番目の素数
---

# --description--

最初の6つの素数を列挙すると：2、3、5、7、11、13となり、6番目の素数が13であることがわかります。

# --instructions--

n番目の素数を返す関数を書いてください。

関数呼び出しの例：
```kotlin
println(nthPrime(6))
// 13 を出力
```

# --seed--

```kotlin
fun nthPrime(n: Int): Int {

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

6番目の素数は13でなければならない

```kotlin
    tryCatch(nthPrime(6) == 13)
```

10番目の素数は29でなければならない

```kotlin
    tryCatch(nthPrime(10) == 29)
```

1000番目の素数は7919でなければならない

```kotlin
    tryCatch(nthPrime(1000) == 7919)
```

10001番目の素数は104743でなければならない

```kotlin
    tryCatch(nthPrime(10001) == 104743)
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
fun nthPrime(n: Int): Int {
    var count = 0
    var num = 1
    while (count < n) {
        num++
        if (isPrime(num)) count++
    }
    return num
}

fun isPrime(n: Int): Boolean {
    if (n < 2) return false
    for (i in 2..Math.sqrt(n.toDouble()).toInt()) {
        if (n % i == 0) return false
    }
    return true
}
```
