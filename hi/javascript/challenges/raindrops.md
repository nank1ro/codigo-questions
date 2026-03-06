---
language: javascript
exerciseType: 1
difficulty: 1
title: बारिश की बूँदें
---

# --description--

आपका कार्य एक संख्या को एक ऐसी स्ट्रिंग में बदलना है जिसमें कुछ संभावित गुणनखंडों के अनुरूप बारिश की बूंदों की ध्वनियाँ हों।
गुणनखंड वह संख्या है जो किसी अन्य संख्या को बिना शेषफल के समान रूप से विभाजित करती है।
यह जाँचने का सबसे सरल तरीका कि कोई संख्या दूसरी की गुणनखंड है या नहीं, मॉड्यूलो ऑपरेशन का उपयोग करना है।
रेनड्रॉप्स के नियम निम्नलिखित हैं:

- यदि 3 गुणनखंड है, तो परिणाम में 'Pling' जोड़ें।
- यदि 5 गुणनखंड है, तो परिणाम में 'Plang' जोड़ें।
- यदि 7 गुणनखंड है, तो परिणाम में 'Plong' जोड़ें।
- यदि 3, 5, या 7 में से कोई भी गुणनखंड नहीं है, तो परिणाम संख्या के अंक होने चाहिए।

# --instructions--

एक फ़ंक्शन लिखें जो सही स्ट्रिंग लौटाए, उदाहरण:

- 28 में 7 गुणनखंड है, लेकिन 3 या 5 नहीं, इसलिए परिणाम `"Plong"` होगा।
- 30 में 3 और 5 दोनों गुणनखंड हैं, लेकिन 7 नहीं, इसलिए परिणाम `"PlingPlang"` होगा।
- 34 में 3, 5, या 7 से कोई भी गुणनखंड नहीं है, इसलिए परिणाम `"34"` होगा।

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
function convert(number) {
  
}
```

# --asserts--

1 के लिए ध्वनि "1" है

```javascript
tryCatch(convert(1) === "1");
```

3 के लिए ध्वनि "Pling" है

```javascript
tryCatch(convert(3) === "Pling");
```

5 के लिए ध्वनि "Plang" है

```javascript
tryCatch(convert(5) === "Plang");
```

7 के लिए ध्वनि "Plong" है

```javascript
tryCatch(convert(7) === "Plong");
```

6 के लिए ध्वनि "Pling" है

```javascript
tryCatch(convert(6) === "Pling");
```

8 के लिए ध्वनि "8" है

```javascript
tryCatch(convert(8) === "8");
```

9 के लिए ध्वनि "Pling" है

```javascript
tryCatch(convert(9) === "Pling");
```

10 के लिए ध्वनि "Plang" है

```javascript
tryCatch(convert(10) === "Plang");
```

14 के लिए ध्वनि "Plong" है

```javascript
tryCatch(convert(14) === "Plong");
```

15 के लिए ध्वनि "PlingPlang" है

```javascript
tryCatch(convert(15) === "PlingPlang");
```

21 के लिए ध्वनि "PlingPlong" है

```javascript
tryCatch(convert(21) === "PlingPlong");
```

25 के लिए ध्वनि "Plang" है

```javascript
tryCatch(convert(25) === "Plang");
```

27 के लिए ध्वनि "Pling" है

```javascript
tryCatch(convert(27) === "Pling");
```

35 के लिए ध्वनि "PlangPlong" है

```javascript
tryCatch(convert(35) === "PlangPlong");
```

49 के लिए ध्वनि "Plong" है

```javascript
tryCatch(convert(49) === "Plong");
```

52 के लिए ध्वनि "52" है

```javascript
tryCatch(convert(52) === "52");
```

105 के लिए ध्वनि "PlingPlangPlong" है

```javascript
tryCatch(convert(105) === "PlingPlangPlong");
```

3125 के लिए ध्वनि "Plang" है

```javascript
tryCatch(convert(3125) === "Plang");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function convert(number) {
  var result = ""
  if (number % 3 == 0) {
    result += "Pling"
  }
  if (number % 5 == 0) {
    result += "Plang"
  }
  if (number % 7 == 0) {
    result += "Plong"
  }
  if (!result) {
    result = number.toString()
  }
  return result
}
```
