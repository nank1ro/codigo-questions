---
language: python
exerciseType: 1
difficulty: 1
title: Hello World!
---
# --description--
__"Hello, World!"__ é o tradicional primeiro programa para começar a programar em uma nova linguagem ou ambiente.
# --instructions--
Escreva uma função que retorna a string "Hello, World!".
# --seed--
```python
def hello():
    pass
```


# --before-asserts--
```python
import unittest
class CodigoTests(unittest.TestCase):
```



# --asserts--
A função deve retornar "Hello, World!".
```python
    def test_say_hi(self):
        self.assertEqual(hello(), "Hello, World!", "--err-t1--")
```



# --after-asserts--
```python
if __name__ == "__main__":
    unittest.main()
```


# --solutions--
```python
def hello():
    return "Hello, World!"
```

