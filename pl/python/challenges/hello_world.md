---
language: python
exerciseType: 1
difficulty: 1
title: Witaj Świecie!
---

# --description--

__"Witaj, Świecie!"__ to tradycyjny pierwszy program dla osób zaczynających programować w nowym języku lub środowisku.

# --instructions--

Napisz funkcję, która zwraca ciąg znaków "Hello, World!".

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

Funkcja powinna zwrócić "Hello, World!".

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
