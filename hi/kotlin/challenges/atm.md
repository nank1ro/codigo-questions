---
language: kotlin
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James एक ATM से N डॉलर निकालना चाहता है।
कैश मशीन लेनदेन तभी स्वीकार करेगी जब N, 5 का गुणज हो, और James के खाते में निकासी लेनदेन करने के लिए पर्याप्त नकदी हो (बैंक शुल्क सहित)।
प्रत्येक सफल निकासी के लिए बैंक `0.50$` शुल्क लेता है।
एक प्रयास किए गए लेनदेन के बाद James के खाते की शेष राशि की गणना करें।
इनपुट निम्नलिखित क्रम में हैं:
1. James जितनी नकदी निकालना चाहता है वह निम्नलिखित सीमा में है: `0 < N <= 2000`।
2. James की प्रारंभिक शेष राशि दो अंकों की सटीकता के साथ दी गई है और निम्नलिखित सीमा में है: `0 < B <= 2000`।

# --instructions--

प्रयास किए गए लेनदेन के बाद खाते की शेष राशि लौटाएं, जो दो अंकों की सटीकता वाली संख्या के रूप में दी गई हो।
यदि लेनदेन पूरा करने के लिए खाते में पर्याप्त पैसा नहीं है, तो वर्तमान बैंक शेष राशि लौटाएं।

फ़ंक्शन कॉल का उदाहरण:
```kotlin
println(accountBalance(10, 20.00))
// prints 9.5
```

# --seed--

```kotlin
fun accountBalance(): Double {
    return
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

एक सफल लेनदेन करें

```kotlin
    tryCatch(accountBalance(50, 120.00) == 69.50)
```

अपर्याप्त धनराशि

```kotlin
    tryCatch(accountBalance(200, 120.00) == 120.00)
```

अस्वीकृत लेनदेन, अमान्य राशि

```kotlin
    tryCatch(accountBalance(22, 120.00) == 120.00)
```

सारा पैसा सफलतापूर्वक निकालें

```kotlin
    tryCatch(accountBalance(95, 95.50) == 0.00)
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
fun accountBalance(withdraw: Int, balance: Double): Double {
    val isMultipleOf5 = withdraw.rem(5) == 0;
    val isAmountAvailable = balance >= (withdraw + 0.50)
    if (isMultipleOf5 && isAmountAvailable) {
        return balance - withdraw - 0.50
    }
    return balance
}
```
