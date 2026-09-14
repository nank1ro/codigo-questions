---
language: kotlin
exerciseType: 1
difficulty: 1
title: コラッツの予想
---

# --description--

コラッツの予想は、任意の正の整数`n`から始めて、1つの単純な規則を繰り返します。`n`が偶数ならそれを半分にし、`n`が奇数なら`3n + 1`で置き換えます。いずれ数列は1に到達します。

例えば、16から始めると数列は`16 -> 8 -> 4 -> 2 -> 1`となり、4ステップかかります。

これが常に起こると証明した人はまだいませんが、これまでテストされたすべての数で成り立っています。

# --instructions--

正の整数`n`を受け取り、1に到達するまでに必要なステップ数を返す関数`collatzSteps`を書いてください。

`collatzSteps(1)`は0になります。1はすでに数列の終わりだからです。`collatzSteps(12)`は9、`collatzSteps(27)`は111です。

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
```

# --seed--

```kotlin
fun collatzSteps(n: Int): Int {

}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`collatzSteps(1)`は、1がすでに数列の終わりであるため、0を返すべきです。

```kotlin
    tryCatch(collatzSteps(1) == 0)
```

`collatzSteps(2)`は1を返すべきです。

```kotlin
    tryCatch(collatzSteps(2) == 1)
```

`collatzSteps(6)`は8を返すべきです。

```kotlin
    tryCatch(collatzSteps(6) == 8)
```

`collatzSteps(7)`は16を返すべきです。

```kotlin
    tryCatch(collatzSteps(7) == 16)
```

`collatzSteps(16)`は4を返すべきです。

```kotlin
    tryCatch(collatzSteps(16) == 4)
```

`collatzSteps(12)`は9を返すべきです。

```kotlin
    tryCatch(collatzSteps(12) == 9)
```

`collatzSteps(27)`は111を返すべきです。

```kotlin
    tryCatch(collatzSteps(27) == 111)
```

`collatzSteps(97)`は118を返すべきです。

```kotlin
    tryCatch(collatzSteps(97) == 118)
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
fun collatzSteps(n: Int): Int {
    var value = n
    var steps = 0
    while (value != 1) {
        value = if (value % 2 == 0) value / 2 else 3 * value + 1
        steps++
    }
    return steps
}
```
