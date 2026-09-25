---
language: python
exerciseType: 1
difficulty: 2
title: Lauflängencodierung
---

# --description--

Lauflängencodierung ist einer der ältesten Kompressionstricks überhaupt: Statt dasselbe Zeichen immer wieder zu schreiben, schreiben Sie, wie oft es sich wiederholt, und danach das Zeichen selbst.

Ein Faxgerät, das eine überwiegend leere Seite scannt, trifft auf lange Strecken identischer Pixel, deshalb wandert eine Reihe von zwölf `W` als viel kürzeres `12W` durch die Leitung. Taucht ein Zeichen nur einmal auf, bringt das Zählen nichts, also wird es einfach einzeln übernommen.

# --instructions--

Schreiben Sie eine Funktion `encode_run`, die eine Zeichenkette `text` entgegennimmt und ihre lauflängencodierte Form zurückgibt.

Jede Folge desselben Zeichens, das zwei- oder mehrmals hintereinander wiederholt wird, wird zu der Länge der Folge in Dezimalschreibweise, gefolgt von dem Zeichen selbst. Eine Folge der Länge eins wird als einzelnes Zeichen übernommen, ohne Zahl davor.

Beispiele:
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- Der Text enthält nur Großbuchstaben von `A` bis `Z` sowie Leerzeichen.
- Eine Folge von mehr als neun Zeichen schreibt ihre vollständige Dezimalzahl, zwölf `W` werden also zu `12W` und nie zu `9W3W`.
- Leerzeichen sind ganz normale Zeichen: Sie werden genauso gezählt und codiert wie Buchstaben.
- Die leere Zeichenkette wird zu der leeren Zeichenkette codiert.

# --seed--

```python
def encode_run(text):
    pass
```

# --before-asserts--

```python
import unittest

class CodigoTests(unittest.TestCase):
```

# --asserts--

Die leere Zeichenkette wird zu der leeren Zeichenkette codiert

```python
    def test1(self):
        self.assertEqual(encode_run(""), "", "--err-t1--")
```

Ein einzelnes Zeichen wird unverändert als es selbst übernommen

```python
    def test2(self):
        self.assertEqual(encode_run("A"), "A", "--err-t2--")
```

Eine Zeichenkette ohne Wiederholungen durchläuft die Codierung unverändert

```python
    def test3(self):
        self.assertEqual(encode_run("ABCDE"), "ABCDE", "--err-t3--")
```

Eine Folge von zwei wird zu der Anzahl, gefolgt von dem Zeichen

```python
    def test4(self):
        self.assertEqual(encode_run("AA"), "2A", "--err-t4--")
```

Das gemischte Beispiel "AABCCCDEEEE" wird zu "2AB3CD4E"

```python
    def test5(self):
        self.assertEqual(encode_run("AABCCCDEEEE"), "2AB3CD4E", "--err-t5--")
```

Eine Folge von zwölf schreibt ihre vollständige Dezimalzahl, deshalb beginnt das Ergebnis mit "12W"

```python
    def test6(self):
        self.assertEqual(encode_run("WWWWWWWWWWWWBWW"), "12WB2W", "--err-t6--")
```

Folgen von Leerzeichen werden genauso codiert wie Folgen von Buchstaben

```python
    def test7(self):
        self.assertEqual(encode_run("  HI  "), "2 HI2 ", "--err-t7--")
```

Eine Folge von zehn wird als "10A" geschrieben, nie als zwei kürzere Folgen

```python
    def test8(self):
        self.assertEqual(encode_run("AAAAAAAAAA"), "10A", "--err-t8--")
```

Einzelne Zeichen, die sich abwechseln, werden alle unverändert als sie selbst übernommen

```python
    def test9(self):
        self.assertEqual(encode_run("ABABAB"), "ABABAB", "--err-t9--")
```

# --after-asserts--

```python
if __name__ == "__main__":
    unittest.main()
```

# --solutions--

```python
def encode_run(text):
    result = ""
    i = 0

    while i < len(text):
        run = 1
        while i + run < len(text) and text[i + run] == text[i]:
            run += 1
        if run > 1:
            result += str(run)
        result += text[i]
        i += run

    return result
```
