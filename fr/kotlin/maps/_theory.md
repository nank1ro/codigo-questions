Une `Map` stocke des **paires clé-valeur** : chaque valeur est retrouvée par sa clé plutôt que par un index.
Les clés sont uniques au sein d'une map, tandis que les valeurs peuvent se répéter.

Vous créez une map en lecture seule avec `mapOf`, en associant chaque clé à sa valeur grâce à la fonction infixe `to` :
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals)
// prints {Italy=Rome, France=Paris}
```
Ici, `"Italy"` et `"France"` sont les clés, et `"Rome"` et `"Paris"` sont leurs valeurs.

---

Pour lire une valeur, vous indexez la map avec sa clé, en utilisant des crochets ou la fonction `get` :
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages["Alice"])    // 30
println(ages.get("Bob"))  // 25
```

Si la clé n'est pas présente, le résultat est `null`, donc le type de `ages["Alice"]` est `Int?`, et non `Int` :
```kotlin
println(ages["Zoe"]) // null
```

---

Lorsqu'une clé peut être absente, `getOrDefault` vous permet de choisir la valeur à utiliser à la place de `null` :
```kotlin
val ages = mapOf("Alice" to 30)
println(ages.getOrDefault("Alice", 0)) // 30
println(ages.getOrDefault("Zoe", 0))   // 0
```
Le premier argument est la clé, le second est la valeur par défaut retournée lorsque la clé n'est pas trouvée.

---

Une map créée avec `mapOf` est en lecture seule. Pour ajouter ou modifier des entrées, utilisez `mutableMapOf`, qui retourne une `MutableMap` :
```kotlin
val ages = mutableMapOf("Alice" to 30)
ages["Bob"] = 25   // adds a new entry
ages["Alice"] = 31 // updates the existing one
println(ages)
// prints {Alice=31, Bob=25}
```
L'affectation avec `map[key] = value` ajoute la paire lorsque la clé est nouvelle et remplace la valeur lorsque la clé existe déjà. Vous pouvez aussi appeler `ages.put("Bob", 25)`, qui fait la même chose.

---

`remove(key)` supprime une entrée d'une `MutableMap`. Si la clé n'est pas présente, rien ne se passe.
La propriété `size` indique le nombre d'entrées que contient la map :
```kotlin
val ages = mutableMapOf("Alice" to 30, "Bob" to 25)
ages.remove("Bob")
println(ages)      // {Alice=30}
println(ages.size) // 1
```

---

Pour vérifier si une clé existe, utilisez `containsKey` ou l'opérateur `in` ; pour vérifier si une valeur existe, utilisez `containsValue` :
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages.containsKey("Alice")) // true
println("Zoe" in ages)             // false
println(ages.containsValue(25))    // true
```

---

La propriété `keys` retourne toutes les clés d'une map sous forme de `Set`, et `values` retourne toutes les valeurs sous forme de collection :
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals.keys)   // [Italy, France]
println(capitals.values) // [Rome, Paris]
```
Les deux conservent l'ordre dans lequel les entrées ont été insérées.

---

Vous pouvez parcourir une map avec `for`, en déstructurant chaque entrée en sa clé et sa valeur :
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
for ((name, age) in ages) {
    println("$name is $age")
}
// prints
// Alice is 30
// Bob is 25
```
Les parenthèses `(name, age)` divisent chaque entrée en deux variables. Les entrées sont parcourues dans l'ordre d'insertion.
