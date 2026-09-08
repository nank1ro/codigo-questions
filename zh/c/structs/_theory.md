**结构体**（struct）把不同类型的相关值组合成一个全新的类型。它内部的每个值称为一个**成员**（member）。
声明在大括号之间列出各个成员，并以分号结尾；它创建了类型 `struct Point`，但还没有创建任何变量：
```c
struct Point {
    int x;
    int y;
};
```
这种类型的变量用 `struct Point` 来声明，它的成员可以像数组一样用大括号**按顺序**初始化：
```c
struct Point p = {3, 4}; // x is 3, y is 4
```
成员通过**点**运算符 `.` 来读写：
```c
printf("%d\n", p.x); // prints "3"
p.y = 10;
```

---

按顺序初始化成员很脆弱：一旦结构体增加了一个成员，所有的初始化值都会错位。从 C99 开始，**指定初始化器**（designated initialiser）用点为每个成员命名，顺序可以任意：
```c
struct Point p = {.y = 4, .x = 3};
```
没有列出的成员会被设为 `0`，因此 `{.y = 5}` 使 `x` 等于 `0`。这与声明时不带任何初始化器的变量 `struct Point q;` 不同，后者的成员在被赋值之前保存的是**垃圾值**：
```c
struct Point q;
q.x = 1;
q.y = 2;
```

---

结构体可以像任何其他值一样传递给函数。参数用完整的类型名来声明，函数用 `.` 读取成员：
```c
struct Point { int x; int y; };

int sum(struct Point p) {
    return p.x + p.y;
}
```
结构体必须在使用它的函数**之前**声明，这样编译器才能提前知道它的成员。

---

每次都写 `struct Point` 很啰嗦。使用 `typedef` 可以给结构体起一个简短的类型名，结构体本身则可以保持匿名：
```c
typedef struct {
    double celsius;
} Temperature;

Temperature t = {21.5};
```
新名字 `Temperature` 可以单独使用，前面不需要 `struct` 关键字。这是实际程序中声明结构体最常见的方式。

---

成员本身也可以是一个结构体。例如，一条线段由两个点组成：
```c
typedef struct { int x; int y; } Point;

typedef struct {
    Point start;
    Point end;
} Segment;
```
内部结构体用它自己的一对大括号初始化，其成员通过链式使用点运算符来访问：
```c
Segment s = {{1, 2}, {5, 2}};
printf("%d\n", s.end.x); // prints "5"
```

---

结构体可以像任何其他类型一样存入数组。每个元素用它自己的一对大括号初始化，循环逐个访问它们，先做索引，再使用点：
```c
Point path[3] = {{0, 0}, {2, 1}, {4, 3}};

for (int i = 0; i < 3; i++) {
    printf("%d\n", path[i].y);
}
```

---

结构体数组传递给函数的方式与数字数组完全一样：参数写作 `Item items[]`，由于数组本身不携带长度，大小需要单独传递：
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

当结构体**按值**传递给函数时，函数收到的是它的一个**副本**。修改参数的成员只会改变这个副本，调用者的变量保持原样：
```c
void reset(Point p) {
    p.x = 0; // changes the copy
}
```
要让函数修改调用者的结构体，需要用 `&` 传递它的**地址**，并把参数声明为**指针** `Point *p`。指针指向的是原始变量，而不是副本：
```c
void reset(Point *p) { ... }

reset(&origin);
```
对较大的结构体来说，复制还要花费时间，因此即使什么都不修改，指针也是通常的选择。

---

通过指针访问成员时，要使用**箭头**运算符 `->` 而不是点：
```c
void grow(Box *b) {
    b->size = b->size * 2;
}
```
`b->size` 是 `(*b).size` 的简写：先顺着指针找到结构体，再取成员。点只能用在结构体上，箭头只能用在指向结构体的指针上。
调用者用 `&` 传递自己变量的地址，通过指针所做的修改在调用结束之后依然可见。

---

接收指向结构体的指针的函数可以就地更新原始值。这是在 C 中编写"修改器"函数的标准方式：第一个参数是要修改的结构体，其余参数是要应用的数据：
```c
void set_number(Player *p, int new_number) {
    p->number = new_number;
}
```
读写都经过同一个箭头：`p->score += 10` 会给指针所指结构体的成员加上 `10`。

---

函数也可以**返回**结构体。先在局部变量里把它构建出来再返回；调用者会收到整个值的一份副本：
```c
Point make_point(int x, int y) {
    Point p = {x, y};
    return p;
}

Point origin = make_point(0, 0);
```
这就是 C 从函数返回多个值的方法：把它们打包进一个结构体。

---

`sizeof` 同样适用于结构体，它是弄清一个结构体占用多少内存的正确方式：
```c
printf("%zu\n", sizeof(Point));
```
大小**至少**是各成员大小之和。它也可能更大，因为编译器可能插入未使用的**填充**（padding）字节，让每个成员落在适合其类型的地址上：`struct { char c; int n; }` 通常是 `8` 字节，而不是 `5`。永远不要硬编码结构体的大小；要向 `sizeof` 询问。

---

结构体不能用 `==` 来比较：对两个结构体写 `a == b` 是**编译错误**。应当**逐个成员**比较它们，并用 `&&` 组合各个结果：
```c
bool same_size(Rectangle a, Rectangle b) {
    return a.width == b.width && a.height == b.height;
}
```
`<` 和 `>` 也是如此：由你决定用哪个成员来定义顺序。

---

结构体经常需要保存文本，文本以固定大小的 `char` 数组成员的形式存储：
```c
typedef struct {
    char name[20];
    int age;
} Person;
```
数组成员在声明之后不能用 `=` 赋值：`p.name = "Ann"` 无法通过编译。要用 `string.h` 中的 `strcpy` 把文本复制进去，把该成员作为目标位置：
```c
Person p;
strcpy(p.name, "Ann");
p.age = 30;
```
只有声明处的大括号初始化器能直接接受字符串：`Person p = {"Ann", 30};`。

---

`printf` 没有能打印整个结构体的格式说明符。通常的解决办法是写一个小函数，按固定的格式打印各个成员，这样程序的每个部分都能以相同的方式显示这个值：
```c
void print_person(Person p) {
    printf("%s (%d)\n", p.name, p.age);
}
```

---

综合运用：接收指向结构体的指针的函数可以通过箭头用 `strcpy` 更新文本成员，因为 `item->name` 就是原始结构体内部的那个 `char` 数组：
```c
void set_title(Book *book, char *title) {
    strcpy(book->title, title);
}
```
记住要在代码顶部添加 `#include <string.h>`，这样才能使用 `strcpy`。
