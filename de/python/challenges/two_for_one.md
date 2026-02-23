---
language: python
exerciseType: 1
title: Two for one
difficulty: 1
---

# --description--

Gegeben einen Namen, geben Sie einen String mit der Nachricht zurück:
`One for X, one for me.`
Dabei ist `X` der angegebene Name.
Wenn jedoch der Name fehlt, geben Sie den String zurück:
`One for you, one for me.`

# --instructions--

Schreiben Sie eine Funktion, die den korrekten String zurückgibt, Beispiele:

**input**: `Walter`
**output**: `One for Walter, one for me.`

**input**:
**output**: `One for you, one for me.`

**input**: `David`
**output**: `One for David, one for me.`

# --seed--

```python
def two_for_one(name):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Kein Name angegeben

```python
    def test_no_name_given(self):
        self.assertEqual(two_for_one(), "One for you, one for me.", "--err-t1--")
```

Geben Sie "James" als Namen an

```python
    def test_a_name_given(self):
        self.assertEqual(two_for_one("James"), "One for James, one for me.", "--err-t2--")
```

Geben Sie "Martha" als Namen an

```python
    def test_another_name_given(self):
        self.assertEqual(two_for_one("Martha"), "One for Martha, one for me.", "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def two_for_one(name = None):
    if not name:
      return "One for you, one for me."
    return f"One for {name}, one for me."
```
