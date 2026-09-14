---
language: swift
exerciseType: 1
difficulty: 2
title: बबल सॉर्ट
---

# --description--

बबल सॉर्ट सबसे सरल सॉर्टिंग एल्गोरिदम में से एक है। यह एक सूची से गुज़रता है और आसन्न तत्वों के हर जोड़े की तुलना करता है, और जब भी वे गलत क्रम में होते हैं तो उन्हें आपस में बदल देता है। हर पूरे चक्र के बाद सबसे बड़ा शेष मान "बुलबुले" की तरह अपनी अंतिम जगह पर पहुँच जाता है, और जैसे ही कोई चक्र बिना एक भी अदला-बदली के पूरा होता है, सूची क्रमबद्ध हो जाती है।

# --instructions--

`bubbleSort` नाम का एक फ़ंक्शन लिखें जो पूर्णांकों की एक सरणी लेता है और उन्हीं मानों के साथ एक **नई** सरणी आरोही क्रम में क्रमबद्ध करके लौटाता है। पास की गई सरणी में बदलाव नहीं होना चाहिए।

आपको बबल सॉर्ट एल्गोरिदम स्वयं लागू करना होगा, आसन्न तत्वों की तुलना करके और उन्हें आपस में बदलकर। मानक लाइब्रेरी के किसी सॉर्टिंग फ़ंक्शन का उपयोग न करें।

आपका फ़ंक्शन एक खाली सरणी, एक ही तत्व वाली सरणी, पहले से क्रमबद्ध सरणी, दोहराए गए मानों और ऋणात्मक संख्याओं के साथ भी काम करना चाहिए।

फ़ंक्शन कॉल का उदाहरण:
```swift
print(bubbleSort([3, 1, 2]))
// prints [1, 2, 3]
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
func bubbleSort(_ arr: [Int]) -> [Int] {
    
}
```

# --asserts--

एक खाली सरणी को एक खाली सरणी लौटानी चाहिए

```swift
do {
    let solution: [Int] = []
    tryCatch(bubbleSort([]) == solution)
}
```

एक ही तत्व वाली सरणी वैसी ही रहनी चाहिए

```swift
do {
    let solution: [Int] = [42]
    tryCatch(bubbleSort([42]) == solution)
}
```

पहले से क्रमबद्ध सरणी उसी क्रम में रहनी चाहिए

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([1, 2, 3, 4, 5]) == solution)
}
```

उल्टे क्रम में क्रमबद्ध सरणी को आरोही क्रम में बदलना चाहिए

```swift
do {
    let solution: [Int] = [1, 2, 3, 4, 5]
    tryCatch(bubbleSort([5, 4, 3, 2, 1]) == solution)
}
```

दोहराए गए सभी मान बने रहने चाहिए

```swift
do {
    let solution: [Int] = [1, 1, 2, 3, 3]
    tryCatch(bubbleSort([3, 1, 3, 2, 1]) == solution)
}
```

ऋणात्मक संख्याओं को धनात्मक संख्याओं से पहले क्रमबद्ध होना चाहिए

```swift
do {
    let solution: [Int] = [-9, -5, -1, 0, 3]
    tryCatch(bubbleSort([-5, 3, -1, 0, -9]) == solution)
}
```

एक लंबी मिश्रित सरणी आरोही क्रम में क्रमबद्ध होनी चाहिए

```swift
do {
    let solution: [Int] = [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]
    tryCatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]) == solution)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```

# --solutions--

```swift
func bubbleSort(_ arr: [Int]) -> [Int] {
    var result = arr
    var end = result.count
    var swapped = true
    while swapped && end > 1 {
        swapped = false
        for i in 1..<end {
            if result[i - 1] > result[i] {
                let temp = result[i - 1]
                result[i - 1] = result[i]
                result[i] = temp
                swapped = true
            }
        }
        end -= 1
    }
    return result
}
```
