Un `Map` almacena **pares clave-valor**: cada valor se busca mediante su clave en lugar de por un índice.
Las claves son únicas dentro de un mapa, mientras que los valores pueden repetirse.

Creas un mapa de solo lectura con `mapOf`, emparejando cada clave con su valor mediante la función infija `to`:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals)
// imprime {Italy=Rome, France=Paris}
```
Aquí `"Italy"` y `"France"` son las claves y `"Rome"` y `"Paris"` son sus valores.

---

Para leer un valor, indexas el mapa con su clave, usando corchetes o la función `get`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages["Alice"])    // 30
println(ages.get("Bob"))  // 25
```

Si la clave no está presente, el resultado es `null`, por lo que el tipo de `ages["Alice"]` es `Int?`, no `Int`:
```kotlin
println(ages["Zoe"]) // null
```

---

Cuando una clave podría estar ausente, `getOrDefault` te permite elegir el valor que se usará en lugar de `null`:
```kotlin
val ages = mapOf("Alice" to 30)
println(ages.getOrDefault("Alice", 0)) // 30
println(ages.getOrDefault("Zoe", 0))   // 0
```
El primer argumento es la clave, el segundo es el valor por defecto devuelto cuando la clave no se encuentra.

---

Un mapa creado con `mapOf` es de solo lectura. Para añadir o cambiar entradas usa `mutableMapOf`, que devuelve un `MutableMap`:
```kotlin
val ages = mutableMapOf("Alice" to 30)
ages["Bob"] = 25   // añade una nueva entrada
ages["Alice"] = 31 // actualiza la existente
println(ages)
// imprime {Alice=31, Bob=25}
```
Asignar con `map[key] = value` añade el par cuando la clave es nueva y reemplaza el valor cuando la clave ya existe. También puedes llamar a `ages.put("Bob", 25)`, que hace lo mismo.

---

`remove(key)` elimina una entrada de un `MutableMap`. Si la clave no está presente, no sucede nada.
La propiedad `size` indica cuántas entradas contiene el mapa:
```kotlin
val ages = mutableMapOf("Alice" to 30, "Bob" to 25)
ages.remove("Bob")
println(ages)      // {Alice=30}
println(ages.size) // 1
```

---

Para comprobar si una clave existe usa `containsKey` o el operador `in`; para comprobar si un valor existe usa `containsValue`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages.containsKey("Alice")) // true
println("Zoe" in ages)             // false
println(ages.containsValue(25))    // true
```

---

La propiedad `keys` devuelve todas las claves de un mapa como un `Set`, y `values` devuelve todos los valores como una colección:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals.keys)   // [Italy, France]
println(capitals.values) // [Rome, Paris]
```
Ambas mantienen el orden en que se insertaron las entradas.

---

Puedes recorrer un mapa con `for`, desestructurando cada entrada en su clave y su valor:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
for ((name, age) in ages) {
    println("$name is $age")
}
// imprime
// Alice is 30
// Bob is 25
```
Los paréntesis `(name, age)` dividen cada entrada en dos variables. Las entradas se visitan en el orden de inserción.

---

Al igual que las listas, los mapas admiten `filter`. La lambda recibe cada entrada y puedes desestructurarla en `(key, value)`; el resultado es un nuevo `Map` con solo las entradas para las que la lambda devuelve `true`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25, "Zoe" to 40)
val adults = ages.filter { (name, age) -> age >= 30 }
println(adults) // {Alice=30, Zoe=40}
```
También existen `filterKeys { }` y `filterValues { }` cuando la condición solo involucra un lado de la entrada.

---

`map` transforma cada entrada de un mapa en un nuevo elemento. A diferencia de `filter`, el resultado es una `List`, no un `Map`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
val labels = ages.map { (name, age) -> "$name: $age" }
println(labels) // [Alice: 30, Bob: 25]
```
