`Map` хранит **пары ключ-значение**: каждое значение ищется по его ключу, а не по индексу.
Ключи уникальны внутри map, тогда как значения могут повторяться.

Вы создаёте map только для чтения с помощью `mapOf`, связывая каждый ключ с его значением с помощью инфиксной функции `to`:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals)
// prints {Italy=Rome, France=Paris}
```
Здесь `"Italy"` и `"France"` — это ключи, а `"Rome"` и `"Paris"` — их значения.

---

Чтобы прочитать значение, вы индексируете map его ключом, используя квадратные скобки или функцию `get`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages["Alice"])    // 30
println(ages.get("Bob"))  // 25
```

Если ключ отсутствует, результатом будет `null`, поэтому тип `ages["Alice"]` — это `Int?`, а не `Int`:
```kotlin
println(ages["Zoe"]) // null
```

---

Когда ключ может отсутствовать, `getOrDefault` позволяет выбрать значение, используемое вместо `null`:
```kotlin
val ages = mapOf("Alice" to 30)
println(ages.getOrDefault("Alice", 0)) // 30
println(ages.getOrDefault("Zoe", 0))   // 0
```
Первый аргумент — это ключ, второй — значение по умолчанию, возвращаемое, если ключ не найден.

---

Map, созданный с помощью `mapOf`, доступен только для чтения. Чтобы добавлять или изменять записи, используйте `mutableMapOf`, который возвращает `MutableMap`:
```kotlin
val ages = mutableMapOf("Alice" to 30)
ages["Bob"] = 25   // adds a new entry
ages["Alice"] = 31 // updates the existing one
println(ages)
// prints {Alice=31, Bob=25}
```
Присваивание с помощью `map[key] = value` добавляет пару, если ключ новый, и заменяет значение, если ключ уже существует. Вы также можете вызвать `ages.put("Bob", 25)`, что делает то же самое.

---

`remove(key)` удаляет запись из `MutableMap`. Если ключ отсутствует, ничего не происходит.
Свойство `size` показывает, сколько записей содержит map:
```kotlin
val ages = mutableMapOf("Alice" to 30, "Bob" to 25)
ages.remove("Bob")
println(ages)      // {Alice=30}
println(ages.size) // 1
```

---

Чтобы проверить, существует ли ключ, используйте `containsKey` или оператор `in`; чтобы проверить, существует ли значение, используйте `containsValue`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages.containsKey("Alice")) // true
println("Zoe" in ages)             // false
println(ages.containsValue(25))    // true
```

---

Свойство `keys` возвращает все ключи map в виде `Set`, а `values` возвращает все значения в виде коллекции:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals.keys)   // [Italy, France]
println(capitals.values) // [Rome, Paris]
```
Оба сохраняют порядок, в котором были добавлены записи.

---

Вы можете перебирать map с помощью `for`, деструктурируя каждую запись на ключ и значение:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
for ((name, age) in ages) {
    println("$name is $age")
}
// prints
// Alice is 30
// Bob is 25
```
Скобки `(name, age)` разбивают каждую запись на две переменные. Записи посещаются в порядке вставки.
