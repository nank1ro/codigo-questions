Ein **regulärer Ausdruck** (Regex) ist eine kleine Mustersprache, die Text beschreibt. Python stellt sie im Standardmodul `re` bereit:
```python
import re
```

`re.search(pattern, text)` sucht nach dem Muster irgendwo im Text. Es gibt ein **Match-Objekt** zurück, wenn es etwas findet, und `None`, wenn nicht. `match.group()` gibt das Stück Text zurück, auf das das Muster gepasst hat:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
```

Zwei Teile des Musters erledigen hier die Arbeit. `\d` bedeutet *eine beliebige Ziffer*, und `+` bedeutet *eines oder mehr des vorherigen Elements*, also liest sich `\d+` als "eine oder mehrere Ziffern". Weitere nützliche Kurzschreibweisen sind `\w` (ein Buchstabe, eine Ziffer oder ein Unterstrich) und `\s` (ein Leerzeichen, ein Tabulator oder ein Zeilenumbruch).

Muster werden als **Raw-Strings** geschrieben, mit einem `r` vor den Anführungszeichen. In einer normalen Python-Zeichenkette leitet der Backslash eine Escape-Sequenz ein, daher ist `"\d"` eine Warnung, die nur darauf wartet zu passieren, und `"\n"` würde zu einem echten Zeilenumbruch werden statt zu den beiden Zeichen, die die Regex-Engine erwartet. Das Präfix `r` macht den Backslash wieder zu einem gewöhnlichen Zeichen, sodass `r"\d"` genau das ist, was die Engine erhält. Verwende immer `r"..."` für Muster.

---

`re.search` durchsucht den ganzen Text, aber `re.match` versucht das Muster nur **ganz am Anfang**:
```python
import re

print(re.search(r"\d+", "order 42"))  # <re.Match object; span=(6, 8), match='42'>
print(re.match(r"\d+", "order 42"))   # None
print(re.match(r"\d+", "42 orders"))  # <re.Match object; span=(0, 2), match='42'>
```

Beide geben `None` zurück, wenn nichts passt, und ein Match-Objekt ist immer truthy, daher fragt man üblicherweise mit einem einfachen `if`, ob es einen Treffer gab:
```python
if re.search(r"\d", text):
    print("there is a digit")
```
Wenn ein echtes `True` oder `False` gebraucht wird, vergleiche mit `is not None` oder wickle den Aufruf in `bool(...)`.

---

Es gibt einen dritten Einstiegspunkt, `re.fullmatch`, der nur dann Erfolg hat, wenn das Muster den **ganzen** Text vom ersten bis zum letzten Zeichen abdeckt. Es ist das richtige Werkzeug zur Validierung:
```python
import re

print(bool(re.fullmatch(r"\d+", "2026")))    # True
print(bool(re.fullmatch(r"\d+", "2026!")))   # False
```

Die drei Funktionen unterscheiden sich also nur darin, wo das Muster sitzen darf: `re.match` am Anfang des Texts, `re.search` irgendwo im Text und `re.fullmatch` über den gesamten Text.

---

Ein Match-Objekt trägt mehr als den gefundenen Text. Neben `.group()` bietet es die Position des Treffers innerhalb der ursprünglichen Zeichenkette:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
print(match.start())  # 6
print(match.end())    # 8
print(match.span())   # (6, 8)
```
`.start()` ist der Index des ersten gefundenen Zeichens, `.end()` ist der Index direkt nach dem letzten, und `.span()` gibt beide als Tupel zurück. Das bedeutet, `text[match.start():match.end()]` ist immer gleich `match.group()`.

Da `re.search` `None` zurückgeben kann, löst das direkte Lesen von `.group()` einen `AttributeError` aus, wenn nichts gepasst hat; prüfe zuerst das Ergebnis.

---

Runde Klammern in einem Muster erzeugen eine **erfassende Gruppe**: einen Teil des Treffers, den man separat zurücklesen kann. Die Gruppen werden von links nach rechts nummeriert, beginnend bei `1`:
```python
import re

match = re.search(r"(\w+)@(\w+)", "write to ada@example today")
print(match.group())   # ada@example
print(match.group(1))  # ada
print(match.group(2))  # example
print(match.groups())  # ('ada', 'example')
```
`match.group(0)` ist der ganze Treffer, genau wie `match.group()`, und `match.groups()` gibt jede Gruppe als Tupel zurück. Die Frage nach einer Gruppennummer, die nicht existiert, löst einen `IndexError` aus.

---

Klammern zu zählen, um Gruppe `3` zu finden, wird schnell mühsam. Eine Gruppe kann mit `(?P<name>...)` einen Namen bekommen und dann mit `match.group("name")` gelesen werden:
```python
import re

match = re.search(r"(?P<hour>\d\d):(?P<minute>\d\d)", "starts at 09:30")
print(match.group("hour"))    # 09
print(match.group("minute"))  # 30
print(match.groupdict())      # {'hour': '09', 'minute': '30'}
```
`match.groupdict()` gibt jede benannte Gruppe als Wörterbuch zurück. Benannte Gruppen behalten auch ihre Nummer, daher funktioniert `match.group(1)` weiterhin.

Das Beispiel verwendet auch einen **Quantifizierer** mit geschweiften Klammern: `\d{2}` bedeutet genau zwei Ziffern, `\d{2,4}` bedeutet zwischen zwei und vier, und `\d{2,}` bedeutet zwei oder mehr. Sie sind die präzise Version von `+` (eines oder mehr), `*` (null oder mehr) und `?` (null oder eines).

---

Eckige Klammern definieren eine **Zeichenklasse**: eine Menge von Zeichen, von denen jedes einzeln an dieser Position akzeptiert wird. `[aeiou]` passt auf einen Vokal, `[0-9]` auf eine Ziffer und `[a-z]` auf einen Kleinbuchstaben. Ein `^` direkt nach der öffnenden Klammer kehrt die Bedeutung um, daher passt `[^0-9]` auf alles, was *keine* Ziffer ist.

Außerhalb einer Klasse sind `^` und `$` **Anker**: `^` bindet das Muster an den Anfang des Texts und `$` an das Ende. Bei `re.fullmatch` sind die Anker implizit, weshalb sich Validierung damit besser liest:
```python
import re

print(bool(re.fullmatch(r"[a-z]{3,8}", "ada")))  # True
print(bool(re.fullmatch(r"[a-z]{3,8}", "Ada")))  # False
```

---

`re.search` hält beim ersten Treffer an. `re.findall(pattern, text)` sammelt stattdessen **jeden** Treffer und gibt sie als Liste von Zeichenketten zurück:
```python
import re

print(re.findall(r"\d+", "a1 bb22 ccc333"))  # ['1', '22', '333']
print(re.findall(r"\d+", "no digits"))       # []
```
Die Liste ist leer, wenn nichts passt, daher gibt es kein `None` zu prüfen: Man kann direkt über sie iterieren oder sie mit `len(...)` messen. Beachte, dass `findall` einfache Zeichenketten zurückgibt, keine Match-Objekte, daher sind Positionen nicht verfügbar.

---

Wenn die Position oder die Gruppen jedes Treffers gebraucht werden, ist `re.finditer(pattern, text)` der richtige Aufruf: Es geht den Text durch und liefert für jeden Treffer ein **Match-Objekt**, jeweils eines:
```python
import re

for match in re.finditer(r"\d+", "a1 bb22"):
    print(match.group(), match.start())
# 1 1
# 22 5
```
`finditer` erzeugt einen Iterator, keine Liste, daher kann es in einer `for`-Schleife oder in einer Comprehension verwendet werden. Wo `findall` nur den Text liefert, liefert `finditer` alles, was ein Match-Objekt weiß.

---

`findall` ändert sein Verhalten, wenn das Muster erfassende Gruppen enthält. Mit genau einer Gruppe gibt es den Inhalt dieser Gruppe statt des ganzen Treffers zurück, und mit zwei oder mehr gibt es für jeden Treffer ein Tupel von Gruppen zurück:
```python
import re

print(re.findall(r"\d+-\d+", "10-20 30-40"))    # ['10-20', '30-40']
print(re.findall(r"(\d+)-\d+", "10-20 30-40"))  # ['10', '30']
```
Das lohnt es sich zu merken: Klammern nur zum Gruppieren zu einem Muster hinzuzufügen, ändert stillschweigend, was `findall` zurückgibt. `re.finditer` verhält sich nie so, weil ein Match-Objekt immer sowohl den vollen Treffer als auch die Gruppen behält.

---

`re.sub(pattern, replacement, text)` gibt eine neue Zeichenkette zurück, in der jeder Treffer ersetzt wurde. Zeichenketten sind unveränderlich, daher bleibt der ursprüngliche Text unangetastet:
```python
import re

print(re.sub(r"\d", "#", "call 555 now"))     # call ### now
print(re.sub(r"\s+", " ", "too    many gaps"))  # too many gaps
```

Der Ersatz kann mit `\1`, `\2`, ... auf die erfassenden Gruppen zurückverweisen (oder mit `\g<name>` bei einer benannten Gruppe), was das Umordnen von Text zu einer Einzeiler-Angelegenheit macht. Der Ersatz ist aus demselben Backslash-Grund ebenfalls ein Raw-String:
```python
import re

print(re.sub(r"(\w+), (\w+)", r"\2 \1", "Lovelace, Ada"))  # Ada Lovelace
```
Ein `count`-Argument begrenzt, wie viele Treffer ersetzt werden: `re.sub(r"\d", "#", "1 2 3", count=1)` ergibt `# 2 3`.

---

Der Ersatz, der `re.sub` gegeben wird, kann auch eine **Funktion** sein. Sie wird einmal pro Treffer aufgerufen, erhält das Match-Objekt und muss die Zeichenkette zurückgeben, die an seine Stelle tritt. So kann ein Ersatz davon abhängen, was gefunden wurde:
```python
import re

def shout(match):
    return match.group().upper()

print(re.sub(r"[a-z]+", shout, "one two"))  # ONE TWO
```
Die Funktion wird mit ihrem Namen übergeben, ohne Klammern: `shout(match)` zu schreiben würde sie sofort aufrufen, statt sie `re.sub` zu übergeben.

---

`str.split` kann nur an einem festen Trennzeichen schneiden. `re.split(pattern, text)` schneidet an allem, was das Muster beschreibt, was chaotische Eingaben üblicherweise brauchen:
```python
import re

print("a, b;c".split(","))            # ['a', ' b;c']
print(re.split(r"[,;]", "a, b;c"))    # ['a', ' b', 'c']
print(re.split(r"[,;\s]+", "a, b;c")) # ['a', 'b', 'c']
```
Das Trennzeichen als `[,;\s]+` zu schreiben lässt eine ganze Folge von Kommas, Semikolons und Leerzeichen als einen einzigen Schnitt zählen, statt leere Zeichenketten zwischen ihnen zu lassen.

Ein `maxsplit`-Argument hält nach einer gegebenen Anzahl von Schnitten an und lässt den Rest des Texts im letzten Element: `re.split(r"\s+", "a b c", maxsplit=1)` ergibt `['a', 'b c']`.

---

Jeder Aufruf von `re.search` oder `re.findall` muss zuerst die Muster-Zeichenkette in einem internen Cache nachschlagen. `re.compile(pattern)` überspringt diese Suche und gibt ein **Musterobjekt** zurück, das dieselben Methoden trägt:
```python
import re

word_re = re.compile(r"[a-z]+")
print(word_re.search("ab 12").group())  # ab
print(word_re.findall("cd ef"))         # ['cd', 'ef']
print(word_re.sub("*", "ab cd"))        # * *
```
Der Text ist das einzige verbleibende Argument, weil das Muster bereits in das Objekt eingebacken ist. Kompilieren lohnt sich, wenn dasselbe Muster viele Male verwendet wird, etwa innerhalb einer Schleife, und es gibt dem Muster auch einen Namen, der erklärt, worauf es passt.

---

**Flags** ändern, wie ein Muster angewendet wird. Jede Funktion in `re` akzeptiert sie als `flags`-Argument, und `re.compile` speichert sie im Musterobjekt:
```python
import re

print(re.search(r"cat", "A Cat", flags=re.IGNORECASE).group())  # Cat
title_re = re.compile(r"^#.*", re.MULTILINE)
```
Die beiden am häufigsten verwendeten sind `re.IGNORECASE`, das Buchstaben in beiden Schreibungen passen lässt, und `re.MULTILINE`, das `^` und `$` am Anfang und Ende jeder Zeile statt des ganzen Texts passen lässt. Mehrere Flags werden mit `|` kombiniert, wie in `re.IGNORECASE | re.MULTILINE`.

Ein Flag ändert nur die Passungsregeln: Der zurückgegebene Text ist immer der Text, der wirklich da war, mit seiner ursprünglichen Schreibweise.
