Toda variable vive en algún lugar de la memoria, y ese lugar tiene un número llamado su **dirección**. El operador `&`, que se lee "dirección de", da la dirección de una variable:
```c
int x = 42;
printf("%p\n", &x); // imprime algo como 0x7ffd5c3e9a4c
```
El especificador `%p` imprime una dirección; el número exacto cambia de una ejecución a otra, así que los programas nunca dependen de él.
Una dirección se guarda en una variable **puntero**. Un puntero se declara con el tipo al que apunta seguido de `*`:
```c
int *p = &x; // p es un puntero a int, y guarda la dirección de x
```
Ahora se dice que `p` **apunta a** `x`. Dos punteros son iguales cuando guardan la misma dirección, así que `p == &x` es verdadero.

---

Un puntero por sí solo es solo una dirección. Para leer el valor guardado en esa dirección **desreferencias** el puntero con el operador `*`:
```c
int x = 42;
int *p = &x;
printf("%d\n", *p); // imprime "42"
```
`*p` significa "el valor al que `p` apunta", y es un `int` como la propia `x`. El mismo símbolo `*` tiene dos papeles: en una declaración `int *p` dice "esto es un puntero", en una expresión `*p` sigue el puntero hasta el valor.

---

Un puntero desreferenciado también puede **asignarse**. Escribir en `*p` guarda el nuevo valor en la dirección que contiene `p`, así que la variable a la que apunta cambia:
```c
int x = 5;
int *p = &x;
*p = 10;
printf("%d\n", x); // imprime "10"
```
`x` y `*p` son dos nombres para la misma memoria. Asignar a `p` sin el `*` cambiaría en cambio **qué dirección** contiene el puntero, no el valor guardado en ella.

---

Un puntero que todavía no apunta a nada debe contener `NULL`, una constante especial definida en `stdio.h` y `stddef.h` que significa "sin dirección":
```c
int *p = NULL;
```
Desreferenciar un puntero `NULL` es un error en tiempo de ejecución que hace que el programa se bloquee, así que un puntero que puede ser `NULL` se comprueba antes de usarlo:
```c
if (p != NULL) {
    printf("%d\n", *p);
}
```
Como `NULL` es cero, `if (p)` es una abreviatura habitual de `if (p != NULL)`. Un puntero declarado sin inicializador contiene basura, no `NULL`, así que inicializa siempre los punteros.

---

Un puntero puede apuntar a cualquier tipo: `double *`, `char *`, `bool *` y así sucesivamente. El tipo de la declaración le dice al compilador cuántos bytes leer cuando se desreferencia el puntero y qué significan:
```c
double price = 9.5;
double *p = &price;
*p = *p * 2; // price ahora vale 19.0
```
Un puntero debe coincidir con el tipo de la variable a la que apunta; `int *p = &price;` es rechazado por el compilador. `NULL` es el único valor que sirve para un puntero de cualquier tipo.

---

Un puntero a `char` funciona como cualquier otro puntero: contiene la dirección de un único carácter, y `*p` lee o escribe ese carácter:
```c
char grade = 'B';
char *p = &grade;
*p = 'A';
printf("%c\n", grade); // imprime "A"
```
Leer a través de un puntero y escribir a través de él se pueden mezclar libremente: `*p = *p + 1` convierte `'A'` en `'B'`.

---

Un puntero guarda una dirección, y todas las direcciones tienen el mismo tamaño en una máquina dada, sin importar qué tipo se guarde en ellas. El `sizeof` de un puntero es por tanto el mismo para `char *`, `int *` y `double *`: `8` bytes en un sistema de 64 bits, `4` en uno de 32 bits:
```c
printf("%zu\n", sizeof(int *));  // imprime "8" en 64 bits
printf("%zu\n", sizeof(double)); // imprime "8"
printf("%zu\n", sizeof(char));   // imprime "1"
```
No confundas el tamaño del puntero con el tamaño de lo que apunta: `sizeof(p)` es el tamaño de la dirección, `sizeof(*p)` es el tamaño del valor.

---

El nombre de un array usado en una expresión da la dirección de su **primer elemento**, así que puede asignarse directamente a un puntero:
```c
int numbers[3] = {10, 20, 30};
int *p = numbers; // igual que &numbers[0]
```
Sumar un entero a un puntero lo avanza tantos **elementos**, no bytes: `p + 1` es la dirección de `numbers[1]`, y `*(p + 1)` es `20`. El compilador escala el paso según el tamaño del tipo.
La indexación también funciona sobre punteros: `p[i]` se define como `*(p + i)`, así que `p[2]` es `30`. Esto se llama **aritmética de punteros**.

---

Como `p + 1` es el siguiente elemento, `p++` mueve un puntero al siguiente elemento in situ. Un bucle puede recorrer un array avanzando un puntero en lugar de un índice:
```c
int *p = values;
for (int i = 0; i < 3; i++) {
    printf("%d\n", *p);
    p++;
}
```
En cada vuelta imprime el elemento al que `p` apunta, y luego avanza `p` un elemento hacia delante.

---

Cuando un array se pasa a una función **decae** a un puntero a su primer elemento. Por esto los parámetros `int values[]` e `int *values` significan exactamente lo mismo, y por esto la función no puede conocer la longitud por sí sola: solo recibe una dirección.
Los punteros al mismo array se pueden comparar y restar. `end - start` es el número de elementos entre ellos, y un bucle puede mover un puntero de una dirección a otra:
```c
for (int *p = start; p < end; p++) {
    printf("%d\n", *p);
}
```
Pasar `numbers` y `numbers + 3` describe los primeros tres elementos sin un parámetro de tamaño aparte.

---

Los argumentos de una función se pasan **por valor**: la función recibe una copia, y asignar a un parámetro nunca cambia la variable de quien llama. Para permitir que una función cambie una variable, pasa la dirección de la variable y desreferencia el puntero dentro:
```c
void reset(int *p) {
    *p = 0;
}

int counter = 7;
reset(&counter); // counter ahora vale 0
```
El ejemplo clásico es intercambiar dos variables, que necesita una copia temporal de un valor mientras el otro se sobrescribe.

---

Una función solo puede `return` (devolver) un valor. Para entregar más, toma punteros a variables de quien llama y escribe los resultados a través de ellos. Estos parámetros se llaman **parámetros de salida**:
```c
void min_max(int a, int b, int *min, int *max) {
    *min = a;
    *max = b;
    if (a > b) {
        *min = b;
        *max = a;
    }
}

int lo, hi;
min_max(4, 9, &lo, &hi); // lo vale 4, hi vale 9
```
Quien llama declara las variables, pasa sus direcciones y las encuentra rellenadas después de la llamada. Muchas funciones estándar usan este patrón, que es por lo que `scanf("%d", &n)` necesita el `&`.

---

Un puntero a un struct accede a los miembros con la flecha `->`, y la dirección de un struct guardado en un array se toma con `&items[i]`. Una función también puede **devolver** un puntero, por ejemplo al elemento que encontró:
```c
Player *first_active(Player players[], int size) {
    for (int i = 0; i < size; i++) {
        if (players[i].active) {
            return &players[i];
        }
    }
    return NULL;
}
```
Quien llama luego lee los miembros a través del puntero devuelto con `->`, tras comprobar que no es `NULL`. Devolver un puntero evita copiar el struct y permite a quien llama modificar el elemento original.

---

`const` puede proteger el valor o el puntero, según dónde se escriba:
```c
const int *p = &a; // puntero a const: *p no se puede cambiar, p puede apuntar a otro lado
int *const q = &a; // puntero const: q siempre apunta a a, pero *q se puede cambiar
```
Lee la declaración de derecha a izquierda: `p` es un puntero a un `int` constante; `q` es un puntero constante a un `int`. Un puntero a const es la forma habitual de prometer que una función solo **lee** lo que recibe, como en `int sum(const int *values, int size)`. Una variable normal se le puede pasar; la promesa solo limita lo que la función puede hacer.

---

Un puntero es una variable, así que tiene su propia dirección, y esa dirección puede guardarse en un **puntero a puntero**, declarado con dos asteriscos:
```c
int x = 7;
int *p = &x;
int **pp = &p;
```
`*pp` es `p`, la dirección de `x`, y `**pp` sigue ambos pasos para llegar a `7`. Los punteros a punteros permiten a una función cambiar qué dirección contiene un puntero: recibe `&p` y asigna a `*pp`.

---

Juntándolo todo: una función que recorre un array con un puntero, guarda un puntero al mejor elemento visto hasta ahora y lo devuelve, o `NULL` cuando no hay nada que devolver:
```c
int *first_negative(int *values, int size) {
    for (int *p = values; p < values + size; p++) {
        if (*p < 0) {
            return p;
        }
    }
    return NULL;
}
```
Quien llama compara el resultado con `NULL` antes de desreferenciarlo, y puede usar `result - values` para recuperar el índice del elemento.
