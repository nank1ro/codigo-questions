Entscheidungen sind erforderlich, wenn wir Code nur dann ausführen möchten, wenn eine bestimmte Bedingung erfüllt ist.
Nehmen wir an, wir möchten nur draußen spielen, wenn das Wetter schön ist.
In der Programmierung können wir eine boolesche Variable `nice_weather` speichern und die Aktion des Spielens draußen ausführen, wenn diese Variable `True` ist, wie hier:
```python
nice_weather = True
if (nice_weather):
    # play outside
```

---

Wir fahren mit dem vorherigen Beispiel fort.
```python
nice_weather = True
if (nice_weather):
    # play outside
```
Wir haben gesehen, dass die `if`-Anweisung den Code-Block nur dann ausführt, wenn die Bedingung `True` ist.
Eine weitere wichtige Sache ist der **Doppelpunkt** `:` und die **Einrückung**, die den Beginn eines Code-Blocks anzeigen.
Einrückung bezieht sich auf die Leerzeichen am Anfang einer Code-Zeile.
Während in anderen Programmiersprachen die Einrückung nur zur Lesbarkeit dient, ist die Einrückung in Python unverzichtbar.
Du kannst deine bevorzugte Anzahl von Leerzeichen verwenden (2, 4, 6, 8), wobei 4 bevorzugt wird.
Hier in der App schlagen wir vor, die **TAB**-Taste zu verwenden, um deine Code-Zeilen einzurücken

---

Wir haben gerade gesehen, wie man einen Code-Block ausführt, wenn eine Bedingung erfüllt ist, jetzt schauen wir uns an, wie man einen anderen Code-Block ausführt, wenn die erste Bedingung fehlschlägt.
Wir gehen draußen spielen, wenn das Wetter schön ist; ansonsten bleiben wir zu Hause.
In Python können wir die `else`-Anweisung verwenden, wie hier:
```python
nice_weather = True
if (nice_weather):
    # play outside
else:
    # stay home
```

---

Nehmen wir an, wir haben eine weitere Bedingung zu überprüfen, wie in diesem Beispiel:
```python
num = 3
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
else:
    print("do something else")
```
und die Ausgabe dieses Codes ist `the number is 3`.
Zunächst überprüfen wir, ob die Zahl gleich 2 ist, was falsch ist.
Dann fahren wir mit der zweiten Anweisung fort und überprüfen, ob `num` gleich 3 ist, was wahr ist, also führen wir den folgenden Code-Block aus, indem wir `the number is 3` ausgeben

---

Wir können so viele `elif`-Anweisungen hinzufügen, wie wir möchten, es gibt keine Grenzen
```python
num = 4
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
elif (num == 4):
    print("the number is 4")
elif (num == 5):
    print("the number is 5")
elif (num == 6):
    print("the number is 6")
```
und die Ausgabe dieses Codes ist `the number is 4`.

---

Wir können auch eine bedingte Anweisung (`if`, `elif` oder `else`) in eine andere bedingte Anweisung einbetten, um eine komplexere Struktur zu erstellen.
```python
num = 4
if (num < 3):
    print("the number is lower than 3")
else:
    if (num == 3):
        print("the number is 3")
    elif (num == 4):
        print("the number is 4")
    else:
        print("the number is greather than 4")
```
und die Ausgabe dieses Codes ist `the number is 4`.
