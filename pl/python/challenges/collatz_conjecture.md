---
language: python
exerciseType: 1
difficulty: 1
title: Hipoteza Collatza
---

# --description--

Hipoteza Collatza zaczyna się od dowolnej dodatniej liczby całkowitej `n` i powtarza jedną prostą regułę: jeśli `n` jest parzyste, dzielimy je na pół; jeśli `n` jest nieparzyste, zastępujemy je wartością `3n + 1`. Prędzej czy później ciąg osiąga 1.

Na przykład ciąg zaczynający się od 16 to `16 -> 8 -> 4 -> 2 -> 1`, więc zajmuje to 4 kroki.

Nikt nigdy nie udowodnił, że zawsze tak się dzieje, ale reguła ta obowiązuje dla każdej dotychczas przetestowanej liczby.

# --instructions--

Napisz funkcję `collatz_steps`, która przyjmuje dodatnią liczbę całkowitą `n` i zwraca liczbę kroków potrzebnych do osiągnięcia 1.

`collatz_steps(1)` to 0, ponieważ 1 to już koniec ciągu. `collatz_steps(12)` to 9, a `collatz_steps(27)` to 111.

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

`collatz_steps(1)` powinno zwrócić 0, ponieważ 1 to już koniec ciągu.

```python
    def test1(self):
        self.assertEqual(collatz_steps(1), 0, "--err-t1--")
```

`collatz_steps(2)` powinno zwrócić 1.

```python
    def test2(self):
        self.assertEqual(collatz_steps(2), 1, "--err-t2--")
```

`collatz_steps(6)` powinno zwrócić 8.

```python
    def test3(self):
        self.assertEqual(collatz_steps(6), 8, "--err-t3--")
```

`collatz_steps(7)` powinno zwrócić 16.

```python
    def test4(self):
        self.assertEqual(collatz_steps(7), 16, "--err-t4--")
```

`collatz_steps(16)` powinno zwrócić 4.

```python
    def test5(self):
        self.assertEqual(collatz_steps(16), 4, "--err-t5--")
```

`collatz_steps(12)` powinno zwrócić 9.

```python
    def test6(self):
        self.assertEqual(collatz_steps(12), 9, "--err-t6--")
```

`collatz_steps(27)` powinno zwrócić 111.

```python
    def test7(self):
        self.assertEqual(collatz_steps(27), 111, "--err-t7--")
```

`collatz_steps(97)` powinno zwrócić 118.

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
