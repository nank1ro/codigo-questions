---
language: javascript
exerciseType: 1
difficulty: 1
title: 아커만 함수
---

# --description--

아커만 함수는 재귀 함수의 고전적인 예로, 특히 원시 재귀 함수가 아니라는 점에서 주목할 만합니다. 값이 매우 빠르게 증가하며, 호출 트리의 크기도 마찬가지입니다.

아커만 함수는 일반적으로 다음과 같이 정의됩니다:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

인수는 절대 음수가 아니며 항상 종료됩니다.

# --instructions--

아커만 함수의 값을 반환하는 함수를 작성하세요.

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
function ack(m, n) {
    
}
```

# --asserts--

`ack(0, 0)`은 1을 반환해야 합니다.

```javascript
tryCatch(ack(0, 0) === 1);
```

`ack(1, 1)`은 3을 반환해야 합니다.

```javascript
tryCatch(ack(1, 1) === 3);
```

`ack(2, 5)`은 13을 반환해야 합니다.

```javascript
tryCatch(ack(2, 5) === 13);
```

`ack(3, 3)`은 61을 반환해야 합니다.

```javascript
tryCatch(ack(3, 3) === 61);
```

# --after-asserts--

```javascript
// DO NOT EDIT FROM HERE 
console.log(`Executed ${_testCount} tests, with ${_testFailedCount} failures`);
// DO NOT EDIT UNTIL HERE
```

# --solutions--

```javascript
function ack(m, n) {
    return m == 0 ?
      n + 1 :
      ack(m - 1, n == 0 ?
        1 :
        ack(m, n - 1))
}
```
