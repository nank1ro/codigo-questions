Une **méthode d'ordre supérieur** est une méthode qui prend une fonction en argument. Les collections Kotlin en offrent beaucoup, et la fonction que vous passez est généralement une **lambda** : une petite fonction anonyme écrite entre accolades.
`map` est la plus courante : elle appelle la lambda sur chaque élément et renvoie une **nouvelle liste** avec les résultats, en laissant l'originale intacte :
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map { it * 2 }
println(doubled) // [2, 4, 6]
println(numbers) // [1, 2, 3]
```
Quand la lambda a un seul paramètre, vous n'avez pas besoin de le déclarer : Kotlin le nomme `it`. La lambda s'écrit après le nom de la méthode, en dehors des parenthèses, qui peuvent être omises quand la lambda est le seul argument. C'est la syntaxe **trailing lambda** et elle est utilisée dans tous les exercices de ce sujet.

---

`filter` prend une lambda qui renvoie un `Boolean`, appelée **prédicat**, et renvoie une nouvelle liste contenant uniquement les éléments pour lesquels le prédicat vaut `true` :
```kotlin
val numbers = listOf(4, -2, 7, 0)
println(numbers.filter { it > 0 }) // [4, 7]
```
Au lieu de `it`, vous pouvez donner un nom au paramètre, suivi d'une flèche `->`. Un paramètre nommé rend les longues lambdas plus lisibles, et il est obligatoire quand une lambda est imbriquée dans une autre, car le `it` intérieur masque l'élément extérieur :
```kotlin
val minLength = 4
val words = listOf("fig", "banana", "kiwi")
println(words.filter { word -> word.length >= minLength }) // [banana, kiwi]
```

---

`forEach` exécute la lambda une fois pour chaque élément et ne renvoie rien. C'est l'alternative d'ordre supérieur à la boucle `for`, et elle sert aux effets de bord comme l'affichage :
```kotlin
listOf("a", "b").forEach { println(it) }
```
`forEachIndexed` vous donne aussi la position de chaque élément. Sa lambda a **deux** paramètres, ils doivent donc être nommés : `it` n'existe que pour les lambdas à exactement un paramètre.
```kotlin
listOf("a", "b").forEachIndexed { index, letter ->
    println("$index: $letter") // 0: a, puis 1: b
}
```

---

`reduce` combine tous les éléments en une seule valeur. Sa lambda prend deux paramètres : l'**accumulateur** (le résultat obtenu jusque-là) et l'élément suivant. Elle démarre avec le premier élément comme accumulateur et exécute la lambda pour chaque élément restant :
```kotlin
val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n }) // 10
```
`reduce` lève une exception sur une liste vide, car il n'y a pas de premier élément pour démarrer. `fold` corrige cela : vous passez la **valeur initiale** de l'accumulateur en argument, et la lambda s'exécute pour chaque élément, y compris le premier :
```kotlin
println(numbers.fold(0) { acc, n -> acc + n })   // 10
println(listOf<Int>().fold(0) { acc, n -> acc + n }) // 0
```
Avec `fold`, l'accumulateur peut même avoir un type différent de celui des éléments, par exemple pour construire une `String` à partir d'une liste de nombres.

---

Certaines méthodes d'ordre supérieur répondent à une question sur la collection au lieu d'en construire une nouvelle. Elles prennent toutes un prédicat :
- `any` renvoie `true` si **au moins un** élément le satisfait
- `all` renvoie `true` si **chaque** élément le satisfait
- `none` renvoie `true` si **aucun** élément ne le satisfait
- `count` renvoie **combien** d'éléments le satisfont
```kotlin
val numbers = listOf(1, 2, 3)
println(numbers.any { it > 2 })   // true
println(numbers.all { it > 2 })   // false
println(numbers.none { it > 2 })  // false
println(numbers.count { it > 1 }) // 2
```
Sur une liste vide, `any` renvoie `false`, tandis que `all` et `none` renvoient `true` : aucun élément ne vient enfreindre la règle.

---

Les méthodes d'agrégation transforment toute une collection en une seule valeur :
- `sum()` additionne une liste de nombres, tandis que `sumOf` additionne la valeur que la lambda calcule pour chaque élément
- `maxByOrNull` et `minByOrNull` renvoient l'**élément** pour lequel la lambda donne la valeur la plus grande ou la plus petite, ou `null` sur une liste vide
```kotlin
val words = listOf("fig", "banana", "kiwi")
println(words.sumOf { it.length })      // 13
println(words.minByOrNull { it.length }) // fig
println(listOf(1, 2, 3).sum())           // 6
```
Notez la différence avec `maxOf { it.length }`, qui renvoie la plus grande **valeur** (`6`) au lieu de l'élément qui l'a produite.

---

`sortedBy` renvoie une nouvelle liste triée selon la valeur que la lambda calcule pour chaque élément, de la plus petite à la plus grande. `sortedByDescending` trie de la plus grande à la plus petite. Quand ce sont les éléments eux-mêmes que vous voulez comparer, `sorted()` et `sortedDescending()` n'ont pas besoin de lambda :
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })            // [fig, kiwi, banana]
println(words.sortedByDescending { it.length })  // [banana, kiwi, fig]
println(words.sorted())                          // [banana, fig, kiwi]
```
Le tri est **stable** : les éléments ayant la même clé conservent leur ordre relatif d'origine. La liste d'origine n'est jamais modifiée.

---

`take(n)` renvoie une nouvelle liste avec les `n` premiers éléments, et `drop(n)` renvoie une nouvelle liste **sans** les `n` premiers éléments. Aucune des deux ne prend de lambda, mais elles sont souvent chaînées après une méthode qui en prend une :
```kotlin
val numbers = listOf(5, 3, 8, 1)
println(numbers.take(2))                    // [5, 3]
println(numbers.drop(2))                    // [8, 1]
println(numbers.sortedDescending().take(2)) // [8, 5]
```
`takeWhile` et `dropWhile` sont les versions avec un prédicat : elles prennent ou écartent les éléments depuis le début **tant que** le prédicat vaut `true`, et s'arrêtent au premier élément qui ne le satisfait pas :
```kotlin
println(numbers.takeWhile { it > 2 }) // [5, 3, 8]
```

---

`groupBy` répartit une collection dans une `Map` : la lambda calcule la **clé** de chaque élément, et chaque clé est associée à la liste des éléments qui l'ont produite, dans leur ordre d'origine :
```kotlin
val words = listOf("fig", "kiwi", "pear")
val byLength = words.groupBy { it.length }
println(byLength)    // {3=[fig], 4=[kiwi, pear]}
println(byLength[4]) // [kiwi, pear]
```
Le résultat a le type `Map<K, List<T>>`, où `K` est le type renvoyé par la lambda et `T` le type des éléments. Les clés apparaissent dans l'ordre où elles sont rencontrées pour la première fois.

---

Quand la lambda renvoie une **liste** pour chaque élément, `map` produit une liste de listes. `flatMap` fait la même chose mais réunit ensuite toutes ces listes en une seule liste plate :
```kotlin
val numbers = listOf(1, 2)
println(numbers.map { listOf(it, -it) })     // [[1, -1], [2, -2]]
println(numbers.flatMap { listOf(it, -it) }) // [1, -1, 2, -2]
```
L'ordre est conservé : toutes les valeurs produites par le premier élément viennent d'abord, puis celles du deuxième, et ainsi de suite. Si vous avez déjà une liste de listes, `flatten()` les réunit sans lambda.

---

`zip` associe les éléments de deux listes position par position. Sans lambda, elle renvoie une liste de valeurs `Pair`, dont les moitiés se lisent avec `.first` et `.second` ; avec une lambda, les deux éléments de chaque position lui sont passés et les résultats sont rassemblés dans une liste :
```kotlin
val names = listOf("Ann", "Bob")
val ages = listOf(31, 25)
println(names.zip(ages))                            // [(Ann, 31), (Bob, 25)]
println(names.zip(ages) { name, age -> "$name:$age" }) // [Ann:31, Bob:25]
```
Le résultat est aussi long que la **plus courte** des deux listes : les éléments en trop de la plus longue sont ignorés.

---

La forme de la lambda doit correspondre à ce que la méthode attend :
- les méthodes qui travaillent sur un élément à la fois (`map`, `filter`, `sortedBy`, `groupBy`...) prennent une lambda à **un paramètre**, où `it` est disponible
- `reduce`, `fold`, `forEachIndexed` et `zip` avec une lambda passent **deux** valeurs, les paramètres doivent donc être nommés explicitement avec `a, b ->`
```kotlin
val numbers = listOf(1, 2, 3)
numbers.map { it * 2 }                  // ok : un paramètre, it est disponible
numbers.reduce { acc, n -> acc + n }    // ok : deux paramètres, nommés
numbers.reduce { it + 1 }               // erreur : it n'existe pas avec deux paramètres
```
Nommer les paramètres est toujours autorisé, même avec un seul : `numbers.map { n -> n * 2 }`.

---

Les méthodes d'ordre supérieur peuvent être **chaînées** : chacune renvoie une nouvelle collection sur laquelle travaille la suivante, si bien qu'un calcul entier se lit comme un pipeline de gauche à droite :
```kotlin
val words = listOf("kiwi", "fig", "banana", "date")
println(words.filter { it.length == 4 }.map { it.uppercase() }.sorted()) // [DATE, KIWI]
```
Les maps ont aussi des méthodes d'ordre supérieur. `mapValues` conserve les clés et remplace chaque valeur par le résultat de la lambda, qui reçoit l'**entrée** avec `.key` et `.value` :
```kotlin
val byLength = words.groupBy { it.length }      // {4=[kiwi, date], 3=[fig], 6=[banana]}
println(byLength.mapValues { it.value.size })   // {4=2, 3=1, 6=1}
```

---

Dans une chaîne, le type de `it` change à chaque étape : après `filter` sur une `List<String>` vous avez toujours des chaînes de caractères, mais après `map { it.length }` vous avez une `List<Int>`, donc la lambda suivante voit des nombres.
```kotlin
val words = listOf("kiwi", "fig")
println(words.map { it.length }.filter { it > 3 }) // [4]
```
Chaque étape renvoie une **nouvelle** liste et ne touche jamais à la précédente, une chaîne peut donc être découpée en valeurs intermédiaires nommées sans changer le résultat.

---

Une lambda peut contenir un autre appel d'ordre supérieur. À l'intérieur de la lambda interne, `it` désigne l'élément **interne** et masque l'externe : nommez donc explicitement le paramètre externe pour garder les deux accessibles :
```kotlin
val sales = listOf("north" to 120, "south" to 80, "north" to 30)
val byRegion = sales.groupBy { it.first }
val totals = byRegion.mapValues { entry -> entry.value.sumOf { it.second } }
println(totals) // {north=150, south=80}
```
`"north" to 120` crée un `Pair`. Ici, la lambda externe travaille sur une entrée de map, tandis que l'interne travaille sur les paires de la liste de cette entrée.

---

Une `Map` peut être traitée comme une liste d'entrées : `filter` et `map` fonctionnent directement sur la map et reçoivent chaque entrée avec `.key` et `.value`. `filter` sur une map renvoie une map, tandis que `map` renvoie une liste. Les méthodes de tri comme `sortedBy` ne sont pas définies sur une map : passez d'abord par `scores.entries`, qui est une collection des entrées :
```kotlin
val scores = mapOf("Ann" to 90, "Bob" to 72)
println(scores.filter { it.value > 80 })              // {Ann=90}
println(scores.entries.sortedBy { it.value }.map { it.key }) // [Bob, Ann]
```
`scores.entries` est l'ensemble de toutes les entrées ; `scores.keys` et `scores.values` n'en donnent qu'un seul côté.
