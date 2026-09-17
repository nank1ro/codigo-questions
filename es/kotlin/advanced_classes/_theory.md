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
println(a == b)  // true, mismos datos
println(a === b) // false, dos objetos diferentes
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

---

A veces necesitas exactamente **una** instancia de algo: un logger, un registro, la configuración de una aplicación. Sustituir `class` por `object` declara ese singleton por ti:

```kotlin
object Registry {
    var size = 0
    fun add() {
        size++
    }
}

Registry.add()
println(Registry.size) // 1
```

La instancia se crea la primera vez que la usas, y usas el nombre directamente: no hay llamada `Registry()` ni constructor. Un `object` puede contener propiedades, métodos, bloques `init`, y puede implementar interfaces o extender una clase.

---

Un `companion object` es el singleton que pertenece a una clase. Además de constantes, su función natural es albergar **funciones de fábrica**: funciones que comprueban o transforman la entrada antes de construir una instancia, y que pueden devolver `null` cuando la entrada no tiene sentido.

Marcar el constructor como `private` obliga a quien llama a pasar por la fábrica:

```kotlin
class Age private constructor(val years: Int) {
    companion object {
        fun of(years: Int): Age? = if (years >= 0) Age(years) else null
    }
}

println(Age.of(30)?.years) // 30
println(Age.of(-1))        // null
```

El companion se invoca sobre el nombre de la clase, `Age.of(...)`, y puede acceder al constructor privado porque vive dentro de la clase.

---

Una `interface` enumera lo que un tipo puede hacer. Sus miembros son abstractos por defecto, pero una interfaz también puede incluir una **implementación por defecto**, un cuerpo que toda clase que la implemente hereda gratis y puede sobrescribir:

```kotlin
interface Greeter {
    val name: String              // abstracto, la clase debe proporcionarlo
    fun greet(): String = "Hi, $name"  // implementación por defecto
}

class Person(override val name: String) : Greeter

class Robot(override val name: String) : Greeter {
    override fun greet(): String = "BEEP $name"
}

println(Person("Ann").greet()) // Hi, Ann
println(Robot("R2").greet())   // BEEP R2
```

Una interfaz no puede almacenar estado (no tiene campos de respaldo), así que una propiedad abstracta debe ser implementada por la clase, normalmente con `override val` en el constructor. A diferencia de una clase, un tipo puede implementar tantas interfaces como quiera.

---

Una clase `abstract` se sitúa entre una interfaz y una clase normal: no se puede instanciar, y mezcla miembros **abstractos**, que no tienen cuerpo y deben sobrescribirse, con miembros concretos que las subclases heredan tal cual.

```kotlin
abstract class Vehicle(val name: String) {
    abstract fun wheels(): Int
    fun describe(): String = "$name has ${wheels()} wheels"
}

class Bike(name: String) : Vehicle(name) {
    override fun wheels(): Int = 2
}

println(Bike("BMX").describe()) // BMX has 2 wheels
```

A diferencia de una interfaz, una clase abstracta tiene constructor y puede almacenar estado en propiedades; por eso la subclase pasa `name` hacia arriba con `: Vehicle(name)`. Una clase solo puede extender una clase, así que recurre a una clase abstracta cuando las subclases comparten datos, y a una interfaz cuando solo comparten comportamiento. Los miembros abstractos se pueden sobrescribir sin añadir `open`.

---

Una clase declarada dentro de otra clase es **anidada** por defecto. No sabe nada sobre la instancia exterior y se construye a partir del nombre de la clase exterior:

```kotlin
class Outer {
    class Nested {
        fun hello() = "hi"
    }
}

println(Outer.Nested().hello()) // hi
```

Añade la palabra clave `inner` y la situación cambia: una clase `inner` lleva una referencia a la instancia exterior, así que puede leer las propiedades exteriores, y se construye **a partir de una instancia**:

```kotlin
class Counter(val step: Int) {
    inner class Doubler {
        fun value() = step * 2
    }
}

println(Counter(5).Doubler().value()) // 10
```

Dentro de una clase `inner`, `this` es el objeto interior; usa `this@Counter` cuando necesites el exterior explícitamente.

---

Las piezas de este tema suelen combinarse: una `enum class` cuyas entradas llevan sus propias propiedades modela un conjunto fijo de etiquetas, mientras que una `data class` transporta los datos que las acompañan.

```kotlin
enum class Speed(val surcharge: Int) {
    STANDARD(0),
    EXPRESS(15)
}

data class Order(val total: Int, val speed: Speed)

val order = Order(100, Speed.EXPRESS)
println(order.total + order.speed.surcharge) // 115
```
