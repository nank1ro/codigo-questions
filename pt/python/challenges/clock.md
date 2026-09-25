---
language: python
exerciseType: 1
difficulty: 2
title: Relógio
---

# --description--

Um relógio de 24 horas mostra a hora do dia como `HH:MM`, começando em `00:00` logo após a meia-noite e terminando em `23:59`, um minuto antes da próxima meia-noite. Ambas as partes são sempre escritas com dois dígitos, então nove minutos após onze da manhã lê-se `11:09`.

Um dia inteiro dura 1440 minutos. Quando o relógio passa de `23:59`, ele volta para `00:00` e começa o dia novamente, e girá-lo para trás além de `00:00` cai em `23:59`.

# --instructions--

Escreva uma função `clock_time` que recebe dois números inteiros, `hours` e `minutes`, e retorna a leitura de um relógio de 24 horas como a string `"HH:MM"`, com ambas as partes preenchidas com dois dígitos.

Exemplos:
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- Qualquer um dos números pode ser negativo, ou maior do que um relógio real permite.
- Calcule o número total de minutos como `hours * 60 + minutes` e depois encaixe esse total na faixa de `0` a `1439` para que o relógio faça a volta em ambas as direções.
- `clock_time(24, 0)` é exatamente um dia, então lê-se `"00:00"`.

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

Oito da manhã lê-se `08:00`

```python
    def test_eight_in_the_morning(self):
        self.assertEqual(clock_time(8, 0), "08:00", "--err-t1--")
```

Números de um dígito são preenchidos com dois, então nove minutos após onze lê-se `11:09`

```python
    def test_single_digits_are_padded(self):
        self.assertEqual(clock_time(11, 9), "11:09", "--err-t2--")
```

Exatamente um dia inteiro de horas faz a volta para `00:00`

```python
    def test_a_full_day_rolls_over(self):
        self.assertEqual(clock_time(24, 0), "00:00", "--err-t3--")
```

Minutos acima de 60 são transportados para as horas

```python
    def test_minutes_carry_into_hours(self):
        self.assertEqual(clock_time(25, 160), "03:40", "--err-t4--")
```

Uma hora negativa gira o relógio para trás além da meia-noite

```python
    def test_a_negative_hour_winds_backwards(self):
        self.assertEqual(clock_time(-1, 15), "23:15", "--err-t5--")
```

Uma contagem de minutos negativa também gira o relógio para trás

```python
    def test_negative_minutes_wind_backwards(self):
        self.assertEqual(clock_time(0, -90), "22:30", "--err-t6--")
```

Mais de um dia inteiro para trás continua fazendo a volta

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
    # O % do Python sempre assume o sinal do divisor, então um total negativo
    # já volta para a faixa 0..1439.
    total = (hours * 60 + minutes) % 1440

    return f"{total // 60:02d}:{total % 60:02d}"
```
