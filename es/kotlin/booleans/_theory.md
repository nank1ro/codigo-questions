Kotlin tiene un tipo booleano básico, llamado `Boolean`.
Los valores booleanos se denominan lógicos, porque solo pueden ser verdadero o falso.
Puedes evaluar cualquier expresión en Kotlin y obtener una de dos respuestas: `true` o `false`.

---

Podemos almacenar el valor booleano `true` en una variable al igual que un número o una cadena.

---

El valor opuesto de `true` es `false`

---

Los valores booleanos también pueden ser negados usando `!` antes de ellos, por ejemplo:
```kotlin
println(!true) // prints false
println(!false) // prints true
```

---

También podemos crear expresiones booleanas usando `&&` (_y_) y `||` (_o_):

- `&&` (_y_): produce verdadero solo si la expresión booleana a la izquierda del operador y la de la derecha son ambas verdaderas.
- `||` (_o_): Produce verdadero si la expresión a la izquierda o a la derecha del operador es verdadera, o si ambas son verdaderas.

```kotlin
println(true && true) // prints true
println(true && false) // prints false
println(false && false) // prints false
println(true || true) // prints true
println(true || false) // prints true
println(false || false) // prints false
```
