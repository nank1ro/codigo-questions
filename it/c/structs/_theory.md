Una **struct** raggruppa valori correlati di tipi diversi in un unico nuovo tipo. Ogni valore al suo interno si chiama **membro**.
La dichiarazione elenca i membri tra parentesi graffe e termina con un punto e virgola; crea il tipo `struct Point`, ma non ancora una variabile:
```c
struct Point {
    int x;
    int y;
};
```
Una variabile di quel tipo si dichiara con `struct Point` e i suoi membri possono essere inizializzati **in ordine** con le graffe, come un array:
```c
struct Point p = {3, 4}; // x vale 3, y vale 4
```
I membri si leggono e si scrivono con l'operatore **punto** `.`:
```c
printf("%d\n", p.x); // stampa "3"
p.y = 10;
```

---

Inizializzare i membri in ordine è fragile: se la struct acquista un membro, ogni inizializzatore si sposta. Da C99 un **inizializzatore designato** nomina ogni membro con un punto, in qualsiasi ordine:
```c
struct Point p = {.y = 4, .x = 3};
```
I membri non elencati vengono impostati a `0`, quindi `{.y = 5}` dà `x` uguale a `0`. È diverso da una variabile dichiarata senza alcun inizializzatore, `struct Point q;`, i cui membri contengono **valori casuali** finché non li assegni:
```c
struct Point q;
q.x = 1;
q.y = 2;
```

---

Una struct può essere passata a una funzione come qualsiasi altro valore. Il parametro si dichiara con il nome completo del tipo e la funzione legge i membri con `.`:
```c
struct Point { int x; int y; };

int sum(struct Point p) {
    return p.x + p.y;
}
```
La struct deve essere dichiarata **prima** della funzione che la usa, così il compilatore ne conosce già i membri.

---

Scrivere `struct Point` ogni volta è verboso. Con `typedef` dai alla struct un nome di tipo breve, e la struct stessa può restare anonima:
```c
typedef struct {
    double celsius;
} Temperature;

Temperature t = {21.5};
```
Il nuovo nome `Temperature` si usa da solo, senza la parola chiave `struct` davanti. È il modo più comune di dichiarare le struct nei programmi reali.

---

Un membro può essere a sua volta una struct. Un segmento, per esempio, è fatto di due punti:
```c
typedef struct { int x; int y; } Point;

typedef struct {
    Point start;
    Point end;
} Segment;
```
La struct interna si inizializza con la sua coppia di graffe e i suoi membri si raggiungono concatenando l'operatore punto:
```c
Segment s = {{1, 2}, {5, 2}};
printf("%d\n", s.end.x); // stampa "5"
```

---

Le struct possono essere memorizzate in un array come qualsiasi altro tipo. Ogni elemento si inizializza con le proprie graffe e un ciclo le visita una a una, prima indicizzando e poi usando il punto:
```c
Point path[3] = {{0, 0}, {2, 1}, {4, 3}};

for (int i = 0; i < 3; i++) {
    printf("%d\n", path[i].y);
}
```

---

Un array di struct si passa a una funzione esattamente come un array di numeri: il parametro si scrive `Item items[]` e, poiché l'array non porta con sé la propria lunghezza, la dimensione si passa separatamente:
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

Quando una struct viene passata a una funzione **per valore**, la funzione ne riceve una **copia**. Modificare un membro del parametro cambia solo la copia e la variabile del chiamante resta com'era:
```c
void reset(Point p) {
    p.x = 0; // cambia la copia
}
```
Per permettere a una funzione di modificare la struct del chiamante, passa il suo **indirizzo** con `&` e dichiara il parametro come **puntatore**, `Point *p`. Il puntatore si riferisce alla variabile originale invece che a una copia:
```c
void reset(Point *p) { ... }

reset(&origin);
```
Copiare costa anche tempo per struct grandi, quindi i puntatori sono la scelta abituale anche quando non si modifica nulla.

---

Attraverso un puntatore i membri si raggiungono con l'operatore **freccia** `->` invece che con il punto:
```c
void grow(Box *b) {
    b->size = b->size * 2;
}
```
`b->size` è una scorciatoia per `(*b).size`: prima segui il puntatore, poi prendi il membro. Il punto funziona solo su una struct, la freccia solo su un puntatore a struct.
Il chiamante passa l'indirizzo della sua variabile con `&`, e la modifica fatta attraverso il puntatore è visibile dopo la chiamata.

---

Una funzione che riceve un puntatore a una struct può aggiornare il valore originale sul posto. È il modo standard di scrivere funzioni "modificatrici" in C, dove il primo parametro è la struct da cambiare e gli altri sono i dati da applicare:
```c
void set_number(Player *p, int new_number) {
    p->number = new_number;
}
```
Lettura e scrittura passano dalla stessa freccia: `p->score += 10` aggiunge al membro della struct a cui il puntatore si riferisce.

---

Una funzione può anche **restituire** una struct. Costruiscila in una variabile locale e restituiscila; il chiamante riceve una copia dell'intero valore:
```c
Point make_point(int x, int y) {
    Point p = {x, y};
    return p;
}

Point origin = make_point(0, 0);
```
È così che in C si restituisce più di un valore da una funzione: impacchettandoli in una struct.

---

`sizeof` funziona anche sulle struct ed è il modo giusto per sapere quanta memoria ne occupa una:
```c
printf("%zu\n", sizeof(Point));
```
La dimensione è **almeno** la somma delle dimensioni dei membri. Può essere maggiore, perché il compilatore può inserire byte di **padding** inutilizzati affinché ogni membro si trovi a un indirizzo adatto al suo tipo: `struct { char c; int n; }` di solito occupa `8` byte, non `5`. Non scrivere mai a mano la dimensione di una struct; chiedila a `sizeof`.

---

Le struct non si possono confrontare con `==`: scrivere `a == b` su due struct è un **errore di compilazione**. Confrontale invece **membro per membro**, combinando i risultati con `&&`:
```c
bool same_size(Rectangle a, Rectangle b) {
    return a.width == b.width && a.height == b.height;
}
```
Lo stesso vale per `<` e `>`: sei tu a decidere quale membro definisce l'ordine.

---

Una struct contiene spesso del testo, memorizzato come membro array di `char` di dimensione fissa:
```c
typedef struct {
    char name[20];
    int age;
} Person;
```
Un membro array non può essere assegnato con `=` dopo la dichiarazione: `p.name = "Ann"` non compila. Copia il testo al suo interno con `strcpy` da `string.h`, passando il membro come destinazione:
```c
Person p;
strcpy(p.name, "Ann");
p.age = 30;
```
Solo un inizializzatore con graffe alla dichiarazione accetta la stringa direttamente: `Person p = {"Ann", 30};`.

---

`printf` non ha uno specificatore per un'intera struct. La soluzione abituale è una piccola funzione che stampa i membri in un formato fisso, così ogni parte del programma mostra il valore allo stesso modo:
```c
void print_person(Person p) {
    printf("%s (%d)\n", p.name, p.age);
}
```

---

Mettendo tutto insieme: una funzione che riceve un puntatore a una struct può aggiornare un membro di testo con `strcpy` attraverso la freccia, poiché `item->name` è l'array di `char` dentro la struct originale:
```c
void set_title(Book *book, char *title) {
    strcpy(book->title, title);
}
```
Ricorda di aggiungere `#include <string.h>` in cima al tuo codice per usare `strcpy`.
