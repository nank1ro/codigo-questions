> Antes de comenzar, quería decirte que estoy muy feliz de enseñarte Dart.
Con este mensaje aprovecho la oportunidad de informarte que la aplicación que estás utilizando fue escrita en Dart, utilizando el marco Flutter. Así que es un honor para mí poder compartir mi experiencia en el lenguaje.

Dart, como muchos otros lenguajes de programación, te permite documentar tu código.
Esto te permite escribir cualquier texto junto al código.
Los comentarios son ignorados por el compilador.

Dart soporta comentarios de _una línea_, comentarios de _múltiples líneas_ y comentarios de _documentación_.

Aquí está cómo escribir un comentario de _una línea_:
```dart
// Este es un comentario. No se ejecuta.
```

---

Puedes apilar comentarios de _una sola línea_ para escribir comentarios de _múltiples líneas_.
```dart
// Este es un
// comentario de múltiples líneas
```

---

También puedes crear bloques de comentarios, o comentarios de _múltiples líneas_.
Los comentarios de _múltiples líneas_ comienzan con `/*` y terminan con `*/`.
```dart
/*
Este es un comentario
de múltiples líneas
*/
```

---

Además de estas dos formas de escribir comentarios, Dart incluye _comentarios de documentación_.

Los _comentarios de documentación_ son comentarios de múltiples líneas o de una sola línea que comienzan con `///` o `/**.` El uso de `///` en líneas consecutivas tiene el mismo efecto que un comentario de documentación de múltiples líneas.

Los _comentarios de documentación_ son muy útiles porque permiten generar documentación.
Querrás agregar _comentarios de documentación_ a tu código para que quede claro qué hace un bloque de código particular.

Dentro de un _comentario de documentación_, el analizador resuelve los nombres encerrados entre corchetes como referencias a otros elementos de la API.
Usando corchetes uno puede referirse a _clases_, _métodos_, _campos_, _variables_, _funciones_ y _parámetros_.

Aquí hay un ejemplo:
```dart
/// Un camélido sudamericano domesticado (Lama glama).
///
/// Como cualquier otro animal, las llamas necesitan comer,
/// así que no olvides usar [feed] para darles algo de [Food].
class Llama {
  String? name;

  /// Alimenta a tu llama con [food].
  ///
  /// La llama típica come una paca de heno por semana.
  void feed(Food food) {
    // ...
  }

  /// Ejercita a tu llama con un [activity] durante
  /// [timeLimit] minutos.
  void exercise(Activity activity, int timeLimit) {
    // ...
  }
}
```

En la documentación generada, `[feed]` se convierte en un enlace a la documentación del método `feed`, y `[Food]` se convierte en un enlace a la documentación de la clase `Food`.
Mientras que `[activity]` y `[timeLimit]` se convierten en un enlace a la documentación de `activity` y `timeLimit` respectivamente.
