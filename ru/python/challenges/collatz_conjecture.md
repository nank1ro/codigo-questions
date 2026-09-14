---
language: python
exerciseType: 1
difficulty: 1
title: Гипотеза Коллатца
---

# --description--

Гипотеза Коллатца начинается с любого положительного целого числа `n` и повторяет одно простое правило: если `n` чётное, разделите его пополам; если `n` нечётное, замените его на `3n + 1`. Рано или поздно последовательность достигает 1.

Например, если начать с 16, последовательность будет `16 -> 8 -> 4 -> 2 -> 1`, то есть потребуется 4 шага.

Никто никогда не доказывал, что это происходит всегда, но это выполняется для каждого проверенного числа.

# --instructions--

Напишите функцию `collatz_steps`, которая принимает положительное целое число `n` и возвращает количество шагов, необходимое, чтобы достичь 1.

`collatz_steps(1)` — это 0, потому что 1 уже является концом последовательности. `collatz_steps(12)` — это 9, а `collatz_steps(27)` — 111.

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

`collatz_steps(1)` должна возвращать 0, потому что 1 уже является концом последовательности.

```python
    def test1(self):
        self.assertEqual(collatz_steps(1), 0, "--err-t1--")
```

`collatz_steps(2)` должна возвращать 1.

```python
    def test2(self):
        self.assertEqual(collatz_steps(2), 1, "--err-t2--")
```

`collatz_steps(6)` должна возвращать 8.

```python
    def test3(self):
        self.assertEqual(collatz_steps(6), 8, "--err-t3--")
```

`collatz_steps(7)` должна возвращать 16.

```python
    def test4(self):
        self.assertEqual(collatz_steps(7), 16, "--err-t4--")
```

`collatz_steps(16)` должна возвращать 4.

```python
    def test5(self):
        self.assertEqual(collatz_steps(16), 4, "--err-t5--")
```

`collatz_steps(12)` должна возвращать 9.

```python
    def test6(self):
        self.assertEqual(collatz_steps(12), 9, "--err-t6--")
```

`collatz_steps(27)` должна возвращать 111.

```python
    def test7(self):
        self.assertEqual(collatz_steps(27), 111, "--err-t7--")
```

`collatz_steps(97)` должна возвращать 118.

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
