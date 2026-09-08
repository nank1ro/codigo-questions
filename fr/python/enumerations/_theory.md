Une **énumération** (ou *enum*) définit un type commun pour un groupe de valeurs fixes et liées entre elles, comme les jours de la semaine ou les couleurs d'un feu tricolore.
Au lieu de faire circuler des chaînes ou des nombres isolés, vous donnez à chaque valeur un **nom**, ce qui rend le code plus lisible et transforme les fautes de frappe en erreurs.
En Python, vous créez une enum en important `Enum` depuis le module `enum` et en déclarant une classe qui en hérite.
Chaque attribut de classe est un **membre** de l'enum, avec un nom et une valeur :
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3
```
Par convention, les noms des membres s'écrivent en majuscules. Vous accédez à un membre via la classe, et l'afficher montre les noms de la classe et du membre :
```python
favourite = Color.GREEN
print(favourite)  # Color.GREEN
```

---

Chaque membre d'une enum a deux attributs : `name`, l'identifiant que vous avez écrit dans la classe, et `value`, la valeur que vous lui avez assignée :
```python
from enum import Enum

class Color(Enum):
    RED = 1
    GREEN = 2

print(Color.GREEN.name)   # GREEN
print(Color.GREEN.value)  # 2
```
La valeur peut être de n'importe quel type, pas seulement un entier : des chaînes, des tuples et des flottants sont des choix courants.
Un membre est un objet normal, vous pouvez donc le stocker dans une variable et lire ses attributs plus tard :
```python
chosen = Color.RED
print(chosen.value)  # 1
```

---

Chaque membre d'une enum existe **une seule fois** : chaque fois que vous écrivez `Color.RED`, vous obtenez exactement le même objet.
Pour cette raison, vous pouvez comparer les membres avec `is` (identité) ainsi qu'avec `==`, et les deux donnent le même résultat :
```python
print(Color.RED is Color.RED)  # True
print(Color.RED == Color.BLUE) # False
```
Un membre n'est **pas** égal à sa valeur brute, car un membre et un simple nombre sont des choses différentes :
```python
print(Color.RED == 1)        # False
print(Color.RED.value == 1)  # True
```
C'est ce qui rend les enums sûres : un `1` venant d'ailleurs dans le programme ne peut pas être confondu avec `Color.RED`.

---

Une classe enum est **itérable** : une boucle `for` sur la classe visite chaque membre, dans l'ordre où ils ont été déclarés :
```python
for color in Color:
    print(color.name, color.value)
```
`len()` renvoie le nombre de membres de l'enum, et `list(Color)` construit une liste de ces membres :
```python
print(len(Color))    # 3
print(list(Color))   # [<Color.RED: 1>, <Color.GREEN: 2>, <Color.BLUE: 3>]
```
Dans une liste, les membres sont affichés avec leur `repr()`, qui inclut la valeur entre chevrons.

---

Vous pouvez obtenir un membre à partir de sa **valeur** en appelant la classe comme une fonction, ou à partir de son **nom** en utilisant les crochets :
```python
print(Color(2))        # Color.GREEN
print(Color["BLUE"])   # Color.BLUE
```
Les deux sont pratiques quand la valeur ou le nom vient de l'extérieur du programme, comme un fichier ou une saisie utilisateur.
Si rien ne correspond, `Color(9)` lève une `ValueError` et `Color["PINK"]` lève une `KeyError`.

---

Souvent, les valeurs exactes n'ont pas d'importance : vous avez seulement besoin que les membres soient distincts.
Dans ce cas, vous pouvez laisser Python choisir les valeurs avec `auto()`, également importé depuis le module `enum`.
Il assigne `1` au premier membre puis compte à partir de là :
```python
from enum import Enum, auto

class Direction(Enum):
    NORTH = auto()
    SOUTH = auto()
    EAST = auto()

print(Direction.EAST.value)  # 3
```

---

Un membre d'une `Enum` simple ne peut pas être comparé avec `<` ni ajouté à un nombre.
Quand les membres représentent des **niveaux** qui doivent être ordonnés, héritez plutôt de `IntEnum` : ses membres sont aussi des entiers, ils prennent donc en charge les comparaisons, l'arithmétique et le tri :
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
Un membre d'`IntEnum` est aussi égal à sa valeur entière : `Priority.LOW == 1` vaut `True`.

---

`StrEnum` (disponible depuis Python 3.11) est l'équivalent chaîne de caractères de `IntEnum` : ses membres sont aussi des chaînes, égaux à leur valeur.
Cela les rend pratiques partout où des chaînes simples sont attendues, comme les clés de configuration ou les paramètres d'API :
```python
from enum import StrEnum

class Mode(StrEnum):
    LIGHT = "light"
    DARK = "dark"

print(Mode.DARK == "dark")  # True
print(Mode.DARK.upper())    # DARK
```
Contrairement à une `Enum` simple, convertir un membre `StrEnum` en texte avec `str()` ou dans une f-string donne sa **valeur**, pas `Mode.DARK`.

---

Une enum est une classe, elle peut donc avoir des **méthodes** et des **propriétés** comme n'importe quelle autre classe.
À l'intérieur, `self` est le membre sur lequel la méthode a été appelée, vous pouvez donc consulter `self.name`, `self.value` ou comparer `self` avec d'autres membres :
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
Toute valeur simple assignée dans le corps de la classe devient un membre, tandis que les fonctions et les propriétés n'en deviennent jamais, peu importe où elles apparaissent.

---

Si deux membres partagent la même valeur, le second n'est pas un nouveau membre mais un **alias** du premier :
```python
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # alias of ACTIVE

print(Status.ENABLED)  # Status.ACTIVE
print(len(Status))     # 1
```
Les alias sont ignorés lors de l'itération et ne sont pas comptés par `len()`.
Habituellement, une valeur dupliquée est une erreur. Le décorateur `unique`, importé depuis `enum`, fait lever à Python une `ValueError` dès qu'une enum avec des alias est déclarée :
```python
from enum import Enum, unique

@unique
class Status(Enum):
    ACTIVE = 1
    ENABLED = 1  # ValueError: duplicate values found
```

---

Un `Flag` est une enum dont les membres peuvent être **combinés** : une valeur peut contenir plusieurs membres à la fois, comme un ensemble d'options.
Déclarez ses membres avec `auto()`, qui pour un `Flag` assigne des puissances de deux (`1`, `2`, `4`, ...), afin que chaque combinaison ait une valeur distincte :
```python
from enum import Flag, auto

class Permission(Flag):
    READ = auto()
    WRITE = auto()
    EXECUTE = auto()
```
Utilisez `|` pour combiner des membres, `in` pour vérifier si un membre fait partie d'une combinaison et `value` pour voir le nombre qui en résulte :
```python
full = Permission.READ | Permission.WRITE | Permission.EXECUTE
print(Permission.WRITE in full)  # True
print(full.value)                # 7
print(full)                      # Permission.READ|WRITE|EXECUTE
```

---

Les enums se marient naturellement avec l'instruction `match` (disponible depuis Python 3.10), qui compare une valeur à une série de motifs `case` et exécute le premier qui correspond :
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
Écrivez toujours le membre avec sa classe, comme `Light.RED` : un nom seul tel que `case RED:` ne comparerait rien, il capturerait simplement la valeur dans une nouvelle variable `RED` et correspondrait à tout.
Le joker `case _:` est le cas par défaut et doit venir en dernier, car aucun motif après lui ne pourrait jamais être atteint.

---

Les membres d'une enum sont **hachables**, ils peuvent donc servir de clés de dictionnaire et d'éléments de set.
Un dictionnaire indexé par une enum est une façon propre d'attacher des données à chaque membre, et le consulter avec un membre est plus sûr que d'utiliser une chaîne brute qui pourrait être mal orthographiée :
```python
class Size(Enum):
    SMALL = 1
    LARGE = 2

prices = {Size.SMALL: 2.5, Size.LARGE: 4.5}
print(prices[Size.LARGE])  # 4.5
```
Comme les membres peuvent apparaître dans n'importe quelle collection, tout ce que vous savez sur les listes, les sets et les compréhensions fonctionne aussi avec eux :
```python
order = [Size.LARGE, Size.SMALL, Size.LARGE]
print(len(set(order)))  # 2
```

---

La valeur d'un membre peut être un **tuple**, ce qui permet d'attacher plusieurs données à chaque membre.
Si l'enum définit une méthode `__init__`, Python l'appelle une fois par membre, en décompressant le tuple dans ses paramètres, vous pouvez donc enregistrer chaque donnée dans son propre attribut :
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
La `value` du membre reste le tuple entier.

---

Itérer sur la classe et rechercher des membres par nom fonctionnent bien ensemble quand vous traitez des données venant de l'extérieur, comme des lignes de log ou un fichier.
Une compréhension de dictionnaire sur la classe prépare une entrée par membre, puis `Level[name]` convertit chaque chaîne entrante en le membre correspondant :
```python
counts = {level: 0 for level in Level}
counts[Level["INFO"]] += 1
```
Comme l'enum conserve l'ordre de déclaration, itérer sur `counts` ensuite donne les membres dans ce même ordre.

---

En plus des méthodes classiques, une enum peut définir des **méthodes de classe** avec `@classmethod`. Elles reçoivent la classe enum elle-même comme `cls`, elles sont donc l'endroit idéal pour des façons alternatives de trouver un membre :
```python
class Color(Enum):
    RED = auto()
    BLUE = auto()

    @classmethod
    def parse(cls, text):
        return cls[text.strip().upper()]

print(Color.parse(" blue "))  # Color.BLUE
```
Avec `auto()`, les méthodes, les propriétés et les recherches, cela vous permet de construire des enums qui portent leur propre comportement.
