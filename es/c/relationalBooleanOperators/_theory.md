Los **operadores relacionales** comparan dos valores. El resultado no es un tipo especial: es un `int` que vale `1` cuando la comparación se cumple y `0` cuando no. C tiene seis de ellos:
```c
printf("%d\n", 5 == 5); // equal: prints "1"
printf("%d\n", 5 != 5); // not equal: prints "0"
printf("%d\n", 3 < 5);  // less than: prints "1"
printf("%d\n", 3 > 5);  // greater than: prints "0"
printf("%d\n", 5 <= 5); // less than or equal: prints "1"
printf("%d\n", 4 >= 5); // greater than or equal: prints "0"
```
Como el resultado es un `int`, se imprime con `%d` y puede almacenarse en una variable `int` como cualquier otro número.

---

Una función puede devolver una comparación directamente: quien la llama recibe `1` o `0`.
```c
int is_big(int n) {
    return n > 100;
}

printf("%d\n", is_big(250)); // prints "1"
```
Elegir entre `>` y `>=` (o `<` y `<=`) decide si el valor del límite cuenta: `n >= 100` es `1` para `100`, `n > 100` es `0`.

---

El error más común de C es escribir `=` cuando se quería `==`. Un único `=` es una **asignación**, y en C una asignación es una expresión cuyo valor es el valor asignado:
```c
int x = 3;
printf("%d\n", x == 7); // compares: prints "0", x is still 3
printf("%d\n", x = 7);  // assigns: prints "7", x is now 7
```
El código con `=` sigue compilando, así que una condición escrita como `if (x = 0)` asigna `0` a `x` silenciosamente en lugar de comprobarla. La mayoría de los compiladores muestran una advertencia por esto: léela.

---

Los **operadores lógicos** combinan condiciones. El operador **and** `&&` da `1` solo cuando ambos lados son verdaderos, el operador **or** `||` da `1` cuando al menos un lado es verdadero:
```c
int t = 25;
printf("%d\n", t > 20 && t < 30); // prints "1"
printf("%d\n", t < 20 || t > 30); // prints "0"
```
En C **cualquier valor distinto de cero cuenta como verdadero** y solo `0` cuenta como falso, así que `5 && 1` es `1` y `0 || -3` es `1`. El resultado de `&&` y `||` es siempre exactamente `1` o `0`.

---

Una variable que contiene `0` o un valor distinto de cero puede usarse como condición por sí sola: `holiday` por sí solo significa "holiday es distinto de cero", no hace falta escribir `holiday != 0`.
```c
int is_open(int weekday, int holiday) {
    return weekday && !holiday;
}
```
El operador **not** `!` invierte una condición: `!0` es `1` y `!` de cualquier valor distinto de cero es `0`.

---

Como `!` convierte cualquier valor distinto de cero en `0` y `0` en `1`, aplicarlo dos veces normaliza un valor a exactamente `0` o `1`: `!!42` es `1`, `!!0` es `0`.
```c
int count = 3;
printf("%d %d\n", !count, !!count); // prints "0 1"
```
Esto es útil cuando una función devuelve un número arbitrario distinto de cero y quieres un `1` limpio.

---

Desde C99 el encabezado `stdbool.h` proporciona el tipo `bool` y las constantes `true` (que es `1`) y `false` (que es `0`):
```c
#include <stdbool.h>

bool open = true;
bool full = 3 > 5;
printf("%d %d\n", open, full); // prints "1 0"
```
Un `bool` sigue siendo un entero por debajo: se imprime con `%d`, y funciona con `&&`, `||` y `!` exactamente como el resultado de una comparación. Solo deja la intención más clara que un `int` normal.

---

Una función que responde a una pregunta de sí/no debe devolver `bool`. Un parámetro `bool` ya es una condición, así que úsalo directamente como operando de `&&` o `||`: escribe `age >= 18 && citizen`, no `citizen == true`.
```c
bool can_enter(int age, bool member) {
    return age >= 16 && member;
}
```
`stdbool.h` ya está incluido encima de tu código en estos ejercicios.

---

`&&` y `||` usan **evaluación de cortocircuito**: se detienen en cuanto se conoce el resultado.
- con `&&`, si el lado izquierdo es `0`, el lado derecho nunca se evalúa
- con `||`, si el lado izquierdo es distinto de cero, el lado derecho nunca se evalúa

Esto te permite proteger una operación peligrosa con una comprobación colocada a su izquierda:
```c
int ok = count != 0 && total / count > 2;
```
Cuando `count` es `0`, la división nunca se ejecuta, así que el programa no se bloquea.

---

La evaluación de cortocircuito también omite llamadas a funciones: en `1 || check()` la función `check` nunca se llama, así que cualquier efecto secundario que tenga (como actualizar un contador) no ocurre.
```c
int calls = 0;

int check() {
    calls++;
    return 1;
}
```
Ten esto en cuenta cuando una función al lado derecho de `&&` o `||` haga algo de lo que dependas.

---

Los operadores tienen una **precedencia** que decide qué se calcula primero:
1. `!` se aplica primero
2. luego las comparaciones relacionales `<`, `>`, `<=`, `>=`
3. luego las comparaciones de igualdad `==`, `!=`
4. luego `&&`
5. luego `||`

Así, `a > 0 && a < 10` no necesita paréntesis, y `a && b || c` significa `(a && b) || c`, porque `&&` liga más fuerte que `||`. Usa paréntesis para forzar una agrupación diferente o simplemente para hacer la intención legible.

---

Un `char` es un entero pequeño, así que los caracteres se comparan con los mismos operadores. Compara contra un literal de carácter entre comillas simples: `"a"` con comillas dobles es una cadena, que no se puede comparar de esta manera.
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // prints "1"
```
Los caracteres consecutivos como `'0'`, `'1'`, ... `'9'` o `'a'`, `'b'`, ... `'z'` tienen códigos consecutivos, así que una comprobación de rango sobre caracteres funciona exactamente como una sobre números:
```c
bool is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

No encadenes comparaciones como en matemáticas. `1 <= x <= 10` compila, pero se evalúa como `(1 <= x) <= 10`: la primera comparación da `0` o `1`, y eso se compara después con `10`, así que toda la expresión es siempre `1`.
```c
int x = 20;
printf("%d\n", 1 <= x <= 10);       // prints "1" (wrong!)
printf("%d\n", 1 <= x && x <= 10);  // prints "0"
```
Escribe siempre ambas comparaciones explícitamente y únelas con `&&`.

---

Cuando una condición mezcla `&&` y `||`, agrupa cada parte con paréntesis incluso cuando la precedencia ya haría lo correcto: la regla se vuelve legible de un vistazo.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
El operador de resto `%` se combina naturalmente con `==`: `n % 4 == 0` es `1` cuando `n` es divisible por `4`.
