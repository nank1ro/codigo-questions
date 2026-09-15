Le C n'a pas d'interpolation de chaînes : le texte et les valeurs sont combinés par `printf` au moyen d'une **chaîne de format**, où chaque spécificateur `%` est remplacé par l'argument correspondant. Les spécificateurs les plus courants sont :
```c
printf("%d\n", 42);      // affiche "42" (int, %i fait la même chose)
printf("%f\n", 2.5);     // affiche "2.500000" (double, 6 décimales par défaut)
printf("%s\n", "hi");    // affiche "hi" (chaîne)
printf("%c\n", 'A');     // affiche "A" (caractère unique)
printf("%x\n", 255);     // affiche "ff" (int en hexadécimal minuscule)
printf("100%%\n");       // affiche "100%" (un signe pourcentage littéral)
```
Le spécificateur doit correspondre au type de l'argument : afficher un `double` avec `%d` ou un `int` avec `%s` ne convertit pas la valeur, cela affiche n'importe quoi ou plante.

---

`sprintf` fonctionne exactement comme `printf`, mais au lieu d'écrire à l'écran il écrit le texte formaté dans un tableau de `char`, appelé **tampon**, suivi du `'\0'` terminateur :
```c
char buffer[32];
sprintf(buffer, "%d-%d", 3, 7);
printf("%s\n", buffer); // affiche "3-7"
```
Le tampon doit être déclaré avant l'appel et doit être assez grand pour tout le texte plus le terminateur, sinon `sprintf` écrit au-delà de sa fin.

---

Une fonction qui construit une chaîne reçoit généralement le tampon en paramètre et le remplit avec `sprintf`. Le tableau appartient à l'appelant, et après l'appel il peut lire le résultat :
```c
void greet(char *out, char *name) {
    sprintf(out, "Hello, %s!", name);
}

char message[32];
greet(message, "Ada");
printf("%s\n", message); // affiche "Hello, Ada!"
```
Dans ces exercices `string.h` est déjà inclus au-dessus de ton code, donc `strcmp` peut servir à comparer le résultat.

---

`%x` affiche un entier en hexadécimal avec des lettres minuscules, et `%X` fait la même chose avec des lettres majuscules. `%c` prend un code de caractère entier et affiche le caractère qu'il représente, donc `%c` avec `65` affiche `A` :
```c
printf("%x %X %c\n", 31, 31, 66); // affiche "1f 1F B"
```

---

Un nombre entre `%` et la lettre fixe la **largeur** minimale du champ. La valeur est complétée par des espaces à gauche, et les **drapeaux** placés juste après le `%` changent ce remplissage :
```c
printf("[%5d]\n", 42);  // affiche "[   42]" aligné à droite sur 5 colonnes
printf("[%-5d]\n", 42); // affiche "[42   ]" le drapeau - aligne à gauche
printf("[%05d]\n", 42); // affiche "[00042]" le drapeau 0 complète avec des zéros
printf("[%+d]\n", 42);  // affiche "[+42]" le drapeau + affiche toujours le signe
```
Une valeur plus longue que la largeur n'est jamais coupée, le champ s'agrandit simplement.

---

La largeur et les drapeaux fonctionnent avec tous les spécificateurs, donc `%02x` affiche un entier en hexadécimal complété par des zéros sur deux chiffres. C'est ainsi que les couleurs s'écrivent sous la forme `#rrggbb` :
```c
printf("%02x\n", 5);   // affiche "05"
printf("%02x\n", 255); // affiche "ff"
```

---

Un point suivi d'un nombre fixe la **précision**. Pour `%f` c'est le nombre de décimales, arrondi ; pour `%s` c'est le nombre maximal de caractères affichés :
```c
printf("%.2f\n", 3.14159);    // affiche "3.14"
printf("%.3s\n", "formatting"); // affiche "for"
```
La largeur et la précision peuvent être combinées : `%8.2f` affiche deux décimales alignées à droite sur 8 colonnes.

---

La précision est la façon habituelle de contrôler l'apparence d'un `double` dans une chaîne. Un rapport comme `0.425` devient un pourcentage en le multipliant par `100` et en affichant une décimale suivie de `%%` :
```c
sprintf(out, "%.1f%%", 0.425 * 100); // out vaut "42.5%"
```

---

`sprintf` et `printf` **renvoient** le nombre de caractères écrits, sans compter le `'\0'` terminateur. C'est la longueur de la chaîne qui vient d'être construite, sans appel séparé à `strlen` :
```c
char buffer[32];
int length = sprintf(buffer, "%d-%d", 3, 7);
printf("%d\n", length); // affiche "3"
```

---

`sprintf` ne sait pas quelle est la taille du tampon. `snprintf` prend la taille du tampon comme deuxième argument et n'écrit jamais plus de `size - 1` caractères plus le `'\0'`, en coupant le texte si nécessaire. Sa valeur de retour est la longueur qu'aurait eue le texte **complet**, donc un résultat supérieur ou égal à `size` signifie que la sortie a été tronquée :
```c
char buffer[8];
int n = snprintf(buffer, sizeof buffer, "%s", "formatting");
printf("%s %d\n", buffer, n); // affiche "formatt 10"
```
`sizeof buffer` donne la taille du tableau en octets, ce qui pour un tableau de `char` correspond à son nombre d'éléments.

---

Comparer la valeur de retour de `snprintf` avec la taille du tampon indique si tout a tenu. C'est le motif sûr pour construire des chaînes de longueur inconnue :
```c
int n = snprintf(out, size, "%s", text);
if (n >= size) {
    // out ne contient que les size - 1 premiers caractères de text
}
```

---

Une chaîne peut être construite en plusieurs étapes en écrivant chaque morceau juste après le précédent. La valeur de retour indique où le texte se termine, donc `buffer + n` est l'adresse du terminateur et le `sprintf` suivant peut continuer à partir de là :
```c
char buffer[32];
int n = sprintf(buffer, "%s", "Hello");
n += sprintf(buffer + n, ", %s", "world"); // buffer vaut "Hello, world", n vaut 12
```
Ajouter chaque valeur de retour à `n` le maintient égal à la longueur totale du texte construit jusqu'ici.

---

Les chaînes peuvent aussi être combinées sans chaîne de format. `strcat` de `string.h` ajoute une copie de son deuxième argument à la fin du premier, qui doit avoir assez de place libre, et `strncat` ajoute au plus un nombre donné de caractères :
```c
char text[32] = "Hi";
strcat(text, "!!!");        // text vaut "Hi!!!"
strncat(text, "abcdef", 2); // text vaut "Hi!!!ab"
```
Les deux ajoutent toujours le `'\0'` terminateur après les caractères ajoutés.

---

Quand il n'y a rien à formater, `puts` affiche une chaîne suivie d'un saut de ligne. Contrairement à `printf` il n'interprète pas `%`, donc le texte est affiché exactement tel qu'il est écrit :
```c
puts("Done");      // affiche "Done" et un saut de ligne
puts("50% off");   // affiche "50% off" et un saut de ligne
printf("50% off"); // non défini : % off n'est pas un spécificateur valide
```
`puts` est le bon choix pour du texte fixe, et `printf` quand des valeurs doivent être insérées.

---

`strncat` est utile quand seule une partie d'une chaîne doit être ajoutée, ou quand le morceau ajouté doit être limité à une longueur maximale :
```c
char name[16] = "file";
strncat(name, ".backup", 3); // name vaut "file.ba"
```
Quand la limite est plus grande que la chaîne, la chaîne entière est ajoutée.

---

Tout ensemble : une ligne de rapport combine un champ de texte aligné à gauche, un séparateur et un nombre aligné à droite avec un nombre fixe de décimales, écrite avec `snprintf` pour ne jamais déborder du tampon :
```c
snprintf(out, size, "%-6s|%5.1f", "Ada", 9.5); // out vaut "Ada   |  9.5"
```
Tant que chaque valeur tient dans sa largeur, toutes les lignes ont la même longueur, donc les colonnes s'alignent quand les lignes sont affichées les unes sous les autres.
