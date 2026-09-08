Un **set** est une collection d'éléments **uniques** : la même valeur ne peut apparaître qu'une seule fois, peu importe le nombre de fois où vous l'écrivez.
Un set est aussi **non ordonné** : il n'y a pas de premier ni de dernier élément, vous ne pouvez donc pas lire un élément par index.
Les sets sont idéaux quand seule *quelle* valeur est présente vous intéresse, pas combien de fois ni à quelle position.
Vous créez un set en écrivant ses éléments entre accolades `{...}` :
```python
colors = {"red", "blue", "red"}
print(len(colors))  # 2
```
Le `"red"` en double est supprimé, donc `len()` ne compte que les éléments distincts.

---

La fonction native `set()` construit un set à partir de n'importe quelle collection, par exemple une liste ou une chaîne.
Comme un set ne garde chaque valeur qu'une seule fois, c'est la méthode classique pour **supprimer les doublons** :
```python
nums = [1, 2, 2, 3]
unique = set(nums)
print(len(unique))  # 3
```
Pour vérifier si une valeur est présente, utilisez l'opérateur `in`, qui renvoie `True` ou `False` :
```python
print(2 in unique)  # True
print(9 in unique)  # False
```
Les vérifications d'appartenance sur un set sont très rapides, même avec des milliers d'éléments.

---

Il y a un piège lors de la création d'un **set vide**.
Les accolades sont aussi la syntaxe des dictionnaires, donc `{}` crée un **dictionnaire** vide, pas un set :
```python
empty = {}
print(type(empty))  # <class 'dict'>
```
Pour obtenir un set vide, vous devez appeler `set()` sans argument :
```python
empty = set()
print(type(empty))  # <class 'set'>
print(len(empty))   # 0
```

---

Les sets sont **mutables** : vous pouvez ajouter et retirer des éléments après leur création.
`add(value)` insère une valeur ; ajouter une valeur déjà présente ne change rien :
```python
letters = {"a", "b"}
letters.add("c")
letters.add("a")
print(len(letters))  # 3
```
Il existe deux façons de retirer un élément :
- `remove(value)` le supprime, mais lève une `KeyError` si la valeur n'est pas dans le set
- `discard(value)` le supprime si présent et ne fait **rien** sinon, sans erreur
```python
letters.remove("a")
letters.discard("z")  # "z" n'y est pas, mais pas d'erreur
letters.remove("z")   # KeyError: 'z'
```

---

`pop()` retire **un élément arbitraire** du set et le renvoie.
Comme un set n'a pas d'ordre, vous ne pouvez pas choisir quel élément est retiré ; appeler `pop()` sur un set vide lève une `KeyError` :
```python
tickets = {101, 102, 103}
picked = tickets.pop()
print(len(tickets))  # 2
```
`clear()` retire **tous** les éléments, laissant un set vide :
```python
tickets.clear()
print(len(tickets))  # 0
```

---

Vous pouvez parcourir un set avec `for`, exactement comme une liste :
```python
for color in {"red", "blue"}:
    print(color)
```
Comme un set n'est pas ordonné, les éléments peuvent sortir dans **n'importe quel ordre**, et cet ordre peut même changer d'une exécution à l'autre.
Quand vous avez besoin d'un ordre prévisible, passez le set à `sorted()`, qui renvoie une **liste** triée de ses éléments :
```python
for color in sorted({"red", "blue"}):
    print(color)  # blue, then red
```

---

L'**union** de deux sets est un nouveau set avec les éléments des **deux**, sans doublons.
Utilisez l'opérateur `|` ou la méthode `union()` :
```python
a = {1, 2}
b = {2, 3}
print(a | b)        # {1, 2, 3}
print(a.union(b))   # {1, 2, 3}
```
Ni `a` ni `b` n'est modifié : les opérations sur les sets renvoient toujours un nouveau set.

---

L'**intersection** de deux sets contient seulement les éléments présents dans **les deux**.
Utilisez l'opérateur `&` ou la méthode `intersection()` :
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a & b)               # {2, 3}
print(a.intersection(b))   # {2, 3}
```
Si les sets n'ont rien en commun, le résultat est un set vide.

---

La **différence** `a - b` contient les éléments de `a` qui ne sont **pas** dans `b`.
L'ordre compte : `a - b` et `b - a` sont généralement différents :
```python
a = {1, 2, 3}
b = {2, 3, 4}
print(a - b)  # {1}
print(b - a)  # {4}
```
La **différence symétrique** `a ^ b` contient les éléments présents dans **exactement un** des deux sets :
```python
print(a ^ b)  # {1, 4}
```
Les formes méthode sont `difference()` et `symmetric_difference()`.

---

Les opérateurs et les méthodes ne sont pas parfaitement équivalents.
Les opérateurs `|`, `&`, `-` et `^` fonctionnent uniquement quand **les deux** opérandes sont des sets.
Les méthodes `union()`, `intersection()`, `difference()` et `symmetric_difference()` acceptent **n'importe quel itérable**, comme une liste ou une chaîne :
```python
a = {1, 2}
print(a.union([2, 3]))  # {1, 2, 3}
print(a | [2, 3])       # TypeError: unsupported operand type(s) for |: 'set' and 'list'
```

---

Les sets peuvent aussi être **comparés** entre eux.
`a.issubset(b)`, ou `a <= b`, vaut `True` quand chaque élément de `a` est aussi dans `b`.
`a.issuperset(b)`, ou `a >= b`, vaut `True` quand `a` contient chaque élément de `b`.
`a.isdisjoint(b)` vaut `True` quand les deux sets n'ont **aucun** élément en commun :
```python
small = {1, 2}
big = {1, 2, 3}
print(small <= big)              # True
print(big.issuperset(small))     # True
print(small.isdisjoint({8, 9}))  # True
```

---

Un set ne peut contenir que des éléments **hachables**, c'est-à-dire des valeurs qui ne peuvent pas changer : des nombres, des chaînes, `True`/`False` et des **tuples**.
Essayer d'ajouter une liste, un dictionnaire ou un autre set lève une `TypeError` :
```python
points = set()
points.add((1, 2))  # ok, un tuple
points.add([1, 2])  # TypeError: unhashable type: 'list'
```
Les sets de tuples sont pratiques pour garder trace de paires uniques, comme des coordonnées ou des enregistrements (nom, âge) :
```python
visits = [(1, 2), (1, 2), (3, 4)]
print(len(set(visits)))  # 2
```

---

Un **frozenset** est un set **immuable** : une fois créé, vous ne pouvez pas ajouter ou retirer d'éléments.
Créez-le avec `frozenset()` à partir de n'importe quelle collection :
```python
days = frozenset(["sat", "sun"])
print("sat" in days)  # True
days.add("mon")       # AttributeError: 'frozenset' object has no attribute 'add'
```
Afficher un frozenset montre son type autour des éléments, comme `frozenset({'sat', 'sun'})`.
Comme il ne peut pas changer, un frozenset est hachable : contrairement à un set normal, il peut être un élément d'un autre set ou une clé de dictionnaire.
Toutes les opérations en lecture seule (`in`, `len()`, `|`, `&`, `-`, `^`, comparaisons) fonctionnent normalement.

---

Une **set comprehension** construit un set en une seule expression, avec la même syntaxe qu'une list comprehension mais avec des accolades :
```python
nums = [1, 2, 2, 3]
squares = {n * n for n in nums}
print(squares)  # {1, 4, 9}
```
Un `if` optionnel filtre les éléments, et les doublons produits par l'expression sont automatiquement supprimés :
```python
evens = {n for n in range(10) if n % 2 == 0}
print(evens)  # {0, 2, 4, 6, 8}
```

---

Les opérations sur les sets peuvent aussi modifier un set **sur place** au lieu d'en renvoyer un nouveau.
`update(iterable)` ajoute chaque élément de n'importe quelle collection, comme `add()` mais pour plusieurs valeurs à la fois :
```python
inventory = {"sword"}
inventory.update(["potion", "map"])
print(len(inventory))  # 3
```
Les opérateurs augmentés fonctionnent aussi sur place : `|=` ajoute les éléments d'un autre set, `&=` ne garde que les éléments communs, `-=` retire les éléments d'un autre set :
```python
inventory -= {"map"}
print(sorted(inventory))  # ['potion', 'sword']
```

---

Deux sets sont **égaux** quand ils contiennent les mêmes éléments, quel que soit l'ordre dans lequel ils ont été écrits :
```python
print({1, 2, 3} == {3, 1, 2})  # True
```
Comparer la longueur d'une collection avec la longueur de son set est un moyen rapide de détecter les doublons : si le set est **plus petit**, une valeur est apparue plus d'une fois :
```python
emails = ["a@x.com", "b@x.com", "a@x.com"]
print(len(set(emails)) < len(emails))  # True
```
La méthode de liste `count(value)` indique combien de fois une valeur apparaît, ce qui aide à trouver *quelles* valeurs sont dupliquées.
