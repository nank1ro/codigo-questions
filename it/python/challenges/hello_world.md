---
language: python
exerciseType: 1
difficulty: 1
title: Hello World!
---

# --description--

__"Hello, World!"__ e' il primo programma tradizionale per iniziare a programmare in un nuovo linguaggio o ambiente.

# --instructions--

Scrivi una funzione che restituisce "Hello, World!".

# --seed--

```python
def hello():
    pass
```

# --before-asserts--

```python
import unittest

class HelloWorldTest(unittest.TestCase):
```

# --asserts--

La funzione deve restituire "Hello, World!".

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
