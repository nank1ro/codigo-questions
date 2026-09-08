Una **enumeración** (`enum`) da nombres a un conjunto de constantes enteras relacionadas, para que puedas escribir `RED` en lugar de un número suelto.
La declaras con la palabra clave `enum`, un nombre y la lista de constantes entre llaves:
```c
enum Color { RED, GREEN, BLUE };
```
Cada constante es un entero: a menos que indiques lo contrario, la primera es `0` y cada siguiente es la anterior más uno, así que `RED` es `0`, `GREEN` es `1` y `BLUE` es `2`.
Como son enteros, las imprimes con `%d`:
```c
printf("%d\n", GREEN);
// prints "1"
```

---

La numeración continúa automáticamente para tantas constantes como enumeres: la cuarta constante es `3`, la quinta es `4` y así sucesivamente.
Los nombres suelen escribirse en mayúsculas, como otras constantes, y deben ser únicos en todo el programa: dos enumeraciones no pueden compartir el nombre de una constante.

---

También puedes darle a una constante un valor explícito con `=`; las constantes posteriores siguen contando a partir de ese valor:
```c
enum Month { JAN = 1, FEB, MAR }; // FEB is 2, MAR is 3
```
Los valores explícitos no tienen por qué ser consecutivos ni crecientes: `enum Status { OK = 200, NOT_FOUND = 404 };` es perfectamente válido.

---

Una enumeración también es un tipo: puedes declarar una variable de ese tipo escribiendo `enum` seguido del nombre de la enumeración, y asignarle una de sus constantes:
```c
enum Color favorite = GREEN;
```
Como las constantes son enteros, comparas variables de tipo enumeración con los operadores habituales:
```c
if (favorite == GREEN) {
    printf("Green it is\n");
}
```

---

Una enumeración puede ser el tipo de un parámetro de función, igual que `int`:
```c
int is_weekend(enum Day day) {
    return day == SAT || day == SUN;
}
```
Dentro de la función, un `switch` es la forma natural de tratar cada constante, porque las constantes de enumeración pueden usarse directamente como etiquetas `case`:
```c
switch (day) {
    case SAT: return 1;
    case SUN: return 1;
    default: return 0;
}
```

---

Cuando cada caso de un `switch` trata una constante, recuerda el `break` después de cada uno, de lo contrario la ejecución continúa con el siguiente caso.
Un caso `default` no es necesario si cubres todas las constantes de la enumeración.

---

Una función también puede devolver una enumeración; basta con usar el tipo enumerado como tipo de retorno y devolver una de sus constantes:
```c
enum Grade grade_for(int score) {
    if (score >= 60) {
        return PASS;
    }
    return FAIL;
}
```
Devolver una constante con nombre es mucho más claro para quien llama que devolver un `0` o un `1` sueltos.

---

Escribir `enum Color` cada vez es tedioso. Con `typedef` le das a la enumeración un nombre de tipo corto, y la enumeración en sí puede permanecer anónima:
```c
typedef enum { RED, GREEN, BLUE } Color;

Color favorite = BLUE;
```
El nuevo nombre `Color` se usa por sí solo, sin la palabra clave `enum` delante.

---

Una constante de enumeración se convierte automáticamente a `int`, así que `int n = BLUE;` es válido y almacena `2`.
El camino inverso se hace con una **conversión**, escribiendo el tipo enumerado entre paréntesis antes del entero:
```c
enum Color c = (enum Color)1; // c is GREEN
```
C no comprueba que el número coincida con una constante: `(enum Color)7` compila aunque ninguna constante sea `7`, así que valida los enteros antes de convertirlos.

---

Una operación aritmética sobre un valor de enumeración produce un `int` simple: `GREEN + 1` es `2`, no `BLUE`.
Para guardar el resultado de nuevo en una variable de enumeración o devolverlo desde una función, conviértelo al tipo enumerado:
```c
enum Color after_green = (enum Color)(GREEN + 1); // BLUE
```
Combinado con el operador de resto `%`, esto te permite recorrer cíclicamente las constantes y volver a la primera.

---

Un truco habitual es añadir una constante extra al final de la enumeración, normalmente llamada `COUNT`: como la numeración empieza en `0`, su valor es exactamente el número de constantes reales que la preceden.
```c
enum Day { MON, TUE, WED, DAY_COUNT }; // DAY_COUNT is 3
```
Ese centinela te permite recorrer todas las constantes sin fijar el número a mano, y sigue siendo correcto cuando añades constantes antes de él:
```c
for (int d = MON; d < DAY_COUNT; d++) {
    printf("%d\n", d);
}
```

---

El centinela `COUNT` también es el tamaño perfecto para un array con una casilla por constante, y las constantes se convierten en índices legibles dentro de él:
```c
enum Fruit { APPLE, BANANA, CHERRY, FRUIT_COUNT };

int stock[FRUIT_COUNT] = {10, 4, 7};
printf("%d\n", stock[BANANA]); // prints "4"
```
Un bucle de `0` a `FRUIT_COUNT` visita cada casilla, y el índice del bucle puede convertirse de nuevo a `enum Fruit` cuando necesites devolverlo.

---

C no ofrece ninguna forma integrada de obtener el nombre de una constante de enumeración: `printf("%d\n", SUMMER)` imprime `2`, no `Summer`. La solución habitual es una pequeña función con un `switch` que devuelve la cadena correspondiente a cada constante.

---

Los valores de enumeración pueden guardarse en arrays como cualquier otro entero: `enum Fruit basket[] = {APPLE, APPLE, CHERRY};` contiene tres frutas, y cada elemento puede compararse con una constante.
