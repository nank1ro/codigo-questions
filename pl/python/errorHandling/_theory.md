**Wyjątek** to sposób, w jaki Python mówi, że instrukcja nie może zostać wykonana. Dzielenie przez zero, konwersja `"abc"` na liczbę całkowitą albo odczyt brakującego klucza słownika — wszystkie go zgłaszają. Gdy nic go nie obsłuży, program zatrzymuje się dokładnie w tym miejscu i wypisuje **traceback**:
```python
print(10 / 0)
```
```
Traceback (most recent call last):
  File "main.py", line 1, in <module>
    print(10 / 0)
          ~~~^~~
ZeroDivisionError: division by zero
```
Traceback wymienia wiersze, które były wykonywane, a ostatni wiersz podaje **typ wyjątku** (`ZeroDivisionError`) i jego komunikat (`division by zero`). To właśnie ten ostatni wiersz należy przeczytać jako pierwszy.

Aby utrzymać program przy życiu, umieść ryzykowną instrukcję w bloku `try`, a sposób naprawy opisz w bloku `except`:
```python
try:
    print(10 / 0)
except ZeroDivisionError:
    print("cannot divide by zero")
```
Python wykonuje blok `try`; jeśli zostanie zgłoszony wymieniony wyjątek, przeskakuje prosto do pasującego bloku `except` i kontynuuje resztę programu.

---

Blok `try` zatrzymuje się na **pierwszej** instrukcji, która zgłasza wyjątek; kolejne wiersze są pomijane, a sterowanie przechodzi do bloku `except`. Nic z bloku `try` nie jest cofane, więc trzymaj go możliwie krótkim:
```python
def half(n):
    try:
        return 10 / n
    except ZeroDivisionError:
        return "undefined"

print(half(2))  # 5.0
print(half(0))  # undefined
```
`return` wewnątrz `except` działa jak każdy inny `return`, co czyni `try`/`except` naturalnym sposobem na zwrócenie wartości zastępczej zamiast awarii programu.

---

Wyjątek, którego nie dopasuje żaden blok `except`, wędruje dalej na zewnątrz: poza wiersz, poza funkcję, która go wykonała, poza jej wywołującego i tak dalej. Jeśli nic go nie przechwyci przed szczytem programu, Python wypisuje traceback, a proces kończy się niezerowym kodem wyjścia. Wiersze po instrukcji, która zawiodła, nigdy się nie wykonują.

---

Klauzula `except` przechwytuje tylko wymieniony typ i jego podklasy. I o to właśnie chodzi: wszystko inne wędruje dalej na zewnątrz, więc nieprzewidziany błąd nadal pokaże się jako traceback, zamiast zostać połknięty.

`int(text)` zgłasza **`ValueError`**, gdy tekst nie opisuje liczby całkowitej, więc to jest typ, który należy wymienić przy odczycie danych od użytkownika:
```python
def to_int(text):
    try:
        return int(text)
    except ValueError:
        return 0

print(to_int("12"))    # 12
print(to_int("oops"))  # 0
```
Wymienienie tu `ValueError` to decyzja, a nie formalność: `int(None)` zgłasza `TypeError`, którego ta funkcja celowo **nie** przechwytuje, ponieważ przekazanie `None` jest błędem programisty i powinno być widoczne.

---

Wybór najwęższego typu, który obejmuje spodziewaną awarię, jest tym, co czyni obsługę błędów godną zaufania. Funkcja czytająca tekst powinna radzić sobie ze złym tekstem (`ValueError`), ale nie może ukrywać wywołania z argumentem niewłaściwego rodzaju (`TypeError`) — ten błąd należy do wywołującego, więc przepuść go dalej.

---

Po jednym bloku `try` może wystąpić **kilka** klauzul `except`, z których każda obsługuje inną awarię innym sposobem naprawy. Python porównuje zgłoszony wyjątek z nimi od góry do dołu i wykonuje **pierwszą** pasującą; pozostałe są pomijane:
```python
try:
    value = 100 / int(text)
except ValueError:
    print("not a number")
except ZeroDivisionError:
    print("cannot divide by zero")
```
Ponieważ wygrywa pierwsze dopasowanie, kolejność ma znaczenie, gdy typy są spokrewnione: klauzula dla typu ogólnego umieszczona nad klauzulą dla typu bardziej szczegółowego zawsze by wygrywała, czyniąc tę szczegółową nieosiągalną.

---

Gdy kilka awarii zasługuje na **tę samą** naprawę, wymienienie ich jako krotki w jednej klauzuli jest krótsze niż powtarzanie bloku:
```python
try:
    value = int(text) / divisor
except (ValueError, ZeroDivisionError):
    value = 0
```
Nawiasy są obowiązkowe: `except ValueError, ZeroDivisionError:` to błąd składni w Pythonie 3. Krotka nadal pozostaje jawną listą typów.

---

`except:` bez żadnego typu po nim to **goły except**. Pasuje do wszystkiego, łącznie z wyjątkami, które nie mają nic wspólnego z chronioną operacją, więc zasada jest prosta: zawsze wymieniaj typy, z których naprawdę potrafisz się podnieść.

---

Wyjątek jest obiektem, a `as` wiąże go z nazwą, dzięki czemu program obsługi może go obejrzeć:
```python
try:
    int("abc")
except ValueError as e:
    print(e)                   # invalid literal for int() with base 10: 'abc'
    print(type(e).__name__)    # ValueError
```
`str(e)` — czyli to, czego używa `print(e)` i pole f-stringa — daje komunikat, z którym wyjątek został utworzony, a `type(e).__name__` daje nazwę klasy jako tekst. Nazwa związana przez `as` istnieje tylko wewnątrz bloku `except`; Python usuwa ją po zakończeniu bloku.

---

Po bloku `try` może wystąpić blok `else`, który wykonuje się **tylko wtedy, gdy blok `try` zakończył się bez zgłoszenia wyjątku**:
```python
try:
    number = int(text)
except ValueError:
    print("not a number")
else:
    print(number * 2)
```
Umieszczenie `print(number * 2)` w bloku `try` też by zadziałało, ale wtedy `ValueError` zgłoszony przez samo wypisywanie zostałby wzięty za błąd konwersji. `else` ogranicza blok `try` do jednej chronionej instrukcji i mieści wszystko, co ma się wydarzyć po sukcesie.

---

Blok `finally` wykonuje się **cokolwiek się stanie**: po bezbłędnym bloku `try`, po bloku `except`, nawet gdy nieprzechwycony przez nikogo wyjątek wędruje na zewnątrz, a także wtedy, gdy blok `try` lub `except` wykona `return`:
```python
def read(text):
    try:
        return int(text)
    except ValueError:
        return 0
    finally:
        print("done")
```
Obie ścieżki wypisują `done`, zanim wartość opuści funkcję. Ta gwarancja jest właśnie tym, do czego służy `finally`: zamknięcie pliku, zwolnienie blokady, przywrócenie ustawienia. Pełna postać to `try` / `except` / `else` / `finally`; `try` potrzebuje co najmniej jednego `except` albo `finally`, a `else` działa tylko obok `except`.

---

Twój własny kod również może zgłaszać wyjątki, instrukcją `raise`, po której następuje obiekt wyjątku:
```python
def set_age(age):
    if age < 0:
        raise ValueError("age cannot be negative")
    return age
```
`raise` natychmiast zatrzymuje funkcję, dokładnie tak jak zrobiłaby to wbudowana awaria. Zwrócenie zamiast tego wartości błędu — `-1`, `None`, `False` — łatwo przeoczyć wywołującemu; wyjątku nie da się zignorować przez przypadek.

Wybierz typ, który opisuje problem: `ValueError`, gdy argument ma właściwy typ, ale niemożliwą wartość, `TypeError`, gdy ma zupełnie zły typ. Tekst przekazany do wyjątku jest jego komunikatem.

---

Garść wbudowanych wyjątków pokrywa większość codziennych awarii:

| Wyjątek | Zgłaszany, gdy | Przykład |
|---|---|---|
| `ValueError` | typ jest właściwy, ale wartość niemożliwa | `int("abc")` |
| `TypeError` | sam typ jest zły | `"x" + 1` |
| `ZeroDivisionError` | dzielenie lub modulo ma zerowy dzielnik | `1 / 0` |
| `KeyError` | słownik nie ma takiego klucza | `{"a": 1}["b"]` |
| `IndexError` | indeks sekwencji jest poza zakresem | `[1, 2][5]` |

Sięgnięcie po jeden z nich zamiast wymyślania nowego typu sprawia, że twoje błędy pozostają czytelne dla każdego, kto zna Pythona.

---

Czasem program obsługi powinien zareagować na awarię, nie biorąc za nią odpowiedzialności: zapisać ją, policzyć, coś zamknąć — a potem pozwolić zająć się nią wywołującemu. Samo `raise` wewnątrz bloku `except` **ponownie zgłasza** obsługiwany wyjątek, z nienaruszonym pierwotnym typem, komunikatem i tracebackiem:
```python
try:
    value = int(text)
except ValueError:
    print("could not read the value")
    raise
```
Napisanie zamiast tego `raise ValueError(...)` utworzyłoby nowy wyjątek z własnym tracebackiem — nie byłaby to już ta sama awaria, którą przechwyciłeś, a to właśnie tę tożsamość zachowuje samo `raise`.

---

Gdy żaden wbudowany typ nie pasuje, zdefiniuj własny, dziedzicząc po `Exception`. Puste ciało zwykle wystarcza — nazwa jest komunikatem dla czytelnika:
```python
class ConfigError(Exception):
    pass
```
Zachowuje się jak każdy inny wyjątek: `raise ConfigError("bad port")`, a `except ConfigError:` go przechwytuje.

Przetłumaczenie niskopoziomowej awarii na własny typ jest częste, a pierwotny błąd nie powinien przy tym zginąć. `raise NewError(...) from original` **łączy** je w łańcuch: zapisuje `original` w atrybucie `__cause__` nowego wyjątku, a traceback pokazuje oba pod napisem *The above exception was the direct cause of the following exception*:
```python
try:
    port = int(text)
except ValueError as e:
    raise ConfigError("bad port") from e
```
Bez `from e` oba nadal są powiązane niejawnie, ale `from` mówi wprost, że pierwszy błąd spowodował drugi.
