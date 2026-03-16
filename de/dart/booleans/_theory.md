Ein __Boolean__ ist ein Datentyp, der nur einen von zwei Werten halten kann: `true` oder `false`.
In Dart wird der Boolean-Typ mit dem Schlüsselwort `bool` deklariert.

```dart
bool isRaining = true;
```

Die Variable `isRaining` speichert den Wert `true`, was bedeutet, dass es derzeit regnet.
Boolesche Werte werden immer in Kleinbuchstaben geschrieben: `true` und `false`.

---

Genau wie jede andere Variable kannst du einen booleschen Wert mit `print()` ausgeben.
Wenn du einen booleschen Wert ausgibst, gibt Dart den Text `true` oder `false` aus.

```dart
bool isSunny = true;
print(isSunny); // true
```

---

Eine boolesche Variable kann auch den Wert `false` halten.
Verwende `false`, wenn etwas nicht der Fall ist.

```dart
bool isLoggedIn = false;
print(isLoggedIn); // false
```

Genau wie `true` muss auch `false` in Kleinbuchstaben geschrieben werden.

---

Der __Negationsoperator__ `!` (auch "nicht" genannt) kehrt einen booleschen Wert um.
Die Anwendung von `!` auf `true` ergibt `false`, und die Anwendung von `!` auf `false` ergibt `true`.

```dart
bool isActive = true;
print(!isActive); // false
```

Dies ist nützlich, wenn du das Gegenteil einer Bedingung überprüfen möchtest.

---

Boolesche Werte werden in der gesamten Programmierung verwendet, um Bedingungen darzustellen und Entscheidungen zu treffen.
Jedes Mal, wenn dein Programm zwischen zwei Möglichkeiten entscheiden muss, ist ein boolescher Wert beteiligt.

Beispiele:
- Ist der Benutzer angemeldet? (`isLoggedIn`)
- Ist die Tür offen? (`isDoorOpen`)
- Wurde die Bestellung versandt? (`isShipped`)
