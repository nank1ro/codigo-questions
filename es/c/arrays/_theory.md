Los arrays son un tipo de dato que puedes usar para almacenar una colección de diferentes piezas de información como una secuencia bajo un único nombre de variable.
Un array almacena múltiples valores de un único tipo y usa **índices** para distinguir estos valores.
Puedes asignar elementos a un array con una expresión de la forma:
```
data_type array_name[array_size] = {item1, item2};
```
`data_type` es el tipo de dato que usarás para el array, por ejemplo `int`, `double`, etc.
`array_name` es el nombre de la variable que almacena los elementos.
`array_size` es el tamaño máximo que el array puede tener.
Finalmente, `item1` e `item2` son los valores que queremos guardar en el array

---

Puedes acceder a un elemento individual del array por su índice.
Un índice es como una dirección que identifica la posición del elemento en el array.
El índice aparece directamente después del nombre del array, entre corchetes, así:
```
list_name[index];
```

Los índices de arrays comienzan con `0`, **¡no** con `1`! Accedes al primer elemento de un array así: `list_name[0]`.
El segundo elemento de un array está en el índice 1: `list_name[1]`.

---

¡Un índice de lista se comporta como cualquier otro nombre de variable! Puede usarse tanto para acceder como para asignar valores.
Viste cómo acceder a un índice de lista así:
```c
int numbers[4] = {5, 6, 7, 8};
numbers[0]; // Obtiene el valor 5
```
Así es como funciona una asignación:
```c
int numbers[4] = {5, 6, 7, 8};
numbers[0] = 1;
printf("%d\n", numbers[0]); // imprime el nuevo valor 1
```

---

Puedes calcular la longitud en bytes de un array obteniendo el `sizeof` del array, luego necesitas dividirlo por el tamaño de un elemento.
Funciona porque cada elemento en el array tiene el mismo tipo, y por lo tanto el mismo tamaño.
La *longitud* resultante es el número de elementos que contiene

---

Un array en C debe tener una longitud fija.
No puedes agregar elementos al final de un array después de declarar su tamaño.

---

En programación C, puedes crear un array de arrays.
Estos arrays se conocen como arrays multidimensionales, por ejemplo:
```c
int numbers[2][3] = {{1, 2, 3}, {4, 5, 6}};
```
