Dart에서 **리스트**는 항목의 순서 있는 컬렉션입니다. 리스트를 만드는 가장 간단한 방법은 `[]` 리터럴 구문입니다:

```dart
List<int> numbers = [1, 2, 3];
```

`var`을 사용한 타입 추론도 사용할 수 있습니다:

```dart
var fruits = ['apple', 'banana', 'cherry'];
```

타입 어노테이션 `List<String>`은 리스트의 모든 요소가 `String`이어야 한다고 Dart에 알립니다.

---

Dart의 리스트는 **0부터 인덱싱**됩니다. 즉, 첫 번째 요소는 인덱스 `0`, 두 번째는 인덱스 `1` 등으로 되어 있습니다.

```dart
var colors = ['red', 'green', 'blue'];
print(colors[0]); // red
print(colors[2]); // blue
```

인덱스로 요소에 접근하는 것은 `list[index]` 구문으로 합니다.

---

`.add()` 메서드는 리스트의 **끝**에 하나의 요소를 추가합니다:

```dart
var nums = [1, 2, 3];
nums.add(4);
print(nums); // [1, 2, 3, 4]
```

`.add()`는 리스트를 **제자리에서** 수정하고 `void`를 반환한다는 점에 유의하세요.

---

`.length` 속성은 리스트의 요소 수를 반환합니다:

```dart
var scores = [95, 87, 72, 100];
print(scores.length); // 4
```

빈 리스트의 길이는 `0`입니다:

```dart
var empty = [];
print(empty.length); // 0
```

---

`.contains()` 메서드는 리스트에 특정 값이 포함되어 있는지 확인합니다. 발견되면 `true`, 그렇지 않으면 `false`를 반환합니다:

```dart
var fruits = ['apple', 'mango', 'grape'];
print(fruits.contains('mango'));  // true
print(fruits.contains('orange')); // false
```

이것은 반복문 없이 포함 여부를 확인하는 데 유용합니다.
