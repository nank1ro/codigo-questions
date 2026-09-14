---
language: python
exerciseType: 1
difficulty: 2
title: Ordinamento a bolle
---

# --description--

L'ordinamento a bolle è uno degli algoritmi di ordinamento più semplici. Percorre una lista e confronta ogni coppia di elementi adiacenti, scambiandoli ogni volta che sono nell'ordine sbagliato. Dopo ogni passata completa il valore più grande rimasto è "salito a galla" fino alla sua posizione finale, e la lista è ordinata non appena una passata si conclude senza un solo scambio.

# --instructions--

Scrivi una funzione chiamata `bubble_sort` che prenda una lista di numeri interi e restituisca una **nuova** lista con gli stessi valori ordinati in ordine crescente. La lista passata non deve essere modificata.

Devi implementare tu stesso l'algoritmo di ordinamento a bolle, confrontando e scambiando elementi adiacenti. Non usare una funzione di ordinamento della libreria standard.

La tua funzione deve funzionare anche con un array vuoto, un array con un solo elemento, un array già ordinato, valori ripetuti e numeri negativi.

Esempio di chiamata di funzione:
```python
print(bubble_sort([3, 1, 2]))
# prints [1, 2, 3]
```

# --seed--

```python
def bubble_sort(arr):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Un array vuoto deve restituire un array vuoto

```python
    def test_1(self):
        self.assertEqual(bubble_sort([]), [], "--err-t1--")
```

Un array con un solo elemento deve rimanere uguale

```python
    def test_2(self):
        self.assertEqual(bubble_sort([42]), [42], "--err-t2--")
```

Un array già ordinato deve mantenere lo stesso ordine

```python
    def test_3(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "--err-t3--")
```

Un array ordinato al contrario deve essere messo in ordine crescente

```python
    def test_4(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "--err-t4--")
```

Tutti i valori ripetuti devono essere mantenuti

```python
    def test_5(self):
        self.assertEqual(bubble_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], "--err-t5--")
```

I numeri negativi devono essere ordinati prima di quelli positivi

```python
    def test_6(self):
        self.assertEqual(bubble_sort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], "--err-t6--")
```

Un array misto più lungo deve essere ordinato in ordine crescente

```python
    def test_7(self):
        self.assertEqual(bubble_sort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], "--err-t7--")
```

L'array passato non deve essere modificato

```python
    def test_8(self):
        original = [3, 1, 2]
        bubble_sort(original)
        self.assertEqual(original, [3, 1, 2], "--err-t8--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def bubble_sort(arr):
    result = list(arr)
    end = len(result)
    swapped = True
    while swapped:
        swapped = False
        for i in range(1, end):
            if result[i - 1] > result[i]:
                result[i - 1], result[i] = result[i], result[i - 1]
                swapped = True
        end -= 1
    return result
```
