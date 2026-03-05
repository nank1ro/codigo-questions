---
language: javascript
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James는 ATM에서 N달러를 인출하려고 합니다.
현금 인출기는 N이 5의 배수이고 James의 계좌에 인출 거래를 수행할 충분한 현금(은행 수수료 포함)이 있는 경우에만 거래를 수락합니다.
성공적인 인출마다 은행은 `0.50$`의 수수료를 부과합니다.
인출 시도 후 James의 계좌 잔액을 계산하세요.
입력은 다음 순서로 주어집니다:
1. James가 인출하려는 현금 금액은 다음 범위에 있습니다: `0 < N <= 2000`.
2. James의 초기 잔액은 소수점 이하 두 자리로 주어지며 다음 범위에 있습니다: `0 < B <= 2000`.

# --instructions--

인출 시도 후의 계좌 잔액을 소수점 이하 두 자리의 숫자로 반환하세요.
거래를 완료하기에 계좌에 충분한 돈이 없는 경우, 현재 은행 잔액을 반환하세요.

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

성공적인 거래를 수행합니다

```javascript
tryCatch(accountBalance(50, 120.00) === 69.50);
```

잔액이 부족합니다

```javascript
tryCatch(accountBalance(200, 120.00) === 120.00);
```

거래 거부, 유효하지 않은 금액

```javascript
tryCatch(accountBalance(22, 120.00) === 120.00);
```

모든 금액을 성공적으로 인출합니다

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
