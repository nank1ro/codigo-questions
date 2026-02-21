Una _interpolación_ de cadenas (String interpolation) es una forma programática de generar una cadena (String).
En Dart podemos usar el signo `+` (concatenación) para mostrar dos o más cadenas juntas, como por ejemplo:
```dart
print("Hola " + "Dart!");
// imprime "Hola Dart!"
```

---

Pero usar el signo `+` para sumar un número como '10' a una cadena como `"amigos"` produce un error ya que son diferentes tipos de valores

---

La interpolación de cadenas nos permite mostrar expresiones como sumar una cadena a un número, sin ningún error.
Colocar una expresión dentro de `${}` la evalúa.
El valor de retorno se convierte a una cadena (String) y se inserta en la cadena resultante

---

Si pones un `$` antes de un nombre de identificador, la interpolación de cadenas insertará el contenido de ese identificador en la `String`

---

Si lo que sigue al signo `$` no es reconocible como un identificador del programa, encontrarás un error

---

También podemos insertar variables después del signo de dólar para mostrar su valor

---

Podemos usar llaves para insertar valores tantas veces como queramos usando la interpolación de cadenas

---

Dentro de los `${}` también podemos poner condiciones, por ejemplo:
```dart
print("La respuesta es ${true ? "correcta": "incorrecta"}");
// imprime La respuesta es correcta
```

---

La interpolación de cadenas se usa mejor en declaraciones de impresión, pero también podemos almacenarlas en variables como cadenas normales.
