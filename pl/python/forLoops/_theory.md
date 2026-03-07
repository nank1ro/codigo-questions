Wiemy, jak powtarzać kod za pomocą pętli `while`.
Na przykład ten program wielokrotnie wyświetla `hello`:
```python
counter = 0

while counter < 5:
    print("hello")
    counter += 1
```
To samo możemy zrobić za pomocą pętli `for`:
```python
for i in range(5):
    print("hello")
```

---

W pętli `for` możemy określić, ile razy ma być wykonana pętla, za pomocą funkcji `range()`

---

Podanie liczby, np. `5`, wewnątrz funkcji `range()` oznacza, że pętla wykona blok kodu 5 razy, od `0` do `4`

---

Zmienna o nazwie `i` jest zmienną licznikową.
Możemy nadać jej dowolną nazwę.
Zlicza, na której iteracji pętli aktualnie się znajdujemy

---

Funkcja `range()` zwraca sekwencję liczb, domyślnie zaczynając od 0, zwiększając o 1 (domyślnie) i zatrzymując się przed podaną liczbą.
Oto składnia tej funkcji:
```python
range(start, stop, step)
```
`start` i `step` są opcjonalne, natomiast `stop` jest wymagane
