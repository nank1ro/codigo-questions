C 语言没有专门的字符串类型：**字符串**是以特殊字符——**空字符**（null terminator）`'\0'`——结尾的 `char` 数组。
创建字符串最简单的方法是使用双引号包裹的字符串字面量：
```c
char name[] = "Codigo";
```
编译器会自动统计字符数量，并在末尾为你添加 `'\0'`。
使用 `%s` 占位符打印字符串：
```c
printf("%s\n", name);
// prints "Codigo"
```

---

空字符会占用内存空间：字面量 `"hi"` 占用 3 个字节，即 `'h'`、`'i'` 和 `'\0'`。
当你自己声明大小时，一定要为它留出空间：
```c
char word[6] = "hello"; // 5 letters + '\0'
```
没有终止符，C 语言就无法知道字符串在哪里结束。

---

头文件 `string.h` 提供了处理字符串的函数。
`strlen` 返回空字符之前的字符数量（终止符本身不计入）：
```c
strlen("hello"); // 5
```
接收字符串的函数将参数声明为 `char *text`，即指向第一个字符的指针。
在这些练习中，`string.h` 和 `ctype.h` 已经包含在你的代码上方。

---

由于字符串是一个数组，每个字符都有一个从 `0` 开始的索引：
```c
char word[] = "Coding";
word[0]; // 'C'
word[5]; // 'g'
```
单个字符使用 `%c` 打印。字符也可以被替换：
```c
word[0] = 'K'; // word is now "Koding"
```

---

由于每个字符串都以 `'\0'` 结尾，你可以在不预先知道其长度的情况下遍历它：只要当前字符不是终止符就继续。
```c
for (int i = 0; text[i] != '\0'; i++) {
    printf("%c\n", text[i]);
}
```

---

数组在声明之后不能用 `=` 赋值：
```c
char copy[20];
copy = "Codigo"; // error
```
要复制字符串，使用 `string.h` 中的 `strcpy(destination, source)`。
目标数组必须足够大，能容纳所有字符加上 `'\0'`。

---

`strcat(destination, source)` 将 `source` 追加到 `destination` 的末尾：
```c
char text[20] = "Hello";
strcat(text, " World");
// text is now "Hello World"
```
与 `strcpy` 一样，目标数组必须有足够的空间容纳结果。

---

两个字符串不能用 `==` 比较：那样比较的是它们在内存中的地址，而不是它们的字符。
应使用 `strcmp(first, second)`，当两个字符串包含完全相同的字符时返回 `0`：
```c
strcmp("cat", "cat"); // 0
strcmp("cat", "dog"); // not 0
```

---

`strcmp` 使用字符编码逐个字符地比较字符串。
当第一个字符串排在第二个之前时，结果为负数；排在之后时为正数；相等时为 `0`：
```c
strcmp("a", "b"); // negative
strcmp("b", "a"); // positive
```

---

`strncpy(destination, source, n)` 最多复制 `n` 个字符。
如果 `source` 比 `n` 长，就不会写入 `'\0'`：你需要自己终止结果。
```c
char prefix[10];
strncpy(prefix, "Codigo", 3);
prefix[3] = '\0'; // prefix is "Cod"
```

---

头文件 `ctype.h` 提供了处理单个字符的函数。
`toupper(c)` 返回字母的大写形式，`tolower(c)` 返回小写形式；其他任何字符都会原样返回：
```c
char letter = toupper('a'); // 'A'
```

---

字符串以指针的形式传递给函数，因此接收 `char *text` 的函数可以直接修改调用者的字符。
将循环直到 `'\0'` 与 `toupper` 结合起来，就可以转换整个字符串：
```c
text[i] = toupper(text[i]);
```

---

`sprintf` 的用法与 `printf` 类似，但它将格式化后的文本写入字符数组，而不是屏幕：
```c
char buffer[30];
sprintf(buffer, "%d items", 3); // buffer is "3 items"
```
缓冲区必须足够大，能容纳整个文本及其 `'\0'`。

---

`sprintf` 是将数字转换为文本的便捷方式：一旦数字进入缓冲区，任何字符串函数都可以对它进行处理。
