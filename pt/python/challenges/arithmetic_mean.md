---
language: python
exerciseType: 1
title: Arithmetic mean
difficulty: 1
---
# --description--
Escreva uma função chamada `mean` para encontrar a _média aritmética_ de um vetor numérico.
# --instructions--
```python
print(mean([1, 2, 3]))
# prints 2
```
Escreva uma função que retorna a média de um vetor numérico.

Exemplo de chamada de função:
# --seed--
```python
def mean():
    pass
```


# --before-asserts--
```python
import unittest
class CodigoTests(unittest.TestCase):
```



# --asserts--
A média de `[1, 2, 3, 4, 5, 6, 7]` deve ser igual a 4
```python
    def test1(self):
        self.assertEqual(mean([1, 2, 3, 4, 5, 6, 7]), 4, "--err-t1--")
```
A média de `[4, 5, 6]` deve ser igual a 5
```python
    def test2(self):
        self.assertEqual(mean([4, 5, 6]), 5, "--err-t2--")
```
A média de `[12, 34, 56, 78]` deve ser igual a 45
```python
    def test3(self):
        self.assertEqual(mean([12, 34, 56, 78]), 45, "--err-t3--")
```







# --after-asserts--
```python
if __name__ == "__main__":
    unittest.main()
```


# --solutions--
```python
from math import fsum
def mean(numbers):
    return fsum(numbers) / float(len(numbers))
```


