Ein **Kommentar** ist eine Notiz im Quellcode für die Menschen, die ihn lesen. Python ignoriert Kommentare vollständig, sie ändern also nie, was das Programm tut.

Der einzige Kommentar, den Python kennt, ist der **einzeilige Kommentar**: er beginnt mit `#` und reicht bis zum Ende der Zeile.
```python
# Greets the user
print("Hello")
```
Verwende Kommentare, um zu erklären, wofür ein Stück Code gedacht ist oder warum es so geschrieben wurde.

---

Ein Kommentar braucht keine eigene Zeile: er kann dem Code in derselben Zeile folgen. Das ist ein **Inline-Kommentar**, ein guter Platz für eine kurze Notiz zu genau dieser Anweisung:
```python
retries = 3  # give up after three attempts
```
Alles von `#` bis zum Ende der Zeile wird ignoriert, während der Code davor wie üblich läuft.

Der Styleguide von Python, **PEP 8**, verlangt hier etwas Abstand: mindestens **zwei Leerzeichen** zwischen dem Code und dem `#` und **ein Leerzeichen** nach dem `#`. Ein Kommentar in eigener Zeile braucht nur das Leerzeichen nach dem `#`.

---

Da Python Kommentare vollständig verwirft, ändert das Hinzufügen oder Löschen eines Kommentars nie, was ein Programm tut. Es läuft nur der Code, der **nicht** auskommentiert ist.

Deshalb ist `#` ein schneller Weg, eine Codezeile abzuschalten, ohne sie zu löschen. Das nennt man **Auskommentieren**:
```python
total = 10
# total = total + 5
print(total)  # prints 10
```
Die zweite Zeile ist jetzt ein Kommentar, `total` bleibt also `10`. Entfernt man das `#`, lebt die Zeile wieder auf.

Auskommentieren ist praktisch, während du experimentierst, aber denk ans Aufräumen: Code, der lange auskommentiert stehen bleibt, verwirrt nur die Person, die ihn als Nächstes liest.

---

Viele Sprachen haben eine zweite Art von Kommentar, einen **Blockkommentar**, der sich über mehrere Zeilen erstreckt, wie `/* ... */`. Eine solche Syntax hat Python nicht: `#` ist alles, was es gibt.

Braucht eine Erklärung mehr als eine Zeile, setze an den Anfang jeder Zeile ein `#`:
```python
# Prints the welcome banner.
# Called once when the app starts.
print("Welcome!")
```
Derselbe Trick kommentiert gleich mehrere Codezeilen auf einmal aus: ein `#` pro Zeile. Jeder Editor kann diese `#` für eine ganze Auswahl mit einem einzigen Shortcut hinzufügen oder entfernen, also kostet das weniger, als es aussieht.

---

Du wirst oft eine **Zeichenkette in dreifachen Anführungszeichen** sehen, die verwendet wird, als wäre sie ein Blockkommentar:
```python
"""
This looks like a comment,
but it is a string.
"""
print("done")
```
Eine Zeichenkette zwischen `"""` und `"""` kann sich über mehrere Zeilen erstrecken, und eine Zeichenkette, die für sich allein steht, ist eine gültige Anweisung: Python erzeugt sie, tut nichts mit ihr und wirft sie weg. Nichts wird ausgegeben, also sieht das Ergebnis wie ein Kommentar aus.

Ist es aber nicht. Es ist ein Zeichenkettenliteral, es gelten also weiterhin die Regeln für Anführungszeichen: ein unausgeglichenes Anführungszeichen oder ein falsches `"""` darin bricht das Programm, während in einem `#`-Kommentar alles erlaubt ist. Es kann auch versehentlich zu einem Docstring werden, wenn es zur ersten Anweisung einer Datei, einer Klasse oder einer Funktion wird. Überall sonst geht es einfach nirgendwohin: CPython wirft die gesamte Anweisung schon beim Kompilieren weg.

Um also Code abzuschalten, verwende `#`. Die Zeichenkette in dreifachen Anführungszeichen hat ihre eigene Aufgabe, die in der nächsten Übung beginnt.

---

Ist eine Zeichenkette die **erste Anweisung** innerhalb einer Funktion, behandelt Python sie als die Dokumentation dieser Funktion. Sie heißt **Docstring**:
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"
```
Konventionsgemäß wird ein Docstring in dreifachen doppelten Anführungszeichen, `"""`, geschrieben, selbst wenn er in eine Zeile passt, damit er später wachsen kann, ohne die Anführungszeichen zu ändern.

Schreibe die Zusammenfassung in der dritten Person, als würdest du die Funktion beschreiben: "Returns...", "Adds...", "Checks...". Der Docstring muss vor jeder anderen Anweisung im Körper stehen, sonst ist er nur eine gewöhnliche Zeichenkette.

---

Ein Docstring wird nicht weggeworfen: Python speichert ihn im `__doc__`-Attribut der Funktion, sodass das Programm seine eigene Dokumentation lesen kann, während es läuft:
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"

print(greet.__doc__)  # Returns the greeting for name.
```
Hat eine Funktion keinen Docstring, ist `__doc__` `None`. Das gibt `help(greet)` aus, und das zeigt ein Editor an, wenn du über den Namen fährst.

---

Auch eine Datei kann dokumentiert werden. Eine Zeichenkette, die als **allererste Anweisung der Datei** geschrieben wird, vor jedem Import oder jeder Definition, ist der **Modul-Docstring**: er sagt, wozu die ganze Datei da ist.
```python
"""Tools for working with rectangles."""

def area(width, height):
    """Returns the area of a rectangle."""
    return width * height
```
Nur die erste Anweisung zählt. Ein Kommentar darf darüber stehen, aber jeglicher echte Code dazwischen macht aus der Zeichenkette wieder eine gewöhnliche, nutzlose Zeichenkette.

---

Klassen funktionieren genauso: steht eine Zeichenkette als erste Anweisung eines Klassenkörpers, ist sie der Docstring dieser Klasse und wird in `__doc__` gespeichert:
```python
class Point:
    """A point on a grid."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

print(Point.__doc__)  # A point on a grid.
```
Jede Methode innerhalb der Klasse kann ebenfalls einen eigenen Docstring haben, gelesen mit `Point.__init__.__doc__`. Die drei Stellen, die einen Docstring akzeptieren, sind also der Anfang eines Moduls, der Anfang einer Klasse und der Anfang einer Funktion.

---

Docstrings und `#`-Kommentare sehen ähnlich aus, beantworten aber unterschiedliche Fragen.

Ein **Docstring** ist für diejenigen, die den Code **verwenden**: was die Funktion tut, was sie erwartet und was sie zurückgibt. Er überlebt in `__doc__`, `help()` liest ihn, Editoren zeigen ihn an, und Dokumentationswerkzeuge sammeln ihn ein.

Ein **Kommentar** ist für diejenigen, die den Code **lesen**: warum diese Zeile so geschrieben ist, was die seltsame Zahl bedeutet, welchen Bug sie umgeht. Er existiert nur in der Quelldatei und ist weg, sobald das Programm läuft.

```python
def timeout():
    """Returns the number of seconds to wait for the server."""
    # the server drops idle connections after 35 seconds
    return 30
```
Also: Die Dokumentation der Funktion kommt in den Docstring, die Notizen zur Implementierung in Kommentare.

---

Reicht eine Zeile nicht, wächst ein Docstring zu einem festen Layout heran, beschrieben in **PEP 257**: eine einzeilige Zusammenfassung, eine Leerzeile, dann die Details, und das schließende `"""` in einer eigenen Zeile.
```python
def to_seconds(minutes):
    """Returns the number of seconds in the given minutes.

    minutes is a whole number and is never negative.
    """
    return minutes * 60
```
Die Leerzeile ist wichtig: Werkzeuge zeigen die erste Zeile für sich allein an, als kurze Beschreibung, und heben sich den Rest für diejenigen auf, die mehr lesen wollen.

---

Der Docstring muss die **erste Zeile des Körpers** sein, über jeder anderen Anweisung. Eine Zeichenkette, die nach dem `return` oder sonst irgendwo im Körper steht, ist nur eine Zeichenkette: `__doc__` bleibt `None` und kein Werkzeug wird sie je anzeigen.

---

Manche Kommentare folgen einer Konvention, die Editoren verstehen. Die häufigsten **Marker** sind:
- `# TODO: ...` markiert etwas, das noch geschrieben werden muss
- `# FIXME: ...` markiert Code, von dem bekannt ist, dass er falsch ist und korrigiert werden muss

```python
limit = 10
# TODO: read the limit from the settings
```
Für Python sind sie ganz normale Kommentare; Editoren sammeln sie in einem eigenen Panel ein, damit offene Arbeit leicht zu finden ist. Ein `TODO` steht meist neben einem Platzhalter, der das Programm laufen lässt, bis der echte Code geschrieben ist.

Wenn du die Arbeit abschließt, ersetze den Platzhalter und entferne den Marker in derselben Änderung, damit der Kommentar nie über den Zustand des Codes lügt.

---

Ein Kommentar über einer Funktion, der sagt, was die Funktion tut, ist am falschen Ort. Der Docstring ist der Platz dafür: er hängt an der Funktion, `help()` findet ihn und Editoren zeigen ihn an, während ein `#`-Kommentar über dem `def` für alle unsichtbar bleibt.

```python
# adds a and b
def add(a, b):
    return a + b
```
Verschiebt man denselben Satz eine Zeile nach unten, zwischen dreifache Anführungszeichen, wird daraus echte Dokumentation:
```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
```

---

Python sucht nach `#` nur im Code, niemals innerhalb einer **Zeichenkette**. Zwischen Anführungszeichen ist `#` ein ganz normales Zeichen:
```python
print("black is #000000")  # a hex colour
```
Das erste `#` ist Teil des Texts, das zweite startet einen echten Kommentar. Dasselbe gilt für `"""` innerhalb eines `#`-Kommentars: dort sind es nur drei Anführungszeichen, und es startet nichts.

---

Ein guter Kommentar erklärt, **warum** der Code etwas tut, nicht **was** er tut. Der Code zeigt bereits, was passiert; es in Worten zu wiederholen fügt nur Rauschen hinzu und veraltet, sobald sich der Code ändert:
```python
# set timeout to 30
timeout = 30
```
Der Grund hinter der Zahl ist das, was man als Leser nicht erraten kann:
```python
# the server drops idle connections after 35 seconds, so stop earlier
timeout = 30
```
Wiederholt ein Kommentar nur die Zeile unter ihm, lösche ihn oder ersetze ihn durch den Grund. Die besten Kommentare sind die, die etwas sagen, das der Code nicht sagen kann.
