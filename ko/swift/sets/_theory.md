**Set**는 동일한 타입의 값을 정해진 순서 없이 저장하는 컬렉션이며, 가장 중요한 점은 **중복을 허용하지 않는다**는 것입니다: 각 값은 최대 한 번만 나타납니다.
Set은 값이 *몇 번* 등장하는지, *어느 위치*에 있는지가 아니라 *어떤* 값이 존재하는지만 중요할 때 가장 적합합니다.
Set은 `Set<Element>` 타입과 배열 형태의 리터럴로 선언합니다:
```swift
let numbers: Set<Int> = [1, 2, 3]
```
이 타입 어노테이션은 필수입니다. 없으면 Swift는 배열을 생성합니다.
리터럴에 같은 값이 여러 번 포함되어 있어도, set은 사본을 하나만 보관합니다:
```swift
let rolls: Set<Int> = [6, 6, 6]
print(rolls.count) // 1
```
`count` 속성은 set이 보관하는 고유한 값의 개수를 알려줍니다.

---

배열과 마찬가지로 set도 상수(`let`)나 변수(`var`)가 될 수 있습니다. 생성된 이후에 변경할 수 있는 것은 `var`로 선언한 set뿐입니다.
빈 set을 만들려면 타입의 이니셜라이저를 호출해야 합니다. 빈 리터럴 `[]`만으로는 Swift에게 어떤 요소 타입을 사용할지 알려줄 수 없기 때문입니다:
```swift
var visited = Set<String>()
print(visited.isEmpty) // true
```
`isEmpty` 속성은 배열과 마찬가지로 set에 요소가 없을 때 `true`가 됩니다.

---

set은 같은 값을 절대 두 번 저장하지 않으므로, `count`는 리터럴에 각 값이 몇 번 적혀 있든 상관없이 *고유한* 값의 개수입니다.

---

값이 set에 있는지 확인하려면 `Bool`을 반환하는 `contains(_:)` 메서드를 사용합니다:
```swift
let primes: Set<Int> = [2, 3, 5, 7]
print(primes.contains(5)) // true
print(primes.contains(6)) // false
```
이 확인은 요소가 수천 개라도 set에서는 매우 빠릅니다. 이것이 멤버십 확인 시 배열보다 set을 선호하는 주된 이유 중 하나입니다.

---

`var` set은 `insert(_:)`와 `remove(_:)`로 수정할 수 있습니다:
```swift
var numbers: Set<Int> = [1, 2]
numbers.insert(3) // {1, 2, 3}
numbers.insert(2) // 2 is already there: nothing changes
numbers.remove(1) // {2, 3}
numbers.remove(9) // 9 is not there: nothing changes
```
이미 존재하는 값을 삽입해도 아무 효과가 없고, 존재하지 않는 값을 제거해도 오류가 발생하지 않습니다.
`remove(_:)`는 제거된 값을 옵셔널로 반환합니다(아무것도 제거되지 않았다면 `nil`). 이를 통해 실제로 제거가 일어났는지 확인할 수 있습니다.
set을 완전히 비우려면 `removeAll()`을 호출하세요.

---

`for`-`in`으로 set을 순회할 수 있지만, set에는 **정해진 순서가 없다**는 점을 기억하세요: 요소는 어떤 순서로든 나올 수 있고, 그 순서는 실행할 때마다 바뀔 수 있습니다.
순서가 중요할 때는 먼저 `sorted()`를 호출하세요: 이는 set은 그대로 둔 채, 요소를 오름차순으로 정렬한 새로운 **배열**을 반환합니다.
```swift
let numbers: Set<Int> = [3, 1, 2]
for number in numbers.sorted() {
    print(number) // 1, 2, 3 on separate lines
}
```
