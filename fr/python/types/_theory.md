Chaque valeur en Python possède un **type** qui indique de quelles données il s'agit et ce que vous pouvez en faire.
Les types de base intégrés sont :
- `int`, un nombre entier comme `42` ou `-3`
- `float`, un nombre avec une partie décimale comme `3.5`
- `str`, un morceau de texte comme `"hello"`
- `bool`, l'une des deux valeurs `True` et `False`
- `NoneType`, le type de la valeur spéciale `None`, qui signifie « aucune valeur »

La fonction intégrée `type()` renvoie le type d'une valeur. L'afficher montre le nom de la classe :
```python
print(type(42))     # <class 'int'>
print(type("hi"))   # <class 'str'>
```
Vous n'écrirez jamais `NoneType` vous-même : `type(None)` le renvoie, mais ce nom n'est pas un intégré comme les quatre autres.

---

`type()` renvoie la classe d'une valeur, vous pouvez donc la comparer à un nom de classe avec `is` :
```python
age = 30
print(type(age) is int)  # True
```
La plupart du temps, cependant, vous voulez seulement savoir **si** une valeur est d'un certain type. C'est le rôle de `isinstance(value, cls)`, qui renvoie `True` ou `False` :
```python
print(isinstance(age, int))    # True
print(isinstance(age, str))    # False
```
Le second argument peut aussi être un **tuple** de classes : le résultat est `True` si la valeur appartient à l'un d'eux :
```python
print(isinstance(2.5, (int, float)))  # True
```

---

Python est **typé dynamiquement** : le type appartient à la **valeur**, pas à la variable.
Une variable n'est qu'un nom attaché à une valeur, et vous pouvez l'attacher à tout moment à une valeur d'un autre type :
```python
x = 10
print(type(x))  # <class 'int'>
x = "ten"
print(type(x))  # <class 'str'>
```
Aucune déclaration ni conversion n'est nécessaire : l'ancienne valeur est simplement oubliée.
C'est pratique, mais cela signifie aussi que le type d'une variable n'est connu qu'à l'exécution du programme, donc un mélange de types par erreur apparaît comme une erreur à l'exécution, pas avant.

---

Vous connaissez déjà les opérateurs arithmétiques. Ce qui compte ici, c'est le **type du résultat**.
Combiner un `int` avec un `float` donne un `float`, même quand la partie décimale est nulle :
```python
print(3 + 0.5)   # 3.5
print(2 * 1.0)   # 2.0
```
La **division réelle** `/` renvoie toujours un `float`, même quand les nombres se divisent exactement :
```python
print(10 / 5)    # 2.0
print(7 / 2)     # 3.5
```
La **division entière** `//` arrondit le résultat à l'entier inférieur (ainsi `-7 // 2` vaut `-4`) et renvoie un `int` quand les deux opérandes sont des entiers. Avec le reste `%`, elle découpe une quantité en parties entières :
```python
print(7 // 2)    # 3
print(7 % 2)     # 1
```

---

Les valeurs ne changent pas de type d'elles-mêmes : pour transformer une valeur en un autre type, vous appelez le nom du type comme une fonction. Cela s'appelle une **conversion** (ou *cast*) :
```python
print(int("42"))      # 42
print(float("3.5"))   # 3.5
print(str(7))         # '7'
print(int(3.9))       # 3
```
`int()` et `float()` lisent des nombres écrits sous forme de texte, comme ceux issus de la saisie utilisateur ou de fichiers. `str()` transforme n'importe quoi en texte, pour pouvoir le joindre avec `+` à d'autres chaînes.
Notez que `int(3.9)` n'arrondit pas : il supprime la partie décimale.

---

Une conversion peut échouer. `int("abc")` ne peut pas produire de nombre, donc elle lève une `ValueError` et le programme s'arrête :
```python
int("abc")   # ValueError: invalid literal for int() with base 10: 'abc'
int("3.5")   # ValueError as well: "3.5" is not a whole number
```
Pour que le programme continue, vous pouvez intercepter l'erreur avec `try` / `except` : le code du bloc `try` s'exécute, et s'il lève l'erreur nommée, c'est le bloc `except` qui s'exécute à la place :
```python
try:
    number = int(text)
except ValueError:
    number = 0
```
Quand la conversion réussit, le bloc `except` est ignoré.

---

Chaque valeur peut être interprétée comme un booléen. `bool()` convertit une valeur en `True` ou `False`, et la même règle est appliquée quand une valeur est utilisée directement dans un `if`.
Les valeurs qui comptent comme **fausses** sont celles qui sont « vides » :
- le nombre `0` (et `0.0`)
- la chaîne vide `""`
- les collections vides comme `[]`, `{}`, `()` et `set()`
- `None`

Toute valeur non vide est **vraie**, y compris les nombres négatifs et les chaînes qui ne font que paraître vides, comme `"0"` ou `" "` :
```python
print(bool(0))     # False
print(bool(-1))    # True
print(bool(""))    # False
print(bool("0"))   # True
```
C'est pourquoi `if name:` est une façon courante de vérifier qu'une chaîne n'est pas vide.

---

`bool` est une **sous-classe** de `int` : `True` se comporte comme `1` et `False` comme `0` partout où un nombre est attendu :
```python
print(True + 1)     # 2
print(True == 1)    # True
print(False * 10)   # 0
```
`sum()` additionne les éléments d'une liste, donc sommer une liste de booléens **compte** combien valent `True` :
```python
answers = [True, False, True]
print(sum(answers))  # 2
```
À cause de cette relation de sous-classe, `isinstance(True, int)` renvoie `True`, tandis que `type(True)` reste `bool`.

---

`None` est une valeur à part qui signifie « rien ici ». C'est ce que renvoie une fonction qui n'a pas d'instruction `return`, et c'est un espace réservé courant pour une valeur encore inconnue.
Comme il n'existe qu'un seul `None`, testez-le avec `is`, pas avec `==` :
```python
result = None
if result is None:
    print("no result yet")
```
Chaque type possède un attribut `__name__` avec son nom sous forme de chaîne, ce qui est pratique pour les messages :
```python
print(type(3).__name__)     # int
print(type(None).__name__)  # NoneType
```

---

L'affichage d'un `float` montre autant de chiffres que nécessaire pour le représenter exactement, ce qui est souvent trop :
```python
print(19.999 * 3)  # 59.997
print(10 / 3)      # 3.3333333333333335
```
Dans une f-string, vous pouvez ajouter une **spécification de format** après un deux-points. `.2f` signifie « nombre à virgule fixe avec 2 décimales » :
```python
total = 10 / 3
print(f"{total:.2f}")   # 3.33
print(f"{total:.0f}")   # 3
```
La valeur est arrondie au nombre de décimales demandé, et des zéros sont ajoutés quand il le faut : `f"{2.5:.2f}"` donne `2.50`.

---

Le formatage ne change que la façon dont un nombre est affiché. Pour obtenir une **valeur** arrondie, utilisez la fonction intégrée `round()` :
```python
print(round(3.14159, 2))  # 3.14
print(round(2.71828, 1))  # 2.7
```
Avec un seul argument, `round()` arrondit au nombre entier le plus proche et renvoie un `int` ; avec un nombre de décimales, elle renvoie un `float` :
```python
print(round(3.7))     # 4
print(round(3.7, 0))  # 4.0
```
Notez que les valeurs exactement à mi-chemin entre deux nombres sont arrondies vers le nombre **pair** : `round(2.5)` vaut `2` et `round(3.5)` vaut `4`.

---

Un `float` est stocké en binaire avec un nombre fixe de bits, donc la plupart des nombres décimaux ne peuvent qu'être **approchés**. L'erreur est minime mais elle apparaît dans les calculs :
```python
print(0.1 + 0.2)   # 0.30000000000000004
```
Pour cette raison, vous ne devez pas comparer des floats avec une égalité exacte. Arrondissez les deux côtés, ou utilisez `math.isclose()`, qui vérifie que deux nombres sont égaux à une minuscule tolérance près :
```python
import math
print(round(0.1 + 0.2, 2) == 0.3)  # True
print(math.isclose(0.1 + 0.2, 0.3))  # True
```
Les entiers n'ont pas ce problème : `1 + 2 == 3` vaut toujours `True`.

---

Contrairement à beaucoup de langages, les entiers de Python n'ont **pas de taille maximale** : un `int` grandit pour contenir autant de chiffres que nécessaire, donc les grands calculs restent exacts :
```python
print(3 ** 100)  # 515377520732011331036461129765621272702107522001
```
Un `float`, en revanche, ne garde qu'environ 15 chiffres significatifs, donc la même puissance calculée en float perd en précision :
```python
print(3.0 ** 100)  # 5.153775207320113e+47
```
Comme `str()` fonctionne sur n'importe quel `int`, un moyen rapide de compter les chiffres d'un nombre est de mesurer la longueur de son texte.

---

Vous pouvez écrire le type attendu d'une variable, d'un paramètre ou d'une valeur de retour sous forme d'**indication de type** (type hint) : un deux-points après le nom pour les variables et les paramètres, une flèche `->` avant les deux-points pour la valeur de retour :
```python
count: int = 3

def greet(name: str) -> str:
    return "Hi " + name
```
Les indications de type sont de la **documentation** pour les humains et pour des outils comme les éditeurs : Python ne les vérifie **pas**. Ce code s'exécute sans se plaindre et affiche `hello` :
```python
count: int = "hello"
print(count)
```
Les indications de type rendent les types prévus clairs, mais c'est la valeur qui décide du type réel.

---

Les conversions peuvent être combinées. `int("3.7")` échoue, mais `float("3.7")` fonctionne, et `int()` d'un `float` supprime la partie décimale :
```python
number = float("3.7")   # 3.7
print(int(number))      # 3
```
`bool()` suit les règles de véracité : `bool("")` vaut `False`, et notez que `bool("False")` vaut `True`, car c'est une chaîne non vide.

---

Le texte provenant de l'extérieur est toujours une `str`, et c'est à votre programme de déterminer quel type il contient réellement.
Une approche courante consiste à essayer d'abord la conversion la plus **stricte**, puis à revenir à la suivante quand elle lève une `ValueError` :
```python
try:
    value = int(text)
except ValueError:
    value = float(text)
```
Imbriquer un second `try` dans le bloc `except` permet de revenir une fois de plus, par exemple pour garder le texte tel quel.
