---
language: javascript
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James想从ATM取款N美元。
ATM只有在N是5的倍数且James的账户有足够的现金来执行取款交易（包括银行手续费）时才会接受交易。
每次成功取款，银行收取 `0.50$` 的手续费。
计算尝试交易后James的账户余额。
输入按以下顺序：
1. James希望取款的金额范围为：`0 < N <= 2000`。
2. James的初始余额精确到两位小数，范围为：`0 < B <= 2000`。

# --instructions--

返回尝试交易后的账户余额，以两位小数精度的数字表示。
如果账户中没有足够的钱来完成交易，则返回当前银行余额。

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

执行一次成功的交易

```javascript
tryCatch(accountBalance(50, 120.00) === 69.50);
```

余额不足

```javascript
tryCatch(accountBalance(200, 120.00) === 120.00);
```

交易被拒绝，金额无效

```javascript
tryCatch(accountBalance(22, 120.00) === 120.00);
```

成功取出所有金额

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
