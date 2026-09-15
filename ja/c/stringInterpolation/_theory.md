Cには文字列補間がありません。テキストと値は**フォーマット文字列**を介して`printf`で組み合わされ、各`%`指定子が対応する引数に置き換えられます。最もよく使われる指定子は以下のとおりです:
```c
printf("%d\n", 42);      // "42" を出力する(int、%i でも同じ)
printf("%f\n", 2.5);     // "2.500000" を出力する(double はデフォルトで小数点以下6桁)
printf("%s\n", "hi");    // "hi" を出力する(文字列)
printf("%c\n", 'A');     // "A" を出力する(1文字)
printf("%x\n", 255);     // "ff" を出力する(int を小文字の16進数として)
printf("100%%\n");       // "100%" を出力する(パーセント記号そのもの)
```
指定子は引数の型と一致していなければなりません。`double`を`%d`で、`int`を`%s`で出力しても値は変換されず、無意味な出力やクラッシュの原因になります。

---

`sprintf`は`printf`とまったく同じように動作しますが、画面に書き出す代わりに、フォーマット済みのテキストを**バッファ**と呼ばれる`char`配列に、終端文字`'\0'`を付けて書き込みます:
```c
char buffer[32];
sprintf(buffer, "%d-%d", 3, 7);
printf("%s\n", buffer); // "3-7" を出力する
```
バッファは呼び出しの前に宣言し、テキスト全体と終端文字を格納できる十分な大きさが必要です。そうしないと`sprintf`は配列の末尾を超えて書き込みます。

---

文字列を構築する関数は、通常バッファをパラメータとして受け取り、`sprintf`でそれを埋めます。配列の所有者は呼び出し側であり、呼び出しの後で結果を読み取ることができます:
```c
void greet(char *out, char *name) {
    sprintf(out, "Hello, %s!", name);
}

char message[32];
greet(message, "Ada");
printf("%s\n", message); // "Hello, Ada!" を出力する
```
これらの演習では`string.h`がコードの上ですでにインクルードされているため、`strcmp`を使って結果を比較できます。

---

`%x` prints an integer in hexadecimal with lowercase letters, and `%X` does the same with uppercase letters. `%c` takes an integer character code and prints the character it stands for, so `%c` with `65` prints `A`:
```c
printf("%x %X %c\n", 31, 31, 66); // "1f 1F B" を出力する
```

---

A number between `%` and the letter sets the minimum **width** of the field. The value is padded with spaces on the left, and **flags** placed right after the `%` change the padding:
```c
printf("[%5d]\n", 42);  // "[   42]" を5桁で右揃えにして出力する
printf("[%-5d]\n", 42); // "[42   ]" を出力する。- フラグは左揃えにする
printf("[%05d]\n", 42); // "[00042]" を出力する。0 フラグはゼロで埋める
printf("[%+d]\n", 42);  // "[+42]" を出力する。+ フラグは常に符号を表示する
```
A value longer than the width is never cut, the field simply grows.

---

Width and flags work with every specifier, so `%02x` prints an integer as hexadecimal padded with zeros to two digits. This is how colors are written as `#rrggbb`:
```c
printf("%02x\n", 5);   // "05" を出力する
printf("%02x\n", 255); // "ff" を出力する
```

---

A dot followed by a number sets the **precision**. For `%f` it is the number of decimals, rounded; for `%s` it is the maximum number of characters printed:
```c
printf("%.2f\n", 3.14159);    // "3.14" を出力する
printf("%.3s\n", "formatting"); // "for" を出力する
```
Width and precision can be combined: `%8.2f` prints two decimals right-aligned in 8 columns.

---

Precision is the usual way to control how a `double` looks in a string. A ratio like `0.425` becomes a percentage by multiplying by `100` and printing one decimal followed by `%%`:
```c
sprintf(out, "%.1f%%", 0.425 * 100); // out は "42.5%"
```

---

`sprintf` and `printf` **return** the number of characters written, not counting the terminating `'\0'`. This is the length of the string that was just built, without a separate `strlen` call:
```c
char buffer[32];
int length = sprintf(buffer, "%d-%d", 3, 7);
printf("%d\n", length); // "3" を出力する
```

---

`sprintf` has no idea how big the buffer is. `snprintf` takes the buffer size as its second argument and never writes more than `size - 1` characters plus the `'\0'`, cutting the text if needed. Its return value is the length the **complete** text would have had, so a result greater than or equal to `size` means the output was truncated:
```c
char buffer[8];
int n = snprintf(buffer, sizeof buffer, "%s", "formatting");
printf("%s %d\n", buffer, n); // "formatt 10" を出力する
```
`sizeof buffer` gives the size of the array in bytes, which for a `char` array is its number of elements.

---

Comparing the return value of `snprintf` with the buffer size tells whether everything fit. This is the safe pattern for building strings of unknown length:
```c
int n = snprintf(out, size, "%s", text);
if (n >= size) {
    // out には text の先頭 size - 1 文字だけが入る
}
```

---

A string can be built in several steps by writing each piece right after the previous one. The return value tells where the text ends, so `buffer + n` is the address of the terminator and the next `sprintf` can continue from there:
```c
char buffer[32];
int n = sprintf(buffer, "%s", "Hello");
n += sprintf(buffer + n, ", %s", "world"); // buffer は "Hello, world"、n は 12
```
Adding each return value to `n` keeps it equal to the total length of the text built so far.

---

Strings can also be combined without a format string. `strcat` from `string.h` appends a copy of its second argument to the end of the first, which must have enough free space, and `strncat` appends at most a given number of characters:
```c
char text[32] = "Hi";
strcat(text, "!!!");        // text は "Hi!!!"
strncat(text, "abcdef", 2); // text は "Hi!!!ab"
```
Both always add the terminating `'\0'` after the appended characters.

---

When there is nothing to format, `puts` prints a string followed by a newline. Unlike `printf` it does not interpret `%`, so the text is printed exactly as written:
```c
puts("Done");      // "Done" と改行を出力する
puts("50% off");   // "50% off" と改行を出力する
printf("50% off"); // 未定義: % off は有効な指定子ではない
```
`puts` is the right choice for fixed text, and `printf` when values must be inserted.

---

`strncat` is useful when only a part of a string must be appended, or when the appended piece must be limited to a maximum length:
```c
char name[16] = "file";
strncat(name, ".backup", 3); // name は "file.ba"
```
When the limit is larger than the string, the whole string is appended.

---

Putting it together: a report row combines a left-aligned text field, a separator and a right-aligned number with a fixed number of decimals, written with `snprintf` so it never overflows the buffer:
```c
snprintf(out, size, "%-6s|%5.1f", "Ada", 9.5); // out は "Ada   |  9.5"
```
As long as every value fits its width, all rows have the same length, so the columns line up when the rows are printed one under the other.
