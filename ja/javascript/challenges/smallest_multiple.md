---
language: javascript
exerciseType: 1
difficulty: 1
title: 最小公倍数
---

# --description--

2520は1から10までのすべての数で余りなく割り切れる最小の数です。

# --instructions--

1から`n`までのすべての数で均等に割り切れる最小の正の数は何ですか？

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

`smallestMultiple(5)`は60を返すべきです。

```javascript
tryCatch(smallestMultiple(5) === 60);
```

`smallestMultiple(7)`は420を返すべきです。

```javascript
tryCatch(smallestMultiple(7) === 420);
```

`smallestMultiple(10)`は2520を返すべきです。

```javascript
tryCatch(smallestMultiple(10) === 2520);
```

`smallestMultiple(13)`は360360を返すべきです。

```javascript
tryCatch(smallestMultiple(13) === 360360);
```

`smallestMultiple(20)`は232792560を返すべきです。

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
