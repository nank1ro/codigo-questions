---
language: python
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Jeder neue Term in der Fibonacci-Sequenz wird durch Addition der beiden vorherigen Terme erzeugt. Beginnend mit 1 und 2 sind die ersten 10 Terme: `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

Wenn Sie die Terme in der Fibonacci-Sequenz betrachten, deren Werte `n` nicht überschreiten, finden Sie die Summe der geraden Terme.

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

Ihre Funktion sollte einen geraden Wert zurückgeben

```python
    def test1(self):
        self.assertEqual(fibonacci_even_sum(10) % 2, 0, "--err-t1--")
```

`fibonacci_even_sum(8)` sollte 10 zurückgeben

```python
    def test2(self):
        self.assertEqual(fibonacci_even_sum(8), 10, "--err-t2--")
```


`fibonacci_even_sum(10)` sollte 10 zurückgeben

```python
    def test3(self):
        self.assertEqual(fibonacci_even_sum(10), 10, "--err-t3--")
```

`fibonacci_even_sum(34)` sollte 44 zurückgeben

```python
    def test4(self):
        self.assertEqual(fibonacci_even_sum(34), 44, "--err-t4--")
```

`fibonacci_even_sum(60)` sollte 44 zurückgeben

```python
    def test5(self):
        self.assertEqual(fibonacci_even_sum(60), 44, "--err-t5--")
```

`fibonacci_even_sum(1000)` sollte 798 zurückgeben

```python
    def test6(self):
        self.assertEqual(fibonacci_even_sum(1000), 798, "--err-t6--")
```

`fibonacci_even_sum(100000)` sollte 60696 zurückgeben

```python
    def test7(self):
        self.assertEqual(fibonacci_even_sum(100000), 60696, "--err-t7--")
```

`fibonacci_even_sum(4000000)` sollte 4613732 zurückgeben

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
