**맵**은 **키-값 쌍**의 컬렉션입니다: 각 값은 고유한 키 아래에 저장되고, 그 키를 사용해 값을 다시 찾을 수 있습니다. 맵은 `{}` 리터럴 구문으로 만들며, 각 쌍을 `key: value` 형태로 작성합니다:

```dart
Map<String, int> ages = {'Ann': 30, 'Bob': 25};
print(ages); // {Ann: 30, Bob: 25}
```

타입 어노테이션 `Map<String, int>`는 모든 키가 `String`이고 모든 값이 `int`라고 Dart에 알립니다. 리스트와 마찬가지로, `var`는 리터럴로부터 타입을 추론합니다:

```dart
var capitals = {'Italy': 'Rome', 'France': 'Paris'};
```

---

값을 읽으려면 리스트의 인덱스와 마찬가지로 대괄호 안에 키를 사용합니다:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages['Ann']); // 30
```

키가 맵에 없으면 조회는 에러를 발생시키지 **않고** `null`을 반환합니다. 이런 이유로 `ages['Ann']`의 타입은 `int`가 아니라 `int?`(널이 될 수 있는 `int`)입니다:

```dart
print(ages['Zed']); // null
```

---

`map[key] = value`로 대입하면, 키가 아직 맵에 없을 때는 새 쌍을 **추가**하고, 이미 존재하는 키라면 그 값을 **업데이트**합니다:

```dart
var ages = {'Ann': 30};
ages['Bob'] = 25; // adds Bob
ages['Ann'] = 31; // updates Ann
print(ages); // {Ann: 31, Bob: 25}
```

새 키는 기존 키 뒤에 추가되므로, 맵은 삽입 순서를 기억합니다.

---

`.remove(key)` 메서드는 맵에서 키와 그 값을 삭제합니다. 삭제된 값을 반환하며, 키가 없었다면 `null`을 반환합니다:

```dart
var ages = {'Ann': 30, 'Bob': 25};
int? removed = ages.remove('Ann');
print(removed); // 30
print(ages); // {Bob: 25}
```

`.length` 속성은 키-값 쌍의 개수를 반환합니다:

```dart
print(ages.length); // 1
```

---

맵이 특정 키를 가지고 있는지 확인하려면 `.containsKey(key)`를 사용합니다. 특정 값을 가진 쌍이 있는지 확인하려면 `.containsValue(value)`를 사용합니다. 둘 다 `bool`을 반환합니다:

```dart
var ages = {'Ann': 30, 'Bob': 25};
print(ages.containsKey('Ann')); // true
print(ages.containsKey('Zed')); // false
print(ages.containsValue(25)); // true
```

---

존재하지 않는 키를 읽어도 절대 에러가 발생하지 않으므로, 조회 결과가 `null`일 수 있다는 점을 항상 고려하세요. 안전한 패턴은 `??` 연산자로 대체 값을 제공하는 것입니다:

```dart
var ages = {'Ann': 30};
int age = ages['Zed'] ?? 0;
print(age); // 0
```

---

`.keys` 속성은 맵의 모든 키를, `.values`는 모든 값을 삽입 순서대로 제공합니다. 둘 다 지연 평가되는 `Iterable`이므로, 실제 `List`가 필요하면 `.toList()`를 호출하세요:

```dart
var ages = {'Ann': 30, 'Bob': 25};
List<String> names = ages.keys.toList();
List<int> years = ages.values.toList();
print(names); // [Ann, Bob]
print(years); // [30, 25]
```
