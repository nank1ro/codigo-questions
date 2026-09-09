C no tiene interpolación de cadenas: el texto y los valores se combinan con `printf` mediante una **cadena de formato**, donde cada especificador `%` se sustituye por el argumento correspondiente. Los especificadores más habituales son:
```c
printf("%d\n", 42);      // prints "42" (int, %i is the same)
printf("%f\n", 2.5);     // prints "2.500000" (double, 6 decimals by default)
printf("%s\n", "hi");    // prints "hi" (string)
printf("%c\n", 'A');     // prints "A" (single character)
printf("%x\n", 255);     // prints "ff" (int as lowercase hexadecimal)
printf("100%%\n");       // prints "100%" (a literal percent sign)
```
El especificador debe coincidir con el tipo del argumento: imprimir un `double` con `%d` o un `int` con `%s` no convierte el valor, imprime basura o provoca un fallo.

---

`sprintf` funciona exactamente igual que `printf`, pero en lugar de escribir en pantalla escribe el texto formateado en un array de `char`, llamado **búfer**, seguido del `'\0'` terminador:
```c
char buffer[32];
sprintf(buffer, "%d-%d", 3, 7);
printf("%s\n", buffer); // prints "3-7"
```
El búfer debe declararse antes de la llamada y debe ser lo bastante grande para todo el texto más el terminador, de lo contrario `sprintf` escribe más allá de su final.

---

Una función que construye una cadena suele recibir el búfer como parámetro y lo rellena con `sprintf`. El array pertenece a quien llama, y después de la llamada puede leer el resultado:
```c
void greet(char *out, char *name) {
    sprintf(out, "Hello, %s!", name);
}

char message[32];
greet(message, "Ada");
printf("%s\n", message); // prints "Hello, Ada!"
```
En estos ejercicios `string.h` ya está incluido encima de tu código, así que se puede usar `strcmp` para comparar el resultado.

---

`%x` imprime un entero en hexadecimal con letras minúsculas, y `%X` hace lo mismo con letras mayúsculas. `%c` toma un código de carácter entero e imprime el carácter que representa, así que `%c` con `65` imprime `A`:
```c
printf("%x %X %c\n", 31, 31, 66); // prints "1f 1F B"
```

---

Un número entre `%` y la letra fija el **ancho** mínimo del campo. El valor se rellena con espacios por la izquierda, y las **banderas** colocadas justo después del `%` cambian el relleno:
```c
printf("[%5d]\n", 42);  // prints "[   42]" right-aligned in 5 columns
printf("[%-5d]\n", 42); // prints "[42   ]" the - flag aligns to the left
printf("[%05d]\n", 42); // prints "[00042]" the 0 flag pads with zeros
printf("[%+d]\n", 42);  // prints "[+42]" the + flag always shows the sign
```
Un valor más largo que el ancho nunca se corta, el campo simplemente crece.

---

El ancho y las banderas funcionan con todos los especificadores, así que `%02x` imprime un entero en hexadecimal rellenado con ceros hasta dos dígitos. Así es como se escriben los colores como `#rrggbb`:
```c
printf("%02x\n", 5);   // prints "05"
printf("%02x\n", 255); // prints "ff"
```

---

Un punto seguido de un número fija la **precisión**. Para `%f` es el número de decimales, redondeado; para `%s` es el número máximo de caracteres impresos:
```c
printf("%.2f\n", 3.14159);    // prints "3.14"
printf("%.3s\n", "formatting"); // prints "for"
```
El ancho y la precisión se pueden combinar: `%8.2f` imprime dos decimales alineados a la derecha en 8 columnas.

---

La precisión es la forma habitual de controlar cómo se ve un `double` en una cadena. Una proporción como `0.425` se convierte en porcentaje multiplicando por `100` e imprimiendo un decimal seguido de `%%`:
```c
sprintf(out, "%.1f%%", 0.425 * 100); // out is "42.5%"
```

---

`sprintf` y `printf` **devuelven** el número de caracteres escritos, sin contar el `'\0'` terminador. Esta es la longitud de la cadena que se acaba de construir, sin una llamada aparte a `strlen`:
```c
char buffer[32];
int length = sprintf(buffer, "%d-%d", 3, 7);
printf("%d\n", length); // prints "3"
```

---

`sprintf` no sabe qué tamaño tiene el búfer. `snprintf` toma el tamaño del búfer como segundo argumento y nunca escribe más de `size - 1` caracteres más el `'\0'`, cortando el texto si hace falta. Su valor de retorno es la longitud que habría tenido el texto **completo**, así que un resultado mayor o igual que `size` significa que la salida se truncó:
```c
char buffer[8];
int n = snprintf(buffer, sizeof buffer, "%s", "formatting");
printf("%s %d\n", buffer, n); // prints "formatt 10"
```
`sizeof buffer` da el tamaño del array en bytes, que para un array de `char` es su número de elementos.

---

Comparar el valor de retorno de `snprintf` con el tamaño del búfer indica si todo cupo. Este es el patrón seguro para construir cadenas de longitud desconocida:
```c
int n = snprintf(out, size, "%s", text);
if (n >= size) {
    // out holds only the first size - 1 characters of text
}
```

---

Una cadena se puede construir en varios pasos escribiendo cada parte justo después de la anterior. El valor de retorno indica dónde termina el texto, así que `buffer + n` es la dirección del terminador y el siguiente `sprintf` puede continuar desde ahí:
```c
char buffer[32];
int n = sprintf(buffer, "%s", "Hello");
n += sprintf(buffer + n, ", %s", "world"); // buffer is "Hello, world", n is 12
```
Sumar cada valor de retorno a `n` lo mantiene igual a la longitud total del texto construido hasta ahora.

---

Las cadenas también se pueden combinar sin una cadena de formato. `strcat` de `string.h` añade una copia de su segundo argumento al final del primero, que debe tener suficiente espacio libre, y `strncat` añade como máximo un número dado de caracteres:
```c
char text[32] = "Hi";
strcat(text, "!!!");        // text is "Hi!!!"
strncat(text, "abcdef", 2); // text is "Hi!!!ab"
```
Ambas añaden siempre el `'\0'` terminador después de los caracteres añadidos.

---

Cuando no hay nada que formatear, `puts` imprime una cadena seguida de un salto de línea. A diferencia de `printf` no interpreta `%`, así que el texto se imprime exactamente como está escrito:
```c
puts("Done");      // prints "Done" and a newline
puts("50% off");   // prints "50% off" and a newline
printf("50% off"); // undefined: % off is not a valid specifier
```
`puts` es la opción correcta para texto fijo, y `printf` cuando hay que insertar valores.

---

`strncat` es útil cuando solo hay que añadir una parte de una cadena, o cuando la parte añadida debe limitarse a una longitud máxima:
```c
char name[16] = "file";
strncat(name, ".backup", 3); // name is "file.ba"
```
Cuando el límite es mayor que la cadena, se añade la cadena entera.

---

Todo junto: una fila de informe combina un campo de texto alineado a la izquierda, un separador y un número alineado a la derecha con un número fijo de decimales, escrito con `snprintf` para que nunca desborde el búfer:
```c
snprintf(out, size, "%-6s|%5.1f", "Ada", 9.5); // out is "Ada   |  9.5"
```
Mientras cada valor quepa en su ancho, todas las filas tienen la misma longitud, así que las columnas quedan alineadas cuando las filas se imprimen una debajo de otra.
