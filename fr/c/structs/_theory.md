Une **struct** regroupe des valeurs liées, de types différents, dans un seul type nouveau. Chaque valeur qu'elle contient s'appelle un **membre**.
La déclaration énumère les membres entre accolades et se termine par un point-virgule ; elle crée le type `struct Point`, mais pas encore de variable :
```c
struct Point {
    int x;
    int y;
};
```
Une variable de ce type se déclare avec `struct Point`, et ses membres peuvent être initialisés **dans l'ordre** avec des accolades, comme un tableau :
```c
struct Point p = {3, 4}; // x vaut 3, y vaut 4
```
Les membres se lisent et s'écrivent avec l'opérateur **point** `.` :
```c
printf("%d\n", p.x); // affiche "3"
p.y = 10;
```

---

Initialiser les membres dans l'ordre est fragile : si la struct gagne un membre, chaque initialiseur se décale. Depuis C99, un **initialiseur désigné** nomme chaque membre avec un point, dans n'importe quel ordre :
```c
struct Point p = {.y = 4, .x = 3};
```
Les membres non listés sont mis à `0`, donc `{.y = 5}` donne `x` égal à `0`. C'est différent d'une variable déclarée sans aucun initialiseur, `struct Point q;`, dont les membres contiennent des **valeurs quelconques** tant que tu ne les affectes pas :
```c
struct Point q;
q.x = 1;
q.y = 2;
```

---

Une struct peut être passée à une fonction comme n'importe quelle autre valeur. Le paramètre se déclare avec le nom complet du type, et la fonction lit les membres avec `.` :
```c
struct Point { int x; int y; };

int sum(struct Point p) {
    return p.x + p.y;
}
```
La struct doit être déclarée **avant** la fonction qui l'utilise, pour que le compilateur connaisse déjà ses membres.

---

Écrire `struct Point` à chaque fois est verbeux. Avec `typedef`, tu donnes à la struct un nom de type court, et la struct elle-même peut rester anonyme :
```c
typedef struct {
    double celsius;
} Temperature;

Temperature t = {21.5};
```
Le nouveau nom `Temperature` s'utilise seul, sans le mot-clé `struct` devant. C'est la façon la plus courante de déclarer des structs dans les vrais programmes.

---

Un membre peut être lui-même une struct. Un segment, par exemple, est fait de deux points :
```c
typedef struct { int x; int y; } Point;

typedef struct {
    Point start;
    Point end;
} Segment;
```
La struct interne s'initialise avec sa propre paire d'accolades, et on atteint ses membres en enchaînant l'opérateur point :
```c
Segment s = {{1, 2}, {5, 2}};
printf("%d\n", s.end.x); // affiche "5"
```

---

Les structs peuvent être stockées dans un tableau comme n'importe quel autre type. Chaque élément s'initialise avec ses propres accolades, et une boucle les parcourt une par une, en indexant d'abord puis en utilisant le point :
```c
Point path[3] = {{0, 0}, {2, 1}, {4, 3}};

for (int i = 0; i < 3; i++) {
    printf("%d\n", path[i].y);
}
```

---

Un tableau de structs se passe à une fonction exactement comme un tableau de nombres : le paramètre s'écrit `Item items[]` et, comme le tableau ne transporte pas sa longueur, la taille est passée séparément :
```c
int count_free(Item items[], int size) {
    int count = 0;
    for (int i = 0; i < size; i++) {
        if (items[i].price == 0) {
            count++;
        }
    }
    return count;
}
```

---

Quand une struct est passée à une fonction **par valeur**, la fonction en reçoit une **copie**. Modifier un membre du paramètre ne change que la copie, et la variable de l'appelant reste telle qu'elle était :
```c
void reset(Point p) {
    p.x = 0; // modifie la copie
}
```
Pour permettre à une fonction de modifier la struct de l'appelant, passe son **adresse** avec `&` et déclare le paramètre comme un **pointeur**, `Point *p`. Le pointeur désigne la variable d'origine au lieu d'une copie :
```c
void reset(Point *p) { ... }

reset(&origin);
```
La copie coûte aussi du temps pour les grosses structs, donc les pointeurs sont le choix habituel même quand rien n'est modifié.

---

À travers un pointeur, on atteint les membres avec l'opérateur **flèche** `->` au lieu du point :
```c
void grow(Box *b) {
    b->size = b->size * 2;
}
```
`b->size` est un raccourci pour `(*b).size` : d'abord tu suis le pointeur, ensuite tu prends le membre. Le point ne fonctionne que sur une struct, la flèche seulement sur un pointeur vers une struct.
L'appelant passe l'adresse de sa variable avec `&`, et la modification faite à travers le pointeur est visible après l'appel.

---

Une fonction qui reçoit un pointeur vers une struct peut mettre à jour la valeur d'origine sur place. C'est la façon standard d'écrire des fonctions « modificatrices » en C, où le premier paramètre est la struct à changer et les autres sont les données à appliquer :
```c
void set_number(Player *p, int new_number) {
    p->number = new_number;
}
```
La lecture et l'écriture passent par la même flèche : `p->score += 10` ajoute au membre de la struct désignée par le pointeur.

---

Une fonction peut aussi **renvoyer** une struct. Construis-la dans une variable locale et renvoie-la ; l'appelant reçoit une copie de la valeur entière :
```c
Point make_point(int x, int y) {
    Point p = {x, y};
    return p;
}

Point origin = make_point(0, 0);
```
C'est ainsi que C renvoie plus d'une valeur depuis une fonction : en les empaquetant dans une struct.

---

`sizeof` fonctionne aussi sur les structs, et c'est la bonne façon de savoir combien de mémoire l'une d'elles occupe :
```c
printf("%zu\n", sizeof(Point));
```
La taille vaut **au moins** la somme des tailles des membres. Elle peut être plus grande, car le compilateur peut insérer des octets de **remplissage** (padding) inutilisés pour que chaque membre se trouve à une adresse adaptée à son type : `struct { char c; int n; }` occupe généralement `8` octets, pas `5`. N'écris jamais en dur la taille d'une struct ; demande-la à `sizeof`.

---

Les structs ne peuvent pas être comparées avec `==` : écrire `a == b` sur deux structs est une **erreur de compilation**. Compare-les plutôt **membre par membre**, en combinant les résultats avec `&&` :
```c
bool same_size(Rectangle a, Rectangle b) {
    return a.width == b.width && a.height == b.height;
}
```
La même chose vaut pour `<` et `>` : c'est toi qui décides quel membre définit l'ordre.

---

Une struct contient souvent du texte, stocké dans un membre tableau de `char` de taille fixe :
```c
typedef struct {
    char name[20];
    int age;
} Person;
```
Un membre tableau ne peut pas être affecté avec `=` après la déclaration : `p.name = "Ann"` ne compile pas. Copie le texte dedans avec `strcpy` de `string.h`, en passant le membre comme destination :
```c
Person p;
strcpy(p.name, "Ann");
p.age = 30;
```
Seul un initialiseur entre accolades à la déclaration accepte la chaîne directement : `Person p = {"Ann", 30};`.

---

`printf` n'a pas de spécificateur pour une struct entière. La solution habituelle est une petite fonction qui affiche les membres dans un format fixe, pour que chaque partie du programme montre la valeur de la même façon :
```c
void print_person(Person p) {
    printf("%s (%d)\n", p.name, p.age);
}
```

---

Pour tout mettre ensemble : une fonction qui reçoit un pointeur vers une struct peut mettre à jour un membre texte avec `strcpy` à travers la flèche, puisque `item->name` est le tableau de `char` situé dans la struct d'origine :
```c
void set_title(Book *book, char *title) {
    strcpy(book->title, title);
}
```
N'oublie pas d'ajouter `#include <string.h>` en haut de ton code pour utiliser `strcpy`.
