리스트는 여러 가지 정보를 하나의 변수 이름 아래에 순서대로 저장할 수 있는 데이터 타입입니다.
리스트는 하나 또는 여러 타입의 값을 저장하며, **인덱스**를 사용하여 이러한 값을 구분합니다.
다음과 같은 형식의 표현식으로 리스트에 항목을 할당할 수 있습니다:
```kotlin
val listName = listOf<itemsType>(item1, item2)
```
`itemsType`은 리스트 내부 항목의 타입을 나타내며, 예를 들어 `Int`, `String`, `Any` 등이 될 수 있습니다.

---

리스트는 특정 순서를 가진 항목들의 컬렉션입니다. Kotlin에는 두 가지 유형의 리스트가 있습니다:

- `List`는 생성 후 수정할 수 없습니다.
- `MutableList`는 생성 후 수정할 수 있으며, 요소를 추가, 제거 또는 업데이트할 수 있습니다.

```kotlin
val numbers = listOf(1, 3, 5)
numbers.add(7) // [1]
```
__[1]__ `List`는 _읽기 전용_이므로 오류가 발생합니다.

수정 가능한 리스트를 생성하려면 `mutableListOf` 키워드를 사용합니다
```kotlin
val numbers = mutableListOf(1, 3, 5)
numbers.add(7)
println(numbers)
// prints [1, 3, 5, 7]
```

---

인덱스를 사용하여 리스트의 개별 항목에 접근할 수 있습니다.
인덱스는 리스트에서 항목의 위치를 식별하는 주소와 같습니다.
인덱스는 리스트 이름 바로 뒤에 대괄호 안에 다음과 같이 표시됩니다:
```kotlin
listName[index]
```

리스트의 인덱스는 `1`이 **아닌** `0`부터 시작합니다! 리스트의 첫 번째 항목에는 다음과 같이 접근합니다: `listName[0]` 또는 `listName.get(0)` 또는 `listName.first()`.
리스트의 두 번째 항목은 인덱스 __1__에 있습니다: `listName[1]`.

---

인덱스는 실제로 첫 번째 요소로부터의 오프셋입니다. 예를 들어, `list[2]`라고 하면 리스트의 두 번째 요소를 요청하는 것이 아니라, 첫 번째 요소에서 2 위치만큼 떨어진 요소를 요청하는 것입니다. 따라서 `list[0]`은 첫 번째 요소(오프셋 0), `list[1]`은 두 번째 요소(오프셋 1), `list[2]`는 세 번째 요소(오프셋 2)이며, 이런 식으로 계속됩니다.

리스트 인덱스는 값에 접근할 때뿐만 아니라 값을 할당할 때도 사용할 수 있습니다.
다음과 같이 리스트 인덱스에 접근하는 방법을 보셨습니다:
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel"]
// Prints the value "Jeremiah"
println(names[0])
```
다음은 값을 할당하는 방법입니다:
```kotlin
val names = mutableListOf("Jeremiah", "Barney", "Ivan", "Noel")
// Assign the new value "Jordan"
names[0] = "Jordan"
// Prints the value "Jordan"
println(names[0])
```

---

문자열과 마찬가지로, 리스트도 `size` 게터를 사용하여 **길이**를 가져올 수 있습니다.
리스트의 길이는 리스트에 포함된 항목의 수입니다

---

또 다른 유용한 리스트 연산은 주어진 요소가 리스트에 있는지 확인하는 `contains` 메서드입니다.
예를 들어, 이름 리스트가 있다면 `contains` 메서드를 사용하여 특정 이름이 리스트에 있는지 확인할 수 있습니다.
```kotlin
val names = listOf("Thomas", "Donald", "Scarlett")
println(names.contains("Scarlett"))
// prints true
```

---

가변 리스트는 고정된 길이를 가질 필요가 없습니다.
언제든지 리스트의 끝에 항목을 추가할 수 있습니다!
가변 리스트에 항목을 추가하려면 `add` 함수 또는 `+=` 단축키를 사용합니다:
```kotlin
val letters = mutableListOf("a", "b")
letters.add("c")
println(letters)
// prints [a, b, c]
```

---

이전 예제에서 보았듯이, `add` 함수를 사용하여 항목을 하나씩 추가할 수 있습니다.
하지만 다른 리스트의 모든 요소를 한 번에 추가해야 한다면 `addAll` 함수 또는 `+=` 단축키를 사용하면 됩니다:
```kotlin
val letters = mutableListOf("a", "b")
val newLetters = listOf("c", "d", "e")
letters.addAll(newLetters)
println(letters)
// prints [a, b, c, d, e]
```

---

때로는 리스트의 일부분만 접근하고 싶을 때가 있습니다.
다음 코드를 살펴보세요:
```kotlin
val numbers = listOf(1, 2, 3, 4) // [1]
val slice = numbers.slice(1..2) // [2]
println(slice)
// prints [2, 3]
```
__[1]__: 먼저 `numbers`라는 _읽기 전용_ 리스트를 생성합니다.
__[2]__: 그런 다음 `slice` 함수를 사용하여 리스트의 부분을 가져와 slice 리스트에 저장합니다.
`slice` 함수 안에 포함할 인덱스를 정의하여 이 작업을 수행합니다.

Kotlin에서는 `..`을 사용하여 마지막 인덱스를 포함할 수 있지만, `until`을 사용하여 마지막 인덱스를 제외할 수도 있습니다

---

`Any` 타입을 지정하면 리스트의 요소는 어떤 타입이든 될 수 있습니다:
```kotlin
var listName: List<Any> = listOf("one", 2, true)
```
실제로 위에는 순서대로 `String`, `Integer`, `Boolean`이 있습니다.
또한 리스트 안에 리스트를 넣을 수도 있습니다!

---

때로는 리스트에서 항목을 검색해야 할 때가 있습니다.
Kotlin에서는 `indexOfFirst` 메서드를 사용할 수 있습니다:
```kotlin
val names = mutableListOf("Trevor", "Zac", "Glenn")
println(names.indexOfFirst { it == "Zac"})
// prints 1
```

`indexOfFirst` 메서드는 리스트의 각 항목에 대해 true가 될 때까지 평가되는 __술어__ 함수를 받아, 해당 요소의 _인덱스_를 반환합니다.
위 코드는 문자열 `"Zac"`을 포함하는 첫 번째 인덱스인 `1`을 출력합니다.

`add(index, element)` 메서드를 사용하여 수정 가능한 리스트의 특정 인덱스에 항목을 삽입할 수도 있습니다:
```kotlin
names.add(1, "Ali")
// prints [Trevor, Ali, Zac, Glenn]
```
위 코드는 인덱스 `1`에 `"Ali"`를 삽입하며, 이 인덱스 이후의 모든 항목은 1만큼 뒤로 이동합니다

---

Kotlin에서는 `for..in` 키워드를 사용하여 매우 간단하게 리스트를 반복할 수 있습니다:
```kotlin
val numbers = listOf(1, 2, 3)
for (num in numbers) {
    println(num)
}
// prints 1, 2, 3
```
`for` 키워드 뒤에 변수 이름이 오며, 이 변수에는 각 리스트 항목의 값이 차례로 할당됩니다.
