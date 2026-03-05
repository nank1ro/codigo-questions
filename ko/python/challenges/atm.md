---
language: python
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James는 ATM에서 N달러를 인출하고 싶습니다.
현금 인출기는 N이 5의 배수이고, James의 계좌에 인출 거래를 수행하기에 충분한 현금(은행 수수료 포함)이 있는 경우에만 거래를 승인합니다.
성공적인 인출마다 은행은 `0.50$`를 수수료로 부과합니다.
인출 시도 후 James의 계좌 잔액을 계산하세요.
입력은 다음 순서로 주어집니다:
1. James가 인출하고자 하는 현금 금액은 다음 범위에 있습니다: `0 < N <= 2000`.
2. James의 초기 잔액은 소수점 두 자리로 주어지며 다음 범위에 있습니다: `0 < B <= 2000`.

# --instructions--

인출 시도 후의 계좌 잔액을 소수점 두 자리 숫자로 반환하세요.
계좌에 거래를 완료하기에 충분한 돈이 없는 경우, 현재 은행 잔액을 반환하세요.

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

성공적인 거래를 수행합니다

```python
    def test_successful_transaction(self):
        self.assertEqual(account_balance(50, 120.00), 69.50, "--err-t1--")
```

잔액이 부족합니다

```python
    def test_insufficient_funds(self):
        self.assertEqual(account_balance(200, 120.00), 120.00, "--err-t2--")
```

거래 거부, 유효하지 않은 금액입니다

```python
    def test_not_multiple_of_5(self):
        self.assertEqual(account_balance(22, 120.00), 120.00, "--err-t3--")
```

모든 금액을 성공적으로 인출합니다

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
