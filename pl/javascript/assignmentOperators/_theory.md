Już wiemy, że aby przypisać wartość do zmiennej, możemy użyć znaku `=`, na przykład:
```javascript
let a = 5;
```

---

Mamy już zainicjowaną zmienną `total`
```javascript
var total = 5;
```
Powiedzmy, że chcemy dodać liczbę `2` do zmiennej `total`, możemy napisać
```javascript
total = total + 2;
```
Działa! Ale istnieje krótszy sposób na zrobienie tego samego:
```javascript
total += 2;
```
Znak `+=` nazywa się **operatorem przypisania z dodawaniem**.
Dodaje wartość do wartości zmiennej i przypisuje wynik do tej zmiennej.

---

Podobnie jak przy przypisaniu z dodawaniem, mamy **operator przypisania z odejmowaniem** `-=`.
Działanie jest takie samo, jedyna różnica polega na tym, że wykonuje odejmowanie.
Poniższe zapisy są równoważne:
```javascript
var num = num - 5;
// jest równoważne z
num -= 5;
```

---

Poznajmy operator **przypisania z mnożeniem** `*=`.
Mnoży zmienną przez wartość i przypisuje wynik do tej zmiennej.
Poniższe zapisy są równoważne:
```javascript
var num = num * 5;
// jest równoważne z
num *= 5;
```

---

Poznajmy operator **przypisania z dzieleniem** `/=`.
Dzieli zmienną przez wartość i przypisuje wynik do tej zmiennej.
Poniższe zapisy są równoważne:
```javascript
num = num / 5;
// jest równoważne z
num /= 5;
```

---

Poznajmy operator **przypisania z resztą** `%=`.
Oblicza resztę z dzielenia zmiennej przez wartość i przypisuje wynik do tej zmiennej.
Poniższe zapisy są równoważne:
```javascript
num = num % 5;
// jest równoważne z
num %= 5;
```
