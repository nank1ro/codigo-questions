La prise de décision est nécessaire quand nous voulons exécuter du code seulement si une certaine condition est satisfaite.
Supposons que nous voulions jouer dehors seulement si le temps est beau.
En programmation, nous pouvons sauvegarder une variable booléenne `nice_weather` et effectuer l'action de jouer dehors `if` cette variable est `true`, comme ceci :
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
}
```

---

Continuons avec l'exemple précédent.
```c
bool nice_weather = true;
if (nice_weather) {
    // play outside
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
    // play outside
} else {
    // stay home
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
