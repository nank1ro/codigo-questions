Zmienne to kontenery do przechowywania wartości danych.
Każda zmienna w Pythonie jest obiektem i w odróżnieniu od innych języków programowania, Python nie ma polecenia do deklarowania zmiennej.
Aby utworzyć zmienną, musimy nadać jej **nazwę**, pamiętając, że nie może zawierać spacji.
Zmienna jest tworzona w momencie pierwszego przypisania do niej wartości.
Przykład tworzenia zmiennej o nazwie `x`:
```python
x = 1
```
W ten sposób przypisaliśmy wartość `1` do zmiennej o nazwie `x`.
Jeśli wydrukujemy zmienną `x`, otrzymamy liczbę `1`:
```python
>>> print(x)
1
```

---

Zmienne są tak nazwane, ponieważ wartość, którą przechowują, może się zmieniać.
Możemy zaktualizować `x` używając `=` i nadając mu nową wartość.
```python
>>> x = 1
>>> print(x)
1
>>> x = 2
>>> print(x)
2
```

---

Możemy również przypisywać zmiennym wartości innych zmiennych. Tutaj możemy przypisać zmiennej `y` wartość `x`
```python
>>> x = 5
>>> y = x
>>> print(y)
5
```

---

Kiedy aktualizujemy zmienną, zapomina ona swoją poprzednią wartość. Tutaj możemy wyświetlić zmienną `x` dwukrotnie i zobaczyć, jak jej wartość się zmienia.
```python
>>> x = 5
>>> print(x)
5
>>> x = 10
>>> print(x)
10
```

---

Zmienne tekstowe (string) można deklarować zarówno za pomocą pojedynczych, jak i podwójnych cudzysłowów:
```python
>>> x = "May"
>>> x = 'May'
```
Oba zapisy są równoważne.

---

Jeśli chcemy, aby nazwa zmiennej składała się z wielu słów, używamy **snake case**.
Oznacza to używanie `_` do łączenia kolejnych słów.
