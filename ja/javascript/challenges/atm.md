---
language: javascript
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

ジェームズはATMからNドルを引き出したいと思っています。
ATMは、Nが5の倍数であり、ジェームズの口座に引き出し取引を行うのに十分な現金がある場合（銀行手数料を含む）にのみ取引を受け付けます。
引き出しが成功するたびに、銀行は`0.50$`の手数料を請求します。
引き出し試行後のジェームズの口座残高を計算してください。
入力は以下の順序です：
1. ジェームズが引き出したい金額は以下の範囲です：`0 < N <= 2000`。
2. ジェームズの初期残高は小数点以下2桁で与えられ、以下の範囲です：`0 < B <= 2000`。

# --instructions--

引き出し試行後の口座残高を小数点以下2桁の数値として返してください。
口座に取引を完了するのに十分なお金がない場合は、現在の銀行残高を返してください。

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

取引が成功する場合

```javascript
tryCatch(accountBalance(50, 120.00) === 69.50);
```

残高不足

```javascript
tryCatch(accountBalance(200, 120.00) === 120.00);
```

取引拒否、無効な金額

```javascript
tryCatch(accountBalance(22, 120.00) === 120.00);
```

全額の引き出しに成功

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
