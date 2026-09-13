Una `data class` es una clase cuya función es **almacenar datos**. A partir de las propiedades que declaras en el constructor primario, el compilador genera cuatro miembros por ti:

- `toString()`, un texto legible `ClassName(prop=value, ...)`
- `equals()` y `hashCode()`, de modo que dos instancias con los mismos datos se consideren iguales
- `copy()`, que construye una nueva instancia reutilizando los valores actuales

```kotlin
data class Book(val title: String, val pages: Int)

val book = Book("Dune", 412)
println(book)          // Book(title=Dune, pages=412)
println(book.copy())   // Book(title=Dune, pages=412)
```

`copy()` brilla especialmente con **argumentos con nombre**: indicas solo las propiedades que quieres cambiar, y todos los demás valores se mantienen.

```kotlin
println(book.copy(pages = 500)) // Book(title=Dune, pages=500)
```

El original nunca se modifica: `copy()` devuelve un objeto completamente nuevo.

---

Por cada propiedad del constructor primario, una data class también genera una función `componentN()`: `component1()` para la primera propiedad, `component2()` para la segunda, y así sucesivamente.

Esas funciones hacen posibles las **declaraciones de desestructuración**, donde desempaquetas un objeto en varias variables en una sola línea:

```kotlin
data class Point(val x: Int, val y: Int)

val point = Point(3, 7)
val (x, y) = point
println(x)               // 3
println(point.component2()) // 7
```

El orden de las variables sigue el orden de las propiedades, no sus nombres. Usa `_` para omitir la que no necesites:

```kotlin
val (_, onlyY) = point
```

---

El `equals()` generado convierte `==` en una comparación **estructural**: dos instancias son iguales cuando todas las propiedades del constructor primario son iguales. El operador `===` es diferente: pregunta si ambos nombres apuntan al **mismo objeto** en memoria.

```kotlin
data class User(val id: Int, val name: String)

val a = User(1, "Ann")
val b = User(1, "Ann")
println(a == b)  // true, same data
println(a === b) // false, two different objects
println(a === a) // true
```

Como `hashCode()` se genera junto con `equals()`, las instancias de una data class también se comportan correctamente dentro de un `Set` o como claves de un `Map`: los duplicados se colapsan.

```kotlin
println(setOf(a, b).size) // 1
```

Una clase normal no genera nada de esto, así que para ella `==` se reduce a la identidad.

---

Los miembros generados solo tienen en cuenta las propiedades declaradas en el **constructor primario**. Una propiedad declarada en el **cuerpo** de la clase es una propiedad normal: no forma parte de `toString()`, `equals()`, `hashCode()` ni `copy()`.

```kotlin
data class Item(val name: String) {
    var quantity: Int = 0
}

val a = Item("nail")
a.quantity = 5
println(a) // Item(name=nail)
```

Esto es fácil de olvidar, así que coloca en el constructor primario todo lo que identifica al objeto, y deja en el cuerpo el estado derivado o temporal.

---

Una clase `sealed` describe un conjunto **cerrado** de alternativas: solo se permiten las subclases escritas en el mismo paquete y módulo, de modo que el compilador conoce todas ellas.

```kotlin
sealed class Shape
data class Circle(val radius: Int) : Shape()
data class Square(val side: Int) : Shape()
```

La ventaja es el **`when` exhaustivo**: cuando haces un `when` sobre un tipo sealed y cubres todas las subclases, puedes omitir la rama `else`. Si añades una nueva subclase más adelante, el compilador avisa de cada `when` que hayas olvidado actualizar, en lugar de tomar el `else` en silencio.

```kotlin
fun name(shape: Shape): String = when (shape) {
    is Circle -> "circle"
    is Square -> "square"
}
```

Después de `is Circle` el valor se convierte automáticamente mediante smart cast, así que `shape.radius` está disponible dentro de esa rama sin ninguna conversión manual.
