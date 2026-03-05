Wir wissen, wie man Code mit einer `while`-Schleife wiederholt.
So wird beispielsweise ein Programm, das Anweisungen wiederholt, um `hello` anzuzeigen:
```swift
var counter = 0

while counter < 5 {
    print("hello")
    counter += 1;
}
```
Das können wir aber auch mit `for`-Schleifen machen:
```swift
for i in 0..<5 {
    print("hello")
}
```

---

In einer `for`-Schleife können wir festlegen, wie oft wir die Schleife ausführen möchten

---

Wir können `..<` verwenden, um bis zur nächsten Nummer ausgeschlossen zu schleifen, oder `...` um bis zur nächsten Nummer eingeschlossen zu schleifen

---

Die Variable namens `i` ist die Zählervariable.
Wir können ihr den Namen geben, den wir möchten.
Sie zählt, in welcher Wiederholung der Schleife wir uns gerade befinden

---

Die Funktion `stride()` gibt eine Sequenz von Zahlen zurück.
Sie benötigt die Parameter _from_, _to_ und _by_.
Dies ist die Syntax der Funktion:
```swift
stride(from:to:by:)
```
Beachten Sie, dass der Wert `to` ausgeschlossen ist

---

Mit der Funktion `stride()` können wir auch geschlossene Bereiche verwenden, indem wir:
```swift
stride(from:through:by:)
```
In diesem Fall ist der Wert `through` enthalten

---

In Swift haben wir auch die `forEach`-Schleife.
Tatsächlich ruft `forEach` den angegebenen Abschluss für jedes Element in der Sequenz in derselben Reihenfolge wie eine `for-in`-Schleife auf:
```swift
// this is an array, we'll see about that soon
let numbers: [Int] = [1, 3, 5, 7, 9]
numbers.forEach { num in
    print(num)
}
```
Die Verwendung der Methode `forEach` unterscheidet sich in zwei wichtigen Punkten von einer `for-in`-Schleife:
1. Die Anweisung `break` oder `continue` kann nicht verwendet werden, um den aktuellen Aufruf des Body-Abschlusses zu beenden oder nachfolgende Aufrufe zu überspringen.
2. Die Verwendung der Anweisung `return` im Body-Abschluss beendet nur den Abschluss und nicht den äußeren Bereich, und es überspringt keine nachfolgenden Aufrufe.
