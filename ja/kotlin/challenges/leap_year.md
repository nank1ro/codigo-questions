---
language: kotlin
exerciseType: 1
difficulty: 3
title: うるう年
---

# --description--

暦年にはちょうど365.25日あります。しかし、最終的にこれは混乱を招きます。なぜなら、人間は通常、小数点ではなく1の正確な割り切りで数えるからです。そこで、後者を避けるために、4年周期ごとに0.25日をすべて足し合わせて、その年を366日（2月29日を閏日として含む）とし、__うるう年__と呼ぶことが決められました。4年周期の他の3年は365日のみを含み、__うるう年ではありません__。

# --instructions--

このチャレンジでは、`Date`クラス、`switch`文、__ifブロック__、__if-elseブロック__、__三項演算子__（`x ? a : b`）、および論理演算子__AND__（`&&`）と__OR__（`||`）を使用せずに、うるう年かどうかを判定します。ただし、__NOT__（`!`）演算子は例外として使用できます。

うるう年の場合は`true`を、そうでない場合は`false`を返してください。

関数呼び出しの例：
```kotlin
println(leapYear(2000))
// prints true
```

# --seed--

```kotlin
fun leapYear(year: Int): Boolean {
    
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

`Date`、`switch`、`if`、`else`、`&&`、`||`、`?`の使用は許可されていません。

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

`2016`年はうるう年です。

```kotlin
    tryCatch(leapYear(2016) == true)
```

`1996`年はうるう年です。

```kotlin
    tryCatch(leapYear(1996) == true)
```

`1600`年はうるう年です。

```kotlin
    tryCatch(leapYear(1600) == true)
```

`2020`年はうるう年です。

```kotlin
    tryCatch(leapYear(2020) == true)
```

`2000`年はうるう年です。

```kotlin
    tryCatch(leapYear(2000) == true)
```

`2008`年はうるう年です。

```kotlin
    tryCatch(leapYear(2008) == true)
```

`1521`年はうるう年ではありません。

```kotlin
    tryCatch(leapYear(1521) == false)
```

`1800`年はうるう年ではありません。

```kotlin
    tryCatch(leapYear(1800) == false)
```

`2007`年はうるう年ではありません。

```kotlin
    tryCatch(leapYear(2007) == false)
```

`2002`年はうるう年ではありません。

```kotlin
    tryCatch(leapYear(2002) == false)
```

`1979`年はうるう年ではありません。

```kotlin
    tryCatch(leapYear(1979) == false)
```

`2006`年はうるう年ではありません。

```kotlin
    tryCatch(leapYear(2006) == false)
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
fun leapYear(year: Int): Boolean {
  var tempYear = year
  while (tempYear % 100 == 0) {
    tempYear = tempYear / 100
  }
  return tempYear % 4 == 0
}
```
