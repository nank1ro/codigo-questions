Un **struct** agrupa valores relacionados de distintos tipos en un único tipo nuevo. Cada valor que contiene se llama **miembro**.
La declaración enumera los miembros entre llaves y termina con punto y coma; crea el tipo `struct Point`, pero todavía ninguna variable:
```c
struct Point {
    int x;
    int y;
};
```
Una variable de ese tipo se declara con `struct Point`, y sus miembros pueden inicializarse **en orden** con llaves, como un array:
```c
struct Point p = {3, 4}; // x vale 3, y vale 4
```
Los miembros se leen y se escriben con el operador **punto** `.`:
```c
printf("%d\n", p.x); // imprime "3"
p.y = 10;
```

---

Inicializar los miembros en orden es frágil: si el struct gana un miembro, cada inicializador se desplaza. Desde C99 un **inicializador designado** nombra cada miembro con un punto, en cualquier orden:
```c
struct Point p = {.y = 4, .x = 3};
```
Los miembros que no se enumeran se ponen a `0`, así que `{.y = 5}` deja `x` igual a `0`. Esto es distinto de una variable declarada sin ningún inicializador, `struct Point q;`, cuyos miembros contienen **basura** hasta que les asignas algo:
```c
struct Point q;
q.x = 1;
q.y = 2;
```

---

Un struct puede pasarse a una función como cualquier otro valor. El parámetro se declara con el nombre completo del tipo, y la función lee los miembros con `.`:
```c
struct Point { int x; int y; };

int sum(struct Point p) {
    return p.x + p.y;
}
```
El struct debe declararse **antes** de la función que lo usa, para que el compilador ya conozca sus miembros.

---

Escribir `struct Point` cada vez es verboso. Con `typedef` le das al struct un nombre de tipo corto, y el struct en sí puede quedarse anónimo:
```c
typedef struct {
    double celsius;
} Temperature;

Temperature t = {21.5};
```
El nuevo nombre `Temperature` se usa por sí solo, sin la palabra clave `struct` delante. Es la forma más habitual de declarar structs en programas reales.

---

Un miembro puede ser a su vez un struct. Un segmento, por ejemplo, está formado por dos puntos:
```c
typedef struct { int x; int y; } Point;

typedef struct {
    Point start;
    Point end;
} Segment;
```
El struct interno se inicializa con su propio par de llaves, y a sus miembros se llega encadenando el operador punto:
```c
Segment s = {{1, 2}, {5, 2}};
printf("%d\n", s.end.x); // imprime "5"
```

---

Los structs pueden guardarse en un array como cualquier otro tipo. Cada elemento se inicializa con sus propias llaves, y un bucle los recorre uno a uno, indexando primero y usando el punto después:
```c
Point path[3] = {{0, 0}, {2, 1}, {4, 3}};

for (int i = 0; i < 3; i++) {
    printf("%d\n", path[i].y);
}
```

---

Un array de structs se pasa a una función igual que un array de números: el parámetro se escribe `Item items[]` y, como el array no lleva consigo su longitud, el tamaño se pasa por separado:
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

Cuando un struct se pasa a una función **por valor**, la función recibe una **copia**. Cambiar un miembro del parámetro cambia solo la copia, y la variable de quien llama queda como estaba:
```c
void reset(Point p) {
    p.x = 0; // cambia la copia
}
```
Para que una función pueda modificar el struct de quien llama, pasa su **dirección** con `&` y declara el parámetro como **puntero**, `Point *p`. El puntero se refiere a la variable original en lugar de a una copia:
```c
void reset(Point *p) { ... }

reset(&origin);
```
Copiar también cuesta tiempo con structs grandes, así que los punteros son la opción habitual incluso cuando no se modifica nada.

---

A través de un puntero se llega a los miembros con el operador **flecha** `->` en lugar del punto:
```c
void grow(Box *b) {
    b->size = b->size * 2;
}
```
`b->size` es un atajo para `(*b).size`: primero sigues el puntero y después tomas el miembro. El punto solo funciona sobre un struct, la flecha solo sobre un puntero a struct.
Quien llama pasa la dirección de su variable con `&`, y el cambio hecho a través del puntero se ve después de la llamada.

---

Una función que recibe un puntero a un struct puede actualizar el valor original en el sitio. Es la forma estándar de escribir funciones "modificadoras" en C, donde el primer parámetro es el struct que hay que cambiar y los demás son los datos que aplicar:
```c
void set_number(Player *p, int new_number) {
    p->number = new_number;
}
```
La lectura y la escritura pasan por la misma flecha: `p->score += 10` suma al miembro del struct al que se refiere el puntero.

---

Una función también puede **devolver** un struct. Constrúyelo en una variable local y devuélvelo; quien llama recibe una copia del valor completo:
```c
Point make_point(int x, int y) {
    Point p = {x, y};
    return p;
}

Point origin = make_point(0, 0);
```
Así es como C devuelve más de un valor desde una función: empaquetándolos en un struct.

---

`sizeof` también funciona con structs, y es la forma correcta de saber cuánta memoria ocupa uno:
```c
printf("%zu\n", sizeof(Point));
```
El tamaño es **al menos** la suma de los tamaños de los miembros. Puede ser mayor, porque el compilador puede insertar bytes de **relleno** (padding) sin usar para que cada miembro quede en una dirección adecuada a su tipo: `struct { char c; int n; }` suele ocupar `8` bytes, no `5`. Nunca escribas a mano el tamaño de un struct; pregúntaselo a `sizeof`.

---

Los structs no se pueden comparar con `==`: escribir `a == b` sobre dos structs es un **error de compilación**. Compáralos **miembro a miembro**, combinando los resultados con `&&`:
```c
bool same_size(Rectangle a, Rectangle b) {
    return a.width == b.width && a.height == b.height;
}
```
Lo mismo vale para `<` y `>`: tú decides qué miembro define el orden.

---

Un struct suele contener texto, guardado como un miembro array de `char` de tamaño fijo:
```c
typedef struct {
    char name[20];
    int age;
} Person;
```
Un miembro array no puede asignarse con `=` después de la declaración: `p.name = "Ann"` no compila. Copia el texto dentro con `strcpy` de `string.h`, pasando el miembro como destino:
```c
Person p;
strcpy(p.name, "Ann");
p.age = 30;
```
Solo un inicializador con llaves en la declaración acepta la cadena directamente: `Person p = {"Ann", 30};`.

---

`printf` no tiene ningún especificador para un struct entero. La solución habitual es una función pequeña que imprime los miembros con un formato fijo, para que todo el programa muestre el valor de la misma manera:
```c
void print_person(Person p) {
    printf("%s (%d)\n", p.name, p.age);
}
```

---

Juntándolo todo: una función que recibe un puntero a un struct puede actualizar un miembro de texto con `strcpy` a través de la flecha, ya que `item->name` es el array de `char` que está dentro del struct original:
```c
void set_title(Book *book, char *title) {
    strcpy(book->title, title);
}
```
Recuerda añadir `#include <string.h>` al principio de tu código para usar `strcpy`.
