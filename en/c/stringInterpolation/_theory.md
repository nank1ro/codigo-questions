C has no string interpolation: text and values are combined by `printf` through a **format string**, where each `%` specifier is replaced by the matching argument. The most common specifiers are:
```c
printf("%d\n", 42);      // prints "42" (int, %i is the same)
printf("%f\n", 2.5);     // prints "2.500000" (double, 6 decimals by default)
printf("%s\n", "hi");    // prints "hi" (string)
printf("%c\n", 'A');     // prints "A" (single character)
printf("%x\n", 255);     // prints "ff" (int as lowercase hexadecimal)
printf("100%%\n");       // prints "100%" (a literal percent sign)
```
The specifier must match the type of the argument: printing a `double` with `%d` or an `int` with `%s` does not convert the value, it prints garbage or crashes.

---

`sprintf` works exactly like `printf`, but instead of writing to the screen it writes the formatted text into a `char` array, called a **buffer**, followed by the terminating `'\0'`:
```c
char buffer[32];
sprintf(buffer, "%d-%d", 3, 7);
printf("%s\n", buffer); // prints "3-7"
```
The buffer must be declared before the call and must be large enough for the whole text plus the terminator, otherwise `sprintf` writes past its end.

---

A function that builds a string usually receives the buffer as a parameter and fills it with `sprintf`. The caller owns the array, and after the call it can read the result:
```c
void greet(char *out, char *name) {
    sprintf(out, "Hello, %s!", name);
}

char message[32];
greet(message, "Ada");
printf("%s\n", message); // prints "Hello, Ada!"
```
In these exercises `string.h` is already included above your code, so `strcmp` can be used to compare the result.

---

`%x` prints an integer in hexadecimal with lowercase letters, and `%X` does the same with uppercase letters. `%c` takes an integer character code and prints the character it stands for, so `%c` with `65` prints `A`:
```c
printf("%x %X %c\n", 31, 31, 66); // prints "1f 1F B"
```

---

A number between `%` and the letter sets the minimum **width** of the field. The value is padded with spaces on the left, and **flags** placed right after the `%` change the padding:
```c
printf("[%5d]\n", 42);  // prints "[   42]" right-aligned in 5 columns
printf("[%-5d]\n", 42); // prints "[42   ]" the - flag aligns to the left
printf("[%05d]\n", 42); // prints "[00042]" the 0 flag pads with zeros
printf("[%+d]\n", 42);  // prints "[+42]" the + flag always shows the sign
```
A value longer than the width is never cut, the field simply grows.

---

Width and flags work with every specifier, so `%02x` prints an integer as hexadecimal padded with zeros to two digits. This is how colors are written as `#rrggbb`:
```c
printf("%02x\n", 5);   // prints "05"
printf("%02x\n", 255); // prints "ff"
```

---

A dot followed by a number sets the **precision**. For `%f` it is the number of decimals, rounded; for `%s` it is the maximum number of characters printed:
```c
printf("%.2f\n", 3.14159);    // prints "3.14"
printf("%.3s\n", "formatting"); // prints "for"
```
Width and precision can be combined: `%8.2f` prints two decimals right-aligned in 8 columns.

---

Precision is the usual way to control how a `double` looks in a string. A ratio like `0.425` becomes a percentage by multiplying by `100` and printing one decimal followed by `%%`:
```c
sprintf(out, "%.1f%%", 0.425 * 100); // out is "42.5%"
```

---

`sprintf` and `printf` **return** the number of characters written, not counting the terminating `'\0'`. This is the length of the string that was just built, without a separate `strlen` call:
```c
char buffer[32];
int length = sprintf(buffer, "%d-%d", 3, 7);
printf("%d\n", length); // prints "3"
```

---

`sprintf` has no idea how big the buffer is. `snprintf` takes the buffer size as its second argument and never writes more than `size - 1` characters plus the `'\0'`, cutting the text if needed. Its return value is the length the **complete** text would have had, so a result greater than or equal to `size` means the output was truncated:
```c
char buffer[8];
int n = snprintf(buffer, sizeof buffer, "%s", "formatting");
printf("%s %d\n", buffer, n); // prints "formatt 10"
```
`sizeof buffer` gives the size of the array in bytes, which for a `char` array is its number of elements.

---

Comparing the return value of `snprintf` with the buffer size tells whether everything fit. This is the safe pattern for building strings of unknown length:
```c
int n = snprintf(out, size, "%s", text);
if (n >= size) {
    // out holds only the first size - 1 characters of text
}
```

---

A string can be built in several steps by writing each piece right after the previous one. The return value tells where the text ends, so `buffer + n` is the address of the terminator and the next `sprintf` can continue from there:
```c
char buffer[32];
int n = sprintf(buffer, "%s", "Hello");
n += sprintf(buffer + n, ", %s", "world"); // buffer is "Hello, world", n is 12
```
Adding each return value to `n` keeps it equal to the total length of the text built so far.

---

Strings can also be combined without a format string. `strcat` from `string.h` appends a copy of its second argument to the end of the first, which must have enough free space, and `strncat` appends at most a given number of characters:
```c
char text[32] = "Hi";
strcat(text, "!!!");        // text is "Hi!!!"
strncat(text, "abcdef", 2); // text is "Hi!!!ab"
```
Both always add the terminating `'\0'` after the appended characters.

---

When there is nothing to format, `puts` prints a string followed by a newline. Unlike `printf` it does not interpret `%`, so the text is printed exactly as written:
```c
puts("Done");      // prints "Done" and a newline
puts("50% off");   // prints "50% off" and a newline
printf("50% off"); // undefined: % off is not a valid specifier
```
`puts` is the right choice for fixed text, and `printf` when values must be inserted.

---

`strncat` is useful when only a part of a string must be appended, or when the appended piece must be limited to a maximum length:
```c
char name[16] = "file";
strncat(name, ".backup", 3); // name is "file.ba"
```
When the limit is larger than the string, the whole string is appended.

---

Putting it together: a report row combines a left-aligned text field, a separator and a right-aligned number with a fixed number of decimals, written with `snprintf` so it never overflows the buffer:
```c
snprintf(out, size, "%-6s|%5.1f", "Ada", 9.5); // out is "Ada   |  9.5"
```
As long as every value fits its width, all rows have the same length, so the columns line up when the rows are printed one under the other.
