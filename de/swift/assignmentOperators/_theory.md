Wir haben bereits gelernt, dass wir das `=`-Zeichen verwenden können, um einer Variablen einen Wert zuzuweisen, wie folgt:
```swift
let a = 5
```

---

Wir haben bereits eine initialisierte Variable `total`
```swift
var total = 5
```
Angenommen, wir möchten die Zahl `2` zur Variablen `total` addieren, können wir schreiben
```swift
total = total + 2
```
Okay, es funktioniert! Aber es gibt eine kürzere Version, um dasselbe zu tun:
```swift
total += 2
```
Das Zeichen `+=` wird **Additionszuweisung** genannt.
Es addiert einen Wert zum Variablenwert und weist das Ergebnis dieser Variablen zu.

---

Genau wie bei der Additionszuweisung haben wir die **Subtraktionszuweisung** `-=`.
Die Funktionalität ist gleich, der einzige Unterschied ist, dass sie die Subtraktion durchführt.
Die folgenden sind genau gleich
```swift
var num = num - 5
// is equal to
num -= 5
```

---

Schauen wir uns den **Multiplikationszuweisungs**-Operator `*=` an.
Er multipliziert die Variable mit einem Wert und weist das Ergebnis dieser Variablen zu.
Die folgenden sind genau gleich
```swift
var num = num * 5
// is equal to
num *= 5
```

---

Schauen wir uns den **Divisionszuweisungs**-Operator `/=` an.
Er teilt die Variable durch einen Wert und weist das Ergebnis dieser Variablen zu.
Die folgenden sind genau gleich
```swift
num = num / 5
// is equal to
num /= 5
```

---

Schauen wir uns den **Restbetragszuweisungs**-Operator `%=` an.
Er berechnet den Rest zwischen der Variablen und einem Wert und weist das Ergebnis dieser Variablen zu.
Die folgenden sind genau gleich
```swift
num = num % 5
// is equal to
num %= 5
```
