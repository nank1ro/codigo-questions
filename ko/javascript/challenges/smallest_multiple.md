---
language: javascript
exerciseType: 1
difficulty: 1
title: 최소 공배수
---

# --description--

2520은 1부터 10까지의 각 숫자로 나머지 없이 나눌 수 있는 가장 작은 숫자입니다.

# --instructions--

1부터 `n`까지의 모든 숫자로 균등하게 나눌 수 있는 가장 작은 양의 정수는 무엇입니까?

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
function smallestMultiple(n) {
  
}
```

# --asserts--

`smallestMultiple(5)`는 60을 반환해야 합니다.

```javascript
tryCatch(smallestMultiple(5) === 60);
```

`smallestMultiple(7)`는 420을 반환해야 합니다.

```javascript
tryCatch(smallestMultiple(7) === 420);
```

`smallestMultiple(10)`은 2520을 반환해야 합니다.

```javascript
tryCatch(smallestMultiple(10) === 2520);
```

`smallestMultiple(13)`은 360360을 반환해야 합니다.

```javascript
tryCatch(smallestMultiple(13) === 360360);
```

`smallestMultiple(20)`은 232792560을 반환해야 합니다.

```javascript
tryCatch(smallestMultiple(20) === 232792560);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function smallestMultiple(n){
  function gcd(a, b) {
    return b === 0 ? a : gcd(b, a%b); // Euclidean algorithm
  }

  function lcm(a, b) {
    return a * b / gcd(a, b);
  }
  var result = 1;
  for(var i = 2; i <= n; i++) {
    result = lcm(result, i);
  }
  return result;
}
```
