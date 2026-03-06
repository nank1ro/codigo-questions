---
language: kotlin
exerciseType: 1
difficulty: 1
title: アッカーマン関数
---

# --description--

アッカーマン関数は再帰関数の古典的な例であり、特に原始再帰関数ではないことで知られています。その値は非常に急速に増大し、呼び出しツリーのサイズも同様です。

アッカーマン関数は通常、次のように定義されます：

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

その引数は決して負にならず、常に終了します

# --instructions--

アッカーマン関数の値を返す関数を書いてください。

# --seed--

```kotlin
fun ack(m: Int, n: Int): Int {
    
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

`ack(0, 0)`は1を返すべきです。

```kotlin
    tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)`は3を返すべきです。

```kotlin
    tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)`は13を返すべきです。

```kotlin
    tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)`は61を返すべきです。

```kotlin
    tryCatch(ack(3, 3) == 61)
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
fun ack(m: Int, n: Int): Int {
    return if (m == 0)
            n + 1
        else (ack(m - 1, 
            if (n == 0)
                1
            else
                ack(m, n - 1)
            )
        ) 
}
```
