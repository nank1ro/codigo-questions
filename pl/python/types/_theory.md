Każda wartość w Pythonie ma **typ**, który mówi, jakiego rodzaju to dane i co można z nimi zrobić.
Podstawowe typy wbudowane to:
- `int`, liczba całkowita jak `42` czy `-3`
- `float`, liczba z częścią dziesiętną jak `3.5`
- `str`, fragment tekstu jak `"hello"`
- `bool`, jedna z dwóch wartości `True` i `False`
- `NoneType`, typ specjalnej wartości `None`, która oznacza "brak wartości"

Wbudowana funkcja `type()` zwraca typ wartości. Wypisanie go pokazuje nazwę klasy:
```python
print(type(42))     # <class 'int'>
print(type("hi"))   # <class 'str'>
```
Nigdy nie napiszesz `NoneType` samodzielnie: `type(None)` go zwraca, ale ta nazwa nie jest wbudowana jak pozostałe cztery.

---

`type()` zwraca klasę wartości, więc możesz ją porównać z nazwą klasy za pomocą `is`:
```python
age = 30
print(type(age) is int)  # True
```
Najczęściej jednak chcesz tylko wiedzieć, **czy** wartość jest danego typu. Do tego służy `isinstance(value, cls)`, które zwraca `True` lub `False`:
```python
print(isinstance(age, int))    # True
print(isinstance(age, str))    # False
```
Drugim argumentem może być też **krotka** klas: wynikiem jest `True`, jeśli wartość należy do którejkolwiek z nich:
```python
print(isinstance(2.5, (int, float)))  # True
```

---

Python jest **dynamicznie typowany**: typ należy do **wartości**, a nie do zmiennej.
Zmienna to tylko nazwa przypisana do wartości i w każdej chwili możesz przypisać ją do wartości innego typu:
```python
x = 10
print(type(x))  # <class 'int'>
x = "ten"
print(type(x))  # <class 'str'>
```
Nie trzeba żadnej deklaracji ani konwersji: stara wartość jest po prostu zapominana.
To wygodne, ale oznacza też, że typ zmiennej jest znany dopiero podczas działania programu, więc pomyłkowe mieszanie typów ujawnia się jako błąd w czasie wykonania, a nie wcześniej.

---

Operatory arytmetyczne już znasz. Tutaj liczy się **typ wyniku**.
Połączenie `int` z `float` daje `float`, nawet gdy część dziesiętna wynosi zero:
```python
print(3 + 0.5)   # 3.5
print(2 * 1.0)   # 2.0
```
**Dzielenie rzeczywiste** `/` zawsze zwraca `float`, nawet gdy liczby dzielą się bez reszty:
```python
print(10 / 5)    # 2.0
print(7 / 2)     # 3.5
```
**Dzielenie całkowite** `//` zaokrągla wynik w dół do najbliższej liczby całkowitej (więc `-7 // 2` to `-4`) i zwraca `int`, gdy oba argumenty są całkowite. Razem z resztą `%` dzieli wielkość na całe części:
```python
print(7 // 2)    # 3
print(7 % 2)     # 1
```

---

Wartości nie zmieniają typu same z siebie: aby zamienić wartość na inny typ, wywołujesz nazwę typu jak funkcję. Nazywa się to **konwersją** (albo *rzutowaniem*):
```python
print(int("42"))      # 42
print(float("3.5"))   # 3.5
print(str(7))         # '7'
print(int(3.9))       # 3
```
`int()` i `float()` odczytują liczby zapisane jako tekst, czyli to, co dostajesz od użytkownika albo z plików. `str()` zamienia cokolwiek na tekst, więc można to połączyć operatorem `+` z innymi napisami.
Zwróć uwagę, że `int(3.9)` nie zaokrągla: odrzuca część dziesiętną.

---

Konwersja może się nie udać. `int("abc")` nie może dać liczby, więc zgłasza `ValueError` i program się zatrzymuje:
```python
int("abc")   # ValueError: invalid literal for int() with base 10: 'abc'
int("3.5")   # ValueError as well: "3.5" is not a whole number
```
Aby program działał dalej, możesz przechwycić błąd za pomocą `try` / `except`: kod w bloku `try` się wykonuje, a jeśli zgłosi wskazany błąd, wykonuje się blok `except`:
```python
try:
    number = int(text)
except ValueError:
    number = 0
```
Gdy konwersja się powiedzie, blok `except` jest pomijany.

---

Każdą wartość można zinterpretować jako wartość logiczną. `bool()` konwertuje wartość na `True` albo `False`, a ta sama reguła obowiązuje, gdy wartość jest użyta bezpośrednio w `if`.
Wartości uznawane za **fałszywe** to te "puste":
- liczba `0` (oraz `0.0`)
- pusty napis `""`
- puste kolekcje, takie jak `[]`, `{}`, `()` i `set()`
- `None`

Każda niepusta wartość jest **prawdziwa**, w tym liczby ujemne i napisy, które tylko wyglądają na puste, jak `"0"` czy `" "`:
```python
print(bool(0))     # False
print(bool(-1))    # True
print(bool(""))    # False
print(bool("0"))   # True
```
Dlatego `if name:` to popularny sposób sprawdzenia, że napis nie jest pusty.

---

`bool` jest **podklasą** `int`: `True` zachowuje się jak `1`, a `False` jak `0` wszędzie tam, gdzie oczekiwana jest liczba:
```python
print(True + 1)     # 2
print(True == 1)    # True
print(False * 10)   # 0
```
`sum()` sumuje elementy listy, więc zsumowanie listy wartości logicznych **zlicza**, ile z nich to `True`:
```python
answers = [True, False, True]
print(sum(answers))  # 2
```
Ze względu na tę relację podklasy `isinstance(True, int)` zwraca `True`, podczas gdy `type(True)` to nadal `bool`.

---

`None` to osobna wartość, która oznacza "nic tu nie ma". Zwraca ją funkcja, która nie ma instrukcji `return`, i jest to popularny symbol zastępczy dla wartości jeszcze nieznanej.
Ponieważ istnieje tylko jedno `None`, sprawdzaj je operatorem `is`, a nie `==`:
```python
result = None
if result is None:
    print("no result yet")
```
Każdy typ ma atrybut `__name__` zawierający jego nazwę jako napis, co przydaje się w komunikatach:
```python
print(type(3).__name__)     # int
print(type(None).__name__)  # NoneType
```

---

Wypisanie `float` pokazuje tyle cyfr, ile potrzeba do dokładnego przedstawienia liczby, co często jest zbyt dużo:
```python
print(19.999 * 3)  # 59.997
print(10 / 3)      # 3.3333333333333335
```
Wewnątrz f-stringa możesz dodać **specyfikację formatu** po dwukropku. `.2f` oznacza "liczba stałoprzecinkowa z 2 miejscami dziesiętnymi":
```python
total = 10 / 3
print(f"{total:.2f}")   # 3.33
print(f"{total:.0f}")   # 3
```
Wartość jest zaokrąglana do żądanej liczby miejsc, a w razie potrzeby dopisywane są zera: `f"{2.5:.2f}"` daje `2.50`.

---

Formatowanie zmienia tylko sposób wyświetlania liczby. Aby otrzymać zaokrągloną **wartość**, użyj wbudowanej funkcji `round()`:
```python
print(round(3.14159, 2))  # 3.14
print(round(2.71828, 1))  # 2.7
```
Z jednym argumentem `round()` zaokrągla do najbliższej liczby całkowitej i zwraca `int`; z liczbą miejsc dziesiętnych zwraca `float`:
```python
print(round(3.7))     # 4
print(round(3.7, 0))  # 4.0
```
Zwróć uwagę, że wartości dokładnie w połowie między dwiema liczbami zaokrąglają się do **parzystej**: `round(2.5)` to `2`, a `round(3.5)` to `4`.

---

`float` jest przechowywany binarnie na ustalonej liczbie bitów, więc większość liczb dziesiętnych może być tylko **przybliżona**. Błąd jest maleńki, ale ujawnia się w arytmetyce:
```python
print(0.1 + 0.2)   # 0.30000000000000004
```
Z tego powodu nie powinieneś porównywać liczb zmiennoprzecinkowych na dokładną równość. Zaokrąglij obie strony albo użyj `math.isclose()`, które sprawdza, czy dwie liczby są równe z dokładnością do maleńkiej tolerancji:
```python
import math
print(round(0.1 + 0.2, 2) == 0.3)  # True
print(math.isclose(0.1 + 0.2, 0.3))  # True
```
Liczby całkowite nie mają tego problemu: `1 + 2 == 3` jest zawsze `True`.

---

W przeciwieństwie do wielu języków liczby całkowite w Pythonie **nie mają maksymalnego rozmiaru**: `int` rośnie, aby pomieścić tyle cyfr, ile trzeba, więc duże obliczenia pozostają dokładne:
```python
print(3 ** 100)  # 515377520732011331036461129765621272702107522001
```
`float` natomiast zachowuje tylko około 15 cyfr znaczących, więc ta sama potęga jako float traci precyzję:
```python
print(3.0 ** 100)  # 5.153775207320113e+47
```
Ponieważ `str()` działa na dowolnym `int`, szybkim sposobem policzenia cyfr liczby jest zmierzenie długości jej tekstu.

---

Oczekiwany typ zmiennej, parametru lub wartości zwracanej możesz zapisać jako **adnotację typu**: dwukropek po nazwie dla zmiennych i parametrów, strzałka `->` przed dwukropkiem dla wartości zwracanej:
```python
count: int = 3

def greet(name: str) -> str:
    return "Hi " + name
```
Adnotacje są **dokumentacją** dla ludzi i dla narzędzi takich jak edytory: Python ich **nie** sprawdza. Ten kod działa bez zastrzeżeń i wypisuje `hello`:
```python
count: int = "hello"
print(count)
```
Adnotacje jasno wyrażają zamierzone typy, ale o rzeczywistym typie wciąż decyduje wartość.

---

Konwersje można łączyć. `int("3.7")` się nie udaje, ale `float("3.7")` działa, a `int()` z wartości `float` odrzuca część dziesiętną:
```python
number = float("3.7")   # 3.7
print(int(number))      # 3
```
`bool()` stosuje reguły prawdziwości: `bool("")` to `False`, a zwróć uwagę, że `bool("False")` to `True`, ponieważ jest to niepusty napis.

---

Tekst pochodzący z zewnątrz jest zawsze typu `str` i to twój program musi ustalić, jaki typ naprawdę zawiera.
Częstym podejściem jest wypróbowanie najpierw **najbardziej restrykcyjnej** konwersji i przejście do kolejnej, gdy zgłosi `ValueError`:
```python
try:
    value = int(text)
except ValueError:
    value = float(text)
```
Zagnieżdżenie drugiego `try` wewnątrz bloku `except` pozwala cofnąć się jeszcze raz, na przykład aby zachować tekst bez zmian.
