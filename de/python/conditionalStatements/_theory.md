Entscheidungen sind erforderlich, wenn wir Code nur dann ausführen möchten, wenn eine bestimmte Bedingung erfüllt ist.
Nehmen wir an, wir möchten nur draußen spielen, wenn das Wetter schön ist.
In der Programmierung können wir eine boolesche Variable `nice_weather` speichern und die Aktion des Spielens draußen ausführen, wenn diese Variable `True` ist, wie hier:
```python
nice_weather = True
if (nice_weather):
    # draußen spielen
```

---

Wir fahren mit dem vorherigen Beispiel fort.
```python
nice_weather = True
if (nice_weather):
    # draußen spielen
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
    # draußen spielen
else:
    # zu Hause bleiben
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

---

Jede bedingte Anweisung braucht das Schlüsselwort `if`, um sie einzuleiten. Es teilt Python mit, dass der darunterliegende Block nur ausgeführt wird, wenn eine Bedingung zutrifft.

---

Eine Bedingung muss kein Vergleich sein — auch ein boolescher Wert wie `True` allein funktioniert, und der Block wird immer dann ausgeführt, wenn dieser Wert `True` ist.

---

Dieselbe Anweisung kann dazu gebracht werden, ihren Block zu überspringen, indem man nur die Bedingung ändert: Sobald sie zu `False` ausgewertet wird, springt Python direkt über den eingerückten Code hinweg.

---

Eine `if`-Zeile in Python besteht aus drei Teilen: dem Schlüsselwort `if`, einer Bedingung und dem Doppelpunkt, der die Zeile abschließt. Alles, was nach diesem Doppelpunkt eingerückt ist, gehört zum Block.

---

Da die Bedingung hier `True` ist, führt Python die darunter eingerückte Zeile aus und gibt `Hello!` aus.

---

Eine `False`-Bedingung bedeutet, dass Python den eingerückten Block nie betritt, sodass gar nichts ausgegeben wird.

---

Der Wert, der entscheidet, ob ein Block ausgeführt wird, heißt Bedingung, und er muss immer zu einem booleschen Wert ausgewertet werden, `True` oder `False`.

---

Der Block unter einem `if` darf nie leer sein: Python löst einen `IndentationError` aus, wenn dem Doppelpunkt keine eingerückte Zeile folgt. `pass` ist der übliche Platzhalter, wenn es noch nichts auszuführen gibt.

---

Der Doppelpunkt gehört zur `if`-Zeile und nicht zum Block: Er markiert das Ende der Bedingung und kündigt an, dass die darunter eingerückten Zeilen Teil der Anweisung sind.

---

Ist eine Bedingung `False`, überspringt Python den gesamten eingerückten Block und fährt bei der nächsten Zeile fort, die nicht unter dem `if` eingerückt ist.

---

Python verlangt keine Klammern um eine Bedingung — `if True:` ist für sich allein eine vollständige Anweisung. Klammern sind hier eine gewöhnliche Gruppierung, dieselbe Art, die auch in der Arithmetik verwendet wird, und sie lassen den Wert unverändert.

---

Ein Code-Block kann mehr als eine Zeile enthalten, und die Zeilen werden in der Reihenfolge ausgeführt, in der sie geschrieben sind — eine Anweisung, die oberhalb einer bestehenden hinzugefügt wird, gibt zuerst aus.

---

Eine boolesche Variable kann ganz allein als Bedingung verwendet werden — sie muss nicht erst mit `True` oder `False` verglichen werden.

---

Ist die Bedingung eine Variable, liest `if` genau das aus, was diese Variable in diesem Moment enthält. Es reicht, die Zuweisung weiter oben zu ändern, um den Block abzuschalten, ohne die `if`-Zeile überhaupt anzufassen.

---

Die eingerückten Zeilen, die zu einer bedingten Anweisung gehören, nennt man ihren Code-Block — die Einrückung ist es, die sie als Teil davon kennzeichnet.

---

Eine Zeile, die außerhalb der Einrückung des `if` steht, wird unabhängig von der Bedingung ausgeführt, da sie nie Teil dieses Blocks war.

---

Ein Code-Block ist nicht auf eine Zeile beschränkt — er kann so kurz oder so lang sein, wie es die Logik erfordert, solange jede Zeile konsequent eingerückt bleibt.

---

Ist `online` auf `False` gesetzt, trifft die Bedingung nie zu, also wird der Block übersprungen und nichts wird ausgegeben.

---

Nur das eingerückte `print` direkt nach dem `if` gehört zu seinem Block; eine Zeile, die auf derselben Einrückungsebene wie das `if` selbst steht, gehört nicht dazu.

---

Eine Zeile, die nach dem `if`-Block steht, aber ohne zusätzliche Einrückung, gehört nicht mehr dazu — sie wird jedes Mal ausgeführt, unabhängig von der Bedingung.

---

Ein Block kann eine beliebige Anzahl von Anweisungen enthalten. Sie werden von oben nach unten ausgeführt, und jede muss auf derselben Ebene eingerückt sein wie die anderen.

---

Weist man der Variable `True` zu, trifft die Bedingung zu, in die sie einfließt, also wird der darunterliegende Block ausgeführt.

---

Weist man stattdessen `False` zu, trifft die Bedingung nicht zu, also wird der darunterliegende Block vollständig übersprungen.

---

Das Schlüsselwort `if` ist es, das eine bedingte Anweisung einleitet — zusammen mit seiner Bedingung entscheidet es, ob der darunterliegende Block ausgeführt wird.

---

`"False"` in Anführungszeichen ist eine Zeichenkette, kein boolescher Wert, und eine nicht leere Zeichenkette zählt immer als wahr. Nur das bloße `False` verhindert, dass ein Block ausgeführt wird.
```python
print(bool("False"))  # True
```

---

Wählt man hier `True`, werden beide Zeilen im Block ausgeführt, nicht nur die erste — alles, was unter dem `if` eingerückt ist, gehört zum selben Block.

---

Der Doppelpunkt ist der eine Teil, auf den eine `if`-Zeile nicht verzichten kann: Er schließt die Bedingung ab und eröffnet den Block. Klammern um die Bedingung sind in Python optional, sodass sich `if True:` und `if (True):` identisch verhalten.

---

Anweisungen wie `if`, `elif` und `else`, die Code je nach einem booleschen Wert ausführen oder überspringen, werden zusammenfassend als bedingte Anweisungen bezeichnet.

---

Der Operator `not` kehrt einen booleschen Wert um: `not True` ergibt `False`, und `not False` ergibt `True`.
```python
is_online = False
print(not is_online)  # True
```

---

`not` erzeugt einen neuen booleschen Wert, statt den zu verändern, den es liest. Nach `is_afternoon = not is_morning` enthält die Variable `is_morning` also weiterhin ihren ursprünglichen Wert.

---

Eine Bedingung steht immer zwischen dem Schlüsselwort `if` und dem darauffolgenden Doppelpunkt, nirgendwo sonst in der Zeile.

---

Es gibt keine feste Grenze dafür, wie viele Zeilen ein `if`-Block enthalten kann — wichtig ist nur, dass jede Zeile auf derselben Ebene eingerückt bleibt.

---

Ein boolesches Literal ist eine völlig gültige Bedingung: `if True:` führt seinen Block jedes Mal aus. Als `if (True):` geschrieben ist es genau dieselbe Anweisung, da Klammern um eine Bedingung in Python optional sind.

---

Der Code-Block einer `if`-Anweisung ist die Gruppe der darunter eingerückten Zeilen, die durch diese Einrückung vom Rest des Programms abgegrenzt wird.

---

Eine Bedingung lässt sich immer auf einen von zwei Werten reduzieren, `True` oder `False` — genau das macht sie zu einem booleschen Wert.
