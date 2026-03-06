---
language: python
exerciseType: 1
difficulty: 1
title: フィボナッチ偶数
---

# --description--

フィボナッチ数列の各新しい項は、前の2つの項を足して生成されます。1と2から始めると、最初の10項は次のようになります：`1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

フィボナッチ数列の項のうち、値が`n`を超えないものについて、偶数値の項の合計を求めてください。

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

関数は偶数値を返すべきです

```python
    def test1(self):
        self.assertEqual(fibonacci_even_sum(10) % 2, 0, "--err-t1--")
```

`fibonacci_even_sum(8)`は10を返すべきです

```python
    def test2(self):
        self.assertEqual(fibonacci_even_sum(8), 10, "--err-t2--")
```


`fibonacci_even_sum(10)`は10を返すべきです

```python
    def test3(self):
        self.assertEqual(fibonacci_even_sum(10), 10, "--err-t3--")
```

`fibonacci_even_sum(34)`は44を返すべきです

```python
    def test4(self):
        self.assertEqual(fibonacci_even_sum(34), 44, "--err-t4--")
```

`fibonacci_even_sum(60)`は44を返すべきです

```python
    def test5(self):
        self.assertEqual(fibonacci_even_sum(60), 44, "--err-t5--")
```

`fibonacci_even_sum(1000)`は798を返すべきです

```python
    def test6(self):
        self.assertEqual(fibonacci_even_sum(1000), 798, "--err-t6--")
```

`fibonacci_even_sum(100000)`は60696を返すべきです

```python
    def test7(self):
        self.assertEqual(fibonacci_even_sum(100000), 60696, "--err-t7--")
```

`fibonacci_even_sum(4000000)`は4613732を返すべきです

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
