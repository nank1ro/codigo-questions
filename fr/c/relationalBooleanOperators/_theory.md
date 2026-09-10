Les **opérateurs relationnels** comparent deux valeurs. Le résultat n'est pas un type spécial : c'est un `int` qui vaut `1` quand la comparaison est vraie et `0` quand elle ne l'est pas. Le C en compte six :
```c
printf("%d\n", 5 == 5); // equal: prints "1"
printf("%d\n", 5 != 5); // not equal: prints "0"
printf("%d\n", 3 < 5);  // less than: prints "1"
printf("%d\n", 3 > 5);  // greater than: prints "0"
printf("%d\n", 5 <= 5); // less than or equal: prints "1"
printf("%d\n", 4 >= 5); // greater than or equal: prints "0"
```
Comme le résultat est un `int`, il s'affiche avec `%d` et peut être stocké dans une variable `int` comme n'importe quel autre nombre.

---

Une fonction peut retourner une comparaison directement : l'appelant reçoit `1` ou `0`.
```c
int is_big(int n) {
    return n > 100;
}

printf("%d\n", is_big(250)); // prints "1"
```
Choisir entre `>` et `>=` (ou `<` et `<=`) décide si la valeur limite est comprise : `n >= 100` vaut `1` pour `100`, `n > 100` vaut `0`.

---

L'erreur la plus courante en C consiste à écrire `=` là où `==` était prévu. Un seul `=` est une **affectation**, et en C une affectation est une expression dont la valeur est la valeur qui a été assignée :
```c
int x = 3;
printf("%d\n", x == 7); // compares: prints "0", x is still 3
printf("%d\n", x = 7);  // assigns: prints "7", x is now 7
```
Le code avec `=` compile quand même, donc une condition écrite `if (x = 0)` met silencieusement `x` à `0` au lieu de le tester. La plupart des compilateurs affichent un avertissement pour cela : lisez-le.

---

Les **opérateurs logiques** combinent des conditions. L'opérateur **et** `&&` donne `1` seulement quand les deux côtés sont vrais, l'opérateur **ou** `||` donne `1` quand au moins un côté est vrai :
```c
int t = 25;
printf("%d\n", t > 20 && t < 30); // prints "1"
printf("%d\n", t < 20 || t > 30); // prints "0"
```
En C, **toute valeur non nulle compte comme vraie** et seul `0` compte comme faux, donc `5 && 1` vaut `1` et `0 || -3` vaut `1`. Le résultat de `&&` et `||` est toujours exactement `1` ou `0`.

---

Une variable qui contient `0` ou une valeur non nulle peut servir de condition à elle seule : `holiday` seul signifie « holiday est non nulle », inutile d'écrire `holiday != 0`.
```c
int is_open(int weekday, int holiday) {
    return weekday && !holiday;
}
```
L'opérateur **non** `!` inverse une condition : `!0` vaut `1` et `!` appliqué à toute valeur non nulle vaut `0`.

---

Puisque `!` transforme toute valeur non nulle en `0` et `0` en `1`, l'appliquer deux fois normalise une valeur exactement à `0` ou `1` : `!!42` vaut `1`, `!!0` vaut `0`.
```c
int count = 3;
printf("%d %d\n", !count, !!count); // prints "0 1"
```
C'est pratique quand une fonction retourne un nombre non nul quelconque et que vous voulez un `1` propre.

---

Depuis C99, l'en-tête `stdbool.h` fournit le type `bool` et les constantes `true` (qui vaut `1`) et `false` (qui vaut `0`) :
```c
#include <stdbool.h>

bool open = true;
bool full = 3 > 5;
printf("%d %d\n", open, full); // prints "1 0"
```
Un `bool` reste un entier sous le capot : il s'affiche avec `%d`, et il fonctionne avec `&&`, `||` et `!` exactement comme un résultat de comparaison. Il rend simplement l'intention plus claire qu'un `int` ordinaire.

---

Une fonction qui répond à une question oui/non devrait retourner `bool`. Un paramètre `bool` est déjà une condition, utilisez-le donc directement comme opérande de `&&` ou `||` : écrivez `age >= 18 && citizen`, pas `citizen == true`.
```c
bool can_enter(int age, bool member) {
    return age >= 16 && member;
}
```
`stdbool.h` est déjà inclus au-dessus de votre code dans ces exercices.

---

`&&` et `||` utilisent l'**évaluation en court-circuit** : ils s'arrêtent dès que le résultat est connu.
- avec `&&`, si le côté gauche vaut `0`, le côté droit n'est jamais évalué
- avec `||`, si le côté gauche est non nul, le côté droit n'est jamais évalué

Cela permet à une vérification à gauche de protéger une opération dangereuse à droite :
```c
int ok = count != 0 && total / count > 2;
```
Quand `count` vaut `0`, la division n'est jamais exécutée, donc le programme ne plante pas.

---

L'évaluation en court-circuit saute aussi les appels de fonction. Dans `1 || check()`, la fonction `check` n'est jamais appelée, donc tout effet de bord qu'elle produit, comme mettre à jour un compteur, ne se produit pas.
```c
int calls = 0;

int check() {
    calls++;
    return 1;
}
```
Gardez cela à l'esprit quand une fonction placée du côté droit de `&&` ou `||` fait quelque chose dont vous dépendez.

---

Les opérateurs ont une **priorité** qui décide de ce qui est calculé en premier :
1. `!` est appliqué en premier
2. puis les comparaisons relationnelles `<`, `>`, `<=`, `>=`
3. puis les comparaisons d'égalité `==`, `!=`
4. puis `&&`
5. puis `||`

Ainsi `a > 0 && a < 10` n'a pas besoin de parenthèses, et `a && b || c` signifie `(a && b) || c` car `&&` est prioritaire sur `||`. Utilisez des parenthèses pour forcer un regroupement différent ou simplement pour rendre l'intention lisible.

---

Un `char` est un petit entier, donc les caractères se comparent avec les mêmes opérateurs. Comparez avec un littéral de caractère entre guillemets simples : `"a"` avec des guillemets doubles est une chaîne, qui ne peut pas être comparée de cette façon.
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // prints "1"
```
Les caractères consécutifs comme `'0'`, `'1'`, ... `'9'` ou `'a'`, `'b'`, ... `'z'` ont des codes consécutifs, donc une vérification d'intervalle sur les caractères fonctionne exactement comme sur les nombres :
```c
bool is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

N'enchaînez pas les comparaisons comme en mathématiques. `1 <= x <= 10` compile, mais il est évalué comme `(1 <= x) <= 10` : la première comparaison donne `0` ou `1`, et cette valeur est ensuite comparée à `10`, donc l'expression entière vaut toujours `1`.
```c
int x = 20;
printf("%d\n", 1 <= x <= 10);       // prints "1" (wrong!)
printf("%d\n", 1 <= x && x <= 10);  // prints "0"
```
Écrivez toujours les deux comparaisons explicitement et joignez-les avec `&&`.

---

Quand une condition mélange `&&` et `||`, groupez chaque partie avec des parenthèses même quand la priorité ferait déjà ce qu'il faut : la règle devient lisible d'un coup d'œil.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
L'opérateur reste `%` se marie naturellement avec `==` : `n % 4 == 0` vaut `1` quand `n` est divisible par `4`.
