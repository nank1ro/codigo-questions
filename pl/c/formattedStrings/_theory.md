W języku C używamy funkcji `printf` z wyrażeniem, aby wyświetlić dwie lub więcej wartości razem, na przykład:
```c
>>> char c = 'C';
>>> printf("Hello %c!\n", c);
Hello C!
```
`%c` służy do wyświetlania pojedynczego znaku

---

Sformatowane ciągi znaków pozwalają nam wyświetlać wyrażenia, takie jak łączenie ciągu z liczbą, bez żadnych błędów.
Do wyświetlania liczby całkowitej używamy wyrażenia `%i`

---

Każda instrukcja sformatowanego ciągu znaków składa się z dwóch części: tekstu, który chcemy umieścić, oraz wyrażenia, które chcemy sformatować wewnątrz tekstu

---

Następnie dodajemy inny rodzaj wartości. Jak tutaj, z `%i`

---

Wstawianie zmiennych takich jak `friends` wyświetla również ich wartość

---

Możemy używać wyrażeń do wstawiania wartości tak często, jak chcemy, wewnątrz sformatowanego ciągu znaków
