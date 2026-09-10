Operatory porównania porównują dwie wartości i zwracają wartość **logiczną**, `True` lub `False`: `==` równe, `!=` różne, `<` mniejsze niż, `>` większe niż, `<=` mniejsze lub równe, `>=` większe lub równe:
```python
age = 18
print(age == 18)  # True
print(age != 18)  # False
print(age < 18)   # False
print(age >= 18)  # True
```
Wynik można zapisać w zmiennej lub wyświetlić bezpośrednio. Pojedynczy `=` to przypisanie, a nie porównanie.

---

Operatory porównania nie ograniczają się do liczb. Łańcuchy znaków są porównywane znak po znaku według ich punktów kodowych, więc `"apple" < "banana"` to `True`, a ponieważ każda wielka litera jest przed małymi, `"Zoo" < "apple"` również daje `True`. Listy i krotki są porównywane element po elemencie w ten sam sposób:
```python
print("cat" < "dog")       # True
print([1, 2, 3] < [1, 3])  # True
print((1, 2) == (1, 2))    # True
```
Porównanie jest wyrażeniem, więc funkcja może użyć `return a < b` bezpośrednio, zamiast opakowywać je w `if`.

---

Porównania można **łączyć w łańcuch**: `1 < x < 10` sprawdza, że `x` jest większe niż `1` **i** mniejsze niż `10`, dokładnie tak jak `1 < x and x < 10`, ale `x` jest obliczane tylko raz:
```python
x = 5
print(1 < x < 10)   # True
print(1 < x <= 5)   # True
print(10 < x < 20)  # False
```
Dowolne operatory porównania można łączyć, a każdy odnosi się do swoich dwóch sąsiadów: `a < b == c` oznacza `a < b and b == c`. Odczytywanie łańcucha jako przedziału, `low < x < high`, to najczęstsze zastosowanie.

---

Operatory logiczne łączą wartości logiczne. `and` daje `True` tylko wtedy, gdy obie strony są `True`, `or` gdy choć jedna nią jest, a `not` odwraca pojedynczą wartość:
```python
age = 20
member = False
print(age >= 18 and member)  # False
print(age >= 18 or member)   # True
print(not member)            # True
```
Porównania wiążą mocniej niż operatory logiczne, więc `age >= 18 and member` nie wymaga nawiasów. Nawiasy są potrzebne, aby zgrupować `or` wewnątrz `and`: `a and (b or c)`.

---

Gdy `not`, `and` i `or` występują w jednym wyrażeniu, Python stosuje najpierw `not`, potem `and`, a na końcu `or`. Zatem `a or b and c` oznacza `a or (b and c)`, a `not a == b` oznacza `not (a == b)`:
```python
x = 6
print(x == 6 or x < 10 and x > 100)  # True: x == 6 or (False)
print(not x == 6)                    # False
```
Gdy zamierzone jest inne grupowanie, dodaj nawiasy; czynią one także wyrażenie łatwiejszym do czytania.

---

Każda wartość ma **wartość logiczną**. `bool(value)` zwraca `False` dla `0`, `0.0`, `None`, pustego łańcucha `""` oraz pustych kontenerów takich jak `[]`, `{}` i `set()`; każda inna wartość jest prawdziwa, w tym `"0"` i `[0]`:
```python
print(bool(0), bool(""), bool(None))   # False False False
print(bool(42), bool("0"), bool([0]))  # True True True
```
`if`, `while`, `and`, `or` i `not` korzystają z tej reguły, więc `if items:` sprawdza, że lista nie jest pusta, a `not name` sprawdza, że łańcuch jest pusty; nie trzeba pisać `len(items) > 0` ani `name == ""`.

---

Ponieważ `if value:` stosuje już wartość logiczną, porównywanie z `== True` lub `== False` jest zbędne, a nawet może być błędne: `2 == True` to `False`, a mimo to `2` jest prawdziwe. Sprawdzaj samą wartość:
```python
values = [0, 1, "", "a", None, [], [0]]
for value in values:
    if value:
        print(value)  # 1, a, [0]
```

---

`and` i `or` nie zawsze zwracają `True` lub `False`: zwracają jeden ze swoich **argumentów**. `a and b` zwraca `a`, jeśli jest fałszywe, a w przeciwnym razie `b`; `a or b` zwraca `a`, jeśli jest prawdziwe, a w przeciwnym razie `b`:
```python
print(0 and "x")       # 0
print(3 and "x")       # x
print("" or "none")    # none
print("hi" or "none")  # hi
```
Wynik jest prawdziwy lub fałszywy dokładnie wtedy, gdy jest takie całe wyrażenie, dlatego `if a and b:` nadal działa. Częstym zastosowaniem jest wartość domyślna: `name = user_input or "guest"`.

---

Operatory logiczne działają w trybie **skróconego obliczania**: `and` zatrzymuje się, gdy tylko jeden argument jest fałszywy, a `or`, gdy tylko jeden jest prawdziwy, ponieważ wynik jest już znany. Pozostałe argumenty nigdy nie są obliczane, więc jeśli są wywołaniami funkcji, nie wykonują się:
```python
def check(n):
    print("checking", n)
    return n > 0

check(-1) and check(5)  # prints only "checking -1"
check(2) or check(-3)   # prints only "checking 2"
```

---

`==` porównuje **wartości**; `is` porównuje **tożsamość**, czyli to, czy obie nazwy odnoszą się do dokładnie tego samego obiektu. Dwie równe listy zbudowane osobno są `==`, ale nie `is`:
```python
a = [1, 2]
b = [1, 2]
c = a
print(a == b, a is b, a is c)  # True False True
```
`is` jest przeznaczone dla singletonów takich jak `None`, `True` i `False`: pisz `value is None` lub `value is not None`, nigdy `value == None`, ponieważ klasa może zdefiniować `==` tak, by zwracało cokolwiek. Używanie `is` z liczbami lub łańcuchami jest zawodne i Python przed tym ostrzega.

---

Skrócone obliczanie to bezpieczny sposób na **zabezpieczenie** operacji, która zawiodłaby dla niektórych wartości. W `word is not None and len(word) < 4` `len(word)` wykonuje się tylko wtedy, gdy `word` nie jest `None`, więc wywołanie nigdy nie zgłasza błędu. Zabezpieczenie musi być pierwsze:
```python
def is_short(word):
    return word is not None and len(word) < 4

print(is_short(None))   # False
print(is_short("cat"))  # True
```
Pamiętaj, że `and` zwraca argument: `word and len(word) < 4` daje `None` dla `None` i `""` dla pustego łańcucha, a nie `False`. Zabezpiecz prawdziwym porównaniem, gdy wymagana jest wartość logiczna.

---

Operator `in` sprawdza **przynależność**: czy element jest na liście, w krotce lub zbiorze, czy podłańcuch jest w łańcuchu, albo czy klucz jest w słowniku. `not in` to jego zaprzeczenie:
```python
fruits = ["apple", "pear"]
print("pear" in fruits)          # True
print("kiwi" not in fruits)      # True
print("ex" in "text")            # True
print("age" in {"name": "Ada"})  # False, only keys are checked
```
Oba zwracają wartość logiczną i czytają się jak angielski, co czyni je preferowanym sposobem sprawdzania przynależności zamiast pisania pętli.
