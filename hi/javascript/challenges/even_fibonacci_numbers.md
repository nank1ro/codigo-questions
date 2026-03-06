---
language: javascript
exerciseType: 1
difficulty: 1
title: सम फिबोनाची संख्याएँ
---

# --description--

फिबोनाची अनुक्रम में प्रत्येक नया पद पिछले दो पदों को जोड़कर उत्पन्न होता है। 1 और 2 से शुरू करते हुए, पहले 10 पद होंगे: `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

फिबोनाची अनुक्रम में उन पदों पर विचार करते हुए जिनके मान `n` से अधिक नहीं हैं, सम-मान वाले पदों का योग ज्ञात करें।

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
function fibonacciEvenSum(n) {
  
}
```

# --asserts--

आपके फ़ंक्शन को एक सम मान लौटाना चाहिए

```javascript
tryCatch(fibonacciEvenSum(10) % 2 === 0);
```

`fibonacciEvenSum(8)` को 10 लौटाना चाहिए

```javascript
tryCatch(fibonacciEvenSum(8) === 10);
```


`fibonacciEvenSum(10)` को 10 लौटाना चाहिए

```javascript
tryCatch(fibonacciEvenSum(10) === 10);
```

`fibonacciEvenSum(34)` को 44 लौटाना चाहिए

```javascript
tryCatch(fibonacciEvenSum(34) === 44);
```

`fibonacciEvenSum(60)` को 44 लौटाना चाहिए

```javascript
tryCatch(fibonacciEvenSum(60) === 44);
```

`fibonacciEvenSum(1000)` को 798 लौटाना चाहिए

```javascript
tryCatch(fibonacciEvenSum(1000) === 798);
```

`fibonacciEvenSum(100000)` को 60696 लौटाना चाहिए

```javascript
tryCatch(fibonacciEvenSum(100000) === 60696);
```

`fibonacciEvenSum(4000000)` को 4613732 लौटाना चाहिए

```javascript
tryCatch(fibonacciEvenSum(4000000) === 4613732);
```


# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
const fibonacciEvenSum = (number) => {
    if (number <= 1) {
        return 0;
    }
    let evenSum = 0,
      prevFibNum = 1,
      fibNum = 2;
    while (fibNum <= number) {
        if (fibNum % 2 == 0) {
            evenSum += fibNum;
        }
        [prevFibNum, fibNum] = [fibNum, prevFibNum + fibNum];
    }
    return evenSum;
};
```
