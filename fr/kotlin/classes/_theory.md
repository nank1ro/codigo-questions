Une **classe** est un modèle pour créer des objets. En Kotlin, on déclare une classe avec le mot-clé `class` suivi du nom de la classe.

Une classe peut contenir des **propriétés** (données) et des **méthodes** (comportement). Pour déclarer une propriété directement dans le constructeur, on la fait précéder de `val` ou `var` :

```kotlin
class Dog(val name: String)
```

Cela crée une classe `Dog` avec une propriété `name`. On crée une instance en appelant la classe comme une fonction :

```kotlin
val dog = Dog("Rex")
println(dog.name) // Rex
```

---

Les classes peuvent avoir plusieurs propriétés dans leur **constructeur primaire**. Chaque propriété est déclarée avec `val` (lecture seule) ou `var` (mutable) directement dans la liste des paramètres du constructeur :

```kotlin
class Person(val name: String, var age: Int)
```

Le mot-clé `val` rend `name` en lecture seule après la création, tandis que `var` rend `age` mutable — on peut le modifier ensuite :

```kotlin
val p = Person("Alice", 30)
p.age = 31  // autorisé car age est var
```

---

Le **bloc `init`** s'exécute immédiatement après le constructeur primaire. Il est utilisé pour effectuer une validation ou une logique d'initialisation lors de la création d'un objet :

```kotlin
class Circle(val radius: Double) {
    init {
        require(radius > 0) { "Radius must be positive" }
    }
}
```

On peut aussi initialiser des propriétés supplémentaires dans `init` :

```kotlin
class Square(val side: Int) {
    val area: Int
    init {
        area = side * side
    }
}
```

---

Les classes peuvent contenir des **méthodes** — des fonctions qui appartiennent à la classe et opèrent sur ses propriétés :

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

Les méthodes sont appelées en utilisant la notation pointée sur une instance :

```kotlin
val c = Counter(0)
c.increment()
println(c.value()) // 1
```

---

Une **`data class`** est une classe spéciale conçue pour contenir des données. Kotlin génère automatiquement `equals()`, `hashCode()`, `toString()` et `copy()` :

```kotlin
data class Point(val x: Int, val y: Int)

val p = Point(1, 2)
println(p)            // Point(x=1, y=2)
println(p.toString()) // Point(x=1, y=2)
```

La fonction `copy()` crée une nouvelle instance avec certaines propriétés modifiées :

```kotlin
val p2 = p.copy(y = 10)
println(p2) // Point(x=1, y=10)
```
