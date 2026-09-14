---
language: javascript
exerciseType: 1
difficulty: 1
title: पैनग्राम
---

# --description--

पैनग्राम एक ऐसा वाक्य है जो अंग्रेजी वर्णमाला के हर अक्षर का कम से कम एक बार उपयोग करता है। सबसे प्रसिद्ध उदाहरण "the quick brown fox jumps over the lazy dog" है, जो सभी 26 अक्षरों को नौ छोटे शब्दों में समा लेता है।

यह जाँच अक्षरों के बड़े या छोटे होने का अंतर नहीं करती, इसलिए `A` और `a` एक ही अक्षर गिने जाते हैं। अंक, विराम चिह्न और रिक्त स्थान अनदेखे किए जाते हैं: वे अक्षर नहीं हैं, लेकिन वे किसी वाक्य को अस्वीकार करने का कारण भी नहीं हैं।

# --instructions--

एक फ़ंक्शन `isPangram` लिखें जो एक वाक्य लेता है और यदि वाक्य पैनग्राम है तो `true` लौटाता है, अन्यथा `false` लौटाता है।

उदाहरण:
```
isPangram("the quick brown fox jumps over the lazy dog") ➞ true
isPangram("the five boxing wizards jump quickly") ➞ true
isPangram("a quick movement of the enemy will jeopardize five gunboats") ➞ false
```

- खाली वाक्य पैनग्राम नहीं है।
- केवल `a` से `z` तक के 26 अक्षर गिने जाते हैं।

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
function isPangram(sentence) {
  
}
```

# --asserts--

खाली वाक्य पैनग्राम नहीं है

```javascript
tryCatch(isPangram("") === false);
```

क्लासिक वाक्य "the quick brown fox jumps over the lazy dog" एक पैनग्राम है

```javascript
tryCatch(isPangram("the quick brown fox jumps over the lazy dog") === true);
```

जिस वाक्य में अक्षर `x` नहीं है वह पैनग्राम नहीं है

```javascript
tryCatch(isPangram("a quick movement of the enemy will jeopardize five gunboats") === false);
```

वाक्य "the five boxing wizards jump quickly" एक पैनग्राम है

```javascript
tryCatch(isPangram("the five boxing wizards jump quickly") === true);
```

अंडरस्कोर अनदेखे किए जाते हैं, इसलिए वाक्य फिर भी पैनग्राम है

```javascript
tryCatch(isPangram("the_quick_brown_fox_jumps_over_the_lazy_dog") === true);
```

अंक अनदेखे किए जाते हैं, इसलिए वाक्य फिर भी पैनग्राम है

```javascript
tryCatch(isPangram("the 1 quick brown fox jumps over the 2 lazy dogs") === true);
```

अंक अक्षरों `e`, `i` और `t` की जगह नहीं लेते

```javascript
tryCatch(isPangram("7h3 qu1ck brown fox jumps ov3r 7h3 lazy dog") === false);
```

बड़े अक्षरों में लिखा वाक्य भी पैनग्राम है

```javascript
tryCatch(isPangram("THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG") === true);
```

वर्णमाला के एक ही आधे हिस्से के बड़े और छोटे अक्षर मिलाना पर्याप्त नहीं है

```javascript
tryCatch(isPangram("abcdefghijklm ABCDEFGHIJKLM") === false);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function isPangram(sentence) {
  const letters = new Set();

  for (const char of sentence.toLowerCase()) {
    if (char >= "a" && char <= "z") {
      letters.add(char);
    }
  }

  return letters.size === 26;
}
```
