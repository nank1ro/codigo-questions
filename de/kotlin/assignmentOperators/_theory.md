Zuweisungsoperatoren werden verwendet, um Variablen Werte zuzuweisen.
Der grundlegendste Zuweisungsoperator ist `=`, der den Wert auf der rechten Seite der Variablen auf der linken Seite zuweist:
```kotlin
var x = 10
```
Hier wird `10` der Variablen `x` zugewiesen.
Du kannst einer bestehenden Variablen auch einen neuen Wert zuweisen:
```kotlin
x = 20
```
Jetzt hält `x` den Wert `20`.

---

Der Operator `+=` ist eine Kurzschreibweise, die einen Wert zu einer Variablen addiert und das Ergebnis wieder zuweist.
Anstatt zu schreiben:
```kotlin
x = x + 5
```
Kann man schreiben:
```kotlin
x += 5
```
Beide Ausdrücke tun dasselbe: sie erhöhen den Wert von `x` um `5`.

---

Der Operator `-=` subtrahiert einen Wert von einer Variablen und weist das Ergebnis wieder zu.
Anstatt zu schreiben:
```kotlin
x = x - 3
```
Kann man schreiben:
```kotlin
x -= 3
```
Dadurch wird der Wert von `x` um `3` verringert.

---

Der Operator `*=` multipliziert eine Variable mit einem Wert und weist das Ergebnis wieder zu.
Anstatt zu schreiben:
```kotlin
x = x * 4
```
Kann man schreiben:
```kotlin
x *= 4
```
Dadurch wird `x` mit `4` multipliziert und das Ergebnis wieder in `x` gespeichert.

---

Der Operator `/=` dividiert eine Variable durch einen Wert und weist das Ergebnis wieder zu.
Anstatt zu schreiben:
```kotlin
x = x / 2
```
Kann man schreiben:
```kotlin
x /= 2
```
Hinweis: Wenn beide Operanden vom Typ `Int` sind, führt Kotlin eine **Ganzzahldivision** durch (der Nachkommaanteil wird abgeschnitten):
```kotlin
var x = 7
x /= 2
// x ist jetzt 3 (nicht 3.5)
```
