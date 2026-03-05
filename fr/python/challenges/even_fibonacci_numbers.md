---
language: python
exerciseType: 1
difficulty: 1
title: Nombres pairs de Fibonacci
---

# --description--

Chaque nouveau terme de la séquence de Fibonacci est généré en ajoutant les deux termes précédents. En commençant par 1 et 2, les 10 premiers termes seront: `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

En considérant les termes de la séquence de Fibonacci dont les valeurs ne dépassent pas `n`, trouvez la somme des termes de valeur paire.

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

Your function should return an even value

```python
    def test1(self):
        self.assertEqual(fibonacci_even_sum(10) % 2, 0, "--err-t1--")
```

`fibonacci_even_sum(8)` should return 10

```python
    def test2(self):
        self.assertEqual(fibonacci_even_sum(8), 10, "--err-t2--")
```


`fibonacci_even_sum(10)` should return 10

```python
    def test3(self):
        self.assertEqual(fibonacci_even_sum(10), 10, "--err-t3--")
```

`fibonacci_even_sum(34)` should return 44

```python
    def test4(self):
        self.assertEqual(fibonacci_even_sum(34), 44, "--err-t4--")
```

`fibonacci_even_sum(60)` should return 44

```python
    def test5(self):
        self.assertEqual(fibonacci_even_sum(60), 44, "--err-t5--")
```

`fibonacci_even_sum(1000)` should return 798

```python
    def test6(self):
        self.assertEqual(fibonacci_even_sum(1000), 798, "--err-t6--")
```

`fibonacci_even_sum(100000)` should return 60696

```python
    def test7(self):
        self.assertEqual(fibonacci_even_sum(100000), 60696, "--err-t7--")
```

`fibonacci_even_sum(4000000)` should return 4613732

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
