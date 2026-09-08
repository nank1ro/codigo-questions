Los **operadores de comparación** comparan dos valores y producen una respuesta: `1` cuando la comparación se cumple y `0` cuando no.
El operador **igual** `==` comprueba si dos valores son iguales, el operador **distinto** `!=` comprueba si difieren:
```c
int a = 7, b = 3;
printf("%d\n", a == b);
// imprime "0"
printf("%d\n", a != b);
// imprime "1"
```
Cuidado: `==` (dos signos) compara, mientras que un único `=` asigna un valor.

---

Los demás operadores de comparación comprueban el orden de dos valores:
- `<` menor que, `>` mayor que
- `<=` menor o igual que, `>=` mayor o igual que
```c
printf("%d\n", 3 < 5);  // imprime "1"
printf("%d\n", 5 >= 6); // imprime "0"
```
Una función puede devolver una comparación directamente, ya que el resultado es un simple `int`:
```c
int is_big(int n) {
    return n > 100;
}
```

---

En C, el resultado de una comparación no es un tipo especial: es un `int` cuyo valor es exactamente `1` (verdadero) o `0` (falso).
Eso significa que puedes almacenarlo en una variable `int` como cualquier otro número:
```c
int n = 42;
int big = n > 100; // big es 0
```
No existe la palabra `true`/`false` en la salida: `printf("%d", 2 == 2)` imprime `1`.

---

Los **operadores lógicos** combinan comparaciones. El operador **and** `&&` da `1` solo cuando ambos lados son verdaderos:
```c
int age = 25;
printf("%d\n", age >= 18 && age < 65); // imprime "1"
```
No encadenes comparaciones como en matemáticas: `1 <= x <= 10` se evalúa como `(1 <= x) <= 10`, que compara un `0` o `1` con `10` y siempre es verdadero.
Escribe siempre las dos comparaciones explícitamente y únelas con `&&`.

---

El operador **or** `||` da `1` cuando al menos un lado es verdadero, y `0` solo cuando ambos lados son falsos:
```c
int day = 1;
printf("%d\n", day == 1 || day == 7); // imprime "1"
```
Cada lado debe ser una comparación completa: `day == 6 || 7` no significa "6 o 7" (verás por qué más adelante).

---

El operador **not** `!` invierte un resultado: `!1` es `0` y `!0` es `1`.
Se coloca delante de la expresión, así que usa paréntesis para negar toda una comparación:
```c
int n = 5;
printf("%d\n", !(n > 3)); // imprime "0"
```
Sin los paréntesis, `!n > 3` calcularía primero `!n` y luego lo compararía con `3`.

---

Los operadores lógicos no solo funcionan con `0` y `1`: en C **cualquier valor distinto de cero cuenta como verdadero** y solo `0` cuenta como falso.
Así, `5 && 1` es `1`, `0 || -3` es `1`, y `!` convierte cualquier valor distinto de cero en `0`:
```c
printf("%d\n", !7); // imprime "0"
printf("%d\n", !0); // imprime "1"
```
Por eso `day == 6 || 7` siempre es verdadero: `7` por sí solo ya es un valor verdadero.

---

`&&` y `||` usan **evaluación de cortocircuito**: se detienen en cuanto se conoce el resultado.
- con `&&`, si el lado izquierdo es `0`, el lado derecho nunca se evalúa
- con `||`, si el lado izquierdo es verdadero, el lado derecho nunca se evalúa

Esto te permite proteger una operación peligrosa con una comprobación colocada a su izquierda:
```c
int safe = divisor != 0 && value / divisor > 2;
```
Cuando `divisor` es `0`, la división nunca se ejecuta.

---

La evaluación de cortocircuito también omite llamadas a funciones: en `0 && check()` la función `check` nunca se llama, así que cualquier efecto secundario que tenga (como actualizar un contador) no ocurre.

---

Los operadores tienen una **precedencia** que decide qué se calcula primero:
1. `!` se aplica primero
2. luego las comparaciones relacionales `<`, `>`, `<=`, `>=`
3. luego las comparaciones de igualdad `==`, `!=`
4. luego `&&`
5. luego `||`

Así, `a > 0 && a < 10` no necesita paréntesis: ambas comparaciones se calculan antes que `&&`.
Y `x == 1 || y == 2 && z == 3` significa `x == 1 || (y == 2 && z == 3)`, porque `&&` liga más fuerte que `||`.

---

Un `char` es un entero pequeño, así que los caracteres se pueden comparar con los mismos operadores.
Compara con un literal de carácter entre comillas simples:
```c
char answer = 'y';
printf("%d\n", answer == 'y'); // imprime "1"
```
Las comillas dobles crearían una cadena, que no se puede comparar de esta forma.

---

Como los caracteres son números, `<` y `>` comparan sus códigos, y caracteres consecutivos como `'a'`, `'b'`, `'c'` o `'0'`, `'1'`, `'2'` tienen códigos consecutivos.
Por eso, comprobar un rango en caracteres funciona exactamente igual que en números:
```c
int is_lower(char c) {
    return c >= 'a' && c <= 'z';
}
```

---

Un error clásico de C es escribir `=` cuando se quería `==`. El código sigue compilando, porque una asignación es una expresión cuyo valor es el valor asignado:
```c
int x = 5;
if (x = 0) { ... } // asigna 0 a x, la condición es 0 (falso)
if (x = 3) { ... } // asigna 3 a x, la condición es 3 (verdadero)
```
La mayoría de los compiladores avisan de esto, así que lee las advertencias cuando una condición se comporte de forma extraña.

---

La condición de un `if` es simplemente una expresión que se trata como verdadera cuando es distinta de cero, así que las comparaciones y los operadores lógicos encajan de forma natural:
```c
if (n < 0) {
    printf("negative\n");
} else if (n == 0) {
    printf("zero\n");
}
```
También puedes almacenar primero el resultado y probar la variable: `int ok = n > 0; if (ok) { ... }`.

---

Un bucle `while` sigue ejecutándose mientras su condición sea distinta de cero, así que una comparación decide cuándo se detiene:
```c
int i = 0;
while (i < 3) {
    printf("%d\n", i);
    i++;
}
// imprime 0, 1, 2
```
Elegir entre `<` y `<=` cambia si se incluye el último valor.

---

Desde C99, la cabecera `stdbool.h` proporciona el tipo `bool` y las constantes `true` (`1`) y `false` (`0`):
```c
#include <stdbool.h>

bool ready = true;
bool done = count == 10;
```
Un `bool` sigue siendo un entero por dentro: al imprimirlo con `%d` se muestra `1` o `0`, y funciona con `&&`, `||` y `!` como cualquier resultado de comparación.
Usar `bool` deja más claro el propósito de una función que devolver un simple `int`.

---

Un parámetro `bool` se puede usar directamente como operando de `&&` o `||`, sin compararlo con `true`: escribe `age >= 18 && citizen`, no `citizen == true`.

---

Cuando una condición mezcla `&&` y `||`, añade paréntesis alrededor de cada grupo aunque la precedencia ya haría lo correcto: hace que la regla sea legible de un vistazo.
```c
bool free_entry = (age < 12 || age >= 65) && !holiday;
```
