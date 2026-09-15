Cada número entero se almacena en memoria como una fila de **bits**, cada uno de los cuales es `0` o `1`. El número `12` se almacena como `00001100` y el número `10` como `00001010`.
Los **operadores bit a bit** trabajan sobre esos bits individuales en lugar de sobre el número como un todo. El operador **AND** `&` compara los dos valores bit a bit y conserva un `1` solo donde *ambos* bits son `1`:
```c
//  00001100   (12)
// &00001010   (10)
//  --------
//  00001000   (8)
printf("%u\n", 12u & 10u);
// imprime "8"
```
Los patrones de bits se suelen escribir como literales hexadecimales como `0x0C`, porque cada dígito hexadecimal representa exactamente cuatro bits. Usa siempre tipos `unsigned` para trabajar con bits e imprímelos con `%u`.

---

El operador **OR** `|` compara los dos valores bit a bit y conserva un `1` donde *al menos uno* de los bits es `1`:
```c
//  00001100   (12)
// |00001010   (10)
//  --------
//  00001110   (14)
printf("%u\n", 12u | 10u);
// imprime "14"
```
`|` es la forma habitual de fusionar dos patrones de bits en uno.

---

El operador **XOR** `^` (or exclusivo) conserva un `1` solo donde los dos bits son *diferentes*:
```c
//  00001100   (12)
// ^00001010   (10)
//  --------
//  00000110   (6)
printf("%u\n", 12u ^ 10u);
// imprime "6"
```
De esto se deduce una propiedad útil: aplicar el mismo XOR dos veces devuelve el valor original.

---

El operador **NOT** `~` toma un único operando e invierte todos sus bits: cada `0` se convierte en `1` y cada `1` se convierte en `0`.
Un `unsigned int` guarda 32 bits, así que `~0x0Fu` los invierte los 32 y produce un número muy grande. Para conservar solo el byte que te interesa, combina `~` con `& 0xFF`:
```c
printf("%u\n", ~0x0Fu & 0xFFu);
// imprime "240"
```
`~` tiene mayor precedencia que `&`, por lo que se aplica primero.
No confundas `~` con el `!` lógico: `!` mira el valor completo y responde `0` o `1`, mientras que `~` reescribe cada bit.

---

El operador **desplazamiento a la izquierda** `<<` mueve cada bit un número de posiciones hacia la izquierda y rellena las posiciones liberadas de la derecha con ceros:
```c
//  00000011   (3)
//  << 2
//  00001100   (12)
printf("%u\n", 3u << 2);
// imprime "12"
```
Desplazar a la izquierda `n` posiciones multiplica el valor por 2 elevado a `n`.
Dos errores hacen que un programa en C tenga comportamiento indefinido: desplazar a la izquierda un valor negativo, y desplazar una cantidad igual o mayor que el ancho del tipo (32 para `unsigned int`). Trabajar con valores **unsigned** te evita el primero.

---

El operador **desplazamiento a la derecha** `>>` mueve cada bit hacia la derecha; los bits que se caen por el extremo derecho se descartan. En un valor unsigned las posiciones liberadas de la izquierda se rellenan con ceros:
```c
//  00001100   (12)
//  >> 2
//  00000011   (3)
printf("%u\n", 12u >> 2);
// imprime "3"
```
Desplazar a la derecha `n` posiciones divide un valor unsigned entre 2 elevado a `n`, descartando el resto.
Desplazar a la derecha un valor *negativo* no es portátil, lo cual es una razón más para trabajar con bits sobre tipos `unsigned`.

---

Cada operador bit a bit binario tiene una forma de **asignación compuesta** que actualiza una variable en el sitio: `&=`, `|=`, `^=`, `<<=` y `>>=`.
```c
unsigned int x = 12;
x &= 10;  // igual que x = x & 10;
x |= 1;   // igual que x = x | 1;
x ^= 3;   // igual que x = x ^ 3;
x <<= 1;  // igual que x = x << 1;
x >>= 2;  // igual que x = x >> 2;
```
Se leen mejor que repetir el nombre de la variable y son la forma habitual de cambiar los bits de una variable de flags.

---

Una **máscara** es un valor cuyos bits seleccionan la parte de otro valor que te interesa. Combinada con `&`, una máscara conserva los bits que son `1` en la máscara y pone a cero todos los demás:
```c
//  10101011   (0xAB)
// &00001111   (0x0F)
//  --------
//  00001011   (0x0B)
printf("%u\n", 0xABu & 0x0Fu);
// imprime "11"
```
`0x0F` conserva los cuatro bits más bajos, llamado el **nibble** bajo, y `0xFF` conserva los ocho bits más bajos, un byte entero.

---

Los bits se numeran desde `0`, empezando por el más a la derecha, así que `1u << n` es una máscara con solo el bit `n` encendido.
Para **establecer** un solo bit, es decir, encenderlo sin tocar los demás, haz un OR del valor con esa máscara:
```c
unsigned int value = 4;      // 00000100
value = value | (1u << 1);   // 00000110
printf("%u\n", value);
// imprime "6"
```
Si el bit ya estaba encendido el valor no cambia, lo que hace que establecer un bit sea seguro de repetir.

---

Para **limpiar** un solo bit, es decir, apagarlo, haz un AND del valor con el *inverso* de la máscara:
```c
unsigned int value = 7;       // 00000111
value = value & ~(1u << 1);   // 00000101
printf("%u\n", value);
// imprime "5"
```
`~(1u << 1)` es un valor con todos los bits encendidos excepto el bit `1`, así que el AND deja todo lo demás intacto.

---

Para **alternar** un solo bit, es decir, invertirlo sin importar su estado actual, haz un XOR del valor con la máscara:
```c
unsigned int value = 5;      // 00000101
value = value ^ (1u << 1);   // 00000111
printf("%u\n", value);
// imprime "7"
```
Como el XOR se deshace a sí mismo, alternar el mismo bit una segunda vez devuelve el valor original.

---

Para **probar** un solo bit, haz un AND del valor con la máscara y comprueba si el resultado es distinto de `0`:
```c
unsigned int value = 10;                  // 00001010
printf("%d\n", (value & (1u << 3)) != 0); // imprime "1"
printf("%d\n", (value & (1u << 2)) != 0); // imprime "0"
```
El AND no produce `1`: produce `0` o la propia máscara, que para el bit `3` es `8`. Por eso el resultado se compara con `!= 0` en lugar de usarse como una respuesta directa.

---

Los **flags** son máscaras con nombre, cada una usando un bit diferente, que pueden almacenarse todas dentro de una sola variable. Se combinan con `|` y se leen con `&`:
```c
unsigned int READ = 0x01, WRITE = 0x02;
unsigned int perms = READ | WRITE;
printf("%d\n", (perms & WRITE) != 0);
// imprime "1"
```
Un solo `unsigned int` puede llevar por tanto 32 respuestas sí/no independientes.

---

Antes de C23 no había ningún especificador de formato que imprimiera un número en binario, y literales como `0b1010` tampoco eran C estándar. Para mostrar los bits escribes el bucle tú mismo: recorre desde el bit más alto hasta el bit `0` e imprime `(value >> i) & 1u` cada vez.
```c
unsigned int value = 5;
for (int i = 3; i >= 0; i--) {
    printf("%u", (value >> i) & 1u);
}
printf("\n");
// imprime "0101"
```
Desplazar el valor hacia abajo `i` posiciones lleva el bit `i` a la posición más a la derecha, donde `& 1u` lo aísla.

---

Contar cuántos bits de un valor son `1` es un bucle de bits clásico: prueba el bit más bajo con `& 1u`, añádelo a un contador, luego desplaza el valor una posición a la derecha con `>>=` y repite hasta que no quede nada.
```c
unsigned int value = 6, count = 0;
while (value != 0) {
    count += value & 1u;
    value >>= 1;
}
// count es 2
```
El bucle siempre termina, porque un valor unsigned desplazado a la derecha suficientes veces se convierte en `0`.

---

Varios números pequeños suelen empaquetarse dentro de un valor mayor. Para recuperar uno de ellos, primero desplázalo hacia abajo hasta que empiece en el bit `0` y luego enmascara todo lo que quede por encima:
```c
unsigned int packed = 0x1234;
printf("%u\n", (packed >> 8) & 0xFF);
// imprime "18", el byte 0x12
```
Primero desplazar y enmascarar después es el orden a recordar: la máscara siempre describe el campo una vez que ha llegado abajo.
