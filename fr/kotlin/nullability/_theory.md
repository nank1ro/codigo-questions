Parfois, une valeur est tout simplement absente : un utilisateur sans deuxième prénom, une recherche qui ne trouve rien, un texte qui ne peut pas être converti en nombre.
Kotlin représente une valeur absente avec `null`, mais une variable normale ne peut jamais la contenir. Chaque type est **non null** par défaut :
```kotlin
var city: String = null // error: Null can not be a value of a non-null type String
```
Pour autoriser une valeur absente, on déclare un type **nullable** en ajoutant un point d'interrogation `?` après le type.
Un `String?` contient soit un `String`, soit `null` :
```kotlin
var city: String? = "Rome"
city = null // allowed
println(city) // null
```
`String` et `String?` sont deux types différents : un `String` n'est jamais absent, un `String?` peut l'être.

---

La différence entre `String` et `String?` est vérifiée par le **compilateur**, et non à l'exécution.
Affecter `null` à un type non null, ou passer une valeur nullable là où une valeur non null est attendue, est une erreur de compilation, si bien que le programme ne démarre même pas :
```kotlin
val name: String = null        // does not compile
val maybe: String? = "hi"
val sure: String = maybe       // does not compile: String? is not a String
```
C'est ainsi que Kotlin évite les plantages « null pointer » courants dans d'autres langages : une valeur ne peut être absente qu'aux endroits où vous l'avez explicitement déclarée avec `?`.

---

Le `?` fonctionne partout où un type est écrit : une fonction peut accepter un paramètre nullable et retourner une valeur nullable.
```kotlin
fun firstChar(text: String?): Char? {
    ...
}
```
On ne peut pas appeler directement une méthode sur une valeur nullable, car elle pourrait être `null`.
L'opérateur d'**appel sûr** `?.` appelle la méthode uniquement lorsque la valeur n'est pas `null` ; sinon, l'expression entière vaut `null` :
```kotlin
val word: String? = "kotlin"
println(word?.length)   // 6
val none: String? = null
println(none?.length)   // null
```
Le résultat d'un appel sûr est toujours nullable : `word?.length` est un `Int?`, et non un `Int`.

---

Très souvent, tout ce que l'on attend d'une valeur nullable, c'est la valeur elle-même ou une valeur par défaut.
L'**opérateur Elvis** `?:` fait exactement cela : il retourne le membre de gauche lorsqu'il n'est pas `null`, sinon la valeur située à sa droite :
```kotlin
val name: String? = null
val shown = name ?: "Guest" // shown is a String equal to "Guest"
```
Comme le membre de droite n'est utilisé que lorsque celui de gauche vaut `null`, le résultat est non null lorsque la valeur par défaut l'est.
`?:` se combine harmonieusement avec `?.` pour ramener un appel sûr à une valeur ordinaire :
```kotlin
val len = name?.length ?: 0 // len is an Int, 0 when name is null
```

---

Les appels sûrs peuvent être **enchaînés** : dès qu'un maillon est `null`, le reste de la chaîne est ignoré et l'expression entière devient `null`.
```kotlin
val text: String? = "  hi  "
println(text?.trim()?.uppercase())   // HI
val none: String? = null
println(none?.trim()?.uppercase())   // null, trim() and uppercase() never run
```
Une chaîne qui se termine par `?:` vous donne un résultat non null en une seule ligne :
```kotlin
val cleaned = text?.trim()?.uppercase() ?: ""
```

---

Les chaînes d'appels sûrs brillent avec les objets imbriqués, où n'importe quel niveau peut être absent :
```kotlin
class Address(val city: String?)
class User(val address: Address?)

val user = User(Address("Rome"))
println(user.address?.city ?: "unknown") // Rome
val nobody = User(null)
println(nobody.address?.city ?: "unknown") // unknown
```
Chaque `?.` protège l'étape suivante, et le `?:` final fournit la valeur par défaut.

---

L'opérateur d'**assertion non null** `!!` convertit une valeur nullable en une valeur non null, en disant au compilateur « je suis sûr que ce n'est pas `null` » :
```kotlin
val word: String? = "kotlin"
println(word!!.length) // 6
```
Si vous vous trompez et que la valeur est `null`, le programme plante à l'exécution avec une `NullPointerException`, l'erreur même que Kotlin a été conçu pour prévenir :
```kotlin
val none: String? = null
println(none!!.length) // NullPointerException
```
N'utilisez `!!` que lorsque la valeur ne peut vraiment pas être `null` ; préférez `?.`, `?:` et les vérifications de null partout ailleurs.

---

Lorsque vous vérifiez avec `if` qu'une valeur n'est pas `null`, le compilateur s'en souvient : dans la branche où la valeur est connue comme étant non null, elle subit un **smart cast** vers le type non null et vous pouvez l'utiliser directement, sans `?.` ni `!!` :
```kotlin
fun greet(name: String?): String {
    if (name != null) {
        return "Hello, " + name.uppercase() // name is a String here
    }
    return "Hello, stranger"
}
```
La même chose se produit après une sortie anticipée :
```kotlin
fun greet(name: String?): String {
    if (name == null) return "Hello, stranger"
    return "Hello, " + name.uppercase() // name is a String from here on
}
```
Les smart casts fonctionnent sur les variables `val` et les paramètres de fonction, dont la valeur ne peut pas changer entre la vérification et l'utilisation.

---

`let` exécute un bloc de code avec la valeur sur laquelle il est appelé, disponible à l'intérieur du bloc sous le nom `it`.
Combiné à un appel sûr, `?.let` exécute le bloc **uniquement** lorsque la valeur n'est pas `null`, et à l'intérieur du bloc `it` est non null :
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to $it") } // prints Sending to ada@example.com
val missing: String? = null
missing?.let { println("Sending to $it") } // nothing happens
```
C'est une alternative compacte à `if (x != null) { ... }` lorsque vous n'avez besoin de la valeur qu'à l'intérieur du bloc.

---

`let` **retourne** également la valeur de la dernière expression de son bloc, si bien que `?.let` peut transformer une valeur nullable et `?:` peut fournir la valeur par défaut lorsqu'elle est `null` :
```kotlin
fun priceLabel(price: Double?): String {
    return price?.let { "$it EUR" } ?: "free"
}
println(priceLabel(9.5))  // 9.5 EUR
println(priceLabel(null)) // free
```
Lorsque `price` est `null`, le bloc `let` est ignoré, l'expression vaut `null` et l'opérateur Elvis retourne `"free"`.

---

Les collections peuvent aussi contenir des éléments nullables : une `List<Int?>` peut contenir des entrées `null`, tandis qu'une `List<Int>` n'en contient jamais.
`filterNotNull()` retourne une nouvelle liste dont les entrées `null` sont retirées, et le type de ses éléments devient non null, si bien que vous pouvez utiliser les éléments librement :
```kotlin
val scores: List<Int?> = listOf(10, null, 20)
val valid = scores.filterNotNull() // List<Int> [10, 20]
println(valid.sum())               // 30
```

---

De nombreuses fonctions standard retournent `null` au lieu d'échouer. `toIntOrNull()` convertit une chaîne en un `Int`, ou retourne `null` lorsque le texte n'est pas un nombre entier :
```kotlin
println("42".toIntOrNull())  // 42
println("4x2".toIntOrNull()) // null
```
`mapNotNull` transforme chaque élément comme `map`, mais écarte les résultats qui valent `null` :
```kotlin
val words = listOf("1", "two", "3")
println(words.mapNotNull { it.toIntOrNull() }) // [1, 3]
```

---

Parfois, une propriété ne peut pas recevoir de valeur lors de la création de l'objet, mais vous savez qu'elle sera définie avant d'être utilisée.
Au lieu de la rendre nullable, marquez-la avec `lateinit` : le type reste non null et aucun `?.` n'est nécessaire pour la lire :
```kotlin
class Game {
    lateinit var player: String

    fun start(name: String) {
        player = name
    }
}
```
`lateinit` a quelques règles : il ne fonctionne que sur les propriétés `var`, uniquement avec des types non null, et pas avec les types primitifs comme `Int` ou `Boolean`.
Lire une propriété `lateinit` avant de l'affecter lève une `UninitializedPropertyAccessException` ; vous pouvez d'abord la vérifier avec `::player.isInitialized`.

---

Lorsqu'un `null` signifie que l'appelant a fait une erreur, échouez tôt avec `requireNotNull`.
Il retourne la valeur comme non null lorsqu'elle est présente, et lève une `IllegalArgumentException` lorsqu'elle vaut `null`, avec un message optionnel :
```kotlin
fun greet(name: String?): String {
    val safeName = requireNotNull(name) { "name is required" }
    return "Hello, $safeName"
}
greet(null) // IllegalArgumentException: name is required
```
Après l'appel, le compilateur applique aussi un smart cast à `name` elle-même en `String`, si bien que `name.length` est autorisé à partir de cette ligne.
Contrairement à `!!`, l'échec comporte un message clair et indique que c'est l'*argument* qui était incorrect.

---

Une fonction d'extension peut être déclarée sur un **récepteur nullable**, si bien qu'elle peut être appelée même sur une valeur `null`. À l'intérieur, `this` est nullable et doit être vérifié :
```kotlin
fun String?.orDash(): String {
    return this ?: "-"
}
val none: String? = null
println(none.orDash()) // -
```
Notez qu'aucun `?.` n'est nécessaire au site d'appel : la fonction gère elle-même le cas `null`.
La bibliothèque standard utilise cette astuce dans `isNullOrEmpty()` et `orEmpty()`, qui peuvent être appelées sans risque sur n'importe quel `String?`.

---

Le membre de droite de `?:` peut être n'importe quelle expression, y compris `return`. Cela offre une manière compacte de sortir d'une fonction dès qu'une valeur est absente :
```kotlin
fun firstUpper(text: String?): Char? {
    val first = text?.firstOrNull() ?: return null
    return first.uppercaseChar() // first is a Char here
}
```
Tous les outils que vous avez vus se combinent bien : les paramètres nullables et les types de retour décrivent *où* une valeur peut être absente, et `?.`, `?:`, `let`, les smart casts et `toIntOrNull` la gèrent sans jamais planter.
