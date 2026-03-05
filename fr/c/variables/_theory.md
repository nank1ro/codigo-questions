Les variables sont des conteneurs pour stocker des valeurs de données.
Chaque variable en C est un objet et comme dans d'autres langages de programmation, C a des commandes pour déclarer une variable.
Pour créer une variable, nous devons lui donner un **type** et un **nom** en gardant à l'esprit qu'il ne doit pas contenir d'espaces.
Une variable est créée au moment où vous lui attribuez une valeur pour la première fois.
Un exemple de création d'une variable nommée `x` est :
```c
int x = 1;
```
De cette façon, nous avons attribué la valeur `1` à la variable _entière_ nommée `x`.
Si nous imprimons la variable `x`, nous obtenons le nombre `1` :
```c
>>> printf("%i\n", x);
1
```

---

Les variables s'appellent ainsi parce que la valeur qu'elles stockent peut changer.
Nous pouvons mettre à jour `x` en utilisant `=` et en lui donnant une nouvelle valeur.
```c
>>> x = 1;
>>> printf("%i\n", x);
1
>>> x = 2;
>>> printf("%i\n", x);
2
```

---

Nous pouvons également donner aux variables les valeurs d'autres variables. Ici, nous pouvons donner à la variable `y` la valeur de `x`
```c
>>> int x = 5;
>>> int y = x;
>>> printf("%i\n", y);
5
```

---

Lorsque nous mettons à jour une variable, elle oublie sa valeur précédente.
Ici, nous pouvons afficher la variable `x` deux fois et voir comment sa valeur se met à jour.
```c
>>> int x = 5;
>>> printf("%i\n", x);
5
>>> x = 10;
>>> printf("%i\n", x);
10
```

---

En C, les variables chaîne ne peuvent être déclarées qu'en utilisant des guillemets doubles :
```c
char x[] = "May";
```

---

Si nous voulons un nom de variable avec plusieurs mots, nous utilisons **snake case**.
Cela signifie utiliser `_` pour connecter les mots supplémentaires.
