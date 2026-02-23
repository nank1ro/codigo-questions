---
language: python
exerciseType: 1
title: 100 doors
difficulty: 1
---

# --description--

Es gibt 100 Türen in einer Reihe, die alle zunächst geschlossen sind.
Sie gehen 100 Mal an den Türen vorbei.
Beim ersten Mal besuchen Sie jede Tür und "schalten" sie um (wenn die Tür geschlossen ist, öffnen Sie sie; wenn sie offen ist, schließen Sie sie).
Beim zweiten Mal besuchen Sie nur jede 2. Tür (d. h. Tür Nr. 2, Nr. 4, Nr. 6, ...) und schalten sie um.
Beim dritten Mal besuchen Sie jede 3. Tür (d. h. Tür Nr. 3, Nr. 6, Nr. 9, ...), und so weiter, bis Sie nur die 100. Tür besuchen.

# --instructions--

Implementieren Sie eine Funktion, um den Zustand der Türen nach dem letzten Durchgang zu bestimmen.
Geben Sie das Endergebnis in einem Array zurück, wobei nur die Türnummer in das Array aufgenommen wird, wenn sie offen ist.
> Die Methode muss mit einer variablen Anzahl von Türen funktionieren.

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

Bei 100 Türen die korrekte Liste der offenen Türen zurückgeben

```python
    def test_1(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(get_final_opened_doors(100), solution, "--err-t1--")
```

Bei 10 Türen die korrekte Liste der offenen Türen zurückgeben

```python
    def test_2(self):
        solution = [1, 4, 9]
        self.assertEqual(get_final_opened_doors(10), solution, "--err-t2--")
```

Bei 950 Türen die korrekte Liste der offenen Türen zurückgeben

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
