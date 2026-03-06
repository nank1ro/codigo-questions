---
language: kotlin
exerciseType: 1
difficulty: 1
title: दो में से एक
---

# --description--

एक नाम दिया गया है, संदेश के साथ एक स्ट्रिंग लौटाएं:
`One for X, one for me.`
जहाँ `X` दिया गया नाम है।
हालांकि, यदि नाम गायब है, तो स्ट्रिंग लौटाएं:
`One for you, one for me.`

# --instructions--

एक फ़ंक्शन लिखें जो सही स्ट्रिंग लौटाए, उदाहरण:

**इनपुट**: `Walter`
**आउटपुट**: `One for Walter, one for me.`

**इनपुट**: `James`
**आउटपुट**: `One for James, one for me.`

**इनपुट**: `Martha`
**आउटपुट**: `One for Martha, one for me.`

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

कोई नाम नहीं दिया गया

```kotlin
    tryCatch(twoForOne() == "One for you, one for me.")
```

नाम के रूप में "James" पास करें

```kotlin
    tryCatch(twoForOne(name = "James") == "One for James, one for me.")
```

नाम के रूप में "Martha" पास करें

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


