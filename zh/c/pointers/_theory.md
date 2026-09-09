每个变量都存放在内存中的某个位置，这个位置有一个编号，称为它的**地址**（address）。`&` 运算符读作"取地址"，给出变量的地址：
```c
int x = 42;
printf("%p\n", &x); // prints something like 0x7ffd5c3e9a4c
```
`%p` 说明符用来打印地址；具体数值每次运行都不一样，因此程序绝不会依赖它。
地址存储在**指针**（pointer）变量中。声明指针时，先写它所指向的类型，再跟一个 `*`：
```c
int *p = &x; // p is a pointer to int, and it holds the address of x
```
这时就说 `p` **指向** `x`。两个指针持有相同地址时即相等，因此 `p == &x` 为真。

---

指针本身只是一个地址。要读取存储在该地址中的值，需要用 `*` 运算符对指针进行**解引用**（dereference）：
```c
int x = 42;
int *p = &x;
printf("%d\n", *p); // prints "42"
```
`*p` 的意思是"`p` 所指向的值"，它和 `x` 本身一样是一个 `int`。同一个符号 `*` 有两种角色：在声明 `int *p` 中表示"这是一个指针"，在表达式 `*p` 中则顺着指针找到值。

---

解引用后的指针也可以被**赋值**。向 `*p` 写入会把新值存储到 `p` 所持有的地址中，因此它指向的变量随之改变：
```c
int x = 5;
int *p = &x;
*p = 10;
printf("%d\n", x); // prints "10"
```
`x` 和 `*p` 是同一块内存的两个名字。不带 `*` 给 `p` 赋值，改变的则是指针所持有的**地址**，而不是存储在该地址中的值。

---

尚未指向任何内容的指针应持有 `NULL`，这是一个定义在 `stdio.h` 和 `stddef.h` 中的特殊常量，表示"没有地址"：
```c
int *p = NULL;
```
对 `NULL` 指针解引用是会导致程序崩溃的运行时错误，因此可能为 `NULL` 的指针在使用前要先检查：
```c
if (p != NULL) {
    printf("%d\n", *p);
}
```
由于 `NULL` 就是零，`if (p)` 是 `if (p != NULL)` 的常见简写。声明时未初始化的指针持有的是垃圾值而非 `NULL`，因此务必始终初始化指针。

---

指针可以指向任何类型：`double *`、`char *`、`bool *` 等等。声明中的类型告诉编译器，解引用指针时要读取多少个字节以及这些字节的含义：
```c
double price = 9.5;
double *p = &price;
*p = *p * 2; // price is now 19.0
```
指针必须与它所指向变量的类型一致；`int *p = &price;` 会被编译器拒绝。`NULL` 是唯一能赋给任何类型指针的值。

---

指向 `char` 的指针和其他任何指针一样：它持有一个字符的地址，`*p` 可以读写该字符：
```c
char grade = 'B';
char *p = &grade;
*p = 'A';
printf("%c\n", grade); // prints "A"
```
通过指针读和写可以随意混用：`*p = *p + 1` 会把 `'A'` 变成 `'B'`。

---

指针存储的是地址，而在同一台机器上，无论其中存储什么类型，所有地址的大小都相同。因此 `char *`、`int *` 和 `double *` 的 `sizeof` 结果相同：在 64 位系统上是 `8` 字节，在 32 位系统上是 `4` 字节：
```c
printf("%zu\n", sizeof(int *));  // prints "8" on 64-bit
printf("%zu\n", sizeof(double)); // prints "8"
printf("%zu\n", sizeof(char));   // prints "1"
```
不要把指针本身的大小与它所指向内容的大小混为一谈：`sizeof(p)` 是地址的大小，`sizeof(*p)` 是值的大小。

---

数组名在表达式中使用时给出其**首个元素**的地址，因此可以直接赋给指针：
```c
int numbers[3] = {10, 20, 30};
int *p = numbers; // same as &numbers[0]
```
给指针加一个整数会使它向前移动相应数量的**元素**，而不是字节：`p + 1` 是 `numbers[1]` 的地址，`*(p + 1)` 是 `20`。编译器会按类型大小对步长进行缩放。
索引也适用于指针：`p[i]` 定义为 `*(p + i)`，所以 `p[2]` 是 `30`。这称为**指针算术**（pointer arithmetic）。

---

由于 `p + 1` 是下一个元素，`p++` 会把指针就地移动到下一个元素。循环可以让指针不断前进，从而代替索引来遍历数组：
```c
int *p = values;
for (int i = 0; i < 3; i++) {
    printf("%d\n", *p);
    p++;
}
```
每一轮先打印 `p` 所指向的元素，然后把 `p` 向前移动一个元素。

---

数组传给函数时会**退化**（decay）为指向其第一个元素的指针。这就是为什么参数 `int values[]` 和 `int *values` 的含义完全相同，也是为什么函数无法自行得知长度：它只收到一个地址。
指向同一数组的指针可以比较和相减。`end - start` 是两者之间的元素个数，循环可以让指针从一个地址推进到另一个地址：
```c
for (int *p = start; p < end; p++) {
    printf("%d\n", *p);
}
```
传入 `numbers` 和 `numbers + 3` 即可描述前三个元素，无需单独的长度参数。

---

函数实参按**值**传递：函数收到的是副本，给参数赋值绝不会改变调用者的变量。要让函数改变一个变量，需传入该变量的地址，并在函数内部对指针解引用：
```c
void reset(int *p) {
    *p = 0;
}

int counter = 7;
reset(&counter); // counter is now 0
```
经典的例子是交换两个变量：在覆写其中一个之前，需要先用一个临时副本保存另一个值。

---

函数只能 `return` 一个值。要交回更多结果，它可以接收指向调用者变量的指针，并通过它们写出结果。这样的参数称为**输出参数**（output parameters）：
```c
void min_max(int a, int b, int *min, int *max) {
    *min = a;
    *max = b;
    if (a > b) {
        *min = b;
        *max = a;
    }
}

int lo, hi;
min_max(4, 9, &lo, &hi); // lo is 4, hi is 9
```
调用者声明变量、传入它们的地址，调用之后就会发现变量已被填好。许多标准库函数都使用这种模式，这正是 `scanf("%d", &n)` 需要 `&` 的原因。

---

指向结构体的指针用箭头 `->` 访问成员，数组中存储的结构体的地址用 `&items[i]` 取得。函数还可以**返回**指针，例如返回它找到的那个元素：
```c
Player *first_active(Player players[], int size) {
    for (int i = 0; i < size; i++) {
        if (players[i].active) {
            return &players[i];
        }
    }
    return NULL;
}
```
调用者在确认返回的指针不为 `NULL` 之后，再用 `->` 通过它读取成员。返回指针可以避免复制结构体，并让调用者能够修改原始元素。

---

`const` 保护的是值还是指针，取决于它写在哪里：
```c
const int *p = &a; // pointer to const: *p cannot be changed, p can point elsewhere
int *const q = &a; // const pointer: q always points to a, but *q can be changed
```
声明要从右往左读：`p` 是指向常量 `int` 的指针；`q` 是指向 `int` 的常量指针。指向 const 的指针是常见的方式，用来承诺函数只**读取**它收到的内容，例如 `int sum(const int *values, int size)`。普通变量也可以传给它；这一承诺只限制函数能做什么。

---

指针本身也是变量，因此它也有自己的地址，这个地址可以存储在**指向指针的指针**（pointer to pointer）中，声明时要用两颗星号：
```c
int x = 7;
int *p = &x;
int **pp = &p;
```
`*pp` 是 `p`，即 `x` 的地址；`**pp` 连走两步到达 `7`。指向指针的指针让函数能够改变指针所持有的地址：函数接收 `&p` 并对 `*pp` 赋值。

---

综合运用：一个函数用指针遍历数组，保存一个指向目前为止最佳元素的指针并将其返回，没有可返回的内容时返回 `NULL`：
```c
int *first_negative(int *values, int size) {
    for (int *p = values; p < values + size; p++) {
        if (*p < 0) {
            return p;
        }
    }
    return NULL;
}
```
调用者在解引用之前先把结果与 `NULL` 比较，并且可以用 `result - values` 还原该元素的索引。
