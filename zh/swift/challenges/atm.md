---
language: swift
exerciseType: 1
difficulty: 1
title: "ATM"
---

# --description--

James 想从 ATM 取款 N 美元。
取款机只有在 N 是 5 的倍数且 James 的账户有足够的现金来执行取款交易（包括银行手续费）时才会接受交易。
每次成功取款，银行收取 `0.50$` 的手续费。
计算 James 尝试交易后的账户余额。
输入按以下顺序排列：
1. James 希望取款的金额范围为：`0 < N <= 2000`。
2. James 的初始余额精确到两位小数，范围为：`0 < B <= 2000`。

# --instructions--

返回尝试交易后的账户余额，精确到两位小数。
如果账户中没有足够的资金完成交易，返回当前银行余额。

> 提示：使用 `_`（下划线）省略参数标签

函数调用示例：
```swift
print(accountBalance(10, 20))
// prints 9,5
```

# --before-seed--

```swift
// DO NOT EDIT FROM HERE
import Foundation

var _testCount = 0
var _testFailedCount = 0
func tryCatch(_ assertion: Bool) {
    _testCount += 1
    if !assertion {
        _testFailedCount += 1
        print("Test Case '--err-t\(_testCount)--' failed")
    }
}
// DO NOT EDIT UNTIL HERE
```

# --seed--

```swift
func accountBalance() -> Double {
    return
}
```

# --asserts--

执行一次成功的交易

```swift
do {
    let expected: Double = 69.50
    tryCatch(accountBalance(50, 120.00) == expected)
}
```

资金不足

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(200, 120.00) == expected)
}
```

拒绝交易，金额无效

```swift
do {
    let expected: Double = 120.00
    tryCatch(accountBalance(22, 120.00) == expected)
}
```

成功取出所有资金

```swift
do {
    let expected: Double = 0.00
    tryCatch(accountBalance(95, 95.50) == expected)
}
```

# --after-asserts--

```swift
print("Executed \(_testCount) tests, with \(_testFailedCount) failures")
```
# --solutions--

```swift
func accountBalance(_ withdraw: Double,_ balance: Double) -> Double {
    let isMultipleOf5 = withdraw.truncatingRemainder(dividingBy: 5) == 0;
    let isAmountAvailable = balance >= (withdraw + 0.50)
    if isMultipleOf5 && isAmountAvailable {
        return balance - withdraw - 0.50
    }
    return balance
}
```
