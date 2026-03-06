你可能遇到过这样的情况：你想重复使用一段代码，只是使用不同的值。
与其重写整段代码，不如定义一个函数，这样可以重复调用，代码也更加简洁。
在 C 语言中，我们使用 `return_type`（返回类型）后跟 `function`（函数）名称，例如：
```c
void say_hello() {
    printf("Hello!\n");
}

int main() {
    say_hello();
    // prints "Hello!"
    return 0;
}
```

---

如果我们想指定参数，__函数定义__中的括号不必为空

---

有时我们希望函数__返回__一个值。
这时可以使用 `return` 关键字。

---

函数可以有多个输入参数，这些参数写在函数的括号内，用逗号分隔。
```c
void say_hello(char *name, bool new_user) {
  char greet[40] = "Hello ";
  strcat(greet, name);
  if (new_user) {
    strcat(greet, "! Welcome on board :)");
  }
  printf("%s\n", greet);
}

int main() {
    // prints "Hello Tom"
    say_hello("Tom", true);
    return 0;
};
```

---

在函数中，我们可以添加一个_可选的注释_来解释函数的功能：
```c
/*
 * Function:  hello_world
 * --------------------
 * prints "Hello, World!" to the screen
 */
function hello_world() {
    printf("Hello, World!\n");
}
```
我们可以使用 `//` 进行单行注释，使用 `/* */` 进行多行注释
