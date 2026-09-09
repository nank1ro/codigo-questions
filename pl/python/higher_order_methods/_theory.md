W Pythonie funkcja jest **wartością**, tak jak liczba czy ciąg znaków. Możesz zapisać ją w zmiennej, umieścić na liście lub przekazać do innej funkcji. Tylko nawiasy ją wywołują: `shout` to sama funkcja, `shout("hi")` to jej wynik:
```python
def shout(text):
    return text.upper() + "!"

say = shout
print(say("hi"))  # HI!
```
Funkcja, która przyjmuje inną funkcję jako parametr albo ją zwraca, nazywa się **funkcją wyższego rzędu**. Wewnątrz niej parametr jest wywoływany z nawiasami jak każda inna funkcja:
```python
def apply(func, value):
    return func(value)

print(apply(shout, "bye"))  # BYE!
print(apply(len, "bye"))    # 3
```

---

Przekazanie funkcji jako argumentu pozwala wywołującemu zdecydować **co** zrobić, podczas gdy funkcja wyższego rzędu decyduje **ile razy** albo **na czym**. Parametr funkcyjny może być wywoływany dowolnie wiele razy, a jego wynik można podać z powrotem do niego:
```python
def repeat(func, value, times):
    for _ in range(times):
        value = func(value)
    return value

def add_one(n):
    return n + 1

print(repeat(add_one, 0, 3))  # 3
```
Działa każdy obiekt wywoływalny: funkcja z `def`, wbudowana jak `len` czy lambda.

---

Wbudowana funkcja `map(func, iterable)` wywołuje `func` na każdym elemencie i produkuje wyniki, po jednym dla każdego elementu. Zwraca leniwy *obiekt map*, więc owiń go w `list()`, aby zobaczyć wartości:
```python
numbers = [1, 2, 3]
print(list(map(lambda n: n * 10, numbers)))  # [10, 20, 30]
```
Można przekazać każdy obiekt wywoływalny, nie tylko lambdę: wbudowaną funkcję taką jak `len` albo metodę wziętą z jej klasy, taką jak `str.upper`, która przyjmuje ciąg znaków jako pierwszy argument:
```python
names = ["ada", "linus"]
print(list(map(str.upper, names)))  # ['ADA', 'LINUS']
print(list(map(len, names)))        # [3, 5]
```

---

Wbudowana funkcja `filter(func, iterable)` zachowuje tylko te elementy, dla których `func` zwraca wartość prawdziwą. Podobnie jak `map` zwraca leniwy obiekt, który trzeba zamienić na listę:
```python
numbers = [4, -2, 7, 0]
print(list(filter(lambda n: n > 0, numbers)))  # [4, 7]
```
Funkcja przekazana do `filter` nazywa się **predykatem**: przyjmuje jeden element i odpowiada na pytanie tak/nie o tym elemencie. Przekazanie `None` zamiast funkcji zachowuje elementy prawdziwe same w sobie, odrzucając `0`, `""` i `None`.

---

`sorted(iterable, key=func)` porządkuje elementy według wartości, którą `func` zwraca dla każdego z nich, nie zmieniając samych elementów. Dodaj `reverse=True`, aby otrzymać największe na początku:
```python
words = ["kiwi", "fig", "banana"]
print(sorted(words, key=len))                # ['fig', 'kiwi', 'banana']
print(sorted(words, key=len, reverse=True))  # ['banana', 'kiwi', 'fig']
```
Sortowanie jest **stabilne**: elementy o równych kluczach zachowują swoją pierwotną kolejność. Funkcja `key` jest wywoływana raz na element, a jej wyniki służą tylko do porównywania, więc wynik nadal zawiera oryginalne słowa, a nie ich długości.

---

Funkcja `key` może wybierać **dowolną część** elementu. Dla listy krotek `lambda s: s[1]` sortuje według drugiego elementu każdej krotki; dla listy słowników `lambda d: d["age"]` sortuje według wartości:
```python
pairs = [("b", 2), ("a", 3), ("c", 1)]
print(sorted(pairs, key=lambda p: p[1]))  # [('c', 1), ('b', 2), ('a', 3)]
```
`min` i `max` przyjmują ten sam parametr `key`, więc `max(pairs, key=lambda p: p[1])` zwraca `('a', 3)`: całą krotkę, a nie tylko liczbę.

---

Funkcja może też **zwracać** funkcję. Zdefiniuj funkcję wewnętrzną przez `def` i zwróć ją bez wywoływania:
```python
def make_greeter(greeting):
    def greet(name):
        return greeting + ", " + name
    return greet

hello = make_greeter("Hello")
print(hello("Ada"))  # Hello, Ada
```
Funkcja wewnętrzna nadal używa `greeting` nawet po zakończeniu `make_greeter`: **pamięta** zmienne z zakresu, w którym powstała. Taka funkcja nazywa się **domknięciem**. Każde wywołanie `make_greeter` tworzy nowe, niezależne domknięcie z własnym `greeting`.

---

Domknięcie może odczytywać zmienne funkcji otaczającej, ale przypisanie do jednej z nich tworzy **nową zmienną lokalną**. Aby aktualizować zewnętrzną zmienną, zadeklaruj ją przez `nonlocal` wewnątrz funkcji wewnętrznej:
```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```
`global` szukałoby `count` na poziomie modułu, gdzie ono nie istnieje. Dzięki `nonlocal` każde wywołanie zwróconej funkcji aktualizuje to samo `count`, więc domknięcie przenosi stan między wywołaniami, jak malutki obiekt.

---

`reduce(func, iterable, initial)` z modułu `functools` zwija sekwencję do **jednej wartości**. Wywołuje `func` z wynikiem dotychczasowym i kolejnym elementem, zaczynając od `initial`:
```python
from functools import reduce

total = reduce(lambda acc, n: acc + n, [1, 2, 3], 0)
print(total)  # 6
```
Kroki to `0 + 1`, potem `1 + 2`, potem `3 + 3`. Gdy `initial` jest pominięte, pierwszym elementem jest wartość początkowa, ale wtedy pusta sekwencja zgłasza `TypeError`, więc podawaj wartość początkową zawsze, gdy sekwencja może być pusta.

---

`partial(func, *fixed)` z `functools` buduje nową funkcję z częścią argumentów **już wypełnionych**. Wywołanie wyniku podaje pozostałe:
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25
```
Argumenty pozycyjne podane do `partial` wypełniają pierwsze parametry; argumenty słownikowe ustalają parametr po nazwie i nadal można je nadpisać przy wywołaniu. Obiekt partial to zwykły obiekt wywoływalny, więc można go przekazać do `map`, `sorted` czy każdej innej funkcji wyższego rzędu.

---

`partial` przydaje się z wbudowanymi funkcjami przyjmującymi opcje. `int(text, base=16)` analizuje szesnastkowy ciąg znaków; ustalenie podstawy daje konwerter o jednym argumencie, który pasuje do `map`:
```python
from functools import partial

hex_to_int = partial(int, base=16)
print(hex_to_int("ff"))                      # 255
print(list(map(hex_to_int, ["a", "10"])))    # [10, 16]
```
Obiekt partial pamięta, co opakowuje: `hex_to_int.func` to `int`, a `hex_to_int.keywords` to `{'base': 16}`.

---

**Dekorator** to funkcja wyższego rzędu, która przyjmuje funkcję i zwraca nową opakowującą ją, zwykle po to, aby dodać zachowanie przed lub po oryginalnym wywołaniu:
```python
def announce(func):
    def wrapper(name):
        print("calling " + func.__name__)
        return func(name)
    return wrapper
```
`func.__name__` to nazwa, z jaką funkcja została zdefiniowana. Zastosowanie dekoratora to zwykłe wywołanie: `greet = announce(greet)`. Składnia `@` umieszczona w linii **nad** `def` robi dokładnie to:
```python
@announce
def greet(name):
    return "Hello, " + name
```
Dekorator musi być zdefiniowany przed użyciem go przez `@`, ponieważ zamiana następuje w chwili, gdy wykonywane jest `def`.

---

Dekorator przyjmujący tylko jeden argument ma niewielkie zastosowanie. Aby opakować **dowolną** funkcję, opakowanie zbiera wszystkie argumenty pozycyjne w `*args` i wszystkie argumenty słownikowe w `**kwargs`, a następnie przekazuje je bez zmian:
```python
def uppercase(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()
    return wrapper

@uppercase
def greet(name, punctuation="!"):
    return "hello " + name + punctuation

print(greet("ada"))                    # HELLO ADA!
print(greet("ada", punctuation="?"))   # HELLO ADA?
```
Wewnątrz opakowania `args` jest krotką, a `kwargs` słownikiem; `*` i `**` w wywołaniu rozpakowują je z powrotem na osobne argumenty.

---

`any(iterable)` zwraca `True`, jeśli **co najmniej jeden** element jest prawdziwy, `all(iterable)` — jeśli **każdy** element jest. Naturalnie łączą się z **wyrażeniem generatora**: wyrażeniem listy zapisanym bez nawiasów kwadratowych, które produkuje wartości pojedynczo zamiast budować listę:
```python
ages = [21, 34, 17]
print(any(age >= 18 for age in ages))  # True
print(all(age >= 18 for age in ages))  # False
```
Ponieważ wartości są produkowane leniwie, `any` zatrzymuje się na pierwszym `True`, a `all` na pierwszym `False`, nie obliczając reszty. `sum` także przyjmuje wyrażenie generatora: `sum(1 for age in ages if age >= 18)` liczy dorosłych.
