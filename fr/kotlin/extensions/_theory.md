Une **fonction d'extension** ajoute une nouvelle fonction à un type existant sans toucher à son code source.
Vous écrivez `fun`, puis le type que vous voulez étendre (le **type receveur**), un point et le nom de la fonction :
```kotlin
fun Int.squared(): Int {
    return this * this
}
println(4.squared()) // 16
```
Dans la fonction, `this` est la valeur sur laquelle la fonction est appelée, appelée le **receveur** : dans `4.squared()` c'est `4`.
Une fois l'extension définie, vous l'appelez avec le point exactement comme une fonction qui aurait fait partie de `Int` depuis le début.

---

Les extensions fonctionnent sur n'importe quel type, même ceux dont vous n'avez pas le code source. `String` vient de la bibliothèque standard, mais vous pouvez quand même lui donner de nouvelles fonctions :
```kotlin
fun String.whisper(): String {
    return this.lowercase() + "..."
}
println("HELLO".whisper()) // hello...
```
Dans une extension vous pouvez omettre `this.` en utilisant les autres membres du receveur : `lowercase()` seul signifie `this.lowercase()`, et `length` seul signifie `this.length`.

---

Une fonction d'extension peut prendre des paramètres comme n'importe quelle autre fonction. Le receveur reste à gauche du point et les paramètres vont entre les parenthèses :
```kotlin
fun Int.isDivisibleBy(other: Int): Boolean {
    return this % other == 0
}
println(12.isDivisibleBy(4)) // true
println(12.isDivisibleBy(5)) // false
```
Le type devant le point est un type normal, vous pouvez donc étendre `List<Int>`, `Double` ou une classe que vous avez écrite de la même façon.

---

Une extension ne modifie **pas** la classe qu'elle étend et n'y insère pas de nouveau membre. Le compilateur réécrit simplement l'appel : `"kotlin".first3()` devient un appel à la fonction avec `"kotlin"` passé en tant que `this`.
```kotlin
fun String.first3(): String = take(3)
val word = "kotlin"
println(word.first3()) // kot
```
C'est pourquoi vous pouvez étendre des classes finales comme `String` et `Int` : rien ne change à l'intérieur, l'extension vit uniquement dans votre code.

---

En plus des fonctions, vous pouvez ajouter une **propriété d'extension**. Elle se déclare avec `val`, le type receveur, un point et le nom, suivis d'un `get()` qui calcule la valeur à chaque lecture de la propriété :
```kotlin
val String.wordCount: Int
    get() = split(" ").size

println("Kotlin is fun".wordCount) // 3
```
Une propriété d'extension ne peut rien stocker : elle n'a pas de champ de stockage, donc un initialiseur comme `val String.label = "text"` est une erreur de compilation. Elle peut seulement calculer sa valeur à partir du receveur.
Les propriétés d'extension ne peuvent pas être déclarées dans une fonction (les propriétés d'extension locales ne sont pas autorisées), contrairement aux fonctions d'extension.

---

Les propriétés d'extension se lisent sans parenthèses, exactement comme le `length` intégré d'une `String`. Elles sont le choix naturel quand la valeur décrit le receveur au lieu d'en faire quelque chose :
```kotlin
val Int.isNegative: Boolean
    get() = this < 0

println((-3).isNegative) // true
println(7.isNegative)    // false
```
Remarquez les parenthèses autour de `-3` : sans elles, `-3.isNegative` lirait d'abord la propriété de `3` puis essaierait de nier un `Boolean`, ce qui ne compile pas.

---

Le type receveur peut être **nullable**. Une extension sur `String?` peut être appelée sur une variable qui peut contenir `null`, et dans la fonction `this` est un `String?`, donc vous gérez vous-même le cas `null`, généralement avec l'opérateur Elvis `?:` rencontré dans les leçons sur la nullabilité :
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val name: String? = null
println(name.orDash())  // -
println("Ada".orDash()) // Ada
```
Appeler `name.orDash()` sur une valeur `null` est sûr : aucun `?.` n'est nécessaire, car la fonction elle-même accepte un receveur `null`.

---

Dans une extension avec un receveur nullable vous pouvez aussi utiliser l'appel sûr `this?.` pour atteindre les membres de la valeur seulement quand elle n'est pas `null`. La bibliothèque standard utilise la même idée pour des fonctions comme `isNullOrEmpty()` :
```kotlin
fun String?.firstOrQuestion(): Char {
    return this?.firstOrNull() ?: '?'
}
val text: String? = null
println(text.firstOrQuestion())    // ?
println("Kotlin".firstOrQuestion()) // K
```

---

Quand une classe possède déjà un membre avec le même nom et les mêmes paramètres qu'une extension, **le membre gagne toujours** : l'extension n'est jamais appelée, et le compilateur vous avertit qu'elle est masquée.
```kotlin
class Box {
    fun describe(): String = "member"
}
fun Box.describe(): String = "extension"

println(Box().describe()) // member
```
Une extension ne peut pas redéfinir ni remplacer un comportement existant ; elle peut seulement ajouter de nouvelles fonctions et propriétés. Pour être choisie, une extension a besoin d'un nom ou d'une liste de paramètres que la classe n'a pas déjà.

---

Une extension peut travailler sur toute une famille de types grâce à un **paramètre de type** : un espace réservé pour un type, déclaré entre chevrons juste après `fun`, que Kotlin remplit à chaque appel. Cela rend l'extension **générique** :
```kotlin
fun <T> List<T>.second(): T {
    return this[1]
}
println(listOf(1, 2, 3).second())      // 2
println(listOf("a", "b").second())     // b
```
Avec `listOf(1, 2, 3)` l'espace réservé `T` est `Int`, avec `listOf("a", "b")` c'est `String`, ainsi la même fonction retourne le bon type à chaque fois.

---

Le paramètre de type peut être utilisé partout dans la signature : comme type de retour, comme `T?` nullable, ou à l'intérieur d'un autre type. Une extension générique qui peut ne rien trouver retourne `T?`, comme le `firstOrNull()` intégré :
```kotlin
fun <T> List<T>.lastOrDefault(default: T): T {
    return if (isEmpty()) default else this[size - 1]
}
println(listOf(1, 2).lastOrDefault(0))          // 2
println(emptyList<String>().lastOrDefault("-")) // -
```
Dans la fonction vous pouvez utiliser `size`, `isEmpty()` et l'indexation exactement comme sur n'importe quelle liste, car le receveur est une `List<T>`.

---

Vous pouvez aussi étendre le **companion object** d'une classe, tant que la classe en déclare un, même vide. Le type receveur s'écrit `ClassName.Companion`, et l'extension s'appelle alors sur le nom de la classe, comme une fonction fabrique :
```kotlin
class Temperature(val degrees: Int) {
    companion object
}
fun Temperature.Companion.freezing(): Temperature = Temperature(0)

println(Temperature.freezing().degrees) // 0
```
La classe et l'extension sont toutes deux des déclarations de premier niveau, elles doivent donc être écrites en dehors de `main`.

---

Une extension sur companion peut prendre des paramètres, ce qui en fait un endroit pratique pour des constructeurs alternatifs qui convertissent depuis une autre unité ou un autre format :
```kotlin
class Distance(val meters: Int) {
    companion object
}
fun Distance.Companion.fromKilometers(km: Int): Distance = Distance(km * 1000)

println(Distance.fromKilometers(3).meters) // 3000
```

---

L'endroit où vous déclarez une extension détermine où elle peut être utilisée, sa **portée** :
- au premier niveau d'un fichier, elle est disponible dans tout le fichier et dans le reste du package
- dans une fonction, c'est une extension locale, utilisable seulement dans cette fonction
- dans une classe, c'est une **extension membre**, utilisable seulement dans cette classe

Une extension membre peut lire les propriétés de la classe où elle vit, elle combine donc deux receveurs : l'instance de la classe et la valeur sur laquelle elle est appelée :
```kotlin
class Greeter(val greeting: String) {
    fun String.greet(): String = "$greeting, $this!"
    fun welcome(name: String): String = name.greet()
}
println(Greeter("Hello").welcome("Ada")) // Hello, Ada!
```
Dans `greet`, `greeting` vient du `Greeter` et `this` est la `String` sur laquelle la fonction est appelée. En dehors de la classe, `"Ada".greet()` est une erreur de compilation.

---

Une fonction d'extension avec exactement **un** paramètre peut être marquée `infix`. Une fonction infix peut être appelée sans le point ni les parenthèses, avec le receveur à gauche et l'argument à droite, ce qui se lit presque comme une phrase :
```kotlin
infix fun Int.percentOf(total: Int): Int = total * this / 100

println(20 percentOf 50)   // 10
println(20.percentOf(50))  // 10, the normal call still works
```
Kotlin s'en sert aussi pour certaines fonctions intégrées : `1 to "one"` construit une `Pair`, et `1 until 5` construit un intervalle.

---

Pour être marquée `infix`, une fonction doit être un membre ou une extension, doit prendre exactement un paramètre, et ce paramètre ne peut pas avoir de valeur par défaut. Tout le reste est une erreur de compilation :
```kotlin
infix fun Int.add(other: Int): Int = this + other          // ok
infix fun add(a: Int, b: Int): Int = a + b                 // error: not a member or extension
infix fun Int.add(a: Int, b: Int): Int = this + a + b      // error: two parameters
```
Les appels infix ont une priorité située entre l'arithmétique et la comparaison : `1 add 2 * 3` vaut `1 add 6`, tandis que `1 add 2 == 3` compare le résultat avec `3`.
