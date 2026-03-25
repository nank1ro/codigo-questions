---
language: kotlin
exerciseType: 1
difficulty: 2
title: 素数の総和
---

# --description--

10未満の素数の和は 2 + 3 + 5 + 7 = 17 です。200万未満のすべての素数の和を求めてください。

# --instructions--

n未満のすべての素数の和を返す関数を書いてください。

関数呼び出しの例：
```kotlin
println(primeSummation(10))
// 17 を出力
```

# --seed--

```kotlin
fun primeSummation(n: Int): Long {

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

10未満の素数の和は17でなければならない

```kotlin
    tryCatch(primeSummation(10) == 17L)
```

1000未満の素数の和は76127でなければならない

```kotlin
    tryCatch(primeSummation(1000) == 76127L)
```

100000未満の素数の和は454396537でなければならない

```kotlin
    tryCatch(primeSummation(100000) == 454396537L)
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
fun primeSummation(n: Int): Long {
    val sieve = BooleanArray(n) { true }
    sieve[0] = false
    if (n > 1) sieve[1] = false
    var i = 2
    while (i * i < n) {
        if (sieve[i]) {
            var j = i * i
            while (j < n) {
                sieve[j] = false
                j += i
            }
        }
        i++
    }
    return sieve.indices.filter { sieve[it] }.sumOf { it.toLong() }
}
```
