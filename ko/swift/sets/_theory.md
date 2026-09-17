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
numbers.insert(2) // 2는 이미 있음: 아무것도 바뀌지 않음
numbers.remove(1) // {2, 3}
numbers.remove(9) // 9는 없음: 아무것도 바뀌지 않음
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
    print(number) // 1, 2, 3이 각각 다른 줄에
}
```

---

set은 집합론의 고전적인 연산을 지원합니다. 각 연산은 **새로운** set을 반환하며 원본은 변경되지 않습니다:
- `a.union(b)`(합집합)는 `a`, `b`, 또는 둘 다에 있는 모든 요소를 포함합니다
- `a.intersection(b)`(교집합)는 `a`와 `b` **둘 다**에 있는 요소만 포함합니다
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.union(b).sorted())        // [1, 2, 3, 4]
print(a.intersection(b).sorted()) // [3]
```

---

두 가지 연산이 더해지면 이 계열이 완성됩니다:
- `a.subtracting(b)`(차집합)는 `a`의 요소 중 `b`에 **없는** 것들을 포함합니다
- `a.symmetricDifference(b)`(대칭차)는 `a` 또는 `b`에는 있지만 **둘 다에는 없는** 요소를 포함합니다
```swift
let a: Set<Int> = [1, 2, 3]
let b: Set<Int> = [3, 4]
print(a.subtracting(b).sorted())          // [1, 2]
print(a.symmetricDifference(b).sorted())  // [1, 2, 4]
```
`union`이나 `intersection`과 달리, `subtracting`은 대칭적이지 않습니다: `a.subtracting(b)`와 `b.subtracting(a)`는 대체로 다릅니다.

---

set끼리 서로 비교할 수도 있습니다. 이 메서드들은 `Bool`을 반환합니다:
- `a.isSubset(of: b)`(부분집합)는 `a`의 모든 요소가 `b`에도 있을 때 `true`입니다
- `a.isSuperset(of: b)`(상위집합)는 `a`가 `b`의 모든 요소를 포함할 때 `true`입니다
- `a.isDisjoint(with: b)`(서로소)는 `a`와 `b`에 공통 요소가 없을 때 `true`입니다
```swift
let small: Set<Int> = [1, 2]
let big: Set<Int> = [1, 2, 3]
print(small.isSubset(of: big))   // true
print(big.isSuperset(of: small)) // true
print(small.isDisjoint(with: big)) // false
```

---

set과 배열은 서로 쉽게 변환할 수 있습니다.
배열을 `Set(...)`에 전달하면 그 요소들로 set이 만들어지며, 이는 **중복을 제거**하는 가장 빠른 방법입니다:
```swift
let votes = [3, 1, 3, 2, 1]
let unique = Set(votes) // {1, 2, 3} in some order
```
set을 `Array(...)`에 전달하면 배열이 반환되지만, set에는 순서가 없으므로 요소가 예측할 수 없는 순서로 나옵니다.
그래서 순서가 있는 결과가 필요할 때는 보통 set에 `sorted()`를 대신 호출합니다. 이 메서드는 이미 배열을 반환합니다:
```swift
let ordered = unique.sorted() // [1, 2, 3]
```
