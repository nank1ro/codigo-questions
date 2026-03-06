---
language: kotlin
exerciseType: 1
difficulty: 1
title: अंकों का योग
---

# --description--

आपको एक पूर्णांक `N` दिया गया है।
N के सभी अंकों का योग गणना करने के लिए एक प्रोग्राम लिखें

# --instructions--

`N` के अंकों का योग लौटाएं।

फ़ंक्शन कॉल का उदाहरण:
```kotlin
println(sumDigits(28))
// prints 10
```

# --seed--

```kotlin
fun sumDigits() {

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

12345 के अंकों का योग 15 है

```kotlin
    tryCatch(sumDigits(12345) == 15)
```

57253 के अंकों का योग 22 है

```kotlin
    tryCatch(sumDigits(57253) == 22)
```

122 के अंकों का योग 5 है

```kotlin
    tryCatch(sumDigits(122) == 5)
```

91979997 के अंकों का योग 60 है

```kotlin
    tryCatch(sumDigits(91979997) == 60)
```

2147483647 के अंकों का योग 46 है

```kotlin
    tryCatch(sumDigits(2147483647) == 46)
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
fun sumDigits(num: Int): Int {
    var n = num
    var result = 0
    while (n > 0) {
        result += n % 10
        n = (n / 10).toInt()
    }
    return result
}
```

