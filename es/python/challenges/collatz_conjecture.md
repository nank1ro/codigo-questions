---
language: python
exerciseType: 1
difficulty: 1
title: Conjetura de Collatz
---

# --description--

La conjetura de Collatz parte de cualquier entero positivo `n` y repite una única regla sencilla: si `n` es par, se reduce a la mitad; si `n` es impar, se sustituye por `3n + 1`. Tarde o temprano la sucesión llega a 1.

Por ejemplo, empezando en 16 la sucesión es `16 -> 8 -> 4 -> 2 -> 1`, así que se necesitan 4 pasos.

Nadie ha demostrado jamás que esto ocurra siempre, pero se cumple para todos los números probados hasta ahora.

# --instructions--

Escribe una función `collatz_steps` que reciba un entero positivo `n` y devuelva el número de pasos necesarios para llegar a 1.

`collatz_steps(1)` es 0, porque 1 ya es el final de la sucesión. `collatz_steps(12)` es 9, y `collatz_steps(27)` es 111.

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

`collatz_steps(1)` debe devolver 0, porque 1 ya es el final de la sucesión.

```python
    def test1(self):
        self.assertEqual(collatz_steps(1), 0, "--err-t1--")
```

`collatz_steps(2)` debe devolver 1.

```python
    def test2(self):
        self.assertEqual(collatz_steps(2), 1, "--err-t2--")
```

`collatz_steps(6)` debe devolver 8.

```python
    def test3(self):
        self.assertEqual(collatz_steps(6), 8, "--err-t3--")
```

`collatz_steps(7)` debe devolver 16.

```python
    def test4(self):
        self.assertEqual(collatz_steps(7), 16, "--err-t4--")
```

`collatz_steps(16)` debe devolver 4.

```python
    def test5(self):
        self.assertEqual(collatz_steps(16), 4, "--err-t5--")
```

`collatz_steps(12)` debe devolver 9.

```python
    def test6(self):
        self.assertEqual(collatz_steps(12), 9, "--err-t6--")
```

`collatz_steps(27)` debe devolver 111.

```python
    def test7(self):
        self.assertEqual(collatz_steps(27), 111, "--err-t7--")
```

`collatz_steps(97)` debe devolver 118.

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
