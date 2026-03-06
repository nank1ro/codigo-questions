---
language: javascript
exerciseType: 1
difficulty: 1
title: 3または5の倍数
---

# --description--

10未満の自然数のうち3または5の倍数を列挙すると、3、5、6、9が得られます。これらの倍数の合計は23です。

# --instructions--

指定されたパラメータ値`number`未満の3または5のすべての倍数の合計を求めてください。

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
function multiplesOf3and5(number) {
  
}
```

# --asserts--

`multiplesOf3and5(10)`は23を返すべきです。

```javascript
tryCatch(multiplesOf3and5(10) === 23);
```

`multiplesOf3and5(1000)`は233168を返すべきです。

```javascript
tryCatch(multiplesOf3and5(1000) === 233168);
```

`multiplesOf3and5(6987)`は11390208を返すべきです

```javascript
tryCatch(multiplesOf3and5(6987) === 11390208);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
const multiplesOf3and5 = (number) => {
  var total = 0;
  for(var i = 0; i < number; i++) {
    if(i % 3 == 0 || i % 5 == 0) {
      total += i;
    }
  }
  return total;
};
```
