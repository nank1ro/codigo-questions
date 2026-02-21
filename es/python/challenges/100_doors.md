---
language: python
exerciseType: 1
title: 100 puertas
difficulty: 1
---

# --description--

Hay 100 puertas en una fila que todas están inicialmente cerradas.
Haces 100 pasadas por las puertas.
La primera vez, visita cada puerta y 'alterna' la puerta (si la puerta está cerrada, ábrela; si está abierta, ciérrala).
La segunda vez, solo visita cada 2ª puerta (es decir, puerta #2, #4, #6, ...) y altérnala.
La tercera vez, visita cada 3ª puerta (es decir, puerta #3, #6, #9, ...), etc., hasta que solo visites la puerta 100.

# --instructions--

Implementa una función para determinar el estado de las puertas después de la última pasada.
Devuelve el resultado final en un arreglo, con solo el número de puerta incluido en el arreglo si está abierta.
> El método debe poder funcionar con un número variable de puertas.

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

Dadas 100 puertas, devuelve la lista correcta de puertas abiertas

```python
    def test_1(self):
        solution = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
        self.assertEqual(get_final_opened_doors(100), solution, "--err-t1--")
```

Dadas 10 puertas, devuelve la lista correcta de puertas abiertas

```python
    def test_2(self):
        solution = [1, 4, 9]
        self.assertEqual(get_final_opened_doors(10), solution, "--err-t2--")
```

Dadas 950 puertas, devuelve la lista correcta de puertas abiertas

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
