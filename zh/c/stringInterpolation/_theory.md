C 没有字符串插值：文本和值通过 `printf` 借助**格式字符串**组合起来，其中每个 `%` 说明符都会被对应的参数替换。最常见的说明符有：
```c
printf("%d\n", 42);      // prints "42" (int, %i is the same)
printf("%f\n", 2.5);     // prints "2.500000" (double, 6 decimals by default)
printf("%s\n", "hi");    // prints "hi" (string)
printf("%c\n", 'A');     // prints "A" (single character)
printf("%x\n", 255);     // prints "ff" (int as lowercase hexadecimal)
printf("100%%\n");       // prints "100%" (a literal percent sign)
```
说明符必须与参数的类型匹配：用 `%d` 打印 `double`，或用 `%s` 打印 `int`，都不会转换该值，而是打印乱码或导致崩溃。

---

`sprintf` 的用法和 `printf` 完全一样，但它不是写到屏幕上，而是把格式化后的文本写入一个 `char` 数组，称为**缓冲区**，并在末尾加上终止符 `'\0'`：
```c
char buffer[32];
sprintf(buffer, "%d-%d", 3, 7);
printf("%s\n", buffer); // prints "3-7"
```
缓冲区必须在调用之前声明，并且要足够大以容纳整段文本加上终止符，否则 `sprintf` 会越过它的末尾继续写。

---

构建字符串的函数通常把缓冲区作为参数接收，并用 `sprintf` 填充它。数组归调用方所有，调用结束后调用方就能读取结果：
```c
void greet(char *out, char *name) {
    sprintf(out, "Hello, %s!", name);
}

char message[32];
greet(message, "Ada");
printf("%s\n", message); // prints "Hello, Ada!"
```
在这些练习中，`string.h` 已经包含在你的代码上方，因此可以用 `strcmp` 来比较结果。

---

`%x` 用小写字母以十六进制打印整数，`%X` 则用大写字母做同样的事。`%c` 接收一个整数字符码并打印它所代表的字符，因此 `%c` 配上 `65` 会打印 `A`：
```c
printf("%x %X %c\n", 31, 31, 66); // prints "1f 1F B"
```

---

`%` 和字母之间的数字设置字段的最小**宽度**。值会在左侧用空格填充，而紧跟在 `%` 后面的**标志**可以改变这种填充：
```c
printf("[%5d]\n", 42);  // prints "[   42]" right-aligned in 5 columns
printf("[%-5d]\n", 42); // prints "[42   ]" the - flag aligns to the left
printf("[%05d]\n", 42); // prints "[00042]" the 0 flag pads with zeros
printf("[%+d]\n", 42);  // prints "[+42]" the + flag always shows the sign
```
比宽度更长的值绝不会被截断，字段只会随之变大。

---

宽度和标志适用于每一种说明符，因此 `%02x` 会把整数以十六进制打印并用零填充到两位。颜色写成 `#rrggbb` 正是这样实现的：
```c
printf("%02x\n", 5);   // prints "05"
printf("%02x\n", 255); // prints "ff"
```

---

一个点后跟一个数字设置**精度**。对 `%f` 来说它是小数位数，会四舍五入；对 `%s` 来说它是最多打印的字符数：
```c
printf("%.2f\n", 3.14159);    // prints "3.14"
printf("%.3s\n", "formatting"); // prints "for"
```
宽度和精度可以组合：`%8.2f` 会在 8 列中右对齐打印两位小数。

---

精度是控制 `double` 在字符串中外观的常用方式。像 `0.425` 这样的比值乘以 `100` 并打印一位小数再跟上 `%%`，就变成了百分比：
```c
sprintf(out, "%.1f%%", 0.425 * 100); // out is "42.5%"
```

---

`sprintf` 和 `printf` 会**返回**写入的字符数，不计终止符 `'\0'`。这就是刚刚构建出来的字符串的长度，无需再单独调用 `strlen`：
```c
char buffer[32];
int length = sprintf(buffer, "%d-%d", 3, 7);
printf("%d\n", length); // prints "3"
```

---

`sprintf` 完全不知道缓冲区有多大。`snprintf` 把缓冲区大小作为第二个参数，写入的字符绝不会超过 `size - 1` 个再加上 `'\0'`，必要时会截断文本。它的返回值是**完整**文本本应有的长度，因此结果大于或等于 `size` 就意味着输出被截断了：
```c
char buffer[8];
int n = snprintf(buffer, sizeof buffer, "%s", "formatting");
printf("%s %d\n", buffer, n); // prints "formatt 10"
```
`sizeof buffer` 给出数组的字节大小，对 `char` 数组来说就是它的元素个数。

---

把 `snprintf` 的返回值与缓冲区大小比较，就能知道内容是否全部放得下。这是构建长度未知的字符串时的安全写法：
```c
int n = snprintf(out, size, "%s", text);
if (n >= size) {
    // out holds only the first size - 1 characters of text
}
```

---

字符串也可以分几步构建，把每一部分紧接着上一部分写入。返回值告诉你文本在哪里结束，因此 `buffer + n` 就是终止符的地址，下一个 `sprintf` 可以从那里继续：
```c
char buffer[32];
int n = sprintf(buffer, "%s", "Hello");
n += sprintf(buffer + n, ", %s", "world"); // buffer is "Hello, world", n is 12
```
把每个返回值累加到 `n` 上，`n` 就始终等于目前已构建文本的总长度。

---

字符串也可以不用格式字符串来拼接。`string.h` 中的 `strcat` 会把第二个参数的副本追加到第一个参数的末尾，第一个参数必须有足够的空闲空间；而 `strncat` 最多追加指定数量的字符：
```c
char text[32] = "Hi";
strcat(text, "!!!");        // text is "Hi!!!"
strncat(text, "abcdef", 2); // text is "Hi!!!ab"
```
两者都总会在追加的字符之后加上终止符 `'\0'`。

---

当没有什么需要格式化时，`puts` 会打印一个字符串并跟上换行。与 `printf` 不同，它不解释 `%`，因此文本会完全按写法原样打印：
```c
puts("Done");      // prints "Done" and a newline
puts("50% off");   // prints "50% off" and a newline
printf("50% off"); // undefined: % off is not a valid specifier
```
固定文本用 `puts` 最合适，而需要插入值时则用 `printf`。

---

当只需要追加字符串的一部分，或者追加的片段必须限制在最大长度以内时，`strncat` 很有用：
```c
char name[16] = "file";
strncat(name, ".backup", 3); // name is "file.ba"
```
当限制大于字符串本身时，整个字符串都会被追加。

---

综合起来：一行报表把左对齐的文本字段、一个分隔符和一个固定小数位数的右对齐数字组合在一起，用 `snprintf` 写入，因此绝不会溢出缓冲区：
```c
snprintf(out, size, "%-6s|%5.1f", "Ada", 9.5); // out is "Ada   |  9.5"
```
只要每个值都能放进各自的宽度，所有行的长度就相同，因此把这些行一行行打印出来时，各列会对齐。
