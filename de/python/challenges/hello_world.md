---
language: python
exerciseType: 1
title: Hello World!
difficulty: 1
---

# --description--

__"Hello, World!"__ ist das traditionelle erste Programm zum Beginn der Programmierung in einer neuen Sprache oder Umgebung.

# --instructions--

Schreiben Sie eine Funktion, die den String "Hello, World!" zurückgibt.

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

Die Funktion sollte "Hello, World!" zurückgeben.

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
