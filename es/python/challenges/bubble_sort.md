---
language: python
exerciseType: 1
difficulty: 2
title: Ordenamiento burbuja
---

# --description--

El ordenamiento burbuja es uno de los algoritmos de ordenación más simples. Recorre una lista y compara cada par de elementos adyacentes, intercambiándolos siempre que están en el orden incorrecto. Después de cada pasada completa, el valor más grande que queda ha "burbujeado" hasta su posición final, y la lista está ordenada en cuanto una pasada termina sin un solo intercambio.

# --instructions--

Escribe una función llamada `bubble_sort` que reciba una lista de números enteros y devuelva una **nueva** lista con los mismos valores ordenados en orden ascendente. La lista que se pasa no debe ser modificada.

Debes implementar el algoritmo de ordenamiento burbuja tú mismo, comparando e intercambiando elementos adyacentes. No uses una función de ordenación de la biblioteca estándar.

Tu función también debe funcionar con un array vacío, un array con un solo elemento, un array que ya está ordenado, valores repetidos y números negativos.

Ejemplo de llamada de función:
```python
print(bubble_sort([3, 1, 2]))
# imprime [1, 2, 3]
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

Un array vacío debe devolver un array vacío

```python
    def test_1(self):
        self.assertEqual(bubble_sort([]), [], "--err-t1--")
```

Un array con un solo elemento debe quedar igual

```python
    def test_2(self):
        self.assertEqual(bubble_sort([42]), [42], "--err-t2--")
```

Un array ya ordenado debe mantener el mismo orden

```python
    def test_3(self):
        self.assertEqual(bubble_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5], "--err-t3--")
```

Un array ordenado a la inversa debe convertirse en orden ascendente

```python
    def test_4(self):
        self.assertEqual(bubble_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5], "--err-t4--")
```

Todos los valores repetidos deben conservarse

```python
    def test_5(self):
        self.assertEqual(bubble_sort([3, 1, 3, 2, 1]), [1, 1, 2, 3, 3], "--err-t5--")
```

Los números negativos deben ordenarse antes que los positivos

```python
    def test_6(self):
        self.assertEqual(bubble_sort([-5, 3, -1, 0, -9]), [-9, -5, -1, 0, 3], "--err-t6--")
```

Un array mixto más largo debe ordenarse en orden ascendente

```python
    def test_7(self):
        self.assertEqual(bubble_sort([9, -3, 14, 0, 7, -8, 2, 14, 5, -1, 11, 6]), [-8, -3, -1, 0, 2, 5, 6, 7, 9, 11, 14, 14], "--err-t7--")
```

El array que se pasa no debe ser modificado

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
