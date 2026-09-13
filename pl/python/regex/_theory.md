**Wyrażenie regularne** (regex) to mały język wzorców opisujących tekst. Python udostępnia go w standardowym module `re`:
```python
import re
```

`re.search(pattern, text)` szuka wzorca gdziekolwiek w tekście. Zwraca **obiekt dopasowania**, gdy coś znajdzie, oraz `None`, gdy nic nie znajdzie. `match.group()` daje z powrotem fragment tekstu, który pasował:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
```

Pracę wykonują tu dwa elementy wzorca. `\d` oznacza *dowolną cyfrę*, a `+` oznacza *jeden lub więcej egzemplarz poprzedniego elementu*, więc `\d+` czytamy jako "jedna lub więcej cyfr". Inne przydatne skróty to `\w` (litera, cyfra lub podkreślnik) oraz `\s` (spacja, tabulator lub znak nowej linii).

Wzorce zapisuje się jako **surowe ciągi znaków**, z `r` przed cudzysłowem. W zwykłym ciągu znaków Pythona ukośnik wsteczny rozpoczyna sekwencję ucieczki, więc `"\d"` to zapowiedź kłopotów, a `"\n"` stałby się prawdziwym znakiem nowej linii zamiast dwóch znaków, których oczekuje silnik wyrażeń regularnych. Prefiks `r` przywraca ukośnikowi charakter zwykłego znaku, więc `r"\d"` to dokładnie to, co otrzymuje silnik. Zawsze używaj `r"..."` dla wzorców.

---

`re.search` przeszukuje cały tekst, ale `re.match` wypróbowuje wzorzec tylko na **samym początku**:
```python
import re

print(re.search(r"\d+", "order 42"))  # <re.Match object; span=(6, 8), match='42'>
print(re.match(r"\d+", "order 42"))   # None
print(re.match(r"\d+", "42 orders"))  # <re.Match object; span=(0, 2), match='42'>
```

Obie funkcje zwracają `None`, gdy nic nie pasuje, a obiekt dopasowania jest zawsze prawdziwy, więc zwykłym sposobem na pytanie "czy dopasowano?" jest prosty `if`:
```python
if re.search(r"\d", text):
    print("there is a digit")
```
Gdy potrzebna jest prawdziwa wartość `True` lub `False`, porównaj z `is not None` lub owiń wywołanie w `bool(...)`.

---

Jest jeszcze trzeci punkt wejścia, `re.fullmatch`, który kończy się sukcesem tylko wtedy, gdy wzorzec pokrywa **cały** tekst od pierwszego do ostatniego znaku. To właściwe narzędzie do walidacji:
```python
import re

print(bool(re.fullmatch(r"\d+", "2026")))    # True
print(bool(re.fullmatch(r"\d+", "2026!")))   # False
```

Te trzy funkcje różnią się więc tylko tym, gdzie wzorzec może się znajdować: `re.match` na początku tekstu, `re.search` gdziekolwiek w tekście, a `re.fullmatch` na całym tekście.

---

Obiekt dopasowania niesie ze sobą więcej niż dopasowany tekst. Oprócz `.group()` oferuje pozycję dopasowania wewnątrz oryginalnego ciągu znaków:
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
print(match.start())  # 6
print(match.end())    # 8
print(match.span())   # (6, 8)
```
`.start()` to indeks pierwszego dopasowanego znaku, `.end()` to indeks tuż za ostatnim, a `.span()` zwraca obie te wartości jako krotkę. To znaczy, że `text[match.start():match.end()]` jest zawsze równe `match.group()`.

Ponieważ `re.search` może zwrócić `None`, bezpośrednie odczytanie `.group()` podnosi `AttributeError`, gdy nic nie pasowało; najpierw sprawdź wynik.

---

Okrągłe nawiasy we wzorcu tworzą **grupę przechwytującą**: część dopasowania, którą można odczytać osobno. Grupy numeruje się od lewej do prawej, zaczynając od `1`:
```python
import re

match = re.search(r"(\w+)@(\w+)", "write to ada@example today")
print(match.group())   # ada@example
print(match.group(1))  # ada
print(match.group(2))  # example
print(match.groups())  # ('ada', 'example')
```
`match.group(0)` to całe dopasowanie, dokładnie tak jak `match.group()`, a `match.groups()` zwraca wszystkie grupy jako krotkę. Żądanie numeru grupy, która nie istnieje, podnosi `IndexError`.

---

Liczenie nawiasów, aby znaleźć grupę `3`, szybko się nudzi. Grupie można nadać nazwę za pomocą `(?P<name>...)`, a następnie odczytać ją przez `match.group("name")`:
```python
import re

match = re.search(r"(?P<hour>\d\d):(?P<minute>\d\d)", "starts at 09:30")
print(match.group("hour"))    # 09
print(match.group("minute"))  # 30
print(match.groupdict())      # {'hour': '09', 'minute': '30'}
```
`match.groupdict()` zwraca wszystkie nazwane grupy jako słownik. Nazwane grupy zachowują też swój numer, więc `match.group(1)` nadal działa.

Przykład używa też **kwantyfikatora** z klamrami: `\d{2}` oznacza dokładnie dwie cyfry, `\d{2,4}` oznacza od dwóch do czterech, a `\d{2,}` oznacza dwie lub więcej. To precyzyjne wersje `+` (jedna lub więcej), `*` (zero lub więcej) i `?` (zero lub jeden).

---

Nawiasy kwadratowe definiują **klasę znaków**: zbiór znaków, z których dowolny jest akceptowany na tej pozycji. `[aeiou]` pasuje do jednej samogłoski, `[0-9]` do jednej cyfry, a `[a-z]` do jednej małej litery. `^` tuż po nawiasie otwierającym odwraca znaczenie, więc `[^0-9]` pasuje do wszystkiego, co *nie* jest cyfrą.

Poza klasą `^` i `$` to **kotwice**: `^` przywiązuje wzorzec do początku tekstu, a `$` do jego końca. W `re.fullmatch` kotwice są domniemane, dlatego walidacja czyta się z nim lepiej:
```python
import re

print(bool(re.fullmatch(r"[a-z]{3,8}", "ada")))  # True
print(bool(re.fullmatch(r"[a-z]{3,8}", "Ada")))  # False
```

---

`re.search` zatrzymuje się na pierwszym dopasowaniu. `re.findall(pattern, text)` zbiera zamiast tego **wszystkie** dopasowania i zwraca je jako listę ciągów znaków:
```python
import re

print(re.findall(r"\d+", "a1 bb22 ccc333"))  # ['1', '22', '333']
print(re.findall(r"\d+", "no digits"))       # []
```
Lista jest pusta, gdy nic nie pasuje, więc nie ma `None` do sprawdzenia: można po niej iterować albo zmierzyć ją od razu za pomocą `len(...)`. Zwróć uwagę, że `findall` zwraca zwykłe ciągi znaków, a nie obiekty dopasowania, więc pozycje nie są dostępne.

---

Gdy potrzebna jest pozycja lub grupy każdego dopasowania, właściwym wyborem jest `re.finditer(pattern, text)`: przechodzi przez tekst i dostarcza **obiekt dopasowania** dla każdego dopasowania, po jednym na raz:
```python
import re

for match in re.finditer(r"\d+", "a1 bb22"):
    print(match.group(), match.start())
# 1 1
# 22 5
```
`finditer` produkuje iterator, a nie listę, więc można go użyć w pętli `for` albo w list comprehension. Tam gdzie `findall` daje tylko tekst, `finditer` daje wszystko, co wie obiekt dopasowania.

---

`findall` zmienia zdanie, gdy wzorzec zawiera grupy przechwytujące. Z dokładnie jedną grupą zwraca zawartość tej grupy zamiast całego dopasowania, a z dwiema lub więcej zwraca krotkę grup dla każdego dopasowania:
```python
import re

print(re.findall(r"\d+-\d+", "10-20 30-40"))    # ['10-20', '30-40']
print(re.findall(r"(\d+)-\d+", "10-20 30-40"))  # ['10', '30']
```
Warto to zapamiętać: dodanie nawiasów do wzorca wyłącznie w celu grupowania po cichu zmienia to, co `findall` zwraca. `re.finditer` nigdy nie zachowuje się w ten sposób, ponieważ obiekt dopasowania zawsze przechowuje zarówno całe dopasowanie, jak i grupy.

---

`re.sub(pattern, replacement, text)` zwraca nowy ciąg znaków, w którym każde dopasowanie zostało zastąpione. Ciągi znaków są niezmienne, więc oryginalny tekst pozostaje nietknięty:
```python
import re

print(re.sub(r"\d", "#", "call 555 now"))     # call ### now
print(re.sub(r"\s+", " ", "too    many gaps"))  # too many gaps
```

Zamiennik może odwoływać się wstecz do grup przechwytujących za pomocą `\1`, `\2`, ... (lub `\g<name>` dla grupy nazwanej), co pozwala przestawiać tekst w jednej linijce. Zamiennik też jest surowym ciągiem znaków, z tego samego powodu dotyczącego ukośnika:
```python
import re

print(re.sub(r"(\w+), (\w+)", r"\2 \1", "Lovelace, Ada"))  # Ada Lovelace
```
Argument `count` ogranicza liczbę zastępowanych dopasowań: `re.sub(r"\d", "#", "1 2 3", count=1)` daje `# 2 3`.

---

Zamiennik podawany do `re.sub` może być też **funkcją**. Jest ona wywoływana raz na dopasowanie, otrzymuje obiekt dopasowania i musi zwrócić ciąg znaków do wstawienia w jego miejsce. W ten sposób zamiennik może zależeć od tego, co dopasowano:
```python
import re

def shout(match):
    return match.group().upper()

print(re.sub(r"[a-z]+", shout, "one two"))  # ONE TWO
```
Funkcję przekazuje się przez nazwę, bez nawiasów: zapis `shout(match)` wywołałby ją od razu zamiast przekazać ją do `re.sub`.

---

`str.split` potrafi ciąć tylko po stałym separatorze. `re.split(pattern, text)` tnie po wszystkim, co opisuje wzorzec, czego zwykle potrzebują nieuporządkowane dane wejściowe:
```python
import re

print("a, b;c".split(","))            # ['a', ' b;c']
print(re.split(r"[,;]", "a, b;c"))    # ['a', ' b', 'c']
print(re.split(r"[,;\s]+", "a, b;c")) # ['a', 'b', 'c']
```
Zapisanie separatora jako `[,;\s]+` sprawia, że cały ciąg przecinków, średników i spacji liczy się jako jedno cięcie, zamiast zostawiać między nimi puste ciągi znaków.

Argument `maxsplit` zatrzymuje się po podanej liczbie cięć, zostawiając resztę tekstu w ostatnim elemencie: `re.split(r"\s+", "a b c", maxsplit=1)` daje `['a', 'b c']`.

---

Każde wywołanie `re.search` czy `re.findall` musi najpierw odszukać ciąg znaków wzorca w wewnętrznej pamięci podręcznej. `re.compile(pattern)` pomija to wyszukiwanie i zwraca **obiekt wzorca**, który niesie te same metody:
```python
import re

word_re = re.compile(r"[a-z]+")
print(word_re.search("ab 12").group())  # ab
print(word_re.findall("cd ef"))         # ['cd', 'ef']
print(word_re.sub("*", "ab cd"))        # * *
```
Jedynym pozostałym argumentem jest tekst, ponieważ wzorzec jest już wbudowany w obiekt. Kompilacja opłaca się, gdy ten sam wzorzec jest używany wiele razy, na przykład wewnątrz pętli, a ponadto nadaje wzorcowi nazwę, która wyjaśnia, do czego on pasuje.

---

**Flagi** zmieniają sposób stosowania wzorca. Każda funkcja w `re` przyjmuje je jako argument `flags`, a `re.compile` zapisuje je w obiekcie wzorca:
```python
import re

print(re.search(r"cat", "A Cat", flags=re.IGNORECASE).group())  # Cat
title_re = re.compile(r"^#.*", re.MULTILINE)
```
Dwie najczęściej używane to `re.IGNORECASE`, która sprawia, że litery pasują w obu wielkościach liter, oraz `re.MULTILINE`, która sprawia, że `^` i `$` pasują na początku i na końcu każdego wiersza zamiast całego tekstu. Kilka flag łączy się znakiem `|`, jak w `re.IGNORECASE | re.MULTILINE`.

Flaga zmienia tylko reguły dopasowania: zwracany tekst to zawsze tekst, który naprawdę tam był, z oryginalną wielkością liter.
