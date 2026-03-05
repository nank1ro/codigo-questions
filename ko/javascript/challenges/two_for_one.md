---
language: javascript
exerciseType: 1
difficulty: 1
title: 둘이서 하나
---

# --description--

이름이 주어지면 다음 메시지가 포함된 문자열을 반환하세요:
`One for X, one for me.`
여기서 `X`는 주어진 이름입니다.
그러나 이름이 없으면 다음 문자열을 반환하세요:
`One for you, one for me.`

# --instructions--

올바른 문자열을 반환하는 함수를 작성하세요. 예시:

**input**: `Walter`
**output**: `One for Walter, one for me.`

**input**:
**output**: `One for you, one for me.`

**input**: `David`
**output**: `One for David, one for me.`

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
function twoForOne() {
  
}
```

# --asserts--

이름이 주어지지 않은 경우

```javascript
tryCatch(twoForOne() === "One for you, one for me.");
```

이름으로 "James"를 전달합니다

```javascript
tryCatch(twoForOne("James") === "One for James, one for me.");
```

이름으로 "Martha"를 전달합니다

```javascript
tryCatch(twoForOne("Martha") === "One for Martha, one for me.");
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function twoForOne(name) {
  if (!name) return "One for you, one for me."
  return `One for ${name}, one for me.`
}
```
