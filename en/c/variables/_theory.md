Variables are containers for storing data values.
Every variable in C is an object and like other programming languages, C has commands for declaring a variable.
To create a variable, we need to give it a **type** and a **name** keeping in mind that it must not contain spaces.
A variable is created the moment you first assign a value to it.
An example of a variable creation named `x` is:
```c
int x = 1;
```
In this way we have assigned the value `1` to the _integer_ variable named `x`.
If we print the variable `x` we get back the number `1`:
```c
>>> printf("%i\n", x);
1
```

---

Variables are called in this way because the value they store can change.
We can update `x` by using `=` and giving it a new value.
```c
>>> x = 1;
>>> printf("%i\n", x);
1
>>> x = 2;
>>> printf("%i\n", x);
2
```

---

We can also give variables the values of other variables. Here, we can give to the `y` variable the value of `x`
```c
>>> int x = 5;
>>> int y = x;
>>> printf("%i\n", y);
5
```

---

When we update a variable, it forgets its previous value.
Here we can display the `x` variable twice and see how its value updates.
```c
>>> int x = 5;
>>> printf("%i\n", x);
5
>>> x = 10;
>>> printf("%i\n", x);
10
```

---

In C string variables can be declared only by using double quotes:
```c
char x[] = "May";
```

---

If we want a variable name with multiple words, we use **snake case**.
It means using `_` to connect the additional words.
