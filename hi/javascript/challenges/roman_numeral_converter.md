---
language: javascript
exerciseType: 1
difficulty: 3
title: रोमन अंक परिवर्तक
---

# --description--

एक फ़ंक्शन बनाएँ जो एक धनात्मक पूर्णांक को पैरामीटर के रूप में ले और उस पूर्णांक के रोमन अंक प्रतिनिधित्व वाली स्ट्रिंग लौटाए। आधुनिक रोमन अंक प्रत्येक अंक को अलग-अलग व्यक्त करके लिखे जाते हैं, सबसे बाएँ अंक से शुरू करते हुए और शून्य मान वाले किसी भी अंक को छोड़ते हुए।

# --instructions--

उदाहरण:
```
convertToRoman(2) ➞ "II"
convertToRoman(12) ➞ "XII"
convertToRoman(16) ➞ "XVI"
```

- सभी रोमन अंक अपरकेस में लौटाए जाने चाहिए।
- इस संकेतन में प्रदर्शित की जा सकने वाली सबसे बड़ी संख्या 3,999 है।

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
function convertToRoman(n) {
  
}
```

# --asserts--

संख्या `2` का मान `II` होना चाहिए

```javascript
tryCatch(convertToRoman(2) === "II");
```

संख्या `12` का मान `XII` होना चाहिए

```javascript
tryCatch(convertToRoman(12) === "XII");
```

संख्या `16` का मान `XVI` होना चाहिए

```javascript
tryCatch(convertToRoman(16) === "XVI");
```

संख्या `44` का मान `XLIV` होना चाहिए

```javascript
tryCatch(convertToRoman(44) === "XLIV");
```

संख्या `68` का मान `LXVIII` होना चाहिए

```javascript
tryCatch(convertToRoman(68) === "LXVIII");
```

संख्या `400` का मान `CD` होना चाहिए

```javascript
tryCatch(convertToRoman(400) === "CD");
```

संख्या `798` का मान `DCCXCVIII` होना चाहिए

```javascript
tryCatch(convertToRoman(798) === "DCCXCVIII");
```

संख्या `1000` का मान `M` होना चाहिए

```javascript
tryCatch(convertToRoman(1000) === "M");
```

संख्या `3999` का मान `MMMCMXCIX` होना चाहिए

```javascript
tryCatch(convertToRoman(3999) === "MMMCMXCIX");
```

संख्या `649` का मान `DCXLIX` होना चाहिए

```javascript
tryCatch(convertToRoman(649) === "DCXLIX");
```

संख्या `1666` का मान `MDCLXVI` होना चाहिए

```javascript
tryCatch(convertToRoman(1666) === "MDCLXVI");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function convertToRoman(n) {
  var result = "";

  const values = [
    [1000, "M"],
    [900, "CM"],
    [500, "D"],
    [400, "CD"],
    [100, "C"],
    [90, "XC"],
    [50, "L"],
    [40, "XL"],
    [10, "X"],
    [9, "IX"],
    [5, "V"],
    [4, "IV"],
    [1, "I"]
  ];

  for (var i = 0; i < values.length; i++) {
    var value = values[i][0];
    var letter = values[i][1];

    while (n >= value) {
      result += letter;
      n -= value;
    }
  }

  return result;
}
```
