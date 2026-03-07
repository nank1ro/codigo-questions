---
language: python
exerciseType: 1
difficulty: 3
title: Rok przestępny
---

# --description--

W roku kalendarzowym jest dokładnie 365,25 dnia. Jednak z czasem prowadzi to do zamieszania, ponieważ ludzie normalnie liczą przez dokładną podzielność przez 1, a nie z miejscami dziesiętnymi. Aby temu zapobiec, postanowiono zsumować wszystkie 0,25 dnia w każdym czteroletnim cyklu i dać temu rokowi 366 dni (włącznie z 29 lutego jako dniem przestępnym) i nazwać go __rokiem przestępnym__. Pozostałe trzy lata w czteroletnim cyklu zawierałyby tylko 365 dni i __nie byłyby latami przestępnymi__.

# --instructions--

W tym wyzwaniu przejdziemy na wyższy poziom, gdzie musisz określić, czy dany rok jest przestępny, bez użycia klasy `datetime`, __bloków if__, __bloków if-elif__ ani __warunków__ (`a if b else c`), ani operatorów logicznych __AND__ (`and`) i __OR__ (`or`), z wyjątkiem operatora __NOT__ (`not`).

Zwróć `True` jeśli jest rokiem przestępnym, `False` w przeciwnym razie.

Przykład wywołania funkcji:
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

Użycie `month`, `day`, `if`, `else`, `elif`, `and`, `or` jest niedozwolone.

```json
{
  "regex": "if|else|elif|and|or|month|day",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

Rok `2016` jest rokiem przestępnym.

```python
    def test1(self):
        self.assertEqual(leap_year(2016), True, "--err-t1--")
```

Rok `1996` jest rokiem przestępnym.

```python
    def test2(self):
        self.assertEqual(leap_year(1996), True, "--err-t2--")
```

Rok `1600` jest rokiem przestępnym.

```python
    def test3(self):
        self.assertEqual(leap_year(1600), True, "--err-t3--")
```

Rok `2020` jest rokiem przestępnym.

```python
    def test4(self):
        self.assertEqual(leap_year(2020), True, "--err-t4--")
```

Rok `2000` jest rokiem przestępnym.

```python
    def test5(self):
        self.assertEqual(leap_year(2000), True, "--err-t5--")
```

Rok `2008` jest rokiem przestępnym.

```python
    def test6(self):
        self.assertEqual(leap_year(2008), True, "--err-t6--")
```

Rok `1521` nie jest rokiem przestępnym.

```python
    def test7(self):
        self.assertEqual(leap_year(1521), False, "--err-t7--")
```

Rok `1800` nie jest rokiem przestępnym.

```python
    def test8(self):
        self.assertEqual(leap_year(1800), False, "--err-t8--")
```

Rok `2007` nie jest rokiem przestępnym.

```python
    def test9(self):
        self.assertEqual(leap_year(2007), False, "--err-t9--")
```

Rok `2002` jest rokiem przestępnym.

```python
    def test10(self):
        self.assertEqual(leap_year(2002), False, "--err-t10--")
```

Rok `1979` nie jest rokiem przestępnym.

```python
    def test11(self):
        self.assertEqual(leap_year(1979), False, "--err-t11--")
```

Rok `2006` nie jest rokiem przestępnym.

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
