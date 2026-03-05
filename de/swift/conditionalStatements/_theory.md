Entscheidungsfindung ist erforderlich, wenn wir Code nur ausführen möchten, wenn eine bestimmte Bedingung erfüllt ist.
Nehmen wir an, wir möchten nur nach draußen gehen, wenn das Wetter schön ist.
In der Programmierung können wir eine boolean-Variable `niceWeather` speichern und die Aktion "nach draußen gehen" ausführen `if` diese Variable `true` ist, wie:
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```

---

Lassen Sie uns mit dem vorherigen Beispiel fortfahren.
```swift
var niceWeather = true
if niceWeather {
    // play outside
}
```
Wir haben gesehen, dass die `if`-Aussage den Code-Block nur ausführt, wenn die Bedingung `true` ist.
Eine weitere wichtige Sache, die zu beachten ist, sind die **geschwungenen Klammern** `{}`, die einen Code-Block angeben.

---

Wir haben gerade gesehen, wie man einen Code-Block ausführt, wenn eine Bedingung eintritt. Jetzt schauen wir uns an, wie man einen anderen Code-Block ausführt, wenn die erste Bedingung fehlschlägt.
Wir gehen nach draußen spielen, wenn das Wetter schön ist; andernfalls bleiben wir zu Hause.
In Swift können wir die `else`-Aussage verwenden, wie:
```swift
var niceWeather = true
if niceWeather {
    // play outside
} else {
    // stay home
}
```

---

Nehmen wir an, wir haben eine weitere Bedingung zu überprüfen, wie in diesem Beispiel:
```swift
var num = 3
if num == 2 {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else {
    print("do something else")
}
```
und die Ausgabe dieses Codes ist `the number is 3`.
Zunächst überprüfen wir, ob die Zahl gleich 2 ist, das ist falsch.
Also gehen wir zur zweiten Aussage über und überprüfen, ob `num` gleich 3 ist, da dies wahr ist, führen wir den folgenden Code-Block aus, indem wir `the number is 3` drucken

---

Wir können so viele `else if`-Aussagen hinzufügen, wie wir möchten, es gibt keine Grenzen
```swift
var num = 4
if (num == 2) {
    print("the number is 2")
} else if num == 3 {
    print("the number is 3")
} else if (num == 4) {
    print("the number is 4")
} else if (num == 5) {
    print("the number is 5")
} else if (num == 6) {
    print("the number is 6")
}
```
und die Ausgabe dieses Codes ist `the number is 4`.

---

Wir können auch eine bedingte Aussage (`if`, `else if` oder `else`) in eine andere bedingte Aussage einbetten, um eine komplexere Struktur zu schaffen.
```swift
var num = 4
if num < 3 {
    print("the number is lower than 3")
} else {
    if num == 3 {
        print("the number is 3")
    } else if num == 4 {
        print("the number is 4")
    } else {
        print("the number is greather than 4")
    }
}
```
und die Ausgabe dieses Codes ist `the number is 4`.

---

Der ternäre bedingte Operator ist ein spezieller Operator mit drei Teilen, der die Form `question ? answer1 : answer2` hat.
Es ist eine Abkürzung zur Evaluierung eines von zwei Ausdrücken, je nachdem, ob `question` wahr oder falsch ist.
Wenn `question` wahr ist, evaluiert es `answer1` und gibt seinen Wert zurück; andernfalls evaluiert es `answer2` und gibt seinen Wert zurück.
```swift
let a = 10, b = 20, c: Int
if (a < b) {
    c = a
} else {
    c = b
}
print(c)
```
Der Kurzcode für den obigen Code ist:
```swift
let a = 10, b = 20, c: Int
c = a < b ? a : b
print(c)
```
`c` ist gleich `a`, weil die Bedingung `a < b` wahr war

---

Der _nil-coalescing operator_ `a ?? b` entpackt ein optionales `a`, wenn es einen Wert enthält, oder gibt einen Standardwert `b` zurück, wenn `a` `nil` ist.
Der Ausdruck `a` ist immer vom optionalen Typ.
Der Ausdruck `b` muss dem Typ entsprechen, der in a gespeichert ist.
Der nil-coalescing operator ist eine Abkürzung für den folgenden Code:
```swift
a != nil ? a! : b
```
