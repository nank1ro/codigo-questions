---
language: kotlin
exerciseType: 1
difficulty: 1
title: FizzBuzz
---

# --description--

एक फ़ंक्शन बनाएं जो एक संख्या को तर्क के रूप में लेता है और `"Fizz"`, `"Buzz"` या `"FizzBuzz"` लौटाता है।

# --instructions--

- यदि संख्या `3` का गुणज है तो आउटपुट `"Fizz"` होना चाहिए
- यदि दी गई संख्या `5` का गुणज है, तो आउटपुट `"Buzz"` होना चाहिए।
- यदि दी गई संख्या `3` और `5` दोनों का गुणज है, तो आउटपुट `"FizzBuzz"` होना चाहिए।
- यदि संख्या `3` या `5` में से किसी का भी गुणज नहीं है, तो संख्या को नीचे दिए गए उदाहरणों में दिखाए अनुसार अपने आप में आउटपुट किया जाना चाहिए।
- आउटपुट हमेशा एक स्ट्रिंग होना चाहिए भले ही यह `3` या `5` का गुणज न हो।

उदाहरण:
```kotlin
fizz_buzz(3) // ➞ "Fizz"
fizz_buzz(5) // ➞ "Buzz"
fizz_buzz(15) // ➞ "FizzBuzz"
fizz_buzz(4) // ➞ "4"
```

# --seed--

```kotlin
fun fizzBuzz() {
    
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

संख्या `3` का मान `"Fizz"` होना चाहिए

```kotlin
    tryCatch(fizzBuzz(3) == "Fizz");
```

संख्या `5` का मान `"Buzz"` होना चाहिए

```kotlin
    tryCatch(fizzBuzz(5) == "Buzz");
```

संख्या `15` का मान `"FizzBuzz"` होना चाहिए

```kotlin
    tryCatch(fizzBuzz(15) == "FizzBuzz");
```

संख्या `10` का मान `"Buzz"` होना चाहिए

```kotlin
    tryCatch(fizzBuzz(10) == "Buzz");
```

संख्या `98` का मान `"98"` होना चाहिए

```kotlin
    tryCatch(fizzBuzz(98) == "98");
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
fun fizzBuzz(number: Int): String {
    if (number % 3 == 0 && number % 5 == 0) {
        return "FizzBuzz"
    }
    if (number % 3 == 0) {
        return "Fizz"
    }
    if (number % 5 == 0) {
        return "Buzz"
    }
    return number.toString()
}
```
