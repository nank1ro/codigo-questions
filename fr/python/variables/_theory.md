Les variables sont des conteneurs pour stocker des valeurs de données.
Chaque variable en Python est un objet et contrairement à d'autres langages de programmation, Python n'a pas de commande pour déclarer une variable.
Pour créer une variable, nous devons lui donner un **nom** en gardant à l'esprit qu'il ne doit pas contenir d'espaces.
Une variable est créée au moment où vous lui assignez une valeur pour la première fois.
Un exemple de création de variable nommée `x` est :
```python
x = 1
```
De cette manière, nous avons assigné la valeur `1` à la variable nommée `x`.
Si nous affichons la variable `x`, nous obtenons le nombre `1` :
```python
>>> print(x)
1
```

---

Les variables s'appellent ainsi parce que la valeur qu'elles stockent peut changer.
Nous pouvons mettre à jour `x` en utilisant `=` et en lui donnant une nouvelle valeur.
```python
>>> x = 1
>>> print(x)
1
>>> x = 2
>>> print(x)
2
```

---

Nous pouvons aussi donner aux variables les valeurs d'autres variables. Ici, nous pouvons donner à la variable `y` la valeur de `x`
```python
>>> x = 5
>>> y = x
>>> print(y)
5
```

---

Quand nous mettons à jour une variable, elle oublie sa valeur précédente. Ici, nous pouvons afficher la variable `x` deux fois et voir comment sa valeur se met à jour.
```python
>>> x = 5
>>> print(x)
5
>>> x = 10
>>> print(x)
10
```

---

Les variables de chaîne peuvent être déclarées soit en utilisant des guillemets simples, soit des guillemets doubles :
```python
>>> x = "May"
>>> x = 'May'
```
Both are the same thing.

---

Si nous voulons un nom de variable avec plusieurs mots, nous utilisons le **snake case**.
Cela signifie utiliser `_` pour connecter les mots supplémentaires.
