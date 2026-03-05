---
language: python
exerciseType: 1
title: Função de Ackermann
difficulty: 1
---

# --description--

A função de Ackermann é um exemplo clássico de uma função recursiva, notável especialmente porque não é uma função recursiva primitiva. Ela cresce muito rapidamente em valor, assim como o tamanho de sua árvore de chamadas.

A função de Ackermann é geralmente definida da seguinte forma:

<latex>A(m, n) = \begin{cases} n + 1 &\text{if } m = 0 \\ A(m - 1,1) &\text{if } m > 0 \text{ and } n = 0 \\ A(m -1, A(m, n - 1)) &\text{if } m > 0 \text{ and } n > 0 \end{cases}</latex>

Seus argumentos nunca são negativos e ela sempre termina

# --instructions--

Escreva uma função que retorne o valor da função de Ackermann.

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

`ack(0, 0)` deve retornar 1.

```python
    def test1(self):
        self.assertEqual(ack(0, 0), 1, "--err-t1--")
```

`ack(1, 1)` deve retornar 3.

```python
    def test2(self):
        self.assertEqual(ack(1, 1), 3, "--err-t2--")
```

`ack(2, 5)` deve retornar 13.

```python
    def test3(self):
        self.assertEqual(ack(2, 5), 13, "--err-t3--")
```

`ack(3, 3)` deve retornar 61.

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
