Une **liste chaînée** stocke les valeurs dans des **nœuds** distincts dispersés en mémoire : chaque nœud contient une valeur et un pointeur vers le nœud suivant, et le dernier pointe vers `NULL`. Le pointeur à l'intérieur fait référence au type en cours de déclaration, la struct a donc besoin d'une **étiquette** pour se nommer elle-même ; le nom du `typedef` n'existe pas encore à l'intérieur des accolades :
```c
typedef struct Node {
    int value;
    struct Node *next;
} Node;
```
Les nœuds sont chaînés en stockant l'adresse de l'un dans le `next` d'un autre, et les membres du nœud pointé sont atteints avec la flèche :
```c
Node second = {2, NULL};
Node first = {1, &second};
printf("%d\n", first.next->value); // prints "2"
```

---

Les nœuds déclarés comme variables locales disparaissent lorsque leur fonction se termine, les listes sont donc construites sur le **tas** avec `malloc` de `stdlib.h`. Il réserve le nombre d'octets demandé et renvoie leur adresse, ou `NULL` lorsque la mémoire est épuisée ; `sizeof(Node)` est la bonne quantité pour un nœud :
```c
Node *node = malloc(sizeof(Node));
node->value = 5;
node->next = NULL;
```
La mémoire du tas n'est jamais libérée d'elle-même : chaque nœud obtenu avec `malloc` doit être rendu avec `free(node)` dès qu'il n'est plus nécessaire. Dans ces exercices `stdlib.h` est inclus et `Node` est déclaré au-dessus de ton code.

---

Une liste est tenue par un seul pointeur vers son premier nœud, la **tête**. Tous les autres nœuds sont atteints depuis la tête en suivant `next`, et la flèche peut être chaînée : `head->next` est le deuxième nœud et `head->next->next` le troisième. Une liste vide est une tête égale à `NULL`, et le `next` du dernier nœud vaut aussi `NULL`, donc suivre une flèche de trop déréférence `NULL` et fait planter le programme.

---

Parcourir une liste, ce qu'on appelle le **parcours**, est une boucle qui part de la tête et suit `next` jusqu'à atteindre `NULL`. Une boucle `for` l'exprime en une seule ligne, avec un pointeur comme variable de boucle :
```c
for (Node *n = head; n != NULL; n = n->next) {
    printf("%d\n", n->value);
}
```
Il n'y a pas d'indice : le seul moyen d'atteindre un nœud est de passer par le pointeur stocké dans celui qui le précède.

---

Ajouter un nœud **devant** le crée, fait pointer le nouveau vers la tête actuelle et le renvoie comme nouvelle tête. L'appelant stocke le résultat dans sa variable de tête :
```c
Node *head = NULL;
head = push_front(head, 7);
head = push_front(head, 8); // the list is now 8, 7
```
Empiler sur une liste vide fonctionne de la même manière : le nouveau nœud pointe vers `NULL` et devient toute la liste.

---

Libérer une liste signifie libérer chaque nœud, une étape de parcours à la fois. Le pointeur `next` doit être sauvegardé **avant** que le nœud ne soit libéré, car un nœud libéré ne doit plus être lu, pas même son `next` :
```c
while (head != NULL) {
    Node *next = head->next;
    free(head);
    head = next;
}
```
Écrire `free(head)` puis `head = head->next` lit de la mémoire qui vient d'être libérée, ce qui est un comportement indéfini. `free(NULL)` est permis et ne fait rien, une liste vide n'a donc pas besoin de cas particulier.

---

Une liste ne stocke pas sa longueur : il faut la compter avec un parcours. La forme `while` de la boucle garde le pointeur à l'extérieur, ce qui est pratique lorsque le corps de la boucle met à jour d'autres variables :
```c
int count = 0;
Node *n = head;
while (n != NULL) {
    count++;
    n = n->next;
}
```
Pour une liste vide, le corps de la boucle ne s'exécute jamais et le compteur reste à `0`.

---

Ajouter un nœud **à la fin** demande le dernier nœud, celui dont le `next` est `NULL`. La fonction avance jusqu'à le trouver, puis y attache le nouveau nœud et renvoie la tête inchangée :
```c
Node *last = head;
while (last->next != NULL) {
    last = last->next;
}
last->next = node;
```
Lorsque la liste est vide, il n'y a pas de dernier nœud où avancer : le nouveau nœud est simplement renvoyé comme tête.

---

Rechercher dans une liste est un parcours qui compare chaque valeur et s'arrête à la première correspondance. La fonction renvoie un pointeur vers le nœud trouvé, ou `NULL` lorsqu'elle atteint la fin de la liste sans correspondance :
```c
Node *found = find(head, 5);
if (found != NULL) {
    printf("%d\n", found->value);
}
```
Renvoyer le nœud plutôt que la valeur permet à l'appelant de le modifier ou de l'utiliser comme point de départ pour une autre opération.

---

Après `free(p)`, la variable `p` contient toujours l'ancienne adresse, mais la mémoire vers laquelle elle pointe ne t'appartient plus : `p` est maintenant un **pointeur pendant** (*dangling pointer*). Lire ou écrire à travers lui, ou le libérer une seconde fois, est un comportement indéfini : le programme peut afficher l'ancienne valeur, afficher n'importe quoi ou planter, et le compilateur ne s'en plaindra pas. Lorsqu'un pointeur doit survivre au `free`, mets-le à `NULL` juste après, afin que toute utilisation ultérieure soit détectée par une vérification de `NULL`.

---

Insérer **après** un nœud donné ne demande aucun parcours : le nouveau nœud récupère le successeur de `node`, puis `node` est fait pointer vers le nouveau :
```c
new_node->next = node->next;
node->next = new_node;
```
L'ordre des deux affectations compte : mettre `node->next` en premier écraserait le seul pointeur vers le reste de la liste, et ces nœuds seraient perdus. Insérer après le dernier nœud fonctionne aussi, puisque son `next` est `NULL`.

---

Retirer le premier nœud est le miroir de `push_front` : sauvegarder l'adresse du deuxième nœud, libérer le premier et renvoyer l'adresse sauvegardée comme nouvelle tête. L'appelant stocke le résultat dans sa variable de tête :
```c
Node *next = head->next;
free(head);
return next;
```
Dépiler jusqu'à ce que la tête soit `NULL` libère toute la liste, un nœud par appel.

---

Retirer un nœud au milieu demande le nœud **précédent**, donc le parcours garde deux pointeurs : `prev`, le nœud déjà visité, et `cur`, celui en cours d'examen. Lorsque `cur` correspond, `prev->next` est fait pour le sauter et `cur` est libéré. Si la correspondance est la tête elle-même, `prev` vaut encore `NULL` et la nouvelle tête est `cur->next` :
```c
if (prev == NULL) {
    head = cur->next;
} else {
    prev->next = cur->next;
}
free(cur);
```
Lorsqu'aucun nœud ne correspond, la liste est renvoyée inchangée.

---

Inverser une liste retourne chaque pointeur `next`, sur place, avec trois pointeurs : `prev` est la partie déjà inversée, `head` le nœud en cours de traitement et `next` une copie du reste de la liste, sauvegardée avant que le lien ne soit modifié. À chaque étape, le nœud courant est fait pointer vers `prev`, puis `prev` et `head` avancent ensemble :
```c
Node *next = head->next;
head->next = prev;
prev = head;
head = next;
```
Lorsque `head` atteint `NULL`, chaque lien a été retourné et `prev` est la nouvelle tête.

---

Une liste chaînée est peu coûteuse là où un tableau l'est, et inversement. Ajouter ou retirer **devant** se réduit à quelques affectations de pointeurs, quelle que soit la longueur, alors qu'un tableau devrait décaler chaque élément. En revanche, les nœuds ne sont pas contigus, il n'y a donc pas de `list[i]` : atteindre le n-ième nœud, le dernier ou la longueur totale signifie avancer depuis la tête à travers chaque nœud intermédiaire. Les programmes qui ajoutent souvent à la fin gardent un second pointeur vers le dernier nœud, la **queue**, pour éviter ce parcours.

---

Pour tout assembler : une liste est souvent construite à partir d'un tableau. Empiler devant inverse l'ordre, donc le tableau est parcouru **à rebours**, du dernier élément au premier, et le premier élément se retrouve à la tête. Le programme affiche ensuite la liste avec un parcours et la libère nœud par nœud, afin que chaque `malloc` soit apparié à un `free`.
