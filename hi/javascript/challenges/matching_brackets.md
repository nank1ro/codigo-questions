---
language: javascript
exerciseType: 1
difficulty: 3
title: कोष्ठकों का मिलान
---

# --description--

कोड, गणित या मार्कअप ले जाने वाला टेक्स्ट कोष्ठकों से भरा होता है, और हर खोलने वाले कोष्ठक को उसी किस्म का एक बंद करने वाला कोष्ठक चाहिए। एक स्ट्रिंग तब संतुलित होती है जब उसके कोष्ठक जोड़े बनाते हैं और प्याज की परतों की तरह एक-दूसरे के भीतर नेस्ट होते हैं: `{[()]}` संतुलित है, जबकि `{[(])}` संतुलित नहीं है, क्योंकि गोल जोड़ा उस वर्ग जोड़े से पहले बंद हो जाता है जिसके भीतर वह स्थित है।

यहाँ तीन जोड़े मायने रखते हैं: गोल `()`, वर्ग `[]` और कर्ली `{}`। स्ट्रिंग का बाकी हर कैरेक्टर नज़रअंदाज़ कर दिया जाता है। एक बंद करने वाले कोष्ठक को सबसे हाल में खोले गए उस कोष्ठक को बंद करना चाहिए जो अभी भी खुला है, और जब स्ट्रिंग समाप्त हो जाए तो कोई कोष्ठक खुला नहीं रहना चाहिए।

# --instructions--

एक फ़ंक्शन `isBalanced` लिखें जो एक स्ट्रिंग लेता है और तब `true` लौटाता है जब उसके सभी कोष्ठक मेल खाते हों और ठीक से नेस्ट होते हों, अन्यथा `false`।

उदाहरण:
```
isBalanced("") ➞ true
isBalanced("{[()]}") ➞ true
isBalanced("{what is (42)}[?]") ➞ true
isBalanced("{[(])}") ➞ false
isBalanced("(") ➞ false
isBalanced(")(") ➞ false
```

- खाली स्ट्रिंग संतुलित होती है।
- जो कैरेक्टर कोष्ठक नहीं हैं उन्हें नज़रअंदाज़ कर दिया जाता है।
- एक बंद करने वाला कोष्ठक सबसे हाल में खोले गए उस कोष्ठक से मेल खाना चाहिए जो अभी भी खुला है।
- जब स्ट्रिंग समाप्त हो तब कोई कोष्ठक खुला नहीं रहना चाहिए।

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
function isBalanced(text) {
  
}
```

# --asserts--

खाली स्ट्रिंग संतुलित होती है

```javascript
tryCatch(isBalanced("") === true);
```

गोल कोष्ठकों का एक जोड़ा संतुलित होता है

```javascript
tryCatch(isBalanced("()") === true);
```

एक-दूसरे के भीतर नेस्ट किए गए तीनों किस्म के जोड़े संतुलित होते हैं

```javascript
tryCatch(isBalanced("{[()]}") === true);
```

दूसरे टेक्स्ट के साथ मिले कोष्ठक भी संतुलित होते हैं

```javascript
tryCatch(isBalanced("{what is (42)}[?]") === true);
```

बगल में रखे गए जोड़े संतुलित होते हैं

```javascript
tryCatch(isBalanced("()[]{}") === true);
```

बिना किसी कोष्ठक वाली स्ट्रिंग संतुलित होती है

```javascript
tryCatch(isBalanced("no brackets in here at all") === true);
```

क्रॉस हो चुका जोड़ा संतुलित नहीं होता

```javascript
tryCatch(isBalanced("{[(])}") === false);
```

कभी बंद न होने वाला खोलने वाला कोष्ठक संतुलित नहीं होता

```javascript
tryCatch(isBalanced("(") === false);
```

किसी खोलने वाले कोष्ठक से पहले आया बंद करने वाला कोष्ठक संतुलित नहीं होता

```javascript
tryCatch(isBalanced(")(") === false);
```

स्ट्रिंग में गहराई में क्रॉस हो चुके जोड़े संतुलित नहीं होते

```javascript
tryCatch(isBalanced("(([]{[}]))") === false);
```

अंत में बचा हुआ बंद करने वाला कोष्ठक संतुलित नहीं होता

```javascript
tryCatch(isBalanced("())") === false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isBalanced(text) {
  const pairs = { ")": "(", "]": "[", "}": "{" };
  const stack = [];

  for (const char of text) {
    if (char === "(" || char === "[" || char === "{") {
      stack.push(char);
    } else if (char in pairs) {
      if (stack.pop() !== pairs[char]) {
        return false;
      }
    }
  }

  return stack.length === 0;
}
```
