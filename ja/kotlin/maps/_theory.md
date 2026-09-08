`Map`は**キーと値のペア**を格納します。すべての値はインデックスではなくキーによって検索されます。
マップの中でキーは一意ですが、値は重複することがあります。

`mapOf`を使うと読み取り専用のマップを作成でき、`to`中置関数で各キーとその値を組み合わせます：
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals)
// prints {Italy=Rome, France=Paris}
```
ここで`"Italy"`と`"France"`がキーで、`"Rome"`と`"Paris"`がそれぞれの値です。

---

値を読み取るには、角括弧または`get`関数を使ってキーでマップにインデックスアクセスします：
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages["Alice"])    // 30
println(ages.get("Bob"))  // 25
```

キーが存在しない場合、結果は`null`になるため、`ages["Alice"]`の型は`Int`ではなく`Int?`です：
```kotlin
println(ages["Zoe"]) // null
```

---

キーが存在しない可能性があるとき、`getOrDefault`を使うと`null`の代わりに使う値を選べます：
```kotlin
val ages = mapOf("Alice" to 30)
println(ages.getOrDefault("Alice", 0)) // 30
println(ages.getOrDefault("Zoe", 0))   // 0
```
最初の引数がキーで、2番目の引数はキーが見つからないときに返されるデフォルト値です。

---

`mapOf`で作成したマップは読み取り専用です。エントリを追加または変更するには`mutableMapOf`を使います。これは`MutableMap`を返します：
```kotlin
val ages = mutableMapOf("Alice" to 30)
ages["Bob"] = 25   // adds a new entry
ages["Alice"] = 31 // updates the existing one
println(ages)
// prints {Alice=31, Bob=25}
```
`map[key] = value`で代入すると、キーが新しい場合はペアが追加され、キーが既に存在する場合は値が置き換えられます。同じことをする`ages.put("Bob", 25)`を呼び出すこともできます。

---

`remove(key)`は`MutableMap`からエントリを削除します。キーが存在しない場合は何も起こりません。
`size`プロパティはマップが保持するエントリ数を示します：
```kotlin
val ages = mutableMapOf("Alice" to 30, "Bob" to 25)
ages.remove("Bob")
println(ages)      // {Alice=30}
println(ages.size) // 1
```

---

キーが存在するかを確認するには`containsKey`または`in`演算子を、値が存在するかを確認するには`containsValue`を使います：
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages.containsKey("Alice")) // true
println("Zoe" in ages)             // false
println(ages.containsValue(25))    // true
```

---

`keys`プロパティはマップのすべてのキーを`Set`として返し、`values`はすべての値をコレクションとして返します：
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals.keys)   // [Italy, France]
println(capitals.values) // [Rome, Paris]
```
どちらもエントリが挿入された順序を保持します。

---

`for`を使ってマップをループし、各エントリをキーと値に分解代入できます：
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
for ((name, age) in ages) {
    println("$name is $age")
}
// prints
// Alice is 30
// Bob is 25
```
括弧`(name, age)`は各エントリを2つの変数に分割します。エントリは挿入順に処理されます。
