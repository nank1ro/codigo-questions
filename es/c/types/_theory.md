C es un lenguaje **de tipado estático**: cada variable se declara con un tipo que determina qué puede almacenar y cuánta memoria ocupa.
Los tres tipos que más usarás son:
- `int` para números enteros, como `30` o `-4`
- `double` para números con parte decimal, como `1.75`
- `char` para un único carácter, escrito entre comillas simples como `'A'`

Cada tipo tiene su propio **especificador de formato** de `printf`: `%d` imprime un `int`, `%f` imprime un `double` (con seis decimales por defecto) y `%c` imprime un `char`:
```c
int age = 30;
double height = 1.75;
char initial = 'A';
printf("%d %f %c\n", age, height, initial);
// imprime "30 1.750000 A"
```
Usar el especificador equivocado para un tipo imprime basura, así que hazlos coincidir siempre.

---

C tiene dos tipos de punto flotante: `float` (precisión simple, unos 7 dígitos significativos) y `double` (precisión doble, unos 15 dígitos significativos).
Un literal decimal como `1.75` es un `double`; para escribir un literal `float` añade el sufijo `f`, como en `1.75f`.
Prefiere `double` a menos que la memoria sea escasa: es el tipo por defecto y es más preciso.
```c
double pi = 3.14159;
float ratio = 0.5f;
```
Una función que devuelve un resultado decimal debería declarar `double` como tipo de retorno, y los parámetros `double` aceptan tanto argumentos enteros como decimales:
```c
double half(double x) {
    return x / 2;
}
```

---

`%f` imprime seis decimales, que rara vez es lo que quieres. Coloca una precisión entre `%` y `f` para elegir cuántos decimales mostrar: `%.2f` imprime dos decimales, `%.1f` imprime uno, y el valor se **redondea**, no se trunca:
```c
double price = 9.987;
printf("%.2f\n", price); // imprime "9.99"
printf("%.1f\n", price); // imprime "10.0"
```
Un `float` se imprime con los mismos especificadores que un `double`: al pasarlo a `printf` se convierte automáticamente a `double`.

---

El resultado de `/` depende de los tipos de sus operandos.
Cuando **ambos** operandos son enteros, el resultado es un entero y la parte decimal se descarta: `7 / 2` es `3`, no `3.5`.
Cuando **al menos uno** de los operandos es un valor de punto flotante, la división conserva los decimales: `7 / 2.0` es `3.5`.
```c
printf("%d\n", 7 / 2);     // imprime "3"
printf("%f\n", 7 / 2.0);   // imprime "3.500000"
```
Escribir el literal como `2.0` en lugar de `2` es la forma más simple de forzar una división de punto flotante.

---

C convierte entre tipos numéricos de forma **implícita** cuando un valor se asigna a una variable de un tipo diferente.
- un `int` almacenado en un `double` se amplía sin pérdida: `double d = 3;` hace que `d` valga `3.0`
- un `double` almacenado en un `int` se **trunca**: `int n = 3.99;` hace que `n` valga `3` (los compiladores suelen avisar de esto)

La conversión ocurre solo en el momento de la asignación. La expresión de la derecha se calcula primero, con sus propios tipos:
```c
double d = 7 / 2;
```
Aquí `7 / 2` es una división entera que da `3`, y solo entonces `3` se convierte en `3.0`.

---

Cuando la conversión implícita no es lo que quieres, o quieres hacerla visible, usa una **conversión explícita (cast)**: escribe el tipo destino entre paréntesis antes del valor.
```c
double x = 3.99;
int n = (int) x;   // n es 3
```
Convertir un valor de punto flotante a `int` **trunca hacia cero**: `(int) 3.99` es `3` y `(int) -2.5` es `-2`, no se realiza ningún redondeo.
El cast se aplica solo al valor justo después de él, así que `(int) x * 2` convierte primero `x` y luego multiplica.

---

Un cast es la forma estándar de obtener una división de punto flotante a partir de dos variables `int`: convierte **un operando** a `double` antes de dividir.
```c
int total = 7, count = 2;
double avg = (double) total / count; // 3.5
```
Convertir todo el resultado en su lugar, como en `(double) (total / count)`, es un error común: la división entera ya ha ocurrido y los decimales se han perdido.

---

Un `char` es en realidad un entero pequeño: almacena el **código ASCII** del carácter.
`'A'` es `65`, `'a'` es `97` y `'0'` es `48`, y los caracteres consecutivos tienen códigos consecutivos.
Por eso puedes hacer aritmética con caracteres:
- `'a' + 1` es `98`, el código de `'b'`
- `'7' - '0'` es `55 - 48`, es decir, el número `7`

El mismo valor puede imprimirse como carácter con `%c` o como número con `%d`:
```c
char c = 'A';
printf("%c %d\n", c, c); // imprime "A 65"
```

---

Las letras mayúsculas y minúsculas están separadas por `32` posiciones en la tabla ASCII: `'A'` es `65` y `'a'` es `97`.
Restar `32` a una letra minúscula da entonces su versión en mayúscula, y el resultado puede almacenarse de nuevo en un `char`:
```c
char upper = 'g' - 32; // 'G'
```

---

`int` no es el único tipo entero. Los modificadores cambian su tamaño y rango:
- `short` usa menos memoria y tiene un rango más pequeño (normalmente de -32768 a 32767)
- `long` tiene un rango más grande (en sistemas de 64 bits, unos ±9 trillones)
- `unsigned` elimina el signo: `unsigned int` va de `0` a unos 4 mil millones, pero nunca puede ser negativo

Un literal que debe ser `long` lleva el sufijo `L`, uno `unsigned` el sufijo `U`, y cada tipo tiene su propio especificador:
```c
long population = 8000000000L;
unsigned int count = 40U;
printf("%ld %u\n", population, count); // imprime "8000000000 40"
```
`%ld` imprime un `long`, `%u` un `unsigned int` y `%lu` un `unsigned long`. Un `int` normal en la mayoría de sistemas admite valores de hasta unos 2 mil millones, así que `5000000000` no cabe en él.

---

El operador `sizeof` indica cuántos **bytes** ocupa un tipo o una variable. Su resultado tiene el tipo `size_t`, que se imprime con `%zu`:
```c
printf("%zu\n", sizeof(int));  // imprime "4" en la mayoría de sistemas
```
El estándar solo garantiza que `sizeof(char)` es `1` y que `short <= int <= long`, pero en un sistema típico de 64 bits los tamaños son: `char` 1, `short` 2, `int` 4, `long` 8, `float` 4, `double` 8.
`sizeof` se usa a menudo para comprobar cuánta memoria ocupa una variable sin codificar el número directamente.

---

Cada tipo entero tiene un rango limitado, y la cabecera `limits.h` da nombre a esos límites: `INT_MAX` e `INT_MIN` para `int`, `LONG_MAX` para `long`, `UINT_MAX` para `unsigned int`, y así sucesivamente.
```c
#include <limits.h>

printf("%d\n", INT_MAX); // imprime "2147483647" en la mayoría de sistemas
```
Sobrepasar `INT_MAX` con un tipo con signo es **comportamiento indefinido**: el programa puede desbordarse, fallar o hacer cualquier otra cosa. Comprueba antes de calcular:
```c
if (a <= INT_MAX - b) { /* a + b es seguro */ }
```
Observa que la comprobación resta en lugar de sumar, porque `a + b` en sí ya podría desbordarse.

---

A diferencia de los tipos con signo, la aritmética **unsigned** está bien definida cuando se sale de rango: el valor **da la vuelta** como un cuentakilómetros.
Sumar `1` a `UINT_MAX` da `0`, y restar `1` a `0` da `UINT_MAX` (`4294967295` cuando `unsigned int` tiene 32 bits):
```c
unsigned int n = UINT_MAX;
n = n + 1;
printf("%u\n", n); // imprime "0"
```
Por eso un bucle que cuenta hacia atrás una variable `unsigned` "hasta que sea negativa" nunca se detiene: un valor unsigned nunca está por debajo de `0`.

---

Desde C99, la cabecera `stdbool.h` proporciona el tipo `bool` con las constantes `true` (`1`) y `false` (`0`).
Un `bool` es un tipo entero con solo dos valores, así que convertir cualquier número a `bool` da `true` para cualquier valor distinto de cero y `false` para `0`. Esto es diferente de convertir a `int`:
```c
#include <stdbool.h>

bool b = 0.5;  // true, porque 0.5 no es cero
int n = 0.5;   // 0, porque los decimales se truncan
```
Comparaciones como `x != 0` ya producen un resultado compatible con `bool`, y una función que devuelve `bool` documenta que responde a una pregunta de sí o no.

---

Una operación aritmética se realiza en el tipo de sus operandos, **no** en el tipo de la variable que recibe el resultado.
Así, `long big = n * n;` con un `n` de tipo `int` multiplica dos valores `int`, se desborda si el producto es demasiado grande, y solo entonces almacena el resultado (ya incorrecto) en el `long`.
Convierte un operando **antes** de la operación para calcular en el tipo más amplio:
```c
int n = 100000;
long big = (long) n * n; // 10000000000, calculado como long
```
La misma regla explica por qué funciona `(double) total / count`: el cast cambia el tipo del operando, y la división lo sigue.

---

Uniendo todo: elige el tipo según la clase de valor, haz que cada especificador de `printf` coincida con el tipo de su argumento, y convierte cuando un cálculo deba realizarse en un tipo distinto al de sus operandos.
