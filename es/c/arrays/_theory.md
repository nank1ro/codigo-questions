Los arreglos son un tipo de dato que puedes usar para almacenar una colección de diferentes piezas de información como una secuencia bajo un solo nombre de variable.
Un arreglo almacena múltiples valores de un solo tipo y usa **índices** para distinguir estos valores.
Puedes asignar elementos a un arreglo con una expresión de la forma:
```
data_type array_name[array_size] = {item1, item2};
```
`data_type` es el tipo de dato que usarás para el arreglo, por ejemplo `int`, `double`, etc.
`array_name` es el nombre de la variable que almacena los elementos.
`array_size` es el tamaño máximo que el arreglo puede tener.
Finalmente, `item1` y `item2` son los valores que queremos guardar en el arreglo

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
