La prise de décision est nécessaire quand nous voulons exécuter du code seulement si une certaine condition est satisfaite.
Supposons que nous voulions jouer dehors seulement si le temps est beau.
En programmation, nous pouvons sauvegarder une variable booléenne `nice_weather` et effectuer l'action de jouer dehors `if` cette variable est `true`, comme ceci :
```c
bool nice_weather = true;
if (nice_weather) {
    // joue dehors
}
```

---

Continuons avec l'exemple précédent.
```c
bool nice_weather = true;
if (nice_weather) {
    // joue dehors
}
```
Nous avons vu que la déclaration `if` exécute le bloc de code seulement si la condition est `true`.
Une autre chose importante à considérer est représentée par les **accolades** `{}` qui indiquent un bloc de code.

---

Nous venons de voir comment exécuter un bloc de code si une condition se produit, maintenant voyons comment exécuter un autre bloc de code si la première condition échoue.
Nous allons jouer dehors si le temps est beau ; sinon, nous restons à la maison.
En C, nous pouvons utiliser la déclaration `else`, comme ceci :
```c
bool nice_weather = false;
if (nice_weather) {
    // joue dehors
} else {
    // reste à la maison
}
```

---

Supposons que nous ayons une autre condition à vérifier, comme dans cet exemple :
```c
int num = 3;
if (num == 2) {
    printf("the number is 2\n");
} else if (num == 3) {
    printf("the number is 3\n");
} else {
    printf("do something else\n");
}
```
et la sortie de ce code est `the number is 3`.
Tout d'abord, vérifions si le nombre est égal à 2, c'est faux.
Passons à la deuxième déclaration et vérifions si `num` est égal à 3, étant vrai, nous exécutons le bloc de code suivant en imprimant `the number is 3`

---

Nous pouvons ajouter autant de déclarations `else if` que nous le voulons, il n'y a pas de limites
```c
int num = 4;
if (num == 2) {
    printf("the number is 2");
} else if (num == 3) {
    printf("the number is 3");
} else if (num == 4) {
    printf("the number is 4");
} else if (num == 5) {
    printf("the number is 5");
} else if (num == 6) {
    printf("the number is 6");
}
```
et la sortie de ce code est `the number is 4`.

---

Nous pouvons également imbriquer une déclaration conditionnelle (`if`, `else if` ou `else`) à l'intérieur d'une autre déclaration conditionnelle, pour créer une structure plus complexe.
```c
int num = 4;
if (num < 3) {
    printf("the number is lower than 3\n");
} else {
    if (num == 3) {
        printf("the number is 3\n");
  } else if (num == 4) {
        printf("the number is 4\n");
  } else {
        printf("the number is greather than 4\n");
  }
}
```
et la sortie de ce code est `the number is 4`.

---

Il est temps de mettre en pratique la syntaxe de la déclaration `if` : le mot-clé, une condition entre parenthèses, et un bloc de code entre accolades.
```c
if (condition) {
    // s'exécute si la condition est vraie
}
```

---

Les littéraux booléens en C sont `true` et `false` : en minuscules, sans guillemets, et définis par `<stdbool.h>` plutôt qu'intégrés au langage. Écrire `True` ne compilera pas comme condition — seule la forme en minuscules fonctionne, et quand elle vaut `true`, le bloc s'exécute.

---

Le C n'a pas de test booléen distinct : une condition est vraie dès que sa valeur est différente de zéro. `false`, défini dans `<stdbool.h>`, vaut simplement `0`, donc un bloc protégé par cette valeur ne s'exécute jamais.

---

Une déclaration `if` en C se compose de trois parties : le mot-clé `if`, une condition entre parenthèses, et un bloc entre accolades. Les parenthèses sont obligatoires — c'est ainsi que le compilateur sait où se termine la condition.

---

Chaque déclaration conditionnelle commence par un mot-clé qui indique au compilateur qu'une condition doit être vérifiée avant de décider ce qui s'exécute ensuite.

---

Une condition littérale `true` est toujours vraie, donc le bloc s'exécute et son `printf` s'exécute exactement tel qu'il est écrit.

---

Une condition littérale `false` n'est jamais vraie, donc le bloc est entièrement ignoré et rien de ce qu'il contient ne s'exécute.

---

Les conditions sont les valeurs qu'une déclaration `if` vérifie : quand une condition est `true`, le bloc s'exécute, quand elle est `false`, il est ignoré.

---

L'accolade ouvrante peut se trouver sur la même ligne que la condition ou sur la ligne suivante. Le C ignore le saut de ligne, donc les deux styles se compilent en exactement le même programme.

---

Les parenthèses autour d'une condition font partie de la syntaxe `if` du C, ce ne sont pas un regroupement optionnel : `if true { ... }` ne compile pas.

---

Un `"false"` entre guillemets est une chaîne de caractères, pas un booléen — et une chaîne dans une condition est une adresse non nulle, ce qui compte comme vrai. Seul le `false` sans guillemets empêche le bloc de s'exécuter.

---

L'espacement entre les éléments d'une ligne `if` est libre en C : `if(true){` et `if (true) {` sont la même instruction pour le compilateur, seul l'ordre des éléments compte.

---

Un bloc de code ne se limite pas à une seule instruction. Chaque instruction entre les accolades s'exécute, l'une après l'autre, dans l'ordre où elle est écrite.

---

Une variable booléenne peut être utilisée directement comme condition, sans avoir besoin de comparaison. Puisque `online` contient déjà `true`, écrire simplement `if (online)` suffit à exécuter le bloc.

---

Une variable `bool` fonctionne comme condition parce que `if` ne regarde que la valeur qu'elle contient à cet instant. Avec `false` dans `online`, `if (online)` se comporte exactement comme `if (false)`.

---

Seul le code entre les accolades d'une déclaration `if` est conditionnel. Tout ce qui est écrit après l'accolade fermante s'exécute sans condition, quelle qu'ait été la condition.

---

Il n'y a pas de limite fixe au nombre d'instructions qu'un bloc de code peut contenir — une ligne ou une centaine, elles s'exécutent toutes ensemble quand la condition est `true`.

---

Lire une variable booléenne comme condition fonctionne comme un littéral : puisque `online` contient `true`, le bloc s'exécute et son `printf` s'exécute.

---

Quand `online` contient `false` à la place, la condition est fausse, donc le bloc est entièrement ignoré et rien de ce qui se trouve dans ces accolades n'est affiché.
