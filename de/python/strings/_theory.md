Eine **Zeichenkette** (String) ist ein Stück Text: eine Folge von Zeichen in Anführungszeichen.
Python akzeptiert sowohl einfache `'...'` als auch doppelte `"..."` Anführungszeichen, und beide funktionieren genau gleich:
```python
name = 'Ada'
language = "Python"
```
Die Wahl ist wichtig, wenn der Text selbst ein Anführungszeichen enthält.
Ein Apostroph in einfachen Anführungszeichen würde die Zeichenkette zu früh beenden. Verwende in diesem Fall doppelte Anführungszeichen:
```python
print("It's sunny")  # It's sunny
```

---

Die eingebaute Funktion `len()` gibt die **Länge** einer Zeichenkette zurück, also wie viele Zeichen sie enthält.
Leerzeichen und Satzzeichen zählen ebenfalls als Zeichen:
```python
print(len("hello"))     # 5
print(len("hi there"))  # 8
print(len(""))          # 0
```

---

Jedes Zeichen einer Zeichenkette hat eine Position, den sogenannten **Index**.
Indizes beginnen bei `0`, nicht bei `1`: das erste Zeichen hat den Index `0`, das zweite den Index `1`, und so weiter.
Schreibe den Index in eckigen Klammern nach der Zeichenkette, um ein einzelnes Zeichen zu lesen:
```python
word = "python"
print(word[0])  # p
print(word[1])  # y
print(word[5])  # n
```
Fragst du nach einem Index, der nicht existiert, wie `word[6]`, wird ein `IndexError` ausgelöst.

---

Indizes können auch **negativ** sein: sie zählen vom Ende der Zeichenkette aus.
`-1` ist das letzte Zeichen, `-2` das davor, und so weiter:
```python
word = "python"
print(word[-1])  # n
print(word[-2])  # o
```
Das ist praktisch, weil du die Länge der Zeichenkette nicht kennen musst, um ihr Ende zu erreichen.

---

Ein **Slice** extrahiert einen Teil einer Zeichenkette.
Schreibe `[start:end]` in eckigen Klammern: das Zeichen an Position `start` ist eingeschlossen, das an Position `end` ist **ausgeschlossen**:
```python
word = "python"
print(word[0:3])  # pyt
print(word[2:4])  # th
```
Du kannst `start` weglassen, um vom Anfang an zu schneiden, oder `end`, um bis zum Ende zu schneiden:
```python
print(word[:2])  # py
print(word[2:])  # thon
```
Slicing löst nie einen Fehler aus: ein `end`, das größer als die Länge ist, stoppt einfach beim letzten Zeichen.

---

Du weißt bereits, dass `+` zwei Zeichenketten zusammenfügt (**Verkettung**).
Der `*`-Operator **wiederholt** eine Zeichenkette eine bestimmte Anzahl von Malen:
```python
print("ab" * 3)        # ababab
print("=" * 10)        # ==========
print("Hi" + "!" * 3)  # Hi!!!
```
Wiederholung ist eine schnelle Möglichkeit, Trennlinien und einfache Muster zu zeichnen.

---

Der `in`-Operator prüft, ob eine Zeichenkette eine andere **enthält**.
Er gibt `True` oder `False` zurück und passt daher gut in ein `if`:
```python
email = "ada@mail.com"
print("@" in email)      # True
print("xyz" in email)    # False
if " " in email:
    print("No spaces allowed")
```
`not in` prüft das Gegenteil.

---

Zeichenketten haben viele eingebaute **Methoden**: Funktionen, die mit einem Punkt nach der Zeichenkette aufgerufen werden.
`upper()` gibt den Text in Großbuchstaben zurück, `lower()` in Kleinbuchstaben:
```python
word = "Python"
print(word.upper())  # PYTHON
print(word.lower())  # python
print(word)          # Python
```
Beachte, dass die Methoden **eine neue Zeichenkette zurückgeben**: das ursprüngliche `word` wird nicht verändert.
`lower()` wird oft verwendet, um Texte ohne Berücksichtigung der Groß-/Kleinschreibung zu vergleichen: `"Yes".lower() == "yes"`.

---

Zeichenketten sind **unveränderlich** (immutable): einmal erstellt, können ihre Zeichen nicht mehr geändert werden.
Eine Zuweisung an einen Index löst einen `TypeError` aus:
```python
word = "dog"
word[1] = "i"  # TypeError: 'str' object does not support item assignment
```
Um eine Zeichenkette zu "ändern", erstellst du eine neue, zum Beispiel mit Slices und Verkettung, und speicherst sie in der Variable:
```python
word = word[0] + "i" + word[2:]
print(word)  # dig
```

---

Von Nutzern eingegebener Text hat oft zusätzliche Leerzeichen darum herum.
Die Methode `strip()` gibt eine Kopie der Zeichenkette **ohne führende und abschließende Leerzeichen** zurück (Leerzeichen, Tabs und Zeilenumbrüche):
```python
name = "   Ada  "
print("[" + name.strip() + "]")  # [Ada]
```
Leerzeichen in der Mitte des Textes bleiben erhalten.
`lstrip()` entfernt nur die linke Seite und `rstrip()` nur die rechte Seite.

---

`split()` zerlegt eine Zeichenkette in eine **Liste** von Teilen.
Ohne Argumente wird an Leerzeichen aufgeteilt; mit einem Argument wird an diesem Trennzeichen aufgeteilt:
```python
print("a b  c".split())      # ['a', 'b', 'c']
print("2024-01-31".split("-"))  # ['2024', '01', '31']
```
`join()` macht das Gegenteil: es fügt die Elemente einer Liste zu einer Zeichenkette zusammen.
Es wird auf dem **Trennzeichen** aufgerufen, und die Liste ist das Argument:
```python
words = ["one", "two", "three"]
print(", ".join(words))  # one, two, three
print("".join(words))    # onetwothree
```

---

`replace(old, new)` gibt eine Kopie der Zeichenkette zurück, in der **jedes** Vorkommen von `old` durch `new` ersetzt wird:
```python
text = "a-b-c"
print(text.replace("-", "+"))  # a+b+c
```
Da Zeichenketten unveränderlich sind, denk daran, das Ergebnis zu speichern, wenn du es behalten willst.

---

`find(sub)` gibt den **Index** des ersten Vorkommens von `sub` zurück, oder `-1`, wenn es nicht gefunden wird:
```python
text = "hello world"
print(text.find("o"))  # 4
print(text.find("z"))  # -1
```
`count(sub)` gibt zurück, **wie oft** `sub` vorkommt:
```python
print(text.count("o"))   # 2
print(text.count("ll"))  # 1
```

---

`startswith(prefix)` und `endswith(suffix)` geben `True` oder `False` zurück, je nachdem, wie die Zeichenkette beginnt oder endet:
```python
url = "https://codigo.dev"
print(url.startswith("https"))  # True
print(url.endswith(".com"))     # False
```
Sie sind die übliche Methode, um Dateiendungen, Protokolle oder Präfixe zu prüfen.

---

Manche Zeichen können nicht direkt in eine Zeichenkette eingegeben werden.
Eine **Escape-Sequenz** ist ein Backslash `\`, gefolgt von einem Buchstaben oder Symbol, das für ein besonderes Zeichen steht:

- `\n` ein Zeilenumbruch
- `\t` ein Tabulator
- `\"` ein doppeltes Anführungszeichen in einer doppelt zitierten Zeichenkette
- `\'` ein einfaches Anführungszeichen in einer einfach zitierten Zeichenkette
- `\\` ein wörtlicher Backslash

```python
print("Line 1\nLine 2")
print("She said \"hi\"")
```
gibt aus:
```
Line 1
Line 2
She said "hi"
```
Jede Escape-Sequenz zählt als **ein** Zeichen, auch wenn du zwei eingibst.

---

Eine Zeichenkette, die sich über **mehrere Zeilen** erstreckt, kann mit **dreifachen Anführungszeichen** `"""..."""` (oder `'''...'''`) geschrieben werden.
Jeder Zeilenumbruch innerhalb der Anführungszeichen wird Teil der Zeichenkette, sodass du `\n` nicht brauchst:
```python
poem = """Roses are red,
Violets are blue"""
print(poem)
```
gibt aus:
```
Roses are red,
Violets are blue
```
Dreifach zitierte Zeichenketten können außerdem frei einfache und doppelte Anführungszeichen enthalten.

---

Da jede String-Methode eine neue Zeichenkette zurückgibt, kannst du Methoden **verketten**, eine nach der anderen.
Jeder Aufruf arbeitet mit dem Ergebnis des vorherigen:
```python
text = "  Hello World  "
print(text.strip().lower())  # hello world
```
Ein Slice akzeptiert auch einen dritten Wert, den **Schritt** (step).
Der Schritt `-1` durchläuft die Zeichenkette rückwärts, der klassische Trick, um sie umzukehren:
```python
print("abc"[::-1])  # cba
```

---

Ein **Slug** ist eine URL-freundliche Version eines Titels: kleingeschrieben, ohne Leerzeichen darum, und Wörter durch Bindestriche getrennt, wie `hello-world`.
Einen zu erstellen ist nur eine Verkettung der Methoden, die du bereits gelernt hast: `strip()`, `lower()` und `replace()`.
