Szablon tekstowy (_String template_) to programowy sposób generowania ciągu znaków.
W Kotlinie możemy użyć znaku `+` (konkatenacja) do wyświetlania dwóch lub więcej ciągów razem, na przykład:
```kotlin
println("Hello " + "Kotlin!")
// prints "Hello Kotlin!"
```

---

Jednak użycie znaku `+` do dodania liczby jak '10' do ciągu znaków jak `"friends"` powoduje błąd, ponieważ są to różne rodzaje wartości

---

Szablony tekstowe pozwalają nam wyświetlać wyrażenia, takie jak dodawanie ciągu do liczby, bez żadnych błędów.
Umieszczenie wyrażenia wewnątrz `${}` powoduje jego ewaluację.
Wartość zwracana jest konwertowana na ciąg znaków i wstawiana do wynikowego ciągu

---

Jeśli umieścisz `$` przed nazwą identyfikatora, szablon tekstowy wstawi zawartość tego identyfikatora do ciągu

---

Jeśli to, co następuje po znaku `$`, nie jest rozpoznawalne jako identyfikator programu, nic szczególnego się nie dzieje

---

Możemy również wstawiać zmienne po znakach dolara, aby wyświetlić ich wartości

---

Możemy używać nawiasów klamrowych do wstawiania wartości tak często, jak chcemy wewnątrz szablonów tekstowych

---

Wewnątrz `${}` możemy również umieszczać warunki, na przykład:
```kotlin
println("${if (true) "Correct" else "Wrong"}")
// prints Correct
```

---

Szablony tekstowe najlepiej stosować w instrukcjach wyświetlania, ale możemy je też przechowywać w zmiennych jak normalne ciągi znaków.
