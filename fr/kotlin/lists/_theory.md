Les listes sont un type de données que vous pouvez utiliser pour stocker une collection de différentes informations sous la forme d'une séquence dans une seule variable.
Une liste stocke plusieurs valeurs d'un ou plusieurs types et utilise des **index** pour distinguer ces valeurs.
Vous pouvez assigner des éléments à une liste avec une expression de la forme :
```kotlin
val listName = listOf<itemsType>(item1, item2)
```
`itemsType` représente le type des éléments à l'intérieur de la liste, par exemple, cela peut être `Int`, `String`, `Any`...

---

Une liste est une collection d'éléments avec un ordre spécifique. Il existe deux types de listes en Kotlin :

- `List` ne peut pas être modifiée après sa création.
- `MutableList` peut être modifiée après sa création, ce qui signifie que vous pouvez ajouter, supprimer ou mettre à jour ses éléments.

```kotlin
val numbers = listOf(1, 3, 5)
numbers.add(7) // [1]
```
__[1]__ lève une erreur car les `List`s sont _en lecture seule_.

Pour créer une liste modifiable, utilisez le mot-clé `mutableListOf`
```kotlin
val numbers = mutableListOf(1, 3, 5)
numbers.add(7)
println(numbers)
// affiche [1, 3, 5, 7]
```

---

Vous pouvez accéder à un élément individuel de la liste par son index.
Un index est comme une adresse qui identifie la place de l'élément dans la liste.
L'index apparaît directement après le nom de la liste, entre les crochets, comme ceci :
```kotlin
listName[index]
```

Les indices de liste commencent par `0`, et **non** par `1` ! Vous accédez au premier élément d'une liste comme ceci : `listName[0]` ou `listName.get(0)` ou même `listName.first()`.
Le deuxième élément d'une liste est à l'index __1__ : `listName[1]`.

---

L'index est en fait un décalage par rapport au premier élément. Par exemple, quand vous dites `list[2]`, vous ne demandez pas le deuxième élément de la liste, mais l'élément qui est à 2 positions de décalage à partir du premier élément. Donc `list[0]` est le premier élément (décalage zéro), `list[1]` est le deuxième élément (décalage de 1), `list[2]` est le troisième élément (décalage de 2), et ainsi de suite.

Un index de liste peut être utilisé à la fois pour accéder et pour assigner des valeurs.
Vous avez vu comment accéder à un index de liste comme ceci :
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel"]
// Affiche la valeur "Jeremiah"
println(names[0])
```
Voici comment fonctionne une attribution :
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel")
// Attribue la nouvelle valeur "Jordan"
names[0] = "Jordan"
// Affiche la valeur "Jordan"
println(names[0])
```

---

Tout comme les chaînes, les listes ont une **longueur** récupérée avec le getter `size`.
La longueur d'une liste est le nombre d'éléments qu'elle contient

---

Une autre opération de liste utile est la méthode `contains` pour découvrir si un élément donné se trouve dans la liste.
Par exemple, si vous avez une liste de noms, vous pouvez utiliser la méthode `contains` pour découvrir si un nom donné est présent dans la liste.
```kotlin
val names = listOf("Thomas", "Donald", "Scarlett")
println(names.contains("Scarlett"))
// affiche true
```

---

Une liste mutable n'a pas besoin d'avoir une longueur fixe.
Vous pouvez ajouter des éléments à la fin d'une liste à tout moment !
Pour ajouter un élément à une liste mutable, nous utilisons la fonction `add` ou le raccourci `+=` :
```kotlin
val letters = mutableListOf("a", "b")
letters.add("c")
println(letters)
// affiche [a, b, c]
```

---

Comme nous l'avons vu dans l'exemple précédent, nous pouvons ajouter des éléments un par un en utilisant la fonction `add`.
Mais si nous devons ajouter tous les éléments d'une autre liste à la fois, nous pouvons simplement utiliser la fonction `addAll`, ou le raccourci `+=` :
```kotlin
val letters = mutableListOf("a", "b")
val newLetters = listOf("c", "d", "e")
letters.addAll(newLetters)
println(letters)
// affiche [a, b, c, d, e]
```

---

Parfois, vous ne souhaitez accéder qu'à une partie d'une liste.
Considérez le code suivant :
```kotlin
val numbers = listOf(1, 2, 3, 4) // [1]
val slice = numbers.slice(1..2) // [2]
println(slice)
// affiche [2, 3]
```
__[1]__: d'abord, nous créons une liste _en lecture seule_ appelée `numbers`.
__[2]__: ensuite, nous extrayons une sous-section de la liste en utilisant la fonction `slice` et la stockons dans la liste slice.
Nous faisons cela en définissant les indices que nous voulons inclure dans la fonction `slice`.

En Kotlin, nous pouvons inclure le dernier index en utilisant `..`, mais nous pouvons aussi exclure le dernier index en utilisant `until`

---

Les éléments des listes peuvent être de n'importe quel type, si nous spécifions le type `Any` :
```kotlin
var listName: List<Any> = listOf("one", 2, true)
```
En fait, ci-dessus, nous avons, dans l'ordre, une `String`, un `Integer` et un `Boolean`.
Mais nous pouvons aussi avoir des listes avec des listes !

---

Parfois, vous devez rechercher un élément dans une liste.
En Kotlin, nous pouvons utiliser la méthode `indexOfFirst` :
```kotlin
val names = mutableListOf("Trevor", "Zac", "Glenn")
println(names.indexOfFirst { it == "Zac"})
// affiche 1
```

La méthode `indexOfFirst` prend une fonction __prédicat__ qui sera évaluée pour chaque élément de la liste jusqu'à ce qu'elle soit vraie, renvoyant l'_index_ de l'élément.
Le code ci-dessus affiche le premier index contenant la chaîne `"Zac"`, `1` dans ce cas.

Nous pouvons également insérer des éléments dans une liste modifiable à un index spécifique, en utilisant la méthode `add(index, element)` :
```kotlin
names.add(1, "Ali")
// affiche [Trevor, Ali, Zac, Glenn]
```
Le code ci-dessus insère `"Ali"` à l'index `1`, ce qui déplace tout, après cet index, vers le bas de 1

---

En Kotlin, nous pouvons boucler à travers une liste d'une manière très simple en utilisant les mots-clés `for..in` :
```kotlin
val numbers = listOf(1, 2, 3)
for (num in numbers) {
    println(num)
}
// affiche 1, 2, 3
```
Un nom de variable suit le mot-clé `for`, il sera assigné à la valeur de chaque élément de la liste à tour de rôle.
