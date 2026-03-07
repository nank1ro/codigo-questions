---
language: python
exerciseType: 1
difficulty: 1
title: Dwa za jednego
---

# --description--

Mając podane imię, zwróć ciąg znaków z komunikatem:
`One for X, one for me.`
Gdzie `X` to podane imię.
Jednak jeśli imię brakuje, zwróć ciąg znaków:
`One for you, one for me.`

# --instructions--

Napisz funkcję, która zwraca poprawny ciąg znaków, przykłady:

**wejście**: `Walter`
**wyjście**: `One for Walter, one for me.`

**wejście**:
**wyjście**: `One for you, one for me.`

**wejście**: `David`
**wyjście**: `One for David, one for me.`

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

Nie podano imienia

```python
    def test_no_name_given(self):
        self.assertEqual(two_for_one(), "One for you, one for me.", "--err-t1--")
```

Podaj "James" jako imię

```python
    def test_a_name_given(self):
        self.assertEqual(two_for_one("James"), "One for James, one for me.", "--err-t2--")
```


Podaj "Martha" jako imię

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
