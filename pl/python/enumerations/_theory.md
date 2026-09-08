**Enumeracja** (*enum*) definiuje wspólny typ dla grupy powiązanych, stałych wartości, takich jak dni tygodnia czy kolory świateł drogowych.
Zamiast przekazywać luźne ciągi znaków lub liczby, nadajesz każdej wartości **nazwę**, dzięki czemu kod jest bardziej czytelny, a literówki stają się błędami.
W Pythonie enumerację tworzysz, importując `Enum` z modułu `enum` i deklarując klasę, która po nim dziedziczy.
Każdy atrybut klasy jest **elementem** enumeracji, mającym nazwę i wartość:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
Zgodnie z konwencją nazwy elementów pisze się wielkimi literami. Do elementu odwołujesz się przez klasę, a jego wypisanie pokazuje nazwy klasy i elementu:
```python
favourite = Color.GREEN
print(favourite)  # Color.GREEN
```

---

Każdy element enumeracji ma dwa atrybuty: `name`, czyli identyfikator zapisany w klasie, oraz `value`, czyli przypisaną mu wartość:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.GREEN.name)   # GREEN
print(Color.GREEN.value)  # 2
```
Wartość może być dowolnego typu, nie tylko liczbą całkowitą: częstym wyborem są ciągi znaków, krotki i liczby zmiennoprzecinkowe.
Element jest zwykłym obiektem, więc możesz zapisać go w zmiennej i później odczytać jego atrybuty:
```python
chosen = Color.RED
print(chosen.value)  # 1
```

---

Każdy element enumeracji istnieje **tylko raz**: za każdym razem, gdy napiszesz `Color.RED`, otrzymujesz dokładnie ten sam obiekt.
Dlatego możesz porównywać elementy zarówno za pomocą `is` (tożsamości), jak i `==`, a oba dają ten sam wynik:
```python
print(Color.RED is Color.RED)  # True
print(Color.RED == Color.BLUE) # False
```
Element **nie** jest równy swojej surowej wartości, ponieważ element i zwykła liczba to różne rzeczy:
```python
print(Color.RED == 1)        # False
print(Color.RED.value == 1)  # True
```
To właśnie sprawia, że enumeracje są bezpieczne: `1` pochodząca z innego miejsca w programie nie może zostać pomylona z `Color.RED`.

---

Klasa enumeracji jest **iterowalna**: pętla `for` po klasie odwiedza każdy element w kolejności, w jakiej zostały zadeklarowane:
```python
for color in Color:
    print(color.name, color.value)
```
`len()` zwraca liczbę elementów enumeracji, a `list(Color)` buduje z nich listę:
```python
print(len(Color))    # 3
print(list(Color))   # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
```
Na liście elementy są wyświetlane za pomocą `repr()`, która zawiera wartość w nawiasach ostrych.

---

Element możesz uzyskać na podstawie jego **wartości**, wywołując klasę jak funkcję, albo na podstawie jego **nazwy**, używając nawiasów kwadratowych:
```python
print(Color(2))        # Color.GREEN
print(Color["BLUE"])   # Color.BLUE
```
Oba sposoby są przydatne, gdy wartość lub nazwa pochodzą spoza programu, na przykład z pliku lub od użytkownika.
Jeśli nic nie pasuje, `Color(9)` zgłasza `ValueError`, a `Color["PINK"]` zgłasza `KeyError`.

---

Często dokładne wartości nie mają znaczenia: potrzebujesz jedynie, aby elementy były różne.
W takim przypadku możesz pozwolić, aby Python dobrał wartości za pomocą `auto()`, również importowanego z modułu `enum`.
Przypisuje on `1` pierwszemu elementowi, a następnie liczy w górę:
```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()

print(Direction.EAST.value)  # 3
```

---

Zwykłego elementu `Enum` nie można porównywać za pomocą `<` ani dodawać do liczby.
Gdy elementy reprezentują **poziomy**, które wymagają uporządkowania, dziedzicz zamiast tego z `IntEnum`: jego elementy są też liczbami całkowitymi, więc obsługują porównania, arytmetykę i sortowanie:
```python
from enum import IntEnum

class Priority(IntEnum):
    LOW = 1
    MEDIUM = 2
    HIGH = 3

print(Priority.HIGH > Priority.LOW)  # True
print(Priority.LOW + 1)              # 2
print(int(Priority.MEDIUM))          # 2
```
Element `IntEnum` jest też równy swojej wartości całkowitej: `Priority.LOW == 1` daje `True`.

---

`StrEnum` (dostępny od Pythona 3.11) to odpowiednik `IntEnum` dla ciągów znaków: jego elementy są również ciągami znaków, równymi swojej wartości.
Dzięki temu są wygodne wszędzie tam, gdzie oczekiwane są zwykłe ciągi znaków, na przykład w kluczach konfiguracji czy parametrach API:
```python
from enum import StrEnum

class Mode(StrEnum):
    LIGHT = "light"
    DARK = "dark"

print(Mode.DARK == "dark")  # True
print(Mode.DARK.upper())    # DARK
```
W przeciwieństwie do zwykłego `Enum`, przekształcenie elementu `StrEnum` na tekst za pomocą `str()` lub w f-stringu daje jego **wartość**, a nie `Mode.DARK`.

---

Enumeracja jest klasą, więc może mieć **metody** i **właściwości** jak każda inna klasa.
Wewnątrz nich `self` to element, na którym wywołano metodę, więc możesz sprawdzać `self.name`, `self.value` albo porównywać `self` z innymi elementami:
```python
from enum import Enum

class Light(Enum):
    RED = 1
    GREEN = 2

    def can_go(self):
        return self is Light.GREEN

    @property
    def label(self):
        return self.name.lower()

print(Light.GREEN.can_go())  # True
print(Light.RED.label)       # red
```
Każda zwykła wartość przypisana w ciele klasy staje się elementem, natomiast funkcje i właściwości nigdy, niezależnie od tego, gdzie się pojawią.

---

Jeśli dwa elementy mają tę samą wartość, drugi nie jest nowym elementem, lecz **aliasem** pierwszego:
```python
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # alias of ACTIVE

print(Status.ENABLED)  # Status.ACTIVE
print(len(Status))     # 1
```
Aliasy są pomijane podczas iteracji i nie są liczone przez `len()`.
Zwykle zduplikowana wartość to błąd. Dekorator `unique`, importowany z `enum`, sprawia, że Python zgłasza `ValueError`, gdy tylko zostanie zadeklarowana enumeracja z aliasami:
```python
from enum import Enum, unique

@unique
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # ValueError: duplicate values found
```

---

`Flag` to enumeracja, której elementy można **łączyć**: jedna wartość może przechowywać kilka elementów naraz, jak zestaw opcji.
Zadeklaruj jej elementy za pomocą `auto()`, które dla `Flag` przypisuje potęgi dwójki (`1`, `2`, `4`, ...), dzięki czemu każda kombinacja ma odrębną wartość:
```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
```
Użyj `|`, aby łączyć elementy, `in`, aby sprawdzić, czy element jest częścią kombinacji, oraz `value`, aby zobaczyć powstałą liczbę:
```python
full = Permission.READ | Permission.WRITE | Permission.EXECUTE
print(Permission.WRITE in full)  # True
print(full.value)                # 7
print(full)                      # Permission.READ|WRITE|EXECUTE
```

---

Enumeracje naturalnie łączą się z instrukcją `match` (dostępną od Pythona 3.10), która porównuje wartość z serią wzorców `case` i wykonuje pierwszy pasujący:
```python
def action(light):
    match light:
        case Light.RED:
            return "Stop"
        case Light.GREEN:
            return "Go"
        case _:
            return "Slow down"
```
Zawsze zapisuj element razem z jego klasą, na przykład `Light.RED`: sama nazwa, jak `case RED:`, nie porównywałaby niczego — po prostu przechwyciłaby wartość do nowej zmiennej `RED` i pasowałaby do wszystkiego.
Wzorzec `case _:` jest domyślny i musi wystąpić jako ostatni, ponieważ żaden wzorzec po nim nie mógłby zostać osiągnięty.

---

Elementy enumeracji są **hashowalne**, więc mogą służyć jako klucze słownika i elementy zbioru.
Słownik kluczowany enumeracją to elegancki sposób na dołączenie danych do każdego elementu, a wyszukiwanie za pomocą elementu jest bezpieczniejsze niż użycie surowego ciągu znaków, w którym można popełnić literówkę:
```python
class Size(Enum):
    SMALL = 1
    LARGE = 2

prices = {Size.SMALL: 2.5, Size.LARGE: 4.5}
print(prices[Size.LARGE])  # 4.5
```
Ponieważ elementy mogą pojawiać się w dowolnej kolekcji, wszystko, co wiesz o listach, zbiorach i comprehension, działa też z nimi:
```python
order = [Size.LARGE, Size.SMALL, Size.LARGE]
print(len(set(order)))  # 2
```

---

Wartością elementu może być **krotka**, co pozwala dołączyć do każdego elementu kilka danych naraz.
Jeśli enumeracja definiuje metodę `__init__`, Python wywołuje ją raz dla każdego elementu, rozpakowując krotkę do jej parametrów, więc możesz zapisać każdą część w osobnym atrybucie:
```python
from enum import Enum

class Planet(Enum):
    EARTH = (5.97, 6371)
    MARS = (0.64, 3390)

    def __init__(self, mass, radius):
        self.mass = mass
        self.radius = radius

print(Planet.MARS.radius)  # 3390
print(Planet.MARS.value)   # (0.64, 3390)
```
`value` elementu pozostaje całą krotką.

---

Iterowanie po klasie i wyszukiwanie elementów po nazwie dobrze ze sobą współpracują, gdy przetwarzasz dane pochodzące z zewnątrz, na przykład linie logu lub plik.
Dictionary comprehension po klasie przygotowuje jeden wpis dla każdego elementu, a `Level[name]` przekształca każdy przychodzący ciąg znaków na pasujący element:
```python
counts = {level: 0 for level in Level}
counts[Level["INFO"]] += 1
```
Ponieważ enumeracja zachowuje kolejność deklaracji, iterowanie po `counts` daje później elementy w tej samej kolejności.

---

Oprócz zwykłych metod enumeracja może definiować **metody klasy** za pomocą `@classmethod`. Otrzymują one samą klasę enumeracji jako `cls`, więc to właściwe miejsce na alternatywne sposoby znajdowania elementu:
```python
class Color(Enum):
    RED = auto()
    BLUE = auto()

    @classmethod
    def parse(cls, text):
        return cls[text.strip().upper()]

print(Color.parse(" blue "))  # Color.BLUE
```
Razem z `auto()`, metodami, właściwościami i wyszukiwaniem pozwala to budować enumeracje, które niosą własne zachowanie.
