---
language: kotlin
exerciseType: 1
difficulty: 1
title: Ackermann फ़ंक्शन
---

# --description--

Ackermann फ़ंक्शन एक पुनरावर्ती फ़ंक्शन का एक उत्कृष्ट उदाहरण है, जो विशेष रूप से इसलिए उल्लेखनीय है क्योंकि यह एक आदिम पुनरावर्ती फ़ंक्शन नहीं है। इसका मान बहुत तेज़ी से बढ़ता है, जैसा कि इसके कॉल ट्री का आकार भी बढ़ता है।

Ackermann फ़ंक्शन को आमतौर पर निम्नानुसार परिभाषित किया जाता है:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

इसके तर्क कभी ऋणात्मक नहीं होते और यह हमेशा समाप्त होता है

# --instructions--

एक फ़ंक्शन लिखें जो Ackermann फ़ंक्शन का मान लौटाए।

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

`ack(0, 0)` को 1 लौटाना चाहिए।

```kotlin
    tryCatch(ack(0, 0) == 1)
```

`ack(1, 1)` को 3 लौटाना चाहिए।

```kotlin
    tryCatch(ack(1, 1) == 3)
```

`ack(2, 5)` को 13 लौटाना चाहिए।

```kotlin
    tryCatch(ack(2, 5) == 13)
```

`ack(3, 3)` को 61 लौटाना चाहिए।

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
