Chaque valeur en Kotlin possède un **type**, qui indique au compilateur de quelles données il s'agit et ce que vous pouvez en faire.
Les types de base sont :
- `Int` : un nombre entier, comme `42` ou `-7`
- `Long` : un nombre entier qui peut être bien plus grand qu'un `Int`
- `Double` : un nombre avec une partie décimale, comme `3.14`
- `Float` : un nombre décimal qui utilise la moitié de la mémoire d'un `Double`, mais qui est moins précis
- `Char` : un caractère unique entre guillemets simples, comme `'a'`
- `Boolean` : soit `true`, soit `false`
- `String` : un morceau de texte entre guillemets doubles, comme `"Hello"`

Comme vous l'avez vu dans les leçons sur les variables, vous pouvez déclarer le type explicitement avec deux points après le nom :
```kotlin
val age: Int = 36
val name: String = "Ada"
```
Une valeur d'un type ne peut pas être stockée dans une variable d'un autre type : `val age: Int = "36"` est une erreur de compilation.

---

La plupart du temps, vous n'écrivez pas le type : Kotlin l'**infère** à partir de la valeur que vous affectez, en suivant quelques règles sur les littéraux :
- un nombre entier, comme `42`, est un `Int`
- un nombre avec une partie décimale, comme `3.14`, est un `Double`
- un texte entre guillemets doubles est un `String`
- un caractère entre guillemets simples est un `Char`
- `true` et `false` sont des `Boolean`
```kotlin
val count = 42     // Int
val price = 9.99   // Double
val name = "Ada"   // String
val grade = 'A'    // Char
val isOpen = true  // Boolean
```
Pour savoir ce que Kotlin a inféré, vous pouvez afficher le nom du type de n'importe quelle valeur avec `::class.simpleName` :
```kotlin
println(count::class.simpleName) // Int
println(price::class.simpleName) // Double
```
Un littéral décimal n'est jamais inféré comme `Float` : `val ratio = 0.5` est un `Double`.

---

Un `Int` peut contenir des nombres entiers jusqu'à environ deux milliards, plus précisément jusqu'à `Int.MAX_VALUE`, qui vaut `2147483647`.
Un littéral entier trop grand pour un `Int` est automatiquement inféré comme un `Long`, et vous pouvez forcer un `Long` pour n'importe quel littéral avec le suffixe `L` :
```kotlin
val big = 3000000000  // Long, too big for an Int
val small = 3L        // Long, thanks to the suffix
```
De la même manière, le suffixe `f` transforme un littéral décimal en `Float` : `val ratio = 0.5f`.
Les grands nombres sont difficiles à lire, donc Kotlin vous permet de placer des tirets bas `_` n'importe où entre les chiffres ; ils sont ignorés par le compilateur :
```kotlin
val population = 8_000_000_000L
val million = 1_000_000
println(million) // 1000000
```

---

Kotlin ne convertit jamais automatiquement entre les types de nombres lors d'une affectation, pas même d'un type plus petit vers un type plus grand : stocker un `Int` dans une variable `Long` ou `Double` est une erreur de compilation.
```kotlin
val count = 3
val total: Long = count      // error: Int is not a Long
val price: Double = count    // error: Int is not a Double
```
Chaque type de nombre possède des **fonctions de conversion** qui construisent une nouvelle valeur du type dont vous avez besoin : `toInt()`, `toLong()`, `toDouble()`, `toFloat()` et, pour obtenir du texte, `toString()`.
```kotlin
val total: Long = count.toLong()
val price: Double = count.toDouble() // 3.0
println(count.toString() + "!")      // 3!
```
Passer d'un décimal à un nombre entier **tronque** : `toInt()` supprime simplement la partie décimale, donc `3.99.toInt()` vaut `3` et `(-3.99).toInt()` vaut `-3`.

---

Ce sont les types des opérandes qui décident du fonctionnement de la division. Lorsque les deux sont des `Int`, l'opérateur `/` effectue une **division entière** : le résultat est un `Int` et le reste est jeté.
Lorsqu'au moins un opérande est un `Double`, `/` effectue une division à virgule flottante et conserve la partie décimale :
```kotlin
println(7 / 2)              // 3
println(7.0 / 2)            // 3.5
val slices = 7
println(slices.toDouble() / 2) // 3.5
```
Pour obtenir un résultat décimal à partir de deux variables `Int`, vous devez donc convertir au moins l'une d'elles **avant** de diviser : `(7 / 2).toDouble()` vaut `3.0`, car la division entière a déjà eu lieu.

---

Lorsqu'une fonction doit retourner un résultat décimal calculé à partir de nombres entiers, convertissez les opérandes en `Double` avant de diviser et déclarez le type de retour comme `Double` :
```kotlin
fun ratio(part: Int, total: Int): Double {
    return part.toDouble() / total
}
println(ratio(1, 4)) // 0.25
```
Rappelez-vous que `sum()` et `size` d'une `List<Int>` sont aussi des `Int`, elles ont donc besoin de la même conversion.

---

Chaque `Char` est stocké sous forme de nombre, son **code**. La propriété `code` donne le `Int` qui se cache derrière un caractère, et `toChar()` fait l'inverse, en transformant un `Int` en le `Char` portant ce code :
```kotlin
println('A'.code)        // 65
println(66.toChar())     // B
println(('A'.code + 2).toChar()) // C
```
Les lettres ont des codes consécutifs, donc ajouter au code fait avancer le long de l'alphabet.
Notez que le code de `'7'` est `55`, et non `7` : pour lire le chiffre que représente un `Char`, utilisez `digitToInt()`, qui retourne `7`.

---

Puisque le code d'un `Char` est un `Int`, vous pouvez faire des calculs avec et reconvertir le résultat en `Char`. C'est ainsi que vous vous déplacez le long de l'alphabet :
```kotlin
val next = ('a'.code + 1).toChar() // 'b'
```
Kotlin vous permet aussi d'ajouter directement un `Int` à un `Char` : `'a' + 1` vaut `'b'`, et la différence entre deux caractères `'d' - 'a'` est le `Int` `3`.

---

Le texte saisi par un utilisateur arrive toujours sous forme de `String`, même quand il ressemble à un nombre. Pour faire des calculs avec, vous devez l'**analyser** : `toInt()` transforme `"42"` en `Int` `42`, et `toDouble()` transforme `"3.5"` en `Double` `3.5`.
```kotlin
val typed = "42"
println(typed.toInt() + 1) // 43
```
Tous les textes ne sont pas des nombres : `"4x2".toInt()` lève une `NumberFormatException` et arrête le programme.
Les alternatives sûres `toIntOrNull()` et `toDoubleOrNull()` retournent `null` au lieu de lever une exception, donc, comme vous l'avez appris dans les leçons sur la nullabilité, vous pouvez fournir une valeur par défaut avec `?:` :
```kotlin
println("4x2".toIntOrNull())      // null
println("4x2".toIntOrNull() ?: 0) // 0
```

---

`toIntOrNull()` ne réussit que lorsque tout le texte est un nombre entier valide, avec un signe optionnel :
```kotlin
println("42".toIntOrNull())   // 42
println("-7".toIntOrNull())   // -7
println("3.5".toIntOrNull())  // null, not a whole number
println(" 42".toIntOrNull())  // null, spaces are not allowed
println("abc".toIntOrNull())  // null
```
Pour un texte décimal, utilisez `toDoubleOrNull()`, qui accepte `"3.5"` et retourne un `Double?` de la même manière.

---

Un `Int` a une taille fixe, il possède donc une plus petite et une plus grande valeur : `Int.MIN_VALUE` vaut `-2147483648` et `Int.MAX_VALUE` vaut `2147483647`.
Dépasser la limite ne provoque **pas** d'erreur : la valeur fait silencieusement le **tour** pour revenir à l'autre extrémité de la plage, un comportement appelé débordement.
```kotlin
println(Int.MAX_VALUE)     // 2147483647
println(Int.MAX_VALUE + 1) // -2147483648
```
Lorsqu'un résultat peut dépasser deux milliards, utilisez un `Long`, dont la limite `Long.MAX_VALUE` est d'environ neuf quintillions. N'oubliez pas de convertir avant l'opération : `Int.MAX_VALUE.toLong() + 1` vaut `2147483648`.

---

Un `Double` stocke les décimaux en binaire, donc certaines valeurs ne peuvent pas être représentées exactement et de petites erreurs apparaissent dans les derniers chiffres :
```kotlin
println(0.1 + 0.2) // 0.30000000000000004
```
Pour afficher un nombre fixe de décimales, utilisez `String.format` avec une chaîne de format : `"%.2f"` signifie « un nombre décimal avec 2 chiffres après la virgule ». Le résultat est un `String`, arrondi à ce nombre de chiffres :
```kotlin
println(String.format("%.2f", 0.1 + 0.2)) // 0.30
println(String.format("%.1f", 3.14159))   // 3.1
println(String.format("%.2f", 2.0))       // 2.00
```

---

`Any` est le type au sommet de la hiérarchie : chaque valeur Kotlin est un `Any`, donc une variable de type `Any` peut contenir un `Int`, un `String`, un `Boolean`, ou n'importe quoi d'autre.
Pour découvrir ce qu'elle contient réellement, vous utilisez l'opérateur `is`, qui retourne `true` lorsque la valeur a ce type :
```kotlin
val value: Any = 42
println(value is Int)    // true
println(value is String) // false
```
Une fois qu'une vérification a réussi, le compilateur effectue un **smart cast** de la valeur : à l'intérieur du `if` (ou de la branche du `when`) vous pouvez l'utiliser comme ce type, sans aucune conversion nécessaire :
```kotlin
if (value is Int) println(value + 1) // 43, value is an Int here
when (value) {
    is String -> println(value.length)
    is Boolean -> println(!value)
}
```
