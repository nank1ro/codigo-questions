---
language: python
exerciseType: 1
difficulty: 2
title: Orologio
---

# --description--

Un orologio a 24 ore mostra l'ora del giorno come `HH:MM`, partendo da `00:00` subito dopo la mezzanotte e arrivando a `23:59` un minuto prima della mezzanotte successiva. Entrambe le parti sono sempre scritte con due cifre, così nove minuti dopo le undici del mattino si legge `11:09`.

Un giorno intero dura 1440 minuti. Quando l'orologio supera `23:59` riparte da `00:00` e ricomincia il giorno, e riavvolgendolo all'indietro oltre `00:00` si torna a `23:59`.

# --instructions--

Scrivi una funzione `clock_time` che riceve due numeri interi, `hours` e `minutes`, e restituisce la lettura di un orologio a 24 ore come stringa `"HH:MM"`, con entrambe le parti portate a due cifre.

Esempi:
```
clock_time(8, 0) ➞ "08:00"
clock_time(25, 160) ➞ "03:40"
clock_time(-1, 15) ➞ "23:15"
```

- Ciascuno dei due numeri può essere negativo, oppure più grande di quanto un orologio reale consenta.
- Calcola il numero totale di minuti come `hours * 60 + minutes`, poi riporta quel totale nell'intervallo da `0` a `1439`, così l'orologio riparte in entrambe le direzioni.
- `clock_time(24, 0)` è esattamente un giorno, quindi si legge `"00:00"`.

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

Le otto del mattino si legge `08:00`

```python
    def test_eight_in_the_morning(self):
        self.assertEqual(clock_time(8, 0), "08:00", "--err-t1--")
```

Le cifre singole vengono portate a due cifre, così nove minuti dopo le undici si legge `11:09`

```python
    def test_single_digits_are_padded(self):
        self.assertEqual(clock_time(11, 9), "11:09", "--err-t2--")
```

Esattamente un giorno intero di ore fa ripartire l'orologio da `00:00`

```python
    def test_a_full_day_rolls_over(self):
        self.assertEqual(clock_time(24, 0), "00:00", "--err-t3--")
```

I minuti oltre 60 vengono riportati nelle ore

```python
    def test_minutes_carry_into_hours(self):
        self.assertEqual(clock_time(25, 160), "03:40", "--err-t4--")
```

Un'ora negativa riavvolge l'orologio all'indietro oltre la mezzanotte

```python
    def test_a_negative_hour_winds_backwards(self):
        self.assertEqual(clock_time(-1, 15), "23:15", "--err-t5--")
```

Anche un numero di minuti negativo riavvolge l'orologio all'indietro

```python
    def test_negative_minutes_wind_backwards(self):
        self.assertEqual(clock_time(0, -90), "22:30", "--err-t6--")
```

Più di un giorno intero all'indietro continua a ripartire

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
    # Il % di Python assume sempre il segno del divisore, quindi un totale
    # negativo è già riportato in avanti in 0..1439.
    total = (hours * 60 + minutes) % 1440

    return f"{total // 60:02d}:{total % 60:02d}"
```
