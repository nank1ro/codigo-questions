Bardzo częstym zadaniem jest zbudowanie nowej listy na podstawie istniejącej.
Za pomocą pętli `for` i `append()` zajmuje to kilka linijek:
```python
nums = [1, 2, 3]
doubled = []
for n in nums:
    doubled.append(n * 2)
print(doubled)  # [2, 4, 6]
```
Python oferuje krótszą formę dokładnie do tego zadania: **list comprehension**, która buduje całą listę w jednym wyrażeniu:
```python
doubled = [n * 2 for n in nums]
```
Składnia to `[wyrażenie for element in iterowalny]`: część `for` przechodzi przez elementy, a wyrażenie po lewej stronie jest obliczane dla każdego z nich.
Wynikiem jest zupełnie nowa lista, dokładnie taka sama jak ta zbudowana za pomocą pętli.

---

Wyrażenie po lewej stronie może być dowolną rzeczą, która tworzy wartość: obliczeniem, wywołaniem funkcji, wywołaniem metody.
Zmienna pętli może mieć dowolną nazwę i istnieje tylko wewnątrz nawiasów kwadratowych:
```python
prices = [10, 20]
with_tax = [price * 1.2 for price in prices]
print(with_tax)  # [12.0, 24.0]
```

---

Comprehension może też **filtrować** elementy.
Dodaj warunek `if` po części `for`: tylko elementy, dla których warunek ma wartość `True`, trafiają do nowej listy:
```python
nums = [5, 12, 8, 20]
big = [n for n in nums if n > 10]
print(big)  # [12, 20]
```
To jest to samo co pętla z `if` w środku, i zastępuje `filter()` z lambdą w bardziej czytelny sposób.

---

Warunek filtrujący może być dowolnym wyrażeniem zwracającym wartość logiczną, w tym wywołaniami funkcji, takimi jak `len()`:
```python
words = ["a", "bee", "cat"]
short = [w for w in words if len(w) < 3]
print(short)  # ['a']
```

---

Iterowalny obiekt nie musi być listą: działa wszystko, po czym można iterować, a `range()` to ulubieniec.
To najszybszy sposób na zbudowanie listy liczb:
```python
squares = [n * n for n in range(4)]
print(squares)  # [0, 1, 4, 9]
```
Pamiętaj, że `range(start, stop)` nie obejmuje `stop`.

---

Comprehension świetnie nadają się do **przekształcania stringów**.
Wywołaj metodę stringa na każdym elemencie albo zbuduj nowy string za pomocą f-stringa:
```python
names = ["ana", "bob"]
greetings = [f"Hi {name.capitalize()}" for name in names]
print(greetings)  # ['Hi Ana', 'Hi Bob']
```

---

Wewnątrz comprehension możesz użyć dowolnej zmiennej zdefiniowanej wcześniej, na przykład jako granicy `range()`.

---

Czasami nie chcesz odrzucać elementów, tylko wybrać **inną wartość** dla niektórych z nich.
Użyj wyrażenia warunkowego `a if warunek else b` jako wyrażenia, po lewej stronie `for`:
```python
nums = [3, -1, 4]
signs = ["+" if n > 0 else "-" for n in nums]
print(signs)  # ['+', '-', '+']
```
Zwróć uwagę na pozycję: `if-else` znajduje się **przed** `for` i zawsze tworzy wartość, natomiast filtr `if` znajduje się **po** `for` i nie ma `else`.

---

Oba warunki można połączyć w tej samej comprehension: `if-else`, aby wybrać wartość, oraz filtr `if` na końcu, aby pominąć niektóre elementy.
```python
nums = [1, 2, 3, 4]
result = ["big" if n > 2 else "small" for n in nums if n != 3]
print(result)  # ['small', 'small', 'big']
```

---

Dwie pozycje `if` łatwo pomylić, więc je rozróżnij:
```python
values = [n if n > 0 else 0 for n in nums]  # if-else przed for: wybiera wartość, else wymagany
positives = [n for n in nums if n > 0]      # if po for: filtruje, else niedozwolony
```
Umieszczenie `else` po filtrującym `if` to błąd składni.

---

Comprehension może mieć **więcej niż jedno `for`**.
Działają jak zagnieżdżone pętle: pierwsze `for` jest pętlą zewnętrzną, drugie — wewnętrzną.
```python
pairs = [a + b for a in ["x", "y"] for b in ["1", "2"]]
print(pairs)  # ['x1', 'x2', 'y1', 'y2']
```

---

Wewnętrzne `for` może użyć zmiennej z zewnętrznego.
To klasyczny sposób na **spłaszczenie** listy list do jednej listy:
```python
matrix = [[1, 2], [3, 4]]
flat = [n for row in matrix for n in row]
print(flat)  # [1, 2, 3, 4]
```
Funkcja `sum()` sumuje wtedy wszystkie liczby z listy.

---

Możesz też iterować po **słowniku**.
Dzięki `.items()` część `for` rozpakowuje każdą parę na dwie zmienne, klucz i wartość:
```python
ages = {"ana": 31, "bob": 25}
lines = [f"{name} is {age}" for name, age in ages.items()]
print(lines)  # ['ana is 31', 'bob is 25']
```

---

Ten sam pomysł działa dla słowników: **dict comprehension** używa nawiasów klamrowych i wyrażenia `key: value`:
```python
names = ["ana", "bob"]
lengths = {name: len(name) for name in names}
print(lengths)  # {'ana': 3, 'bob': 3}
```

---

Nawiasy klamrowe **bez** części `key: value` dają **set comprehension**.
Set to nieuporządkowana kolekcja, która przechowuje tylko unikalne wartości, więc duplikaty znikają automatycznie:
```python
nums = [1, 2, 2, 3, 3, 3]
unique = {n for n in nums}
print(unique)  # {1, 2, 3}
```

---

**Kiedy powinieneś użyć comprehension?**
Jest idealna, gdy wynikiem jest lista (albo dict, albo set), a logika mieści się w jednej czytelnej linijce: prosta transformacja, opcjonalny filtr.
Jeśli potrzebujesz kilku instrukcji, więcej niż dwóch zagnieżdżonych `for`, albo linijka robi się trudna do odczytania, napisz zamiast tego zwykłą pętlę `for`: kod będzie dłuższy, ale bardziej czytelny.
Comprehension zastępuje też większość zastosowań `map()` i `filter()` z lambdami:
```python
doubled = list(map(lambda n: n * 2, nums))
doubled = [n * 2 for n in nums]  # same result, easier to read
```
