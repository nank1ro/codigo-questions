Une **énumération** (`enum`) donne des noms à un ensemble de constantes entières liées, afin que vous puissiez écrire `RED` au lieu d'un simple nombre.
Vous la déclarez avec le mot-clé `enum`, un nom et la liste des constantes entre accolades :
```c
enum Color { RED, GREEN, BLUE };
```
Chaque constante est un entier : sauf indication contraire, la première vaut `0` et chaque suivante vaut la précédente plus un, donc `RED` vaut `0`, `GREEN` vaut `1` et `BLUE` vaut `2`.
Comme ce sont des entiers, vous les affichez avec `%d` :
```c
printf("%d\n", GREEN);
// prints "1"
```

---

La numérotation continue automatiquement pour autant de constantes que vous en listez : la quatrième constante est `3`, la cinquième est `4`, et ainsi de suite.
Les noms sont généralement écrits en majuscules, comme les autres constantes, et ils doivent être uniques dans tout le programme : deux énumérations ne peuvent pas partager le nom d'une constante.

---

Vous pouvez aussi donner une valeur explicite à une constante avec `=` ; les constantes suivantes continuent de compter à partir de cette valeur :
```c
enum Month { JAN = 1, FEB, MAR }; // FEB is 2, MAR is 3
```
Les valeurs explicites n'ont pas besoin d'être consécutives ou croissantes : `enum Status { OK = 200, NOT_FOUND = 404 };` est parfaitement valide.

---

Une énumération est aussi un type : vous pouvez déclarer une variable de ce type en écrivant `enum` suivi du nom de l'énumération, et lui assigner une de ses constantes :
```c
enum Color favorite = GREEN;
```
Comme les constantes sont des entiers, vous comparez les variables d'énumération avec les opérateurs habituels :
```c
if (favorite == GREEN) {
    printf("Green it is\n");
}
```

---

Une énumération peut être le type d'un paramètre de fonction, exactement comme `int` :
```c
int is_weekend(enum Day day) {
    return day == SAT || day == SUN;
}
```
À l'intérieur de la fonction, un `switch` est la façon naturelle de traiter chaque constante, car les constantes d'énumération peuvent être utilisées directement comme étiquettes `case` :
```c
switch (day) {
    case SAT: return 1;
    case SUN: return 1;
    default: return 0;
}
```

---

Quand chaque cas d'un `switch` traite une constante, pensez au `break` après chacun, sinon l'exécution se poursuit dans le cas suivant.
Un cas `default` n'est pas nécessaire si vous couvrez toutes les constantes de l'énumération.

---

Une fonction peut aussi retourner une énumération ; utilisez simplement le type énuméré comme type de retour et retournez une de ses constantes :
```c
enum Grade grade_for(int score) {
    if (score >= 60) {
        return PASS;
    }
    return FAIL;
}
```
Retourner une constante nommée est beaucoup plus clair pour l'appelant que retourner un simple `0` ou `1`.

---

Écrire `enum Color` à chaque fois est fastidieux. Avec `typedef`, vous donnez à l'énumération un nom de type court, et l'énumération elle-même peut rester anonyme :
```c
typedef enum { RED, GREEN, BLUE } Color;

Color favorite = BLUE;
```
Le nouveau nom `Color` est utilisé seul, sans le mot-clé `enum` devant.

---

Une constante d'énumération se convertit automatiquement en `int`, donc `int n = BLUE;` est valide et stocke `2`.
Le chemin inverse se fait avec une **conversion**, en écrivant le type énuméré entre parenthèses avant l'entier :
```c
enum Color c = (enum Color)1; // c is GREEN
```
C ne vérifie pas que le nombre correspond à une constante : `(enum Color)7` compile même si aucune constante ne vaut `7`, il faut donc valider les entiers avant de les convertir.

---

Une opération arithmétique sur une valeur d'énumération produit un simple `int` : `GREEN + 1` vaut `2`, pas `BLUE`.
Pour stocker à nouveau le résultat dans une variable d'énumération ou le retourner depuis une fonction, convertissez-le vers le type énuméré :
```c
enum Color after_green = (enum Color)(GREEN + 1); // BLUE
```
Combiné à l'opérateur modulo `%`, cela permet de parcourir cycliquement les constantes et de revenir à la première.

---

Une astuce courante consiste à ajouter une constante supplémentaire à la fin de l'énumération, généralement nommée `COUNT` : comme la numérotation commence à `0`, sa valeur correspond exactement au nombre de constantes réelles qui la précèdent.
```c
enum Day { MON, TUE, WED, DAY_COUNT }; // DAY_COUNT is 3
```
Cette sentinelle vous permet de parcourir toutes les constantes sans coder le nombre en dur, et elle reste correcte quand vous ajoutez des constantes avant elle :
```c
for (int d = MON; d < DAY_COUNT; d++) {
    printf("%d\n", d);
}
```

---

La sentinelle `COUNT` est aussi la taille parfaite pour un tableau avec une case par constante, et les constantes deviennent des indices lisibles dans celui-ci :
```c
enum Fruit { APPLE, BANANA, CHERRY, FRUIT_COUNT };

int stock[FRUIT_COUNT] = {10, 4, 7};
printf("%d\n", stock[BANANA]); // prints "4"
```
Une boucle de `0` à `FRUIT_COUNT` visite chaque case, et l'indice de boucle peut être reconverti en `enum Fruit` quand vous devez le retourner.

---

C n'offre aucun moyen intégré d'obtenir le nom d'une constante d'énumération : `printf("%d\n", SUMMER)` affiche `2`, pas `Summer`. La solution habituelle est une petite fonction avec un `switch` qui retourne la chaîne correspondant à chaque constante.

---

Les valeurs d'énumération peuvent être stockées dans des tableaux comme n'importe quel autre entier : `enum Fruit basket[] = {APPLE, APPLE, CHERRY};` contient trois fruits, et chaque élément peut être comparé à une constante.
