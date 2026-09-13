**Komentarz** to notatka zapisana w kodzie źródłowym dla osób, które go czytają. Python całkowicie ignoruje komentarze, więc nigdy nie zmieniają one zachowania programu.

Jedynym rodzajem komentarza w Pythonie jest **komentarz jednolinijkowy**: zaczyna się od `#` i ciągnie do końca linii.
```python
# Greets the user
print("Hello")
```
Używaj komentarzy, aby wyjaśnić, do czego służy fragment kodu albo dlaczego został napisany w ten sposób.

---

Komentarz nie musi mieć własnej linii: może następować po kodzie w tej samej linii. To **komentarz w linii**, dobre miejsce na krótką notatkę o tej konkretnej instrukcji:
```python
retries = 3  # give up after three attempts
```
Wszystko od `#` do końca linii jest ignorowane, a kod przed nim wykonuje się jak zwykle.

Przewodnik stylu Pythona, **PEP 8**, wymaga tu odrobiny odstępów: co najmniej **dwóch spacji** między kodem a `#` oraz **jednej spacji** po `#`. Komentarz w osobnej linii potrzebuje tylko spacji po `#`.

---

Ponieważ Python całkowicie pomija komentarze, dodanie lub usunięcie komentarza nigdy nie zmienia zachowania programu. Wykonuje się tylko kod, który **nie** jest zakomentowany.

Dzięki temu `#` jest szybkim sposobem na wyłączenie linii kodu bez jej usuwania. Nazywa się to **zakomentowaniem**:
```python
total = 10
# total = total + 5
print(total)  # prints 10
```
Druga linia jest teraz komentarzem, więc `total` pozostaje `10`. Usunięcie `#` przywraca linię do życia.

Zakomentowanie przydaje się podczas eksperymentów, ale pamiętaj o porządkach: kod zakomentowany na dłużej tylko wprowadza w błąd tego, kto będzie go czytał po tobie.

---

Wiele języków ma drugi rodzaj komentarza, **komentarz blokowy**, obejmujący kilka linii, jak `/* ... */`. Python nie ma takiej składni: wszystko sprowadza się do `#`.

Gdy wyjaśnienie potrzebuje więcej niż jednej linii, postaw `#` na początku każdej linii:
```python
# Prints the welcome banner.
# Called once when the app starts.
print("Welcome!")
```
Ten sam trik zakomentowuje od razu kilka linii kodu: po jednym `#` na linię. Każdy edytor potrafi dodać lub usunąć te `#` dla całego zaznaczenia jednym skrótem, więc to mniej pracy, niż się wydaje.

---

Często można zobaczyć **ciąg znaków w potrójnych cudzysłowach** używany tak, jakby był komentarzem blokowym:
```python
"""
This looks like a comment,
but it is a string.
"""
print("done")
```
Ciąg znaków między `"""` i `"""` może obejmować kilka linii, a ciąg znaków zapisany samodzielnie jest poprawną instrukcją: Python go tworzy, nic z nim nie robi i go wyrzuca. Nic nie jest wypisywane, więc wynik wygląda jak komentarz.

Nie jest to jednak komentarz. To literał ciągu znaków, więc nadal obowiązują zasady dotyczące cudzysłowów: niedomknięty cudzysłów albo zbłąkane `"""` w środku psują program, podczas gdy w komentarzu `#` wolno wszystko. Taki ciąg może też przypadkiem stać się docstringiem, jeśli okaże się pierwszą instrukcją pliku, klasy lub funkcji. W każdym innym miejscu po prostu nigdzie nie trafia: CPython wyrzuca całą instrukcję już podczas kompilacji.

A więc do wyłączania kodu używaj `#`. Ciąg znaków w potrójnych cudzysłowach ma własne zadanie, które zaczyna się w następnej lekcji.

---

Gdy ciąg znaków jest **pierwszą instrukcją** wewnątrz funkcji, Python traktuje go jako dokumentację tej funkcji. Nazywa się go **docstringiem**:
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"
```
Zgodnie z konwencją docstring zapisuje się w potrójnych cudzysłowach, `"""`, nawet gdy mieści się w jednej linii, aby mógł później urosnąć bez zmiany cudzysłowów.

Zapisuj podsumowanie w trzeciej osobie, jakby opisywało funkcję: "Returns...", "Adds...", "Checks...". Docstring musi poprzedzać każdą inną instrukcję w ciele funkcji, w przeciwnym razie jest to po prostu zwykły ciąg znaków.

---

Docstring nie jest wyrzucany: Python przechowuje go w atrybucie `__doc__` funkcji, więc program może czytać własną dokumentację podczas działania:
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"

print(greet.__doc__)  # Returns the greeting for name.
```
Gdy funkcja nie ma docstringa, `__doc__` ma wartość `None`. To właśnie wypisuje `help(greet)` i to pokazuje edytor, gdy najedziesz kursorem na nazwę.

---

Udokumentować można też cały plik. Ciąg znaków zapisany jako **pierwsza instrukcja pliku**, przed jakimkolwiek importem lub definicją, to **docstring modułu**: mówi on, do czego służy cały plik.
```python
"""Tools for working with rectangles."""

def area(width, height):
    """Returns the area of a rectangle."""
    return width * height
```
Liczy się tylko pierwsza instrukcja. Nad nią może znajdować się komentarz, ale jakikolwiek prawdziwy kod pomiędzy zamienia ten ciąg z powrotem w zwykły, bezużyteczny ciąg znaków.

---

Z klasami jest tak samo: ciąg znaków umieszczony jako pierwsza instrukcja ciała klasy to docstring tej klasy i jest przechowywany w `__doc__`:
```python
class Point:
    """A point on a grid."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

print(Point.__doc__)  # A point on a grid.
```
Każda metoda w klasie też może mieć własny docstring, odczytywany przez `Point.__init__.__doc__`. Trzy miejsca przyjmujące docstring to zatem początek modułu, początek klasy i początek funkcji.

---

Docstringi i komentarze `#` wyglądają podobnie, ale odpowiadają na różne pytania.

**Docstring** jest dla tego, kto kod **używa**: co funkcja robi, czego oczekuje i co zwraca. Przetrwa w `__doc__`, czyta go `help()`, pokazują go edytory, a narzędzia dokumentacyjne go zbierają.

**Komentarz** jest dla tego, kto kod **czyta**: dlaczego ta linia jest zapisana w ten sposób, co oznacza dziwna liczba, jaki błąd obejmuje. Istnieje tylko w pliku źródłowym i znika, gdy tylko program ruszy.

```python
def timeout():
    """Returns the number of seconds to wait for the server."""
    # the server drops idle connections after 35 seconds
    return 30
```
A więc: dokumentacja funkcji trafia do docstringa, a notatki o implementacji — do komentarzy.

---

Gdy jedna linia nie wystarcza, docstring rozwija się w stały układ, opisany w **PEP 257**: jednolinijkowe podsumowanie, pusta linia, potem szczegóły, a zamykające `"""` w osobnej linii.
```python
def to_seconds(minutes):
    """Returns the number of seconds in the given minutes.

    minutes is a whole number and is never negative.
    """
    return minutes * 60
```
Pusta linia ma znaczenie: narzędzia pokazują pierwszą linię osobno, jako krótki opis, a resztę zostawiają dla tych, którzy chcą przeczytać więcej.

---

Docstring musi być **pierwszą linią ciała**, nad wszystkimi innymi instrukcjami. Ciąg znaków zapisany po `return` albo gdziekolwiek indziej w ciele to tylko ciąg znaków: `__doc__` pozostaje `None` i żadne narzędzie nigdy go nie pokaże.

---

Niektóre komentarze są zgodne z konwencją, którą rozumieją edytory. Najczęstsze **znaczniki** to:
- `# TODO: ...` oznacza coś, co jeszcze trzeba napisać
- `# FIXME: ...` oznacza kod, o którym wiadomo, że jest błędny i wymaga poprawy

```python
limit = 10
# TODO: read the limit from the settings
```
Dla Pythona to zwykłe komentarze; edytory zbierają je w osobnym panelu, więc zaległa praca jest łatwa do znalezienia. `TODO` zwykle stoi obok kodu zastępczego, który utrzymuje program w działaniu, dopóki prawdziwy kod nie zostanie napisany.

Kiedy skończysz pracę, zamień kod zastępczy i usuń znacznik w tej samej zmianie, aby komentarz nigdy nie kłamał o stanie kodu.

---

Komentarz umieszczony nad funkcją, aby powiedzieć, co funkcja robi, jest w złym miejscu. Właśnie do tego służy docstring: jest przypisany do funkcji, znajduje go `help()` i pokazują edytory, podczas gdy komentarz `#` nad `def` jest dla nich wszystkich niewidoczny.

```python
# adds a and b
def add(a, b):
    return a + b
```
Przeniesienie tego samego zdania o linię niżej, między potrójne cudzysłowy, czyni z niego prawdziwą dokumentację:
```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
```

---

Python szuka `#` tylko w kodzie, nigdy wewnątrz **ciągu znaków**. Między cudzysłowami `#` jest zwykłym znakiem:
```python
print("black is #000000")  # a hex colour
```
Pierwszy `#` jest częścią tekstu, a drugi rozpoczyna prawdziwy komentarz. To samo dotyczy `"""` wewnątrz komentarza `#`: są tam po prostu trzema znakami cudzysłowu i niczego nie rozpoczynają.

---

Dobry komentarz wyjaśnia **dlaczego** kod coś robi, a nie **co** robi. Kod sam pokazuje, co się dzieje; powtarzanie tego słowami dodaje tylko szumu i starzeje się, gdy tylko kod się zmieni:
```python
# set timeout to 30
timeout = 30
```
Powód, dla którego wybrano tę liczbę, to coś, czego czytelnik nie odgadnie:
```python
# the server drops idle connections after 35 seconds, so stop earlier
timeout = 30
```
Jeśli komentarz tylko powtarza linię poniżej, usuń go albo zastąp powodem. Najlepsze komentarze to te, które mówią coś, czego kod powiedzieć nie potrafi.
