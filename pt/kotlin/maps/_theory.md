Um `Map` armazena **pares chave-valor**: cada valor é procurado pela sua chave em vez de por um índice.
As chaves são únicas dentro de um map, enquanto os valores podem se repetir.

Você cria um map somente leitura com `mapOf`, associando cada chave ao seu valor usando a função infixa `to`:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals)
// imprime {Italy=Rome, France=Paris}
```
Aqui `"Italy"` e `"France"` são as chaves e `"Rome"` e `"Paris"` são seus valores.

---

Para ler um valor você indexa o map com sua chave, usando colchetes ou a função `get`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages["Alice"])    // 30
println(ages.get("Bob"))  // 25
```

Se a chave não estiver presente o resultado é `null`, então o tipo de `ages["Alice"]` é `Int?`, não `Int`:
```kotlin
println(ages["Zoe"]) // null
```

---

Quando uma chave pode estar ausente, `getOrDefault` permite escolher o valor a ser usado em vez de `null`:
```kotlin
val ages = mapOf("Alice" to 30)
println(ages.getOrDefault("Alice", 0)) // 30
println(ages.getOrDefault("Zoe", 0))   // 0
```
O primeiro argumento é a chave, o segundo é o valor padrão retornado quando a chave não é encontrada.

---

Um map criado com `mapOf` é somente leitura. Para adicionar ou alterar entradas use `mutableMapOf`, que retorna um `MutableMap`:
```kotlin
val ages = mutableMapOf("Alice" to 30)
ages["Bob"] = 25   // adiciona uma nova entrada
ages["Alice"] = 31 // atualiza a existente
println(ages)
// imprime {Alice=31, Bob=25}
```
Atribuir com `map[key] = value` adiciona o par quando a chave é nova e substitui o valor quando a chave já existe. Você também pode chamar `ages.put("Bob", 25)`, que faz o mesmo.

---

`remove(key)` exclui uma entrada de um `MutableMap`. Se a chave não estiver presente, nada acontece.
A propriedade `size` indica quantas entradas o map contém:
```kotlin
val ages = mutableMapOf("Alice" to 30, "Bob" to 25)
ages.remove("Bob")
println(ages)      // {Alice=30}
println(ages.size) // 1
```

---

Para verificar se uma chave existe use `containsKey` ou o operador `in`; para verificar se um valor existe use `containsValue`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages.containsKey("Alice")) // true
println("Zoe" in ages)             // false
println(ages.containsValue(25))    // true
```

---

A propriedade `keys` retorna todas as chaves de um map como um `Set`, e `values` retorna todos os valores como uma coleção:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals.keys)   // [Italy, France]
println(capitals.values) // [Rome, Paris]
```
Ambas mantêm a ordem em que as entradas foram inseridas.

---

Você pode percorrer um map com `for`, desestruturando cada entrada em sua chave e valor:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
for ((name, age) in ages) {
    println("$name is $age")
}
// imprime
// Alice is 30
// Bob is 25
```
Os parênteses `(name, age)` dividem cada entrada em duas variáveis. As entradas são percorridas na ordem de inserção.

---

Assim como as listas, os maps suportam `filter`. A lambda recebe cada entrada e você pode desestruturá-la em `(key, value)`; o resultado é um novo `Map` contendo apenas as entradas para as quais a lambda retorna `true`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25, "Zoe" to 40)
val adults = ages.filter { (name, age) -> age >= 30 }
println(adults) // {Alice=30, Zoe=40}
```
Também existem `filterKeys { }` e `filterValues { }` para quando a condição envolve apenas um dos lados da entrada.

---

`map` transforma cada entrada de um map em um novo elemento. Ao contrário de `filter`, o resultado é uma `List`, não um `Map`:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
val labels = ages.map { (name, age) -> "$name: $age" }
println(labels) // [Alice: 30, Bob: 25]
```
