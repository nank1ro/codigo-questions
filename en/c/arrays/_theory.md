Arrays are a datatype you can use to store a collection of different pieces of information as a sequence under a single variable name.
An array stores multiple values of a single type and uses **indexes** to distinguish these values.
You can assign items to an array with an expression of the form:
```
data_type array_name[array_size] = {item1, item2};
```
`data_type` is the type of data you'll be using for the array, for example `int`, `double`, etc.
`array_name` is the name of the variable that stores the items.
`array_size` is the maximum size that the array can have.
Finally, `item1` and `item2` are the values that we want to save in the array

---

You can access an individual item of the array by its index.
An index is like an address that identifies the item's place in the array.
The index appears directly after the array name, in between brackets, like this:
```
list_name[index];
```

Array indices begin with `0`, **not** `1`! You access the first item in a array like this: `list_name[0]`.
The second item in a array is at index 1: `list_name[1]`.

---

A list index behaves like any other variable name! It can be used to access as well as assign values.
You saw how to access a list index like this:
```c
int numbers[4] = {5, 6, 7, 8};
numbers[0]; // Gets the value 5
```
This is how an assignment works:
```c
int numbers[4] = {5, 6, 7, 8};
numbers[0] = 1;
printf("%d\n", numbers[0]); // prints the new value 1
```

---

You can calculate the length in bytes of an array obtaining the `sizeof` the array, then you need to divide it by the size of one element.
It works because every item in the array has the same type, and as such the same size.
The resulting *length* is the number of items it contains

---

An array in C must have a fixed length.
You can't add items to the end of an array, after declaring its size.

---

In C programming, you can create an array of arrays.
These arrays are known as multidimensional arrays, for example:
```c
int numbers[2][3] = {{1, 2, 3}, {4, 5, 6}};
```
