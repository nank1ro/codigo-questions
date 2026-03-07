---
language: python
exerciseType: 1
title: Funkcja Ackermanna
difficulty: 1
---

# --description--

Funkcja Ackermanna jest klasycznym przykładem funkcji rekurencyjnej, godnym uwagi zwłaszcza dlatego, że nie jest funkcją prymitywnie rekurencyjną. Jej wartości rosną bardzo szybko, podobnie jak rozmiar jej drzewa wywołań.

Funkcja Ackermanna jest zazwyczaj definiowana następująco:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Jej argumenty nigdy nie są ujemne i zawsze kończy działanie

# --instructions--

Napisz funkcję, która zwraca wartość funkcji Ackermanna.

# --seed--

```python
def ack(m, n):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

`ack(0, 0)` powinno zwrócić 1.

```python
    def test1(self):
        self.assertEqual(ack(0, 0), 1, "--err-t1--")
```

`ack(1, 1)` powinno zwrócić 3.

```python
    def test2(self):
        self.assertEqual(ack(1, 1), 3, "--err-t2--")
```

`ack(2, 5)` powinno zwrócić 13.

```python
    def test3(self):
        self.assertEqual(ack(2, 5), 13, "--err-t3--")
```

`ack(3, 3)` powinno zwrócić 61.

```python
    def test4(self):
        self.assertEqual(ack(3, 3), 61, "--err-t4--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def ack(m, n):
    if m == 0:
        return n + 1
    else:
        if (n == 0):
            return ack(m - 1, 1)
        return ack(m - 1, ack(m, n - 1))
```
