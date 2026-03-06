배열은 여러 가지 정보를 하나의 변수 이름 아래에 순서대로 저장할 수 있는 데이터 타입입니다.
배열은 하나 또는 여러 타입의 값을 저장하며, **인덱스**를 사용하여 이러한 값들을 구분합니다.
다음과 같은 형식의 표현식으로 배열에 항목을 할당할 수 있습니다:
```javascript
var arrayName = [item1, item2];
```

---

배열의 개별 항목에 인덱스를 사용하여 접근할 수 있습니다.
인덱스는 배열에서 항목의 위치를 식별하는 주소와 같습니다.
인덱스는 배열 이름 바로 뒤에 대괄호 안에 다음과 같이 표시됩니다:
```javascript
arrayName[index];
```
배열 인덱스는 `1`이 아닌 `0`부터 시작합니다! 배열의 첫 번째 항목에는 다음과 같이 접근합니다: `arrayName[0]`.
배열의 두 번째 항목은 인덱스 1에 있습니다: `arrayName[1]`.

---

배열 인덱스는 다른 변수 이름과 동일하게 동작합니다.
인덱스를 사용하여 값에 접근하거나 값을 할당할 수 있습니다.
배열 인덱스에 접근하는 방법은 다음과 같습니다:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Prints the value "Jeremiah"
console.log(names[0]);
```
값을 할당하는 방법은 다음과 같습니다:
```javascript
var names = ["Jeremiah", "Barney", "Ivan", "Noel"];
// Assign the new value "Jordan"
names[0] = "Jordan";
// Prints the value "Jordan"
console.log(names[0]);
```

---

문자열과 마찬가지로, 배열에도 **길이**가 있습니다.
배열의 길이는 배열에 포함된 항목의 수입니다

---

배열은 고정된 길이를 가질 필요가 없습니다.
언제든지 배열의 끝에 항목을 추가할 수 있습니다!
배열에 항목을 추가하려면 `push` 함수를 사용합니다:
```javascript
var letters = ["a", "b"];
letters.push("c");
console.log(letters);
// Prints ["a", "b", "c"]
```

---

때때로 배열의 일부분에만 접근하고 싶을 때가 있습니다.
다음 코드를 살펴보세요:
```javascript
let numbers = [1, 2, 3, 4];
let slice = numbers.slice(1, 3);
console.log(slice);
// prints [2, 3]
```
먼저 `numbers`라는 배열을 생성합니다.
그런 다음 배열의 일부를 가져와 slice 배열에 저장합니다.
배열 이름 뒤에 원하는 인덱스를 정의하여 이를 수행합니다: `numbers.slice(1, 3)`.
오른쪽 인덱스는 포함되지 않는다는 점을 기억하세요

---

JavaScript에서는 배열을 원하는 대로 슬라이스할 수 있습니다!
```javascript
// Grabs the first two items
listName.slice(0, 2);
// Grabs the fourth through last items
listName.slice(3);
```
배열 슬라이스에 배열의 맨 처음 또는 맨 마지막 항목이 포함되는 경우, 해당 항목의 인덱스를 포함할 필요가 없습니다

---

배열 요소는 어떤 타입이든 될 수 있습니다.
```javascript
var arrayName = ["one", 2, true];
```
실제로 위 코드에는 순서대로 문자열, 정수, 불리언이 있습니다.
하지만 배열 안에 배열을 넣을 수도 있습니다!

---

때때로 배열에서 항목을 검색해야 할 때가 있습니다.
JavaScript에서는 `indexOf()` 메서드를 사용할 수 있습니다:
```javascript
var names = ["Trevor", "Zac", "Glenn"];
console.log(names.indexOf('Zac'));
// prints 1
```
위 코드는 문자열 `"Zac"`을 포함하는 첫 번째 인덱스인 `1`을 출력합니다.
`splice()` 메서드를 사용하여 특정 인덱스에 항목을 삽입할 수도 있습니다:
```javascript
names.splice(1, 0, "Ali");
// prints ["Trevor", "Ali", "Zac", "Glenn"]
```
위 코드는 인덱스 `1`에 `"Ali"`를 삽입하며, 이 인덱스 이후의 모든 항목을 1칸씩 뒤로 이동시킵니다.
두 번째 값 `0`은 _삭제 개수_를 의미하며, 이 경우 배열에서 어떤 항목도 삭제하지 않습니다. 하지만 `1`을 지정했다면 `Zac` 값이 배열에서 제거되었을 것입니다

---

JavaScript에서는 `for..of` 키워드를 사용하여 매우 간단하게 배열을 반복할 수 있습니다:
```javascript
var numbers = [1, 2, 3];
for (num of numbers) {
    console.log(num);
}
// prints 1, 2, 3 
```
`for` 키워드 뒤에 변수 이름이 오며, 이 변수에는 각 배열 항목의 값이 차례로 할당됩니다.
