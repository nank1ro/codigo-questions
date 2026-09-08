A `Map` stores **key-value pairs**: every value is looked up by its key instead of by an index.
Keys are unique inside a map, while values can repeat.

You create a read-only map with `mapOf`, pairing each key with its value using the `to` infix function:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals)
// prints {Italy=Rome, France=Paris}
```
Here `"Italy"` and `"France"` are the keys and `"Rome"` and `"Paris"` are their values.

---

To read a value you index the map with its key, using square brackets or the `get` function:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages["Alice"])    // 30
println(ages.get("Bob"))  // 25
```

If the key is not present the result is `null`, so the type of `ages["Alice"]` is `Int?`, not `Int`:
```kotlin
println(ages["Zoe"]) // null
```

---

When a key might be missing, `getOrDefault` lets you choose the value to use instead of `null`:
```kotlin
val ages = mapOf("Alice" to 30)
println(ages.getOrDefault("Alice", 0)) // 30
println(ages.getOrDefault("Zoe", 0))   // 0
```
The first argument is the key, the second is the default value returned when the key is not found.

---

A map created with `mapOf` is read-only. To add or change entries use `mutableMapOf`, which returns a `MutableMap`:
```kotlin
val ages = mutableMapOf("Alice" to 30)
ages["Bob"] = 25   // adds a new entry
ages["Alice"] = 31 // updates the existing one
println(ages)
// prints {Alice=31, Bob=25}
```
Assigning with `map[key] = value` adds the pair when the key is new and replaces the value when the key already exists. You can also call `ages.put("Bob", 25)`, which does the same.

---

`remove(key)` deletes an entry from a `MutableMap`. If the key is not present nothing happens.
The `size` property tells how many entries the map holds:
```kotlin
val ages = mutableMapOf("Alice" to 30, "Bob" to 25)
ages.remove("Bob")
println(ages)      // {Alice=30}
println(ages.size) // 1
```

---

To check whether a key exists use `containsKey` or the `in` operator; to check whether a value exists use `containsValue`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages.containsKey("Alice")) // true
println("Zoe" in ages)             // false
println(ages.containsValue(25))    // true
```

---

The `keys` property returns all the keys of a map as a `Set`, and `values` returns all the values as a collection:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals.keys)   // [Italy, France]
println(capitals.values) // [Rome, Paris]
```
Both keep the order in which the entries were inserted.

---

You can loop over a map with `for`, destructuring each entry into its key and value:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
for ((name, age) in ages) {
    println("$name is $age")
}
// prints
// Alice is 30
// Bob is 25
```
The parentheses `(name, age)` split every entry into two variables. Entries are visited in insertion order.
