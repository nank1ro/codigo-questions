---
language: python
exerciseType: 1
difficulty: 2
title: Reloj
---

# --description--

Un reloj de 24 horas muestra la hora del día como `HH:MM`, empezando en `00:00` justo después de la medianoche y terminando en `23:59`, un minuto antes de la siguiente medianoche. Ambas partes se escriben siempre con dos dígitos, así que nueve minutos después de las once de la mañana se lee `11:09`.

Un día completo dura 1440 minutos. Cuando el reloj pasa de `23:59`, vuelve a `00:00` y empieza el día de nuevo, y girarlo hacia atrás más allá de `00:00` cae en `23:59`.

# --instructions--

Escribe una función `clock_time` que reciba dos números enteros, `hours` y `minutes`, y devuelva la lectura de un reloj de 24 horas como la cadena `"HH:MM"`, con ambas partes rellenas con dos dígitos.

Ejemplos:
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- Cualquiera de los dos números puede ser negativo, o mayor de lo que permite un reloj real.
- Calcula el número total de minutos como `hours * 60 + minutes` y después encaja ese total en el rango de `0` a `1439` para que el reloj dé la vuelta en ambas direcciones.
- `clock_time(24, 0)` es exactamente un día, así que se lee `"00:00"`.

# --seed--

```python
def clock_time(hours, minutes):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

A las ocho de la mañana se lee `08:00`

```python
    def test_eight_in_the_morning(self):
        self.assertEqual(clock_time(8, 0), "08:00", "--err-t1--")
```

Los números de un solo dígito se rellenan con dos, así que nueve minutos después de las once se lee `11:09`

```python
    def test_single_digits_are_padded(self):
        self.assertEqual(clock_time(11, 9), "11:09", "--err-t2--")
```

Exactamente un día completo de horas da la vuelta a `00:00`

```python
    def test_a_full_day_rolls_over(self):
        self.assertEqual(clock_time(24, 0), "00:00", "--err-t3--")
```

Los minutos por encima de 60 se trasladan a las horas

```python
    def test_minutes_carry_into_hours(self):
        self.assertEqual(clock_time(25, 160), "03:40", "--err-t4--")
```

Una hora negativa gira el reloj hacia atrás más allá de la medianoche

```python
    def test_a_negative_hour_winds_backwards(self):
        self.assertEqual(clock_time(-1, 15), "23:15", "--err-t5--")
```

Una cantidad negativa de minutos también gira el reloj hacia atrás

```python
    def test_negative_minutes_wind_backwards(self):
        self.assertEqual(clock_time(0, -90), "22:30", "--err-t6--")
```

Más de un día completo hacia atrás sigue dando la vuelta

```python
    def test_more_than_a_day_backwards(self):
        self.assertEqual(clock_time(-25, 0), "23:00", "--err-t7--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def clock_time(hours, minutes):
    # El % de Python siempre toma el signo del divisor, así que un total
    # negativo ya vuelve al rango 0..1439.
    total = (hours * 60 + minutes) % 1440

    return f"{total // 60:02d}:{total % 60:02d}"
```
