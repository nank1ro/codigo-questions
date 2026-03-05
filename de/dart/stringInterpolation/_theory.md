Eine String-_Interpolation_ ist eine programmatische Möglichkeit, einen String zu generieren.
In Dart können wir das `+`-Zeichen (Verkettung) verwenden, um zwei oder mehr Strings zusammen anzuzeigen, wie:
```dart
print("Hello " + "Dart!");
// prints "Hello Dart!"
```

---

Aber die Verwendung des Zeichens `+`, um eine Zahl wie '10' zu einem String wie ` "friends"` hinzuzufügen, führt zu einem Fehler, da es sich um unterschiedliche Arten von Werten handelt

---

String-Interpolation ermöglicht es uns, Ausdrücke wie das Hinzufügen eines Strings zu einer Zahl ohne Fehler anzuzeigen.
Ein Ausdruck in `${}` wird ausgewertet.
Der Rückgabewert wird in einen String konvertiert und in den resultierenden String eingefügt

---

Wenn Sie ein `$` vor einen Identifikatornamen setzen, wird die String-Interpolation den Inhalt dieses Identifikators in den `String` einfügen

---

Wenn das, was dem `$`-Zeichen folgt, nicht als Programmbezeichner erkennbar ist, erhalten Sie einen Fehler

---

Wir können auch Variablen nach den Dollarzeichen einfügen, um ihren Wert anzuzeigen

---

Wir können geschweifte Klammern verwenden, um Werte so oft einzufügen, wie wir möchten, mit der String-Interpolation

---

Innerhalb der `${}` können wir auch Bedingungen eingeben, zum Beispiel:
```dart
print("The answer is ${true ? "correct": "wrong"}");
// prints The answer is correct
```

---

String-Interpolation wird am besten in Print-Anweisungen verwendet, aber wir können sie auch in Variablen wie normale Strings speichern.
