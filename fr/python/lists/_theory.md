Les listes sont un type de données que vous pouvez utiliser pour stocker une collection de différents éléments d'information sous la forme d'une séquence dans un seul nom de variable.
Une liste stocke plusieurs valeurs de n'importe quel type et utilise des **indices** pour distinguer ces valeurs.
Vous pouvez attribuer des éléments à une liste avec une expression de la forme :
```python
list_name = [item1, item2]
```

---

Vous pouvez accéder à un élément individuel de la liste par son indice.
Un indice est comme une adresse qui identifie la place de l'élément dans la liste.
L'indice apparaît directement après le nom de la liste, entre crochets, comme ceci :
```python
list_name[index]
```

List indices begin with `0`, **not** `1`! You access the first item in a list like this: `list_name[0]`.
The second item in a list is at index 1: `list_name[1]`.

---

Un indice de liste se comporte comme n'importe quel autre nom de variable ! Il peut être utilisé pour accéder ainsi que pour assigner des valeurs.
Vous avez vu comment accéder à un indice de liste comme ceci :
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] # Gets the value "Jeremiah"
```
Voici comment fonctionne une affectation :
```python
names = ["Jeremiah", "Barney", "Ivan", "Noel"]
names[0] = "Jordan"
names[0] # Gets the new value "Jordan"
```

---

Tout comme les chaînes, les listes ont une **longueur**.
La longueur d'une liste est le nombre d'éléments qu'elle contient

---

Une liste n'a pas besoin d'avoir une longueur fixe.
Vous pouvez ajouter des éléments à la fin d'une liste à tout moment !
To add an item to a list we use the `append` keyword:
```python
>>> letters = ["a", "b"]
>>> letters.append("c")
>>> print(letters)
['a', 'b', 'c']
```

---

Parfois, vous ne voulez accéder qu'à une partie d'une liste.
Considérez le code suivant :
```python
>>> numbers = [1, 2, 3, 4]
>>> slice = numbers[1:3]
>>> print(slice)
[2, 3]
```
D'abord, nous créons une liste appelée `numbers`.
Ensuite, nous prenons une sous-section de la liste et la stockons dans la liste de tranches.
Nous le faisons en définissant les indices que nous voulons inclure après le nom de la liste : `numbers[1:3]`.
En Python, quand nous spécifions une partie d'une liste de cette manière, nous incluons l'élément avec le premier indice, `1`, mais nous excluons l'élément avec le deuxième indice, `3`.

---

Vous pouvez découper une chaîne exactement comme une liste ! En fait, vous pouvez penser aux chaînes comme des listes de caractères : chaque caractère est un élément séquentiel dans la liste, à partir de l'indice `0`.
```python
list_name[:2]
# Grabs the first two items
list_name[3:]
# Grabs the fourth through last items
```
Si votre tranche de liste inclut le tout premier ou le dernier élément d'une liste (ou d'une chaîne), l'indice de cet élément ne doit pas être inclus.

---

Les éléments de liste peuvent être de n'importe quel type :
```python
list_name = ["one", 2, True]
```
En fait, ci-dessus nous avons, dans l'ordre, une chaîne, un entier et une valeur booléenne.
Mais nous pouvons aussi avoir des listes avec des listes !

---

Parfois, vous devez rechercher un élément dans une liste.
En Python, nous pouvons utiliser la méthode `index()` :
```python
>>> names = ["Trevor", "Zac", "Glenn"]
>>> print(names.index("Zac"))
1
```
The code above prints the first index that contains the string `"Zac"`, `1` in this case.
We can also insert items into a list in a specific index, using the `insert()` method:
```python
>>> names.insert(1, "Ali")
>>> print(names)
['Trevor', 'Ali', 'Zac', 'Glenn']
```
The code above inserts `"Ali"` at index `1`, which moves everything, after this index, down by 1

---

En Python, nous pouvons parcourir une liste de manière très simple en utilisant les mots-clés `for..in` :
```python
>>> numbers = [1, 2, 3]
>>> for num in numbers:
>>>     print(num)
1
2
3
```
A variable name follows the `for` keyword, it will be assigned the value of each list item in turn.

---

Les **tuples** sont comme des listes mais sont beaucoup plus rapides.
Cependant, les valeurs des tuples ne peuvent pas être modifiées.
Nous avons tendance à utiliser des tuples pour les données **read-only** qui restenttant while the program is running.
To create a tuple we use the round brackets `()`

---

Il peut y avoir des moments où nous voulons convertir notre tuple en liste.
Pour ce faire, nous pouvons utiliser la fonction `list()`

---

De même, nous pouvons convertir une liste en tuple
