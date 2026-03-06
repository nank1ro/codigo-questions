---
language: python
exerciseType: 1
title: FizzBuzz
difficulty: 1
---

# --description--

एक फ़ंक्शन बनाएं जो एक संख्या को आर्गुमेंट के रूप में लेता है और `"Fizz"`, `"Buzz"` या `"FizzBuzz"` लौटाता है।

# --instructions--

- यदि संख्या `3` का गुणज है तो आउटपुट `"Fizz"` होना चाहिए
- यदि दी गई संख्या `5` का गुणज है, तो आउटपुट `"Buzz"` होना चाहिए।
- यदि दी गई संख्या `3` और `5` दोनों का गुणज है, तो आउटपुट `"FizzBuzz"` होना चाहिए।
- यदि संख्या `3` या `5` में से किसी का भी गुणज नहीं है, तो संख्या को नीचे दिए गए उदाहरणों में दिखाए अनुसार अपने आप आउटपुट किया जाना चाहिए।
- आउटपुट हमेशा एक स्ट्रिंग होना चाहिए भले ही यह `3` या `5` का गुणज न हो।

उदाहरण:
```python
fizz_buzz(3) // ➞ "Fizz"
fizz_buzz(5) // ➞ "Buzz"
fizz_buzz(15) // ➞ "FizzBuzz"
fizz_buzz(4) // ➞ "4"
```

# --seed--

```python
def fizz_buzz():
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

संख्या `3` का परिणाम `"Fizz"` होना चाहिए

```python
    def test1(self):
        self.assertEqual(fizz_buzz(3), "Fizz", "--err-t1--")
```

संख्या `5` का परिणाम `"Buzz"` होना चाहिए

```python
    def test2(self):
        self.assertEqual(fizz_buzz(5), "Buzz", "--err-t2--")
```

संख्या `15` का परिणाम `"FizzBuzz"` होना चाहिए

```python
    def test3(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz", "--err-t3--")
```

संख्या `10` का परिणाम `"Buzz"` होना चाहिए

```python
    def test4(self):
        self.assertEqual(fizz_buzz(10), "Buzz", "--err-t4--")
```

संख्या `98` का परिणाम `"98"` होना चाहिए

```python
    def test5(self):
        self.assertEqual(fizz_buzz(98), "98", "--err-t5--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def fizz_buzz(number):
    if number % 3 == 0 and number % 5 == 0:
        return "FizzBuzz"
    if number % 3 == 0:
        return "Fizz"
    if number % 5 == 0:
        return "Buzz"
    return str(number)
```
