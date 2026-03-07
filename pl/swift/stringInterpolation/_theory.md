W Swift możemy używać znaku `+`, aby wyświetlić dwa lub więcej ciągów razem, na przykład:
```swift
print("Hello " + "Swift!") // prints "Hello Swift!"
```

---

Jednak użycie znaku `+` do dodania liczby, np. '10', do ciągu, np. ` "friends"`, powoduje błąd, ponieważ są to różne rodzaje wartości

---

Interpolacja ciągów pozwala nam wyświetlać wyrażenia, takie jak dodanie ciągu do liczby, bez żadnego błędu.

---

Każda interpolacja ciągów składa się z dwóch części: `\()`, gdzie wstawiamy liczbę lub zmienną, oraz normalny ciąg

---

Następnie dodajemy różny rodzaj wartości w nawiasach klamrowych, aby wyświetlić je jako jedno polecenie print. Tutaj z `\(5)`

---

Wstawianie zmiennych, takich jak `friends`, między nawiasy okrągłe wyświetla również ich wartość

---

Możemy używać nawiasów okrągłych do wstawiania wartości tyle razy, ile chcemy wewnątrz interpolacji ciągów

---

Interpolacje ciągów najlepiej stosować w instrukcjach print, ale możemy je również przechowywać w zmiennych jak zwykłe ciągi.
