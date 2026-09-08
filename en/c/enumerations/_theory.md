An **enumeration** (`enum`) gives names to a set of related integer constants, so you can write `RED` instead of a bare number.
You declare it with the `enum` keyword, a name and the list of constants between braces:
```c
enum Color { RED, GREEN, BLUE };
```
Every constant is an integer: unless you say otherwise, the first one is `0` and each following one is the previous plus one, so `RED` is `0`, `GREEN` is `1` and `BLUE` is `2`.
Because they are integers, you print them with `%d`:
```c
printf("%d\n", GREEN);
// prints "1"
```

---

The numbering continues automatically for as many constants as you list: the fourth constant is `3`, the fifth is `4` and so on.
The names are usually written in uppercase, like other constants, and they must be unique in the whole program: two enumerations cannot share a constant name.

---

You can also give a constant an explicit value with `=`; the constants after it keep counting up from that value:
```c
enum Month { JAN = 1, FEB, MAR }; // FEB is 2, MAR is 3
```
Explicit values do not have to be consecutive or increasing: `enum Status { OK = 200, NOT_FOUND = 404 };` is perfectly valid.

---

An enumeration is also a type: you can declare a variable of that type by writing `enum` followed by the enumeration name, and assign one of its constants to it:
```c
enum Color favorite = GREEN;
```
Since the constants are integers, you compare enum variables with the usual operators:
```c
if (favorite == GREEN) {
    printf("Green it is\n");
}
```

---

An enumeration can be the type of a function parameter, exactly like `int`:
```c
int is_weekend(enum Day day) {
    return day == SAT || day == SUN;
}
```
Inside the function, a `switch` is the natural way to handle each constant, because enum constants can be used directly as `case` labels:
```c
switch (day) {
    case SAT: return 1;
    case SUN: return 1;
    default: return 0;
}
```

---

When every case of a `switch` handles one constant, remember the `break` after each one, otherwise execution falls through to the next case.
A `default` case is not required if you cover every constant of the enumeration.

---

A function can return an enumeration too; just use the enum type as the return type and return one of its constants:
```c
enum Grade grade_for(int score) {
    if (score >= 60) {
        return PASS;
    }
    return FAIL;
}
```
Returning a named constant is much clearer for the caller than returning a bare `0` or `1`.

---

Writing `enum Color` every time is verbose. With `typedef` you give the enumeration a short type name, and the enumeration itself can stay anonymous:
```c
typedef enum { RED, GREEN, BLUE } Color;

Color favorite = BLUE;
```
The new name `Color` is used on its own, without the `enum` keyword in front of it.

---

An enum constant converts to `int` automatically, so `int n = BLUE;` is valid and stores `2`.
Going the other way is done with a **cast**, writing the enum type between parentheses before the integer:
```c
enum Color c = (enum Color)1; // c is GREEN
```
C does not check that the number matches a constant: `(enum Color)7` compiles even though no constant is `7`, so validate integers before converting them.

---

Arithmetic on an enum value produces a plain `int`: `GREEN + 1` is `2`, not `BLUE`.
To store the result back into an enum variable or return it from a function, cast it to the enum type:
```c
enum Color after_green = (enum Color)(GREEN + 1); // BLUE
```
Combined with the remainder operator `%`, this lets you cycle through the constants and wrap around to the first one.

---

A common trick is to add one extra constant at the end of the enumeration, usually named `COUNT`: since numbering starts at `0`, its value is exactly the number of real constants that come before it.
```c
enum Day { MON, TUE, WED, DAY_COUNT }; // DAY_COUNT is 3
```
That sentinel lets you loop over every constant without hard-coding the number, and it stays correct when you add constants before it:
```c
for (int d = MON; d < DAY_COUNT; d++) {
    printf("%d\n", d);
}
```

---

The `COUNT` sentinel is also the perfect size for an array with one slot per constant, and the constants become readable indexes into it:
```c
enum Fruit { APPLE, BANANA, CHERRY, FRUIT_COUNT };

int stock[FRUIT_COUNT] = {10, 4, 7};
printf("%d\n", stock[BANANA]); // prints "4"
```
A loop from `0` to `FRUIT_COUNT` visits every slot, and the loop index can be cast back to `enum Fruit` when you need to return it.

---

C has no built-in way to get the name of an enum constant: `printf("%d\n", SUMMER)` prints `2`, not `Summer`. The usual solution is a small function with a `switch` that returns the matching string for each constant.

---

Enum values can be stored in arrays like any other integers: `enum Fruit basket[] = {APPLE, APPLE, CHERRY};` holds three fruits, and each element can be compared with a constant.
