---
language: kotlin
exerciseType: 1
difficulty: 1
title: 足し算
---

# --description--

2つの整数`num1`と`num2`が与えられた場合、これら2つの数を足すプログラムを書いてください

# --instructions--

2つの数の合計を返す関数を書いてください。

関数呼び出しの例：
```kotlin
println(addition(1, 2))
// prints 3
```

# --seed--

```kotlin
fun addition() {
    
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

1と3の合計は4に等しくなければなりません

```kotlin
    tryCatch(addition(1, 3) == 4)
```

200と210の合計は410に等しくなければなりません

```kotlin
    tryCatch(addition(200, 210) == 410)
```

15と35の合計は50に等しくなければなりません

```kotlin
    tryCatch(addition(15, 35) == 50)
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
fun addition(num1: Int, num2: Int): Int {
    return num1 + num2
}
```
