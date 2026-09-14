---
language: python
exerciseType: 1
difficulty: 1
title: Congettura di Collatz
---

# --description--

La congettura di Collatz parte da un qualsiasi intero positivo `n` e ripete una semplice regola: se `n` è pari, si dimezza; se `n` è dispari, si sostituisce con `3n + 1`. Prima o poi la sequenza arriva a 1.

Per esempio, partendo da 16 la sequenza è `16 -> 8 -> 4 -> 2 -> 1`, quindi servono 4 passi.

Nessuno ha mai dimostrato che questo accada sempre, ma vale per ogni numero mai testato.

# --instructions--

Scrivi una funzione `collatz_steps` che riceve un intero positivo `n` e restituisce il numero di passi necessari per arrivare a 1.

`collatz_steps(1)` è 0, perché 1 è già la fine della sequenza. `collatz_steps(12)` è 9, e `collatz_steps(27)` è 111.

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

`collatz_steps(1)` deve restituire 0, perché 1 è già la fine della sequenza.

```python
    def test1(self):
        self.assertEqual(collatz_steps(1), 0, "--err-t1--")
```

`collatz_steps(2)` deve restituire 1.

```python
    def test2(self):
        self.assertEqual(collatz_steps(2), 1, "--err-t2--")
```

`collatz_steps(6)` deve restituire 8.

```python
    def test3(self):
        self.assertEqual(collatz_steps(6), 8, "--err-t3--")
```

`collatz_steps(7)` deve restituire 16.

```python
    def test4(self):
        self.assertEqual(collatz_steps(7), 16, "--err-t4--")
```

`collatz_steps(16)` deve restituire 4.

```python
    def test5(self):
        self.assertEqual(collatz_steps(16), 4, "--err-t5--")
```

`collatz_steps(12)` deve restituire 9.

```python
    def test6(self):
        self.assertEqual(collatz_steps(12), 9, "--err-t6--")
```

`collatz_steps(27)` deve restituire 111.

```python
    def test7(self):
        self.assertEqual(collatz_steps(27), 111, "--err-t7--")
```

`collatz_steps(97)` deve restituire 118.

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
