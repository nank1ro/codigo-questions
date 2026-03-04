---
language: python
exerciseType: 1
difficulty: 3
title: Leap Year
---

# --description--

En un año del calendario hay exactamente 365.25 días. Pero, eventualmente, esto llevará a confusión porque los humanos normalmente cuentan por divisibilidad exacta de 1 y no con puntos decimales. Entonces, para evitar lo anterior, se decidió sumar todos los 0.25 días cada ciclo de cuatro años y dar a ese año 366 días (incluyendo el 29 de febrero como día intercalario) y llamarlo __año bisiesto__. Los otros tres años en el ciclo de cuatro años solo contendrían 365 días y __no serían años bisiestos__.

# --instructions--

En este desafío lo llevaremos a un nuevo nivel, donde debes determinar si es un año bisiesto o no sin el uso de la clase `datetime`, __bloques if__, __bloques if-elif__ o __condicionales__ (`a if b else c`) ni los operadores lógicos __AND__ (`and`) y __OR__ (`or`) con la excepción del operador __NOT__ (`not`).

Devuelve `True` si es un año bisiesto, `False` en caso contrario.

Ejemplo de llamada de función:
```dart
print(leap_year(2000))
// imprime true
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

No se permite el uso de `month`, `day`, `if`, `else`, `elif`, `and`, `or`.

```json
{
  "regex": "if|else|elif|and|or|month|day",
  "modifiers": ["m"],
  "shouldMatch": false
}
```

El año `2016` es un año bisiesto.

```python
    def test1(self):
        self.assertEqual(leap_year(2016), True, "--err-t1--")
```

El año `1996` es un año bisiesto.

```python
    def test2(self):
        self.assertEqual(leap_year(1996), True, "--err-t2--")
```

El año `1600` es un año bisiesto.

```python
    def test3(self):
        self.assertEqual(leap_year(1600), True, "--err-t3--")
```

El año `2020` es un año bisiesto.

```python
    def test4(self):
        self.assertEqual(leap_year(2020), True, "--err-t4--")
```

El año `2000` es un año bisiesto.

```python
    def test5(self):
        self.assertEqual(leap_year(2000), True, "--err-t5--")
```

El año `2008` es un año bisiesto.

```python
    def test6(self):
        self.assertEqual(leap_year(2008), True, "--err-t6--")
```

El año `1521` no es un año bisiesto.

```python
    def test7(self):
        self.assertEqual(leap_year(1521), False, "--err-t7--")
```

El año `1800` no es un año bisiesto.

```python
    def test8(self):
        self.assertEqual(leap_year(1800), False, "--err-t8--")
```

El año `2007` no es un año bisiesto.

```python
    def test9(self):
        self.assertEqual(leap_year(2007), False, "--err-t9--")
```

El año `2002` es un año bisiesto.

```python
    def test10(self):
        self.assertEqual(leap_year(2002), False, "--err-t10--")
```

El año `1979` no es un año bisiesto.

```python
    def test11(self):
        self.assertEqual(leap_year(1979), False, "--err-t11--")
```

El año `2006` no es un año bisiesto.

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
