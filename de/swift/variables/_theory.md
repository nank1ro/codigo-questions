Variablen sind Container zum Speichern von Datenwerten.
Jede Variable in Swift ist ein Objekt.
Um eine Variable zu erstellen, müssen wir ihr einen **Namen** geben und beachten, dass dieser keine Leerzeichen enthalten darf.
Eine Variable wird in dem Moment erstellt, in dem du ihr zum ersten Mal einen Wert zuweist.
In Swift deklarierst du Konstanten mit dem `let`-Schlüsselwort und Variablen mit dem `var`-Schlüsselwort.
Der Wert einer Konstante kann nicht geändert werden, sobald er gesetzt ist, während eine Variable in Zukunft auf einen anderen Wert gesetzt werden kann.
Ein Beispiel für die Erstellung einer Variable namens `x` ist:
```swift
var x = 1
```
Auf diese Weise haben wir der Variablen `x` den Wert `1` zugewiesen.
Wenn wir die Variable `x` ausgeben, bekommen wir die Zahl `1` zurück:
```swift
print(x) // prints 1
```

---

Variablen werden so genannt, weil sich der Wert, den sie speichern, ändern kann.
Wir können `x` mit Hilfe von `=` aktualisieren und ihm einen neuen Wert geben.
```swift
var x = 1
print(x) // prints 1
x = 2
print(x) // prints 2
```

---

Wir können Variablen auch die Werte anderer Variablen zuweisen. Hier können wir der Variablen `y` den Wert von `x` zuweisen.
```swift
var x = 5
var y = x
print(y) // prints 5
```

---

Wenn wir eine Variable aktualisieren, vergisst sie ihren vorherigen Wert. Hier können wir die Variable `x` zweimal anzeigen und sehen, wie sich ihr Wert aktualisiert.
```swift
var x = 5
print(x) // prints 5
x = 10
print(x) // prints 10
```

---

In Swift können String-Variablen nur mit Hilfe von doppelten Anführungszeichen deklariert werden:
```swift
let x = "May"
```

---

Wenn wir einen Variablennamen mit mehreren Wörtern möchten, verwenden wir **camelCase**.
Es ist die Praxis, Sätze so zu schreiben, dass jedes Wort in der Mitte des Satzes mit einem großen Buchstaben beginnt.
