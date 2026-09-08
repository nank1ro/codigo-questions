Une **énumération** (ou *enum*) définit un type commun pour un groupe de valeurs liées, afin de pouvoir travailler avec ces valeurs de manière sûre du point de vue des types.
En Kotlin, on en déclare une avec les mots-clés `enum class`, en listant ses **entrées** séparées par des virgules :
```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
```
Par convention, les noms des entrées sont écrits en majuscules. Chaque entrée est une valeur du type enum et on y accède via le nom de la classe :
```kotlin
val heading = Direction.NORTH
println(heading) // NORTH
```
Les classes enum doivent être déclarées au niveau supérieur d'un fichier (ou à l'intérieur d'une autre classe), jamais à l'intérieur d'une fonction.

---

Chaque entrée d'un enum possède deux propriétés intégrées :

- `name` est le nom de l'entrée sous forme de `String`
- `ordinal` est sa position dans la déclaration, en commençant à `0`

```kotlin
enum class Direction {
    NORTH, SOUTH, EAST, WEST
}
println(Direction.EAST.name)    // EAST
println(Direction.EAST.ordinal) // 2
```

---

Les entrées d'un enum se comparent avec `==` :
```kotlin
val heading = Direction.NORTH
println(heading == Direction.NORTH) // true
```

Une expression `when` est la manière naturelle de brancher sur un enum. Lorsqu'elle couvre **toutes** les entrées, elle est *exhaustive* et n'a pas besoin de branche `else` :
```kotlin
fun arrow(direction: Direction): String = when (direction) {
    Direction.NORTH -> "^"
    Direction.SOUTH -> "v"
    Direction.EAST -> ">"
    Direction.WEST -> "<"
}
```
Si vous oubliez une entrée, le compilateur signale une erreur au lieu de laisser le bug atteindre l'exécution.

---

Un enum peut avoir un **constructeur**, comme une classe classique. Chaque entrée passe alors ses propres arguments, et les valeurs sont stockées dans des propriétés :
```kotlin
enum class Planet(val moons: Int) {
    MERCURY(0),
    EARTH(1),
    MARS(2)
}
println(Planet.MARS.moons) // 2
```
Les propriétés du constructeur sont généralement déclarées avec `val`, car les données d'une entrée ne sont pas censées changer.

---

Les enums peuvent aussi déclarer des **méthodes**. La liste des entrées doit être fermée par un point-virgule `;` avant toute déclaration de membre :
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
À l'intérieur d'une méthode, vous pouvez accéder aux propriétés de l'entrée, ainsi qu'à `name` et `ordinal`.

---

Chaque enum expose une propriété `entries` : une liste de toutes ses entrées dans l'ordre de déclaration. Elle est pratique pour itérer :
```kotlin
for (direction in Direction.entries) {
    println(direction.name)
}
// NORTH
// SOUTH
// EAST
// WEST
```
Étant une liste, `entries` prend aussi en charge `size` et l'indexation, par exemple `Direction.entries[0]` vaut `NORTH`.

Le code plus ancien utilise à la place la fonction `values()`, qui retourne un tableau ; `entries` est le choix recommandé depuis Kotlin 1.9.

---

Pour passer d'un `String` à une entrée, utilisez la fonction `valueOf`. Elle recherche l'entrée dont le `name` correspond exactement :
```kotlin
val direction = Direction.valueOf("EAST")
println(direction == Direction.EAST) // true
```
La correspondance est sensible à la casse : `Direction.valueOf("east")` lève une `IllegalArgumentException` car aucune entrée ne porte ce nom.

---

Un enum peut déclarer une **méthode abstraite** et laisser chaque entrée fournir sa propre implémentation dans un corps entouré d'accolades :
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
Chaque entrée se comporte différemment tout en partageant le même type et la même signature de méthode.

---

Une **interface** déclare des méthodes sans corps ; tout type qui l'implémente doit les fournir :
```kotlin
interface Greeter {
    fun greet(): String
}
```
Les enums peuvent implémenter des interfaces. On liste l'interface après un deux-points et on marque chaque implémentation avec `override`. À l'intérieur du corps de l'enum, l'entrée courante est `this` et les autres entrées peuvent être référencées sans le nom de la classe :
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
