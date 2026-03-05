---
language: python
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

In einem Kalenderjahr gibt es genau 365,25 Tage. Aber das wird schließlich zu Verwirrung führen, weil Menschen normalerweise nach exakter Teilbarkeit durch 1 zählen und nicht mit Dezimalzahlen. Um das zu vermeiden, wurde beschlossen, alle 0,25 Tage alle vier Jahre zu addieren und diesem Jahr 366 Tage zu geben (mit dem 29. Februar als Schalttag) und es __Schaltjahr__ zu nennen. Die anderen drei Jahre in dem vierjährigen Zyklus würden nur 365 Tage enthalten und __würden keine Schaltjahre sein__.

# --instructions--

In dieser Herausforderung werden wir es auf eine neue Ebene bringen, in der Sie bestimmen sollen, ob es ein Schaltjahr ist oder nicht, ohne die `datetime` Klasse zu verwenden, __if-Blöcke__, __if-elif-Blöcke__ oder __Bedingungen__ (`a if b else c`) noch die logischen Operatoren __AND__ (`and`) und __OR__ (`or__), mit Ausnahme des __NOT__ (`not`) Operators.

Geben Sie `True` zurück, wenn es ein Schaltjahr ist, ansonsten `False`.

Example of function call:
```dart
print(leap_year(2000))
// prints true
```

# --seed--

```python
def leap_year(year):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Die Verwendung von `month`, `day`, `if`, `else`, `elif`, `and`, `or` ist nicht zulässig.

```json
{
  "regex": "if|else|elif|and|or|month|day",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Das Jahr `2016` ist ein Schaltjahr.

```python
    def test1(self):
        self.assertEqual(leap_year(2016), True, "--err-t1--")
```

Das Jahr `1996` ist ein Schaltjahr.

```python
    def test2(self):
        self.assertEqual(leap_year(1996), True, "--err-t2--")
```

Das Jahr `1600` ist ein Schaltjahr.

```python
    def test3(self):
        self.assertEqual(leap_year(1600), True, "--err-t3--")
```

Das Jahr `2020` ist ein Schaltjahr.

```python
    def test4(self):
        self.assertEqual(leap_year(2020), True, "--err-t4--")
```

Das Jahr `2000` ist ein Schaltjahr.

```python
    def test5(self):
        self.assertEqual(leap_year(2000), True, "--err-t5--")
```

Das Jahr `2008` ist ein Schaltjahr.

```python
    def test6(self):
        self.assertEqual(leap_year(2008), True, "--err-t6--")
```

Das Jahr `1521` ist kein Schaltjahr.

```python
    def test7(self):
        self.assertEqual(leap_year(1521), False, "--err-t7--")
```

Das Jahr `1800` ist kein Schaltjahr.

```python
    def test8(self):
        self.assertEqual(leap_year(1800), False, "--err-t8--")
```

Das Jahr `2007` ist kein Schaltjahr.

```python
    def test9(self):
        self.assertEqual(leap_year(2007), False, "--err-t9--")
```

Das Jahr `2002` ist kein Schaltjahr.

```python
    def test10(self):
        self.assertEqual(leap_year(2002), False, "--err-t10--")
```

Das Jahr `1979` ist kein Schaltjahr.

```python
    def test11(self):
        self.assertEqual(leap_year(1979), False, "--err-t11--")
```

Das Jahr `2006` ist kein Schaltjahr.

```python
    def test12(self):
        self.assertEqual(leap_year(2006), False, "--err-t12--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def leap_year(year):
    return (year % 4 == 0) ^ ((year % 100 == 0) & (year % 400 != 0))
```

```python
def leap_year(year):
    while year % 100 == 0:
        year = year // 100
    return year % 4 == 0
```
