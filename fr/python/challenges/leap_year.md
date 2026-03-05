---
language: python
exerciseType: 1
difficulty: 3
title: Année bissextile
---

# --description--

Dans une année civile, il y a exactement 365,25 jours. Mais, à terme, cela peut prêter à confusion car les humains comptent normalement par divisibilité exacte de 1 et non avec des décimales. Ainsi, pour éviter cela, il a été décidé d'additionner tous les 0,25 jours sur un cycle de quatre ans et de donner à cette année 366 jours (incluant le 29 février comme jour intercalaire) et de l'appeler une __année bissextile__. Les trois autres années du cycle de quatre ans ne contiendraient que 365 jours et __ne seraient pas des années bissextiles__.

# --instructions--

Dans ce défi, nous passons à un niveau supérieur, où vous devez déterminer si c'est une année bissextile ou non sans utiliser la classe `datetime`, les __blocs if__, les __blocs if-elif__ ou les __conditionnelles__ (`a if b else c`) ni les opérateurs logiques __ET__ (`and`) et __OU__ (`or`) à l'exception de l'opérateur __NON__ (`not`).

Retournez `True` si c'est une année bissextile, `False` sinon.

Exemple d'appel de fonction :
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

The use of `month`, `day`, `if`, `else`, `elif`, `and`, `or` is not allowed.

```json
{
  "regex": "if|else|elif|and|or|month|day",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

The year `2016` is a leap year.

```python
    def test1(self):
        self.assertEqual(leap_year(2016), True, "--err-t1--")
```

The year `1996` is a leap year.

```python
    def test2(self):
        self.assertEqual(leap_year(1996), True, "--err-t2--")
```

The year `1600` is a leap year.

```python
    def test3(self):
        self.assertEqual(leap_year(1600), True, "--err-t3--")
```

The year `2020` is a leap year.

```python
    def test4(self):
        self.assertEqual(leap_year(2020), True, "--err-t4--")
```

The year `2000` is a leap year.

```python
    def test5(self):
        self.assertEqual(leap_year(2000), True, "--err-t5--")
```

The year `2008` is a leap year.

```python
    def test6(self):
        self.assertEqual(leap_year(2008), True, "--err-t6--")
```

The year `1521` is not a leap year.

```python
    def test7(self):
        self.assertEqual(leap_year(1521), False, "--err-t7--")
```

The year `1800` is not a leap year.

```python
    def test8(self):
        self.assertEqual(leap_year(1800), False, "--err-t8--")
```

The year `2007` is not a leap year.

```python
    def test9(self):
        self.assertEqual(leap_year(2007), False, "--err-t9--")
```

The year `2002` is a leap year.

```python
    def test10(self):
        self.assertEqual(leap_year(2002), False, "--err-t10--")
```

The year `1979` is not a leap year.

```python
    def test11(self):
        self.assertEqual(leap_year(1979), False, "--err-t11--")
```

The year `2006` is not a leap year.

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
