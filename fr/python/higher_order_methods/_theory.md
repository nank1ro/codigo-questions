En Python une fonction est une **valeur**, tout comme un nombre ou une chaîne. Vous pouvez la stocker dans une variable, la mettre dans une liste ou la passer à une autre fonction. Seules les parenthèses l'appellent : `shout` est la fonction elle-même, `shout("hi")` est son résultat :
```python
def shout(text):
    return text.upper() + "!"

say = shout
print(say("hi"))  # HI!
```
Une fonction qui reçoit une autre fonction en paramètre, ou qui en renvoie une, est appelée une **fonction d'ordre supérieur**. À l'intérieur, le paramètre est appelé avec des parenthèses comme n'importe quelle autre fonction :
```python
def apply(func, value):
    return func(value)

print(apply(shout, "bye"))  # BYE!
print(apply(len, "bye"))    # 3
```

---

Passer une fonction en argument laisse à l'appelant le choix de **quoi** faire, tandis que la fonction d'ordre supérieur décide **combien de fois** ou **sur quoi**. Le paramètre fonction peut être appelé autant de fois que nécessaire, et son résultat peut lui être redonné en entrée :
```python
def repeat(func, value, times):
    for _ in range(times):
        value = func(value)
    return value

def add_one(n):
    return n + 1

print(repeat(add_one, 0, 3))  # 3
```
N'importe quel appelable convient : une fonction `def`, une fonction native comme `len` ou une `lambda`.

---

La fonction native `map(func, iterable)` appelle `func` sur chaque élément et produit les résultats, un pour chaque élément. Elle renvoie un *map object* paresseux, il faut donc l'envelopper dans `list()` pour voir les valeurs :
```python
numbers = [1, 2, 3]
print(list(map(lambda n: n * 10, numbers)))  # [10, 20, 30]
```
N'importe quel appelable peut être passé, pas seulement une lambda : une fonction native comme `len`, ou une méthode prise depuis sa classe, comme `str.upper`, qui prend la chaîne comme premier argument :
```python
names = ["ada", "linus"]
print(list(map(str.upper, names)))  # ['ADA', 'LINUS']
print(list(map(len, names)))        # [3, 5]
```

---

La fonction native `filter(func, iterable)` ne garde que les éléments pour lesquels `func` renvoie une valeur vraie. Comme `map`, elle renvoie un objet paresseux qui doit être transformé en liste :
```python
numbers = [4, -2, 7, 0]
print(list(filter(lambda n: n > 0, numbers)))  # [4, 7]
```
La fonction passée à `filter` est appelée un **prédicat** : elle prend un élément et répond à une question par oui ou non à son sujet. Passer `None` au lieu d'une fonction garde les éléments qui sont vrais par eux-mêmes, en écartant `0`, `""` et `None`.

---

`sorted(iterable, key=func)` ordonne les éléments selon la valeur que `func` renvoie pour chacun d'eux, sans modifier les éléments eux-mêmes. Ajoutez `reverse=True` pour obtenir les plus grands en premier :
```python
words = ["kiwi", "fig", "banana"]
print(sorted(words, key=len))                # ['fig', 'kiwi', 'banana']
print(sorted(words, key=len, reverse=True))  # ['banana', 'kiwi', 'fig']
```
Le tri est **stable** : les éléments dont les clés sont égales conservent leur ordre d'origine. La fonction `key` est appelée une fois par élément et ses résultats servent uniquement à comparer, donc la sortie contient toujours les mots d'origine, pas leurs longueurs.

---

La fonction `key` peut choisir **n'importe quelle partie** d'un élément. Pour une liste de tuples, `lambda s: s[1]` trie selon le deuxième élément de chaque tuple ; pour une liste de dictionnaires, `lambda d: d["age"]` trie selon une valeur :
```python
pairs = [("b", 2), ("a", 3), ("c", 1)]
print(sorted(pairs, key=lambda p: p[1]))  # [('c', 1), ('b', 2), ('a', 3)]
```
`min` et `max` acceptent le même paramètre `key`, donc `max(pairs, key=lambda p: p[1])` renvoie `('a', 3)` : le tuple entier, pas seulement le nombre.

---

Une fonction peut aussi **renvoyer** une fonction. Définissez une fonction interne avec `def` et renvoyez-la sans l'appeler :
```python
def make_greeter(greeting):
    def greet(name):
        return greeting + ", " + name
    return greet

hello = make_greeter("Hello")
print(hello("Ada"))  # Hello, Ada
```
La fonction interne continue d'utiliser `greeting` même après la fin de `make_greeter` : elle **se souvient** des variables de la portée où elle a été créée. Une telle fonction est appelée une **fermeture** (closure). Chaque appel à `make_greeter` crée une nouvelle fermeture indépendante avec son propre `greeting`.

---

Une fermeture peut lire les variables de la fonction englobante, mais affecter une valeur à l'une d'elles crée au contraire une **nouvelle variable locale**. Pour mettre à jour la variable externe, déclarez-la avec `nonlocal` dans la fonction interne :
```python
def make_counter():
    count = 0
    def increment():
        nonlocal count
        count += 1
        return count
    return increment
```
`global` chercherait `count` au niveau du module, où il n'existe pas. Avec `nonlocal`, chaque appel à la fonction renvoyée met à jour le même `count`, donc la fermeture conserve un état entre les appels, comme un petit objet.

---

`reduce(func, iterable, initial)` du module `functools` réduit une séquence en une **valeur unique**. Elle appelle `func` avec le résultat obtenu jusque-là et l'élément suivant, en partant de `initial` :
```python
from functools import reduce

total = reduce(lambda acc, n: acc + n, [1, 2, 3], 0)
print(total)  # 6
```
Les étapes sont `0 + 1`, puis `1 + 2`, puis `3 + 3`. Quand `initial` est omis, le premier élément sert de valeur de départ, mais une séquence vide lève alors une `TypeError` ; donnez donc une valeur initiale dès que la séquence peut être vide.

---

`partial(func, *fixed)` de `functools` construit une nouvelle fonction dont certains arguments sont **déjà fournis**. Appeler le résultat fournit les arguments restants :
```python
from functools import partial

def power(base, exponent):
    return base ** exponent

square = partial(power, exponent=2)
print(square(5))  # 25
```
Les arguments positionnels donnés à `partial` remplissent les premiers paramètres ; les arguments nommés fixent un paramètre par son nom et peuvent encore être remplacés au moment de l'appel. Un partial est un simple appelable, il peut donc être passé à `map`, `sorted` ou à toute autre fonction d'ordre supérieur.

---

`partial` est pratique avec les fonctions natives qui acceptent des options. `int(text, base=16)` analyse une chaîne hexadécimale ; fixer la base donne un convertisseur à un seul argument qui convient à `map` :
```python
from functools import partial

hex_to_int = partial(int, base=16)
print(hex_to_int("ff"))                      # 255
print(list(map(hex_to_int, ["a", "10"])))    # [10, 16]
```
L'objet partial se souvient de ce qu'il enveloppe : `hex_to_int.func` est `int`, et `hex_to_int.keywords` est `{'base': 16}`.

---

Un **décorateur** est une fonction d'ordre supérieur qui prend une fonction et en renvoie une nouvelle qui l'enveloppe, généralement pour ajouter un comportement avant ou après l'appel d'origine :
```python
def announce(func):
    def wrapper(name):
        print("calling " + func.__name__)
        return func(name)
    return wrapper
```
`func.__name__` est le nom sous lequel la fonction a été définie. Appliquer le décorateur n'est qu'un appel : `greet = announce(greet)`. La syntaxe `@` placée sur la ligne **au-dessus** d'un `def` fait exactement cela :
```python
@announce
def greet(name):
    return "Hello, " + name
```
Le décorateur doit être défini avant d'être utilisé avec `@`, car le remplacement a lieu dès que le `def` s'exécute.

---

Un décorateur qui n'accepte qu'un seul argument est peu utile. Pour envelopper **n'importe quelle** fonction, le wrapper collecte tous les arguments positionnels dans `*args` et tous les arguments nommés dans `**kwargs`, et les transmet sans les modifier :
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
Dans le wrapper, `args` est un tuple et `kwargs` un dictionnaire ; le `*` et le `**` dans l'appel les redéploient en arguments séparés.

---

`any(iterable)` renvoie `True` si **au moins un** élément est vrai, `all(iterable)` si **tous** le sont. Ils se combinent naturellement avec une **expression génératrice** : une compréhension de liste écrite sans les crochets, qui produit les valeurs une à une au lieu de construire une liste :
```python
ages = [21, 34, 17]
print(any(age >= 18 for age in ages))  # True
print(all(age >= 18 for age in ages))  # False
```
Comme les valeurs sont produites paresseusement, `any` s'arrête au premier `True` et `all` au premier `False`, sans évaluer le reste. `sum` accepte aussi une expression génératrice : `sum(1 for age in ages if age >= 18)` compte les adultes.
