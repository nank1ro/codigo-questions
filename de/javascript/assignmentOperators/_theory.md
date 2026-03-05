Wir haben bereits gelernt, dass wir das `=` Zeichen verwenden können, um einer Variable einen Wert zuzuweisen, wie:
```javascript
let a = 5;
```

---

Wir haben bereits eine initialisierte Variable `total`
```javascript
var total = 5;
```
Nehmen wir an, wir wollen die Zahl `2` zur Variable `total` addieren, wir können schreiben
```javascript
total = total + 2;
```
Okay, es funktioniert! Aber es gibt eine kürzere Version, um das Gleiche zu tun:
```javascript
total += 2;
```
Das Zeichen `+=` wird **Additionszuweisung** genannt.
Es addiert einen Wert zum Variablenwert und weist das Ergebnis dieser Variable zu.

---

Genau wie bei der Additionszuweisung haben wir die **Subtraktionszuweisung** `-=`.
Die Funktionalität ist dieselbe, der einzige Unterschied ist, dass sie die Subtraktion durchführt.
Die folgenden sind also genau gleich
```javascript
var num = num - 5;
// ist gleichbedeutend mit
num -= 5;
```

---

Schauen wir uns den **Multiplikationszuweisungs** Operator `*=` an.
Er multipliziert die Variable mit einem Wert und weist das Ergebnis dieser Variable zu.
Die folgenden sind also genau gleich
```javascript
var num = num * 5;
// ist gleichbedeutend mit
num *= 5;
```

---

Schauen wir uns den **Divisionszuweisungs** Operator `/=` an.
Er teilt die Variable durch einen Wert und weist das Ergebnis dieser Variable zu.
Die folgenden sind also genau gleich
```javascript
num = num / 5;
// ist gleichbedeutend mit
num /= 5;
```

---

Schauen wir uns den **Modulo-Zuweisungs** Operator `%=` an.
Er berechnet den Rest der Variable und eines Wertes und weist das Ergebnis dieser Variable zu.
Die folgenden sind also genau gleich
```javascript
num = num % 5;
// ist gleichbedeutend mit
num %= 5;
```
