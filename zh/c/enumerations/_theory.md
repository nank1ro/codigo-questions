**枚举**（`enum`）为一组相关的整数常量命名，这样你就可以写 `RED` 而不是一个孤零零的数字。
你使用 `enum` 关键字、一个名称以及花括号之间的常量列表来声明它：
```c
enum Color { RED, GREEN, BLUE };
```
每个常量都是一个整数：除非另有说明，第一个常量是 `0`，后面每一个都是前一个加一，因此 `RED` 是 `0`，`GREEN` 是 `1`，`BLUE` 是 `2`。
因为它们是整数，所以你用 `%d` 打印它们：
```c
printf("%d\n", GREEN);
// prints "1"
```

---

编号会随着你列出的常量数量自动继续：第四个常量是 `3`，第五个是 `4`，依此类推。
名称通常像其他常量一样使用大写字母书写，并且必须在整个程序中唯一：两个枚举不能共用同一个常量名。

---

你也可以用 `=` 给某个常量指定显式的值；它之后的常量会从这个值继续递增：
```c
enum Month { JAN = 1, FEB, MAR }; // FEB is 2, MAR is 3
```
显式的值不必是连续的或递增的：`enum Status { OK = 200, NOT_FOUND = 404 };` 完全合法。

---

枚举也是一种类型：你可以通过写 `enum` 加上枚举名来声明该类型的变量，并给它赋值某个常量：
```c
enum Color favorite = GREEN;
```
由于常量是整数，你可以用通常的运算符比较 enum 变量：
```c
if (favorite == GREEN) {
    printf("Green it is\n");
}
```

---

枚举可以作为函数参数的类型，就像 `int` 一样：
```c
int is_weekend(enum Day day) {
    return day == SAT || day == SUN;
}
```
在函数内部，`switch` 是处理每个常量的自然方式，因为枚举常量可以直接用作 `case` 标签：
```c
switch (day) {
    case SAT: return 1;
    case SUN: return 1;
    default: return 0;
}
```

---

当 `switch` 的每个 case 都处理一个常量时，记得在每个 case 后加上 `break`，否则执行会继续落入下一个 case。
如果覆盖了枚举的所有常量，就不需要 `default` 分支。

---

函数也可以返回枚举；只需把 enum 类型用作返回类型，并返回它的某个常量：
```c
enum Grade grade_for(int score) {
    if (score >= 60) {
        return PASS;
    }
    return FAIL;
}
```
相比返回一个孤零零的 `0` 或 `1`，返回一个命名常量对调用者来说清晰得多。

---

每次都写 `enum Color` 很啰嗦。用 `typedef` 可以给枚举起一个简短的类型名，而枚举本身可以保持匿名：
```c
typedef enum { RED, GREEN, BLUE } Color;

Color favorite = BLUE;
```
新名称 `Color` 可以单独使用，前面不需要加 `enum` 关键字。

---

枚举常量会自动转换为 `int`，所以 `int n = BLUE;` 是合法的，并保存 `2`。
反过来的转换要用**强制类型转换**来完成，即在整数前用括号写出枚举类型：
```c
enum Color c = (enum Color)1; // c is GREEN
```
C 不会检查这个数字是否对应某个常量：`(enum Color)7` 可以编译通过，即使没有任何常量的值是 `7`，所以转换前要先校验整数。

---

对 enum 值做算术运算得到的是普通的 `int`：`GREEN + 1` 是 `2`，而不是 `BLUE`。
要把结果存回 enum 变量或从函数中返回，需要把它转换为 enum 类型：
```c
enum Color after_green = (enum Color)(GREEN + 1); // BLUE
```
结合取余运算符 `%`，这可以让你在常量之间循环，并绕回到第一个常量。

---

一个常见的技巧是在枚举末尾多加一个常量，通常命名为 `COUNT`：由于编号从 `0` 开始，它的值正好等于它之前真正常量的数量。
```c
enum Day { MON, TUE, WED, DAY_COUNT }; // DAY_COUNT is 3
```
这个哨兵值让你可以遍历所有常量而不用把数字写死，并且在你在它前面添加常量时依然保持正确：
```c
for (int d = MON; d < DAY_COUNT; d++) {
    printf("%d\n", d);
}
```

---

`COUNT` 哨兵值同样是数组大小的完美选择，每个常量对应一个槽位，常量本身就成了易读的索引：
```c
enum Fruit { APPLE, BANANA, CHERRY, FRUIT_COUNT };

int stock[FRUIT_COUNT] = {10, 4, 7};
printf("%d\n", stock[BANANA]); // prints "4"
```
从 `0` 到 `FRUIT_COUNT` 的循环会访问每一个槽位，需要返回循环索引时可以把它转换回 `enum Fruit`。

---

C 没有内置的方法来获取枚举常量的名称：`printf("%d\n", SUMMER)` 打印的是 `2`，而不是 `Summer`。常见的做法是写一个带 `switch` 的小函数，为每个常量返回对应的字符串。

---

枚举值可以像其他整数一样存储在数组中：`enum Fruit basket[] = {APPLE, APPLE, CHERRY};` 保存了三种水果，每个元素都可以与某个常量比较。
