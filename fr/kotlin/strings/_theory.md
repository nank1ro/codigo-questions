Un `String` est une suite de caractères écrite entre guillemets doubles.
La propriété `length` indique combien de caractères contient une chaîne, espaces compris :
```kotlin
val greeting = "Hello world"
println(greeting.length) // 11
println("".length)       // 0
```

---

Chaque caractère d'une chaîne possède un **index**, à partir de `0` pour le premier.
Vous lisez un caractère avec des crochets ou la fonction `get`, et le résultat est un `Char` :
```kotlin
val word = "Kotlin"
println(word[0])     // K
println(word.get(1)) // o
```
Le dernier caractère se trouve à l'index `length - 1`. Les fonctions `first()` et `last()` sont des raccourcis pratiques :
```kotlin
println(word[word.length - 1]) // n
println(word.first())          // K
println(word.last())           // n
```

---

`uppercase()` retourne une copie de la chaîne avec toutes les lettres en majuscules, `lowercase()` fait l'inverse.
La chaîne d'origine n'est pas modifiée :
```kotlin
val name = "Kotlin"
println(name.uppercase()) // KOTLIN
println(name.lowercase()) // kotlin
println(name)             // Kotlin
```

---

Pour vérifier si une chaîne contient un morceau de texte, vous utilisez `contains`, `startsWith` et `endsWith`. Elles retournent toutes un `Boolean` :
```kotlin
val file = "photo.png"
println(file.contains("oto"))   // true
println(file.startsWith("ph"))  // true
println(file.endsWith(".jpg"))  // false
```
La vérification est sensible à la casse, sauf si vous passez `ignoreCase = true` :
```kotlin
println("Hello".contains("hello"))                    // false
println("Hello".contains("hello", ignoreCase = true)) // true
```

---

`indexOf` retourne l'index où un morceau de texte apparaît **pour la première fois**, ou `-1` s'il n'apparaît pas du tout.
`lastIndexOf` cherche à partir de la fin à la place :
```kotlin
val text = "hello"
println(text.indexOf("l"))     // 2
println(text.lastIndexOf("l")) // 3
println(text.indexOf("z"))     // -1
```

---

`substring` extrait une partie d'une chaîne. Avec deux arguments, elle prend les caractères depuis l'index de début jusqu'à l'index de fin, **sans l'inclure**.
Avec un seul argument, elle prend tout depuis cet index jusqu'à la fin :
```kotlin
val text = "Kotlin"
println(text.substring(0, 3)) // Kot
println(text.substring(3))    // lin
```
Combiner `indexOf` et `substring` permet de découper une chaîne autour d'un marqueur :
```kotlin
val email = "ann@mail.com"
println(email.substring(email.indexOf("@") + 1)) // mail.com
```

---

`split` découpe une chaîne en une `List` de morceaux autour d'un séparateur, tandis que `joinToString` fait l'inverse : elle assemble les éléments d'une collection en une seule chaîne avec le séparateur de votre choix :
```kotlin
val csv = "a,b,c"
val parts = csv.split(",")
println(parts)                  // [a, b, c]
println(parts.joinToString("/")) // a/b/c
```

---

Comme `split` retourne une `List`, vous pouvez parcourir ses éléments comme n'importe quelle autre liste :
```kotlin
for (part in "a-b".split("-")) {
    println(part)
}
// affiche a, puis b
```

---

La saisie utilisateur contient souvent des espaces en trop. `trim()` retourne la chaîne sans les espaces au début et à la fin, `trimStart()` et `trimEnd()` les suppriment d'un seul côté :
```kotlin
val raw = "  hello  "
println(raw.trim())      // "hello"
println(raw.trimStart()) // "hello  "
println(raw.trimEnd())   // "  hello"
```
`isEmpty()` vaut `true` pour `""`, tandis que `isBlank()` vaut aussi `true` pour les chaînes composées uniquement d'espaces :
```kotlin
println("   ".isEmpty()) // false
println("   ".isBlank()) // true
```

---

`replace(old, new)` retourne une copie de la chaîne où **chaque** occurrence de `old` est remplacée par `new` :
```kotlin
val text = "a-b-c"
println(text.replace("-", "+")) // a+b+c
println(text)                   // a-b-c
```

---

`repeat(n)` retourne la chaîne concaténée `n` fois :
```kotlin
println("ab".repeat(3)) // ababab
```
`padStart(width, char)` ajoute `char` au début jusqu'à ce que la chaîne atteigne `width` caractères ; `padEnd` les ajoute à la fin.
Si la chaîne est déjà assez longue, elle est retournée inchangée :
```kotlin
println("7".padStart(3, '0'))   // 007
println("hi".padEnd(5, '.'))    // hi...
println("1234".padStart(2, '0')) // 1234
```
Les nombres ne sont pas des chaînes : appelez d'abord `toString()`, comme dans `42.toString().padStart(4, '0')`.

---

Deux chaînes sont égales quand elles contiennent les mêmes caractères dans le même ordre. En Kotlin, `==` compare le **contenu** des chaînes, c'est donc la manière normale de les comparer.
`equals` fait la même chose, mais accepte aussi `ignoreCase = true` pour ignorer la différence entre majuscules et minuscules :
```kotlin
println("hello" == "hello")                          // true
println("Hello" == "hello")                          // false
println("Hello".equals("hello", ignoreCase = true))  // true
```
`===` vérifie si deux variables pointent vers exactement le même objet en mémoire, ce qui n'est presque jamais ce que vous voulez avec des chaînes.

---

`reversed()` retourne la chaîne avec ses caractères dans l'ordre inverse :
```kotlin
println("stressed".reversed()) // desserts
```
Un mot qui se lit de la même façon dans les deux sens, comme `"level"`, s'appelle un **palindrome**.

---

Les chaînes sont **immuables** : une fois créées, elles ne changent jamais. Toutes les fonctions vues jusqu'ici, comme `uppercase()` ou `replace()`, retournent une **nouvelle** chaîne et laissent l'originale intacte.
Pour conserver le résultat, vous devez le stocker, par exemple en réaffectant une `var` :
```kotlin
var name = "kotlin"
name.uppercase()        // le résultat est jeté
println(name)           // kotlin
name = name.uppercase() // le résultat est stocké
println(name)           // KOTLIN
```

---

Construire une longue chaîne morceau par morceau avec `+` crée une nouvelle chaîne à chaque étape. Un `StringBuilder` est un tampon de texte mutable conçu pour ce travail : `append` ajoute du texte à la fin (et retourne le builder, ce qui permet d'enchaîner les appels) et `toString()` donne la `String` finale :
```kotlin
val sb = StringBuilder()
sb.append("Hello")
sb.append(", ").append("world")
println(sb.toString()) // Hello, world
```
`append` accepte des chaînes, des caractères et des nombres.
