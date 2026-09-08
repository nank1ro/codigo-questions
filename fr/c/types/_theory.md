C est un langage à **typage statique** : chaque variable est déclarée avec un type qui détermine ce qu'elle peut stocker et l'espace mémoire qu'elle occupe.
Les trois types que vous utiliserez le plus sont :
- `int` pour les nombres entiers, comme `30` ou `-4`
- `double` pour les nombres à partie décimale, comme `1.75`
- `char` pour un seul caractère, écrit entre guillemets simples comme `'A'`

Chaque type a son propre **spécificateur de format** `printf` : `%d` affiche un `int`, `%f` affiche un `double` (avec six décimales par défaut) et `%c` affiche un `char` :
```c
int age = 30;
double height = 1.75;
char initial = 'A';
printf("%d %f %c\n", age, height, initial);
// affiche "30 1.750000 A"
```
Utiliser le mauvais spécificateur pour un type affiche n'importe quoi, alors faites-les toujours correspondre.

---

C possède deux types à virgule flottante : `float` (simple précision, environ 7 chiffres significatifs) et `double` (double précision, environ 15 chiffres significatifs).
Un littéral décimal comme `1.75` est un `double` ; pour écrire un littéral `float`, ajoutez le suffixe `f`, comme dans `1.75f`.
Préférez `double` sauf si la mémoire est limitée : c'est le type par défaut et il est plus précis.
```c
double pi = 3.14159;
float ratio = 0.5f;
```
Une fonction qui retourne un résultat décimal doit déclarer `double` comme type de retour, et les paramètres `double` acceptent aussi bien des arguments entiers que décimaux :
```c
double half(double x) {
    return x / 2;
}
```

---

`%f` affiche six décimales, ce qui est rarement ce que vous voulez. Placez une précision entre `%` et `f` pour choisir combien de décimales afficher : `%.2f` affiche deux décimales, `%.1f` en affiche une, et la valeur est **arrondie**, pas tronquée :
```c
double price = 9.987;
printf("%.2f\n", price); // affiche "9.99"
printf("%.1f\n", price); // affiche "10.0"
```
Un `float` s'affiche avec les mêmes spécificateurs qu'un `double` : lorsqu'il est passé à `printf`, il est converti automatiquement en `double`.

---

Le résultat de `/` dépend des types de ses opérandes.
Quand **les deux** opérandes sont des entiers, le résultat est un entier et la partie décimale est perdue : `7 / 2` vaut `3`, pas `3.5`.
Quand **au moins un** des opérandes est une valeur à virgule flottante, la division conserve les décimales : `7 / 2.0` vaut `3.5`.
```c
printf("%d\n", 7 / 2);     // affiche "3"
printf("%f\n", 7 / 2.0);   // affiche "3.500000"
```
Écrire le littéral `2.0` au lieu de `2` est le moyen le plus simple de forcer une division à virgule flottante.

---

C convertit entre les types numériques de manière **implicite** lorsqu'une valeur est assignée à une variable d'un type différent.
- un `int` stocké dans un `double` est élargi sans perte : `double d = 3;` rend `d` égal à `3.0`
- un `double` stocké dans un `int` est **tronqué** : `int n = 3.99;` rend `n` égal à `3` (les compilateurs avertissent généralement de cela)

La conversion n'a lieu qu'au moment de l'affectation. L'expression de droite est d'abord calculée avec ses propres types :
```c
double d = 7 / 2;
```
Ici, `7 / 2` est une division entière qui donne `3`, et ce n'est qu'ensuite que `3` est converti en `3.0`.

---

Lorsque la conversion implicite n'est pas ce que vous voulez, ou que vous voulez la rendre visible, utilisez une **conversion explicite (cast)** : écrivez le type cible entre parenthèses avant la valeur.
```c
double x = 3.99;
int n = (int) x;   // n vaut 3
```
Convertir une valeur à virgule flottante en `int` **tronque vers zéro** : `(int) 3.99` vaut `3` et `(int) -2.5` vaut `-2`, aucun arrondi n'a lieu.
Le cast ne s'applique qu'à la valeur juste après lui, donc `(int) x * 2` convertit d'abord `x` puis multiplie.

---

Un cast est le moyen standard d'obtenir une division à virgule flottante à partir de deux variables `int` : convertissez **un seul opérande** en `double` avant de diviser.
```c
int total = 7, count = 2;
double avg = (double) total / count; // 3.5
```
Convertir plutôt le résultat entier, comme dans `(double) (total / count)`, est une erreur courante : la division entière a déjà eu lieu et les décimales sont perdues.

---

Un `char` est en réalité un petit entier : il stocke le **code ASCII** du caractère.
`'A'` vaut `65`, `'a'` vaut `97` et `'0'` vaut `48`, et des caractères consécutifs ont des codes consécutifs.
C'est pourquoi vous pouvez faire de l'arithmétique sur des caractères :
- `'a' + 1` vaut `98`, le code de `'b'`
- `'7' - '0'` vaut `55 - 48`, c'est-à-dire le nombre `7`

La même valeur peut être affichée comme caractère avec `%c` ou comme nombre avec `%d` :
```c
char c = 'A';
printf("%c %d\n", c, c); // affiche "A 65"
```

---

Les lettres majuscules et minuscules sont séparées de `32` positions dans la table ASCII : `'A'` vaut `65` et `'a'` vaut `97`.
Soustraire `32` à une lettre minuscule donne donc sa version majuscule, et le résultat peut être stocké dans un `char` :
```c
char upper = 'g' - 32; // 'G'
```

---

`int` n'est pas le seul type entier. Des modificateurs changent sa taille et sa plage :
- `short` utilise moins de mémoire et a une plage plus petite (généralement de -32768 à 32767)
- `long` a une plage plus grande (sur les systèmes 64 bits, environ ±9 trillions)
- `unsigned` supprime le signe : `unsigned int` va de `0` à environ 4 milliards, mais ne peut jamais être négatif

Un littéral qui doit être `long` prend le suffixe `L`, un `unsigned` le suffixe `U`, et chaque type a son propre spécificateur :
```c
long population = 8000000000L;
unsigned int count = 40U;
printf("%ld %u\n", population, count); // affiche "8000000000 40"
```
`%ld` affiche un `long`, `%u` un `unsigned int` et `%lu` un `unsigned long`. Un `int` classique, sur la plupart des systèmes, contient des valeurs jusqu'à environ 2 milliards, donc `5000000000` n'y tient pas.

---

L'opérateur `sizeof` indique combien d'**octets** occupe un type ou une variable. Son résultat a le type `size_t`, qui s'affiche avec `%zu` :
```c
printf("%zu\n", sizeof(int));  // affiche "4" sur la plupart des systèmes
```
La norme garantit seulement que `sizeof(char)` vaut `1` et que `short <= int <= long`, mais sur un système 64 bits typique, les tailles sont : `char` 1, `short` 2, `int` 4, `long` 8, `float` 4, `double` 8.
`sizeof` est souvent utilisé pour vérifier combien de mémoire une variable occupe sans coder le nombre en dur.

---

Chaque type entier a une plage limitée, et l'en-tête `limits.h` donne un nom à ces limites : `INT_MAX` et `INT_MIN` pour `int`, `LONG_MAX` pour `long`, `UINT_MAX` pour `unsigned int`, et ainsi de suite.
```c
#include <limits.h>

printf("%d\n", INT_MAX); // affiche "2147483647" sur la plupart des systèmes
```
Dépasser `INT_MAX` avec un type signé est un **comportement indéfini** : le programme peut déborder, planter, ou faire n'importe quoi d'autre. Vérifiez avant de calculer :
```c
if (a <= INT_MAX - b) { /* a + b est sûr */ }
```
Notez que la vérification soustrait au lieu d'additionner, car `a + b` lui-même pourrait déjà déborder.

---

Contrairement aux types signés, l'arithmétique **unsigned** est bien définie lorsqu'elle sort de sa plage : la valeur **revient au début** comme un compteur kilométrique.
Ajouter `1` à `UINT_MAX` donne `0`, et soustraire `1` à `0` donne `UINT_MAX` (`4294967295` quand `unsigned int` a 32 bits) :
```c
unsigned int n = UINT_MAX;
n = n + 1;
printf("%u\n", n); // affiche "0"
```
C'est pourquoi une boucle qui décompte une variable `unsigned` "jusqu'à ce qu'elle soit négative" ne s'arrête jamais : une valeur unsigned n'est jamais inférieure à `0`.

---

Depuis C99, l'en-tête `stdbool.h` fournit le type `bool` avec les constantes `true` (`1`) et `false` (`0`).
Un `bool` est un type entier avec seulement deux valeurs, donc convertir n'importe quel nombre en `bool` donne `true` pour toute valeur non nulle et `false` pour `0`. C'est différent de la conversion en `int` :
```c
#include <stdbool.h>

bool b = 0.5;  // true, car 0.5 n'est pas zéro
int n = 0.5;   // 0, car les décimales sont tronquées
```
Des comparaisons comme `x != 0` produisent déjà un résultat compatible avec `bool`, et une fonction retournant `bool` indique qu'elle répond à une question par oui ou par non.

---

Une opération arithmétique est effectuée dans le type de ses opérandes, **et non** dans le type de la variable qui reçoit le résultat.
Ainsi, `long big = n * n;` avec un `n` de type `int` multiplie deux valeurs `int`, déborde si le produit est trop grand, et ce n'est qu'ensuite que le résultat (déjà faux) est stocké dans le `long`.
Convertissez un opérande **avant** l'opération pour calculer dans le type le plus large :
```c
int n = 100000;
long big = (long) n * n; // 10000000000, calculé en long
```
La même règle explique pourquoi `(double) total / count` fonctionne : le cast change le type de l'opérande, et la division suit.

---

Pour tout assembler : choisissez le type en fonction de la nature de la valeur, faites correspondre chaque spécificateur `printf` au type de son argument, et convertissez lorsqu'un calcul doit se faire dans un type différent de celui de ses opérandes.
