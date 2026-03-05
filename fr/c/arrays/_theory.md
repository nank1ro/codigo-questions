Les tableaux sont un type de données que vous pouvez utiliser pour stocker une collection de différents éléments d'information sous la forme d'une séquence sous un seul nom de variable.
Un tableau stocke plusieurs valeurs d'un seul type et utilise des **indices** pour distinguer ces valeurs.
Vous pouvez assigner des éléments à un tableau avec une expression de la forme :
```
data_type array_name[array_size] = {item1, item2};
```
`data_type` est le type de données que vous utiliserez pour le tableau, par exemple `int`, `double`, etc.
`array_name` est le nom de la variable qui stocke les éléments.
`array_size` est la taille maximale que le tableau peut avoir.
Enfin, `item1` et `item2` sont les valeurs que nous voulons sauvegarder dans le tableau

---

Vous pouvez accéder à un élément individuel du tableau par son indice.
Un indice est comme une adresse qui identifie la place de l'élément dans le tableau.
L'indice apparaît directement après le nom du tableau, entre crochets, comme ceci :
```
list_name[index];
```

Les indices du tableau commencent par `0`, **pas** `1` ! Vous accédez au premier élément du tableau comme ceci : `list_name[0]`.
Le deuxième élément du tableau est à l'indice 1 : `list_name[1]`.

---

Un indice de liste se comporte comme n'importe quel autre nom de variable ! Il peut être utilisé pour accéder ainsi que pour assigner des valeurs.
Vous avez vu comment accéder à un indice de liste comme ceci :
```c
int numbers[4] = {5, 6, 7, 8};
numbers[0]; // Gets the value 5
```
Voici comment fonctionne une assignation :
```c
int numbers[4] = {5, 6, 7, 8};
numbers[0] = 1;
printf("%d\n", numbers[0]); // prints the new value 1
```

---

Vous pouvez calculer la longueur en octets d'un tableau en obtenant la `sizeof` du tableau, puis vous devez la diviser par la taille d'un élément.
Cela fonctionne parce que chaque élément du tableau a le même type, et donc la même taille.
La *longueur* résultante est le nombre d'éléments qu'il contient

---

Un tableau en C doit avoir une longueur fixe.
Vous ne pouvez pas ajouter d'éléments à la fin d'un tableau, après avoir déclaré sa taille.

---

En programmation C, vous pouvez créer un tableau de tableaux.
Ces tableaux sont connus sous le nom de tableaux multidimensionnels, par exemple :
```c
int numbers[2][3] = {{1, 2, 3}, {4, 5, 6}};
```
