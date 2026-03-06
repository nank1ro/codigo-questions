---
language: kotlin
exerciseType: 1
difficulty: 1
title: बारिश की बूँदें
---

# --description--

आपका कार्य एक संख्या को एक ऐसी स्ट्रिंग में बदलना है जिसमें कुछ संभावित गुणनखंडों के अनुरूप बारिश की बूँदों की आवाज़ें हों।
एक गुणनखंड वह संख्या है जो किसी अन्य संख्या को पूर्ण रूप से विभाजित करती है, कोई शेष नहीं छोड़ती।
यह जाँचने का सबसे सरल तरीका कि कोई संख्या दूसरी का गुणनखंड है या नहीं, मॉड्यूलो ऑपरेशन का उपयोग करना है।
बारिश की बूँदों के नियम यह हैं कि यदि दी गई संख्या:

- का गुणनखंड 3 है, तो परिणाम में 'Pling' जोड़ें।
- का गुणनखंड 5 है, तो परिणाम में 'Plang' जोड़ें।
- का गुणनखंड 7 है, तो परिणाम में 'Plong' जोड़ें।
- का गुणनखंड 3, 5, या 7 में से कोई नहीं है, तो परिणाम संख्या के अंक होने चाहिए।

# --instructions--

एक फ़ंक्शन लिखें जो सही स्ट्रिंग लौटाए, उदाहरण:

- 28 का गुणनखंड 7 है, लेकिन 3 या 5 नहीं, इसलिए परिणाम `"Plong"` होगा।
- 30 के गुणनखंड 3 और 5 दोनों हैं, लेकिन 7 नहीं, इसलिए परिणाम `"PlingPlang"` होगा।
- 34 का गुणनखंड 3, 5, या 7 नहीं है, इसलिए परिणाम `"34"` होगा।

फ़ंक्शन कॉल का उदाहरण:
```kotlin
println(raindrops(28))
// prints "Plong"
```

# --seed--

```kotlin
fun raindrops(): String {
    
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

1 के लिए ध्वनि "1" है

```kotlin
    tryCatch(raindrops(1) == "1")
```

3 के लिए ध्वनि "Pling" है

```kotlin
    tryCatch(raindrops(3) == "Pling")
```

5 के लिए ध्वनि "Plang" है

```kotlin
    tryCatch(raindrops(5) == "Plang")
```

7 के लिए ध्वनि "Plong" है

```kotlin
    tryCatch(raindrops(7) == "Plong")
```

6 के लिए ध्वनि "Pling" है

```kotlin
    tryCatch(raindrops(6) == "Pling")
```

8 के लिए ध्वनि "8" है

```kotlin
    tryCatch(raindrops(8) == "8")
```

9 के लिए ध्वनि "Pling" है

```kotlin
    tryCatch(raindrops(9) == "Pling")
```

10 के लिए ध्वनि "Plang" है

```kotlin
    tryCatch(raindrops(10) == "Plang")
```

14 के लिए ध्वनि "Plong" है

```kotlin
    tryCatch(raindrops(14) == "Plong")
```

15 के लिए ध्वनि "PlingPlang" है

```kotlin
    tryCatch(raindrops(15) == "PlingPlang")
```

21 के लिए ध्वनि "PlingPlong" है

```kotlin
    tryCatch(raindrops(21) == "PlingPlong")
```

25 के लिए ध्वनि "Plang" है

```kotlin
    tryCatch(raindrops(25) == "Plang")
```

27 के लिए ध्वनि "Pling" है

```kotlin
    tryCatch(raindrops(27) == "Pling")
```

35 के लिए ध्वनि "PlangPlong" है

```kotlin
    tryCatch(raindrops(35) == "PlangPlong")
```

49 के लिए ध्वनि "Plong" है

```kotlin
    tryCatch(raindrops(49) == "Plong")
```

52 के लिए ध्वनि "52" है

```kotlin
    tryCatch(raindrops(52) == "52")
```

105 के लिए ध्वनि "PlingPlangPlong" है

```kotlin
    tryCatch(raindrops(105) == "PlingPlangPlong")
```

3125 के लिए ध्वनि "Plang" है

```kotlin
    tryCatch(raindrops(3125) == "Plang")
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
fun raindrops(num: Int): String {
    var result = "";
    if (num % 3 == 0) {
        result += "Pling"
    } 
    if (num % 5 == 0) {
        result += "Plang"
    }
    if (num % 7 == 0) {
        result += "Plong"
    }
    if (result.isEmpty()) {
        result = num.toString()     
    }
    return result
}
```
