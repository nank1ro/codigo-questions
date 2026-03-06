**객체(Objects)**는 배열과 유사하지만, 인덱스 대신 *키(key)*를 사용하여 값에 접근합니다.
키는 문자열이나 숫자가 될 수 있습니다.
객체는 다음과 같이 중괄호로 감싸서 표현합니다:
```javascript
var objectName = {"key1": 1, "key2": 2, "key3": 3};
```
이것은 세 개의 *키-값 쌍*을 가진 `objectName`이라는 딕셔너리입니다.
키 `key1`은 값 `1`을 가리키고, `key2`는 `2`를 가리키는 식입니다.

---

키를 사용하여 딕셔너리 값에 접근하는 것은 인덱스를 사용하여 배열 값에 접근하는 것과 같습니다:
```javascript
// user 딕셔너리에서 age 값을 가져옵니다
user['age'];
```

---

배열과 마찬가지로, 딕셔너리는 _변경 가능(mutable)_ 합니다.
이는 생성된 후에도 변경할 수 있다는 것을 의미합니다 (상수로 선언되지 않은 경우).
이것의 장점 중 하나는 다음과 같이 딕셔너리가 생성된 후에 새로운 _키/값 쌍_을 추가할 수 있다는 것입니다:
```javascript
dictName[newKeyName] = newValue;
```

---

딕셔너리 변수는 변경 가능하기 때문에 다양한 방법으로 변경할 수 있습니다.
'delete' 키워드를 사용하여 딕셔너리에서 항목을 제거할 수 있습니다:
```javascript
delete dictName[keyName];
```
이렇게 하면 딕셔너리에서 키 `keyName`과 해당 값이 제거됩니다.

---

딕셔너리의 모든 키를 나열하려면 어떻게 해야 할까요?
`Object.keys()` 메서드를 사용하면 됩니다.

---

딕셔너리의 모든 값을 나열하려면 어떻게 해야 할까요?
`Object.values()` 메서드를 사용하면 됩니다.

---

배열과 마찬가지로, `Object.entries()` 메서드를 사용하여 딕셔너리 요소를 반복할 수 있습니다.
```javascript
var user = {"first_name": "John", "last_name": "Hood", "age": 30};
for (const [key, value] of Object.entries(user)) {
    console.log(`${key}: ${value}`);
}
```
