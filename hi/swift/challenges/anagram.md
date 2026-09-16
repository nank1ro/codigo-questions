---
language: swift
exerciseType: 1
difficulty: 2
title: अनाग्राम
---

# --description--

दो शब्द अनाग्राम होते हैं जब एक दूसरे के अक्षरों की पुनर्व्यवस्था हो: वे बिल्कुल वही अक्षर उपयोग करते हैं, प्रत्येक अक्षर उतनी ही बार, बस अलग क्रम में। `listen` और `silent` अनाग्राम हैं, और वैसे ही `stone` और `tones` भी।

कोई शब्द कभी अपने आप का अनाग्राम नहीं होता। यदि दोनों शब्द बिल्कुल समान हैं, तो कुछ भी पुनर्व्यवस्थित नहीं हुआ, इसलिए उत्तर `false` है। दोनों शब्द छोटे अक्षरों में दिए जाते हैं और उनमें केवल `a` से `z` तक के अक्षर होते हैं।

# --instructions--

एक फ़ंक्शन `isAnagram` लिखें जो दो शब्द, `first` और `second`, लेता है और यदि वे एक-दूसरे के अनाग्राम हैं तो `true` लौटाता है, अन्यथा `false` लौटाता है।

उदाहरण:
```
isAnagram("listen", "silent") ➞ true
isAnagram("stone", "tones") ➞ true
isAnagram("stone", "stone") ➞ false
isAnagram("abc", "abcd") ➞ false
isAnagram("aab", "abb") ➞ false
```

- दो समान शब्द अनाग्राम नहीं होते।
- अलग-अलग लंबाई के शब्द कभी अनाग्राम नहीं होते।
- प्रत्येक अक्षर दोनों शब्दों में उतनी ही बार आना चाहिए।

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
func isAnagram(_ first: String, _ second: String) -> Bool {
    
}
```

# --asserts--

शब्द "listen" और "silent" अनाग्राम हैं

```swift
tryCatch(isAnagram("listen", "silent") == true)
```

शब्द "stone" और "tones" अनाग्राम हैं

```swift
tryCatch(isAnagram("stone", "tones") == true)
```

कोई शब्द अपने आप का अनाग्राम नहीं होता

```swift
tryCatch(isAnagram("stone", "stone") == false)
```

अलग-अलग लंबाई के शब्द अनाग्राम नहीं होते

```swift
tryCatch(isAnagram("abc", "abcd") == false)
```

समान अक्षरों की अलग-अलग मात्रा अनाग्राम नहीं होती

```swift
tryCatch(isAnagram("aab", "abb") == false)
```

शब्द "anagram" और "nagaram" अनाग्राम हैं

```swift
tryCatch(isAnagram("anagram", "nagaram") == true)
```

समान लंबाई वाले दो शब्द जिनके अक्षर अलग हैं, अनाग्राम नहीं होते

```swift
tryCatch(isAnagram("rat", "car") == false)
```

दो खाली शब्द समान होते हैं, इसलिए वे अनाग्राम नहीं होते

```swift
tryCatch(isAnagram("", "") == false)
```

दो अलग एकल अक्षर अनाग्राम नहीं होते

```swift
tryCatch(isAnagram("a", "b") == false)
```

शब्द "evil" और "vile" अनाग्राम हैं

```swift
tryCatch(isAnagram("evil", "vile") == true)
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func isAnagram(_ first: String, _ second: String) -> Bool {
    if first == second {
        return false
    }

    return first.sorted() == second.sorted()
}
```
