Czasami zmienna nie ma jeszcze **żadnej wartości** do przechowania: użytkownik, który się nie zalogował, wyszukiwanie, które nic nie znalazło, ustawienie, które nigdy nie zostało wybrane. Python reprezentuje to za pomocą specjalnej wartości `None`.
`None` jest wartością jak każda inna: możesz ją przypisać, wypisać i przekazać do funkcji. Jej typ to `NoneType`, a w całym programie istnieje dokładnie **jedna** wartość `None`, więc każde `None`, które napiszesz, odnosi się do tego samego obiektu:
```python
winner = None
print(winner)                 # None
print(type(winner).__name__)  # NoneType
print(winner is None)         # True
```
`None` to nie `0`, nie pusty ciąg znaków i nie `False`: to osobna wartość oznaczająca "nic tu nie ma".

---

Każde wywołanie funkcji daje wartość, nawet gdy funkcja pozornie niczego nie zwraca. Funkcja **bez** instrukcji `return` albo z samotnym `return` oddaje `None`:
```python
def say_hello():
    print("hello")

result = say_hello()
print(result)  # None
```
Dlatego wywołanie `print(my_list.append(3))` pokazuje `None`: `append` zmienia listę w miejscu i nic nie zwraca.
Funkcja, która tylko wykonuje czynność (wypisywanie, zapisywanie, zmienianie listy), zwykle zwraca `None`, podczas gdy funkcja, która coś oblicza, musi to jawnie zwrócić za pomocą `return`.

---

Aby sprawdzić, czy zmienna przechowuje `None`, używaj `is` i `is not`, nigdy `==`:
```python
if user is None:
    print("nobody logged in")
if user is not None:
    print("welcome")
```
`==` pyta "czy te wartości są *równe*?", i każda klasa może odpowiedzieć na to pytanie po swojemu, definiując metodę `__eq__`. `is` pyta "czy to *ten sam obiekt*?", i nic nie może zmienić tej odpowiedzi.
Skoro `None` jest tylko jedno, `is None` jest zawsze poprawne i nieco szybsze, podczas gdy `== None` może dać zaskakującą odpowiedź dla obiektów z własnym `__eq__`.

---

`None` liczy się jako **fałsz** w warunku, więc `if not value:` daje `True`, gdy `value` to `None`. Kuszące jest użycie tego jako sprawdzenia na `None`, ale ten sam test jest także `True` dla `0`, `""`, `[]` i każdej innej pustej wartości:
```python
count = 0
if not count:
    print("missing?")   # printed, but 0 is a real value!
```
Gdy "brak wartości" i "pusta wartość" muszą być potraktowane różnie, najpierw sprawdź `is None`, a potem prawdziwość:
```python
if count is None:
    print("no count yet")
elif not count:
    print("count is zero")
```
Używaj `if not value:` tylko wtedy, gdy naprawdę chcesz traktować `None` i puste wartości tak samo.

---

Parametr może mieć **wartość domyślną**, używaną wtedy, gdy wywołujący pomija argument. `None` to typowa wartość domyślna oznaczająca "nie podano":
```python
def greet(name=None):
    if name is None:
        name = "stranger"
    print("Hello, " + name)

greet()       # Hello, stranger
greet("Ada")  # Hello, Ada
```
Ma to znaczenie dla list i słowników. Wartość domyślna jest obliczana **raz**, przy definiowaniu funkcji, więc `def add(item, items=[])` współdzieli tę samą listę między wszystkimi wywołaniami, które pomijają `items`, a elementy się kumulują. Rozwiązaniem jest użycie `None` jako wartości domyślnej i utworzenie świeżej listy wewnątrz funkcji:
```python
def add(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

Odczytanie brakującego klucza ze słownika za pomocą `[]` podnosi `KeyError`. Metoda `get` jest bezpieczną alternatywą: zwraca wartość, gdy klucz istnieje, i `None`, gdy go nie ma:
```python
ages = {"Ada": 36}
print(ages.get("Ada"))    # 36
print(ages.get("Grace"))  # None
```
`get` przyjmuje drugi argument: wartość do zwrócenia **zamiast** `None`, gdy klucza brakuje:
```python
print(ages.get("Grace", 0))  # 0
```
To najczęstszy sposób, w jaki `None` pojawia się w codziennym kodzie: wyszukiwanie, które nic nie znalazło.

---

Funkcja, która zwraca liczbę **lub** `None`, powinna powiedzieć o tym w swojej sygnaturze. **Podpowiedź typu** (type hint) to adnotacja dokumentująca oczekiwany typ: `name: str` dla parametru i `-> int` dla wartości zwracanej. Python nie wymusza podpowiedzi, ale edytory i czytelnicy na nich polegają:
```python
def parse_age(text: str) -> int | None:
    if text.isdigit():
        return int(text)
    return None
```
`int | None` czytamy "`int` albo `None`". Starszy zapis `Optional[int]` z modułu `typing` oznacza dokładnie to samo i wciąż można go spotkać w istniejącym kodzie.
Za każdym razem, gdy zobaczysz `| None` w sygnaturze, pamiętaj, aby sprawdzić wynik, zanim go użyjesz.

---

Funkcje, które mogą otrzymać `None`, często zaczynają od **strażnika** (guard): instrukcji `if`, która kończy działanie wcześniej, gdy nie ma nic do roboty. Reszta funkcji może wtedy zakładać, że wartość jest obecna, bez zagnieżdżania wszystkiego w `else`:
```python
def shout(text):
    if text is None:
        return None
    return text.upper() + "!"
```
Strażnicy stoją na początku, w kolejności, w jakiej sprawdzania muszą nastąpić: nie można wywołać `text.split()`, zanim dowiesz się, że `text` nie jest `None`.

---

Operator `or` nie zwraca `True` ani `False`: zwraca swój **lewy** operand, gdy ten jest prawdziwy, a **prawy** operand w przeciwnym razie. Daje to jednolinijkowy sposób podania wartości zapasowej:
```python
name = None
print(name or "anonymous")  # anonymous
name = "Ada"
print(name or "anonymous")  # Ada
```
Haczyk polega na tym, że `or` patrzy na prawdziwość, a nie na `None`: `0`, `""` i `[]` też są zastępowane wartością zapasową. Używaj `x or fallback` tylko wtedy, gdy każda pusta wartość też ma stać się wartością zapasową.

---

Gdy `0` lub `""` muszą zostać zachowane, a zastąpione ma być tylko `None`, wartość zapasowa wymaga jawnego sprawdzenia `is None`. Zwartą formą jest **wyrażenie warunkowe**, `a if condition else b`, które przyjmuje wartość `a`, gdy warunek jest prawdziwy, a `b` w przeciwnym razie:
```python
timeout = 0
seconds = timeout if timeout is not None else 30
print(seconds)  # 0, not 30
```

---

Lista może zawierać `None` obok prawdziwych wartości, na przykład odczyty, które się nie powiodły, albo odpowiedzi, które zostały pominięte. Większość operacji go nie akceptuje: `sum([8, None])` podnosi `TypeError`.
Odfiltruj wartości `None` za pomocą list comprehension, którego warunkiem jest `is not None`:
```python
readings = [3, None, 5]
valid = [r for r in readings if r is not None]
print(valid)  # [3, 5]
```
Użycie zamiast tego `if r` usunęłoby też każde `0`, więc bądź dokładny, gdy zero jest poprawnym odczytem.

---

Wyszukanie połączone ze sprawdzeniem `None` zwykle wymaga dwóch linii: jednej do zapisania wyniku i jednej do jego przetestowania. Operator **wyrażenia przypisania** `:=`, nazywany *walrusem*, przypisuje wartość **wewnątrz** wyrażenia, więc oba kroki mieszczą się w `if`:
```python
ages = {"Ada": 36}
if (age := ages.get("Ada")) is not None:
    print(age + 1)  # 37
```
Nawiasy są wymagane: bez nich `:=` próbowałby przypisać całe porównanie. Po `if` zmienna `age` pozostaje dostępna jak każda inna zmienna.

---

Nie każde "nie znaleziono" jest zgłaszane przez `None`. Niektóre starsze funkcje zwracają zamiast tego wartość **sentinel**, czyli zwykłą wartość, której nadano specjalne znaczenie. Metoda `find` dla ciągów znaków zwraca indeks podciągu albo `-1`, gdy go nie ma:
```python
print("banana".find("n"))  # 2
print("banana".find("x"))  # -1
```
Funkcja `re.match(pattern, text)` z modułu `re` sprawdza, czy `text` zaczyna się od `pattern`, i zwraca obiekt dopasowania albo `None`, gdy nie ma dopasowania.
`None` to bezpieczniejsza konwencja: `-1` jest poprawnym indeksem, więc `text[text.find("x")]` po cichu zwraca ostatni znak zamiast kończyć się błędem, podczas gdy użycie `None` jako indeksu od razu podnosi błąd.

---

`None` nie da się uporządkować: `None < 1` podnosi `TypeError`, ponieważ Python nie ma pojęcia, czy "nic" jest mniejsze, czy większe od liczby.
Ma to znaczenie, gdy `None` służy jako wartość początkowa wyszukiwania, na przykład "najlepsza wartość widziana dotąd, o ile w ogóle jakaś była". Każde porównanie musi być chronione sprawdzeniem `is None` umieszczonym **najpierw**, aby `or` uległo zwarciu i porównanie było pomijane, gdy nie ma jeszcze czego porównywać:
```python
if best is None or value > best:
    best = value
```
Zapisane odwrotnie, `value > best or best is None` porównywałoby z `None` w pierwszej iteracji i kończyło się błędem.
