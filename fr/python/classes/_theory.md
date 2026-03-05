Python est un langage de programmation orienté objet, ce qui signifie qu'il manipule des constructions de programmation appelées objets.
Vous pouvez penser à un objet comme une seule structure de données qui contient des données ainsi que des fonctions; les fonctions d'un objet sont appelées ses méthodes.
Par exemple, lorsque vous appelez:
```python
dict_name.items()
```
Python vérifie si `my_dict` a une méthode `items()` (que tous les dictionnaires ont) et exécute cette méthode s'il la trouve.

---

Une classe de base se compose uniquement du mot-clé `class` et du nom de la classe, par exemple:
```python
class ClassName:
    pass
```

---

Remplaçons `pass` par quelque chose d'autre.
La méthode `__init__()` est requise pour les classes, et elle est utilisée pour __initialiser__ les objets qu'elle crée.
`__init__()` prend toujours au moins un argument, `self`, qui fait référence à l'objet en cours de création.
Vous pouvez penser à `__init__()` comme la méthode qui démarre chaque objet que la classe crée.

---

Bien sûr, la méthode `__init__()` peut utiliser plus de paramètres que `self`

---

Le premier argument `__init__()` est utilisé pour faire référence à l'objet instance, et par convention, cet argument s'appelle `self`.
Si vous ajoutez des arguments supplémentaires (par exemple, un `gender` et des `legs` pour votre animal) en définissant chacun d'eux égal à `self.gender` et `self.legs` dans le corps de `__init__()`, cela fera en sorte que lorsque vous créez un objet instance de votre classe `Animal`, vous devrez donner à chaque instance un gender et des legs, et ceux-ci seront associés à l'instance particulière que vous créez

---

Définir une classe ne crée pas d'objet.
Pour ce faire, nous devons créer une __instance__ d'une classe

---

Quand une classe a ses propres fonctions, ces fonctions sont appelées __méthodes__. Vous avez déjà vu une telle méthode: `__init__()`.
Mais vous pouvez aussi définir vos propres méthodes!
