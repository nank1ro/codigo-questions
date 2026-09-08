A **struct** groups related values of different types into a single new type. Each value inside it is called a **member**.
The declaration lists the members between braces and ends with a semicolon; it creates the type `struct Point` but no variable yet:
```c
struct Point {
    int x;
    int y;
};
```
A variable of that type is declared with `struct Point`, and its members can be initialised **in order** with braces, like an array:
```c
struct Point p = {3, 4}; // x is 3, y is 4
```
Members are read and written with the **dot** operator `.`:
```c
printf("%d\n", p.x); // prints "3"
p.y = 10;
```

---

Initialising members in order is fragile: if the struct gains a member, every initialiser shifts. Since C99 a **designated initialiser** names each member with a dot, in any order:
```c
struct Point p = {.y = 4, .x = 3};
```
Members that are not listed are set to `0`, so `{.y = 5}` gives `x` equal to `0`. This is different from a variable declared without any initialiser, `struct Point q;`, whose members hold **garbage** until you assign them:
```c
struct Point q;
q.x = 1;
q.y = 2;
```

---

A struct can be passed to a function like any other value. The parameter is declared with the full type name, and the function reads the members with `.`:
```c
struct Point { int x; int y; };

int sum(struct Point p) {
    return p.x + p.y;
}
```
The struct must be declared **before** the function that uses it, so the compiler already knows its members.

---

Writing `struct Point` every time is verbose. With `typedef` you give the struct a short type name, and the struct itself can stay anonymous:
```c
typedef struct {
    double celsius;
} Temperature;

Temperature t = {21.5};
```
The new name `Temperature` is used on its own, without the `struct` keyword in front of it. This is the most common way to declare structs in real programs.

---

A member can itself be a struct. A segment, for example, is made of two points:
```c
typedef struct { int x; int y; } Point;

typedef struct {
    Point start;
    Point end;
} Segment;
```
The inner struct is initialised with its own pair of braces, and its members are reached by chaining the dot operator:
```c
Segment s = {{1, 2}, {5, 2}};
printf("%d\n", s.end.x); // prints "5"
```

---

Structs can be stored in an array like any other type. Each element is initialised with its own braces, and a loop visits them one by one, indexing first and then using the dot:
```c
Point path[3] = {{0, 0}, {2, 1}, {4, 3}};

for (int i = 0; i < 3; i++) {
    printf("%d\n", path[i].y);
}
```

---

An array of structs is passed to a function exactly like an array of numbers: the parameter is written as `Item items[]` and, since the array does not carry its length, the size is passed separately:
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

When a struct is passed to a function **by value**, the function receives a **copy** of it. Changing a member of the parameter changes the copy only, and the caller's variable stays as it was:
```c
void reset(Point p) {
    p.x = 0; // changes the copy
}
```
To let a function modify the caller's struct, pass its **address** with `&` and declare the parameter as a **pointer**, `Point *p`. The pointer refers to the original variable instead of a copy:
```c
void reset(Point *p) { ... }

reset(&origin);
```
Copying also costs time for large structs, so pointers are the usual choice even when nothing is modified.

---

Through a pointer the members are reached with the **arrow** operator `->` instead of the dot:
```c
void grow(Box *b) {
    b->size = b->size * 2;
}
```
`b->size` is a shortcut for `(*b).size`: first follow the pointer, then take the member. The dot works only on a struct, the arrow only on a pointer to a struct.
The caller passes the address of its variable with `&`, and the change made through the pointer is visible after the call.

---

A function that receives a pointer to a struct can update the original value in place. This is the standard way to write "modifier" functions in C, where the first parameter is the struct to change and the others are the data to apply:
```c
void set_number(Player *p, int new_number) {
    p->number = new_number;
}
```
Reading and writing go through the same arrow: `p->score += 10` adds to the member of the struct the pointer refers to.

---

A function can also **return** a struct. Build it in a local variable and return it; the caller receives a copy of the whole value:
```c
Point make_point(int x, int y) {
    Point p = {x, y};
    return p;
}

Point origin = make_point(0, 0);
```
This is how C returns more than one value from a function: pack them into a struct.

---

`sizeof` works on structs too, and it is the right way to know how much memory one occupies:
```c
printf("%zu\n", sizeof(Point));
```
The size is **at least** the sum of the sizes of the members. It can be larger, because the compiler may insert unused **padding** bytes so that each member sits at an address suited to its type: `struct { char c; int n; }` is usually `8` bytes, not `5`. Never hard-code the size of a struct; ask `sizeof`.

---

Structs cannot be compared with `==`: writing `a == b` on two structs is a **compilation error**. Compare them **member by member** instead, combining the results with `&&`:
```c
bool same_size(Rectangle a, Rectangle b) {
    return a.width == b.width && a.height == b.height;
}
```
The same applies to `<` and `>`: you decide which member defines the order.

---

A struct often holds text, stored as a `char` array member with a fixed size:
```c
typedef struct {
    char name[20];
    int age;
} Person;
```
An array member cannot be assigned with `=` after the declaration: `p.name = "Ann"` does not compile. Copy the text into it with `strcpy` from `string.h`, passing the member as the destination:
```c
Person p;
strcpy(p.name, "Ann");
p.age = 30;
```
Only a brace initialiser at the declaration accepts the string directly: `Person p = {"Ann", 30};`.

---

`printf` has no specifier for a whole struct. The usual solution is a small function that prints the members in a fixed format, so every part of the program shows the value the same way:
```c
void print_person(Person p) {
    printf("%s (%d)\n", p.name, p.age);
}
```

---

Putting it together: a function that receives a pointer to a struct can update a text member with `strcpy` through the arrow, since `item->name` is the `char` array inside the original struct:
```c
void set_title(Book *book, char *title) {
    strcpy(book->title, title);
}
```
Remember to add `#include <string.h>` at the top of your code to use `strcpy`.
