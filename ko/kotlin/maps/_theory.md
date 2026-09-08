`Map`은 **키-값 쌍**을 저장합니다: 모든 값은 인덱스가 아니라 키로 조회됩니다.
map 안에서 키는 고유하지만, 값은 중복될 수 있습니다.

`mapOf`를 사용하면 읽기 전용 map을 만들 수 있으며, `to` 중위 함수로 각 키와 값을 짝지을 수 있습니다:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals)
// prints {Italy=Rome, France=Paris}
```
여기서 `"Italy"`와 `"France"`가 키이고, `"Rome"`과 `"Paris"`가 각각의 값입니다.

---

값을 읽으려면 대괄호나 `get` 함수를 사용해 키로 map을 인덱싱합니다:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages["Alice"])    // 30
println(ages.get("Bob"))  // 25
```

키가 존재하지 않으면 결과는 `null`이므로 `ages["Alice"]`의 타입은 `Int`가 아니라 `Int?`입니다:
```kotlin
println(ages["Zoe"]) // null
```

---

키가 없을 수도 있을 때, `getOrDefault`를 사용하면 `null` 대신 사용할 값을 선택할 수 있습니다:
```kotlin
val ages = mapOf("Alice" to 30)
println(ages.getOrDefault("Alice", 0)) // 30
println(ages.getOrDefault("Zoe", 0))   // 0
```
첫 번째 인자는 키이고, 두 번째 인자는 키를 찾지 못했을 때 반환되는 기본값입니다.

---

`mapOf`로 만든 map은 읽기 전용입니다. 항목을 추가하거나 변경하려면 `MutableMap`을 반환하는 `mutableMapOf`를 사용합니다:
```kotlin
val ages = mutableMapOf("Alice" to 30)
ages["Bob"] = 25   // adds a new entry
ages["Alice"] = 31 // updates the existing one
println(ages)
// prints {Alice=31, Bob=25}
```
`map[key] = value`로 대입하면 키가 새로운 경우 쌍이 추가되고, 키가 이미 존재하면 값이 교체됩니다. 같은 동작을 하는 `ages.put("Bob", 25)`를 호출할 수도 있습니다.

---

`remove(key)`는 `MutableMap`에서 항목을 삭제합니다. 키가 없으면 아무 일도 일어나지 않습니다.
`size` 프로퍼티는 map이 가진 항목의 개수를 알려줍니다:
```kotlin
val ages = mutableMapOf("Alice" to 30, "Bob" to 25)
ages.remove("Bob")
println(ages)      // {Alice=30}
println(ages.size) // 1
```

---

키가 존재하는지 확인하려면 `containsKey`나 `in` 연산자를, 값이 존재하는지 확인하려면 `containsValue`를 사용합니다:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
println(ages.containsKey("Alice")) // true
println("Zoe" in ages)             // false
println(ages.containsValue(25))    // true
```

---

`keys` 프로퍼티는 map의 모든 키를 `Set`으로 반환하고, `values`는 모든 값을 컬렉션으로 반환합니다:
```kotlin
val capitals = mapOf("Italy" to "Rome", "France" to "Paris")
println(capitals.keys)   // [Italy, France]
println(capitals.values) // [Rome, Paris]
```
둘 다 항목이 삽입된 순서를 유지합니다.

---

`for`로 map을 순회하며 각 항목을 키와 값으로 구조 분해할 수 있습니다:
```kotlin
val ages = mapOf("Alice" to 30, "Bob" to 25)
for ((name, age) in ages) {
    println("$name is $age")
}
// prints
// Alice is 30
// Bob is 25
```
괄호 `(name, age)`는 각 항목을 두 개의 변수로 나눕니다. 항목은 삽입된 순서대로 방문됩니다.
