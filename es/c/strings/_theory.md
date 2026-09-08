C no tiene un tipo de dato string dedicado: una **cadena** es un array de `char` que termina con un carácter especial, el **terminador nulo** `'\0'`.
La forma más sencilla de crear una es un literal de cadena entre comillas dobles:
```c
char name[] = "Codigo";
```
El compilador cuenta los caracteres y añade el `'\0'` al final por ti.
Para imprimir una cadena usa el marcador `%s`:
```c
printf("%s\n", name);
// imprime "Codigo"
```

---

El terminador nulo ocupa espacio en memoria: el literal `"hi"` ocupa 3 bytes, `'h'`, `'i'` y `'\0'`.
Cuando declaras el tamaño tú mismo, deja siempre espacio para él:
```c
char word[6] = "hello"; // 5 letras + '\0'
```
Sin el terminador, C no tiene forma de saber dónde termina la cadena.

---

La cabecera `string.h` proporciona funciones que trabajan con cadenas.
`strlen` devuelve el número de caracteres antes del terminador nulo (el terminador en sí no se cuenta):
```c
strlen("hello"); // 5
```
Una función que recibe una cadena declara el parámetro como `char *text`, un puntero al primer carácter.
En estos ejercicios `string.h` y `ctype.h` ya están incluidos encima de tu código.

---

Dado que una cadena es un array, cada carácter tiene un índice que empieza en `0`:
```c
char word[] = "Coding";
word[0]; // 'C'
word[5]; // 'g'
```
Un único carácter se imprime con `%c`. Los caracteres también se pueden reemplazar:
```c
word[0] = 'K'; // word ahora es "Koding"
```

---

Como toda cadena termina con `'\0'`, puedes recorrerla sin conocer su longitud de antemano: continúa mientras el carácter actual no sea el terminador.
```c
for (int i = 0; text[i] != '\0'; i++) {
    printf("%c\n", text[i]);
}
```

---

Un array no puede asignarse con `=` después de su declaración:
```c
char copy[20];
copy = "Codigo"; // error
```
Para copiar una cadena usa `strcpy(destination, source)` de `string.h`.
El destino debe ser lo suficientemente grande para contener todos los caracteres más el `'\0'`.

---

`strcat(destination, source)` añade `source` al final de `destination`:
```c
char text[20] = "Hello";
strcat(text, " World");
// text ahora es "Hello World"
```
Como con `strcpy`, el array de destino debe tener suficiente espacio para el resultado.

---

Dos cadenas no se pueden comparar con `==`: eso compararía sus direcciones en memoria, no sus caracteres.
Usa `strcmp(first, second)` en su lugar, que devuelve `0` cuando las dos cadenas contienen exactamente los mismos caracteres:
```c
strcmp("cat", "cat"); // 0
strcmp("cat", "dog"); // no 0
```

---

`strcmp` compara las cadenas carácter por carácter usando sus códigos de carácter.
El resultado es negativo cuando la primera cadena va antes que la segunda, positivo cuando va después, y `0` cuando son iguales:
```c
strcmp("a", "b"); // negativo
strcmp("b", "a"); // positivo
```

---

`strncpy(destination, source, n)` copia como máximo `n` caracteres.
Si `source` es más larga que `n`, no se escribe ningún `'\0'`: tienes que terminar el resultado tú mismo.
```c
char prefix[10];
strncpy(prefix, "Codigo", 3);
prefix[3] = '\0'; // prefix es "Cod"
```

---

La cabecera `ctype.h` proporciona funciones que trabajan con un único carácter.
`toupper(c)` devuelve la versión en mayúscula de una letra y `tolower(c)` la versión en minúscula; cualquier otro carácter se devuelve sin cambios:
```c
char letter = toupper('a'); // 'A'
```

---

Una cadena se pasa a una función como un puntero, así que una función que recibe `char *text` puede cambiar los caracteres del llamador directamente.
Combinar un bucle hasta `'\0'` con `toupper` convierte toda una cadena:
```c
text[i] = toupper(text[i]);
```

---

`sprintf` funciona como `printf`, pero escribe el texto formateado en un array de caracteres en lugar de en la pantalla:
```c
char buffer[30];
sprintf(buffer, "%d items", 3); // buffer es "3 items"
```
El buffer debe ser lo suficientemente grande para todo el texto y su `'\0'`.

---

`sprintf` es una forma práctica de convertir un número en texto: una vez que está en un buffer, cualquier función de cadenas puede trabajar con él.
