---
language: kotlin
exerciseType: 1
difficulty: 1
title: 3 या 5 के गुणज
---

# --description--

यदि हम 10 से नीचे की सभी प्राकृतिक संख्याओं को सूचीबद्ध करें जो 3 या 5 के गुणज हैं, तो हमें 3, 5, 6 और 9 मिलते हैं। इन गुणजों का योग 23 है।

# --instructions--

दिए गए पैरामीटर मान `number` से नीचे 3 या 5 के सभी गुणजों का योग ज्ञात करें।

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
fun multiplesOf3and5(number) {
  
}
```

# --before-asserts--

```kotlin
fun main() {
```

# --asserts--

`multiplesOf3and5(10)` को 23 लौटाना चाहिए।

```kotlin
tryCatch(multiplesOf3and5(10) == 23)
```

`multiplesOf3and5(1000)` को 233168 लौटाना चाहिए।

```kotlin
tryCatch(multiplesOf3and5(1000) == 233168)
```

`multiplesOf3and5(6987)` को 11390208 लौटाना चाहिए

```kotlin
tryCatch(multiplesOf3and5(6987) == 11390208)
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
fun multiplesOf3and5(number: Int): Int {
    var total = 0
    for (i in 0 until number) {
        if (i % 3 == 0 || i % 5 == 0) {
            total += i
        }
    }
    return total
}
```
