La prise de décision est nécessaire lorsque nous voulons exécuter du code uniquement si une certaine condition est remplie.
Supposons que nous voulions jouer dehors uniquement si le temps est beau.
En programmation, nous pouvons enregistrer une variable booléenne `nice_weather` et effectuer l'action de jouer dehors `if` cette variable est `True`, comme :
```python
nice_weather = True
if (nice_weather):
    # jouer dehors
```

---

Continuons avec l'exemple précédent.
```python
nice_weather = True
if (nice_weather):
    # jouer dehors
```
Nous avons vu que la déclaration `if` exécute le bloc de code uniquement si la condition est `True`.
Une autre chose importante à considérer est représentée par les **deux-points** `:` et l'**indentation**, qui indiquent le début d'un bloc de code.
L'indentation fait référence aux espaces au début d'une ligne de code.
Alors que dans d'autres langages de programmation l'indentation du code n'est que pour la lisibilité, l'indentation en Python est essentielle.
Vous pouvez utiliser votre nombre préféré d'espaces (2, 4, 6, 8), en notant que le préféré est 4.
Ici, dans l'application, nous vous suggérons d'utiliser la touche **TAB** pour indenter votre ligne de codes

---

Nous avons vu comment exécuter un bloc de code si une condition se produit, maintenant voyons comment exécuter un autre bloc de code si la première condition échoue.
Nous allons jouer dehors si le temps est beau ; sinon, nous restons à la maison.
En Python, nous pouvons utiliser la déclaration `else`, comme :
```python
nice_weather = True
if (nice_weather):
    # jouer dehors
else:
    # rester à la maison
```

---

Supposons que nous ayons une autre condition à vérifier, comme dans cet exemple :
```python
num = 3
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
else:
    print("do something else")
```
et la sortie de ce code est `the number is 3`.
Avant tout, vérifions si le nombre est égal à 2, c'est faux.
Passons donc à la deuxième déclaration et vérifions si `num` est égal à 3, étant vrai nous exécutons le bloc de code suivant en imprimant `the number is 3`

---

Nous pouvons ajouter autant de déclarations `elif` que nous le voulons, il n'y a pas de limites
```python
num = 4
if (num == 2):
    print("the number is 2")
elif (num == 3):
    print("the number is 3")
elif (num == 4):
    print("the number is 4")
elif (num == 5):
    print("the number is 5")
elif (num == 6):
    print("the number is 6")
```
et la sortie de ce code est `the number is 4`.

---

Nous pouvons également imbriquer une déclaration conditionnelle (`if`, `elif` ou `else`) à l'intérieur d'une autre déclaration conditionnelle, pour créer une structure plus complexe.
```python
num = 4
if (num < 3):
    print("the number is lower than 3")
else:
    if (num == 3):
        print("the number is 3")
    elif (num == 4):
        print("the number is 4")
    else:
        print("the number is greather than 4")
```
et la sortie de ce code est `the number is 4`.

---

Chaque déclaration conditionnelle a besoin du mot-clé `if` pour l'introduire. C'est ce qui indique à Python que le bloc ci-dessous ne s'exécute que si une condition est remplie.

---

Une condition n'a pas besoin d'être une comparaison — une valeur booléenne comme `True` seule fonctionne aussi, et le bloc s'exécute chaque fois que cette valeur est `True`.

---

La même déclaration peut être amenée à ignorer son bloc simplement en changeant la condition : chaque fois qu'elle vaut `False`, Python saute directement le code indenté.

---

Une ligne `if` en Python se compose de trois parties : le mot-clé `if`, une condition, et les deux-points qui terminent la ligne. Tout ce qui est indenté après ces deux-points constitue le bloc.

---

Puisque la condition ici est `True`, Python exécute la ligne indentée en dessous et affiche `Hello!`.

---

Une condition `False` signifie que Python n'entre jamais dans le bloc indenté, donc rien n'est affiché du tout.

---

La valeur qui décide si un bloc s'exécute s'appelle une condition, et elle doit toujours s'évaluer en un booléen, `True` ou `False`.

---

Le bloc sous un `if` ne peut jamais être vide : Python lève une `IndentationError` si aucune ligne indentée ne suit les deux-points. `pass` est le substitut habituel lorsqu'il n'y a encore rien à exécuter.

---

Les deux-points appartiennent à la ligne `if` et non au bloc : ils marquent la fin de la condition et annoncent que les lignes indentées en dessous font partie de la déclaration.

---

Quand une condition est `False`, Python ignore tout le bloc indenté et poursuit à la prochaine ligne qui n'est pas indentée sous le `if`.

---

Python n'exige pas de parenthèses autour d'une condition — `if True:` est une déclaration complète à elle seule. Les parenthèses ici ne sont qu'un regroupement ordinaire, du même type que celui utilisé en arithmétique, et elles laissent la valeur inchangée.

---

Un bloc de code peut contenir plus d'une ligne, et les lignes s'exécutent dans l'ordre où elles sont écrites — une instruction ajoutée au-dessus d'une instruction existante s'affiche en premier.

---

Une variable booléenne peut être utilisée comme condition à elle seule — il n'est pas nécessaire de la comparer d'abord à `True` ou `False`.

---

Quand la condition est une variable, `if` lit ce que cette variable contient à cet instant. Modifier l'affectation ci-dessus suffit à désactiver le bloc, sans toucher du tout à la ligne `if`.

---

Les lignes indentées qui appartiennent à une déclaration conditionnelle sont appelées son bloc de code — c'est l'indentation qui les marque comme en faisant partie.

---

Une ligne qui se trouve en dehors de l'indentation du `if` s'exécute quelle qu'ait été la condition, puisqu'elle n'a jamais fait partie de ce bloc.

---

Un bloc de code ne se limite pas à une seule ligne — il peut être aussi court ou aussi long que la logique l'exige, tant que chaque ligne reste indentée de façon cohérente.

---

Avec `online` défini sur `False`, la condition n'est jamais remplie, donc le bloc est ignoré et rien n'est affiché.

---

Seul le `print` indenté juste après le `if` appartient à son bloc ; une ligne écrite avec la même indentation que le `if` lui-même n'en fait pas partie.

---

Une ligne placée après le bloc `if` mais sans indentation supplémentaire n'en fait plus partie — elle s'exécute à chaque fois, quelle qu'ait été la condition.

---

Un bloc peut contenir n'importe quel nombre d'instructions. Elles s'exécutent de haut en bas, et chacune doit être indentée au même niveau que les autres.

---

Affecter `True` à la variable fait que la condition qu'elle alimente est remplie, donc le bloc en dessous s'exécute.

---

Affecter `False` à la place fait échouer la condition, donc le bloc en dessous est entièrement ignoré.

---

Le mot-clé `if` est ce qui démarre une déclaration conditionnelle — avec sa condition, il décide si le bloc ci-dessous s'exécute.

---

`"False"` entre guillemets est une chaîne de caractères, pas un booléen, et une chaîne non vide compte toujours comme vraie. Seul le `False` nu empêche un bloc de s'exécuter.
```python
print(bool("False"))  # True
```

---

Choisir `True` ici exécute les deux lignes du bloc, pas seulement la première — tout ce qui est indenté sous le `if` appartient au même bloc.

---

Les deux-points sont le seul élément dont une ligne `if` ne peut se passer : ils ferment la condition et ouvrent le bloc. Les parenthèses autour de la condition sont optionnelles en Python, donc `if True:` et `if (True):` se comportent de manière identique.

---

Les déclarations comme `if`, `elif` et `else`, qui exécutent ou ignorent du code selon une valeur booléenne, sont collectivement appelées déclarations conditionnelles.

---

L'opérateur `not` inverse une valeur booléenne : `not True` vaut `False`, et `not False` vaut `True`.
```python
is_online = False
print(not is_online)  # True
```

---

`not` construit un nouveau booléen au lieu de modifier celui qu'il lit, donc après `is_afternoon = not is_morning`, la variable `is_morning` conserve toujours sa valeur d'origine.

---

Une condition se trouve toujours entre le mot-clé `if` et les deux-points qui le suivent, nulle part ailleurs dans la ligne.

---

Il n'y a pas de limite stricte au nombre de lignes qu'un bloc `if` peut contenir — ce qui compte, c'est que chaque ligne reste indentée au même niveau.

---

Un littéral booléen fait une condition parfaitement valable : `if True:` exécute son bloc à chaque fois. L'écrire sous la forme `if (True):` est exactement la même déclaration, puisque les parenthèses autour d'une condition sont optionnelles en Python.

---

Le bloc de code d'une déclaration `if` est le groupe de lignes indentées en dessous, distingué du reste du programme par cette indentation.

---

Une condition se réduit toujours à l'une de deux valeurs, `True` ou `False` — c'est ce qui en fait un booléen.
