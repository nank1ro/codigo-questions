---
language: kotlin
exerciseType: 1
difficulty: 1
title: जोड़
---

# --description--

दो पूर्णांक `num1` और `num2` दिए गए हैं, इन दो संख्याओं को जोड़ने के लिए एक प्रोग्राम लिखें

# --instructions--

एक फ़ंक्शन लिखें जो दो संख्याओं का योग लौटाए।

फ़ंक्शन कॉल का उदाहरण:
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

1 और 3 का योग 4 होना चाहिए

```kotlin
    tryCatch(addition(1, 3) == 4)
```

200 और 210 का योग 410 होना चाहिए

```kotlin
    tryCatch(addition(200, 210) == 410)
```

15 और 35 का योग 50 होना चाहिए

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
