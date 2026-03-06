---
language: javascript
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

जेम्स एक ATM से N डॉलर निकालना चाहता है।
कैश मशीन लेनदेन तभी स्वीकार करेगी जब N 5 का गुणज हो, और जेम्स के खाते में निकासी लेनदेन करने के लिए पर्याप्त नकदी हो (बैंक शुल्क सहित)।
प्रत्येक सफल निकासी के लिए बैंक `0.50$` शुल्क लेता है।
एक प्रयास किए गए लेनदेन के बाद जेम्स के खाते की शेष राशि की गणना करें।
इनपुट निम्नलिखित क्रम में हैं:
1. जेम्स जितनी नकदी निकालना चाहता है वह निम्नलिखित सीमा में है: `0 < N <= 2000`।
2. जेम्स की प्रारंभिक शेष राशि दो दशमलव अंकों की सटीकता के साथ दी गई है और निम्नलिखित सीमा में है: `0 < B <= 2000`।

# --instructions--

प्रयास किए गए लेनदेन के बाद खाते की शेष राशि लौटाएँ, जो दो दशमलव अंकों की सटीकता वाली संख्या के रूप में दी गई हो।
यदि खाते में लेनदेन पूरा करने के लिए पर्याप्त धन नहीं है, तो वर्तमान बैंक शेष राशि लौटाएँ।

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
function accountBalance() {
  
}
```

# --asserts--

एक सफल लेनदेन करें

```javascript
tryCatch(accountBalance(50, 120.00) === 69.50);
```

अपर्याप्त धनराशि

```javascript
tryCatch(accountBalance(200, 120.00) === 120.00);
```

अस्वीकृत लेनदेन, अमान्य राशि

```javascript
tryCatch(accountBalance(22, 120.00) === 120.00);
```

सारा पैसा सफलतापूर्वक निकालें

```javascript
tryCatch(accountBalance(95, 95.50) === 0.00);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function accountBalance(withdraw, balance) {
  if ((withdraw % 5 == 0) && (balance >= (withdraw + 0.50))) {
    return balance - withdraw - 0.50;
  }
  return balance;
}
```
