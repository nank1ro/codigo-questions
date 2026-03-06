---
language: python
exerciseType: 1
difficulty: 1
title: ATM
---

# --description--

James एक ATM से N डॉलर निकालना चाहता है।
कैश मशीन केवल तभी लेनदेन स्वीकार करेगी जब N, 5 का गुणज हो, और James के खाते में निकासी लेनदेन करने के लिए पर्याप्त नकदी हो (बैंक शुल्क सहित)।
प्रत्येक सफल निकासी के लिए बैंक `0.50$` शुल्क लेता है।
एक प्रयास किए गए लेनदेन के बाद James के खाते की शेष राशि की गणना करें।
इनपुट निम्नलिखित क्रम में हैं:
1. James जितनी नकदी निकालना चाहता है वह निम्नलिखित सीमा में है: `0 < N <= 2000`।
2. James की प्रारंभिक शेष राशि दो दशमलव अंकों की सटीकता के साथ दी गई है और निम्नलिखित सीमा में है: `0 < B <= 2000`।

# --instructions--

प्रयास किए गए लेनदेन के बाद खाते की शेष राशि लौटाएं, जो दो दशमलव अंकों की सटीकता वाली संख्या के रूप में दी गई हो।
यदि लेनदेन पूरा करने के लिए खाते में पर्याप्त धन नहीं है, तो वर्तमान बैंक शेष राशि लौटाएं।

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

एक सफल लेनदेन करें

```python
    def test_successful_transaction(self):
        self.assertEqual(account_balance(50, 120.00), 69.50, "--err-t1--")
```

अपर्याप्त धनराशि

```python
    def test_insufficient_funds(self):
        self.assertEqual(account_balance(200, 120.00), 120.00, "--err-t2--")
```

लेनदेन अस्वीकृत, अमान्य राशि

```python
    def test_not_multiple_of_5(self):
        self.assertEqual(account_balance(22, 120.00), 120.00, "--err-t3--")
```

सारा पैसा सफलतापूर्वक निकालें

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
