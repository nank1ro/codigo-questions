Un **comentario** es texto dentro de tu código fuente destinado a las personas, no al compilador. El compilador descarta los comentarios antes de compilar el programa, así que puedes usarlos para explicar para qué sirve el código, dejar recordatorios o anotar una decisión.

El tipo más común es el **comentario de una sola línea**: todo lo que va desde `//` hasta el final de esa línea se ignora.
```c
// Greet the user
printf("Hello\n");
```
La primera línea no hace nada cuando se ejecuta el programa; solo el `printf` produce una salida.

---

Como el compilador elimina los comentarios por completo, añadir o borrar un comentario nunca cambia lo que hace un programa. Solo se ejecuta el código que **no** está comentado.

Esto hace de `//` una forma rápida de desactivar una línea de código sin borrarla. Esto se llama **comentar** (commenting out):
```c
int total = 10;
// total = total + 5;
printf("%d\n", total); // prints "10"
```
La segunda línea ahora es un comentario, así que `total` se queda en `10`. Al quitar el `//`, la línea vuelve a la vida.

Comentar es útil mientras experimentas, pero recuerda limpiar después: el código que permanece comentado durante mucho tiempo solo confunde a quien lo lea después.

---

Cuando un comentario necesita más de una línea, C ofrece el **comentario multilínea** (también llamado comentario de bloque): empieza con `/*` y termina con `*/`, y todo lo que hay en medio se ignora, incluidos los saltos de línea.
```c
/*
  Prints the welcome banner.
  Called once when the program starts.
*/
printf("Welcome!\n");
```
Un comentario de bloque también puede ser corto y quedar en una sola línea: `/* como este */`.

A diferencia de `//`, que se detiene al final de la línea, un comentario `/*` solo se detiene en el `*/`. Si olvidas cerrarlo, el compilador tratará todo el código siguiente como parte del comentario.

---

Los comentarios de bloque **no se anidan**. El compilador termina un comentario `/*` en el primer `*/` que encuentra, sin importar cuántos `/*` haya antes:
```c
/* outer /* inner */ still code */
```
Aquí el comentario termina justo después de `inner`, así que `still code */` se compila como código y produce un error.

Esto importa cuando quieres comentar un bloque que ya contiene un comentario `/* */`: el `*/` interno cerraría tu comentario externo demasiado pronto. En ese caso, pon `//` delante de cada línea en su lugar.

---

Un comentario no necesita su propia línea: puede seguir al código en la misma línea. Esto es un **comentario al final de la línea**, y es un buen lugar para una nota corta sobre esa sentencia concreta:
```c
int retries = 3; // give up after three attempts
```
Tanto `//` como `/* */` funcionan como comentarios al final de la línea, pero ten cuidado con `/*`: como solo se detiene en `*/`, un `/*` sin cerrar al final de una línea se traga las líneas que siguen y el programa ya no compila.

---

Un uso común de los comentarios de bloque es el **comentario de cabecera**: un bloque corto situado justo encima de una función que dice qué hace, qué significan sus parámetros y qué devuelve.
```c
/*
 * Returns the number of seconds in the given minutes.
 * minutes: a whole number of minutes, never negative
 */
int to_seconds(int minutes) {
    return minutes * 60;
}
```
Quien llame a `to_seconds` puede ahora leer la cabecera en lugar del cuerpo. Mantén la cabecera junto a la función para que se actualicen juntas.

---

El compilador reemplaza cada comentario por un solo espacio. Esto significa que un comentario `/* */` puede aparecer donde pueda aparecer un espacio, incluso en medio de una sentencia o una expresión:
```c
int area = width /* cm */ * height /* cm */;
```
Esto resulta útil en ocasiones para etiquetar los operandos o los argumentos de una llamada. Un comentario `//` no puede hacer esto, porque comentaría el resto de la línea, incluido el código que va después.

---

Los programadores usan algunas palabras clave convencionales al principio de un comentario para señalar trabajo que no está terminado:

- `TODO` marca algo que todavía falta por escribir
- `FIXME` marca código que se sabe que está mal y debe corregirse

```c
// TODO: validate the input before using it
// FIXME: crashes when the list is empty
```
Los editores y las herramientas pueden listar estos marcadores, así que el trabajo pendiente es fácil de encontrar. Una vez hecho el trabajo, borra el marcador: un `TODO` obsoleto induce a error.

---

Un buen comentario explica **por qué** el código hace algo, no **qué** hace. El código ya muestra lo que ocurre; repetirlo con palabras añade ruido y queda obsoleto en cuanto cambia el código:
```c
// multiply price by 90 and divide by 100
return price * 90 / 100;
```
El motivo detrás de los números es lo que un lector no puede adivinar:
```c
// launch discount: members get 10% off until the end of June
return price * 90 / 100;
```
Si un comentario solo repite la línea de abajo, bórralo o reemplázalo por el motivo.

---

Resumiendo: usa `//` para notas cortas y comentarios al final de la línea, `/* */` para bloques más largos y comentarios de cabecera, marca el trabajo sin terminar con `TODO` o `FIXME`, y elimina el código comentado y los marcadores obsoletos cuando ya no hagan falta.
