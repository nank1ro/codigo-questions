---
language: javascript
exerciseType: 1
difficulty: 1
title: 100 दरवाज़े
---

# --description--

एक पंक्ति में 100 दरवाज़े हैं जो शुरू में सभी बंद हैं।
आप दरवाज़ों से 100 बार गुज़रते हैं।
पहली बार, हर दरवाज़े पर जाएँ और दरवाज़े को 'टॉगल' करें (अगर दरवाज़ा बंद है तो खोलें; अगर खुला है तो बंद करें)।
दूसरी बार, केवल हर दूसरे दरवाज़े पर जाएँ (यानी, दरवाज़ा #2, #4, #6, ...) और उसे टॉगल करें।
तीसरी बार, हर तीसरे दरवाज़े पर जाएँ (यानी, दरवाज़ा #3, #6, #9, ...), आदि, जब तक आप केवल 100वें दरवाज़े पर न जाएँ।

# --instructions--

अंतिम पास के बाद दरवाज़ों की स्थिति निर्धारित करने के लिए एक फ़ंक्शन लागू करें।
अंतिम परिणाम एक ऐरे में लौटाएँ, जिसमें केवल उन दरवाज़ों की संख्या शामिल हो जो खुले हैं।
> विधि को दरवाज़ों की परिवर्तनशील संख्या के साथ काम करने में सक्षम होना चाहिए।

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
function getFinalOpenedDoors(numDoors) {
    
}
```

# --asserts--

100 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएँ

```javascript
const sol1 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100];
tryCatch(arraysMatch(getFinalOpenedDoors(100), sol1));
```

10 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएँ

```javascript
const sol2 = [1, 4, 9];
tryCatch(arraysMatch(getFinalOpenedDoors(10), sol2));
```

950 दरवाज़े दिए गए हैं, खुले दरवाज़ों की सही सूची लौटाएँ

```javascript
const sol3 = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900];
tryCatch(arraysMatch(getFinalOpenedDoors(950), sol3));
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function getFinalOpenedDoors(numDoors) {
    const openDoors = [];
    var i = 1;
    while (Math.pow(i, 2) <= numDoors) {
        openDoors.push(Math.pow(i, 2));
        i++;
    }
    return openDoors;
}
```
