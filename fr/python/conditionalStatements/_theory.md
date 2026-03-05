La prise de décision est nécessaire lorsque nous voulons exécuter du code uniquement si une certaine condition est remplie.
Supposons que nous voulions jouer dehors uniquement si le temps est beau.
En programmation, nous pouvons enregistrer une variable booléenne `nice_weather` et effectuer l'action de jouer dehors `if` cette variable est `True`, comme :
```python
nice_weather = True
if (nice_weather):
    # play outside
```

---

Continuons avec l'exemple précédent.
```python
nice_weather = True
if (nice_weather):
    # play outside
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
    # play outside
else:
    # stay home
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
