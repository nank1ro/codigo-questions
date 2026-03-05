Les `Set`s sont un type de données que vous pouvez utiliser pour stocker une collection de différentes informations sous la forme d'une séquence dans une seule variable.
La différence principale avec les `List`s est qu'un `Set` n'autorise qu'un seul élément de chaque valeur.

Comme les `List`s, un `Set` stocke plusieurs valeurs d'un ou plusieurs types et utilise des **index** pour distinguer ces valeurs.
Vous pouvez assigner des éléments à un ensemble avec une expression de la forme :
```kotlin
val setName = setOf<itemsType>(item1, item2)
```
`itemsType` représente le type des éléments à l'intérieur du set, par exemple, cela peut être `Int`, `String`, `Any`...

---

Un `Set` est une collection d'éléments __uniques__ sans ordre spécifique.

```kotlin
val numbers = setOf(1, 1, 2) // [1]
println(numbers)
// affiche [1, 2]
```

À __[1]__ nous essayons de créer un ensemble avec le nombre __1__ présent deux fois mais comme vous pouvez le voir, chaque élément doit être unique et le deuxième __1__ est automatiquement rejeté.

---

Il existe deux types de `Set`s en Kotlin :

- `Set` ne peut pas être modifié après sa création.
- `MutableSet` peut être modifié après sa création, ce qui signifie que vous pouvez ajouter, supprimer ou mettre à jour ses éléments.

```kotlin
val numbers = setOf(1, 2, 3)
numbers.add(4) // [1]
```
__[1]__ lève une erreur car les `Set`s sont _en lecture seule_.

Pour créer un ensemble modifiable, utilisez le mot-clé `mutableSetOf`
```kotlin
val numbers = mutableSetOf(1, 2, 3)
numbers.add(4)
println(numbers)
// affiche [1, 2, 3, 4]
```

---

L'activité la plus courante du `Set` est de tester l'appartenance en utilisant `in` ou `contains()`

```kotlin
val numbers = setOf(1, 2, 3)
println(2 in numbers) // affiche true
println(numbers.contains(5)) // affiche false
```

Comme vous pouvez le voir ci-dessus, `in` et `contains` renvoient un `Bool` indiquant si l'élément transmis est présent dans l'ensemble

---

L'ordre des éléments dans un `Set` n'est pas important.
En fait, si vous essayez de comparer deux `Set`s avec le même élément mais dans un ordre différent, vous obtenez qu'ils sont égaux.

---

Sur les `Set`s, vous pouvez effectuer plusieurs opérations comme vérifier l'union, l'intersection, la différence et le sous-ensemble.

```kotlin
val firstNumbers = setOf(1, 2, 3)
val lastNumbers = setOf(3, 4, 5)
val union = firstNumbers.union(lastNumbers) // [1, 2, 3, 4, 5]
val intersection = firstNumbers intersect lastNumbers // [3]
val difference = firstNumbers subtract lastNumbers // [1, 2]
val subset = firstNumbers.containsAll(lastNumbers) // false
```

---

Pour convertir un `Set` en `List`, nous pouvons utiliser la fonction `toList()`
