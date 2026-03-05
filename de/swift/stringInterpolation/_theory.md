In Swift können wir das `+`-Zeichen verwenden, um zwei oder mehr Strings zusammen anzuzeigen, wie hier:
```swift
print("Hello " + "Swift!") // prints "Hello Swift!"
```

---

Aber das `+`-Zeichen zu verwenden, um eine Zahl wie '10' zu einem String wie ` "friends"` hinzuzufügen, erzeugt einen Fehler, da sie verschiedene Arten von Werten sind

---

String-Interpolation ermöglicht es uns, Ausdrücke wie das Hinzufügen eines Strings zu einer Zahl anzuzeigen, ohne Fehler.

---

Jede String-Interpolations-Anweisung besteht aus zwei Teilen, der `\()`, in die wir die Zahl oder Variable einfügen, und dem normalen String

---

Danach fügen wir die verschiedene Art von Wert in geschweifte Klammern ein, damit sie als eine Print-Anweisung angezeigt wird. Wie hier, mit `\(5)`

---

Das Einfügen von Variablen wie `friends` zwischen den runden Klammern zeigt auch deren Wert an

---

Wir können runde Klammern verwenden, um Werte so oft einzufügen, wie wir möchten in der String-Interpolation

---

String-Interpolationen werden am besten in Print-Anweisungen verwendet, aber wir können sie auch wie normale Strings in Variablen speichern.
