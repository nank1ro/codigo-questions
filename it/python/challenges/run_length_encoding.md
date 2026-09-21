---
language: python
exerciseType: 1
difficulty: 2
title: Codifica run-length
---

# --description--

La codifica run-length è uno dei trucchi di compressione più antichi che esistano: invece di scrivere più e più volte lo stesso carattere, scrivi quante volte si ripete e poi il carattere stesso.

Un fax che scansiona una pagina quasi tutta bianca incontra lunghe distese di pixel identici, così una riga di dodici `W` viaggia lungo la linea come la ben più corta `12W`. Quando un carattere compare una sola volta, contarlo non porta nessun vantaggio, quindi viene copiato da solo.

# --instructions--

Scrivi una funzione `encode_run` che riceve una stringa `text` e restituisce la sua forma codificata run-length.

Ogni sequenza dello stesso carattere ripetuto due o più volte diventa la lunghezza della sequenza scritta in decimale, seguita da quel carattere. Una sequenza di lunghezza uno viene copiata come singolo carattere, senza nessun numero davanti.

Esempi:
```
encode_run("") ➞ ""
encode_run("AB") ➞ "AB"
encode_run("AABCCCDEEEE") ➞ "2AB3CD4E"
encode_run("WWWWWWWWWWWWBWW") ➞ "12WB2W"
encode_run("  HI  ") ➞ "2 HI2 "
```

- Il testo contiene solo lettere maiuscole dalla `A` alla `Z` e spazi.
- Una sequenza più lunga di nove caratteri usa il suo conteggio decimale completo, quindi dodici `W` diventano `12W` e mai `9W3W`.
- Gli spazi sono caratteri normali: vengono contati e codificati esattamente come le lettere.
- La stringa vuota si codifica nella stringa vuota.

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

La stringa vuota si codifica nella stringa vuota

```python
    def test1(self):
        self.assertEqual(encode_run(""), "", "--err-t1--")
```

Un singolo carattere viene copiato così com'è

```python
    def test2(self):
        self.assertEqual(encode_run("A"), "A", "--err-t2--")
```

Una stringa senza ripetizioni attraversa il processo invariata

```python
    def test3(self):
        self.assertEqual(encode_run("ABCDE"), "ABCDE", "--err-t3--")
```

Una sequenza di due diventa il conteggio seguito dal carattere

```python
    def test4(self):
        self.assertEqual(encode_run("AA"), "2A", "--err-t4--")
```

L'esempio misto "AABCCCDEEEE" diventa "2AB3CD4E"

```python
    def test5(self):
        self.assertEqual(encode_run("AABCCCDEEEE"), "2AB3CD4E", "--err-t5--")
```

Una sequenza di dodici usa il suo conteggio decimale completo, quindi il risultato inizia con "12W"

```python
    def test6(self):
        self.assertEqual(encode_run("WWWWWWWWWWWWBWW"), "12WB2W", "--err-t6--")
```

Le sequenze di spazi vengono codificate esattamente come le sequenze di lettere

```python
    def test7(self):
        self.assertEqual(encode_run("  HI  "), "2 HI2 ", "--err-t7--")
```

Una sequenza di dieci viene scritta come "10A", mai come due sequenze più corte

```python
    def test8(self):
        self.assertEqual(encode_run("AAAAAAAAAA"), "10A", "--err-t8--")
```

I caratteri singoli che si alternano vengono tutti copiati così come sono

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
