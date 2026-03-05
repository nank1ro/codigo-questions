Ein String _template_ ist eine programmgesteuerte Möglichkeit, einen String zu generieren.
In Kotlin können wir das `+` Zeichen (Konkatenation) verwenden, um zwei oder mehr Strings zusammen anzuzeigen, wie:
```kotlin
println("Hello " + "Kotlin!")
// prints "Hello Kotlin!"
```

---

Aber das Verwenden des Zeichens `+`, um eine Zahl wie „10" zu einem String wie „friends" hinzuzufügen, erzeugt einen Fehler, da sie unterschiedliche Werttypen sind

---

String-Templates ermöglichen es uns, Ausdrücke wie das Hinzufügen eines Strings zu einer Zahl ohne Fehler anzuzeigen.
Das Platzieren eines Ausdrucks in `${}` wertet ihn aus.
Der Rückgabewert wird in einen String konvertiert und in den resultierenden String eingefügt

---

Wenn du ein $ vor einen Bezeichnernamen stellst, fügt das String-Template den Inhalt dieses Bezeichners in den String ein

---

Wenn das, was dem `$` Zeichen folgt, nicht als Programmbezeichner erkannt wird, passiert nichts Besonderes

---

Wir können auch Variablen nach den Dollarzeichen einfügen, um ihren Wert anzuzeigen

---

Wir können geschweifte Klammern verwenden, um Werte so oft wie wir möchten in die String-Templates einzufügen

---

Innerhalb der `${}` können wir auch Bedingungen einfügen, zum Beispiel:
```kotlin
println("${if (true) "Correct" else "Wrong"}")
// prints Correct
```

---

String-Templates werden am besten in print-Anweisungen verwendet, aber wir können sie auch wie normale Strings in Variablen speichern.
