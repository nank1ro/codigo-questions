We know how to repeat code using a `while` loop.
Like this program repeating statements to display `hello`
```c
int counter = 0;

while (counter < 5) {
	printf("Hello\n");
	counter++;
}
```
But we can do the same with `for` loops:
```c
for (int i = 0; i < 5; i++) {
	printf("Hello\n");
}
```

---

In a `for` loop we can specify how many times we'd like our loop to run

---

We can use `<` to loop until the next number excluded, or `<=` to loop until the next number included

---

The variable called `i` is the counter variable.
We can give it the name we want.
It counts what repetition of the loop we're currently on
