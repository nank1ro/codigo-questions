C has no dedicated string type: a **string** is an array of `char` that ends with a special character, the **null terminator** `'\0'`.
The easiest way to create one is a string literal between double quotes:
```c
char name[] = "Codigo";
```
The compiler counts the characters and adds the `'\0'` at the end for you.
To print a string use the `%s` placeholder:
```c
printf("%s\n", name);
// prints "Codigo"
```

---

The null terminator takes space in memory: the literal `"hi"` occupies 3 bytes, `'h'`, `'i'` and `'\0'`.
When you declare the size yourself, always leave room for it:
```c
char word[6] = "hello"; // 5 letters + '\0'
```
Without the terminator, C has no way of knowing where the string ends.

---

The header `string.h` provides functions that work on strings.
`strlen` returns the number of characters before the null terminator (the terminator itself is not counted):
```c
strlen("hello"); // 5
```
A function that receives a string declares the parameter as `char *text`, a pointer to the first character.
In these exercises `string.h` and `ctype.h` are already included above your code.

---

Since a string is an array, every character has an index starting from `0`:
```c
char word[] = "Coding";
word[0]; // 'C'
word[5]; // 'g'
```
A single character is printed with `%c`. Characters can also be replaced:
```c
word[0] = 'K'; // word is now "Koding"
```

---

Because every string ends with `'\0'`, you can walk through it without knowing its length in advance: keep going while the current character is not the terminator.
```c
for (int i = 0; text[i] != '\0'; i++) {
    printf("%c\n", text[i]);
}
```

---

An array cannot be assigned with `=` after its declaration:
```c
char copy[20];
copy = "Codigo"; // error
```
To copy a string use `strcpy(destination, source)` from `string.h`.
The destination must be large enough to hold all the characters plus the `'\0'`.

---

`strcat(destination, source)` appends `source` to the end of `destination`:
```c
char text[20] = "Hello";
strcat(text, " World");
// text is now "Hello World"
```
As with `strcpy`, the destination array must have enough room for the result.

---

Two strings cannot be compared with `==`: that would compare their addresses in memory, not their characters.
Use `strcmp(first, second)` instead, which returns `0` when the two strings contain exactly the same characters:
```c
strcmp("cat", "cat"); // 0
strcmp("cat", "dog"); // not 0
```

---

`strcmp` compares the strings character by character using their character codes.
The result is negative when the first string comes before the second, positive when it comes after, and `0` when they are equal:
```c
strcmp("a", "b"); // negative
strcmp("b", "a"); // positive
```

---

`strncpy(destination, source, n)` copies at most `n` characters.
If `source` is longer than `n`, no `'\0'` is written: you have to terminate the result yourself.
```c
char prefix[10];
strncpy(prefix, "Codigo", 3);
prefix[3] = '\0'; // prefix is "Cod"
```

---

The header `ctype.h` provides functions that work on a single character.
`toupper(c)` returns the uppercase version of a letter and `tolower(c)` the lowercase one; any other character is returned unchanged:
```c
char letter = toupper('a'); // 'A'
```

---

A string is passed to a function as a pointer, so a function receiving `char *text` can change the caller's characters in place.
Combining a loop until `'\0'` with `toupper` converts a whole string:
```c
text[i] = toupper(text[i]);
```

---

`sprintf` works like `printf`, but writes the formatted text into a char array instead of the screen:
```c
char buffer[30];
sprintf(buffer, "%d items", 3); // buffer is "3 items"
```
The buffer must be large enough for the whole text and its `'\0'`.

---

`sprintf` is a handy way to turn a number into text: once it is in a buffer, every string function can work on it.
