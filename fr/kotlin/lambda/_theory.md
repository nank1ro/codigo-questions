Une **lambda** est une petite fonction sans nom, écrite directement comme une expression entre accolades.
Les paramètres viennent d'abord, puis une flèche `->`, puis le corps :
```kotlin
val add = { a: Int, b: Int -> a + b }
```
Une lambda est une valeur comme une autre : vous pouvez la stocker dans une variable et l'appeler plus tard avec des parenthèses, exactement comme une fonction :
```kotlin
println(add(2, 3)) // 5
```
Une lambda sans paramètres n'a pas de flèche du tout : `val hello = { println("Hello!") }`.

---

Chaque lambda possède un **type fonction**, écrit comme les types des paramètres entre parenthèses, une flèche, puis le type de retour.
La lambda `{ a: Int, b: Int -> a + b }` a le type `(Int, Int) -> Int` : elle prend deux valeurs `Int` et retourne un `Int`.
Lorsque vous déclarez le type fonction sur la variable, les types des paramètres à l'intérieur de la lambda peuvent être omis car le compilateur les connaît déjà :
```kotlin
val add: (Int, Int) -> Int = { a, b -> a + b }
val greet: (String) -> Unit = { name -> println("Hi, $name") }
```
Une lambda qui ne retourne rien a le type de retour `Unit`.

---

Le corps d'une lambda peut s'étendre sur plusieurs lignes. Il n'y a pas de mot-clé `return` : la valeur de la **dernière expression** est ce que la lambda retourne.
```kotlin
val describe: (Int) -> String = { n ->
    val half = n / 2
    "half of $n is $half" // returned
}
println(describe(10)) // half of 10 is 5
```
Comme `if` est une expression en Kotlin, elle peut être la dernière ligne et décider du résultat :
```kotlin
val parity: (Int) -> String = { n -> if (n % 2 == 0) "even" else "odd" }
```

---

Lorsqu'une lambda a exactement **un** paramètre, vous pouvez ne pas le déclarer : Kotlin le nomme `it` pour vous.
```kotlin
// val double: (Int) -> Int = { n -> n * 2 }
val double: (Int) -> Int = { it * 2 } // same thing
```
`it` n'existe que lorsque le paramètre n'est pas déclaré explicitement, et uniquement pour les lambdas à un seul paramètre.
Il permet de garder compactes les lambdas courtes, mais pour des corps plus longs un vrai nom est plus clair.

---

Les lambdas sont surtout utilisées comme arguments d'autres fonctions. Les collections offrent de nombreuses fonctions qui prennent une lambda :
- `forEach` exécute la lambda une fois pour chaque élément
- `map` construit une nouvelle liste avec le résultat de la lambda pour chaque élément
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map({ it * 2 }) // [2, 4, 6]
```
Lorsque la lambda est le **dernier** argument, vous pouvez la sortir des parenthèses ; lorsqu'elle est le seul argument, les parenthèses peuvent être complètement omises. C'est ce qu'on appelle la syntaxe de la **lambda finale** (*trailing lambda*) et c'est la façon habituelle de l'écrire :
```kotlin
val doubled = numbers.map { it * 2 }
doubled.forEach { println(it) }
```

---

Une lambda qui retourne un `Boolean` est appelée un **prédicat**. Plusieurs fonctions de collection en prennent un :
- `filter` garde uniquement les éléments pour lesquels le prédicat est `true`
- `count` retourne le nombre d'éléments qui le satisfont
- `any` et `all` indiquent si certains ou tous les éléments le satisfont
```kotlin
val numbers = listOf(1, 2, 3, 4, 5, 6)
println(numbers.filter { it % 2 == 0 }) // [2, 4, 6]
println(numbers.count { it > 4 })        // 2
println(numbers.any { it > 5 })          // true
```
Les appels peuvent être **enchaînés** : chaque fonction retourne une nouvelle liste sur laquelle la suivante travaille.
```kotlin
println(numbers.filter { it % 2 == 0 }.map { it * 10 }) // [20, 40, 60]
```

---

Les lambdas pilotent aussi le tri et l'agrégation :
- `sortedBy` retourne une nouvelle liste ordonnée selon la valeur que la lambda calcule pour chaque élément ; `sortedByDescending` fait l'inverse
- `reduce` combine tous les éléments en une seule valeur : la lambda reçoit le résultat accumulé jusqu'ici et l'élément suivant
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })          // [fig, kiwi, banana]
println(words.sortedByDescending { it.length }) // [banana, kiwi, fig]

val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n })   // 10
```
`reduce` commence avec le premier élément comme `acc`, puis exécute la lambda pour chaque élément restant.

---

Avec `reduce`, la forme du résultat dépend de la lambda. Toute opération qui combine deux valeurs fonctionne : une somme, un produit, garder le plus grand des deux.
```kotlin
val numbers = listOf(3, 9, 4)
println(numbers.reduce { acc, n -> if (n > acc) n else acc }) // 9
```
Notez que `reduce` lève une exception sur une liste vide, car il n'y a pas de premier élément par lequel commencer.

---

Une lambda peut utiliser les variables déclarées autour d'elle, même après que le code environnant est passé à autre chose. Cela s'appelle une **closure** : la lambda *capture* les variables dont elle a besoin.
Contrairement à beaucoup d'autres langages, Kotlin permet à une lambda de **modifier** une variable `var` capturée :
```kotlin
var clicks = 0
val onClick = { clicks++ }
onClick()
onClick()
println(clicks) // 2
```
Chaque appel de `onClick` met à jour la même variable `clicks` que voit le code extérieur.

---

Puisqu'une lambda est une valeur, une fonction peut en **retourner** une. Le type de retour est un type fonction :
```kotlin
fun multiplier(factor: Int): (Int) -> Int {
    return { it * factor }
}
val triple = multiplier(3)
println(triple(5)) // 15
```
La lambda retournée capture `factor`, ainsi chaque appel de `multiplier` construit une fonction différente.
Les fonctions qui prennent ou retournent d'autres fonctions sont appelées des **fonctions d'ordre supérieur**.

---

Une lambda retournée peut capturer une variable `var` déclarée à l'intérieur de la fonction. Cette variable continue d'exister après que la fonction a retourné, et seule la lambda peut y accéder : c'est un état privé.
```kotlin
fun makeGreeter(): () -> String {
    var calls = 0
    return { calls++; "hello #$calls" }
}
val greeter = makeGreeter()
println(greeter()) // hello #1
println(greeter()) // hello #2
```
Chaque appel de `makeGreeter()` déclare un nouveau `calls`, ainsi deux greeters comptent indépendamment.

---

Vous pouvez écrire vos propres fonctions d'ordre supérieur : un paramètre avec un type fonction accepte n'importe quelle lambda de cette forme, et à l'intérieur de la fonction vous l'appelez comme une fonction ordinaire.
```kotlin
fun repeatTwice(text: String, transform: (String) -> String): String {
    return transform(transform(text))
}
println(repeatTwice("a", { it + "!" })) // a!!
println(repeatTwice("a") { it + "!" })  // same, with a trailing lambda
```
Placer le paramètre fonction en **dernière** position est ce qui rend la syntaxe de la lambda finale disponible pour les appelants.

---

Lorsque la fonction dont vous avez besoin existe déjà, il n'est pas nécessaire de l'envelopper dans une lambda : une **référence de fonction** `::name` transforme une fonction nommée en une valeur avec le type fonction correspondant.
```kotlin
fun isEven(n: Int) = n % 2 == 0
val numbers = listOf(1, 2, 3, 4)
println(numbers.filter { isEven(it) }) // [2, 4]
println(numbers.filter(::isEven))      // [2, 4], same thing
```
Les fonctions membres sont référencées à travers leur type, comme `String::uppercase` :
```kotlin
println(listOf("a", "b").map(String::uppercase)) // [A, B]
```

---

Une **fonction anonyme** est une fonction déclarée avec `fun` mais sans nom. C'est une autre façon de créer une valeur fonction :
```kotlin
val square = fun(x: Int): Int {
    return x * x
}
println(square(4)) // 16
```
Différemment d'une lambda, elle peut déclarer son type de retour explicitement et elle utilise `return` pour produire la valeur.
Les fonctions anonymes et les lambdas sont interchangeables : toutes deux peuvent être passées à `map`, `filter` ou à toute fonction qui prend un type fonction.

---

Les fonctions d'ordre supérieur peuvent à la fois prendre et retourner des fonctions. Un exemple classique est la **composition** : construire une nouvelle fonction qui exécute une fonction et envoie son résultat dans une autre.
```kotlin
fun andThen(first: (Int) -> Int, second: (Int) -> Int): (Int) -> Int {
    return { n -> second(first(n)) }
}
val addOneThenDouble = andThen({ it + 1 }, { it * 2 })
println(addOneThenDouble(3)) // 8
```
La lambda retournée capture à la fois `first` et `second`, ainsi elle continue de fonctionner longtemps après que `andThen` a retourné.

---

Certaines fonctions prennent une **lambda avec récepteur** : à l'intérieur de la lambda, `this` est un objet spécifique, ainsi vous pouvez appeler ses membres directement sans le nommer.
`buildString` est un exemple courant : à l'intérieur de sa lambda, `this` est un `StringBuilder`, ainsi `append` peut être appelée comme si c'était une fonction locale :
```kotlin
val text = buildString {
    append("Hello")
    append(", ")
    append("world")
}
println(text) // Hello, world
```
`buildString` retourne la chaîne finale. C'est une alternative pratique à la concaténation avec `+` dans une boucle.
