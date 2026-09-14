---
language: python
exerciseType: 1
difficulty: 2
title: Ricerca binaria
---

# --description--

La ricerca binaria trova un valore all'interno di una collezione **ordinata** dimezzando ripetutamente l'intervallo di ricerca: guarda l'elemento centrale e, se non è quello che cerchi, continua nella metà sinistra quando il valore cercato è più piccolo o nella metà destra quando è più grande.

Poiché ogni passo scarta metà degli elementi rimanenti, la ricerca binaria arriva alla risposta in poche comparazioni anche su collezioni molto grandi, mentre controllare gli elementi uno per uno costerebbe tanti passi quanti sono gli elementi.

# --instructions--

Scrivi una funzione `binary_search` che riceve una lista di numeri interi ordinata in modo crescente e un numero intero cercato, e restituisce l'indice del valore cercato all'interno della lista, oppure `-1` quando il valore non è presente.

La lista non contiene mai duplicati, quindi l'indice è sempre unico. La lista può anche essere vuota. La tua funzione deve usare la ricerca binaria, dimezzando l'intervallo di ricerca a ogni passo, non una scansione lineare.

Esempio di chiamata di funzione:
```python
print(binary_search([1, 3, 5, 7], 5))
# prints 2
```

# --seed--

```python
def binary_search(arr, target):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

La ricerca in una lista vuota deve restituire -1

```python
    def test1(self):
        self.assertEqual(binary_search([], 7), -1, "--err-t1--")
```

La ricerca di 5 in `[5]` deve restituire 0

```python
    def test2(self):
        self.assertEqual(binary_search([5], 5), 0, "--err-t2--")
```

La ricerca di 9 in `[5]` deve restituire -1

```python
    def test3(self):
        self.assertEqual(binary_search([5], 9), -1, "--err-t3--")
```

Il primo elemento -9 della lista di 12 elementi deve essere trovato all'indice 0

```python
    def test4(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, "--err-t4--")
```

L'ultimo elemento 78 della lista di 12 elementi deve essere trovato all'indice 11

```python
    def test5(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, "--err-t5--")
```

L'elemento 15 deve essere trovato all'indice 6

```python
    def test6(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, "--err-t6--")
```

L'elemento 22 deve essere trovato all'indice 7

```python
    def test7(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, "--err-t7--")
```

Il valore 12, che si trova tra 11 e 15, deve restituire -1

```python
    def test8(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, "--err-t8--")
```

Un valore cercato più piccolo di ogni elemento deve restituire -1

```python
    def test9(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, "--err-t9--")
```

Un valore cercato più grande di ogni elemento deve restituire -1

```python
    def test10(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 100), -1, "--err-t10--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == target:
            return mid
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return -1
```
