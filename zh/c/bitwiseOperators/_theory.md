每个整数在内存中都存储为一行**位**（bit），每一位要么是 `0` 要么是 `1`。数字 `12` 存储为 `00001100`，数字 `10` 存储为 `00001010`。
**位运算符**作用于这些单个的位，而不是把数字当作整体。**AND**（按位与）运算符 `&` 逐位比较两个值，只在*两个*位都为 `1` 的地方保留 `1`：
```c
//  00001100   (12)
// &00001010   (10)
//  --------
//  00001000   (8)
printf("%u\n", 12u & 10u);
// 打印 "8"
```
位模式通常写成十六进制字面量，比如 `0x0C`，因为每个十六进制数字恰好对应四个位。做位运算时始终使用 `unsigned` 类型，并用 `%u` 打印它们。

---

**OR**（按位或）运算符 `|` 逐位比较两个值，只要*至少有一个*位为 `1` 就保留 `1`：
```c
//  00001100   (12)
// |00001010   (10)
//  --------
//  00001110   (14)
printf("%u\n", 12u | 10u);
// 打印 "14"
```
`|` 是把两个位模式合并成一个的常用方法。

---

**XOR**（按位异或，exclusive or）运算符 `^` 只在两个位*不同*的地方保留 `1`：
```c
//  00001100   (12)
// ^00001010   (10)
//  --------
//  00000110   (6)
printf("%u\n", 12u ^ 10u);
// 打印 "6"
```
由此可得一个有用的性质：对同一个值应用两次 XOR 会得到原来的值。

---

**NOT**（按位取反）运算符 `~` 只接受一个操作数，并把它的每一个位都翻转：每个 `0` 变成 `1`，每个 `1` 变成 `0`。
一个 `unsigned int` 持有 32 个位，所以 `~0x0Fu` 会翻转全部 32 个位，得到一个非常大的数。要只保留你关心的那个字节，可以把 `~` 和 `& 0xFF` 结合使用：
```c
printf("%u\n", ~0x0Fu & 0xFFu);
// 打印 "240"
```
`~` 的优先级比 `&` 高，所以它先被应用。
不要把 `~` 和逻辑 `!` 混淆：`!` 看的是整个值并给出 `0` 或 `1`，而 `~` 改写每一个位。

---

**左移**运算符 `<<` 把每一个位向左移动若干个位置，并用零填充右侧腾出的位置：
```c
//  00000011   (3)
//  << 2
//  00001100   (12)
printf("%u\n", 3u << 2);
// 打印 "12"
```
左移 `n` 位相当于把值乘以 2 的 `n` 次方。
两种错误会让 C 程序变成未定义行为：对负值做左移，以及移动的位数等于或超过类型的宽度（`unsigned int` 为 32）。使用**无符号**值可以让你避开前一种。

---

**右移**运算符 `>>` 把每一个位向右移动；从右端移出的位会被丢弃。对无符号值来说，左侧腾出的位置用零填充：
```c
//  00001100   (12)
//  >> 2
//  00000011   (3)
printf("%u\n", 12u >> 2);
// 打印 "3"
```
右移 `n` 位相当于把无符号值除以 2 的 `n` 次方，并丢弃余数。
对*负*值做右移是不可移植的，这是把位运算保持在 `unsigned` 类型上的又一个理由。

---

每个二元位运算符都有一个**复合赋值**形式，可以原地更新变量：`&=`、`|=`、`^=`、`<<=` 和 `>>=`。
```c
unsigned int x = 12;
x &= 10;  // 相当于 x = x & 10;
x |= 1;   // 相当于 x = x | 1;
x ^= 3;   // 相当于 x = x ^ 3;
x <<= 1;  // 相当于 x = x << 1;
x >>= 2;  // 相当于 x = x >> 2;
```
它们比重复写变量名更易读，也是修改标志变量各位的常用方式。

---

**掩码**是一种值，它的位用来选取另一个值中你关心的部分。与 `&` 结合使用时，掩码会保留掩码中为 `1` 的位，并把其余的位全部清零：
```c
//  10101011   (0xAB)
// &00001111   (0x0F)
//  --------
//  00001011   (0x0B)
printf("%u\n", 0xABu & 0x0Fu);
// 打印 "11"
```
`0x0F` 保留最低的四个位，称为低**半字节**（nibble），`0xFF` 保留最低的八个位，即一个完整的字节。

---

位从最右边那位开始从 `0` 编号，所以 `1u << n` 是一个只打开第 `n` 位的掩码。
要**置位**单个位，也就是在不碰其他位的情况下把它打开，用该掩码对值做 OR（或）运算：
```c
unsigned int value = 4;      // 00000100
value = value | (1u << 1);   // 00000110
printf("%u\n", value);
// 打印 "6"
```
如果该位本来就开着，值不会改变，这使得置位操作可以安全地重复。

---

要**清零**单个位，也就是把它关掉，用掩码的*反*对值做 AND（与）运算：
```c
unsigned int value = 7;       // 00000111
value = value & ~(1u << 1);   // 00000101
printf("%u\n", value);
// 打印 "5"
```
`~(1u << 1)` 是一个除第 `1` 位外每一位都开着的值，所以 AND 运算会保持其他位原样不动。

---

要**翻转**单个位，也就是不管它当前状态如何都把它翻转，用掩码对值做 XOR（异或）运算：
```c
unsigned int value = 5;      // 00000101
value = value ^ (1u << 1);   // 00000111
printf("%u\n", value);
// 打印 "7"
```
由于 XOR 会自我抵消，第二次翻转同一个位会得到原来的值。

---

要**测试**单个位，用掩码对值做 AND 运算，并检查结果是否不同于 `0`：
```c
unsigned int value = 10;                  // 00001010
printf("%d\n", (value & (1u << 3)) != 0); // 打印 "1"
printf("%d\n", (value & (1u << 2)) != 0); // 打印 "0"
```
AND 的结果并不是 `1`：它要么是 `0`，要么是掩码本身（对第 `3` 位来说是 `8`）。这就是为什么要把结果与 `!= 0` 比较，而不是直接把它当作答案。

---

**Flags** are named masks, each one using a different bit, that can all be stored inside a single variable. They are combined with `|` and read back with `&`:
```c
unsigned int READ = 0x01, WRITE = 0x02;
unsigned int perms = READ | WRITE;
printf("%d\n", (perms & WRITE) != 0);
// 打印 "1"
```
One `unsigned int` can therefore carry 32 independent yes/no answers.

---

Before C23 there was no format specifier that printed a number in binary, and literals like `0b1010` were not standard C either. To show the bits you write the loop yourself: walk from the highest bit down to bit `0` and print `(value >> i) & 1u` each time.
```c
unsigned int value = 5;
for (int i = 3; i >= 0; i--) {
    printf("%u", (value >> i) & 1u);
}
printf("\n");
// 打印 "0101"
```
Shifting the value down by `i` brings bit `i` into the rightmost place, where `& 1u` isolates it.

---

Counting how many bits of a value are `1` is a classic bit loop: test the lowest bit with `& 1u`, add it to a counter, then shift the value one place right with `>>=` and repeat until nothing is left.
```c
unsigned int value = 6, count = 0;
while (value != 0) {
    count += value & 1u;
    value >>= 1;
}
// count 为 2
```
The loop always ends, because an unsigned value shifted right enough times becomes `0`.

---

Several small numbers are often packed inside one larger value. To read one of them back, first shift it down so it starts at bit `0`, then mask off everything above it:
```c
unsigned int packed = 0x1234;
printf("%u\n", (packed >> 8) & 0xFF);
// 打印 "18"，即 0x12 字节
```
Shifting first and masking afterwards is the order to remember: the mask always describes the field once it has reached the bottom.
