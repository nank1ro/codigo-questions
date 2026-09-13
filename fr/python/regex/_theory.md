Une **expression régulière** (regex) est un petit langage de motifs qui décrit du texte. Python le fournit dans le module standard `re` :
```python
import re
```

`re.search(pattern, text)` cherche le motif n'importe où dans le texte. Elle renvoie un **objet de correspondance** lorsqu'elle trouve quelque chose, et `None` sinon. `match.group()` renvoie le morceau de texte qui a correspondu :
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
```

Deux éléments du motif font le travail ici. `\d` signifie *n'importe quel chiffre* et `+` signifie *un ou plusieurs exemplaires de l'élément précédent*, donc `\d+` se lit « un ou plusieurs chiffres ». D'autres raccourcis utiles sont `\w` (une lettre, un chiffre ou un underscore) et `\s` (un espace, une tabulation ou un retour à la ligne).

Les motifs s'écrivent sous forme de **chaînes brutes**, avec un `r` devant les guillemets. Dans une chaîne Python normale, l'antislash commence une séquence d'échappement, donc `"\d"` est une erreur qui ne demande qu'à arriver et `"\n"` deviendrait un véritable retour à la ligne au lieu des deux caractères attendus par le moteur d'expressions régulières. Le préfixe `r` rend l'antislash à nouveau ordinaire, donc `r"\d"` est exactement ce que le moteur reçoit. Utilisez toujours `r"..."` pour les motifs.

---

`re.search` parcourt tout le texte, mais `re.match` n'essaie le motif qu'au **tout début** :
```python
import re

print(re.search(r"\d+", "order 42"))  # <re.Match object; span=(6, 8), match='42'>
print(re.match(r"\d+", "order 42"))   # None
print(re.match(r"\d+", "42 orders"))  # <re.Match object; span=(0, 2), match='42'>
```

Toutes deux renvoient `None` quand rien ne correspond, et un objet de correspondance est toujours truthy, donc la façon habituelle de demander « y a-t-il eu une correspondance ? » est un simple `if` :
```python
if re.search(r"\d", text):
    print("there is a digit")
```
Quand un véritable `True` ou `False` est nécessaire, comparez avec `is not None` ou enveloppez l'appel dans `bool(...)`.

---

Il existe un troisième point d'entrée, `re.fullmatch`, qui ne réussit que lorsque le motif couvre le texte **entier**, du premier au dernier caractère. C'est l'outil tout indiqué pour la validation :
```python
import re

print(bool(re.fullmatch(r"\d+", "2026")))    # True
print(bool(re.fullmatch(r"\d+", "2026!")))   # False
```

Ainsi, les trois fonctions ne diffèrent que par l'endroit où le motif est autorisé à se trouver : `re.match` au début du texte, `re.search` n'importe où dans le texte et `re.fullmatch` sur la totalité du texte.

---

Un objet de correspondance transporte plus que le texte qui a correspondu. Outre `.group()`, il offre la position de la correspondance dans la chaîne d'origine :
```python
import re

match = re.search(r"\d+", "order 42 shipped")
print(match.group())  # 42
print(match.start())  # 6
print(match.end())    # 8
print(match.span())   # (6, 8)
```
`.start()` est l'index du premier caractère correspondant, `.end()` l'index juste après le dernier et `.span()` renvoie les deux sous forme de tuple. Cela signifie que `text[match.start():match.end()]` est toujours égal à `match.group()`.

Comme `re.search` peut renvoyer `None`, lire `.group()` immédiatement lève une `AttributeError` quand rien ne correspond ; vérifiez d'abord le résultat.

---

Les parenthèses dans un motif créent un **groupe de capture** : une partie de la correspondance qui peut être relue séparément. Les groupes sont numérotés de gauche à droite, à partir de `1` :
```python
import re

match = re.search(r"(\w+)@(\w+)", "write to ada@example today")
print(match.group())   # ada@example
print(match.group(1))  # ada
print(match.group(2))  # example
print(match.groups())  # ('ada', 'example')
```
`match.group(0)` est la correspondance entière, exactement comme `match.group()`, et `match.groups()` renvoie tous les groupes sous forme de tuple. Demander un numéro de groupe qui n'existe pas lève une `IndexError`.

---

Compter les parenthèses pour trouver le groupe `3` devient vite pénible. Un groupe peut recevoir un nom avec `(?P<name>...)` puis être lu avec `match.group("name")` :
```python
import re

match = re.search(r"(?P<hour>\d\d):(?P<minute>\d\d)", "starts at 09:30")
print(match.group("hour"))    # 09
print(match.group("minute"))  # 30
print(match.groupdict())      # {'hour': '09', 'minute': '30'}
```
`match.groupdict()` renvoie tous les groupes nommés sous forme de dictionnaire. Les groupes nommés gardent aussi leur numéro, donc `match.group(1)` fonctionne toujours.

L'exemple utilise aussi un **quantificateur** avec des accolades : `\d{2}` signifie exactement deux chiffres, `\d{2,4}` signifie entre deux et quatre, et `\d{2,}` signifie deux ou plus. Ce sont la version précise de `+` (un ou plus), `*` (zéro ou plus) et `?` (zéro ou un).

---

Les crochets définissent une **classe de caractères** : un ensemble de caractères dont n'importe lequel est accepté à cette position. `[aeiou]` correspond à une voyelle, `[0-9]` à un chiffre et `[a-z]` à une lettre minuscule. Un `^` juste après le crochet ouvrant inverse le sens, donc `[^0-9]` correspond à tout ce qui n'est *pas* un chiffre.

En dehors d'une classe, `^` et `$` sont des **ancres** : `^` attache le motif au début du texte et `$` à la fin. Avec `re.fullmatch` les ancres sont implicites, c'est pourquoi la validation se lit mieux avec lui :
```python
import re

print(bool(re.fullmatch(r"[a-z]{3,8}", "ada")))  # True
print(bool(re.fullmatch(r"[a-z]{3,8}", "Ada")))  # False
```

---

`re.search` s'arrête à la première correspondance. `re.findall(pattern, text)` collecte plutôt **toutes** les correspondances et les renvoie sous forme de liste de chaînes :
```python
import re

print(re.findall(r"\d+", "a1 bb22 ccc333"))  # ['1', '22', '333']
print(re.findall(r"\d+", "no digits"))       # []
```
La liste est vide quand rien ne correspond, donc il n'y a pas de `None` à vérifier : on peut la parcourir en boucle ou la mesurer avec `len(...)` immédiatement. Notez que `findall` renvoie des chaînes simples, pas des objets de correspondance, donc les positions ne sont pas disponibles.

---

Quand la position ou les groupes de chaque correspondance sont nécessaires, `re.finditer(pattern, text)` est le bon appel : il parcourt le texte et produit un **objet de correspondance** pour chaque correspondance, un à la fois :
```python
import re

for match in re.finditer(r"\d+", "a1 bb22"):
    print(match.group(), match.start())
# 1 1
# 22 5
```
`finditer` produit un itérateur, pas une liste, donc il peut être utilisé dans une boucle `for` ou dans une compréhension. Là où `findall` ne donne que le texte, `finditer` donne tout ce qu'un objet de correspondance sait.

---

`findall` change de comportement quand le motif contient des groupes de capture. Avec exactement un groupe, il renvoie le contenu de ce groupe au lieu de la correspondance entière, et avec deux groupes ou plus il renvoie un tuple de groupes pour chaque correspondance :
```python
import re

print(re.findall(r"\d+-\d+", "10-20 30-40"))    # ['10-20', '30-40']
print(re.findall(r"(\d+)-\d+", "10-20 30-40"))  # ['10', '30']
```
Cela vaut la peine de s'en souvenir : ajouter des parenthèses à un motif juste pour grouper change silencieusement ce que `findall` renvoie. `re.finditer` ne se comporte jamais ainsi, car un objet de correspondance garde toujours à la fois la correspondance complète et les groupes.

---

`re.sub(pattern, replacement, text)` renvoie une nouvelle chaîne où chaque correspondance a été remplacée. Les chaînes sont immuables, donc le texte d'origine reste intact :
```python
import re

print(re.sub(r"\d", "#", "call 555 now"))     # call ### now
print(re.sub(r"\s+", " ", "too    many gaps"))  # too many gaps
```

Le remplacement peut faire référence aux groupes de capture avec `\1`, `\2`, ... (ou `\g<name>` pour un groupe nommé), ce qui permet de réordonner du texte en une seule ligne. Le remplacement est lui aussi une chaîne brute, pour la même raison liée à l'antislash :
```python
import re

print(re.sub(r"(\w+), (\w+)", r"\2 \1", "Lovelace, Ada"))  # Ada Lovelace
```
Un argument `count` limite le nombre de correspondances remplacées : `re.sub(r"\d", "#", "1 2 3", count=1)` donne `# 2 3`.

---

Le remplacement donné à `re.sub` peut aussi être une **fonction**. Elle est appelée une fois par correspondance, reçoit l'objet de correspondance et doit renvoyer la chaîne à mettre à sa place. C'est ainsi qu'un remplacement peut dépendre de ce qui a été trouvé :
```python
import re

def shout(match):
    return match.group().upper()

print(re.sub(r"[a-z]+", shout, "one two"))  # ONE TWO
```
La fonction est passée par son nom, sans parenthèses : écrire `shout(match)` l'appellerait immédiatement au lieu de la confier à `re.sub`.

---

`str.split` ne peut couper que sur un séparateur fixe. `re.split(pattern, text)` coupe sur tout ce que décrit le motif, ce dont l'entrée désordonnée a généralement besoin :
```python
import re

print("a, b;c".split(","))            # ['a', ' b;c']
print(re.split(r"[,;]", "a, b;c"))    # ['a', ' b', 'c']
print(re.split(r"[,;\s]+", "a, b;c")) # ['a', 'b', 'c']
```
Écrire le séparateur sous la forme `[,;\s]+` fait qu'une suite entière de virgules, points-virgules et espaces compte pour une seule coupe, au lieu de laisser des chaînes vides entre elles.

Un argument `maxsplit` s'arrête après un nombre donné de coupes, en laissant le reste du texte dans le dernier élément : `re.split(r"\s+", "a b c", maxsplit=1)` donne `['a', 'b c']`.

---

Chaque appel à `re.search` ou `re.findall` doit d'abord chercher la chaîne du motif dans un cache interne. `re.compile(pattern)` saute cette recherche et renvoie un **objet motif** qui porte les mêmes méthodes :
```python
import re

word_re = re.compile(r"[a-z]+")
print(word_re.search("ab 12").group())  # ab
print(word_re.findall("cd ef"))         # ['cd', 'ef']
print(word_re.sub("*", "ab cd"))        # * *
```
Le texte est le seul argument restant, car le motif est déjà intégré à l'objet. Compiler se révèle utile quand le même motif est utilisé de nombreuses fois, par exemple dans une boucle, et cela donne aussi au motif un nom qui explique ce qu'il trouve.

---

Les **flags** (drapeaux) modifient la façon dont un motif est appliqué. Chaque fonction de `re` les accepte comme argument `flags`, et `re.compile` les stocke dans l'objet motif :
```python
import re

print(re.search(r"cat", "A Cat", flags=re.IGNORECASE).group())  # Cat
title_re = re.compile(r"^#.*", re.MULTILINE)
```
Les deux plus utilisés sont `re.IGNORECASE`, qui fait correspondre les lettres quelle que soit leur casse, et `re.MULTILINE`, qui fait correspondre `^` et `$` au début et à la fin de chaque ligne au lieu de tout le texte. Plusieurs flags se combinent avec `|`, comme dans `re.IGNORECASE | re.MULTILINE`.

Un flag ne change que les règles de correspondance : le texte renvoyé est toujours le texte réellement présent, avec sa casse d'origine.
