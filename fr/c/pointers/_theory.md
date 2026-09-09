Chaque variable vit quelque part en mémoire, et cet endroit porte un numéro appelé son **adresse**. L'opérateur `&`, qui se lit « adresse de », donne l'adresse d'une variable :
```c
int x = 42;
printf("%p\n", &x); // prints something like 0x7ffd5c3e9a4c
```
Le spécificateur `%p` affiche une adresse ; le nombre exact change d'une exécution à l'autre, les programmes ne s'y fient donc jamais.
Une adresse se stocke dans une variable de type **pointeur**. Un pointeur se déclare avec le type vers lequel il pointe, suivi de `*` :
```c
int *p = &x; // p is a pointer to int, and it holds the address of x
```
`p` est maintenant dit **pointer vers** `x`. Deux pointeurs sont égaux lorsqu'ils contiennent la même adresse, donc `p == &x` est vrai.

---

Un pointeur à lui seul n'est qu'une adresse. Pour lire la valeur stockée à cette adresse, tu **déréférences** le pointeur avec l'opérateur `*` :
```c
int x = 42;
int *p = &x;
printf("%d\n", *p); // prints "42"
```
`*p` signifie « la valeur vers laquelle `p` pointe », et c'est un `int` comme `x` lui-même. Le même symbole `*` a deux rôles : dans une déclaration `int *p`, il dit « ceci est un pointeur », dans une expression `*p`, il suit le pointeur jusqu'à la valeur.

---

Un pointeur déréférencé peut aussi être **affecté**. Écrire dans `*p` stocke la nouvelle valeur à l'adresse contenue dans `p`, donc la variable vers laquelle il pointe change :
```c
int x = 5;
int *p = &x;
*p = 10;
printf("%d\n", x); // prints "10"
```
`x` et `*p` sont deux noms pour la même mémoire. Affecter à `p` sans le `*` changerait plutôt **quelle adresse** le pointeur contient, pas la valeur qui y est stockée.

---

Un pointeur qui ne pointe encore vers rien doit contenir `NULL`, une constante spéciale définie dans `stdio.h` et `stddef.h` qui signifie « aucune adresse » :
```c
int *p = NULL;
```
Déréférencer un pointeur `NULL` est une erreur à l'exécution qui fait planter le programme, donc un pointeur qui peut être `NULL` est vérifié avant utilisation :
```c
if (p != NULL) {
    printf("%d\n", *p);
}
```
Comme `NULL` vaut zéro, `if (p)` est un raccourci courant pour `if (p != NULL)`. Un pointeur déclaré sans initialiseur contient une valeur indéterminée, pas `NULL`, donc initialise toujours les pointeurs.

---

Un pointeur peut pointer vers n'importe quel type : `double *`, `char *`, `bool *` et ainsi de suite. Le type dans la déclaration indique au compilateur combien d'octets lire lorsque le pointeur est déréférencé et ce qu'ils signifient :
```c
double price = 9.5;
double *p = &price;
*p = *p * 2; // price is now 19.0
```
Un pointeur doit correspondre au type de la variable vers laquelle il pointe ; `int *p = &price;` est rejeté par le compilateur. `NULL` est la seule valeur qui convient à un pointeur de n'importe quel type.

---

Un pointeur vers `char` fonctionne comme n'importe quel autre pointeur : il contient l'adresse d'un seul caractère, et `*p` lit ou écrit ce caractère :
```c
char grade = 'B';
char *p = &grade;
*p = 'A';
printf("%c\n", grade); // prints "A"
```
La lecture via un pointeur et l'écriture via celui-ci peuvent être mélangées librement : `*p = *p + 1` transforme `'A'` en `'B'`.

---

Un pointeur stocke une adresse, et chaque adresse a la même taille sur une machine donnée, quel que soit le type qui y est stocké. `sizeof` d'un pointeur est donc le même pour `char *`, `int *` et `double *` : `8` octets sur un système 64 bits, `4` sur un système 32 bits :
```c
printf("%zu\n", sizeof(int *));  // prints "8" on 64-bit
printf("%zu\n", sizeof(double)); // prints "8"
printf("%zu\n", sizeof(char));   // prints "1"
```
Ne confonds pas la taille du pointeur avec la taille de ce vers quoi il pointe : `sizeof(p)` est la taille de l'adresse, `sizeof(*p)` est la taille de la valeur.

---

Un nom de tableau utilisé dans une expression donne l'adresse de son **premier élément**, il peut donc être affecté directement à un pointeur :
```c
int numbers[3] = {10, 20, 30};
int *p = numbers; // same as &numbers[0]
```
Ajouter un entier à un pointeur l'avance de autant d'**éléments**, pas d'octets : `p + 1` est l'adresse de `numbers[1]`, et `*(p + 1)` vaut `20`. Le compilateur met à l'échelle le pas selon la taille du type.
L'indexation fonctionne aussi sur les pointeurs : `p[i]` est défini comme `*(p + i)`, donc `p[2]` vaut `30`. Cela s'appelle l'**arithmétique des pointeurs**.

---

Comme `p + 1` désigne l'élément suivant, `p++` fait avancer le pointeur lui-même vers l'élément suivant. Une boucle peut parcourir un tableau en faisant avancer un pointeur au lieu d'un indice :
```c
int *p = values;
for (int i = 0; i < 3; i++) {
    printf("%d\n", *p);
    p++;
}
```
Chaque tour affiche l'élément vers lequel `p` pointe, puis déplace `p` d'un élément vers l'avant.

---

Quand un tableau est passé à une fonction, il **se dégrade** en un pointeur vers son premier élément. C'est pourquoi les paramètres `int values[]` et `int *values` signifient exactement la même chose, et pourquoi la fonction ne peut pas connaître la longueur toute seule : elle ne reçoit qu'une adresse.
Des pointeurs dans le même tableau peuvent être comparés et soustraits. `end - start` est le nombre d'éléments entre eux, et une boucle peut faire courir un pointeur d'une adresse à une autre :
```c
for (int *p = start; p < end; p++) {
    printf("%d\n", *p);
}
```
Passer `numbers` et `numbers + 3` décrit les trois premiers éléments sans paramètre de taille séparé.

---

Les arguments d'une fonction sont passés **par valeur** : la fonction reçoit une copie, et affecter une valeur à un paramètre ne change jamais la variable de l'appelant. Pour qu'une fonction puisse modifier une variable, passe l'adresse de la variable et déréférence le pointeur à l'intérieur :
```c
void reset(int *p) {
    *p = 0;
}

int counter = 7;
reset(&counter); // counter is now 0
```
L'exemple classique est l'échange de deux variables, qui a besoin d'une copie temporaire d'une valeur pendant que l'autre est écrasée.

---

Une fonction ne peut `return` qu'une seule valeur. Pour en rendre plusieurs, elle prend des pointeurs vers des variables appartenant à l'appelant et y écrit les résultats. De tels paramètres sont appelés **paramètres de sortie** :
```c
void min_max(int a, int b, int *min, int *max) {
    *min = a;
    *max = b;
    if (a > b) {
        *min = b;
        *max = a;
    }
}

int lo, hi;
min_max(4, 9, &lo, &hi); // lo is 4, hi is 9
```
L'appelant déclare les variables, passe leurs adresses et les retrouve remplies après l'appel. Beaucoup de fonctions standard utilisent ce motif, et c'est pour cela que `scanf("%d", &n)` a besoin du `&`.

---

Un pointeur vers une structure atteint ses membres avec la flèche `->`, et l'adresse d'une structure stockée dans un tableau se prend avec `&items[i]`. Une fonction peut aussi **renvoyer** un pointeur, par exemple vers l'élément qu'elle a trouvé :
```c
Player *first_active(Player players[], int size) {
    for (int i = 0; i < size; i++) {
        if (players[i].active) {
            return &players[i];
        }
    }
    return NULL;
}
```
L'appelant lit ensuite les membres via le pointeur renvoyé avec `->`, après avoir vérifié qu'il n'est pas `NULL`. Renvoyer un pointeur évite de copier la structure et permet à l'appelant de modifier l'élément d'origine.

---

`const` peut protéger soit la valeur, soit le pointeur, selon l'endroit où il est écrit :
```c
const int *p = &a; // pointer to const: *p cannot be changed, p can point elsewhere
int *const q = &a; // const pointer: q always points to a, but *q can be changed
```
Lis la déclaration de droite à gauche : `p` est un pointeur vers un `int` constant ; `q` est un pointeur constant vers un `int`. Un pointeur vers const est la façon habituelle de promettre qu'une fonction se contente de **lire** ce qu'elle reçoit, comme dans `int sum(const int *values, int size)`. Une variable normale peut lui être passée ; la promesse ne limite que ce que la fonction peut faire.

---

Un pointeur est une variable, il a donc sa propre adresse, et cette adresse peut être stockée dans un **pointeur de pointeur**, déclaré avec deux étoiles :
```c
int x = 7;
int *p = &x;
int **pp = &p;
```
`*pp` est `p`, l'adresse de `x`, et `**pp` suit les deux étapes jusqu'à `7`. Les pointeurs de pointeurs permettent à une fonction de changer l'adresse que contient un pointeur : elle reçoit `&p` et affecte à `*pp`.

---

Pour finir, tout ensemble : une fonction qui parcourt un tableau avec un pointeur, garde un pointeur vers le meilleur élément rencontré jusque-là et le renvoie, ou `NULL` quand il n'y a rien à renvoyer :
```c
int *first_negative(int *values, int size) {
    for (int *p = values; p < values + size; p++) {
        if (*p < 0) {
            return p;
        }
    }
    return NULL;
}
```
L'appelant compare le résultat à `NULL` avant de le déréférencer, et peut utiliser `result - values` pour retrouver l'indice de l'élément.
