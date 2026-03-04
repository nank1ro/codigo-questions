---
language: python
exerciseType: 1
difficulty: 1
title: Gotas de lluvia
---

# --description--

Tu tarea es convertir un número en una cadena que contiene sonidos de gotas de lluvia correspondientes a ciertos factores potenciales.
Un factor es un número que se divide uniformemente en otro número, sin dejar residuo.
La forma más simple de probar si un número es un factor de otro es usar la operación módulo.
Las reglas de raindrops son las siguientes:

- tiene 3 como factor, agrega 'Pling' al resultado.
- tiene 5 como factor, agrega 'Plang' al resultado.
- tiene 7 como factor, agrega 'Plong' al resultado.
- no tiene 3, 5 o 7 como factor, el resultado debe ser los dígitos del número.

# --instructions--

Escribe una función que devuelva la cadena correcta, ejemplos:

- 28 tiene 7 como factor, pero no 3 o 5, entonces el resultado sería `"Plong"`.
- 30 tiene tanto 3 como 5 como factores, pero no 7, entonces el resultado sería `"PlingPlang"`.
- 34 no es factorizado por 3, 5 o 7, entonces el resultado sería `"34"`.

# --seed--

```python
def convert(number):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

El sonido para 1 es "1"

```python
    def test_the_sound_for_1_is_1(self):
        self.assertEqual(convert(1), "1", "--err-t1--")
```

El sonido para 3 es "Pling"

```python
    def test_the_sound_for_3_is_pling(self):
        self.assertEqual(convert(3), "Pling", "--err-t2--")
```

El sonido para 5 es "Plang"

```python
    def test_the_sound_for_5_is_plang(self):
        self.assertEqual(convert(5), "Plang", "--err-t3--")
```

El sonido para 7 es "Plong"

```python
    def test_the_sound_for_7_is_plong(self):
        self.assertEqual(convert(7), "Plong", "--err-t4--")
```

El sonido para 6 es "Pling"

```python
    def test_the_sound_for_6_is_pling(self):
        self.assertEqual(convert(6), "Pling", "--err-t5--")
```

El sonido para 8 es "8"

```python
    def test_the_sound_for_8_is_8(self):
        self.assertEqual(convert(8), "8", "--err-t6--")
```

El sonido para 9 es "Pling"

```python
    def test_the_sound_for_9_is_pling(self):
        self.assertEqual(convert(9), "Pling", "--err-t7--")
```

El sonido para 10 es "Plang"

```python
    def test_the_sound_for_10_is_plang(self):
        self.assertEqual(convert(10), "Plang", "--err-t8--")
```

El sonido para 14 es "Plong"

```python
    def test_the_sound_for_14_is_plong(self):
        self.assertEqual(convert(14), "Plong", "--err-t9--")
```

El sonido para 15 es "PlingPlang"

```python
    def test_the_sound_for_15_is_pling_plang(self):
        self.assertEqual(convert(15), "PlingPlang", "--err-t10--")
```

El sonido para 21 es "PlingPlong"

```python
    def test_the_sound_for_21_is_pling_plong(self):
        self.assertEqual(convert(21), "PlingPlong", "--err-t11--")
```

El sonido para 25 es "Plang"

```python
    def test_the_sound_for_25_is_plang(self):
        self.assertEqual(convert(25), "Plang", "--err-t12--")
```

El sonido para 27 es "Pling"

```python
    def test_the_sound_for_27_is_pling(self):
        self.assertEqual(convert(27), "Pling", "--err-t13--")
```

El sonido para 35 es "PlangPlong"

```python
    def test_the_sound_for_35_is_plang_plong(self):
        self.assertEqual(convert(35), "PlangPlong", "--err-t14--")
```

El sonido para 49 es "Plong"

```python
    def test_the_sound_for_49_is_plong(self):
        self.assertEqual(convert(49), "Plong", "--err-t15--")
```

El sonido para 52 es "52"

```python
    def test_the_sound_for_52_is_52(self):
        self.assertEqual(convert(52), "52", "--err-t16--")
```

El sonido para 105 es "PlingPlangPlong"

```python
    def test_the_sound_for_105_is_pling_plang_plong(self):
        self.assertEqual(convert(105), "PlingPlangPlong", "--err-t17--")
```

El sonido para 3125 es "Plang"

```python
    def test_the_sound_for_3125(self):
        self.assertEqual(convert(3125), "Plang", "--err-t18--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def convert(number):
    result = ''
    if number % 3 == 0:
        result += 'Pling'
    if number % 5 == 0:
        result += 'Plang'
    if number % 7 == 0:
        result += 'Plong'

    if not result:
        result = str(number)
    return result
```
