---
language: python
exerciseType: 1
difficulty: 2
title: Binäre Suche
---

# --description--

Die binäre Suche findet einen Wert in einer **sortierten** Sammlung, indem sie den Suchbereich wiederholt halbiert: Sieh dir das Element in der Mitte an, und wenn es nicht das gesuchte ist, mach in der linken Hälfte weiter, wenn der gesuchte Wert kleiner ist, oder in der rechten Hälfte, wenn er größer ist.

Da jeder Schritt die Hälfte der verbleibenden Elemente verwirft, erreicht die binäre Suche die Antwort selbst bei sehr großen Sammlungen mit einer Handvoll Vergleichen, während das Prüfen der Elemente eines nach dem anderen so viele Schritte kosten würde, wie es Elemente gibt.

# --instructions--

Schreibe eine Funktion `binary_search`, die eine aufsteigend sortierte Liste von ganzen Zahlen und eine gesuchte ganze Zahl entgegennimmt und den Index der gesuchten Zahl in der Liste zurückgibt oder `-1`, wenn die Zahl nicht vorhanden ist.

Die Liste enthält niemals Duplikate, der Index ist also immer eindeutig. Die Liste kann auch leer sein. Deine Funktion muss die binäre Suche verwenden und den Suchbereich bei jedem Schritt halbieren, statt linear zu suchen.

Beispiel für einen Funktionsaufruf:
```python
print(binary_search([1, 3, 5, 7], 5))
# gibt 2 aus
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

Die Suche in einer leeren Liste muss -1 zurückgeben

```python
    def test1(self):
        self.assertEqual(binary_search([], 7), -1, "--err-t1--")
```

Die Suche nach 5 in `[5]` muss 0 zurückgeben

```python
    def test2(self):
        self.assertEqual(binary_search([5], 5), 0, "--err-t2--")
```

Die Suche nach 9 in `[5]` muss -1 zurückgeben

```python
    def test3(self):
        self.assertEqual(binary_search([5], 9), -1, "--err-t3--")
```

Das erste Element -9 der 12-elementigen Liste muss am Index 0 gefunden werden

```python
    def test4(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -9), 0, "--err-t4--")
```

Das letzte Element 78 der 12-elementigen Liste muss am Index 11 gefunden werden

```python
    def test5(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 78), 11, "--err-t5--")
```

Das Element 15 muss am Index 6 gefunden werden

```python
    def test6(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 15), 6, "--err-t6--")
```

Das Element 22 muss am Index 7 gefunden werden

```python
    def test7(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 22), 7, "--err-t7--")
```

Der Wert 12, der zwischen 11 und 15 liegt, muss -1 zurückgeben

```python
    def test8(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], 12), -1, "--err-t8--")
```

Ein gesuchter Wert, der kleiner als jedes Element ist, muss -1 zurückgeben

```python
    def test9(self):
        self.assertEqual(binary_search([-9, -4, 0, 3, 7, 11, 15, 22, 38, 45, 61, 78], -100), -1, "--err-t9--")
```

Ein gesuchter Wert, der größer als jedes Element ist, muss -1 zurückgeben

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
