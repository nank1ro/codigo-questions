---
language: python
exerciseType: 1
difficulty: 1
title: Menor múltiplo
---

# --description--

2520 é o menor número que pode ser dividido por cada um dos números de 1 a 10 sem nenhum resto.

# --instructions--

Qual é o menor número positivo que é divisível por todos os números de 1 a `n`?

# --seed--

```python
def smallest_multiple(n) {
  
}
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`smallest_multiple(5)` deve retornar 60.

```python
    def test1(self):
        self.assertEqual(smallest_multiple(5), 60, "--err-t1--")
```

`smallest_multiple(7)` deve retornar 420.

```python
    def test2(self):
        self.assertEqual(smallest_multiple(7), 420, "--err-t2--")
```

`smallest_multiple(10)` deve retornar 2520.

```python
    def test3(self):
        self.assertEqual(smallest_multiple(10), 2520, "--err-t3--")
```

`smallest_multiple(13)` deve retornar 360360.

```python
    def test4(self):
        self.assertEqual(smallest_multiple(13), 360360, "--err-t4--")
```

`smallest_multiple(20)` deve retornar 232792560.

```python
    def test5(self):
        self.assertEqual(smallest_multiple(20), 232792560, "--err-t5--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def smallest_multiple(n):
  def gcd(a, b):
    return a if b == 0 else gcd(b, a % b) # Euclidean algorithm

  def lcm(a, b):
    return a * b / gcd(a, b)

  result = 1
  for i in range(2, n+1):
    result = lcm(result, i)

  return result
```
