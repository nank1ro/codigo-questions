---
language: kotlin
exerciseType: 1
difficulty: 1
title: 雨粒
---

# --description--

あなたの課題は、数値を特定の因数に対応する雨粒の音を含む文字列に変換することです。
因数とは、別の数を割り切れる数のことで、余りが残りません。
ある数が別の数の因数であるかどうかをテストする最も簡単な方法は、剰余演算を使用することです。
雨粒のルールは、与えられた数が：

- 3を因数に持つ場合、結果に'Pling'を追加する。
- 5を因数に持つ場合、結果に'Plang'を追加する。
- 7を因数に持つ場合、結果に'Plong'を追加する。
- 3、5、7のいずれも因数に持たない場合、結果はその数の数字そのものになる。

# --instructions--

正しい文字列を返す関数を書いてください。例：

- 28は7を因数に持ちますが、3や5は持たないので、結果は`"Plong"`になります。
- 30は3と5の両方を因数に持ちますが、7は持たないので、結果は`"PlingPlang"`になります。
- 34は3、5、7のいずれの因数も持たないので、結果は`"34"`になります。

関数呼び出しの例：
```kotlin
println(raindrops(28))
// prints "Plong"
```

# --seed--

```kotlin
fun raindrops(): String {
    
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

1の音は"1"

```kotlin
    tryCatch(raindrops(1) == "1")
```

3の音は"Pling"

```kotlin
    tryCatch(raindrops(3) == "Pling")
```

5の音は"Plang"

```kotlin
    tryCatch(raindrops(5) == "Plang")
```

7の音は"Plong"

```kotlin
    tryCatch(raindrops(7) == "Plong")
```

6の音は"Pling"

```kotlin
    tryCatch(raindrops(6) == "Pling")
```

8の音は"8"

```kotlin
    tryCatch(raindrops(8) == "8")
```

9の音は"Pling"

```kotlin
    tryCatch(raindrops(9) == "Pling")
```

10の音は"Plang"

```kotlin
    tryCatch(raindrops(10) == "Plang")
```

14の音は"Plong"

```kotlin
    tryCatch(raindrops(14) == "Plong")
```

15の音は"PlingPlang"

```kotlin
    tryCatch(raindrops(15) == "PlingPlang")
```

21の音は"PlingPlong"

```kotlin
    tryCatch(raindrops(21) == "PlingPlong")
```

25の音は"Plang"

```kotlin
    tryCatch(raindrops(25) == "Plang")
```

27の音は"Pling"

```kotlin
    tryCatch(raindrops(27) == "Pling")
```

35の音は"PlangPlong"

```kotlin
    tryCatch(raindrops(35) == "PlangPlong")
```

49の音は"Plong"

```kotlin
    tryCatch(raindrops(49) == "Plong")
```

52の音は"52"

```kotlin
    tryCatch(raindrops(52) == "52")
```

105の音は"PlingPlangPlong"

```kotlin
    tryCatch(raindrops(105) == "PlingPlangPlong")
```

3125の音は"Plang"

```kotlin
    tryCatch(raindrops(3125) == "Plang")
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
fun raindrops(num: Int): String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty()) {
        result = num.toString()     
    }
    return result
}
```
