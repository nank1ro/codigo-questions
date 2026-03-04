Una plantilla de cadena _template_ es una forma programática de generar una cadena.
En Kotlin podemos usar el signo `+` (concatenación) para mostrar dos o más cadenas juntas, como:
```kotlin
println("Hello " + "Kotlin!")
// prints "Hello Kotlin!"
```

---

Pero usar el signo `+` para sumar un número como '10' a una cadena como ` "friends"` produce un error, ya que son valores de diferente tipo

---

Las plantillas de cadena nos permiten mostrar expresiones como sumar una cadena a un número, sin ningún error.
Al colocar una expresión dentro de `${}` la evaluamos.
El valor de retorno se convierte a una cadena y se inserta en la cadena resultante

---

Si pones un $ antes del nombre de un identificador, la plantilla de cadena insertará el contenido de ese identificador en la cadena

---

Si lo que sigue al signo `$` no es reconocible como un identificador de programa, no ocurre nada especial

---

También podemos insertar variables después de los signos de dólar para mostrar su valor

---

Podemos usar llaves para insertar valores tantas veces como queramos dentro de las plantillas de cadena

---

Dentro de `${}` también podemos poner condiciones, por ejemplo:
```kotlin
println("${if (true) "Correcto" else "Incorrecto"}")
// imprime Correcto
```

---

Las plantillas de cadena se usan mejor en sentencias de impresión, pero también podemos almacenarlas en variables como cadenas normales.
