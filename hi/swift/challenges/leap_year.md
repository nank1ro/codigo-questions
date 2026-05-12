---
language: swift
exerciseType: 1
difficulty: 3
title: लीप वर्ष
---

# --description--

एक कैलेंडर वर्ष में ठीक 365.25 दिन होते हैं। लेकिन, अंततः, यह भ्रम पैदा करेगा क्योंकि मनुष्य सामान्यतः 1 की सटीक विभाज्यता से गिनते हैं, दशमलव बिंदुओं से नहीं। इसलिए, इससे बचने के लिए, हर चार वर्ष के चक्र में सभी 0.25 दिनों को जोड़कर उस वर्ष को 366 दिन (29 फरवरी को एक अतिरिक्त दिन के रूप में शामिल करते हुए) देने और इसे __लीप वर्ष__ कहने का निर्णय लिया गया। चार वर्ष के चक्र में अन्य तीन वर्षों में केवल 365 दिन होंगे और वे __लीप वर्ष नहीं होंगे__।

# --instructions--

इस चुनौती में हम इसे एक नए स्तर पर ले जाएंगे, जहां आपको `Date` क्लास, `switch` स्टेटमेंट, __if ब्लॉक__, __if-else ब्लॉक__ या __टर्नरी ऑपरेशन__ (`x ? a : b`) और न ही लॉजिकल ऑपरेटर __AND__ (`&&`) और __OR__ (`||`) के उपयोग के बिना यह निर्धारित करना है कि यह लीप वर्ष है या नहीं, __NOT__ (`!`) ऑपरेटर को छोड़कर।

यदि लीप वर्ष है तो `true` लौटाएं, अन्यथा `false`।

फ़ंक्शन कॉल का उदाहरण:
```swift
print(leapYear(2000))
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
func leapYear(_ year: Int) -> Bool {
    
}
```

# --asserts--

`Date`, `switch`, `if`, `else`, `&&`, `||` या `?` का उपयोग अनुमत नहीं है।

```json
{
  "regex": "if|else|switch|\\?|&&|\\|\\||Date",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

वर्ष `2016` एक लीप वर्ष है।

```swift
tryCatch(leapYear(2016) == true)
```

वर्ष `1996` एक लीप वर्ष है।

```swift
tryCatch(leapYear(1996) == true)
```

वर्ष `1600` एक लीप वर्ष है।

```swift
tryCatch(leapYear(1600) == true)
```

वर्ष `2020` एक लीप वर्ष है।

```swift
tryCatch(leapYear(2020) == true)
```

वर्ष `2000` एक लीप वर्ष है।

```swift
tryCatch(leapYear(2000) == true)
```

वर्ष `2008` एक लीप वर्ष है।

```swift
tryCatch(leapYear(2008) == true)
```

वर्ष `1521` लीप वर्ष नहीं है।

```swift
tryCatch(leapYear(1521) == false)
```

वर्ष `1800` लीप वर्ष नहीं है।

```swift
tryCatch(leapYear(1800) == false)
```

वर्ष `2007` लीप वर्ष नहीं है।

```swift
tryCatch(leapYear(2007) == false)
```

वर्ष `2002` लीप वर्ष नहीं है।

```swift
tryCatch(leapYear(2002) == false)
```

वर्ष `1979` लीप वर्ष नहीं है।

```swift
tryCatch(leapYear(1979) == false)
```

वर्ष `2006` लीप वर्ष नहीं है।

```swift
tryCatch(leapYear(2006) == false)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func leapYear(_ year: Int) -> Bool {
    var yr = year
    while yr % 100 == 0 {
        yr = yr / 100
    }
    return yr % 4 == 0
}
```
