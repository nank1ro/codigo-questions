---
language: python
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James would like to withdraw N dollars from an ATM.
The cash machine will only accept the transaction if N is a multiple of 5, and James' account has enough cash to perform the withdrawal transaction (including bank charges).
For each successful withdrawal the bank charges `0.50$`.
Calculate James' account balance after an attempted transaction.
The inputs are in the following order:
1. the amount of cash which James wishes to withdraw is in the following range: `0 < N <= 2000`.
2. James' initial balance is given with two digits of precision and is in the following range: `0 < B <= 2000`.

# --instructions--

Return the account balance after the attempted transaction, given as a number with two digits of precision.
If there is not enough money in the account to complete the transaction, return the current bank balance.

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

Perform a successful transaction

```python
    def test_successful_transaction(self):
        self.assertEqual(account_balance(50, 120.00), 69.50, "--err-t1--")
```

Insufficient funds

```python
    def test_insufficient_funds(self):
        self.assertEqual(account_balance(200, 120.00), 120.00, "--err-t2--")
```

Refused transaction, invalid amount

```python
    def test_not_multiple_of_5(self):
        self.assertEqual(account_balance(22, 120.00), 120.00, "--err-t3--")
```

Withdraw all money successfully

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
