---
language: python
exerciseType: 1
title: 100 doors
difficulty: 1
---

# --description--

Ci sono 100 porte in fila che inizialmente sono tutte chiuse.
Fai 100 passaggi davanti alle porte.
La prima volta che passi, visita ogni porta e "alterna" la porta (se la porta è chiusa, aprila; se è aperta, chiudila).
La seconda volta, visita solo ogni 2a porta (cioè la porta #2, #4, #6, ...) e modificala.
La terza volta, visita ogni 3a porta (cioè la porta #3, #6, #9, ...), etc., fino a visitare solo la 100esima porta.

# --instructions--

Implementa una funzione per determinare lo stato delle porte dopo l'ultimo passaggio.
Restituire il risultato finale in un array, con solo il numero delle porte aperte.
> Il metodo deve essere in grado di funzionare con un numero variabile di porte.

# --seed--

```python
def calcola_porte_aperte(num_porte):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Date 100 porte, restituire l'elenco corretto delle porte aperte

```python
    def test_1(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(calcola_porte_aperte(100), solution, "--err-t1--")
```

Date 10 porte, restituire l'elenco corretto delle porte aperte

```python
    def test_2(self):
        solution = [1, 4, 9]
        self.assertEqual(calcola_porte_aperte(10), solution, "--err-t2--")
```

Date 950 porte, restituire l'elenco corretto delle porte aperte

```python
    def test_3(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400, 441, 484, 529, 576, 625, 676, 729, 784, 841, 900]
        self.assertEqual(calcola_porte_aperte(950), solution, "--err-t3--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def calcola_porte_aperte(num_porte):
    porte_aperte = []
    i = 1;
    while (i**2) <= num_porte:
        porte_aperte.append(i**2)
        i += 1
    return porte_aperte
```
