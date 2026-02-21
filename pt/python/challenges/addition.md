---
language: python
exerciseType: 1
title: Addition
difficulty: 1
---
# --description--
Dados dois inteiros `num1` e `num2`, escreva um programa para adicionar esses dois números
# --instructions--
Escreva uma função que retorna a soma de dois números
# --seed--
```python
def addition():
    pass
```


# --before-asserts--
```python
import unittest
class CodigoTests(unittest.TestCase):
```



# --asserts--
A soma de 1 e 3 deve ser igual a 4
```python
    def test_addition1(self):
        self.assertEqual(addition(1, 3), 4, "--err-t1--")
```
A soma de 200 e 210 deve ser igual a 410
```python
    def test_addition2(self):
        self.assertEqual(addition(200, 210), 410, "--err-t2--")
```
A soma de 15 e 35 deve ser igual a 50
```python
    def test_addition3(self):
        self.assertEqual(addition(15, 35), 50, "--err-t3--")
```







# --after-asserts--
```python
if __name__ == "__main__":
    unittest.main()
```


# --solutions--
```python
def addition(num1, num2):
    return num1 + num2
```

