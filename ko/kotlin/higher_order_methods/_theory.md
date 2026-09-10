**고차 메서드**는 함수를 인자로 받는 메서드입니다. Kotlin 컬렉션은 이런 메서드를 많이 제공하며, 전달하는 함수는 보통 **람다**, 즉 중괄호 사이에 작성하는 작은 익명 함수입니다.
`map`이 가장 흔한 예입니다. 모든 요소에 대해 람다를 호출하고 그 결과를 담은 **새 리스트**를 반환하며, 원본은 그대로 둡니다:
```kotlin
val numbers = listOf(1, 2, 3)
val doubled = numbers.map { it * 2 }
println(doubled) // [2, 4, 6]
println(numbers) // [1, 2, 3]
```
람다에 매개변수가 하나뿐이면 선언할 필요가 없습니다. Kotlin이 그것을 `it`이라고 부릅니다. 람다는 메서드 이름 뒤, 괄호 바깥에 쓰며, 람다가 유일한 인자일 때는 괄호를 생략할 수 있습니다. 이것이 **trailing lambda** 문법이고, 이 주제의 모든 연습에서 사용합니다.

---

`filter`는 `Boolean`을 반환하는 람다, 즉 **술어**를 받아 술어가 `true`인 요소만 담은 새 리스트를 반환합니다:
```kotlin
val numbers = listOf(4, -2, 7, 0)
println(numbers.filter { it > 0 }) // [4, 7]
```
`it` 대신 매개변수에 이름을 붙이고 화살표 `->`를 이어 쓸 수도 있습니다. 이름 붙인 매개변수는 긴 람다를 읽기 쉽게 만들고, 람다가 다른 람다 안에 중첩될 때는 반드시 필요합니다. 안쪽의 `it`이 바깥 요소를 가리기 때문입니다:
```kotlin
val minLength = 4
val words = listOf("fig", "banana", "kiwi")
println(words.filter { word -> word.length >= minLength }) // [banana, kiwi]
```

---

`forEach`는 각 요소마다 람다를 한 번씩 실행하고 아무것도 반환하지 않습니다. `for` 루프의 고차 메서드 버전이며, 출력 같은 부수 효과에 사용합니다:
```kotlin
listOf("a", "b").forEach { println(it) }
```
`forEachIndexed`는 각 요소의 위치도 함께 줍니다. 이 람다는 매개변수가 **두 개**이므로 반드시 이름을 붙여야 합니다. `it`은 매개변수가 정확히 하나인 람다에만 존재하기 때문입니다.
```kotlin
listOf("a", "b").forEachIndexed { index, letter ->
    println("$index: $letter") // 0: a, 그다음 1: b
}
```

---

`reduce`는 모든 요소를 하나의 값으로 합칩니다. 이 람다는 두 매개변수, 즉 **누산기**(지금까지의 결과)와 다음 요소를 받습니다. 첫 번째 요소를 누산기로 삼아 시작하고, 남은 모든 요소에 대해 람다를 실행합니다:
```kotlin
val numbers = listOf(1, 2, 3, 4)
println(numbers.reduce { acc, n -> acc + n }) // 10
```
`reduce`는 빈 리스트에서 예외를 던집니다. 시작할 첫 번째 요소가 없기 때문입니다. `fold`가 이를 해결합니다. 누산기의 **초기값**을 인자로 전달하면 첫 요소를 포함한 모든 요소에 대해 람다가 실행됩니다:
```kotlin
println(numbers.fold(0) { acc, n -> acc + n })   // 10
println(listOf<Int>().fold(0) { acc, n -> acc + n }) // 0
```
`fold`에서는 누산기가 요소와 다른 타입이어도 됩니다. 예를 들어 숫자 리스트로 `String`을 만들 수 있습니다.

---

일부 고차 메서드는 새 컬렉션을 만드는 대신 컬렉션에 대한 질문에 답합니다. 모두 술어를 받습니다:
- `any`는 **적어도 하나의** 요소가 술어를 만족하면 `true`를 반환합니다
- `all`은 **모든** 요소가 술어를 만족하면 `true`를 반환합니다
- `none`은 **어떤** 요소도 술어를 만족하지 않으면 `true`를 반환합니다
- `count`는 술어를 만족하는 요소가 **몇 개인지** 반환합니다
```kotlin
val numbers = listOf(1, 2, 3)
println(numbers.any { it > 2 })   // true
println(numbers.all { it > 2 })   // false
println(numbers.none { it > 2 })  // false
println(numbers.count { it > 1 }) // 2
```
빈 리스트에서 `any`는 `false`를 반환하고, `all`과 `none`은 `true`를 반환합니다. 규칙을 깨는 요소가 하나도 없기 때문입니다.

---

집계 메서드는 컬렉션 전체를 하나의 값으로 바꿉니다:
- `sum()`은 숫자 리스트를 더하고, `sumOf`는 람다가 각 요소에 대해 계산한 값을 더합니다
- `maxByOrNull`과 `minByOrNull`은 람다가 가장 큰 값 또는 가장 작은 값을 주는 **요소**를 반환하며, 빈 리스트에서는 `null`을 반환합니다
```kotlin
val words = listOf("fig", "banana", "kiwi")
println(words.sumOf { it.length })      // 13
println(words.minByOrNull { it.length }) // fig
println(listOf(1, 2, 3).sum())           // 6
```
`maxOf { it.length }`와의 차이에 주의하세요. 이쪽은 그 값을 만들어낸 요소가 아니라 가장 큰 **값**(`6`)을 반환합니다.

---

`sortedBy`는 람다가 각 요소에 대해 계산한 값을 기준으로 작은 것부터 정렬한 새 리스트를 반환합니다. `sortedByDescending`은 큰 것부터 정렬합니다. 비교하려는 것이 요소 자체라면 `sorted()`와 `sortedDescending()`은 람다가 필요 없습니다:
```kotlin
val words = listOf("kiwi", "fig", "banana")
println(words.sortedBy { it.length })            // [fig, kiwi, banana]
println(words.sortedByDescending { it.length })  // [banana, kiwi, fig]
println(words.sorted())                          // [banana, fig, kiwi]
```
정렬은 **안정적**입니다. 키가 같은 요소들은 원래의 상대 순서를 유지합니다. 원본 리스트는 절대 수정되지 않습니다.

---

`take(n)`은 처음 `n`개의 요소를 담은 새 리스트를 반환하고, `drop(n)`은 처음 `n`개의 요소를 **제외한** 새 리스트를 반환합니다. 둘 다 람다를 받지 않지만, 람다를 받는 메서드 뒤에 이어 붙이는 경우가 많습니다:
```kotlin
val numbers = listOf(5, 3, 8, 1)
println(numbers.take(2))                    // [5, 3]
println(numbers.drop(2))                    // [8, 1]
println(numbers.sortedDescending().take(2)) // [8, 5]
```
`takeWhile`과 `dropWhile`은 술어를 받는 버전입니다. 술어가 `true`인 **동안** 앞에서부터 요소를 가져오거나 버리고, 술어를 만족하지 않는 첫 번째 요소에서 멈춥니다:
```kotlin
println(numbers.takeWhile { it > 2 }) // [5, 3, 8]
```

---

`groupBy`는 컬렉션을 `Map`으로 나눕니다. 람다가 각 요소의 **키**를 계산하고, 각 키에는 그 키를 만들어낸 요소들의 리스트가 원래 순서대로 연결됩니다:
```kotlin
val words = listOf("fig", "kiwi", "pear")
val byLength = words.groupBy { it.length }
println(byLength)    // {3=[fig], 4=[kiwi, pear]}
println(byLength[4]) // [kiwi, pear]
```
결과의 타입은 `Map<K, List<T>>`이며, `K`는 람다가 반환하는 타입이고 `T`는 요소의 타입입니다. 키는 처음 만난 순서대로 나타납니다.

---

람다가 각 요소마다 **리스트**를 반환하면 `map`은 리스트의 리스트를 만듭니다. `flatMap`은 같은 일을 한 뒤 그 리스트들을 하나의 평평한 리스트로 합칩니다:
```kotlin
val numbers = listOf(1, 2)
println(numbers.map { listOf(it, -it) })     // [[1, -1], [2, -2]]
println(numbers.flatMap { listOf(it, -it) }) // [1, -1, 2, -2]
```
순서는 유지됩니다. 첫 번째 요소가 만들어낸 값들이 먼저 오고, 그다음 두 번째 요소의 값들이 오는 식입니다. 이미 리스트의 리스트를 가지고 있다면 `flatten()`이 람다 없이 합쳐줍니다.

---

`zip`은 두 리스트의 요소를 위치별로 짝짓습니다. 람다가 없으면 `Pair` 값들의 리스트를 반환하며, 각 절반은 `.first`와 `.second`로 읽습니다. 람다를 주면 각 위치의 두 요소가 람다로 전달되고 그 결과가 리스트에 모입니다:
```kotlin
val names = listOf("Ann", "Bob")
val ages = listOf(31, 25)
println(names.zip(ages))                            // [(Ann, 31), (Bob, 25)]
println(names.zip(ages) { name, age -> "$name:$age" }) // [Ann:31, Bob:25]
```
결과의 길이는 두 리스트 중 **더 짧은** 쪽에 맞춰집니다. 더 긴 쪽의 남는 요소는 무시됩니다.

---

람다의 형태는 메서드가 기대하는 것과 맞아야 합니다:
- 한 번에 하나의 요소를 다루는 메서드(`map`, `filter`, `sortedBy`, `groupBy`...)는 **매개변수 하나**짜리 람다를 받고, 거기서는 `it`을 쓸 수 있습니다
- `reduce`, `fold`, `forEachIndexed`, 그리고 람다를 받는 `zip`은 **두** 값을 전달하므로 `a, b ->`처럼 매개변수에 명시적으로 이름을 붙여야 합니다
```kotlin
val numbers = listOf(1, 2, 3)
numbers.map { it * 2 }                  // ok: 매개변수 하나, it 사용 가능
numbers.reduce { acc, n -> acc + n }    // ok: 매개변수 두 개, 이름 붙임
numbers.reduce { it + 1 }               // 오류: 매개변수가 두 개면 it은 존재하지 않음
```
매개변수에 이름을 붙이는 것은 하나뿐일 때도 언제나 허용됩니다: `numbers.map { n -> n * 2 }`.

---

고차 메서드는 **연결**할 수 있습니다. 각각이 새 컬렉션을 반환하고 다음 메서드가 그것을 다루므로, 계산 전체가 왼쪽에서 오른쪽으로 흐르는 파이프라인처럼 읽힙니다:
```kotlin
val words = listOf("kiwi", "fig", "banana", "date")
println(words.filter { it.length == 4 }.map { it.uppercase() }.sorted()) // [DATE, KIWI]
```
맵에도 고차 메서드가 있습니다. `mapValues`는 키를 그대로 두고 각 값을 람다의 결과로 바꿉니다. 이 람다는 `.key`와 `.value`를 가진 **엔트리**를 받습니다:
```kotlin
val byLength = words.groupBy { it.length }      // {4=[kiwi, date], 3=[fig], 6=[banana]}
println(byLength.mapValues { it.value.size })   // {4=2, 3=1, 6=1}
```

---

체인 안에서 `it`의 타입은 단계마다 바뀝니다. `List<String>`에 `filter`를 적용한 뒤에는 여전히 문자열이지만, `map { it.length }` 뒤에는 `List<Int>`가 되므로 다음 람다는 숫자를 봅니다.
```kotlin
val words = listOf("kiwi", "fig")
println(words.map { it.length }.filter { it > 3 }) // [4]
```
모든 단계는 **새** 리스트를 반환하고 이전 리스트는 결코 건드리지 않으므로, 체인을 이름 붙인 중간 값들로 나누어도 결과는 달라지지 않습니다.

---

람다 안에 또 다른 고차 메서드 호출을 넣을 수 있습니다. 안쪽 람다에서 `it`은 **안쪽** 요소를 가리키며 바깥 요소를 가리므로, 둘 다 사용할 수 있도록 바깥 매개변수에는 명시적으로 이름을 붙이세요:
```kotlin
val sales = listOf("north" to 120, "south" to 80, "north" to 30)
val byRegion = sales.groupBy { it.first }
val totals = byRegion.mapValues { entry -> entry.value.sumOf { it.second } }
println(totals) // {north=150, south=80}
```
`"north" to 120`은 `Pair`를 만듭니다. 여기서 바깥 람다는 맵의 엔트리를 다루고, 안쪽 람다는 그 엔트리의 리스트에 있는 페어들을 다룹니다.

---

`Map`은 엔트리의 리스트처럼 다룰 수 있습니다. `filter`와 `map`은 맵에 바로 동작하며 `.key`와 `.value`를 가진 각 엔트리를 받습니다. 맵에 대한 `filter`는 맵을 반환하고, `map`은 리스트를 반환합니다. `sortedBy` 같은 정렬 메서드는 맵에 정의되어 있지 않으므로, 엔트리들의 컬렉션인 `scores.entries`를 먼저 거치세요:
```kotlin
val scores = mapOf("Ann" to 90, "Bob" to 72)
println(scores.filter { it.value > 80 })              // {Ann=90}
println(scores.entries.sortedBy { it.value }.map { it.key }) // [Bob, Ann]
```
`scores.entries`는 모든 엔트리의 집합이고, `scores.keys`와 `scores.values`는 한쪽만 줍니다.
