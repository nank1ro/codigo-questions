Les **opérateurs de comparaison** comparent deux valeurs et produisent un résultat : `1` quand la comparaison est vraie et `0` sinon.
L'opérateur **égal** `==` vérifie si deux valeurs sont identiques, l'opérateur **différent** `!=` vérifie si elles diffèrent :
```c
int a = 7, b = 3;
printf("%d\n", a == b);
// affiche "0"
printf("%d\n", a != b);
// affiche "1"
```
Attention : `==` (deux signes) compare, alors qu'un seul `=` assigne une valeur.

---

Les autres opérateurs de comparaison vérifient l'ordre de deux valeurs :
- `<` inférieur à, `>` supérieur à
- `<=` inférieur ou égal à, `>=` supérieur ou égal à
```c
printf("%d\n", 3 < 5);  // affiche "1"
printf("%d\n", 5 >= 6); // affiche "0"
```
Une fonction peut retourner une comparaison directement, car le résultat est un simple `int` :
```c
int is_big(int n) {
    return n > 100;
}
```

---

En C, le résultat d'une comparaison n'est pas un type spécial : c'est un `int` dont la valeur est exactement `1` (vrai) ou `0` (faux).
Cela signifie que vous pouvez le stocker dans une variable `int` comme n'importe quel autre nombre :
```c
int n = 42;
int big = n > 100; // big vaut 0
```
Il n'y a pas de mot `true`/`false` dans la sortie : `printf("%d", 2 == 2)` affiche `1`.

---

Les **opérateurs logiques** combinent des comparaisons. L'opérateur **et** `&&` donne `1` seulement quand les deux côtés sont vrais :
```c
int age = 25;
printf("%d\n", age >= 18 && age < 65); // affiche "1"
```
Ne chaînez pas les comparaisons comme en mathématiques : `1 <= x <= 10` est évalué comme `(1 <= x) <= 10`, qui compare un `0` ou `1` à `10` et est toujours vrai.
Écrivez toujours les deux comparaisons explicitement et joignez-les avec `&&`.

---

L'opérateur **ou** `||` donne `1` quand au moins un côté est vrai, et `0` seulement quand les deux côtés sont faux :
```c
int day = 1;
printf("%d\n", day == 1 || day == 7); // affiche "1"
```
Chaque côté doit être une comparaison complète : `day == 6 || 7` ne signifie pas "6 ou 7" (vous verrez pourquoi plus tard).

---

L'opérateur **non** `!` inverse un résultat : `!1` vaut `0` et `!0` vaut `1`.
Il se place devant l'expression, utilisez donc des parenthèses pour nier une comparaison entière :
```c
int n = 5;
printf("%d\n", !(n > 3)); // affiche "0"
```
Sans les parenthèses, `!n > 3` calculerait d'abord `!n` puis le comparerait à `3`.

---

Les opérateurs logiques ne fonctionnent pas seulement avec `0` et `1` : en C, **toute valeur non nulle compte comme vraie** et seul `0` compte comme faux.
Ainsi, `5 && 1` vaut `1`, `0 || -3` vaut `1`, et `!` transforme toute valeur non nulle en `0` :
```c
printf("%d\n", !7); // affiche "0"
printf("%d\n", !0); // affiche "1"
```
C'est pourquoi `day == 6 || 7` est toujours vrai : `7` seul est déjà une valeur vraie.

---

`&&` et `||` utilisent l'**évaluation en court-circuit** : ils s'arrêtent dès que le résultat est connu.
- avec `&&`, si le côté gauche vaut `0`, le côté droit n'est jamais évalué
- avec `||`, si le côté gauche est vrai, le côté droit n'est jamais évalué

Cela permet de protéger une opération dangereuse avec une vérification placée à sa gauche :
```c
int safe = divisor != 0 && value / divisor > 2;
```
Quand `divisor` vaut `0`, la division n'est jamais exécutée.

---

L'évaluation en court-circuit saute aussi les appels de fonction : dans `0 && check()`, la fonction `check` n'est jamais appelée, donc aucun effet de bord qu'elle produirait (comme mettre à jour un compteur) ne se produit.

---

Les opérateurs ont une **priorité** qui décide de ce qui est calculé en premier :
1. `!` est appliqué en premier
2. puis les comparaisons relationnelles `<`, `>`, `<=`, `>=`
3. puis les comparaisons d'égalité `==`, `!=`
4. puis `&&`
5. puis `||`

Ainsi, `a > 0 && a < 10` n'a pas besoin de parenthèses : les deux comparaisons sont calculées avant `&&`.
Et `x == 1 || y == 2 && z == 3` signifie `x == 1 || (y == 2 && z == 3)`, car `&&` est plus prioritaire que `||`.

---

Un `char` est un petit entier, les caractères peuvent donc être comparés avec les mêmes opérateurs.
Comparez avec un littéral de caractère entre guillemets simples :
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // affiche "1"
```
Des guillemets doubles créeraient une chaîne, qui ne peut pas être comparée ainsi.

---

Comme les caractères sont des nombres, `<` et `>` comparent leurs codes, et des caractères consécutifs comme `'a'`, `'b'`, `'c'` ou `'0'`, `'1'`, `'2'` ont des codes consécutifs.
Une vérification de plage sur des caractères fonctionne donc exactement comme sur des nombres :
```c
int is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

Une erreur classique en C consiste à écrire `=` alors que `==` était voulu. Le code compile quand même, car une affectation est une expression dont la valeur est la valeur affectée :
```c
int x = 5;
if (x = 0) { ... } // affecte 0 à x, la condition vaut 0 (faux)
if (x = 3) { ... } // affecte 3 à x, la condition vaut 3 (vrai)
```
La plupart des compilateurs avertissent à ce sujet, alors lisez les avertissements quand une condition se comporte étrangement.

---

La condition d'un `if` est simplement une expression traitée comme vraie quand elle est non nulle, donc les comparaisons et les opérateurs logiques s'y intègrent naturellement :
```c
if (n < 0) {
    printf("negative\n");
} else if (n == 0) {
    printf("zero\n");
}
```
Vous pouvez aussi stocker d'abord le résultat et tester la variable : `int ok = n > 0; if (ok) { ... }`.

---

Une boucle `while` continue de s'exécuter tant que sa condition est non nulle, donc une comparaison décide quand elle s'arrête :
```c
int i = 0;
while (i < 3) {
    printf("%d\n", i);
    i++;
}
// affiche 0, 1, 2
```
Choisir entre `<` et `<=` change si la dernière valeur est incluse.

---

Depuis C99, l'en-tête `stdbool.h` fournit le type `bool` et les constantes `true` (`1`) et `false` (`0`) :
```c
#include <stdbool.h>

bool ready = true;
bool done = count == 10;
```
Un `bool` reste un entier en interne : l'afficher avec `%d` montre `1` ou `0`, et il fonctionne avec `&&`, `||` et `!` comme n'importe quel résultat de comparaison.
Utiliser `bool` rend l'intention d'une fonction plus claire que de retourner un simple `int`.

---

Un paramètre `bool` peut être utilisé directement comme opérande de `&&` ou `||`, sans le comparer à `true` : écrivez `age >= 18 && citizen`, pas `citizen == true`.

---

Quand une condition mélange `&&` et `||`, ajoutez des parenthèses autour de chaque groupe même quand la priorité ferait déjà ce qu'il faut : cela rend la règle lisible d'un coup d'œil.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
