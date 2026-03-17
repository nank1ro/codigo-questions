Una **clase** es un plano para crear objetos. En Kotlin, se declara una clase con la palabra clave `class` seguida del nombre de la clase.

Una clase puede contener **propiedades** (datos) y **métodos** (comportamiento). Para declarar una propiedad directamente en el constructor, se le añade el prefijo `val` o `var`:

```kotlin
class Dog(val name: String)
```

Esto crea una clase `Dog` con una propiedad `name`. Se crea una instancia llamando a la clase como si fuera una función:

```kotlin
val dog = Dog("Rex")
println(dog.name) // Rex
```

---

Las clases pueden tener múltiples propiedades en su **constructor primario**. Cada propiedad se declara con `val` (solo lectura) o `var` (mutable) directamente en la lista de parámetros del constructor:

```kotlin
class Person(val name: String, var age: Int)
```

La palabra clave `val` hace que `name` sea de solo lectura después de la creación, mientras que `var` hace que `age` sea mutable — se puede cambiar después:

```kotlin
val p = Person("Alice", 30)
p.age = 31  // permitido porque age es var
```

---

El **bloque `init`** se ejecuta inmediatamente después del constructor primario. Se usa para realizar validaciones o lógica de configuración cuando se crea un objeto:

```kotlin
class Circle(val radius: Double) {
    init {
        require(radius > 0) { "Radius must be positive" }
    }
}
```

También se pueden inicializar propiedades adicionales dentro de `init`:

```kotlin
class Square(val side: Int) {
    val area: Int
    init {
        area = side * side
    }
}
```

---

Las clases pueden contener **métodos** — funciones que pertenecen a la clase y operan sobre sus propiedades:

```kotlin
class Counter(var count: Int) {
    fun increment() {
        count++
    }
    fun value(): Int {
        return count
    }
}
```

Los métodos se llaman usando la notación de punto en una instancia:

```kotlin
val c = Counter(0)
c.increment()
println(c.value()) // 1
```

---

Una **`data class`** es una clase especial diseñada para almacenar datos. Kotlin genera automáticamente `equals()`, `hashCode()`, `toString()` y `copy()`:

```kotlin
data class Point(val x: Int, val y: Int)

val p = Point(1, 2)
println(p)            // Point(x=1, y=2)
println(p.toString()) // Point(x=1, y=2)
```

La función `copy()` crea una nueva instancia con algunas propiedades modificadas:

```kotlin
val p2 = p.copy(y = 10)
println(p2) // Point(x=1, y=10)
```
