Le C n'a pas de type string dédié : une **chaîne** est un tableau de `char` qui se termine par un caractère spécial, le **caractère de fin de chaîne** `'\0'`.
La façon la plus simple d'en créer une est un littéral de chaîne entre guillemets doubles :
```c
char name[] = "Codigo";
```
Le compilateur compte les caractères et ajoute le `'\0'` à la fin pour vous.
Pour afficher une chaîne, utilisez le format `%s` :
```c
printf("%s\n", name);
// affiche "Codigo"
```

---

Le caractère de fin de chaîne prend de la place en mémoire : le littéral `"hi"` occupe 3 octets, `'h'`, `'i'` et `'\0'`.
Quand vous déclarez vous-même la taille, laissez toujours de la place pour lui :
```c
char word[6] = "hello"; // 5 lettres + '\0'
```
Sans le terminateur, le C n'a aucun moyen de savoir où se termine la chaîne.

---

L'en-tête `string.h` fournit des fonctions qui travaillent sur les chaînes.
`strlen` retourne le nombre de caractères avant le caractère de fin de chaîne (le terminateur lui-même n'est pas compté) :
```c
strlen("hello"); // 5
```
Une fonction qui reçoit une chaîne déclare le paramètre comme `char *text`, un pointeur vers le premier caractère.
Dans ces exercices, `string.h` et `ctype.h` sont déjà inclus au-dessus de votre code.

---

Puisqu'une chaîne est un tableau, chaque caractère a un indice commençant à `0` :
```c
char word[] = "Coding";
word[0]; // 'C'
word[5]; // 'g'
```
Un seul caractère s'affiche avec `%c`. Les caractères peuvent aussi être remplacés :
```c
word[0] = 'K'; // word vaut maintenant "Koding"
```

---

Comme toute chaîne se termine par `'\0'`, vous pouvez la parcourir sans connaître sa longueur à l'avance : continuez tant que le caractère actuel n'est pas le terminateur.
```c
for (int i = 0; text[i] != '\0'; i++) {
    printf("%c\n", text[i]);
}
```

---

Un tableau ne peut pas être assigné avec `=` après sa déclaration :
```c
char copy[20];
copy = "Codigo"; // erreur
```
Pour copier une chaîne, utilisez `strcpy(destination, source)` de `string.h`.
La destination doit être assez grande pour contenir tous les caractères plus le `'\0'`.

---

`strcat(destination, source)` ajoute `source` à la fin de `destination` :
```c
char text[20] = "Hello";
strcat(text, " World");
// text vaut maintenant "Hello World"
```
Comme avec `strcpy`, le tableau de destination doit avoir assez de place pour le résultat.

---

Deux chaînes ne peuvent pas être comparées avec `==` : cela comparerait leurs adresses en mémoire, pas leurs caractères.
Utilisez plutôt `strcmp(first, second)`, qui retourne `0` quand les deux chaînes contiennent exactement les mêmes caractères :
```c
strcmp("cat", "cat"); // 0
strcmp("cat", "dog"); // pas 0
```

---

`strcmp` compare les chaînes caractère par caractère en utilisant leurs codes de caractère.
Le résultat est négatif quand la première chaîne vient avant la seconde, positif quand elle vient après, et `0` quand elles sont égales :
```c
strcmp("a", "b"); // négatif
strcmp("b", "a"); // positif
```

---

`strncpy(destination, source, n)` copie au maximum `n` caractères.
Si `source` est plus longue que `n`, aucun `'\0'` n'est écrit : vous devez terminer le résultat vous-même.
```c
char prefix[10];
strncpy(prefix, "Codigo", 3);
prefix[3] = '\0'; // prefix vaut "Cod"
```

---

L'en-tête `ctype.h` fournit des fonctions qui travaillent sur un seul caractère.
`toupper(c)` retourne la version majuscule d'une lettre et `tolower(c)` la version minuscule ; tout autre caractère est retourné inchangé :
```c
char letter = toupper('a'); // 'A'
```

---

Une chaîne est passée à une fonction en tant que pointeur, donc une fonction recevant `char *text` peut modifier directement les caractères de l'appelant.
Combiner une boucle jusqu'à `'\0'` avec `toupper` convertit toute une chaîne :
```c
text[i] = toupper(text[i]);
```

---

`sprintf` fonctionne comme `printf`, mais écrit le texte formaté dans un tableau de caractères au lieu de l'écran :
```c
char buffer[30];
sprintf(buffer, "%d items", 3); // buffer vaut "3 items"
```
Le tampon doit être assez grand pour tout le texte et son `'\0'`.

---

`sprintf` est un moyen pratique de transformer un nombre en texte : une fois dans un tampon, chaque fonction de chaîne peut le manipuler.
