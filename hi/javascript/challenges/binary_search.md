---
language: javascript
exerciseType: 1
difficulty: 2
title: बाइनरी सर्च
---

# --description--

बाइनरी सर्च खोज की सीमा को बार-बार आधा करके किसी **क्रमबद्ध** कलेक्शन में एक मान ढूंढता है: बीच में स्थित तत्व को देखें, और यदि वही तत्व नहीं है जिसे आप चाहते हैं, तो जब लक्ष्य छोटा हो तो बाएं आधे हिस्से में और जब लक्ष्य बड़ा हो तो दाएं आधे हिस्से में खोज जारी रखें।

चूंकि हर चरण शेष तत्वों में से आधे तत्वों को छोड़ देता है, इसलिए बाइनरी सर्च बहुत बड़े कलेक्शन पर भी कुछ ही तुलनाओं में उत्तर तक पहुंच जाता है, जबकि तत्वों को एक-एक करके जांचने में उतने ही चरण लगते हैं जितने तत्व होते हैं।

# --instructions--

एक फ़ंक्शन `binarySearch` लिखें जो आरोही क्रम में क्रमबद्ध पूर्णांकों की एक सरणी और एक लक्ष्य पूर्णांक लेता है, और सरणी के भीतर लक्ष्य का इंडेक्स लौटाता है, या `-1` लौटाता है जब लक्ष्य मौजूद न हो।

सरणी में कभी डुप्लिकेट नहीं होते, इसलिए इंडेक्स हमेशा अद्वितीय होता है। सरणी खाली भी हो सकती है। आपके फ़ंक्शन को लीनियर स्कैन नहीं, बल्कि बाइनरी सर्च का उपयोग करना चाहिए, हर चरण में खोज की सीमा को आधा करते हुए।

फ़ंक्शन कॉल का उदाहरण:
```javascript
console.log(binarySearch([1, 3, 5, 7], 5));
// prints 2
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
// DO NOT EDIT UNTIL HERE
```

# --seed--

```javascript
function binarySearch(arr, target) {
  
}
```

# --asserts--

खाली सरणी में खोज करने पर -1 लौटाना चाहिए।

```javascript
tryCatch(binarySearch([], 7) === -1);
```

`[5]` में 5 खोजने पर 0 लौटाना चाहिए।

```javascript
tryCatch(binarySearch([5], 5) === 0);
```

`[5]` में 9 खोजने पर -1 लौटाना चाहिए।

```javascript
tryCatch(binarySearch([5], 9) === -1);
```

12 तत्वों वाली सरणी का पहला तत्व -9 इंडेक्स 0 पर मिलना चाहिए।

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9) === 0);
```

12 तत्वों वाली सरणी का अंतिम तत्व 78 इंडेक्स 11 पर मिलना चाहिए।

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78) === 11);
```

तत्व 15 इंडेक्स 6 पर मिलना चाहिए।

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15) === 6);
```

तत्व 22 इंडेक्स 7 पर मिलना चाहिए।

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22) === 7);
```

मान 12, जो 11 और 15 के बीच स्थित है, -1 लौटाना चाहिए।

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12) === -1);
```

हर तत्व से छोटा लक्ष्य -1 लौटाना चाहिए।

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100) === -1);
```

हर तत्व से बड़ा लक्ष्य -1 लौटाना चाहिए।

```javascript
tryCatch(binarySearch([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100) === -1);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function binarySearch(arr, target) {
  let low = 0;
  let high = arr.length - 1;
  while (low <= high) {
    const mid = Math.floor((low + high) / 2);
    if (arr[mid] === target) {
      return mid;
    }
    if (arr[mid] < target) {
      low = mid + 1;
    } else {
      high = mid - 1;
    }
  }
  return -1;
}
```
