`Set`은 서로 다른 여러 정보를 하나의 변수 이름 아래에 순서대로 저장할 수 있는 데이터 타입입니다.
`List`와의 주요 차이점은 `Set`은 각 값의 요소를 하나만 허용한다는 것입니다.

`List`와 마찬가지로 `Set`은 하나 또는 여러 타입의 값을 저장하며 **인덱스**를 사용하여 이러한 값을 구분합니다.
다음과 같은 형식의 표현식으로 set에 항목을 할당할 수 있습니다:
```kotlin
val setName = setOf<itemsType>(item1, item2)
```
`itemsType`은 set 내부 항목의 타입을 나타내며, 예를 들어 `Int`, `String`, `Any` 등이 될 수 있습니다.

---

`Set`은 특정 순서가 없는 __고유한__ 항목의 컬렉션입니다.

```kotlin
val numbers = setOf(1, 1, 2) // [1]
println(numbers)
// prints [1, 2]
```

__[1]__에서 숫자 __1__이 두 번 포함된 set을 생성하려고 하지만, 보시다시피 각 요소는 고유해야 하며 두 번째 __1__은 자동으로 제거됩니다.

---

Kotlin에는 두 가지 종류의 `Set`이 있습니다:

- `Set`은 생성 후 수정할 수 없습니다.
- `MutableSet`은 생성 후 수정할 수 있으며, 요소를 추가, 제거 또는 업데이트할 수 있습니다.

```kotlin
val numbers = setOf(1, 2, 3)
numbers.add(4) // [1]
```
__[1]__은 `Set`이 _읽기 전용_이기 때문에 오류를 발생시킵니다.

수정 가능한 set을 생성하려면 `mutableSetOf` 키워드를 사용합니다
```kotlin
val numbers = mutableSetOf(1, 2, 3)
numbers.add(4)
println(numbers)
// prints [1, 2, 3, 4]
```

---

`Set`의 가장 일반적인 활용은 `in` 또는 `contains()`를 사용하여 멤버십을 테스트하는 것입니다

```kotlin
val numbers = setOf(1, 2, 3)
println(2 in numbers) // prints true
println(numbers.contains(5)) // prints false
```

위에서 볼 수 있듯이 `in`과 `contains`는 전달된 요소가 set에 존재하는지 여부를 나타내는 `Bool`을 반환합니다

---

`Set`에서 요소의 순서는 중요하지 않습니다.
실제로 동일한 요소를 가지지만 다른 순서를 가진 두 개의 `Set`을 비교하면 동일하다는 결과를 얻습니다.

---

`Set`에서는 합집합, 교집합, 차집합, 부분집합 확인과 같은 여러 연산을 수행할 수 있습니다.

```kotlin
val firstNumbers = setOf(1, 2, 3)
val lastNumbers = setOf(3, 4, 5)
val union = firstNumbers.union(lastNumbers) // [1, 2, 3, 4, 5]
val intersection = firstNumbers intersect lastNumbers // [3]
val difference = firstNumbers subtract lastNumbers // [1, 2]
val subset = firstNumbers.containsAll(lastNumbers) // false
```

---

`Set`을 `List`로 변환하려면 `toList()` 함수를 사용할 수 있습니다
