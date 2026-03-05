---
language: python
exerciseType: 1
difficulty: 1
title: Two for one
---

# --description--

Geben Sie einen Namen an, geben Sie einen String mit der Nachricht zurück:
`One for X, one for me.`
Wobei `X` der angegebene Name ist.
Wenn der Name jedoch fehl, geben Sie den String zurück:
`One for you, one for me.`

# --instructions--

Schreiben Sie eine Funktion, die den richtigen String zurückgibt, Beispiele:

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

Übergeben Sie "James" als Name

```python
    def test_a_name_given(self):
        self.assertEqual(two_for_one("James"), "One for James, one for me.", "--err-t2--")
```


Übergeben Sie "Martha" als Name

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
