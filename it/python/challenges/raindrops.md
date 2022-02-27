---
language: python
exerciseType: 1
difficulty: 1
title: Gocce di pioggia
---

# --description--

Il tuo compito e' quello di convertiire un numero in una stringa che contiene suoni di gocce di pioggia corrispondenti a determinati fattori potenziali.
Un fattore e' un numero che si divide uniformemente in un altro numero, senza lasciare alcun resto.
Il modo piu' semplice per verificare se un numero e' un fattore di un altro e' utilizzare l'operazione modulo.
Le regole delle gocce di pioggia sono che se un dato numero:

- ha 3 come fattore, aggiungi 'Pling' al risultato.
- ha 5 come fattore, aggiungi 'Plang' al risultato.
- ha 7 come fattore, aggiungi 'Plong' al risultato.
- non ha 3, 5 o 7 come fattore, il risultato dovrebbe essere costituito dalle cifre del numero.

# --instructions--

Scrivi una funzione che restituisca la stringa corretta, ad esempio:

- 28 ha 7 come fattore, ma non 3 o 5, quindi il risultato e' `"Plong"`.
- 30 ha sia 3 che 5 come fattori, ma non 7, quindi il risultato e' `"PlingPlang"`.
- 34 non e' fattorizzato da 3, 5, o 7, quindi il risultato e' `"34"`.

# --seed--

```python
def converti(num):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Il suono per 1 è "1"

```python
    def test_the_sound_for_1_is_1(self):
        self.assertEqual(converti(1), "1", "--err-t1--")
```

Il suono per 3 è "Pling"

```python
    def test_the_sound_for_3_is_pling(self):
        self.assertEqual(converti(3), "Pling", "--err-t2--")
```

Il suono per 5 è "Plang"

```python
    def test_the_sound_for_5_is_plang(self):
        self.assertEqual(converti(5), "Plang", "--err-t3--")
```

Il suono per 7 è "Plong"

```python
    def test_the_sound_for_7_is_plong(self):
        self.assertEqual(converti(7), "Plong", "--err-t4--")
```

Il suono per 6 è "Pling"

```python
    def test_the_sound_for_6_is_pling(self):
        self.assertEqual(converti(6), "Pling", "--err-t5--")
```

Il suono per 8 è "8"

```python
    def test_the_sound_for_8_is_8(self):
        self.assertEqual(converti(8), "8", "--err-t6--")
```

Il suono per 9 è "Pling"

```python
    def test_the_sound_for_9_is_pling(self):
        self.assertEqual(converti(9), "Pling", "--err-t7--")
```

Il suono per 10 è "Plang"

```python
    def test_the_sound_for_10_is_plang(self):
        self.assertEqual(converti(10), "Plang", "--err-t8--")
```

Il suono per 14 è "Plong"

```python
    def test_the_sound_for_14_is_plong(self):
        self.assertEqual(converti(14), "Plong", "--err-t9--")
```

Il suono per 15 è "PlingPlang"

```python
    def test_the_sound_for_15_is_pling_plang(self):
        self.assertEqual(converti(15), "PlingPlang", "--err-t10--")
```

Il suono per 21 è "PlingPlong"

```python
    def test_the_sound_for_21_is_pling_plong(self):
        self.assertEqual(converti(21), "PlingPlong", "--err-t11--")
```

Il suono per 25 è "Plang"

```python
    def test_the_sound_for_25_is_plang(self):
        self.assertEqual(converti(25), "Plang", "--err-t12--")
```

Il suono per 27 è "Pling"

```python
    def test_the_sound_for_27_is_pling(self):
        self.assertEqual(converti(27), "Pling", "--err-t13--")
```

Il suono per 35 è "PlangPlong"

```python
    def test_the_sound_for_35_is_plang_plong(self):
        self.assertEqual(converti(35), "PlangPlong", "--err-t14--")
```

Il suono per 49 è "Plong"

```python
    def test_the_sound_for_49_is_plong(self):
        self.assertEqual(converti(49), "Plong", "--err-t15--")
```

Il suono per 52 è "52"

```python
    def test_the_sound_for_52_is_52(self):
        self.assertEqual(converti(52), "52", "--err-t16--")
```

Il suono per 105 è "PlingPlangPlong"

```python
    def test_the_sound_for_105_is_pling_plang_plong(self):
        self.assertEqual(converti(105), "PlingPlangPlong", "--err-t17--")
```

Il suono per 3125 è "Plang"

```python
    def test_the_sound_for_3125(self):
        self.assertEqual(converti(3125), "Plang", "--err-t18--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def converti(num):
    res = ''
    if num % 3 == 0:
        res += 'Pling'
    if num % 5 == 0:
        res += 'Plang'
    if num % 7 == 0:
        res += 'Plong'

    if not res:
        res = str(num)
    return res
```

