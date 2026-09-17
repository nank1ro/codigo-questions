Une `data class` est une classe dont le rôle est de **stocker des données**. À partir des propriétés que vous déclarez dans le constructeur principal, le compilateur génère pour vous quatre membres :

- `toString()`, un texte lisible `ClassName(prop=value, ...)`
- `equals()` et `hashCode()`, pour que deux instances avec les mêmes données soient considérées comme égales
- `copy()`, qui construit une nouvelle instance en réutilisant les valeurs actuelles

```kotlin
data class Book(val title: String, val pages: Int)

val book = Book("Dune", 412)
println(book)          // Book(title=Dune, pages=412)
println(book.copy())   // Book(title=Dune, pages=412)
```

`copy()` brille vraiment avec les **arguments nommés** : vous nommez uniquement les propriétés que vous voulez changer, et toutes les autres valeurs sont conservées.

```kotlin
println(book.copy(pages = 500)) // Book(title=Dune, pages=500)
```

L'original n'est jamais modifié : `copy()` renvoie un tout nouvel objet.

---

Pour chaque propriété du constructeur principal, une data class génère aussi une fonction `componentN()` : `component1()` pour la première propriété, `component2()` pour la deuxième, et ainsi de suite.

Ces fonctions alimentent les **déclarations de déstructuration**, où vous décomposez un objet en plusieurs variables en une seule ligne :

```kotlin
data class Point(val x: Int, val y: Int)

val point = Point(3, 7)
val (x, y) = point
println(x)               // 3
println(point.component2()) // 7
```

L'ordre des variables suit l'ordre des propriétés, pas leurs noms. Utilisez `_` pour ignorer celle dont vous n'avez pas besoin :

```kotlin
val (_, onlyY) = point
```

---

Le `equals()` généré fait de `==` une comparaison **structurelle** : deux instances sont égales quand chaque propriété du constructeur principal est égale. L'opérateur `===` est différent, il demande si les deux noms pointent vers le **même objet** en mémoire.

```kotlin
data class User(val id: Int, val name: String)

val a = User(1, "Ann")
val b = User(1, "Ann")
println(a == b)  // true, mêmes données
println(a === b) // false, deux objets différents
println(a === a) // true
```

Comme `hashCode()` est généré avec `equals()`, les instances d'une data class se comportent aussi correctement dans un `Set` ou comme clés d'un `Map` : les doublons fusionnent.

```kotlin
println(setOf(a, b).size) // 1
```

Une classe régulière ne génère rien de tout cela, donc pour elle `==` retombe sur l'identité.

---

Les membres générés ne regardent que les propriétés déclarées dans le **constructeur principal**. Une propriété déclarée dans le **corps** de la classe est une propriété normale : elle ne fait partie ni de `toString()`, ni de `equals()`, ni de `hashCode()`, ni de `copy()`.

```kotlin
data class Item(val name: String) {
    var quantity: Int = 0
}

val a = Item("nail")
a.quantity = 5
println(a) // Item(name=nail)
```

C'est facile à oublier, alors mettez dans le constructeur principal tout ce qui identifie l'objet, et gardez l'état dérivé ou temporaire dans le corps.

---

Une classe `sealed` décrit un ensemble **fermé** d'alternatives : seules les sous-classes écrites dans le même package et le même module sont autorisées, ainsi le compilateur connaît chacune d'elles.

```kotlin
sealed class Shape
data class Circle(val radius: Int) : Shape()
data class Square(val side: Int) : Shape()
```

Le bénéfice, c'est le `when` **exhaustif** : quand vous branchez sur un type sealed et couvrez chaque sous-classe, vous pouvez omettre la branche `else`. Ajoutez une nouvelle sous-classe plus tard et le compilateur signale chaque `when` que vous avez oublié de mettre à jour, au lieu de prendre silencieusement le `else`.

```kotlin
fun name(shape: Shape): String = when (shape) {
    is Circle -> "circle"
    is Square -> "square"
}
```

Après `is Circle`, la valeur subit un smart cast, donc `shape.radius` est disponible dans cette branche sans aucun cast manuel.

---

Parfois, vous avez besoin d'exactement **une** instance de quelque chose : un logger, un registre, une configuration d'application. Remplacer `class` par `object` déclare ce singleton pour vous :

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

L'instance est créée la première fois que vous la touchez, et vous utilisez le nom lui-même, il n'y a pas d'appel `Registry()` ni de constructeur. Un `object` peut contenir des propriétés, des méthodes, des blocs `init`, et il peut implémenter des interfaces ou étendre une classe.

---

Un `companion object` est le singleton qui appartient à une classe. En plus des constantes, son rôle naturel est d'héberger des **fonctions fabrique** : des fonctions qui vérifient ou transforment l'entrée avant de construire une instance, et qui peuvent retourner `null` quand l'entrée n'a pas de sens.

Marquer le constructeur `private` force chaque appelant à passer par la fabrique :

```kotlin
class Age private constructor(val years: Int) {
    companion object {
        fun of(years: Int): Age? = if (years >= 0) Age(years) else null
    }
}

println(Age.of(30)?.years) // 30
println(Age.of(-1))        // null
```

Le companion est appelé sur le nom de la classe, `Age.of(...)`, et il peut atteindre le constructeur privé car il vit à l'intérieur de la classe.

---

Une `interface` liste ce qu'un type peut faire. Ses membres sont abstraits par défaut, mais une interface peut aussi fournir une **implémentation par défaut**, un corps que chaque classe implémentante hérite gratuitement et peut redéfinir :

```kotlin
interface Greeter {
    val name: String              // abstrait, la classe doit le fournir
    fun greet(): String = "Hi, $name"  // implémentation par défaut
}

class Person(override val name: String) : Greeter

class Robot(override val name: String) : Greeter {
    override fun greet(): String = "BEEP $name"
}

println(Person("Ann").greet()) // Hi, Ann
println(Robot("R2").greet())   // BEEP R2
```

Une interface ne peut pas stocker d'état (elle n'a pas de backing fields), donc une propriété abstraite doit être implémentée par la classe, généralement avec `override val` dans le constructeur. Contrairement à une classe, un type peut implémenter autant d'interfaces qu'il le souhaite.

---

Une classe `abstract` se situe entre une interface et une classe normale : elle ne peut pas être instanciée, et elle mélange des membres **abstraits**, qui n'ont pas de corps et doivent être redéfinis, avec des membres concrets que les sous-classes héritent tels quels.

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

Contrairement à une interface, une classe abstraite a un constructeur et peut stocker un état dans des propriétés, c'est pourquoi la sous-classe remonte `name` avec `: Vehicle(name)`. Une classe ne peut étendre qu'une seule classe, donc tournez-vous vers une classe abstraite quand les sous-classes partagent des données, et vers une interface quand elles ne partagent que du comportement. Les membres abstraits sont redéfinissables sans ajouter `open`.

---

Une classe déclarée à l'intérieur d'une autre classe est **imbriquée** par défaut. Elle ne sait rien de l'instance externe et vous la construisez à partir du nom de la classe externe :

```kotlin
class Outer {
    class Nested {
        fun hello() = "hi"
    }
}

println(Outer.Nested().hello()) // hi
```

Ajoutez le mot-clé `inner` et la situation change : une classe `inner` porte une référence vers l'instance externe, donc elle peut lire les propriétés externes, et vous la construisez **à partir d'une instance** :

```kotlin
class Counter(val step: Int) {
    inner class Doubler {
        fun value() = step * 2
    }
}

println(Counter(5).Doubler().value()) // 10
```

À l'intérieur d'une classe `inner`, `this` est l'objet interne ; utilisez `this@Counter` quand vous avez besoin explicitement de l'objet externe.

---

Les pièces de ce sujet se combinent habituellement : une `enum class` dont les entrées portent leurs propres propriétés modélise un ensemble fixe de balises, tandis qu'une `data class` transporte la charge utile qui les accompagne.

```kotlin
enum class Speed(val surcharge: Int) {
    STANDARD(0),
    EXPRESS(15)
}

data class Order(val total: Int, val speed: Speed)

val order = Order(100, Speed.EXPRESS)
println(order.total + order.speed.surcharge) // 115
```
