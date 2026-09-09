**고차 함수**는 다른 함수를 인수로 받거나 함수를 반환하거나 둘 다 하는 함수입니다. 여러분은 이미 `map`, `filter`, `reduce`와 `sorted(by:)`를 만났습니다: 이들은 클로저를 받아 컬렉션의 요소에 적용합니다. Swift에는 이 외에도 많은 고차 함수가 있으며, 이를 알면 긴 반복문을 읽기 쉬운 한 줄로 바꿀 수 있습니다.
`compactMap`은 `map`과 같이 작동하지만, 클로저가 옵셔널을 반환하고 `nil`인 결과는 버려집니다:
```swift
let words = ["3", "seven", "12"]
let numbers = words.compactMap { Int($0) }
print(numbers) // [3, 12]
```
`Int("seven")`은 `nil`이므로 그 요소는 사라지고, 결과는 `[Int?]`가 아니라 `[Int]`가 됩니다.

---

`flatMap`은 **배열**을 반환하는 클로저를 위한 것입니다: 배열의 배열을 만드는 대신, 반환된 모든 배열을 하나의 평평한 결과로 합칩니다:
```swift
let teams = [["Ann", "Bob"], ["Cid"]]
print(teams.map { $0 })     // [["Ann", "Bob"], ["Cid"]]
print(teams.flatMap { $0 }) // ["Ann", "Bob", "Cid"]
```
클로저는 평탄화되기 전에 각 내부 배열을 변환할 수도 있습니다. 예를 들어 `teams.flatMap { $0.reversed() }`는 `["Bob", "Ann", "Cid"]`를 반환합니다.

---

세 가지 `map` 변형은 클로저가 반환하는 것에서만 차이가 있습니다:
- `map`: 모든 값, 요소당 하나의 결과
- `compactMap`: 옵셔널, `nil`인 결과는 버려집니다
- `flatMap`: 배열, 모든 결과가 하나의 배열로 합쳐집니다

`flatMap`에 전달된 클로저는 내부 배열에 대해 `map`을 호출할 수 있으므로, 하나의 변환을 다른 변환 안에 중첩할 수 있습니다:
```swift
let matrix = [[1, 2], [3]]
print(matrix.flatMap { row in row.map { $0 + 1 } }) // [2, 3, 4]
```

---

`reduce`는 매 단계마다 새로운 누적 값을 만들며, 결과가 배열이나 딕셔너리일 때는 낭비가 됩니다. `reduce(into:)`는 클로저에 누적 값을 `inout` 매개변수로 전달하므로, `return` 없이 제자리에서 수정할 수 있습니다:
```swift
let words = ["a", "b", "a"]
let counts = words.reduce(into: [String: Int]()) { result, word in
    result[word, default: 0] += 1
}
print(counts["a"]!) // 2
```
`[String: Int]()`는 빈 딕셔너리를 만들고, `result[word, default: 0]`는 현재 개수를 읽거나 키가 없을 때 `0`을 읽습니다.

---

일부 고차 함수는 컬렉션을 변환하는 대신 컬렉션에 대한 질문에 답합니다. 이들은 모두 `Bool`을 반환하는 클로저를 받습니다:
- `first(where:)`는 클로저를 만족하는 첫 번째 요소를 반환하고, 없으면 `nil`을 반환합니다
- `contains(where:)`는 최소 한 개의 요소가 클로저를 만족하면 `true`를 반환합니다
- `allSatisfy`는 모든 요소가 클로저를 만족하면 `true`를 반환합니다

```swift
let nums = [4, 9, 16]
print(nums.first(where: { $0 > 5 }))  // Optional(9)
print(nums.contains(where: { $0 > 5 })) // true
print(nums.allSatisfy { $0 > 5 })       // false
```
`filter`와 달리 `first(where:)`는 첫 번째 일치에서 멈추고 새 배열을 만들지 않습니다.

---

`contains(where:)`와 `allSatisfy`는 플래그 변수를 사용하는 반복문의 흔한 패턴을 대체합니다. 두 함수 모두 답을 알 수 있게 되는 즉시 멈춥니다: `contains(where:)`는 첫 번째 일치에서, `allSatisfy`는 클로저를 만족하지 않는 첫 번째 요소에서 멈춥니다.
```swift
let ages = [15, 22, 40]
let anyMinor = ages.contains { $0 < 18 }  // true
let allAdults = ages.allSatisfy { $0 >= 18 } // false
```
`contains { ... }`는 `contains(where:)`의 후행 클로저 형태이며, 특정 값을 찾는 `contains(_:)`와 혼동해서는 안 됩니다.

---

고차 함수는 직접 만든 구조체의 배열을 포함하여 어떤 배열에도 사용할 수 있습니다. `filter`를 적용한 뒤 `map`을 이어서 사용하는 것은 일부 요소를 선택하고 각 요소에서 값을 추출하는 일반적인 방법입니다:
```swift
struct Book {
    var title: String
    var pages: Int
}
let books = [Book(title: "Dune", pages: 412), Book(title: "Haiku", pages: 40)]
let long = books.filter { $0.pages > 100 }.map { $0.title }
print(long) // ["Dune"]
```
반대 순서로, 즉 `map`을 먼저 하고 `filter`를 나중에 하면 검사가 사용하기 전에 `pages` 프로퍼티가 사라져 버립니다.

---

클로저가 하나의 프로퍼티만 읽을 때는 대신 **키 경로**를 전달할 수 있습니다: `\.name`은 "요소의 `name` 프로퍼티"를 뜻하며, `map(\.name)`은 `map { $0.name }`과 같습니다.
프로퍼티로 정렬할 때는 일반적인 두 인자 클로저를 사용하여 두 요소에서 그 프로퍼티를 비교합니다:
```swift
struct City {
    var name: String
    var population: Int
}
let cities = [City(name: "Oslo", population: 700), City(name: "Rome", population: 2800)]
let byPopulation = cities.sorted { $0.population > $1.population }
print(byPopulation.map(\.name)) // ["Rome", "Oslo"]
```

---

**여러 기준**으로 정렬하려면 첫 번째 프로퍼티를 비교하고, 첫 번째 값들이 같을 때만 두 번째 프로퍼티로 넘어갑니다:
```swift
let sorted = people.sorted {
    if $0.age != $1.age {
        return $0.age < $1.age
    }
    return $0.name < $1.name
}
```
여기서 사람들은 나이순으로 정렬되고, 나이가 같은 사람들은 이름순으로 정렬됩니다. 클로저는 첫 번째 요소가 두 번째 요소보다 앞에 와야 할 때만 `true`를 반환해야 하므로, 같은 경우에는 다음 비교로 넘어갑니다.

---

`enumerated()`는 배열을 `(offset, element)` 쌍의 시퀀스로 바꾸므로, 클로저는 각 요소의 값과 함께 그 위치를 사용할 수 있습니다:
```swift
let steps = ["mix", "bake"]
let numbered = steps.enumerated().map { pair in
    "\(pair.offset + 1). \(pair.element)"
}
print(numbered) // ["1. mix", "2. bake"]
```
각 쌍은 튜플이므로, 클로저는 이를 분해할 수도 있습니다: `.map { (i, step) in "\(i + 1). \(step)" }`.

---

`zip`은 두 시퀀스의 요소를 위치별로 짝지어 튜플의 시퀀스를 만듭니다. 더 짧은 쪽이 끝나면 멈춥니다:
```swift
let names = ["Ann", "Bob"]
let ages = [31, 27, 99]
let pairs = zip(names, ages).map { "\($0) is \($1)" }
print(pairs) // ["Ann is 31", "Bob is 27"]
```
클로저 안에서 `$0`은 첫 번째 시퀀스의 요소이고 `$1`은 두 번째 시퀀스의 요소입니다. `zip`은 메서드가 아니라 자유 함수입니다: `a.zip(b)`가 아니라 `zip(a, b)`라고 씁니다.

---

`forEach`는 `for-in` 반복문의 고차 함수 쌍둥이입니다: 각 요소마다 클로저를 순서대로 한 번씩 호출합니다. 차이는 반복을 빠져나가는 방식에 있습니다. `for-in`에서는 `break`로 빠져나가거나 `continue`할 수 있지만, `forEach` 클로저 안에서는 `break`와 `continue`가 허용되지 않고, `return`은 클로저의 **현재 호출**만 끝낸 뒤 다음 요소가 평소처럼 처리됩니다:
```swift
[1, 2, 3].forEach { n in
    if n == 2 { return }
    print(n)
}
// prints 1 and 3
```
모든 요소에 짧은 부수 효과를 적용할 때는 `forEach`를, 조기에 멈춰야 할 때는 `for-in`을 사용하세요.

---

`Dictionary(grouping:by:)`는 컬렉션을 배열들의 딕셔너리로 나눕니다. 클로저는 각 요소의 **키**를 계산하고, 같은 키를 가진 모든 요소는 같은 배열에 들어갑니다:
```swift
let words = ["apple", "bee", "avocado"]
let byInitial = Dictionary(grouping: words, by: { $0.first! })
print(byInitial["a"]!) // ["apple", "avocado"]
```
`mapValues`는 키는 그대로 두면서 딕셔너리의 모든 값을 변환하므로, 그룹화 다음의 자연스러운 다음 단계입니다:
```swift
let sizes = byInitial.mapValues { $0.count }
print(sizes["a"]!) // 2
```

---

`prefix(while:)`은 클로저가 `true`를 반환하는 **동안** 처음부터 요소를 가져가다가, 클로저를 만족하지 않는 첫 번째 요소에서 멈춥니다. 뒤의 요소들이 다시 통과하더라도 마찬가지입니다. `drop(while:)`은 그 보완입니다: 같은 시작 구간을 건너뛰고 나머지 모든 것을 반환합니다:
```swift
let temps = [12, 15, 21, 14]
print(temps.prefix { $0 < 20 }) // [12, 15]
print(temps.drop { $0 < 20 })   // [21, 14]
```
둘 다 `ArraySlice`를 반환하는데, 이것은 원본 배열에 대한 뷰로, 배열처럼 출력되며 `Array(...)`로 배열로 바꿀 수 있습니다.

---

고차 함수를 직접 작성할 수도 있습니다. 클로저를 받아 그것으로 만든 **새 클로저를 반환**하는 함수는 흔한 패턴입니다: 반환된 클로저는 원래 클로저를 캡처하므로, 매개변수에는 `@escaping`을 표시해야 합니다.
예를 들어 `negate`는 술어를 그 반대로 바꾸어 `filter`에 전달할 수 있게 해 줍니다:
```swift
func negate(_ predicate: @escaping (Int) -> Bool) -> (Int) -> Bool {
    return { !predicate($0) }
}
let isEven: (Int) -> Bool = { $0 % 2 == 0 }
print([1, 2, 3, 4].filter(negate(isEven))) // [1, 3]
```
`filter(negate(isEven))`는 후행 클로저 문법 없이 클로저를 일반 인수로 전달한다는 점에 유의하세요.

---

배열에 대한 `map`과 `filter`는 **즉시 평가**됩니다: 각각은 다음 단계가 실행되기 전에 배열 전체를 처리하고 새 배열을 만듭니다. 큰 컬렉션을 다루거나 첫 번째 결과만 필요할 때는 이것이 낭비입니다.
`lazy` 프로퍼티는 요소가 실제로 요청될 때만 연산이 실행되는 뷰를 반환하며, 전체 체인을 통해 한 번에 한 요소씩 처리합니다:
```swift
let firstBig = (1...1000).lazy.map { $0 * $0 }.first { $0 > 50 }
print(firstBig!) // 64
```
여기서는 `1, 2, ..., 8`만 제곱됩니다: `first(where:)`는 조건을 만족하는 요소를 찾을 때까지 요소를 요구하고, 체인은 거기서 멈춥니다. `lazy`가 없다면 `map`이 먼저 1000개의 숫자를 모두 제곱할 것입니다.
