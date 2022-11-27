---
language: python
exerciseType: 1
title: Funzione di Ackermann
difficulty: 1
---

# --description--

La funzione Ackermann è un classico esempio di funzione ricorsiva, nota soprattutto perché non è una funzione ricorsiva primitiva. Cresce molto rapidamente in valore, così come la dimensione delle chiamate.

La funzione Ackermann è solitamente definita come segue:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

La funzione termina sempre e i suoi argomenti non sono mai negativi

# --instructions--

Scrivi una funzione che restituisca il valore della funzione Ackermann.

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

`ack(0, 0)` deve restituire 1.

```python
    def test1(self):
        self.assertEqual(ack(0, 0), 1, "--err-t1--")
```

`ack(1, 1)` deve restituire 3.

```python
    def test2(self):
        self.assertEqual(ack(1, 1), 3, "--err-t2--")
```

`ack(2, 5)` deve restituire 13.

```python
    def test3(self):
        self.assertEqual(ack(2, 5), 13, "--err-t3--")
```

`ack(3, 3)` deve restituire 61.

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
