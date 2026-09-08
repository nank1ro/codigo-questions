Un'**enumerazione** (o *enum*) definisce un tipo comune per un gruppo di valori correlati e fissi, come i giorni della settimana o i colori di un semaforo.
Invece di passare in giro stringhe o numeri sparsi, assegni a ogni valore un **nome**, così il codice è più leggibile e i refusi diventano errori.
In Python crei un enum importando `Enum` dal modulo `enum` e dichiarando una classe che eredita da esso.
Ogni attributo della classe è un **membro** dell'enum, con un nome e un valore:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
Per convenzione i nomi dei membri si scrivono in maiuscolo. Accedi a un membro tramite la classe, e stamparlo mostra i nomi della classe e del membro:
```python
favourite = Color.GREEN
print(favourite)  # Color.GREEN
```

---

Ogni membro di un enum ha due attributi: `name`, l'identificatore che hai scritto nella classe, e `value`, il valore che gli hai assegnato:
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.GREEN.name)   # GREEN
print(Color.GREEN.value)  # 2
```
Il valore può essere di qualsiasi tipo, non solo un intero: stringhe, tuple e float sono scelte comuni.
Un membro è un oggetto normale, quindi puoi memorizzarlo in una variabile e leggere i suoi attributi in seguito:
```python
chosen = Color.RED
print(chosen.value)  # 1
```

---

Ogni membro di un enum esiste **una sola volta**: ogni volta che scrivi `Color.RED` ottieni esattamente lo stesso oggetto.
Per questo motivo puoi confrontare i membri con `is` (identità) così come con `==`, ed entrambi danno lo stesso risultato:
```python
print(Color.RED is Color.RED)  # True
print(Color.RED == Color.BLUE) # False
```
Un membro **non** è uguale al suo valore grezzo, perché un membro e un numero semplice sono cose diverse:
```python
print(Color.RED == 1)        # False
print(Color.RED.value == 1)  # True
```
È questo che rende gli enum sicuri: un `1` proveniente da un'altra parte del programma non può essere scambiato per `Color.RED`.

---

Una classe enum è **iterabile**: un ciclo `for` sulla classe visita ogni membro, nell'ordine in cui sono stati dichiarati:
```python
for color in Color:
    print(color.name, color.value)
```
`len()` restituisce quanti membri ha l'enum, e `list(Color)` ne costruisce una lista:
```python
print(len(Color))    # 3
print(list(Color))   # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
```
Dentro una lista, i membri vengono mostrati con il loro `repr()`, che include il valore tra parentesi angolari.

---

Puoi ottenere un membro a partire dal suo **valore** chiamando la classe come una funzione, o dal suo **nome** usando le parentesi quadre:
```python
print(Color(2))        # Color.GREEN
print(Color["BLUE"])   # Color.BLUE
```
Entrambi sono comodi quando il valore o il nome proviene dall'esterno del programma, come un file o un input dell'utente.
Se non c'è corrispondenza, `Color(9)` solleva un `ValueError` e `Color["PINK"]` solleva un `KeyError`.

---

Spesso i valori esatti non contano: ti serve solo che i membri siano distinti.
In quel caso puoi lasciare che sia Python a scegliere i valori con `auto()`, importato anch'esso dal modulo `enum`.
Assegna `1` al primo membro e poi conta a salire:
```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()

print(Direction.EAST.value)  # 3
```

---

Un membro di un `Enum` semplice non può essere confrontato con `<` né aggiunto a un numero.
Quando i membri rappresentano **livelli** che richiedono un ordinamento, eredita invece da `IntEnum`: i suoi membri sono anche interi, quindi supportano confronti, aritmetica e ordinamento:
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
Un membro di `IntEnum` è anche uguale al suo valore intero: `Priority.LOW == 1` è `True`.

---

`StrEnum` (disponibile da Python 3.11) è la controparte stringa di `IntEnum`: i suoi membri sono anche stringhe, uguali al loro valore.
Questo li rende comodi ovunque siano previste stringhe semplici, come chiavi di configurazione o parametri di API:
```python
from enum import StrEnum

class Mode(StrEnum):
    LIGHT = "light"
    DARK = "dark"

print(Mode.DARK == "dark")  # True
print(Mode.DARK.upper())    # DARK
```
A differenza di un `Enum` semplice, convertire un membro di `StrEnum` in testo con `str()` o dentro una f-string restituisce il suo **valore**, non `Mode.DARK`.

---

Un enum è una classe, quindi può avere **metodi** e **proprietà** come qualsiasi altra classe.
Al loro interno, `self` è il membro su cui il metodo è stato chiamato, quindi puoi leggere `self.name`, `self.value` o confrontare `self` con altri membri:
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
Qualsiasi valore semplice assegnato nel corpo della classe diventa un membro, mentre le funzioni e le proprietà mai, indipendentemente da dove compaiono.

---

Se due membri condividono lo stesso valore, il secondo non è un nuovo membro ma un **alias** del primo:
```python
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # alias of ACTIVE

print(Status.ENABLED)  # Status.ACTIVE
print(len(Status))     # 1
```
Gli alias vengono saltati durante l'iterazione e non sono contati da `len()`.
Di solito un valore duplicato è un errore. Il decoratore `unique`, importato da `enum`, fa sì che Python sollevi un `ValueError` appena viene dichiarato un enum con alias:
```python
from enum import Enum, unique

@unique
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # ValueError: duplicate values found
```

---

Un `Flag` è un enum i cui membri possono essere **combinati**: un valore può contenere più membri contemporaneamente, come un insieme di opzioni.
Dichiara i suoi membri con `auto()`, che per un `Flag` assegna potenze di due (`1`, `2`, `4`, ...), così ogni combinazione ha un valore distinto:
```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
```
Usa `|` per combinare i membri, `in` per verificare se un membro fa parte di una combinazione e `value` per vedere il numero risultante:
```python
full = Permission.READ | Permission.WRITE | Permission.EXECUTE
print(Permission.WRITE in full)  # True
print(full.value)                # 7
print(full)                      # Permission.READ|WRITE|EXECUTE
```

---

Gli enum si abbinano naturalmente all'istruzione `match` (disponibile da Python 3.10), che confronta un valore con una serie di pattern `case` ed esegue il primo che corrisponde:
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
Scrivi sempre il membro con la sua classe, come `Light.RED`: un nome da solo come `case RED:` non confronterebbe nulla, catturerebbe soltanto il valore in una nuova variabile `RED` e corrisponderebbe a tutto.
Il jolly `case _:` è il caso predefinito e deve venire per ultimo, perché qualsiasi pattern dopo di esso non potrebbe mai essere raggiunto.

---

I membri di un enum sono **hashable**, quindi possono essere usati come chiavi di un dizionario e come elementi di un set.
Un dizionario indicizzato da un enum è un modo pulito per associare dati a ogni membro, e cercare un valore con un membro è più sicuro che usare una stringa grezza che potrebbe contenere un refuso:
```python
class Size(Enum):
    SMALL = 1
    LARGE = 2

prices = {Size.SMALL: 2.5, Size.LARGE: 4.5}
print(prices[Size.LARGE])  # 4.5
```
Poiché i membri possono comparire in qualsiasi collezione, tutto ciò che sai su liste, set e comprehensions funziona anche con loro:
```python
order = [Size.LARGE, Size.SMALL, Size.LARGE]
print(len(set(order)))  # 2
```

---

Il valore di un membro può essere una **tupla**, che ti permette di associare più dati a ogni membro.
Se l'enum definisce un metodo `__init__`, Python lo chiama una volta per membro, spacchettando la tupla nei suoi parametri, così puoi salvare ogni dato nel suo attributo:
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
Il `value` del membro resta tutta la tupla.

---

Iterare sulla classe e cercare i membri per nome funzionano bene insieme quando elabori dati provenienti dall'esterno, come righe di log o un file.
Una dictionary comprehension sulla classe prepara una voce per membro, poi `Level[name]` converte ogni stringa in arrivo nel membro corrispondente:
```python
counts = {level: 0 for level in Level}
counts[Level["INFO"]] += 1
```
Poiché l'enum conserva l'ordine di dichiarazione, iterare su `counts` in seguito restituisce i membri nello stesso ordine.

---

Oltre ai metodi normali, un enum può definire **metodi di classe** con `@classmethod`. Ricevono la classe enum stessa come `cls`, quindi sono il posto giusto per modi alternativi di trovare un membro:
```python
class Color(Enum):
    RED = auto()
    BLUE = auto()

    @classmethod
    def parse(cls, text):
        return cls[text.strip().upper()]

print(Color.parse(" blue "))  # Color.BLUE
```
Insieme a `auto()`, metodi, proprietà e ricerche, questo ti permette di costruire enum che incapsulano il proprio comportamento.
