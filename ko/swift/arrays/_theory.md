배열은 여러 개의 서로 다른 정보를 하나의 변수 이름 아래에 순서가 있는 컬렉션으로 저장할 수 있는 데이터 타입입니다.
배열은 하나 또는 여러 타입의 값을 저장하며, **인덱스**를 사용하여 이러한 값을 구별합니다.
다음과 같은 형식의 표현식으로 배열에 항목을 할당할 수 있습니다:
```swift
var arrayName: [itemsType] = [item1, item2]
```
`itemsType`은 배열 내부 항목의 타입을 나타내며, 예를 들어 `Int`, `String`, `Any` 등이 될 수 있습니다.

---

배열의 개별 항목에 인덱스를 사용하여 접근할 수 있습니다.
인덱스는 배열에서 항목의 위치를 식별하는 주소와 같습니다.
인덱스는 배열 이름 바로 뒤에 대괄호 안에 다음과 같이 나타납니다:
```swift
arrayName[index]
```

배열 인덱스는 `1`이 아니라 `0`부터 시작합니다! 배열의 첫 번째 항목에 다음과 같이 접근합니다: `arrayName[0]`.
배열의 두 번째 항목은 인덱스 1에 있습니다: `arrayName[1]`.

---

배열 인덱스는 다른 변수 이름과 같은 역할을 합니다.
값을 접근하거나 할당하는 데 사용할 수 있습니다.
다음과 같이 배열 인덱스에 접근하는 방법을 살펴보았습니다:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// "Jeremiah" 값을 출력합니다
print(names[0])
```
값을 할당하는 방법은 다음과 같습니다:
```swift
var names = ["Jeremiah", "Barney", "Ivan", "Noel"]
// 새로운 값 "Jordan"을 할당합니다
names[0] = "Jordan"
// "Jordan" 값을 출력합니다
print(names[0])
```

---

문자열과 마찬가지로, 배열에도 **길이** `count`가 있습니다.
배열의 길이는 배열에 포함된 항목의 수입니다

---

배열은 고정된 길이를 가질 필요가 없습니다.
언제든지 배열의 끝에 항목을 추가할 수 있습니다!
배열에 항목을 추가하려면 `append` 함수를 사용합니다:
```swift
var letters = ["a", "b"]
letters.append("c")
print(letters)
// ["a", "b", "c"]를 출력합니다
```

---

때때로 배열의 일부분만 접근하고 싶을 수 있습니다.
다음 코드를 살펴보세요:
```swift
let numbers = [1, 2, 3, 4]
let slice = numbers[1...2]
print(slice)
// [2, 3]을 출력합니다
```
먼저 `numbers`라는 배열을 생성합니다.
그런 다음 배열의 일부분을 가져와 slice 배열에 저장합니다.
배열 이름 뒤에 포함할 인덱스를 정의하여 이를 수행합니다: `numbers[1...2]`.
Swift에서는 `...`를 사용하여 마지막 인덱스를 포함할 수 있지만, `..<`를 사용하여 마지막 인덱스를 제외할 수도 있습니다

---

Swift에서는 원하는 대로 배열을 슬라이스할 수 있습니다!
```swift
// 처음 두 항목을 가져옵니다
listName[..<2]
// 네 번째부터 마지막 항목까지 가져옵니다
listName[3...]
```
배열 슬라이스에 맨 처음 또는 맨 마지막 항목이 포함되는 경우, 해당 항목의 인덱스를 포함할 필요가 없습니다

---

`Any` 타입을 지정하면 배열 요소는 어떤 타입이든 될 수 있습니다:
```swift
var arrayName: [Any] = ["one", 2, true]
```
실제로 위에는 순서대로 문자열, 정수, 불리언이 있습니다.
또한 배열 안에 배열을 넣을 수도 있습니다!

---

때때로 배열에서 항목을 검색해야 할 때가 있습니다.
Swift에서는 `firstIndex()` 메서드를 사용할 수 있습니다:
```swift
var names: [String] = ["Trevor", "Zac", "Glenn"]
if let index = names.firstIndex(of: "Zac") {
  print(index)
}
// 1을 출력합니다
```
위 코드는 `"Zac"` 문자열이 포함된 첫 번째 인덱스, 이 경우 `1`을 출력합니다.
`insert()` 메서드를 사용하여 배열의 특정 인덱스에 항목을 삽입할 수도 있습니다:
```swift
names.insert("Ali", at: 1)
// ["Trevor", "Ali", "Zac", "Glenn"]을 출력합니다
```
위 코드는 인덱스 `1`에 `"Ali"`를 삽입하며, 이 인덱스 이후의 모든 항목이 1칸씩 뒤로 이동합니다

---

Swift에서는 `for..in` 키워드를 사용하여 매우 간단하게 배열을 반복할 수 있습니다:
```swift
var numbers = [1, 2, 3]
for num in numbers {
    print(num)
}
// 1, 2, 3을 출력합니다
```
`for` 키워드 뒤에 변수 이름이 오며, 이 변수에 각 배열 항목의 값이 차례로 할당됩니다.

---

**튜플**은 배열과 비슷하지만 요소에 이름을 지정하고 그 이름으로 참조할 수 있습니다.
튜플을 생성하려면 소괄호 `()`를 사용합니다
```swift
var person = (firstName: "John", lastName: "Smith")
var firstName = person.firstName // John
var lastName = person.lastName // Smith
```
