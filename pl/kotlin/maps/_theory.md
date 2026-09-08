`Map` przechowuje **pary klucz-wartość**: każda wartość jest wyszukiwana za pomocą jej klucza, a nie indeksu.
Klucze są unikalne wewnątrz mapy, natomiast wartości mogą się powtarzać.

Mapę tylko do odczytu tworzysz za pomocą `mapOf`, łącząc każdy klucz z jego wartością za pomocą funkcji infiksowej `to`:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals)
// prints {Italy=Rome, France=Paris}
```
Tutaj `"Italy"` i `"France"` to klucze, a `"Rome"` i `"Paris"` to ich wartości.

---

Aby odczytać wartość, indeksujesz mapę jej kluczem, używając nawiasów kwadratowych lub funkcji `get`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages["Alice"])    // 30
println(ages.get("Bob"))  // 25
```

Jeśli klucz nie istnieje, wynikiem jest `null`, więc typ `ages["Alice"]` to `Int?`, a nie `Int`:
```kotlin
println(ages["Zoe"]) // null
```

---

Gdy klucz może nie istnieć, `getOrDefault` pozwala wybrać wartość używaną zamiast `null`:
```kotlin
val ages = mapOf("Alice" to 30)
println(ages.getOrDefault("Alice", 0)) // 30
println(ages.getOrDefault("Zoe", 0))   // 0
```
Pierwszy argument to klucz, drugi to wartość domyślna zwracana, gdy klucz nie zostanie znaleziony.

---

Mapa utworzona za pomocą `mapOf` jest tylko do odczytu. Aby dodać lub zmienić wpisy, użyj `mutableMapOf`, która zwraca `MutableMap`:
```kotlin
val ages = mutableMapOf("Alice" to 30)
ages["Bob"] = 25   // adds a new entry
ages["Alice"] = 31 // updates the existing one
println(ages)
// prints {Alice=31, Bob=25}
```
Przypisanie za pomocą `map[key] = value` dodaje parę, gdy klucz jest nowy, i zastępuje wartość, gdy klucz już istnieje. Możesz też wywołać `ages.put("Bob", 25)`, co robi to samo.

---

`remove(key)` usuwa wpis z `MutableMap`. Jeśli klucz nie istnieje, nic się nie dzieje.
Właściwość `size` mówi, ile wpisów zawiera mapa:
```kotlin
val ages = mutableMapOf("Alice" to 30, "Bob" to 25)
ages.remove("Bob")
println(ages)      // {Alice=30}
println(ages.size) // 1
```

---

Aby sprawdzić, czy klucz istnieje, użyj `containsKey` lub operatora `in`; aby sprawdzić, czy istnieje wartość, użyj `containsValue`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages.containsKey("Alice")) // true
println("Zoe" in ages)             // false
println(ages.containsValue(25))    // true
```

---

Właściwość `keys` zwraca wszystkie klucze mapy jako `Set`, a `values` zwraca wszystkie wartości jako kolekcję:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals.keys)   // [Italy, France]
println(capitals.values) // [Rome, Paris]
```
Obie zachowują kolejność, w jakiej wpisy zostały dodane.

---

Możesz iterować po mapie za pomocą `for`, rozkładając każdy wpis na klucz i wartość:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
for ((name, age) in ages) {
    println("$name is $age")
}
// prints
// Alice is 30
// Bob is 25
```
Nawiasy `(name, age)` dzielą każdy wpis na dwie zmienne. Wpisy są odwiedzane w kolejności wstawiania.
