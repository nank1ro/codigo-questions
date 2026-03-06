---
language: kotlin
exerciseType: 1
difficulty: 1
title: 2対1
---

# --description--

名前が与えられた場合、次のメッセージを含む文字列を返します：
`One for X, one for me.`
ここで`X`は与えられた名前です。
ただし、名前がない場合は、次の文字列を返します：
`One for you, one for me.`

# --instructions--

正しい文字列を返す関数を書いてください。例：

**入力**: `Walter`
**出力**: `One for Walter, one for me.`

**入力**: `James`
**出力**: `One for James, one for me.`

**入力**: `Martha`
**出力**: `One for Martha, one for me.`

# --seed--

```kotlin
fun twoForOne(): String {
    
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

名前なし

```kotlin
    tryCatch(twoForOne() == "One for you, one for me.")
```

名前に"James"を渡す

```kotlin
    tryCatch(twoForOne(name = "James") == "One for James, one for me.")
```

名前に"Martha"を渡す

```kotlin
    tryCatch(twoForOne(name = "Martha") == "One for Martha, one for me.")
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
fun twoForOne(name: String? = null): String {
    name?.let {
        return "One for $it, one for me."
    }
    return "One for you, one for me."
}
```


