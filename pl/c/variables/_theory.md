Zmienne to kontenery do przechowywania wartości danych.
Każda zmienna w C jest obiektem i podobnie jak w innych językach programowania, C ma polecenia do deklarowania zmiennej.
Aby utworzyć zmienną, musimy nadać jej **typ** i **nazwę**, pamiętając, że nie może zawierać spacji.
Zmienna jest tworzona w momencie pierwszego przypisania do niej wartości.
Przykład tworzenia zmiennej o nazwie `x`:
```c
int x = 1;
```
W ten sposób przypisaliśmy wartość `1` do zmiennej _całkowitoliczbowej_ o nazwie `x`.
Jeśli wyświetlimy zmienną `x`, otrzymamy z powrotem liczbę `1`:
```c
>>> printf("%i\n", x);
1
```

---

Zmienne są nazywane w ten sposób, ponieważ przechowywana przez nie wartość może się zmieniać.
Możemy zaktualizować `x` używając `=` i podając nową wartość.
```c
>>> x = 1;
>>> printf("%i\n", x);
1
>>> x = 2;
>>> printf("%i\n", x);
2
```

---

Możemy również nadawać zmiennym wartości innych zmiennych. Tutaj możemy nadać zmiennej `y` wartość `x`:
```c
>>> int x = 5;
>>> int y = x;
>>> printf("%i\n", y);
5
```

---

Kiedy aktualizujemy zmienną, zapomina ona swoją poprzednią wartość.
Tutaj możemy wyświetlić zmienną `x` dwa razy i zobaczyć, jak jej wartość się zmienia.
```c
>>> int x = 5;
>>> printf("%i\n", x);
5
>>> x = 10;
>>> printf("%i\n", x);
10
```

---

W C zmienne łańcuchowe mogą być deklarowane tylko przy użyciu podwójnych cudzysłowów:
```c
char x[] = "May";
```

---

Jeśli chcemy, aby nazwa zmiennej składała się z wielu słów, używamy **snake case**.
Oznacza to używanie `_` do łączenia kolejnych słów.
