---
language: python
exerciseType: 1
difficulty: 1
title: Conjecture de Collatz
---

# --description--

La conjecture de Collatz part de n'importe quel entier positif `n` et répète une règle simple : si `n` est pair, on le divise par deux ; si `n` est impair, on le remplace par `3n + 1`. Tôt ou tard, la séquence atteint 1.

Par exemple, en partant de 16, la séquence est `16 -> 8 -> 4 -> 2 -> 1`, donc il faut 4 étapes.

Personne n'a jamais prouvé que cela se produit toujours, mais c'est vrai pour tous les nombres testés jusqu'à présent.

# --instructions--

Écrivez une fonction `collatz_steps` qui prend un entier positif `n` et retourne le nombre d'étapes nécessaires pour atteindre 1.

`collatz_steps(1)` vaut 0, car 1 est déjà la fin de la séquence. `collatz_steps(12)` vaut 9, et `collatz_steps(27)` vaut 111.

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

`collatz_steps(1)` doit retourner 0, car 1 est déjà la fin de la séquence.

```python
    def test1(self):
        self.assertEqual(collatz_steps(1), 0, "--err-t1--")
```

`collatz_steps(2)` doit retourner 1.

```python
    def test2(self):
        self.assertEqual(collatz_steps(2), 1, "--err-t2--")
```

`collatz_steps(6)` doit retourner 8.

```python
    def test3(self):
        self.assertEqual(collatz_steps(6), 8, "--err-t3--")
```

`collatz_steps(7)` doit retourner 16.

```python
    def test4(self):
        self.assertEqual(collatz_steps(7), 16, "--err-t4--")
```

`collatz_steps(16)` doit retourner 4.

```python
    def test5(self):
        self.assertEqual(collatz_steps(16), 4, "--err-t5--")
```

`collatz_steps(12)` doit retourner 9.

```python
    def test6(self):
        self.assertEqual(collatz_steps(12), 9, "--err-t6--")
```

`collatz_steps(27)` doit retourner 111.

```python
    def test7(self):
        self.assertEqual(collatz_steps(27), 111, "--err-t7--")
```

`collatz_steps(97)` doit retourner 118.

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
