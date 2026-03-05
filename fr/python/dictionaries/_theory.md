Les **dictionnaires** sont similaires aux listes et aux tuples, mais vous accédez aux valeurs en cherchant une *clé* au lieu d'un index.
Une clé peut être n'importe quelle chaîne ou nombre.
Les dictionnaires sont entre accolades, comme ceci :
```python
d = {"key1": 1, "key2": 2, "key3": 3}
```
Ceci est un dictionnaire appelé `d` avec trois *paires clé-valeur*.
La clé `key1` pointe vers la valeur `1`, `key2` vers `2`, et ainsi de suite.

---

L'accès aux valeurs du dictionnaire par clé est tout comme l'accès aux valeurs de la liste par index :
```python
user['age']
# gets the age value from the user dictionary
```

---

Comme les Listes, les Dictionnaires sont _mutables_.
Cela signifie qu'ils peuvent être modifiés après leur création.
Un avantage de ceci est que nous pouvons ajouter de nouvelles _paires clé/valeur_ au dictionnaire après sa création comme ceci :
```python
dict_name[new_key_name] = new_value
```

---

La longueur `len()` d'un dictionnaire est le nombre de _paires clé-valeur_ qu'il a.
Chaque paire ne compte qu'une fois, même si la valeur est une liste. (C'est vrai : vous pouvez aussi mettre des listes dans des dictionnaires !)

---

Parce que les dictionnaires sont mutables, ils peuvent être modifiés de plusieurs façons. Les éléments peuvent être supprimés d'un dictionnaire avec la commande `del` :
```python
del dict_name[key_name]
```
supprimera la clé `key_name` et sa valeur associée du dictionnaire.

---

Que faire si nous voulons lister toutes les clés du dictionnaire ?
Eh bien, il y a la méthode `keys()` .

---

Que faire si nous voulons lister toutes les valeurs du dictionnaire ?
Eh bien, il y a la méthode `values()` .

---

Comme pour les listes, nous pouvons boucler entre les éléments du dictionnaire en utilisant les mots-clés `for..in`
Pour obtenir à la fois la clé et la valeur dans la boucle, nous pouvons utiliser la méthode `items()` :
```python
for key, value in dict_name:
    print(key, value)
```

---

Nous pouvons également utiliser le mot-clé `in` que nous avons utilisé avec les boucles pour déterminer si un dictionnaire contient une certaine __clé__

---

Pour __ajouter__ ou __changer__ des valeurs à un dictionnaire, nous pouvons également utiliser la méthode `update()` avec les _paires clé-valeur_ que nous voulons ajouter entre accolades

---

Que se passe-t-il si nous voulons __supprimer__ une valeur d'un dictionnaire ?
Il y a la méthode `pop()` :
```python
dict_name.pop("key_name")
```
