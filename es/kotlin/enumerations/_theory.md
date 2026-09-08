Una **enumeración** (o *enum*) define un tipo común para un grupo de valores relacionados, para que puedas trabajar con esos valores de forma segura en cuanto a tipos.
En Kotlin se declara con las palabras clave `enum class`, listando sus **entradas** separadas por comas:
```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
```
Por convención, los nombres de las entradas se escriben en mayúsculas. Cada entrada es un valor del tipo enum y se accede a ella a través del nombre de la clase:
```kotlin
val heading = Direction.NORTH
println(heading) // NORTH
```
Las clases enum deben declararse en el nivel superior de un archivo (o dentro de otra clase), nunca dentro de una función.

---

Cada entrada de un enum tiene dos propiedades integradas:

- `name` es el nombre de la entrada como `String`
- `ordinal` es su posición en la declaración, empezando en `0`

```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
println(Direction.EAST.name)    // EAST
println(Direction.EAST.ordinal) // 2
```

---

Las entradas de un enum se comparan con `==`:
```kotlin
val heading = Direction.NORTH
println(heading == Direction.NORTH) // true
```

Una expresión `when` es la forma natural de ramificar sobre un enum. Cuando cubre **todas** las entradas es *exhaustiva* y no necesita una rama `else`:
```kotlin
fun arrow(direction: Direction): String = when (direction) {
    Direction.NORTH -> "^"
    Direction.SOUTH -> "v"
    Direction.EAST -> ">"
    Direction.WEST -> "<"
}
```
Si olvidas una entrada, el compilador reporta un error en lugar de dejar que el bug llegue al tiempo de ejecución.

---

Un enum puede tener un **constructor**, igual que una clase normal. Cada entrada pasa entonces sus propios argumentos, y los valores se almacenan en propiedades:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2)
}
println(Planet.MARS.moons) // 2
```
Las propiedades del constructor normalmente se declaran con `val`, ya que los datos de una entrada no están pensados para cambiar.

---

Los enums también pueden declarar **métodos**. La lista de entradas debe cerrarse con un punto y coma `;` antes de cualquier declaración de miembro:
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2);

    fun hasMoons(): Boolean {
        return moons > 0
    }
}
println(Planet.EARTH.hasMoons()) // true
```
Dentro de un método puedes acceder a las propiedades de la entrada, así como a `name` y `ordinal`.

---

Cada enum expone una propiedad `entries`: una lista con todas sus entradas en el orden de declaración. Es muy útil para iterar:
```kotlin
for (direction in Direction.entries) {
    println(direction.name)
}
// NORTH
// SOUTH
// EAST
// WEST
```
Al ser una lista, `entries` también admite `size` e indexación, por ejemplo `Direction.entries[0]` es `NORTH`.

El código antiguo usa en su lugar la función `values()`, que devuelve un array; `entries` es la opción recomendada desde Kotlin 1.9.

---

Para pasar de un `String` de vuelta a una entrada, usa la función `valueOf`. Busca la entrada cuyo `name` coincide exactamente:
```kotlin
val direction = Direction.valueOf("EAST")
println(direction == Direction.EAST) // true
```
La coincidencia distingue mayúsculas de minúsculas: `Direction.valueOf("east")` lanza una `IllegalArgumentException` porque ninguna entrada tiene ese nombre.

---

Un enum puede declarar un **método abstracto** y dejar que cada entrada proporcione su propia implementación en un cuerpo delimitado por llaves:
```kotlin
enum class Operation {
    ADD {
        override fun apply(a: Int, b: Int): Int = a + b
    },
    SUBTRACT {
        override fun apply(a: Int, b: Int): Int = a - b
    };

    abstract fun apply(a: Int, b: Int): Int
}
println(Operation.ADD.apply(2, 3)) // 5
```
Cada entrada se comporta de forma distinta, aunque comparte el mismo tipo y la misma firma de método.

---

Una **interfaz** declara métodos sin cuerpo; cualquier tipo que la implemente debe proporcionarlos:
```kotlin
interface Greeter {
    fun greet(): String
}
```
Los enums pueden implementar interfaces. Se lista la interfaz después de dos puntos y se marca cada implementación con `override`. Dentro del cuerpo del enum, la entrada actual es `this` y las demás entradas pueden referenciarse sin el nombre de la clase:
```kotlin
enum class Language : Greeter {
    ENGLISH, ITALIAN;

    override fun greet(): String = when (this) {
        ENGLISH -> "Hello"
        ITALIAN -> "Ciao"
    }
}
println(Language.ITALIAN.greet()) // Ciao
```
