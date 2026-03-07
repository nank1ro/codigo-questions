Już dowiedzieliśmy się, że do przypisania wartości do zmiennej możemy użyć znaku `=`, na przykład:
```swift
let a = 5
```

---

Mamy już zainicjowaną zmienną `total`
```swift
var total = 5
```
Powiedzmy, że chcemy dodać liczbę `2` do zmiennej `total`, możemy napisać
```swift
total = total + 2
```
Dobrze, działa! Ale istnieje krótsza wersja, która robi to samo:
```swift
total += 2
```
Znak `+=` nazywa się **przypisaniem dodawania**.
Dodaje wartość do wartości zmiennej i przypisuje wynik do tej zmiennej.

---

Podobnie jak w przypisaniu dodawania, mamy **przypisanie odejmowania** `-=`.
Funkcjonalność jest taka sama, jedyną różnicą jest to, że wykonuje odejmowanie.
Poniższe są dokładnie tym samym:
```swift
var num = num - 5
// is equal to
num -= 5
```

---

Przyjrzyjmy się operatorowi **przypisania mnożenia** `*=`.
Mnoży zmienną przez wartość i przypisuje wynik do tej zmiennej.
Poniższe są dokładnie tym samym:
```swift
var num = num * 5
// is equal to
num *= 5
```

---

Przyjrzyjmy się operatorowi **przypisania dzielenia** `/=`.
Dzieli zmienną przez wartość i przypisuje wynik do tej zmiennej.
Poniższe są dokładnie tym samym:
```swift
num = num / 5
// is equal to
num /= 5
```

---

Przyjrzyjmy się operatorowi **przypisania reszty** `%=`.
Oblicza resztę ze zmiennej i wartości, a wynik przypisuje do tej zmiennej.
Poniższe są dokładnie tym samym:
```swift
num = num % 5
// is equal to
num %= 5
```
