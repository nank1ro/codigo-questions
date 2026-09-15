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
