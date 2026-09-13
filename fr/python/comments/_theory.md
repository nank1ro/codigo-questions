Un **commentaire** est une note écrite dans le code source pour les personnes qui le lisent. Python ignore complètement les commentaires, ils ne changent donc jamais ce que fait le programme.

La seule sorte de commentaire que Python possède est le **commentaire sur une seule ligne** : il commence par `#` et s'étend jusqu'à la fin de la ligne.
```python
# Greets the user
print("Hello")
```
Utilisez les commentaires pour expliquer à quoi sert un morceau de code, ou pourquoi il a été écrit de cette façon.

---

Un commentaire n'a pas besoin de sa propre ligne : il peut suivre le code sur la même ligne. C'est un **commentaire en ligne**, et c'est un bon endroit pour une courte note sur cette instruction précise :
```python
retries = 3  # give up after three attempts
```
Tout ce qui va de `#` jusqu'à la fin de la ligne est ignoré, tandis que le code avant lui s'exécute normalement.

Le guide de style de Python, **PEP 8**, demande un peu d'espacement ici : au moins **deux espaces** entre le code et le `#`, et **une espace** après le `#`. Un commentaire sur sa propre ligne n'a besoin que de l'espace après le `#`.

---

Comme Python supprime complètement les commentaires, ajouter ou supprimer un commentaire ne change jamais ce que fait un programme. Seul le code qui n'est **pas** commenté s'exécute.

Cela fait de `#` un moyen rapide de désactiver une ligne de code sans la supprimer. On appelle cela **mettre en commentaire** :
```python
total = 10
# total = total + 5
print(total)  # prints 10
```
La deuxième ligne est maintenant un commentaire, donc `total` reste `10`. Retirer le `#` redonne vie à la ligne.

Mettre en commentaire est pratique pendant que vous expérimentez, mais pensez à faire le ménage : du code qui reste commenté longtemps ne fait que troubler la personne qui le lira ensuite.

---

Beaucoup de langages ont une seconde sorte de commentaire, un **commentaire bloc** qui s'étend sur plusieurs lignes, comme `/* ... */`. Python n'a pas de syntaxe de ce genre : `#` est tout ce qui existe.

Quand une explication a besoin de plus d'une ligne, mettez un `#` devant chaque ligne :
```python
# Prints the welcome banner.
# Called once when the app starts.
print("Welcome!")
```
La même astuce met en commentaire plusieurs lignes de code d'un coup : un `#` par ligne. Chaque éditeur sait ajouter ou retirer ces `#` à toute une sélection avec un seul raccourci, donc c'est moins fastidieux qu'il n'y paraît.

---

Vous verrez souvent une **chaîne entre guillemets triples** utilisée comme si c'était un commentaire bloc :
```python
"""
This looks like a comment,
but it is a string.
"""
print("done")
```
Une chaîne entre `"""` et `"""` peut s'étendre sur plusieurs lignes, et une chaîne écrite seule est une instruction valide : Python la construit, n'en fait rien et la jette. Rien n'est affiché, donc le résultat ressemble à un commentaire.

Ce n'en est pas un. C'est un littéral de chaîne, donc les règles des guillemets s'appliquent toujours : un guillemet non apparié ou un `"""` égaré à l'intérieur casse le programme, tandis qu'à l'intérieur d'un commentaire `#` tout est permis. Elle peut aussi devenir une docstring par accident si elle se retrouve comme première instruction d'un fichier, d'une classe ou d'une fonction. Partout ailleurs, elle ne mène simplement nulle part : CPython jette toute l'instruction dès la compilation.

Donc, pour désactiver du code, utilisez `#`. La chaîne entre guillemets triples a son propre travail, qui commence à l'exercice suivant.

---

Quand une chaîne est la **première instruction** à l'intérieur d'une fonction, Python la traite comme la documentation de cette fonction. Elle s'appelle une **docstring** :
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"
```
Par convention, une docstring s'écrit entre guillemets doubles triples, `"""`, même quand elle tient sur une ligne, pour qu'elle puisse grandir plus tard sans changer les guillemets.

Écrivez le résumé à la troisième personne, comme si vous décriviez la fonction : « Returns... », « Adds... », « Checks... ». La docstring doit venir avant toute autre instruction dans le corps, sinon ce n'est qu'une chaîne ordinaire.

---

Une docstring n'est pas jetée : Python la stocke dans l'attribut `__doc__` de la fonction, pour que le programme puisse lire sa propre documentation pendant qu'il s'exécute :
```python
def greet(name):
    """Returns the greeting for name."""
    return "Hi, " + name + "!"

print(greet.__doc__)  # Returns the greeting for name.
```
Quand une fonction n'a pas de docstring, `__doc__` vaut `None`. C'est ce que `help(greet)` affiche, et ce qu'un éditeur montre quand vous survolez le nom.

---

Un fichier peut aussi être documenté. Une chaîne écrite comme **toute première instruction du fichier**, avant tout import ou toute définition, est la **docstring de module** : elle dit à quoi sert tout le fichier.
```python
"""Tools for working with rectangles."""

def area(width, height):
    """Returns the area of a rectangle."""
    return width * height
```
Seule la première instruction compte. Un commentaire peut se trouver au-dessus, mais n'importe quel vrai code entre les deux retransforme la chaîne en une simple chaîne ordinaire, inutile.

---

Les classes fonctionnent de la même manière : une chaîne placée comme première instruction du corps d'une classe est la docstring de cette classe, et elle est stockée dans `__doc__` :
```python
class Point:
    """A point on a grid."""

    def __init__(self, x, y):
        self.x = x
        self.y = y

print(Point.__doc__)  # A point on a grid.
```
Chaque méthode à l'intérieur de la classe peut aussi avoir sa propre docstring, lue avec `Point.__init__.__doc__`. Les trois endroits qui acceptent une docstring sont donc le haut d'un module, le haut d'une classe et le haut d'une fonction.

---

Les docstrings et les commentaires `#` se ressemblent mais répondent à des questions différentes.

Une **docstring** est destinée à celui qui **utilise** le code : ce que fait la fonction, ce qu'elle attend et ce qu'elle renvoie. Elle survit dans `__doc__`, `help()` la lit, les éditeurs l'affichent et les outils de documentation la collectent.

Un **commentaire** est destiné à celui qui **lit** le code : pourquoi cette ligne est écrite de cette façon, ce que signifie le nombre étrange, quel bug il contourne. Il n'existe que dans le fichier source et disparaît dès que le programme s'exécute.

```python
def timeout():
    """Returns the number of seconds to wait for the server."""
    # the server drops idle connections after 35 seconds
    return 30
```
Donc : la documentation de la fonction va dans la docstring, les notes sur l'implémentation vont dans les commentaires.

---

Quand une ligne ne suffit pas, une docstring prend une disposition fixe, décrite dans la **PEP 257** : un résumé d'une ligne, une ligne vide, puis les détails, et le `"""` de fermeture sur une ligne à part.
```python
def to_seconds(minutes):
    """Returns the number of seconds in the given minutes.

    minutes is a whole number and is never negative.
    """
    return minutes * 60
```
La ligne vide compte : les outils affichent la première ligne seule, comme une courte description, et gardent le reste pour celui qui veut en lire plus.

---

La docstring doit être la **première ligne du corps**, au-dessus de toute autre instruction. Une chaîne écrite après le `return`, ou n'importe où ailleurs dans le corps, n'est qu'une chaîne : `__doc__` reste `None` et aucun outil ne l'affichera jamais.

---

Certains commentaires suivent une convention que les éditeurs comprennent. Les **marqueurs** les plus courants sont :
- `# TODO: ...` signale quelque chose qui doit encore être écrit
- `# FIXME: ...` signale du code que l'on sait faux et qui doit être corrigé

```python
limit = 10
# TODO: read the limit from the settings
```
Pour Python, ce sont des commentaires ordinaires ; les éditeurs les rassemblent dans un panneau dédié, donc le travail en attente est facile à trouver. Un `TODO` se trouve généralement à côté d'un espace réservé qui garde le programme en marche jusqu'à ce que le vrai code soit écrit.

Quand vous terminez le travail, remplacez l'espace réservé et supprimez le marqueur dans le même changement, pour que le commentaire ne mente jamais sur l'état du code.

---

Un commentaire placé au-dessus d'une fonction pour dire ce que fait la fonction est au mauvais endroit. La docstring est l'endroit prévu pour cela : elle est attachée à la fonction, `help()` la trouve et les éditeurs l'affichent, tandis qu'un commentaire `#` au-dessus du `def` reste invisible pour tous.

```python
# adds a and b
def add(a, b):
    return a + b
```
Déplacer la même phrase d'une ligne vers le bas, entre guillemets triples, en fait une vraie documentation :
```python
def add(a, b):
    """Returns the sum of a and b."""
    return a + b
```

---

Python ne cherche le `#` que dans le code, jamais à l'intérieur d'une **chaîne**. Entre guillemets, `#` est un caractère ordinaire :
```python
print("black is #000000")  # a hex colour
```
Le premier `#` fait partie du texte, le second commence un vrai commentaire. Il en va de même pour `"""` à l'intérieur d'un commentaire `#` : là, ce ne sont que trois caractères guillemets, et cela ne commence rien.

---

Un bon commentaire explique **pourquoi** le code fait quelque chose, pas **ce** qu'il fait. Le code montre déjà ce qui se passe ; le répéter avec des mots ajoute du bruit et devient obsolète dès que le code change :
```python
# set timeout to 30
timeout = 30
```
La raison derrière le nombre est ce qu'un lecteur ne peut pas deviner :
```python
# the server drops idle connections after 35 seconds, so stop earlier
timeout = 30
```
Si un commentaire ne fait que répéter la ligne en dessous, supprimez-le ou remplacez-le par la raison. Les meilleurs commentaires sont ceux qui disent quelque chose que le code ne peut pas dire.
