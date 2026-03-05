**딕셔너리**는 배열이나 튜플과 비슷하지만, 인덱스 대신 *키*를 사용하여 값에 접근합니다.
키는 문자열이나 숫자가 될 수 있습니다.
딕셔너리는 대괄호로 감싸며, 다음과 같이 작성합니다:
```swift
var dictionaryName: [String: Int] = ["key1": 1, "key2": 2, "key3": 3]
```
이것은 세 개의 *키-값 쌍*을 가진 `dictionaryName`이라는 딕셔너리입니다.
키 `key1`은 값 `1`을 가리키고, `key2`는 `2`를 가리키며, 나머지도 마찬가지입니다.

---

키를 사용하여 딕셔너리 값에 접근하는 것은 인덱스로 배열 값에 접근하는 것과 같습니다:
```swift
// gets the age value from the user dictionary
user['age']
```

---

배열과 마찬가지로, 딕셔너리는 _변경 가능(mutable)_ 합니다.
이는 딕셔너리가 생성된 후에도 변경할 수 있다는 의미입니다 (상수로 선언되지 않은 경우).
이 장점 중 하나는 딕셔너리가 생성된 후에도 새로운 _키/값 쌍_ 을 추가할 수 있다는 것입니다:
```swift
dictName[newKeyName] = newValue
```

---

딕셔너리의 길이 `count`는 딕셔너리가 가진 _키-값 쌍_ 의 개수입니다.
각 쌍은 값이 배열이더라도 한 번만 셉니다. (맞습니다: 딕셔너리 안에 배열을 넣을 수도 있습니다!)

---

딕셔너리는 변경 가능하므로, 다양한 방법으로 변경할 수 있습니다. `removeValue(forKey:)` 메서드를 사용하여 딕셔너리에서 항목을 제거할 수 있습니다:
```swift
if let removedValue = dictName.removeValue(forKey: "keyName") {
    print("The removed value is \(removedValue).") // prints the removed value, if the key exists
}
```
이 코드는 딕셔너리에서 키 `keyName`과 그에 연결된 값을 제거합니다.

---

딕셔너리의 모든 키를 나열하고 싶다면 어떻게 해야 할까요?
`keys` 속성을 사용하면 됩니다.

---

딕셔너리의 모든 값을 나열하고 싶다면 어떻게 해야 할까요?
`values` 속성을 사용하면 됩니다.

---

배열과 마찬가지로, `for..in` 키워드를 사용하여 딕셔너리 요소를 반복할 수 있습니다.
반복문에서 키와 값을 모두 얻으려면 별도의 속성을 지정할 필요가 없습니다:
```swift
for (key, value) in dictName {
    print("\(key): \(value)")
}
```

---

배열에서 사용했던 `isEmpty` 속성을 사용하여 딕셔너리가 비어 있는지 확인할 수도 있습니다

---

딕셔너리에 값을 __추가__하거나 __변경__하기 위해 `updateValue(_:forKey:)` 메서드를 사용할 수도 있습니다

---

이전에 `removeValue()` 메서드를 사용하여 딕셔너리에서 _키-값 쌍_ 을 제거하는 방법을 배웠습니다.
키에 `nil` 값을 할당하여 요소를 제거할 수도 있습니다
```swift
dictName[keyName] = nil
// keyName has been removed from the dictionary dictName
```
