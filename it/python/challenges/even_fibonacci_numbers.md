---
language: python
exerciseType: 1
difficulty: 1
title: Even Fibonacci numbers
---

# --description--

Ogni nuovo termine della sequenza di Fibonacci viene generato sommando i due termini precedenti. Iniziando con 1 e 2, i primi 10 termini saranno: `1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...`

# --instructions--

Considerando i termini della sequenza di Fibonacci i cui valori non superano `n`, trova la somma dei termini con valore pari.

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

La tua funzione deve restituire un numero pari

```python
    def test1(self):
        self.assertEqual(fibonacci_even_sum(10) % 2, 0, "--err-t1--")
```

`fibonacci_even_sum(8)` deve restituire 10

```python
    def test2(self):
        self.assertEqual(fibonacci_even_sum(8), 10, "--err-t2--")
```


`fibonacci_even_sum(10)` deve restituire 10

```python
    def test3(self):
        self.assertEqual(fibonacci_even_sum(10), 10, "--err-t3--")
```

`fibonacci_even_sum(34)` deve restituire 44

```python
    def test4(self):
        self.assertEqual(fibonacci_even_sum(34), 44, "--err-t4--")
```

`fibonacci_even_sum(60)` deve restituire 44

```python
    def test5(self):
        self.assertEqual(fibonacci_even_sum(60), 44, "--err-t5--")
```

`fibonacci_even_sum(1000)` deve restituire 798

```python
    def test6(self):
        self.assertEqual(fibonacci_even_sum(1000), 798, "--err-t6--")
```

`fibonacci_even_sum(100000)` deve restituire 60696

```python
    def test7(self):
        self.assertEqual(fibonacci_even_sum(100000), 60696, "--err-t7--")
```

`fibonacci_even_sum(4000000)` deve restituire 4613732

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
