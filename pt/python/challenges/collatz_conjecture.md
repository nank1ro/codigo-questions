---
language: python
exerciseType: 1
difficulty: 1
title: Conjectura de Collatz
---

# --description--

A conjectura de Collatz parte de qualquer número inteiro positivo `n` e repete uma regra simples: se `n` é par, divida-o pela metade; se `n` é ímpar, substitua-o por `3n + 1`. Mais cedo ou mais tarde a sequência chega a 1.

Por exemplo, partindo de 16 a sequência é `16 -> 8 -> 4 -> 2 -> 1`, então leva 4 passos.

Ninguém jamais provou que isso sempre acontece, mas vale para todos os números já testados.

# --instructions--

Escreva uma função `collatz_steps` que recebe um número inteiro positivo `n` e retorna o número de passos necessários para chegar a 1.

`collatz_steps(1)` é 0, porque 1 já é o fim da sequência. `collatz_steps(12)` é 9, e `collatz_steps(27)` é 111.

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

`collatz_steps(1)` deve retornar 0, porque 1 já é o fim da sequência.

```python
    def test1(self):
        self.assertEqual(collatz_steps(1), 0, "--err-t1--")
```

`collatz_steps(2)` deve retornar 1.

```python
    def test2(self):
        self.assertEqual(collatz_steps(2), 1, "--err-t2--")
```

`collatz_steps(6)` deve retornar 8.

```python
    def test3(self):
        self.assertEqual(collatz_steps(6), 8, "--err-t3--")
```

`collatz_steps(7)` deve retornar 16.

```python
    def test4(self):
        self.assertEqual(collatz_steps(7), 16, "--err-t4--")
```

`collatz_steps(16)` deve retornar 4.

```python
    def test5(self):
        self.assertEqual(collatz_steps(16), 4, "--err-t5--")
```

`collatz_steps(12)` deve retornar 9.

```python
    def test6(self):
        self.assertEqual(collatz_steps(12), 9, "--err-t6--")
```

`collatz_steps(27)` deve retornar 111.

```python
    def test7(self):
        self.assertEqual(collatz_steps(27), 111, "--err-t7--")
```

`collatz_steps(97)` deve retornar 118.

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
