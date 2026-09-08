Una `Map` memorizza **coppie chiave-valore**: ogni valore viene cercato tramite la sua chiave anziché tramite un indice.
Le chiavi sono uniche all'interno di una mappa, mentre i valori possono ripetersi.

Puoi creare una mappa di sola lettura con `mapOf`, abbinando ogni chiave al suo valore tramite la funzione infissa `to`:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals)
// prints {Italy=Rome, France=Paris}
```
Qui `"Italy"` e `"France"` sono le chiavi e `"Rome"` e `"Paris"` sono i loro valori.

---

Per leggere un valore, indicizzi la mappa con la sua chiave, usando le parentesi quadre oppure la funzione `get`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages["Alice"])    // 30
println(ages.get("Bob"))  // 25
```

Se la chiave non è presente il risultato è `null`, quindi il tipo di `ages["Alice"]` è `Int?`, non `Int`:
```kotlin
println(ages["Zoe"]) // null
```

---

Quando una chiave potrebbe mancare, `getOrDefault` ti permette di scegliere il valore da usare al posto di `null`:
```kotlin
val ages = mapOf("Alice" to 30)
println(ages.getOrDefault("Alice", 0)) // 30
println(ages.getOrDefault("Zoe", 0))   // 0
```
Il primo argomento è la chiave, il secondo è il valore predefinito restituito quando la chiave non viene trovata.

---

Una mappa creata con `mapOf` è di sola lettura. Per aggiungere o modificare elementi usa `mutableMapOf`, che restituisce una `MutableMap`:
```kotlin
val ages = mutableMapOf("Alice" to 30)
ages["Bob"] = 25   // adds a new entry
ages["Alice"] = 31 // updates the existing one
println(ages)
// prints {Alice=31, Bob=25}
```
L'assegnazione con `map[key] = value` aggiunge la coppia quando la chiave è nuova e sostituisce il valore quando la chiave esiste già. Puoi anche chiamare `ages.put("Bob", 25)`, che fa la stessa cosa.

---

`remove(key)` elimina un elemento da una `MutableMap`. Se la chiave non è presente non succede nulla.
La proprietà `size` indica quanti elementi contiene la mappa:
```kotlin
val ages = mutableMapOf("Alice" to 30, "Bob" to 25)
ages.remove("Bob")
println(ages)      // {Alice=30}
println(ages.size) // 1
```

---

Per verificare se una chiave esiste usa `containsKey` oppure l'operatore `in`; per verificare se un valore esiste usa `containsValue`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages.containsKey("Alice")) // true
println("Zoe" in ages)             // false
println(ages.containsValue(25))    // true
```

---

La proprietà `keys` restituisce tutte le chiavi di una mappa come `Set`, e `values` restituisce tutti i valori come collezione:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals.keys)   // [Italy, France]
println(capitals.values) // [Rome, Paris]
```
Entrambe mantengono l'ordine in cui gli elementi sono stati inseriti.

---

Puoi ciclare su una mappa con `for`, destrutturando ogni elemento nella sua chiave e nel suo valore:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
for ((name, age) in ages) {
    println("$name is $age")
}
// prints
// Alice is 30
// Bob is 25
```
Le parentesi `(name, age)` dividono ogni elemento in due variabili. Gli elementi vengono visitati nell'ordine di inserimento.
