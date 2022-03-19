You might have considered the situation where you would like to reuse a piece of code, just with a few different values.
Instead of rewriting the whole code, it's much cleaner to define a function, which can then be used repeatedly.
In C we use the `return_type` followed by the `function` name, for example:
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

The parentheses in the __function definition__ don't have to be empty if we want to specify parameters

---

Sometimes we want a function to __return__ a value.
Well, there's the `return` keyword.

---

Functions can have multiple input parameters, which are written within the function's parentheses, separated by commas.
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

In functions we can add an _optional comment_ that explains what the function does:
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
We can use `//` for a single line comment and `/* */` for a multi line comment
