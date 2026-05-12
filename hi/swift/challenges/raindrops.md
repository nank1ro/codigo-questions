---
language: swift
exerciseType: 1
difficulty: 1
title: बारिश की बूंदें
---

# --description--

आपका कार्य एक संख्या को एक स्ट्रिंग में बदलना है जिसमें कुछ संभावित गुणनखंडों के अनुरूप बारिश की बूंदों की आवाज़ें हों।
एक गुणनखंड वह संख्या है जो किसी अन्य संख्या को बिना शेषफल के पूर्णतः विभाजित करती है।
यह जांचने का सबसे सरल तरीका कि कोई संख्या किसी अन्य की गुणनखंड है या नहीं, मॉड्यूलो ऑपरेशन का उपयोग करना है।
बारिश की बूंदों के नियम यह हैं कि यदि दी गई संख्या:

- 3 गुणनखंड है, तो परिणाम में 'Pling' जोड़ें।
- 5 गुणनखंड है, तो परिणाम में 'Plang' जोड़ें।
- 7 गुणनखंड है, तो परिणाम में 'Plong' जोड़ें।
- 3, 5, या 7 में से कोई भी गुणनखंड नहीं है, तो परिणाम संख्या के अंक होने चाहिए।

# --instructions--

एक फ़ंक्शन लिखें जो सही स्ट्रिंग लौटाए, उदाहरण:

- 28 में 7 गुणनखंड है, लेकिन 3 या 5 नहीं, इसलिए परिणाम `"Plong"` होगा।
- 30 में 3 और 5 दोनों गुणनखंड हैं, लेकिन 7 नहीं, इसलिए परिणाम `"PlingPlang"` होगा।
- 34 में 3, 5, या 7 में से कोई गुणनखंड नहीं है, इसलिए परिणाम `"34"` होगा।

> संकेत: `_` (अंडरस्कोर) के साथ आर्गुमेंट लेबल हटाएं

फ़ंक्शन कॉल का उदाहरण:
```swift
print(raindrops(28))
// prints "Plong"
```

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func raindrops() {
    
}
```

# --asserts--

1 के लिए ध्वनि "1" है

```swift
tryCatch("1" == raindrops(1))
```

3 के लिए ध्वनि "Pling" है

```swift
tryCatch("Pling" == raindrops(3))
```

5 के लिए ध्वनि "Plang" है

```swift
tryCatch("Plang" == raindrops(5))
```

7 के लिए ध्वनि "Plong" है

```swift
tryCatch("Plong" == raindrops(7))
```

6 के लिए ध्वनि "Pling" है

```swift
tryCatch("Pling" == raindrops(6))
```

8 के लिए ध्वनि "8" है

```swift
tryCatch("8" == raindrops(8))
```

9 के लिए ध्वनि "Pling" है

```swift
tryCatch("Pling" == raindrops(9))
```

10 के लिए ध्वनि "Plang" है

```swift
tryCatch("Plang" == raindrops(10))
```

14 के लिए ध्वनि "Plong" है

```swift
tryCatch("Plong" == raindrops(14))
```

15 के लिए ध्वनि "PlingPlang" है

```swift
tryCatch("PlingPlang" == raindrops(15))
```

21 के लिए ध्वनि "PlingPlong" है

```swift
tryCatch("PlingPlong" == raindrops(21))
```

25 के लिए ध्वनि "Plang" है

```swift
tryCatch("Plang" == raindrops(25))
```

27 के लिए ध्वनि "Pling" है

```swift
tryCatch("Pling" == raindrops(27))
```

35 के लिए ध्वनि "PlangPlong" है

```swift
tryCatch("PlangPlong" == raindrops(35))
```

49 के लिए ध्वनि "Plong" है

```swift
tryCatch("Plong" == raindrops(49))
```

52 के लिए ध्वनि "52" है

```swift
tryCatch("52" == raindrops(52))
```

105 के लिए ध्वनि "PlingPlangPlong" है

```swift
tryCatch("PlingPlangPlong" == raindrops(105))
```

3125 के लिए ध्वनि "Plang" है

```swift
tryCatch("Plang" == raindrops(3125))
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func raindrops(_ num: Int) -> String {
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
    if (result.isEmpty) {
        result = String(num);         
    }

    return result
}
```


