---
language: python
exerciseType: 1
title: 100 drzwi
difficulty: 1
---

# --description--

W rzędzie stoi 100 drzwi, wszystkie początkowo zamknięte.
Wykonujesz 100 przejść obok drzwi.
Przy pierwszym przejściu odwiedzasz każde drzwi i 'przełączasz' je (jeśli drzwi są zamknięte, otwierasz je; jeśli są otwarte, zamykasz je).
Przy drugim przejściu odwiedzasz tylko co drugie drzwi (tj. drzwi nr 2, 4, 6, ...) i je przełączasz.
Przy trzecim przejściu odwiedzasz co trzecie drzwi (tj. drzwi nr 3, 6, 9, ...) itd., aż do odwiedzenia tylko 100. drzwi.

# --instructions--

Zaimplementuj funkcję określającą stan drzwi po ostatnim przejściu.
Zwróć końcowy wynik w tablicy, z numerem drzwi uwzględnionym w tablicy tylko wtedy, gdy są otwarte.
> Metoda musi być w stanie działać ze zmienną liczbą drzwi.

# --seed--

```python
def get_final_opened_doors(num_doors):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Dla 100 drzwi zwróć poprawną listę otwartych drzwi

```python
    def test_1(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(get_final_opened_doors(100), solution, "--err-t1--")
```

Dla 10 drzwi zwróć poprawną listę otwartych drzwi

```python
    def test_2(self):
        solution = [1, 4, 9]
        self.assertEqual(get_final_opened_doors(10), solution, "--err-t2--")
```

Dla 950 drzwi zwróć poprawną listę otwartych drzwi

```python
    def test_3(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        self.assertEqual(get_final_opened_doors(950), solution, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def get_final_opened_doors(num_doors):
    open_doors = []
    i = 1;
    while (i**2) <= num_doors:
        open_doors.append(i**2)
        i += 1
    return open_doors
```
