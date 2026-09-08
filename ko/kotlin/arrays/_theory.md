**배열**은 같은 타입의 값을 정해진 개수만큼 하나의 변수 이름 아래에 저장합니다.
`arrayOf`로 배열을 생성하고, 대괄호와 `0`부터 시작하는 **인덱스**로 요소를 읽으며, `size`로 요소의 개수를 얻습니다:
```kotlin
val colors = arrayOf("red", "green", "blue")
println(colors[0])   // red
println(colors.size) // 3
```
마지막 요소는 인덱스 `size - 1`에 있습니다.

---

`arrayOf(1, 2, 3)`은 각 요소가 박싱된 객체인 `Array<Int>`를 생성합니다.
기본 타입을 위해 Kotlin은 `IntArray`, `DoubleArray`, `BooleanArray`와 같은 전용의 더 효율적인 타입을 제공합니다:
```kotlin
val a = intArrayOf(1, 2, 3)   // IntArray
val b = doubleArrayOf(1.5, 2.5) // DoubleArray
```
각 인덱스를 받는 **init** 람다로 정해진 크기의 배열을 만들거나, 0으로 채워진 `IntArray`를 만들 수도 있습니다:
```kotlin
val doubles = Array(3) { i -> i * 2 } // [0, 2, 4]
val zeros = IntArray(3)               // [0, 0, 0]
val evens = IntArray(4) { it * 2 }    // [0, 2, 4, 6]
```

---

모든 배열에는 인덱스를 다루기 위한 두 가지 유용한 속성이 있습니다:
- `indices`는 `0`부터 마지막 인덱스까지, 유효한 인덱스의 범위입니다
- `lastIndex`는 마지막 요소의 인덱스, 즉 `size - 1`입니다
```kotlin
val letters = arrayOf("x", "y")
println(letters.lastIndex) // 1
for (i in letters.indices) {
    println(letters[i])
}
// prints x, then y
```

---

배열이 `val`로 선언되어 있어도, 인덱스에 값을 대입하여 **요소**를 교체할 수 있습니다:
```kotlin
val nums = intArrayOf(1, 2, 3)
nums[0] = 10 // nums is now [10, 2, 3]
```
모든 요소를 순회하려면 `for` 루프나 `forEach`를 사용할 수 있습니다:
```kotlin
for (n in nums) {
    println(n)
}
nums.forEach { println(it) }
```
`n`과 `it`은 값의 읽기 전용 복사본이므로 재대입할 수 없으며, 요소를 수정하려면 인덱스가 필요하다는 점에 유의하세요.

---

배열이 어떤 값을 가지고 있는지 확인하려면 `in`이나 `contains`를 사용하며, 둘 다 `Boolean`을 반환합니다.
`indexOf`는 처음 발견된 위치의 인덱스를 반환하고, 값이 없으면 `-1`을 반환합니다:
```kotlin
val nums = intArrayOf(4, 8, 15)
println(8 in nums)          // true
println(nums.contains(3))   // false
println(nums.indexOf(15))   // 2
println(nums.indexOf(16))   // -1
```

---

배열을 그대로 출력하면 요소가 표시되지 않고 `[Ljava.lang.String;@1b6d3586`와 같은 것이 출력됩니다.
읽기 쉬운 문자열을 만들려면 `joinToString`을 사용하고, 필요하다면 구분자를 지정할 수 있습니다(기본값은 `", "`입니다). 대괄호로 감싼 요소를 얻으려면 `contentToString`을 사용합니다:
```kotlin
val nums = intArrayOf(1, 2, 3)
println(nums.joinToString())      // 1, 2, 3
println(nums.joinToString("-"))   // 1-2-3
println(nums.contentToString())   // [1, 2, 3]
```

---

배열은 **제자리에서** 정렬하거나, 새로 정렬된 컬렉션으로 복사할 수 있습니다:
- `sort()`와 `sortDescending()`은 배열 자체를 재정렬하며 아무것도 반환하지 않습니다
- `reverse()`는 배열 자체의 순서를 뒤집습니다
- `sorted()`, `sortedDescending()`, `reversed()`는 배열을 그대로 두고 새로운 `List`를 반환합니다
```kotlin
val nums = intArrayOf(3, 1, 2)
nums.sort()                 // nums is now [1, 2, 3]
println(nums.reversed())    // [3, 2, 1], nums is still [1, 2, 3]
```

---

숫자 배열에는 집계 함수가 함께 제공됩니다:
```kotlin
val nums = intArrayOf(3, 9, 1)
println(nums.sum())     // 13
println(nums.max())     // 9
println(nums.min())     // 1
println(nums.average()) // 4.333333333333333
println(nums.count())   // 3
```
`max()`와 `min()`은 빈 배열에서 예외를 던지므로, 배열이 비어 있을 수 있다면 `maxOrNull()`과 `minOrNull()`을 사용하세요.

---

배열과 `MutableList`의 주요 차이점은 배열이 **고정된 크기**를 갖는다는 것입니다: 한 번 생성하면 요소를 교체할 수는 있지만 추가하거나 제거할 수는 없으며, `add` 함수도 없습니다.
`nums + 4`와 같은 표현식은 `nums`를 늘리는 것이 아니라 완전히 새로운 배열을 만듭니다:
```kotlin
val nums = arrayOf(1, 2, 3)
nums[0] = 9              // ok, nums is [9, 2, 3]
val bigger = nums + 4    // new array [9, 2, 3, 4], nums still has 3 elements
```
요소의 개수가 시간에 따라 바뀐다면 `MutableList`를, 개수를 미리 알고 있거나 기본 타입 성능이 필요하다면 배열을 선호하세요.

---

배열은 리스트와 동일한 변환 함수를 지원합니다. `filter`는 조건에 맞는 요소를 남기고, `map`은 모든 요소를 변환합니다.
둘 다 배열이 아니라 새로운 `List`를 반환합니다:
```kotlin
val nums = intArrayOf(1, 2, 3)
val odds = nums.filter { it % 2 == 1 } // List [1, 3]
val tripled = nums.map { it * 3 }      // List [3, 6, 9]
println(tripled)                       // [3, 6, 9]
```
결과가 리스트이므로, 그대로 출력하면 요소가 표시됩니다.

---

루프를 도는 동안 인덱스와 값이 모두 필요할 때는 `withIndex()`로 각 쌍을 구조 분해하거나 `forEachIndexed`를 사용하세요:
```kotlin
val pets = arrayOf("cat", "dog")
for ((i, pet) in pets.withIndex()) {
    println("$i -> $pet")
}
pets.forEachIndexed { i, pet -> println("$i -> $pet") }
// both print 0 -> cat, then 1 -> dog
```

---

배열과 리스트는 서로 쉽게 변환됩니다:
- `toList()`와 `toMutableList()`는 배열을 리스트로 복사합니다
- `toTypedArray()`는 리스트를 `Array<T>`로 복사합니다
- `toIntArray()`는 `Int` 리스트를 `IntArray`로 복사합니다
```kotlin
val arr = arrayOf("a", "b")
val list = arr.toMutableList() // MutableList [a, b]
list.add("c")
val back = list.toTypedArray() // Array [a, b, c]
val nums = listOf(1, 2).toIntArray() // IntArray [1, 2]
```
모든 변환은 **복사본**을 만들기 때문에, 결과를 변경해도 원본에는 영향이 없습니다.

---

리스트와 달리, 같은 요소를 가진 두 배열은 `==`로 비교했을 때 **같지 않습니다**: 배열은 참조로 비교되므로, `==`가 `true`가 되는 것은 완전히 동일한 배열 객체일 때뿐입니다.
내용을 비교하려면 `contentEquals`를 사용하세요:
```kotlin
val a = intArrayOf(1, 2, 3)
val b = intArrayOf(1, 2, 3)
println(a == b)              // false
println(a.contentEquals(b))  // true
println(listOf(1, 2) == listOf(1, 2)) // true, lists compare their elements
```

---

배열은 크기가 고정되어 있으므로, 일부를 가져오려면 새로운 배열을 만들어야 합니다:
- `copyOf()`는 배열 전체를 복사하고, `copyOf(n)`은 처음 `n`개의 요소를 복사합니다
- `copyOfRange(from, to)`는 인덱스 `from`부터 `to` **직전까지**의 요소를 복사합니다
- `sliceArray(range)`는 범위의 양 끝을 포함한 인덱스의 요소를 복사합니다
```kotlin
val nums = intArrayOf(10, 20, 30, 40)
println(nums.copyOfRange(1, 3).contentToString()) // [20, 30]
println(nums.sliceArray(0..1).contentToString())  // [10, 20]
```
