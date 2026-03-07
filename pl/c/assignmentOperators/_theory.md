Nauczyliśmy się już, że aby przypisać wartość do zmiennej, możemy użyć znaku `=`, na przykład:
```c
int a = 5;
```

---

Mamy już zainicjalizowaną zmienną `total`
```c
int total = 5;
```
Powiedzmy, że chcemy dodać liczbę `2` do zmiennej `total`, możemy napisać
```c
total = total + 2;
```
Dobrze, działa! Ale jest krótsza wersja, która robi to samo:
```c
total += 2;
```
Znak `+=` nazywa się **przypisaniem dodawania**.
Dodaje wartość do wartości zmiennej i przypisuje wynik do tej zmiennej.

---

Podobnie jak przy przypisaniu dodawania, mamy **przypisanie dekrementacji** `-=`.
Funkcjonalność jest taka sama, jedyna różnica polega na tym, że wykonuje odejmowanie.
Zatem poniższe są dokładnie tym samym
```c
num = num - 5;
// is equal to
num -= 5;
```

---

Zobaczmy operator **przypisania mnożenia** `*=`.
Mnoży zmienną przez wartość i przypisuje wynik do tej zmiennej.
Zatem poniższe są dokładnie tym samym
```c
num = num * 5;
// is equal to
num *= 5;
```

---

Zobaczmy operator **przypisania dzielenia** `/=`.
Dzieli zmienną przez wartość i przypisuje wynik do tej zmiennej.
Zatem poniższe są dokładnie tym samym
```c
num = num / 5;
// is equal to
num /= 5;
```

---

Zobaczmy operator **przypisania modulo** `%=`.
Oblicza resztę z dzielenia zmiennej przez wartość i przypisuje wynik do tej zmiennej.
Zatem poniższe są dokładnie tym samym
```c
num = num % 5;
// is equal to
num %= 5;
```
