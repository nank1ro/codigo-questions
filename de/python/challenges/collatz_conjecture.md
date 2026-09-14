---
language: python
exerciseType: 1
difficulty: 1
title: Collatz-Vermutung
---

# --description--

Die Collatz-Vermutung startet von einer beliebigen positiven ganzen Zahl `n` und wiederholt eine einfache Regel: Ist `n` gerade, wird es halbiert; ist `n` ungerade, wird es durch `3n + 1` ersetzt. Früher oder später erreicht die Folge die 1.

Startet man zum Beispiel bei 16, lautet die Folge `16 -> 8 -> 4 -> 2 -> 1`, sie benötigt also 4 Schritte.

Niemand hat je bewiesen, dass das immer geschieht, aber es gilt für jede bisher getestete Zahl.

# --instructions--

Schreiben Sie eine Funktion `collatz_steps`, die eine positive ganze Zahl `n` nimmt und die Anzahl der Schritte zurückgibt, die benötigt werden, um 1 zu erreichen.

`collatz_steps(1)` ist 0, weil 1 bereits das Ende der Folge ist. `collatz_steps(12)` ist 9, und `collatz_steps(27)` ist 111.

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

`collatz_steps(1)` sollte 0 zurückgeben, weil 1 bereits das Ende der Folge ist.

```python
    def test1(self):
        self.assertEqual(collatz_steps(1), 0, "--err-t1--")
```

`collatz_steps(2)` sollte 1 zurückgeben.

```python
    def test2(self):
        self.assertEqual(collatz_steps(2), 1, "--err-t2--")
```

`collatz_steps(6)` sollte 8 zurückgeben.

```python
    def test3(self):
        self.assertEqual(collatz_steps(6), 8, "--err-t3--")
```

`collatz_steps(7)` sollte 16 zurückgeben.

```python
    def test4(self):
        self.assertEqual(collatz_steps(7), 16, "--err-t4--")
```

`collatz_steps(16)` sollte 4 zurückgeben.

```python
    def test5(self):
        self.assertEqual(collatz_steps(16), 4, "--err-t5--")
```

`collatz_steps(12)` sollte 9 zurückgeben.

```python
    def test6(self):
        self.assertEqual(collatz_steps(12), 9, "--err-t6--")
```

`collatz_steps(27)` sollte 111 zurückgeben.

```python
    def test7(self):
        self.assertEqual(collatz_steps(27), 111, "--err-t7--")
```

`collatz_steps(97)` sollte 118 zurückgeben.

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
