---
language: python
exerciseType: 1
title: Addition
difficulty: 1
---

# --description--

Gegeben seien zwei Ganzzahlen `num1` und `num2`. Schreiben Sie ein Programm, um diese beiden Zahlen zu addieren

# --instructions--

Schreiben Sie eine Funktion, die die Summe von zwei Zahlen zurückgibt

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

Die Summe von 1 und 3 muss gleich 4 sein

```python
    def test_addition1(self):
        self.assertEqual(addition(1, 3), 4, "--err-t1--")
```

Die Summe von 200 und 210 muss gleich 410 sein

```python
    def test_addition2(self):
        self.assertEqual(addition(200, 210), 410, "--err-t2--")
```

Die Summe von 15 und 35 muss gleich 50 sein

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
