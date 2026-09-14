---
language: javascript
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
```javascript
console.log(bubbleSort([3, 1, 2]));
// prints [ 1, 2, 3 ]
```

# --before-seed--

```javascript
// DO NOT EDIT FROM HERE
var _testFailedCount = 0;
var _testCount = 0;
var assert = require('assert')
const tryCatch = (...args) => {
  _testCount++
  try { assert(...args) }
  catch (e) {
    _testFailedCount++
    console.log(`Test Case '--err-t${_testCount}--' failed`);
  }
};

// Returns true if two arrays are equal and in the same order
var arraysMatch = function (arr1, arr2) {
    // Check if the arrays are the same length
    if (arr1.length !== arr2.length) return false;

    // Check if all items exist and are in the same order
    for (var i = 0; i < arr1.length; i++) {
        if (arr1[i] !== arr2[i]) return false;
    }

    // Otherwise, return true
    return true;
};
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function bubbleSort(arr) {
  
}
```

# --asserts--

एक खाली सरणी को एक खाली सरणी लौटानी चाहिए

```javascript
tryCatch(arraysMatch(bubbleSort([]), []));
```

एक ही तत्व वाली सरणी वैसी ही रहनी चाहिए

```javascript
tryCatch(arraysMatch(bubbleSort([42]), [42]));
```

पहले से क्रमबद्ध सरणी उसी क्रम में रहनी चाहिए

```javascript
tryCatch(arraysMatch(bubbleSort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5]));
```

उल्टे क्रम में क्रमबद्ध सरणी को आरोही क्रम में बदलना चाहिए

```javascript
tryCatch(arraysMatch(bubbleSort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5]));
```

दोहराए गए सभी मान बने रहने चाहिए

```javascript
tryCatch(arraysMatch(bubbleSort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3]));
```

ऋणात्मक संख्याओं को धनात्मक संख्याओं से पहले क्रमबद्ध होना चाहिए

```javascript
tryCatch(arraysMatch(bubbleSort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3]));
```

एक लंबी मिश्रित सरणी आरोही क्रम में क्रमबद्ध होनी चाहिए

```javascript
tryCatch(arraysMatch(bubbleSort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14]));
```

पास की गई सरणी में बदलाव नहीं होना चाहिए

```javascript
const original = [3, 1, 2];
bubbleSort(original);
tryCatch(arraysMatch(original, [3, 1, 2]));
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function bubbleSort(arr) {
  const result = [...arr];
  let end = result.length;
  let swapped = true;
  while (swapped) {
    swapped = false;
    for (let i = 1; i < end; i++) {
      if (result[i - 1] > result[i]) {
        const temp = result[i - 1];
        result[i - 1] = result[i];
        result[i] = temp;
        swapped = true;
      }
    }
    end--;
  }
  return result;
}
```
