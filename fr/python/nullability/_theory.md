Parfois, une variable n'a **aucune valeur** à stocker : un utilisateur qui ne s'est pas connecté, une recherche qui n'a rien trouvé, un paramètre qui n'a jamais été choisi. Python représente cela avec la valeur spéciale `None`.
`None` est une valeur comme les autres : vous pouvez l'assigner, l'afficher et la passer à des fonctions. Son type est `NoneType`, et il existe exactement **un** `None` dans tout le programme, donc chaque `None` que vous écrivez fait référence au même objet :
```python
winner = None
print(winner)                 # None
print(type(winner).__name__)  # NoneType
print(winner is None)         # True
```
`None` n'est pas `0`, ni une chaîne vide et ni `False` : c'est une valeur à part qui signifie « rien ici ».

---

Chaque appel de fonction produit une valeur, même lorsque la fonction ne semble rien renvoyer. Une fonction **sans** instruction `return`, ou avec un `return` seul, renvoie `None` :
```python
def say_hello():
    print("hello")

result = say_hello()
print(result)  # None
```
C'est pourquoi appeler `print(my_list.append(3))` affiche `None` : `append` modifie la liste en place et ne renvoie rien.
Une fonction qui effectue seulement une action (afficher, sauvegarder, modifier une liste) renvoie généralement `None`, tandis qu'une fonction qui calcule quelque chose doit le `return` explicitement.

---

Pour vérifier si une variable contient `None`, utilisez `is` et `is not`, jamais `==` :
```python
if user is None:
    print("nobody logged in")
if user is not None:
    print("welcome")
```
`==` demande « ces valeurs sont-elles *égales* ? », et n'importe quelle classe peut répondre à cette question à sa manière en définissant la méthode `__eq__`. `is` demande « sont-ils le *même objet* ? », et rien ne peut changer la réponse.
Puisqu'il n'existe qu'un seul `None`, `is None` est toujours correct et légèrement plus rapide, tandis que `== None` peut donner une réponse surprenante pour les objets avec un `__eq__` personnalisé.

---

`None` compte comme **faux** dans une condition, donc `if not value:` est `True` quand `value` est `None`. Il est tentant de l'utiliser comme test de `None`, mais le même test est aussi `True` pour `0`, `""`, `[]` et toutes les autres valeurs vides :
```python
count = 0
if not count:
    print("missing?")   # printed, but 0 is a real value!
```
Quand « aucune valeur » et « valeur vide » doivent être traitées différemment, vérifiez d'abord `is None`, puis la véracité :
```python
if count is None:
    print("no count yet")
elif not count:
    print("count is zero")
```
Utilisez `if not value:` seulement quand vous voulez vraiment traiter `None` et les valeurs vides de la même manière.

---

Un paramètre peut avoir une **valeur par défaut**, utilisée quand l'appelant omet l'argument. `None` est la valeur par défaut habituelle pour « non fourni » :
```python
def greet(name=None):
    if name is None:
        name = "stranger"
    print("Hello, " + name)

greet()       # Hello, stranger
greet("Ada")  # Hello, Ada
```
Cela compte pour les listes et les dictionnaires. Une valeur par défaut est évaluée **une seule fois**, quand la fonction est définie, donc `def add(item, items=[])` partage la même liste entre tous les appels qui omettent `items`, et les éléments s'accumulent. La solution est de mettre `None` par défaut et de créer une nouvelle liste dans la fonction :
```python
def add(item, items=None):
    if items is None:
        items = []
    items.append(item)
    return items
```

---

Lire une clé absente d'un dictionnaire avec `[]` lève une `KeyError`. La méthode `get` est l'alternative sûre : elle renvoie la valeur quand la clé existe et `None` quand elle n'existe pas :
```python
ages = {"Ada": 36}
print(ages.get("Ada"))    # 36
print(ages.get("Grace"))  # None
```
`get` accepte un second argument, la valeur à renvoyer **à la place de** `None` quand la clé est absente :
```python
print(ages.get("Grace", 0))  # 0
```
C'est ainsi que `None` apparaît le plus souvent dans le code du quotidien : une recherche qui n'a rien trouvé.

---

Une fonction qui renvoie un nombre **ou** `None` devrait le dire dans sa signature. Une **indication de type** (type hint) est une annotation qui documente le type attendu : `name: str` pour un paramètre et `-> int` pour la valeur de retour. Python n'impose pas les indications de type, mais les éditeurs et les lecteurs s'y fient :
```python
def parse_age(text: str) -> int | None:
    if text.isdigit():
        return int(text)
    return None
```
`int | None` se lit « un `int` ou `None` ». L'ancienne écriture `Optional[int]` du module `typing` signifie exactement la même chose, et vous la rencontrerez encore dans du code existant.
Chaque fois que vous voyez `| None` dans une signature, pensez à vérifier le résultat avant de l'utiliser.

---

Les fonctions qui peuvent recevoir `None` commencent souvent par une **garde** : un `if` qui renvoie tôt quand il n'y a rien à traiter. Le reste de la fonction peut alors supposer que la valeur est présente, sans tout imbriquer dans un `else` :
```python
def shout(text):
    if text is None:
        return None
    return text.upper() + "!"
```
Les gardes viennent en premier, dans l'ordre où les vérifications doivent se produire : vous ne pouvez pas appeler `text.split()` avant de savoir que `text` n'est pas `None`.

---

L'opérateur `or` ne renvoie pas `True` ou `False` : il renvoie son opérande **gauche** quand celui-ci est vrai, et son opérande **droit** sinon. Cela donne un moyen en une ligne de fournir une valeur de repli :
```python
name = None
print(name or "anonymous")  # anonymous
name = "Ada"
print(name or "anonymous")  # Ada
```
Le piège est que `or` regarde la véracité, pas `None` : `0`, `""` et `[]` sont aussi remplacés par la valeur de repli. Utilisez `x or fallback` seulement quand chaque valeur vide doit devenir la valeur de repli aussi.

---

Quand `0` ou `""` doivent être conservés et que seul `None` doit être remplacé, la valeur de repli a besoin d'une vérification explicite `is None`. La forme compacte est l'**expression conditionnelle**, `a if condition else b`, qui vaut `a` quand la condition est vraie et `b` sinon :
```python
timeout = 0
seconds = timeout if timeout is not None else 30
print(seconds)  # 0, not 30
```

---

Une liste peut contenir `None` à côté de vraies valeurs, par exemple des relevés qui ont échoué ou des réponses qui ont été ignorées. La plupart des opérations ne l'acceptent pas : `sum([8, None])` lève une `TypeError`.
Filtrez les valeurs `None` avec une liste en compréhension dont la condition est `is not None` :
```python
readings = [3, None, 5]
valid = [r for r in readings if r is not None]
print(valid)  # [3, 5]
```
Utiliser `if r` à la place supprimerait aussi chaque `0`, donc soyez explicite quand zéro est un relevé valide.

---

Une recherche suivie d'une vérification de `None` nécessite généralement deux lignes : une pour stocker le résultat, une pour le tester. L'opérateur d'**expression d'affectation** `:=`, surnommé le *walrus*, affecte une valeur **à l'intérieur** d'une expression, donc les deux étapes tiennent dans le `if` :
```python
ages = {"Ada": 36}
if (age := ages.get("Ada")) is not None:
    print(age + 1)  # 37
```
Les parenthèses sont obligatoires : sans elles, `:=` essaierait d'affecter toute la comparaison. Après le `if`, `age` reste disponible comme n'importe quelle autre variable.

---

Tous les « introuvable » ne sont pas signalés avec `None`. Certaines fonctions plus anciennes renvoient à la place une valeur **sentinelle**, une valeur normale à laquelle on donne une signification spéciale. La méthode de chaîne `find` renvoie l'indice d'une sous-chaîne, ou `-1` quand elle est absente :
```python
print("banana".find("n"))  # 2
print("banana".find("x"))  # -1
```
La fonction `re.match(pattern, text)` du module `re` vérifie si `text` commence par `pattern`, et renvoie un objet match, ou `None` quand il n'y a pas de correspondance.
`None` est la convention la plus sûre : `-1` est un indice valide, donc `text[text.find("x")]` renvoie silencieusement le dernier caractère au lieu d'échouer, tandis qu'utiliser `None` comme indice lève une erreur immédiatement.

---

`None` ne peut pas être ordonné : `None < 1` lève une `TypeError`, parce que Python n'a aucune idée de savoir si « rien » est plus petit ou plus grand qu'un nombre.
Cela compte quand `None` est utilisé comme valeur de départ d'une recherche, comme « la meilleure valeur vue jusqu'ici, s'il y en a une ». Chaque comparaison doit être protégée par une vérification `is None` placée **en premier**, pour que `or` court-circuite et que la comparaison soit ignorée quand il n'y a encore rien à comparer :
```python
if best is None or value > best:
    best = value
```
Écrite dans l'autre sens, `value > best or best is None` comparerait avec `None` à la première itération et planterait.
