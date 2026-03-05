Wir haben bereits gelernt, dass wir den `=`-Operator verwenden können, um einem Variablen einen Wert zuzuweisen, wie folgt:
```c
int a = 5;
```

---

Wir haben bereits eine initialisierte Variable `total`
```c
int total = 5;
```
Angenommen, wir wollen die Zahl `2` zur Variable `total` addieren, dann können wir schreiben
```c
total = total + 2;
```
Okay, das funktioniert! Aber es gibt eine kürzere Version für dasselbe:
```c
total += 2;
```
Das Zeichen `+=` wird **Additionszuweisung** genannt.
Es addiert einen Wert zum Variablenwert und weist das Ergebnis der Variablen zu.

---

Genau wie bei der Additionszuweisung haben wir die **Subtraktionszuweisung** `-=`.
Die Funktionalität ist dieselbe, der einzige Unterschied besteht darin, dass sie die Subtraktion durchführt.
Die folgenden sind genau gleich
```c
num = num - 5;
// ist gleich wie
num -= 5;
```

---

Schauen wir uns den **Multiplikationszuweisungs**-Operator `*=` an.
Er multipliziert die Variable mit einem Wert und weist das Ergebnis der Variablen zu.
Die folgenden sind genau gleich
```c
num = num * 5;
// ist gleich wie
num *= 5;
```

---

Schauen wir uns den **Divisionszuweisungs**-Operator `/=` an.
Er dividiert die Variable durch einen Wert und weist das Ergebnis der Variablen zu.
Die folgenden sind genau gleich
```c
num = num / 5;
// ist gleich wie
num /= 5;
```

---

Schauen wir uns den **Modulo-Zuweisungs**-Operator `%=` an.
Er berechnet den Modulo aus der Variablen und einem Wert und weist das Ergebnis der Variablen zu.
Die folgenden sind genau gleich
```c
num = num % 5;
// ist gleich wie
num %= 5;
```
