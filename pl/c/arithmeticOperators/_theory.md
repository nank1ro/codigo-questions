Operatory służą do wykonywania operacji na zmiennych i wartościach.
Zacznijmy od operatorów arytmetycznych, w szczególności od operatora **dodawania** `+`.
Służy on do dodawania dwóch liczb, na przykład:
```
>>> 5 + 3
8
```

---

Przejdźmy teraz do operatora **odejmowania** `-`.
Służy on do odejmowania jednej liczby od drugiej, na przykład:
```
>>> 5 - 3
2
```

---

Przyjrzyjmy się operatorowi **mnożenia** `*`.
Służy on do mnożenia dwóch liczb, na przykład:
```
>>> 5 * 3
15
```

---

Przyjrzyjmy się operatorowi **dzielenia** `/`.
Służy on do dzielenia dwóch liczb, na przykład:
```c
>>> 10 / 5
2
```

---

Przyjrzyjmy się operatorowi **modulo** `%`.
Służy on do wyznaczania reszty z dzielenia dwóch liczb, na przykład:
```
>>> 5 % 2
1
```
Wynik wynosi 1, ponieważ 5 podzielone przez 2 daje iloraz 2 i resztę 1
```
>>> 9 % 3
0
```
Ten wynik to 0, ponieważ 9 podzielone przez 3 daje iloraz 3 i resztę 0

---

C nie ma operatora **potęgowania**, dlatego musimy użyć funkcji `pow()` dostępnej w bibliotece `math.h`.
Potęgowanie odpowiada wielokrotnemu mnożeniu podstawy: tzn. **b** z wykładnikiem *n* to iloczyn *n* podstaw:
![exponentiation](https://bit.ly/3zcz6Lt)
```
>>> pow(5, 2);
25
```

---

Przyjrzyjmy się **dzieleniu całkowitemu** z użyciem funkcji `floor()`.
Funkcja ta zwraca całkowitą część ilorazu, na przykład:
```
>>> 5.0 / 2
2.5
>>> floor(2.5)
2.0
```
Znane również jako dzielenie całkowite. Wynik jest liczbą całkowitą, choć *typ* wyniku niekoniecznie jest int.
