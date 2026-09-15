---
language: python
exerciseType: 1
difficulty: 2
title: Checksum di Luhn
---

# --description--

L'algoritmo di Luhn è un semplice checksum usato per validare numeri identificativi, come i numeri delle carte di credito.

Prima di controllare un numero, rimuovi ogni spazio dalla stringa. La stringa è valida solo se ciò che resta è più lungo di un carattere e la stringa originale non contiene altro che cifre e spazi.

Per eseguire il controllo, parti dalla cifra più a destra e procedi verso sinistra, raddoppiando una cifra su due. Quando il raddoppio produce un numero maggiore di 9, sottrai 9. Poi somma tutte le cifre: il numero è valido solo se la somma è divisibile per 10.

Ad esempio, `"059"` dà `0`, poi `5` raddoppiato è `10` che diventa `1`, poi `9`. La loro somma è `10`, che è divisibile per 10, quindi il numero è valido.

# --instructions--

Scrivi una funzione `is_valid` che riceve una stringa e restituisce `True` quando il numero è valido, `False` altrimenti.

- `"4539 3195 0343 6467"` passa il checksum, quindi il risultato è `True`.
- `"8273 1232 7352 0569"` non passa il checksum, quindi il risultato è `False`.
- `"0"` è lungo solo un carattere, quindi il risultato è `False`.
- `"055-444-285"` contiene un carattere che non è una cifra né uno spazio, quindi il risultato è `False`.

Esempio di chiamata di funzione:
```python
print(is_valid("095 245 88"))
# stampa True
```

# --seed--

```python
def is_valid(value):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Una singola cifra non è valida.

```python
    def test_a_single_digit_is_not_valid(self):
        self.assertEqual(is_valid("0"), False, "--err-t1--")
```

Una singola cifra preceduta da uno spazio non è valida.

```python
    def test_a_single_digit_with_a_space_is_not_valid(self):
        self.assertEqual(is_valid(" 0"), False, "--err-t2--")
```

Il numero `"059"` è valido.

```python
    def test_059_is_valid(self):
        self.assertEqual(is_valid("059"), True, "--err-t3--")
```

Il numero `"59"` è valido.

```python
    def test_59_is_valid(self):
        self.assertEqual(is_valid("59"), True, "--err-t4--")
```

Il numero `"055 444 285"` è valido.

```python
    def test_055_444_285_is_valid(self):
        self.assertEqual(is_valid("055 444 285"), True, "--err-t5--")
```

Il numero `"055 444 286"` non è valido.

```python
    def test_055_444_286_is_not_valid(self):
        self.assertEqual(is_valid("055 444 286"), False, "--err-t6--")
```

Il numero `"8273 1232 7352 0569"` non è valido.

```python
    def test_8273_1232_7352_0569_is_not_valid(self):
        self.assertEqual(is_valid("8273 1232 7352 0569"), False, "--err-t7--")
```

Il numero `"4539 3195 0343 6467"` è valido.

```python
    def test_4539_3195_0343_6467_is_valid(self):
        self.assertEqual(is_valid("4539 3195 0343 6467"), True, "--err-t8--")
```

Il numero `"1 2345 6789 1234 5678 9012"` non è valido.

```python
    def test_a_long_number_is_not_valid(self):
        self.assertEqual(is_valid("1 2345 6789 1234 5678 9012"), False, "--err-t9--")
```

Il numero `"095 245 88"` è valido.

```python
    def test_095_245_88_is_valid(self):
        self.assertEqual(is_valid("095 245 88"), True, "--err-t10--")
```

Una lettera rende il numero non valido.

```python
    def test_a_letter_is_not_valid(self):
        self.assertEqual(is_valid("055a 444 285"), False, "--err-t11--")
```

I trattini rendono il numero non valido.

```python
    def test_dashes_are_not_valid(self):
        self.assertEqual(is_valid("055-444-285"), False, "--err-t12--")
```

Un carattere di punteggiatura rende il numero non valido.

```python
    def test_punctuation_is_not_valid(self):
        self.assertEqual(is_valid(":9"), False, "--err-t13--")
```

I simboli rendono il numero non valido.

```python
    def test_symbols_are_not_valid(self):
        self.assertEqual(is_valid("055# 444$ 285"), False, "--err-t14--")
```

Una stringa vuota non è valida.

```python
    def test_an_empty_string_is_not_valid(self):
        self.assertEqual(is_valid(""), False, "--err-t15--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def is_valid(value):
    total = 0
    count = 0
    for char in reversed(value):
        if char == ' ':
            continue
        if char < '0' or char > '9':
            return False
        digit = int(char)
        if count % 2 == 1:
            digit *= 2
            if digit > 9:
                digit -= 9
        total += digit
        count += 1
    return count > 1 and total % 10 == 0
```
