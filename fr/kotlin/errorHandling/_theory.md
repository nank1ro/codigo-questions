Une **exception** est la façon dont Kotlin signale qu'une instruction ne peut pas être exécutée. Convertir `"abc"` en nombre, diviser un entier par zéro ou lire au-delà de la fin d'une liste en lèvent toutes.

```kotlin
fun main() {
    println("before")
    val n = "abc".toInt()
    println("after")
}
```
Ce programme affiche `before` puis s'arrête. `toInt()` ne peut pas lire `"abc"`, donc il **lève** une `NumberFormatException` ; rien dans le programme ne la traite, si bien que Kotlin termine le programme avec un rapport d'erreur et `after` n'est jamais affiché.

Vous pouvez aussi lever une exception vous-même avec le mot-clé `throw` :
```kotlin
throw Exception("something went wrong")
```

Une exception que personne ne traite n'est pas un avertissement : c'est la fin de l'exécution.

---

Pour garder le programme en vie, placez l'instruction risquée dans un bloc `try` et décrivez la récupération dans un bloc `catch` :
```kotlin
try {
    println("abc".toInt())
} catch (e: Exception) {
    println("cannot read that number")
}
println("still running")
```
Kotlin exécute le bloc `try` ; dès qu'une instruction qu'il contient lève une exception, le reste du bloc est ignoré et le contrôle saute au bloc `catch`. Le nom entre parenthèses — `e` ici — est l'objet exception, et `Exception` est le type intercepté.

Une fois le bloc `catch` terminé, le programme continue normalement avec la ligne qui suit l'ensemble `try`/`catch`.

---

Intercepter `Exception` intercepte tout, ce qui est rarement ce que vous voulez : une faute de frappe ailleurs dans le bloc serait aussi avalée. Nommez plutôt le **type exact** dont vous savez récupérer.

Chaque échec a son propre type. `"abc".toInt()` lève une `NumberFormatException`, c'est donc ce type qu'il faut intercepter :
```kotlin
try {
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("that is not a number")
}
```
Si un autre type d'exception est levé dans le bloc, ce `catch` ne correspond pas et l'exception continue de se propager hors de la fonction.

---

Un `try` peut être suivi de plusieurs blocs `catch`, chacun gérant un type différent :
```kotlin
val letters = listOf("a", "b")
val index = 5
val text = "abc"
try {
    println(letters[index] + text.toInt())
} catch (e: NumberFormatException) {
    println("not a number")
} catch (e: IndexOutOfBoundsException) {
    println("no such letter")
} catch (e: Exception) {
    println("something else went wrong")
}
```
Kotlin essaie les blocs **de haut en bas** et exécute le premier dont le type correspond. Un seul bloc est exécuté.

L'ordre a donc de l'importance. `NumberFormatException` et `IndexOutOfBoundsException` sont toutes deux des variantes d'`Exception`, donc un `catch (e: Exception)` écrit en premier correspondrait à chaque échec et les blocs en dessous ne seraient jamais exécutés. Écrivez le type le plus spécifique en premier et le plus général en dernier.

---

Un bloc `finally` peut être ajouté à la fin. Il s'exécute **quoi qu'il arrive** : après un `try` réussi, après qu'un `catch` a récupéré, et même lorsque l'exception n'est pas interceptée du tout.

```kotlin
try {
    println("reading")
    println("abc".toInt())
} catch (e: NumberFormatException) {
    println("bad number")
} finally {
    println("closing")
}
```
```
reading
bad number
closing
```
C'est donc l'endroit pour le nettoyage qui ne doit pas être sauté, comme la fermeture d'un fichier. Un `try` a besoin d'au moins un `catch` ou un `finally`, mais il peut avoir les deux.

---

En Kotlin, `try` n'est pas seulement une instruction : c'est une **expression** qui produit une valeur. La valeur est la dernière expression du bloc qui s'est exécuté — le bloc `try` quand rien n'a échoué, le bloc `catch` dans le cas contraire.

```kotlin
val n = try { "abc".toInt() } catch (e: NumberFormatException) { 0 }
println(n) // 0
```
C'est la forme idiomatique en Kotlin. Au lieu de déclarer une `var`, de l'affecter à deux endroits et d'espérer que chaque chemin la définit, vous obtenez une seule `val` qui contient toujours une valeur utilisable.

Notez qu'un bloc `finally` ne change jamais la valeur : il ne s'exécute que pour ses effets de bord.

---

Comme `try` est une expression, il peut être utilisé partout où une valeur est attendue — notamment comme corps entier d'une fonction écrite avec `=` :
```kotlin
fun length(text: String): Int = try {
    text.toInt()
} catch (e: NumberFormatException) {
    -1
}
```
Les deux blocs doivent produire une valeur du même type, ici `Int`. Écrivez la valeur de repli comme dernière expression du bloc `catch` ; il n'y a pas de `return` dans l'un ou l'autre bloc.

---

Lever et intercepter n'est pas gratuit, et pour les conversions courantes Kotlin propose une variante moins coûteuse qui retourne simplement `null` au lieu de lever une exception : `toIntOrNull()`, `toDoubleOrNull()`, `toLongOrNull()`.

```kotlin
println("42".toIntOrNull())  // 42
println("abc".toIntOrNull()) // null
```
Combiné à l'opérateur elvis `?:`, qui fournit une valeur de remplacement lorsque la valeur à sa gauche est `null`, l'ensemble `try`/`catch` se réduit à une seule ligne :
```kotlin
val n = "abc".toIntOrNull() ?: 0
println(n) // 0
```
Recourez à `try`/`catch` lorsque l'échec est vraiment exceptionnel ; recourez à `toIntOrNull()` lorsqu'une entrée incorrecte est attendue.

---

Vos propres fonctions peuvent refuser une entrée incorrecte de la même manière que la bibliothèque standard, avec `throw`. La bibliothèque fournit déjà un type pour le cas le plus courant : `IllegalArgumentException` signifie « la valeur que vous m'avez passée n'est pas acceptable ».

```kotlin
fun half(n: Int): Int {
    if (n < 0) throw IllegalArgumentException("n must not be negative")
    return n / 2
}
```
`throw` termine la fonction immédiatement — le `return` en dessous n'est jamais atteint. L'appelant décide quoi en faire :
```kotlin
try { println(half(-4)) }
catch (e: IllegalArgumentException) { println("rejected") }
```
Lever une exception vaut mieux que retourner silencieusement une valeur inventée : une réponse fausse se propage loin, une exception s'arrête au premier appelant prêt à la traiter.

---

Chaque exception transporte le texte avec lequel elle a été créée. Dans un bloc `catch`, vous le lisez via la propriété `message` de l'objet exception :
```kotlin
try {
    throw IllegalArgumentException("price must be positive")
} catch (e: IllegalArgumentException) {
    println(e.message) // price must be positive
}
```
`message` est nullable, car une exception peut être construite sans aucun texte ; `e.message ?: "unknown"` fournit une valeur de remplacement sûre lorsque vous avez besoin d'un simple `String`.

Préférez afficher `e.message` plutôt que l'objet exception lui-même : le texte propre à l'objet inclut aussi le nom de la classe, ce qui est du bruit pour la personne qui lit la sortie.

---

Écrire `if (...) throw IllegalArgumentException(...)` pour chaque argument devient bruyant, si bien que Kotlin fournit deux raccourcis qui se lisent comme des phrases simples :

```kotlin
require(n >= 0) { "n must not be negative" }   // lève une IllegalArgumentException
check(started) { "not started" }               // lève une IllegalStateException
```
Toutes deux prennent une condition et un bloc produisant le message, et toutes deux lèvent une exception **lorsque la condition est fausse**. La seule différence est le type d'exception, et cette différence est un message pour le lecteur :

* `require` protège les **arguments** passés par l'appelant, et échoue avec une `IllegalArgumentException`.
* `check` protège l'**état** de l'objet ou du programme, et échoue avec une `IllegalStateException`.

Le bloc n'est évalué que lorsque la vérification échoue, si bien que construire le message ne coûte rien lorsque tout va bien.

---

Lorsqu'aucun des types intégrés ne décrit bien votre échec, déclarez le vôtre. Une exception est une classe ordinaire qui étend `Exception` et transmet son texte au parent :

```kotlin
class InsufficientFundsException(message: String) : Exception(message)
```
Cette seule ligne est un type d'exception complet. Elle est levée et interceptée comme n'importe quelle autre, et `e.message` retourne le texte avec lequel elle a été construite :
```kotlin
try {
    throw InsufficientFundsException("balance too low")
} catch (e: InsufficientFundsException) {
    println(e.message) // balance too low
}
```
Le gain est la précision : un appelant peut intercepter `InsufficientFundsException` seule et laisser chaque autre échec continuer de se propager.

---

`runCatching` exécute un bloc et ne laisse jamais une exception s'échapper. À la place, il rend un `Result`, un objet contenant **soit** la valeur produite par le bloc, **soit** l'exception qu'il a levée :

```kotlin
val ok = runCatching { "42".toInt() }
val bad = runCatching { "abc".toInt() }

println(ok.isSuccess)   // true
println(bad.isFailure)  // true
```
La valeur est lue ensuite, et vous choisissez ce que doit devenir un échec :
```kotlin
println(ok.getOrNull())      // 42
println(bad.getOrNull())     // null
println(bad.getOrElse { 0 }) // 0
```
`getOrNull()` transforme un échec en `null`, tandis que `getOrElse { ... }` exécute le bloc pour construire une valeur de remplacement. Rien n'est levé sur le site d'appel, si bien que l'échec peut être transporté et traité plus tard.

---

Un `Result` peut aussi être inspecté sans être déballé. `onFailure` exécute son bloc uniquement lorsque le résultat contient une exception, `onSuccess` uniquement lorsqu'il contient une valeur, et **tous deux rendent le même `Result`**, si bien que les appels peuvent être enchaînés :

```kotlin
runCatching { "abc".toInt() }
    .onFailure { println("could not read it") }
    .onSuccess { println("read $it") }
```
Dans le bloc, l'exception (ou la valeur) est disponible comme `it`, si bien que `it.message` est le texte de l'échec.

C'est la forme « journaliser et continuer » : signalez le problème là où il se produit, puis continuez, sans `return` prématuré et sans `var` définie depuis deux endroits.

---

L'endroit où se trouve le `try` décide de la quantité de travail qu'une seule valeur incorrecte détruit. Englobez la **boucle entière** et le premier échec abandonne le reste du lot ; englobez le **corps** et seul cet élément est perdu :

```kotlin
var total = 0
for (value in listOf("3", "x", "5")) {
    try {
        total += value.toInt()
    } catch (e: NumberFormatException) {
        // on ignore celle-ci
    }
}
println(total) // 8
```
Cela se marie naturellement avec une fonction de validation qui lève une exception : la fonction énonce une règle et refuse tout ce qui la viole, et la boucle décide qu'un refus ne coûte qu'un seul élément.
