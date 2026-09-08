`Map` 存储**键值对**：每个值都通过其键来查找，而不是通过索引。
在一个 map 中键是唯一的，而值可以重复。

你可以使用 `mapOf` 创建一个只读的 map，通过中缀函数 `to` 将每个键与其值配对：
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals)
// prints {Italy=Rome, France=Paris}
```
这里 `"Italy"` 和 `"France"` 是键，`"Rome"` 和 `"Paris"` 是它们的值。

---

要读取一个值，你可以使用方括号或 `get` 函数，通过键对 map 进行索引：
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages["Alice"])    // 30
println(ages.get("Bob"))  // 25
```

如果键不存在，结果为 `null`，因此 `ages["Alice"]` 的类型是 `Int?`，而不是 `Int`：
```kotlin
println(ages["Zoe"]) // null
```

---

当一个键可能不存在时，`getOrDefault` 让你选择用来代替 `null` 的值：
```kotlin
val ages = mapOf("Alice" to 30)
println(ages.getOrDefault("Alice", 0)) // 30
println(ages.getOrDefault("Zoe", 0))   // 0
```
第一个参数是键，第二个参数是找不到该键时返回的默认值。

---

用 `mapOf` 创建的 map 是只读的。要添加或修改条目，请使用返回 `MutableMap` 的 `mutableMapOf`：
```kotlin
val ages = mutableMapOf("Alice" to 30)
ages["Bob"] = 25   // adds a new entry
ages["Alice"] = 31 // updates the existing one
println(ages)
// prints {Alice=31, Bob=25}
```
使用 `map[key] = value` 赋值时，如果键是新的就会添加这个对，如果键已经存在就会替换其值。你也可以调用 `ages.put("Bob", 25)`，效果相同。

---

`remove(key)` 会从 `MutableMap` 中删除一个条目。如果键不存在，则什么都不会发生。
`size` 属性表示 map 中包含多少个条目：
```kotlin
val ages = mutableMapOf("Alice" to 30, "Bob" to 25)
ages.remove("Bob")
println(ages)      // {Alice=30}
println(ages.size) // 1
```

---

要检查某个键是否存在，可以使用 `containsKey` 或 `in` 运算符；要检查某个值是否存在，可以使用 `containsValue`：
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages.containsKey("Alice")) // true
println("Zoe" in ages)             // false
println(ages.containsValue(25))    // true
```

---

`keys` 属性以 `Set` 的形式返回 map 的所有键，`values` 则以集合的形式返回所有值：
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals.keys)   // [Italy, France]
println(capitals.values) // [Rome, Paris]
```
两者都保留了条目插入时的顺序。

---

你可以用 `for` 遍历一个 map，把每个条目解构为它的键和值：
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
for ((name, age) in ages) {
    println("$name is $age")
}
// prints
// Alice is 30
// Bob is 25
```
括号 `(name, age)` 把每个条目拆分成两个变量。条目按插入顺序被访问。
