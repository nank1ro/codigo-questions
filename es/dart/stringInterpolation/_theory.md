Una _interpolación_ de String es una forma programática de generar una String.
En Dart podemos usar el signo `+` (concatenación) para mostrar dos o más strings juntos, como:
```dart
print("Hello " + "Dart!");
// prints "Hello Dart!"
```

---

Pero usar el signo `+` para agregar un número como '10' a una cadena como ` "friends"` produce un error ya que son un tipo diferente de valores

---

La interpolación de cadenas nos permite mostrar expresiones como agregar una cadena a un número, sin ningún error.
Colocar una expresión dentro de `${}` la evalúa.
El valor de retorno se convierte en una String e se inserta en la String resultante

---

Si pones un `$` antes de un nombre de identificador, la interpolación de cadenas insertará el contenido de ese identificador en la `String`

---

Si lo que sigue al signo `$` no es reconocible como un identificador de programa, vas a encontrarte con un error

---

También podemos insertar variables después de los signos de dólar para mostrar su valor

---

Podemos usar llaves para insertar valores tantas veces como queramos usando la interpolación de cadenas

---

Dentro de `${}` también podemos poner condiciones, por ejemplo:
```dart
print("The answer is ${true ? "correct": "wrong"}");
// prints The answer is correct
```

---

La interpolación de cadenas se usa mejor en sentencias print, pero también podemos almacenarlas en variables como cadenas normales.
