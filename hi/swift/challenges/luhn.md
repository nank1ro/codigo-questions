---
language: swift
exerciseType: 1
difficulty: 2
title: लूह्न चेकसम
---

# --description--

लूह्न एल्गोरिदम एक सरल चेकसम है जिसका उपयोग क्रेडिट कार्ड नंबरों जैसी पहचान संख्याओं को मान्य करने के लिए किया जाता है।

किसी संख्या की जांच करने से पहले, स्ट्रिंग से हर स्पेस हटा दें। स्ट्रिंग तभी मान्य है जब शेष बचा हिस्सा एक कैरेक्टर से लंबा हो और मूल स्ट्रिंग में अंकों और स्पेस के अलावा कुछ और न हो।

जांच करने के लिए, सबसे दाईं ओर के अंक से शुरू करें और बाईं ओर बढ़ते हुए हर दूसरे अंक को दोगुना करें। जब दोगुना करने पर 9 से बड़ी संख्या बनती है, तो उसमें से 9 घटा दें। फिर सभी अंकों का योग करें: संख्या तभी मान्य होती है जब योग 10 से विभाज्य हो।

उदाहरण के लिए, `"059"` देता है `0`, फिर `5` का दोगुना `10` होता है जो `1` बन जाता है, फिर `9`। उनका योग `10` है, जो 10 से विभाज्य है, इसलिए संख्या मान्य है।

# --instructions--

एक फ़ंक्शन `isValid` लिखें जो एक स्ट्रिंग लेता है और संख्या मान्य होने पर `true` लौटाता है, अन्यथा `false`।

- `"4539 3195 0343 6467"` चेकसम पास करता है, इसलिए परिणाम `true` है।
- `"8273 1232 7352 0569"` चेकसम में विफल होता है, इसलिए परिणाम `false` है।
- `"0"` केवल एक कैरेक्टर लंबा है, इसलिए परिणाम `false` है।
- `"055-444-285"` में ऐसा कैरेक्टर है जो अंक या स्पेस नहीं है, इसलिए परिणाम `false` है।

> संकेत: `_` (अंडरस्कोर) के साथ आर्गुमेंट लेबल हटाएं

फ़ंक्शन कॉल का उदाहरण:
```swift
print(isValid("095 245 88"))
// prints true
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
func isValid(_ value: String) -> Bool {
    
}
```

# --asserts--

एक अकेला अंक मान्य नहीं है।

```swift
tryCatch(isValid("0") == false)
```

शुरुआत में स्पेस के साथ एक अकेला अंक मान्य नहीं है।

```swift
tryCatch(isValid(" 0") == false)
```

संख्या `"059"` मान्य है।

```swift
tryCatch(isValid("059") == true)
```

संख्या `"59"` मान्य है।

```swift
tryCatch(isValid("59") == true)
```

संख्या `"055 444 285"` मान्य है।

```swift
tryCatch(isValid("055 444 285") == true)
```

संख्या `"055 444 286"` मान्य नहीं है।

```swift
tryCatch(isValid("055 444 286") == false)
```

संख्या `"8273 1232 7352 0569"` मान्य नहीं है।

```swift
tryCatch(isValid("8273 1232 7352 0569") == false)
```

संख्या `"4539 3195 0343 6467"` मान्य है।

```swift
tryCatch(isValid("4539 3195 0343 6467") == true)
```

संख्या `"1 2345 6789 1234 5678 9012"` मान्य नहीं है।

```swift
tryCatch(isValid("1 2345 6789 1234 5678 9012") == false)
```

संख्या `"095 245 88"` मान्य है।

```swift
tryCatch(isValid("095 245 88") == true)
```

एक अक्षर संख्या को अमान्य बना देता है।

```swift
tryCatch(isValid("055a 444 285") == false)
```

डैश संख्या को अमान्य बना देते हैं।

```swift
tryCatch(isValid("055-444-285") == false)
```

एक विराम चिह्न कैरेक्टर संख्या को अमान्य बना देता है।

```swift
tryCatch(isValid(":9") == false)
```

प्रतीक संख्या को अमान्य बना देते हैं।

```swift
tryCatch(isValid("055# 444$ 285") == false)
```

खाली स्ट्रिंग मान्य नहीं है।

```swift
tryCatch(isValid("") == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isValid(_ value: String) -> Bool {
    var sum = 0
    var count = 0
    for character in value.reversed() {
        if character == " " {
            continue
        }
        guard character.isASCII, character.isNumber,
              let number = character.wholeNumberValue else {
            return false
        }
        var digit = number
        if count % 2 == 1 {
            digit *= 2
            if digit > 9 {
                digit -= 9
            }
        }
        sum += digit
        count += 1
    }
    return count > 1 && sum % 10 == 0
}
```
