---
language: python
exerciseType: 1
difficulty: 1
title: Collatz conjecture
---

# --description--

The Collatz conjecture starts from any positive integer `n` and repeats one simple rule: if `n` is even, halve it; if `n` is odd, replace it with `3n + 1`. Sooner or later the sequence reaches 1.

For example, starting from 16 the sequence is `16 -> 8 -> 4 -> 2 -> 1`, so it takes 4 steps.

Nobody has ever proved that this always happens, but it holds for every number ever tested.

# --instructions--

Write a function `collatz_steps` that takes a positive integer `n` and returns the number of steps needed to reach 1.

`collatz_steps(1)` is 0, because 1 is already the end of the sequence. `collatz_steps(12)` is 9, and `collatz_steps(27)` is 111.

# --seed--

```python
def collatz_steps(n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`collatz_steps(1)` should return 0, because 1 is already the end of the sequence.

```python
    def test1(self):
        self.assertEqual(collatz_steps(1), 0, "--err-t1--")
```

`collatz_steps(2)` should return 1.

```python
    def test2(self):
        self.assertEqual(collatz_steps(2), 1, "--err-t2--")
```

`collatz_steps(6)` should return 8.

```python
    def test3(self):
        self.assertEqual(collatz_steps(6), 8, "--err-t3--")
```

`collatz_steps(7)` should return 16.

```python
    def test4(self):
        self.assertEqual(collatz_steps(7), 16, "--err-t4--")
```

`collatz_steps(16)` should return 4.

```python
    def test5(self):
        self.assertEqual(collatz_steps(16), 4, "--err-t5--")
```

`collatz_steps(12)` should return 9.

```python
    def test6(self):
        self.assertEqual(collatz_steps(12), 9, "--err-t6--")
```

`collatz_steps(27)` should return 111.

```python
    def test7(self):
        self.assertEqual(collatz_steps(27), 111, "--err-t7--")
```

`collatz_steps(97)` should return 118.

```python
    def test8(self):
        self.assertEqual(collatz_steps(97), 118, "--err-t8--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def collatz_steps(n):
    value = n
    steps = 0
    while value != 1:
        value = value // 2 if value % 2 == 0 else 3 * value + 1
        steps += 1
    return steps
```
