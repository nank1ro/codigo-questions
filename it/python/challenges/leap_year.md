---
language: python
exerciseType: 1
difficulty: 3
title: Anno bisestile
---

# --description--

In un anno solare ci sono esattamente 365.25 giorni. Ma questo poteva portare confusione perché gli esseri umani normalmente contano in base all'esatta divisibilità di 1 e non con i punti decimali. Quindi, per evitare quest'ultimo problema, si decise di sommare tutti gli 0.25 giorni ogni ciclo di quattro anni e dare a quell'anno 366 giorni (includendo il 29 febbraio come giorno intercalare) e chiamarlo __anno bisestile__. Gli altri tre anni del ciclo quadriennale contengono solo 365 giorni e non sono __anni bisestili__.

# --instructions--

In questa sfida ci spingeremo ad un nuovo livello, in cui dovremo determinare se si tratta di un anno bisestile o meno senza l'uso della classe `datetime`, dei blocchi __if__, __if-elif__ o delle __operazioni ausiliarie__ (`a if b else c`) né degli operatori logici __AND__ (`and`) e __OR__ (`or`) con l'eccezione dell'operatore __NOT__ (`not`).

Restituisci `True` se è un anno bisestile, `False` altrimenti.

Esempio di chiamata di funzione:
```dart
print(leapYear(2000));
// stampa true
```

In this challenge we'll take it to a new level, where you are to determine if it's a leap year or not without the use of the `datetime` class, __if blocks__, __if-elif blocks__ or __conditionals__ (`a if b else c`) nor the logical operators __AND__ (`and`) and __OR__ (`or`) with the exemption of the __NOT__ (`not`) operator.

Return `true` if it's a leap year, `false` otherwise.

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

L'uso di `month`, `day`, `if`, `else`, `elif`, `and`, `or` non è consentito.

```json
{
  "regex": "if|else|elif|and|or|month|day",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

L'anno `2016` è bisestile.

```python
    def test1(self):
        self.assertEqual(leap_year(2016), True, "--err-t1--")
```

L'anno `1996` è bisestile.

```python
    def test2(self):
        self.assertEqual(leap_year(1996), True, "--err-t2--")
```

L'anno `1600` è bisestile.

```python
    def test3(self):
        self.assertEqual(leap_year(1600), True, "--err-t3--")
```

L'anno `2020` è bisestile.

```python
    def test4(self):
        self.assertEqual(leap_year(2020), True, "--err-t4--")
```

L'anno `2000` è bisestile.

```python
    def test5(self):
        self.assertEqual(leap_year(2000), True, "--err-t5--")
```

L'anno `2008` è bisestile.

```python
    def test6(self):
        self.assertEqual(leap_year(2008), True, "--err-t6--")
```

L'anno `1521` non è bisestile.

```python
    def test7(self):
        self.assertEqual(leap_year(1521), False, "--err-t7--")
```

L'anno `1800` non è bisestile.

```python
    def test8(self):
        self.assertEqual(leap_year(1800), False, "--err-t8--")
```

L'anno `2007` non è bisestile.

```python
    def test9(self):
        self.assertEqual(leap_year(2007), False, "--err-t9--")
```

L'anno `2002` è bisestile.

```python
    def test10(self):
        self.assertEqual(leap_year(2002), False, "--err-t10--")
```

L'anno `1979` non è bisestile.

```python
    def test11(self):
        self.assertEqual(leap_year(1979), False, "--err-t11--")
```

L'anno `2006` non è bisestile.

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
