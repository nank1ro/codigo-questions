---
language: javascript
exerciseType: 1
difficulty: 2
title: घड़ी
---

# --description--

24 घंटे की घड़ी दिन के समय को `HH:MM` के रूप में दिखाती है, जो आधी रात के ठीक बाद `00:00` से शुरू होती है और अगली आधी रात से एक मिनट पहले `23:59` पर समाप्त होती है। दोनों भाग हमेशा दो अंकों में लिखे जाते हैं, इसलिए सुबह ग्यारह बजकर नौ मिनट को `11:09` पढ़ा जाता है।

एक पूरे दिन में 1440 मिनट होते हैं। जैसे ही घड़ी `23:59` से आगे निकलती है, वह `00:00` पर लौट आती है और दिन को फिर से शुरू करती है, और इसे `00:00` से पीछे की ओर घुमाने पर `23:59` पर पहुँचती है।

# --instructions--

एक फ़ंक्शन `clockTime` लिखें जो दो पूर्ण संख्याएं, `hours` और `minutes`, लेता है और 24 घंटे की घड़ी का समय `"HH:MM"` स्ट्रिंग के रूप में लौटाता है, जिसमें दोनों भाग दो अंकों तक पैड किए गए होते हैं।

उदाहरण:
```
clockTime(8, 0) ➞ "08:00"
clockTime(25, 160) ➞ "03:40"
clockTime(-1, 15) ➞ "23:15"
```

- कोई भी संख्या ऋणात्मक हो सकती है, या किसी असली घड़ी की अनुमति से बड़ी हो सकती है।
- मिनटों की कुल संख्या `hours * 60 + minutes` के रूप में निकालें, फिर उस कुल को `0` से `1439` की सीमा में लपेटें ताकि घड़ी दोनों दिशाओं में घूम जाए।
- `clockTime(24, 0)` ठीक एक पूरा दिन है, इसलिए उसे `"00:00"` पढ़ा जाता है।

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
function clockTime(hours, minutes) {
  
}
```

# --asserts--

सुबह के आठ बजे को `08:00` पढ़ा जाता है

```javascript
tryCatch(clockTime(8, 0) === "08:00");
```

एकल अंक दो अंकों तक पैड किए जाते हैं, इसलिए ग्यारह बजकर नौ मिनट को `11:09` पढ़ा जाता है

```javascript
tryCatch(clockTime(11, 9) === "11:09");
```

पूरे एक दिन के घंटे `00:00` पर घूम जाते हैं

```javascript
tryCatch(clockTime(24, 0) === "00:00");
```

60 से अधिक मिनट घंटों में जुड़ जाते हैं

```javascript
tryCatch(clockTime(25, 160) === "03:40");
```

ऋणात्मक घंटा घड़ी को आधी रात से पीछे की ओर घुमा देता है

```javascript
tryCatch(clockTime(-1, 15) === "23:15");
```

ऋणात्मक मिनट गिनती भी घड़ी को पीछे की ओर घुमा देती है

```javascript
tryCatch(clockTime(0, -90) === "22:30");
```

एक पूरे दिन से अधिक पीछे जाने पर भी घड़ी घूमती रहती है

```javascript
tryCatch(clockTime(-25, 0) === "23:00");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function clockTime(hours, minutes) {
  // % बाएं ऑपरेंड का चिह्न रखता है, इसलिए 0..1439 में पहुँचने के लिए
  // एक पूरा दिन जोड़ें और फिर दोबारा लपेटें।
  const total = (((hours * 60 + minutes) % 1440) + 1440) % 1440;

  const hh = String(Math.floor(total / 60)).padStart(2, "0");
  const mm = String(total % 60).padStart(2, "0");
  return `${hh}:${mm}`;
}
```
