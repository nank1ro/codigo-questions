---
language: python
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James想从ATM取N美元。
ATM只有在N是5的倍数且James的账户有足够的现金来完成取款交易（包括银行手续费）时才会接受交易。
每次成功取款，银行收取 `0.50$` 的手续费。
计算一次取款尝试后James的账户余额。
输入按以下顺序给出：
1. James希望取出的现金金额在以下范围内：`0 < N <= 2000`。
2. James的初始余额精确到两位小数，范围如下：`0 < B <= 2000`。

# --instructions--

返回取款尝试后的账户余额，精确到两位小数。
如果账户中没有足够的资金来完成交易，则返回当前银行余额。

# --seed--

```python
def account_balance():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

执行一次成功的交易

```python
    def test_successful_transaction(self):
        self.assertEqual(account_balance(50, 120.00), 69.50, "--err-t1--")
```

余额不足

```python
    def test_insufficient_funds(self):
        self.assertEqual(account_balance(200, 120.00), 120.00, "--err-t2--")
```

交易被拒绝，金额无效

```python
    def test_not_multiple_of_5(self):
        self.assertEqual(account_balance(22, 120.00), 120.00, "--err-t3--")
```

成功取出所有资金

```python
    def test_withdraw_all(self):
        self.assertEqual(account_balance(95, 95.50), 0.00, "--err-t4--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def account_balance(withdraw, balance):
    if (withdraw % 5 == 0) and (balance >= (withdraw + 0.50)):
        return balance - withdraw - 0.50
    return balance
```
