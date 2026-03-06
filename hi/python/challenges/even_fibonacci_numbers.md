---
language: python
exerciseType: 1
difficulty: 1
title: सम फिबोनाची संख्याएं
---

# --description--

फिबोनाची अनुक्रम में प्रत्येक नया पद पिछले दो पदों को जोड़कर उत्पन्न किया जाता है। 1 और 2 से शुरू करते हुए, पहले 10 पद होंगे: `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

फिबोनाची अनुक्रम में उन पदों पर विचार करते हुए जिनके मान `n` से अधिक नहीं हैं, सम-मान वाले पदों का योग ज्ञात करें।

# --seed--

```python
def fibonacci_even_sum(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

आपके फ़ंक्शन को एक सम मान लौटाना चाहिए

```python
    def test1(self):
        self.assertEqual(fibonacci_even_sum(10) % 2, 0, "--err-t1--")
```

`fibonacci_even_sum(8)` को 10 लौटाना चाहिए

```python
    def test2(self):
        self.assertEqual(fibonacci_even_sum(8), 10, "--err-t2--")
```


`fibonacci_even_sum(10)` को 10 लौटाना चाहिए

```python
    def test3(self):
        self.assertEqual(fibonacci_even_sum(10), 10, "--err-t3--")
```

`fibonacci_even_sum(34)` को 44 लौटाना चाहिए

```python
    def test4(self):
        self.assertEqual(fibonacci_even_sum(34), 44, "--err-t4--")
```

`fibonacci_even_sum(60)` को 44 लौटाना चाहिए

```python
    def test5(self):
        self.assertEqual(fibonacci_even_sum(60), 44, "--err-t5--")
```

`fibonacci_even_sum(1000)` को 798 लौटाना चाहिए

```python
    def test6(self):
        self.assertEqual(fibonacci_even_sum(1000), 798, "--err-t6--")
```

`fibonacci_even_sum(100000)` को 60696 लौटाना चाहिए

```python
    def test7(self):
        self.assertEqual(fibonacci_even_sum(100000), 60696, "--err-t7--")
```

`fibonacci_even_sum(4000000)` को 4613732 लौटाना चाहिए

```python
    def test8(self):
        self.assertEqual(fibonacci_even_sum(4000000), 4613732, "--err-t8--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def fibonacci_even_sum(number):
    if number <= 1:
        return 0
    even_sum = 0
    prev_fib_num = 1
    fib_num = 2
    while fib_num <= number:
        if fib_num % 2 == 0:
            even_sum += fib_num
        prev_fib_num, fib_num = fib_num, prev_fib_num + fib_num
    return even_sum
```
