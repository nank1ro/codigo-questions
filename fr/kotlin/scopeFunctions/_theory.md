Les **fonctions de portée** exécutent un bloc de code *dans le contexte d'un objet*. Elles n'ajoutent pas de nouvelles fonctionnalités au langage : elles rendent simplement le code qui travaille sur un seul objet plus court et plus facile à lire. Kotlin en compte cinq : `let`, `run`, `with`, `apply` et `also`.

Elles ne diffèrent que sur **deux** points : la façon dont l'objet est référencé dans le bloc, et ce que l'appel renvoie. Commençons par `let` : dans son bloc, l'objet s'appelle `it`, et l'appel retourne le **résultat de la dernière expression** du bloc.
```kotlin
val word = "kotlin"
val letters = word.let { it.length } // 6
println(letters)
```
Sans `let`, il faudrait une variable temporaire ; avec lui, l'objet reste disponible sous le nom court `it` tant que le bloc dure.

---

Comme `let` retourne la valeur de sa dernière expression, c'est un moyen pratique de **transformer une valeur en autre chose** sans nommer une variable intermédiaire :
```kotlin
val price = 12
val label = price.let { "$it EUR" }
println(label) // 12 EUR
```
Dans le bloc, vous pouvez utiliser `it` autant de fois que nécessaire :
```kotlin
println("kiwi".let { "${it.uppercase()} has ${it.length} letters" })
// KIWI has 4 letters
```

---

`let` devient vraiment utile après un appel sûr. `?.let { ... }` exécute le bloc **uniquement** lorsque la valeur n'est pas `null`, et dans le bloc `it` est une valeur non null, donc aucune vérification supplémentaire n'est nécessaire :
```kotlin
val email: String? = "ada@example.com"
email?.let { println("Sending to ${it.uppercase()}") }
```
Lorsque la valeur est `null`, l'expression entière vaut `null` et le bloc ne s'exécute jamais ; l'opérateur Elvis `?:` est donc le partenaire naturel pour fournir une valeur de repli :
```kotlin
fun label(city: String?): String {
    return city?.let { "City: $it" } ?: "No city"
}
```

---

Dans un bloc `let`, vous n'êtes pas obligé d'appeler l'objet `it` : vous pouvez donner un nom au paramètre de la lambda, ce qui garde le code lisible lorsque les blocs sont imbriqués ou lorsque `it` ne dirait rien d'utile.
```kotlin
val price: Int? = 12
println(price?.let { amount -> "$amount EUR" }) // 12 EUR
```
Le même nommage fonctionne pour toutes les fonctions de portée qui utilisent `it`, c'est-à-dire pour `let` et `also`.

---

`apply` avance sur les deux axes à la fois : dans son bloc, l'objet est le récepteur `this` (ses membres peuvent donc être utilisés **sans aucun préfixe**), et l'appel retourne **l'objet lui-même**, et non le résultat du bloc.

Cette combinaison fait de `apply` l'outil idéal pour **configurer** un objet juste au moment où vous le créez :
```kotlin
class Server {
    var host = "localhost"
    var port = 80
}

val server = Server().apply {
    host = "example.com"
    port = 8080
}
println("${server.host}:${server.port}") // example.com:8080
```
`host` et `port` dans le bloc sont `this.host` et `this.port` ; comme `apply` redonne le `Server` configuré, celui-ci peut être affecté immédiatement.

---

`apply` ne se limite pas aux objets que vous venez de créer : il fonctionne sur n'importe quel objet et, comme il redonne l'objet, vous pouvez utiliser l'expression entière partout où l'objet est attendu.
```kotlin
val box = Box()
box.apply { label = "tools" }        // modifie box et le renvoie
println(listOf(Box().apply { label = "nails" }).size) // 1
```
Le bloc est un bloc de code ordinaire, il peut donc contenir autant d'instructions que nécessaire.

---

`also` est l'image miroir de `apply` : l'objet est référencé comme `it`, et l'appel retourne **l'objet lui-même**. Comme le résultat du bloc est jeté, `also` sert aux **effets de bord** comme la journalisation ou la vérification, et il peut s'insérer au milieu d'une chaîne sans changer ce que la chaîne produit :
```kotlin
val total = listOf(1, 2, 3)
    .also { println("size: ${it.size}") } // size: 3
    .sum()
println(total) // 6
```
Lisez-le comme *« et fais aussi ceci avec lui »* : la valeur continue de circuler vers l'étape suivante sans être modifiée.

---

Lorsque le bloc a besoin de l'objet comme **argument** d'autre chose, `also` se lit mieux que `apply` : `it` peut être passé directement, tandis que `this` devrait être écrit explicitement.
```kotlin
val names = mutableListOf<String>()
val user = "ada".also { names.add(it) }
println(user)  // ada
println(names) // [ada]
```
La valeur de l'expression reste `"ada"` : `also` se contente de la regarder passer.

---

`run` est `let` avec l'autre façon de nommer l'objet : dans le bloc, l'objet est `this`, ses membres n'ont donc pas besoin de préfixe, et l'appel retourne le **résultat de la dernière expression**.

Il convient lorsque vous lisez plusieurs membres d'un même objet pour calculer une valeur :
```kotlin
class Rect(val w: Int, val h: Int)

val area = Rect(3, 4).run { w * h }
println(area) // 12
```
Comparez-le avec `apply`, qui utilise `this` exactement de la même manière mais rend l'objet au lieu du résultat du bloc.

---

`with` fait le même travail que `run`, mais il n'est **pas** une extension : l'objet est passé comme premier argument au lieu d'être le récepteur d'un appel avec point.
```kotlin
val text = with(StringBuilder()) {
    append("Hello")
    append(", world")
    toString()
}
println(text) // Hello, world
```
Dans le bloc, l'objet est `this` et l'appel retourne la dernière expression, exactement comme `run`. Préférez `with` lorsque vous avez déjà un objet non null et que vous voulez regrouper plusieurs appels sur lui ; préférez `run` lorsque l'objet sort d'une chaîne ou peut nécessiter un appel sûr (`obj?.run { ... }`).

---

Les cinq fonctions de portée sont maintenant sur la table, et chacune n'est qu'un point sur les deux axes :
- `let` - l'objet est `it`, retourne le résultat du bloc
- `run` - l'objet est `this`, retourne le résultat du bloc
- `with` - l'objet est `this` (passé comme argument), retourne le résultat du bloc
- `apply` - l'objet est `this`, retourne l'objet
- `also` - l'objet est `it`, retourne l'objet

Choisissez la ligne dont vous avez besoin : `it` se lit mieux lorsque vous passez l'objet à autre chose, `this` se lit mieux lorsque vous touchez à beaucoup de ses membres ; retournez le résultat du bloc lorsque vous voulez une nouvelle valeur, retournez l'objet lorsque vous voulez continuer à travailler avec.
