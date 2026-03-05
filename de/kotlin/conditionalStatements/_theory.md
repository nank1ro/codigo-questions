Entscheidungen sind erforderlich, wenn wir Code nur dann ausführen möchten, wenn eine bestimmte Bedingung erfüllt ist.
Nehmen wir an, wir möchten nur dann nach draußen spielen, wenn das Wetter schön ist.
In der Programmierung können wir eine boolesche Variable `niceWeather` speichern und die Aktion zum Spielen draußen durchführen, `if` diese Variable `true` ist, wie:
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```

---

Lassen Sie uns das vorherige Beispiel fortsetzen.
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
}
```
Wir haben gesehen, dass die `if`-Anweisung den Codeblock nur dann ausführt, wenn die Bedingung `true` ist.
Ein weiteres wichtiges Merkmal sind die **geschwungenen Klammern** `{}`, die einen Codeblock kennzeichnen.

---

Wir haben gerade gesehen, wie man einen Codeblock ausführt, wenn eine Bedingung eintritt. Jetzt schauen wir, wie man einen anderen Codeblock ausführt, wenn die erste Bedingung fehlschlägt.
Wir gehen nach draußen spielen, wenn das Wetter schön ist; ansonsten bleiben wir zu Hause.
In Kotlin können wir die `else`-Anweisung verwenden, wie:
```kotlin
var niceWeather = true
if (niceWeather) {
    // play outside
} else {
    // stay home
}
```

---

Nehmen wir an, wir haben eine weitere Bedingung zu überprüfen, wie in diesem Beispiel:
```kotlin
var num = 3
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else {
    println("do something else")
}
```
und die Ausgabe dieses Codes ist `the number is 3`.
Zunächst prüfen wir, ob die Zahl gleich 2 ist, das ist falsch.
Also gehen wir zur zweiten Anweisung über und prüfen, ob `num` gleich 3 ist, da dies wahr ist, führen wir den folgenden Codeblock aus, indem wir `the number is 3` ausgeben.

---

Wir können so viele `else if`-Anweisungen hinzufügen, wie wir möchten, es gibt keine Grenzen.
```kotlin
var num = 4
if (num == 2) {
    println("the number is 2")
} else if (num == 3) {
    println("the number is 3")
} else if (num == 4) {
    println("the number is 4")
} else if (num == 5) {
    println("the number is 5")
} else if (num == 6) {
    println("the number is 6")
}
```
und die Ausgabe dieses Codes ist `the number is 4`.

---

Wir können auch eine bedingte Anweisung (`if`, `else if` oder `else`) in eine andere bedingte Anweisung verschachteln, um eine komplexere Struktur zu erstellen.
```kotlin
var num = 4
if (num < 3) {
    println("the number is lower than 3")
} else {
    if (num == 3) {
        println("the number is 3")
    } else if (num == 4) {
        println("the number is 4")
    } else {
        println("the number is greather than 4")
    }
}
```
und die Ausgabe dieses Codes ist `the number is 4`.

---

Der _Elvis-Operator_ `a ?: b` entpackt ein optionales `a`, wenn es einen Wert enthält, oder gibt einen Standardwert `b` zurück, wenn `a` `null` ist.
Der Ausdruck `a` ist immer vom optionalen Typ.
Der Ausdruck `b` muss dem Typ entsprechen, der in a gespeichert ist.
Der Elvis-Operator ist eine Abkürzung für den folgenden Code:
```kotlin
if (a != null) a else b
```
