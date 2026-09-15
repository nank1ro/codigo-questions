---
language: python
exerciseType: 1
difficulty: 2
title: Búsqueda binaria
---

# --description--

La búsqueda binaria encuentra un valor dentro de una colección **ordenada** dividiendo repetidamente por la mitad el rango de búsqueda: mira el elemento del medio y, si no es el que buscas, continúa en la mitad izquierda cuando el valor buscado es menor o en la mitad derecha cuando es mayor.

Como cada paso descarta la mitad de los elementos restantes, la búsqueda binaria llega a la respuesta en unas pocas comparaciones incluso en colecciones muy grandes, mientras que comprobar los elementos uno por uno costaría tantos pasos como elementos haya.

# --instructions--

Escribe una función `binary_search` que recibe una lista de números enteros ordenada de forma ascendente y un número entero buscado, y devuelve el índice del valor buscado dentro de la lista, o `-1` cuando el valor no está presente.

La lista nunca contiene duplicados, por lo que el índice siempre es único. La lista también puede estar vacía. Tu función debe usar búsqueda binaria, dividiendo el rango de búsqueda por la mitad en cada paso, no un recorrido lineal.

Ejemplo de llamada de función:
```python
print(binary_search([1, 3, 5, 7], 5))
# imprime 2
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

Buscar en una lista vacía debe devolver -1

```python
    def test1(self):
        self.assertEqual(binary_search([], 7), -1, "--err-t1--")
```

Buscar 5 en `[5]` debe devolver 0

```python
    def test2(self):
        self.assertEqual(binary_search([5], 5), 0, "--err-t2--")
```

Buscar 9 en `[5]` debe devolver -1

```python
    def test3(self):
        self.assertEqual(binary_search([5], 9), -1, "--err-t3--")
```

El primer elemento -9 de la lista de 12 elementos debe encontrarse en el índice 0

```python
    def test4(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, "--err-t4--")
```

El último elemento 78 de la lista de 12 elementos debe encontrarse en el índice 11

```python
    def test5(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, "--err-t5--")
```

El elemento 15 debe encontrarse en el índice 6

```python
    def test6(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, "--err-t6--")
```

El elemento 22 debe encontrarse en el índice 7

```python
    def test7(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, "--err-t7--")
```

El valor 12, que está entre 11 y 15, debe devolver -1

```python
    def test8(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, "--err-t8--")
```

Un valor buscado menor que todos los elementos debe devolver -1

```python
    def test9(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, "--err-t9--")
```

Un valor buscado mayor que todos los elementos debe devolver -1

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
