_Interpolacja_ ciągów znaków to programowy sposób generowania ciągu.
W Dart możemy używać znaku `+` (konkatenacja), aby wyświetlać dwa lub więcej ciągów razem, na przykład:
```dart
print("Hello " + "Dart!");
// prints "Hello Dart!"
```

---

Jednak używanie znaku `+` do dodania liczby jak '10' do ciągu jak `"friends"` powoduje błąd, ponieważ są to różne rodzaje wartości

---

Interpolacja ciągów znaków pozwala nam wyświetlać wyrażenia takie jak dodawanie ciągu do liczby, bez żadnego błędu.
Umieszczenie wyrażenia wewnątrz `${}` powoduje jego wykonanie.
Zwracana wartość jest konwertowana na ciąg i wstawiana do wynikowego ciągu

---

Jeśli umieścisz `$` przed nazwą identyfikatora, interpolacja ciągu wstawi zawartość tego identyfikatora do `String`

---

Jeśli to, co następuje po znaku `$`, nie jest rozpoznawalne jako identyfikator programu, napotkasz błąd

---

Możemy też wstawiać zmienne po znakach dolara, aby pokazać ich wartość

---

Możemy używać nawiasów klamrowych, aby wstawiać wartości tyle razy, ile chcemy, używając interpolacji ciągów

---

Wewnątrz `${}` możemy też umieszczać warunki, na przykład:
```dart
print("The answer is ${true ? "correct": "wrong"}");
// prints The answer is correct
```

---

Interpolacja ciągów najlepiej sprawdza się w instrukcjach print, ale możemy też przechowywać je w zmiennych jak zwykłe ciągi.
