Une tâche très courante consiste à construire une nouvelle liste à partir d'une liste existante.
Avec une boucle `for` et `append()`, cela prend quelques lignes :
```python
nums = [1, 2, 3]
doubled = []
for n in nums:
    doubled.append(n * 2)
print(doubled)  # [2, 4, 6]
```
Python propose une forme plus courte pour exactement cette tâche : la **list comprehension**, qui construit toute la liste en une seule expression :
```python
doubled = [n * 2 for n in nums]
```
La syntaxe est `[expression for élément in itérable]` : la partie `for` parcourt les éléments, et l'expression à gauche est évaluée pour chacun d'eux.
Le résultat est une toute nouvelle liste, exactement la même que celle construite avec la boucle.

---

L'expression à gauche peut être n'importe quoi qui produit une valeur : un calcul, un appel de fonction, un appel de méthode.
La variable de boucle peut avoir n'importe quel nom, et elle n'existe qu'à l'intérieur des crochets :
```python
prices = [10, 20]
with_tax = [price * 1.2 for price in prices]
print(with_tax)  # [12.0, 24.0]
```

---

Une comprehension peut aussi **filtrer** les éléments.
Ajoutez une condition `if` après la partie `for` : seuls les éléments pour lesquels la condition est `True` se retrouvent dans la nouvelle liste :
```python
nums = [5, 12, 8, 20]
big = [n for n in nums if n > 10]
print(big)  # [12, 20]
```
C'est la même chose qu'une boucle avec un `if` à l'intérieur, et cela remplace `filter()` avec une lambda de manière plus lisible.

---

La condition de filtre peut être n'importe quelle expression qui donne un booléen, y compris des appels de fonction comme `len()` :
```python
words = ["a", "bee", "cat"]
short = [w for w in words if len(w) < 3]
print(short)  # ['a']
```

---

L'itérable n'a pas besoin d'être une liste : tout ce sur quoi vous pouvez boucler fonctionne, et `range()` est un favori.
C'est le moyen le plus rapide de construire une liste de nombres :
```python
squares = [n * n for n in range(4)]
print(squares)  # [0, 1, 4, 9]
```
Rappelez-vous que `range(start, stop)` exclut `stop`.

---

Les comprehensions sont excellentes pour **transformer des chaînes**.
Appelez une méthode de chaîne sur chaque élément, ou construisez une nouvelle chaîne avec une f-string :
```python
names = ["ana", "bob"]
greetings = [f"Hi {name.capitalize()}" for name in names]
print(greetings)  # ['Hi Ana', 'Hi Bob']
```

---

À l'intérieur d'une comprehension, vous pouvez utiliser toute variable définie avant elle, par exemple comme limite d'un `range()`.

---

Parfois, vous ne voulez pas supprimer des éléments, mais choisir **une valeur différente** pour certains d'entre eux.
Utilisez une expression conditionnelle `a if condition else b` comme expression, à gauche du `for` :
```python
nums = [3, -1, 4]
signs = ["+" if n > 0 else "-" for n in nums]
print(signs)  # ['+', '-', '+']
```
Notez la position : le `if-else` se place **avant** le `for` et produit toujours une valeur, tandis que le filtre `if` se place **après** le `for` et n'a pas de `else`.

---

Les deux conditions peuvent être combinées dans la même comprehension : un `if-else` pour choisir la valeur, et un filtre `if` à la fin pour ignorer certains éléments.
```python
nums = [1, 2, 3, 4]
result = ["big" if n > 2 else "small" for n in nums if n != 3]
print(result)  # ['small', 'small', 'big']
```

---

Les deux positions de `if` se confondent facilement, gardez-les donc distinctes :
```python
values = [n if n > 0 else 0 for n in nums]  # if-else avant le for : choisit une valeur, else obligatoire
positives = [n for n in nums if n > 0]      # if après le for : filtre, else interdit
```
Mettre un `else` après le filtre `if` est une erreur de syntaxe.

---

Une comprehension peut avoir **plus d'un `for`**.
Ils fonctionnent comme des boucles imbriquées : le premier `for` est la boucle externe, le second est la boucle interne.
```python
pairs = [a + b for a in ["x", "y"] for b in ["1", "2"]]
print(pairs)  # ['x1', 'x2', 'y1', 'y2']
```

---

Le `for` interne peut utiliser la variable de l'externe.
C'est la façon classique d'**aplatir** une liste de listes en une seule liste :
```python
matrix = [[1, 2], [3, 4]]
flat = [n for row in matrix for n in row]
print(flat)  # [1, 2, 3, 4]
```
La fonction `sum()` additionne ensuite tous les nombres d'une liste.

---

Vous pouvez aussi boucler sur un **dictionnaire**.
Avec `.items()`, la partie `for` déballe chaque paire en deux variables, une clé et une valeur :
```python
ages = {"ana": 31, "bob": 25}
lines = [f"{name} is {age}" for name, age in ages.items()]
print(lines)  # ['ana is 31', 'bob is 25']
```

---

La même idée fonctionne pour les dictionnaires : une **dict comprehension** utilise des accolades et une expression `key: value` :
```python
names = ["ana", "bob"]
lengths = {name: len(name) for name in names}
print(lengths)  # {'ana': 3, 'bob': 3}
```

---

Les accolades **sans** la partie `key: value` donnent une **set comprehension**.
Un set est une collection non ordonnée qui ne garde que des valeurs uniques, donc les doublons disparaissent automatiquement :
```python
nums = [1, 2, 2, 3, 3, 3]
unique = {n for n in nums}
print(unique)  # {1, 2, 3}
```

---

**Quand devriez-vous utiliser une comprehension ?**
Elle est parfaite quand le résultat est une liste (ou un dict, ou un set) et que la logique tient sur une ligne lisible : une transformation simple, un filtre optionnel.
Si vous avez besoin de plusieurs instructions, de plus de deux `for` imbriqués, ou que la ligne devient difficile à lire, écrivez plutôt une simple boucle `for` : le code sera plus long, mais plus clair.
Une comprehension remplace aussi la plupart des usages de `map()` et `filter()` avec des lambdas :
```python
doubled = list(map(lambda n: n * 2, nums))
doubled = [n * 2 for n in nums]  # same result, easier to read
```
