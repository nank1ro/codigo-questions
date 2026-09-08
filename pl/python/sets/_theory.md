**Zbiór** to kolekcja **unikalnych** elementów: ta sama wartość może wystąpić tylko raz, niezależnie od tego, ile razy ją zapiszesz.
Zbiór jest też **nieuporządkowany**: nie ma pierwszego ani ostatniego elementu, więc nie możesz odczytać elementu po indeksie.
Zbiory są idealne, gdy zależy ci tylko na tym, *które* wartości są obecne, a nie ile razy albo na jakiej pozycji.
Zbiór tworzysz, zapisując jego elementy w nawiasach klamrowych `{...}`:
```python
colors = {"red", "blue", "red"}
print(len(colors))  # 2
```
Duplikat `"red"` zostaje odrzucony, więc `len()` liczy tylko odrębne elementy.

---

Wbudowana funkcja `set()` buduje zbiór z dowolnej kolekcji, na przykład listy lub ciągu znaków.
Ponieważ zbiór przechowuje każdą wartość tylko raz, jest to klasyczny sposób na **usunięcie duplikatów**:
```python
nums = [1, 2, 2, 3]
unique = set(nums)
print(len(unique))  # 3
```
Aby sprawdzić, czy wartość jest obecna, użyj operatora `in`, który zwraca `True` lub `False`:
```python
print(2 in unique)  # True
print(9 in unique)  # False
```
Sprawdzanie przynależności w zbiorze jest bardzo szybkie, nawet przy tysiącach elementów.

---

Jest pewna pułapka przy tworzeniu **pustego zbioru**.
Nawiasy klamrowe to również składnia słowników, więc `{}` tworzy pusty **słownik**, a nie zbiór:
```python
empty = {}
print(type(empty))  # <class 'dict'>
```
Aby otrzymać pusty zbiór, musisz wywołać `set()` bez argumentów:
```python
empty = set()
print(type(empty))  # <class 'set'>
print(len(empty))   # 0
```

---

Zbiory są **mutowalne**: możesz dodawać i usuwać elementy po ich utworzeniu.
`add(value)` wstawia wartość; dodanie takiej, która już jest obecna, nic nie zmienia:
```python
letters = {"a", "b"}
letters.add("c")
letters.add("a")
print(len(letters))  # 3
```
Istnieją dwa sposoby usunięcia elementu:
- `remove(value)` go usuwa, ale zgłasza `KeyError`, jeśli wartości nie ma w zbiorze
- `discard(value)` usuwa ją, jeśli jest obecna, i **nic nie robi** w przeciwnym razie, bez błędu
```python
letters.remove("a")
letters.discard("z")  # "z" is not there, but no error
letters.remove("z")   # KeyError: 'z'
```

---

`pop()` usuwa **dowolny element** ze zbioru i go zwraca.
Ponieważ zbiór nie ma kolejności, nie możesz wybrać, który element zostanie usunięty; wywołanie `pop()` na pustym zbiorze zgłasza `KeyError`:
```python
tickets = {101, 102, 103}
picked = tickets.pop()
print(len(tickets))  # 2
```
`clear()` usuwa **wszystkie** elementy, pozostawiając pusty zbiór:
```python
tickets.clear()
print(len(tickets))  # 0
```

---

Możesz przechodzić przez zbiór za pomocą `for`, dokładnie jak przez listę:
```python
for color in {"red", "blue"}:
    print(color)
```
Ponieważ zbiór jest nieuporządkowany, elementy mogą pojawić się w **dowolnej kolejności**, a ta kolejność może się nawet zmieniać między uruchomieniami.
Gdy potrzebujesz przewidywalnej kolejności, przekaż zbiór do `sorted()`, która zwraca posortowaną **listę** jego elementów:
```python
for color in sorted({"red", "blue"}):
    print(color)  # blue, then red
```

---

**Suma** dwóch zbiorów to nowy zbiór z elementami **obu**, bez duplikatów.
Użyj operatora `|` lub metody `union()`:
```python
a = {1, 2}
b = {2, 3}
print(a | b)        # {1, 2, 3}
print(a.union(b))   # {1, 2, 3}
```
Ani `a`, ani `b` nie zostają zmodyfikowane: operacje na zbiorach zawsze zwracają nowy zbiór.

---

**Przecięcie** dwóch zbiorów zawiera tylko elementy obecne w **obu**.
Użyj operatora `&` lub metody `intersection()`:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)               # {2, 3}
print(a.intersection(b))   # {2, 3}
```
Jeśli zbiory nie mają nic wspólnego, wynikiem jest pusty zbiór.

---

**Różnica** `a - b` zawiera elementy `a`, których **nie ma** w `b`.
Kolejność ma znaczenie: `a - b` i `b - a` zwykle się różnią:
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)  # {1}
print(b - a)  # {4}
```
**Różnica symetryczna** `a ^ b` zawiera elementy, które są w **dokładnie jednym** z dwóch zbiorów:
```python
print(a ^ b)  # {1, 4}
```
Formy metodowe to `difference()` i `symmetric_difference()`.

---

Operatory i metody nie są całkowicie równoważne.
Operatory `|`, `&`, `-` i `^` działają tylko wtedy, gdy **oba** argumenty są zbiorami.
Metody `union()`, `intersection()`, `difference()` i `symmetric_difference()` przyjmują **dowolny obiekt iterowalny**, jak listę czy ciąg znaków:
```python
a = {1, 2}
print(a.union([2, 3]))  # {1, 2, 3}
print(a | [2, 3])       # TypeError: unsupported operand type(s) for |: 'set' and 'list'
```

---

Zbiory można też **porównywać** ze sobą.
`a.issubset(b)`, czyli `a <= b`, ma wartość `True`, gdy każdy element `a` jest też w `b`.
`a.issuperset(b)`, czyli `a >= b`, ma wartość `True`, gdy `a` zawiera każdy element `b`.
`a.isdisjoint(b)` ma wartość `True`, gdy oba zbiory nie mają **żadnego** wspólnego elementu:
```python
small = {1, 2}
big = {1, 2, 3}
print(small <= big)              # True
print(big.issuperset(small))     # True
print(small.isdisjoint({8, 9}))  # True
```

---

Zbiór może zawierać tylko elementy **haszowalne**, czyli wartości, które nie mogą się zmieniać: liczby, ciągi znaków, `True`/`False` i **krotki**.
Próba dodania listy, słownika lub innego zbioru zgłasza `TypeError`:
```python
points = set()
points.add((1, 2))  # ok, a tuple
points.add([1, 2])  # TypeError: unhashable type: 'list'
```
Zbiory krotek są przydatne do śledzenia unikalnych par, jak współrzędne czy rekordy (name, age):
```python
visits = [(1, 2), (1, 2), (3, 4)]
print(len(set(visits)))  # 2
```

---

**frozenset** to **niemutowalny** zbiór: po utworzeniu nie możesz dodawać ani usuwać elementów.
Utwórz go za pomocą `frozenset()` z dowolnej kolekcji:
```python
days = frozenset(["sat", "sun"])
print("sat" in days)  # True
days.add("mon")       # AttributeError: 'frozenset' object has no attribute 'add'
```
Wypisanie frozenset pokazuje jego typ wokół elementów, na przykład `frozenset({'sat', 'sun'})`.
Ponieważ nie może się zmieniać, frozenset jest haszowalny: w przeciwieństwie do zwykłego zbioru może być elementem innego zbioru lub kluczem słownika.
Wszystkie operacje tylko do odczytu (`in`, `len()`, `|`, `&`, `-`, `^`, porównania) działają tak jak zwykle.

---

**Wyrażenie zbiorowe** (set comprehension) buduje zbiór w jednym wyrażeniu, z tą samą składnią co list comprehension, ale z nawiasami klamrowymi:
```python
nums = [1, 2, 2, 3]
squares = {n * n for n in nums}
print(squares)  # {1, 4, 9}
```
Opcjonalne `if` filtruje elementy, a duplikaty utworzone przez wyrażenie są automatycznie odrzucane:
```python
evens = {n for n in range(10) if n % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}
```

---

Operacje na zbiorach mogą też modyfikować zbiór **w miejscu**, zamiast zwracać nowy.
`update(iterable)` dodaje każdy element dowolnej kolekcji, podobnie jak `add()`, ale dla wielu wartości naraz:
```python
inventory = {"sword"}
inventory.update(["potion", "map"])
print(len(inventory))  # 3
```
Operatory rozszerzone też działają w miejscu: `|=` dodaje elementy innego zbioru, `&=` zachowuje tylko wspólne, `-=` usuwa elementy innego zbioru:
```python
inventory -= {"map"}
print(sorted(inventory))  # ['potion', 'sword']
```

---

Dwa zbiory są **równe**, gdy zawierają te same elementy, niezależnie od kolejności, w jakiej zostały zapisane:
```python
print({1, 2, 3} == {3, 1, 2})  # True
```
Porównanie długości kolekcji z długością jej zbioru to szybki sposób na wykrycie duplikatów: jeśli zbiór jest **mniejszy**, jakaś wartość pojawiła się więcej niż raz:
```python
emails = ["a@x.com", "b@x.com", "a@x.com"]
print(len(set(emails)) < len(emails))  # True
```
Metoda listy `count(value)` mówi, ile razy pojawia się dana wartość, co pomaga znaleźć, *które* wartości są zduplikowane.
