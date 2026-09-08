Un **tableau** stocke un nombre fixe de valeurs du même type sous un seul nom de variable.
Vous en créez un avec `arrayOf`, lisez un élément avec des crochets et un **index** commençant à `0`, et obtenez le nombre d'éléments avec `size` :
```kotlin
val colors = arrayOf("red", "green", "blue")
println(colors[0])   // red
println(colors.size) // 3
```
Le dernier élément se trouve à l'index `size - 1`.

---

`arrayOf(1, 2, 3)` crée un `Array<Int>` où chaque élément est un objet boxé.
Pour les types primitifs, Kotlin propose des types dédiés et plus efficaces comme `IntArray`, `DoubleArray` et `BooleanArray` :
```kotlin
val a = intArrayOf(1, 2, 3)   // IntArray
val b = doubleArrayOf(1.5, 2.5) // DoubleArray
```
Vous pouvez aussi construire un tableau d'une taille donnée avec une lambda d'**initialisation** qui reçoit chaque index, ou un `IntArray` rempli de zéros :
```kotlin
val doubles = Array(3) { i -> i * 2 } // [0, 2, 4]
val zeros = IntArray(3)               // [0, 0, 0]
val evens = IntArray(4) { it * 2 }    // [0, 2, 4, 6]
```

---

Chaque tableau possède deux propriétés pratiques pour travailler avec les index :
- `indices` est la plage des index valides, de `0` au dernier
- `lastIndex` est l'index du dernier élément, c'est-à-dire `size - 1`
```kotlin
val letters = arrayOf("x", "y")
println(letters.lastIndex) // 1
for (i in letters.indices) {
    println(letters[i])
}
// prints x, then y
```

---

Même lorsqu'un tableau est déclaré avec `val`, ses **éléments** peuvent être remplacés en assignant à un index :
```kotlin
val nums = intArrayOf(1, 2, 3)
nums[0] = 10 // nums is now [10, 2, 3]
```
Pour visiter chaque élément, vous pouvez utiliser une boucle `for` ou `forEach` :
```kotlin
for (n in nums) {
    println(n)
}
nums.forEach { println(it) }
```
Notez que `n` et `it` sont des copies en lecture seule des valeurs et ne peuvent pas être réassignées, donc pour modifier des éléments vous avez besoin de leur index.

---

Pour vérifier si un tableau contient une valeur, utilisez `in` ou `contains`, tous deux retournent un `Boolean`.
`indexOf` retourne l'index de la première occurrence, ou `-1` quand la valeur n'est pas présente :
```kotlin
val nums = intArrayOf(4, 8, 15)
println(8 in nums)          // true
println(nums.contains(3))   // false
println(nums.indexOf(15))   // 2
println(nums.indexOf(16))   // -1
```

---

Afficher un tableau directement ne montre pas ses éléments, cela affiche quelque chose comme `[Ljava.lang.String;@1b6d3586`.
Utilisez `joinToString` pour construire une chaîne lisible, avec éventuellement un séparateur personnalisé (celui par défaut est `", "`), ou `contentToString` pour obtenir les éléments entre crochets :
```kotlin
val nums = intArrayOf(1, 2, 3)
println(nums.joinToString())      // 1, 2, 3
println(nums.joinToString("-"))   // 1-2-3
println(nums.contentToString())   // [1, 2, 3]
```

---

Les tableaux peuvent être triés **sur place** ou copiés dans une nouvelle collection triée :
- `sort()` et `sortDescending()` réorganisent le tableau lui-même et ne retournent rien
- `reverse()` inverse l'ordre du tableau lui-même
- `sorted()`, `sortedDescending()` et `reversed()` laissent le tableau inchangé et retournent une nouvelle `List`
```kotlin
val nums = intArrayOf(3, 1, 2)
nums.sort()                 // nums is now [1, 2, 3]
println(nums.reversed())    // [3, 2, 1], nums is still [1, 2, 3]
```

---

Les tableaux numériques disposent de fonctions d'agrégation :
```kotlin
val nums = intArrayOf(3, 9, 1)
println(nums.sum())     // 13
println(nums.max())     // 9
println(nums.min())     // 1
println(nums.average()) // 4.333333333333333
println(nums.count())   // 3
```
`max()` et `min()` lèvent une exception sur un tableau vide, utilisez `maxOrNull()` et `minOrNull()` quand le tableau peut être vide.

---

La principale différence entre un tableau et une `MutableList` est qu'un tableau a une **taille fixe** : une fois créé, vous pouvez remplacer ses éléments mais jamais en ajouter ou en retirer, il n'existe pas de fonction `add`.
Des expressions comme `nums + 4` ne font pas grandir `nums`, elles construisent un tout nouveau tableau :
```kotlin
val nums = arrayOf(1, 2, 3)
nums[0] = 9              // ok, nums is [9, 2, 3]
val bigger = nums + 4    // new array [9, 2, 3, 4], nums still has 3 elements
```
Préférez une `MutableList` quand le nombre d'éléments change au fil du temps, et un tableau quand il est connu à l'avance ou quand vous avez besoin des performances des types primitifs.

---

Les tableaux prennent en charge les mêmes fonctions de transformation que les listes. `filter` conserve les éléments correspondant à une condition et `map` transforme chaque élément.
Les deux retournent une nouvelle `List`, pas un tableau :
```kotlin
val nums = intArrayOf(1, 2, 3)
val odds = nums.filter { it % 2 == 1 } // List [1, 3]
val tripled = nums.map { it * 3 }      // List [3, 6, 9]
println(tripled)                       // [3, 6, 9]
```
Comme le résultat est une liste, l'afficher directement montre ses éléments.

---

Quand vous avez besoin à la fois de l'index et de la valeur pendant une boucle, utilisez `withIndex()` et déstructurez chaque paire, ou `forEachIndexed` :
```kotlin
val pets = arrayOf("cat", "dog")
for ((i, pet) in pets.withIndex()) {
    println("$i -> $pet")
}
pets.forEachIndexed { i, pet -> println("$i -> $pet") }
// both print 0 -> cat, then 1 -> dog
```

---

Les tableaux et les listes se convertissent facilement entre eux :
- `toList()` et `toMutableList()` copient un tableau dans une liste
- `toTypedArray()` copie une liste dans un `Array<T>`
- `toIntArray()` copie une liste de `Int` dans un `IntArray`
```kotlin
val arr = arrayOf("a", "b")
val list = arr.toMutableList() // MutableList [a, b]
list.add("c")
val back = list.toTypedArray() // Array [a, b, c]
val nums = listOf(1, 2).toIntArray() // IntArray [1, 2]
```
Chaque conversion crée une **copie**, donc modifier le résultat n'affecte pas l'original.

---

Contrairement aux listes, deux tableaux avec les mêmes éléments ne sont **pas** égaux avec `==` : les tableaux sont comparés par référence, donc `==` vaut `true` uniquement pour le tout même objet tableau.
Pour comparer le contenu, utilisez `contentEquals` :
```kotlin
val a = intArrayOf(1, 2, 3)
val b = intArrayOf(1, 2, 3)
println(a == b)              // false
println(a.contentEquals(b))  // true
println(listOf(1, 2) == listOf(1, 2)) // true, lists compare their elements
```

---

Comme les tableaux ont une taille fixe, prendre une partie de l'un d'eux signifie créer un nouveau tableau :
- `copyOf()` copie le tableau entier, `copyOf(n)` copie les `n` premiers éléments
- `copyOfRange(from, to)` copie les éléments de l'index `from` jusqu'à `to` **exclu**
- `sliceArray(range)` copie les éléments aux index de la plage, les deux bornes incluses
```kotlin
val nums = intArrayOf(10, 20, 30, 40)
println(nums.copyOfRange(1, 3).contentToString()) // [20, 30]
println(nums.sliceArray(0..1).contentToString())  // [10, 20]
```
