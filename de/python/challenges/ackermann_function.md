---
language: python
exerciseType: 1
title: Ackermann function
difficulty: 1
---

# --description--

Die Ackermann-Funktion ist ein klassisches Beispiel für eine rekursive Funktion, besonders bemerkenswert weil es keine primitive rekursive Funktion ist. Sie wächst sehr schnell im Wert, ebenso wie die Größe ihres Aufrufbaums.

Die Ackermann-Funktion ist normalerweise wie folgt definiert:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Ihre Argumente sind niemals negativ und sie endet immer

# --instructions--

Schreiben Sie eine Funktion, die den Wert der Ackermann-Funktion zurückgibt.

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

`ack(0, 0)` sollte 1 zurückgeben.

```python
    def test1(self):
        self.assertEqual(ack(0, 0), 1, "--err-t1--")
```

`ack(1, 1)` sollte 3 zurückgeben.

```python
    def test2(self):
        self.assertEqual(ack(1, 1), 3, "--err-t2--")
```

`ack(2, 5)` sollte 13 zurückgeben.

```python
    def test3(self):
        self.assertEqual(ack(2, 5), 13, "--err-t3--")
```

`ack(3, 3)` sollte 61 zurückgeben.

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
