---
language: python
exerciseType: 1
difficulty: 2
title: Luhn checksum
---

# --description--

Algorytm Luhna to prosta suma kontrolna służąca do sprawdzania poprawności numerów identyfikacyjnych, takich jak numery kart kredytowych.

Przed sprawdzeniem numeru usuń wszystkie spacje z ciągu znaków. Ciąg znaków jest poprawny tylko wtedy, gdy to, co zostało, jest dłuższe niż jeden znak, a oryginalny ciąg znaków zawiera wyłącznie cyfry i spacje.

Aby wykonać sprawdzenie, zacznij od skrajnie prawej cyfry i przesuwaj się w lewo, podwajając co drugą cyfrę. Gdy podwojenie da liczbę większą niż 9, odejmij od niej 9. Następnie zsumuj wszystkie cyfry: numer jest poprawny tylko wtedy, gdy suma jest podzielna przez 10.

Na przykład `"059"` daje `0`, potem podwojone `5` to `10`, które staje się `1`, a następnie `9`. Ich suma wynosi `10`, czyli liczbę podzielną przez 10, więc numer jest poprawny.

# --instructions--

Napisz funkcję `is_valid`, która przyjmuje ciąg znaków i zwraca `True`, gdy numer jest poprawny, a `False` w przeciwnym razie.

- `"4539 3195 0343 6467"` przechodzi sumę kontrolną, więc wynik to `True`.
- `"8273 1232 7352 0569"` nie przechodzi sumy kontrolnej, więc wynik to `False`.
- `"0"` ma długość tylko jednego znaku, więc wynik to `False`.
- `"055-444-285"` zawiera znak, który nie jest cyfrą ani spacją, więc wynik to `False`.

Przykład wywołania funkcji:
```python
print(is_valid("095 245 88"))
# prints True
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

Pojedyncza cyfra nie jest poprawna.

```python
    def test_a_single_digit_is_not_valid(self):
        self.assertEqual(is_valid("0"), False, "--err-t1--")
```

Pojedyncza cyfra ze spacją na początku nie jest poprawna.

```python
    def test_a_single_digit_with_a_space_is_not_valid(self):
        self.assertEqual(is_valid(" 0"), False, "--err-t2--")
```

Numer `"059"` jest poprawny.

```python
    def test_059_is_valid(self):
        self.assertEqual(is_valid("059"), True, "--err-t3--")
```

Numer `"59"` jest poprawny.

```python
    def test_59_is_valid(self):
        self.assertEqual(is_valid("59"), True, "--err-t4--")
```

Numer `"055 444 285"` jest poprawny.

```python
    def test_055_444_285_is_valid(self):
        self.assertEqual(is_valid("055 444 285"), True, "--err-t5--")
```

Numer `"055 444 286"` nie jest poprawny.

```python
    def test_055_444_286_is_not_valid(self):
        self.assertEqual(is_valid("055 444 286"), False, "--err-t6--")
```

Numer `"8273 1232 7352 0569"` nie jest poprawny.

```python
    def test_8273_1232_7352_0569_is_not_valid(self):
        self.assertEqual(is_valid("8273 1232 7352 0569"), False, "--err-t7--")
```

Numer `"4539 3195 0343 6467"` jest poprawny.

```python
    def test_4539_3195_0343_6467_is_valid(self):
        self.assertEqual(is_valid("4539 3195 0343 6467"), True, "--err-t8--")
```

Numer `"1 2345 6789 1234 5678 9012"` nie jest poprawny.

```python
    def test_a_long_number_is_not_valid(self):
        self.assertEqual(is_valid("1 2345 6789 1234 5678 9012"), False, "--err-t9--")
```

Numer `"095 245 88"` jest poprawny.

```python
    def test_095_245_88_is_valid(self):
        self.assertEqual(is_valid("095 245 88"), True, "--err-t10--")
```

Litera powoduje, że numer jest niepoprawny.

```python
    def test_a_letter_is_not_valid(self):
        self.assertEqual(is_valid("055a 444 285"), False, "--err-t11--")
```

Myślniki powodują, że numer jest niepoprawny.

```python
    def test_dashes_are_not_valid(self):
        self.assertEqual(is_valid("055-444-285"), False, "--err-t12--")
```

Znak interpunkcyjny powoduje, że numer jest niepoprawny.

```python
    def test_punctuation_is_not_valid(self):
        self.assertEqual(is_valid(":9"), False, "--err-t13--")
```

Symbole powodują, że numer jest niepoprawny.

```python
    def test_symbols_are_not_valid(self):
        self.assertEqual(is_valid("055# 444$ 285"), False, "--err-t14--")
```

Pusty ciąg znaków nie jest poprawny.

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
