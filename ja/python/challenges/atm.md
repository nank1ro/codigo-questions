---
language: python
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

ジェームズはATMからN ドルを引き出したいと思っています。
ATMは、Nが5の倍数であり、ジェームズの口座に引き出し取引を実行するのに十分な現金がある場合（銀行手数料を含む）にのみ取引を受け付けます。
引き出しが成功するたびに、銀行は`0.50$`の手数料を請求します。
引き出し取引を試みた後のジェームズの口座残高を計算してください。
入力は以下の順序です：
1. ジェームズが引き出したい現金の額は次の範囲です：`0 < N <= 2000`。
2. ジェームズの初期残高は小数点以下2桁で与えられ、次の範囲です：`0 < B <= 2000`。

# --instructions--

取引を試みた後の口座残高を、小数点以下2桁の数値として返してください。
取引を完了するのに十分な金額が口座にない場合は、現在の口座残高を返してください。

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

取引の成功

```python
    def test_successful_transaction(self):
        self.assertEqual(account_balance(50, 120.00), 69.50, "--err-t1--")
```

残高不足

```python
    def test_insufficient_funds(self):
        self.assertEqual(account_balance(200, 120.00), 120.00, "--err-t2--")
```

取引拒否、無効な金額

```python
    def test_not_multiple_of_5(self):
        self.assertEqual(account_balance(22, 120.00), 120.00, "--err-t3--")
```

全額の引き出し成功

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
