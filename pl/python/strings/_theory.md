**String** to fragment tekstu: sekwencja znaków ujęta w cudzysłów.
Python akceptuje zarówno pojedyncze `'...'`, jak i podwójne `"..."` cudzysłowy, i działają one dokładnie tak samo:
```python
name = 'Ada'
language = "Python"
```
Wybór ma znaczenie, gdy sam tekst zawiera cudzysłów.
Apostrof wewnątrz pojedynczych cudzysłowów zakończyłby ciąg znaków zbyt wcześnie, więc w takim przypadku użyj podwójnych cudzysłowów:
```python
print("It's sunny")  # It's sunny
```

---

Wbudowana funkcja `len()` zwraca **długość** ciągu znaków, czyli liczbę zawartych w nim znaków.
Spacje i znaki interpunkcyjne również liczą się jako znaki:
```python
print(len("hello"))     # 5
print(len("hi there"))  # 8
print(len(""))          # 0
```

---

Każdy znak ciągu znaków ma pozycję zwaną **indeksem**.
Indeksy zaczynają się od `0`, a nie od `1`: pierwszy znak ma indeks `0`, drugi indeks `1`, i tak dalej.
Napisz indeks w nawiasach kwadratowych po ciągu znaków, aby odczytać pojedynczy znak:
```python
word = "python"
print(word[0])  # p
print(word[1])  # y
print(word[5])  # n
```
Zapytanie o indeks, który nie istnieje, jak `word[6]`, powoduje błąd `IndexError`.

---

Indeksy mogą być również **ujemne**: liczą się wtedy od końca ciągu znaków.
`-1` to ostatni znak, `-2` ten przed nim, i tak dalej:
```python
word = "python"
print(word[-1])  # n
print(word[-2])  # o
```
Jest to przydatne, ponieważ nie musisz znać długości ciągu znaków, aby dotrzeć do jego końca.

---

**Wycinek** (slice) wyodrębnia część ciągu znaków.
Napisz `[początek:koniec]` w nawiasach kwadratowych: znak na pozycji `początek` jest uwzględniony, a ten na pozycji `koniec` jest **wykluczony**:
```python
word = "python"
print(word[0:3])  # pyt
print(word[2:4])  # th
```
Możesz pominąć `początek`, aby wycinać od początku, lub `koniec`, aby wycinać do końca:
```python
print(word[:2])  # py
print(word[2:])  # thon
```
Wycinanie nigdy nie powoduje błędu: `koniec` większy niż długość po prostu zatrzymuje się na ostatnim znaku.

---

Już wiesz, że `+` łączy dwa ciągi znaków (**konkatenacja**).
Operator `*` **powtarza** ciąg znaków określoną liczbę razy:
```python
print("ab" * 3)        # ababab
print("=" * 10)        # ==========
print("Hi" + "!" * 3)  # Hi!!!
```
Powtarzanie to szybki sposób na rysowanie separatorów i prostych wzorów.

---

Operator `in` sprawdza, czy jeden ciąg znaków **zawiera** inny.
Zwraca `True` lub `False`, więc naturalnie pasuje do wnętrza `if`:
```python
email = "ada@mail.com"
print("@" in email)      # True
print("xyz" in email)    # False
if " " in email:
    print("No spaces allowed")
```
`not in` sprawdza sytuację przeciwną.

---

Ciągi znaków mają wiele wbudowanych **metod**: funkcji wywoływanych z kropką po ciągu znaków.
`upper()` zwraca tekst wielkimi literami, `lower()` małymi literami:
```python
word = "Python"
print(word.upper())  # PYTHON
print(word.lower())  # python
print(word)          # Python
```
Zauważ, że metody **zwracają nowy ciąg znaków**: oryginalne `word` nie zostaje zmienione.
`lower()` jest często używane do porównywania tekstów bez rozróżniania wielkości liter: `"Yes".lower() == "yes"`.

---

Ciągi znaków są **niemutowalne**: po utworzeniu ich znaki nie mogą zostać zmienione.
Przypisanie do indeksu powoduje błąd `TypeError`:
```python
word = "dog"
word[1] = "i"  # TypeError: 'str' object does not support item assignment
```
Aby "zmienić" ciąg znaków, budujesz nowy, na przykład za pomocą wycinków i konkatenacji, i zapisujesz go w zmiennej:
```python
word = word[0] + "i" + word[2:]
print(word)  # dig
```

---

Tekst wpisywany przez użytkowników często ma dodatkowe spacje wokół siebie.
Metoda `strip()` zwraca kopię ciągu znaków **bez początkowych i końcowych białych znaków** (spacji, tabulatorów i znaków nowej linii):
```python
name = "   Ada  "
print("[" + name.strip() + "]")  # [Ada]
```
Spacje w środku tekstu są zachowywane.
`lstrip()` usuwa tylko lewą stronę, a `rstrip()` tylko prawą.

---

`split()` dzieli ciąg znaków na **listę** fragmentów.
Bez argumentów dzieli po białych znakach; z argumentem dzieli po podanym separatorze:
```python
print("a b  c".split())      # ['a', 'b', 'c']
print("2024-01-31".split("-"))  # ['2024', '01', '31']
```
`join()` robi coś odwrotnego: skleja elementy listy w jeden ciąg znaków.
Jest wywoływana na **separatorze**, a lista jest argumentem:
```python
words = ["one", "two", "three"]
print(", ".join(words))  # one, two, three
print("".join(words))    # onetwothree
```

---

`replace(old, new)` zwraca kopię ciągu znaków, w której **każde** wystąpienie `old` jest zastąpione przez `new`:
```python
text = "a-b-c"
print(text.replace("-", "+"))  # a+b+c
```
Ponieważ ciągi znaków są niemutowalne, pamiętaj, aby zapisać wynik, jeśli chcesz go zachować.

---

`find(sub)` zwraca **indeks** pierwszego wystąpienia `sub`, albo `-1`, jeśli nie zostanie znalezione:
```python
text = "hello world"
print(text.find("o"))  # 4
print(text.find("z"))  # -1
```
`count(sub)` zwraca **ile razy** `sub` występuje:
```python
print(text.count("o"))   # 2
print(text.count("ll"))  # 1
```

---

`startswith(prefix)` i `endswith(suffix)` zwracają `True` lub `False` w zależności od tego, jak zaczyna się lub kończy ciąg znaków:
```python
url = "https://codigo.dev"
print(url.startswith("https"))  # True
print(url.endswith(".com"))     # False
```
To standardowy sposób sprawdzania rozszerzeń plików, protokołów lub prefiksów.

---

Niektórych znaków nie można wpisać bezpośrednio wewnątrz ciągu znaków.
**Sekwencja ucieczki** to ukośnik wsteczny `\`, po którym następuje litera lub symbol reprezentujący znak specjalny:

- `\n` nowa linia
- `\t` tabulator
- `\"` cudzysłów podwójny wewnątrz ciągu znaków w cudzysłowie podwójnym
- `\'` cudzysłów pojedynczy wewnątrz ciągu znaków w cudzysłowie pojedynczym
- `\\` dosłowny ukośnik wsteczny

```python
print("Line 1\nLine 2")
print("She said \"hi\"")
```
wypisuje:
```
Line 1
Line 2
She said "hi"
```
Każda sekwencja ucieczki liczy się jako **jeden** znak, nawet jeśli wpiszesz dwa.

---

Ciąg znaków rozciągający się na **kilka linii** można zapisać za pomocą **potrójnych cudzysłowów** `"""..."""` (lub `'''...'''`).
Każde złamanie linii wewnątrz cudzysłowów staje się częścią ciągu znaków, więc nie potrzebujesz `\n`:
```python
poem = """Roses are red,
Violets are blue"""
print(poem)
```
wypisuje:
```
Roses are red,
Violets are blue
```
Ciągi znaków w potrójnych cudzysłowach mogą też swobodnie zawierać pojedyncze i podwójne cudzysłowy.

---

Ponieważ każda metoda ciągu znaków zwraca nowy ciąg znaków, możesz **łączyć** metody jedna po drugiej.
Każde wywołanie działa na wyniku poprzedniego:
```python
text = "  Hello World  "
print(text.strip().lower())  # hello world
```
Wycinek akceptuje też trzecią wartość, **krok**.
Krok `-1` przechodzi przez ciąg znaków od tyłu, co jest klasyczną sztuczką na jego odwrócenie:
```python
print("abc"[::-1])  # cba
```

---

**Slug** to przyjazna dla URL-i wersja tytułu: małe litery, bez spacji wokół, a słowa oddzielone myślnikami, jak `hello-world`.
Zbudowanie go to po prostu łańcuch metod, których się nauczyłeś: `strip()`, `lower()` i `replace()`.
